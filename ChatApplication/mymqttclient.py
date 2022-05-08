#!/usr/bin/env python3
import json
from utility.mqtt_client import MqttClient

class MyMqttClient(MqttClient):
    TOPIC_CHAT:str = '/chat'
    
    _receive_message_queue = []
        
    @property
    def receive_message_queue(self):
        """getter

        Returns:
            list: _receive_message_queue
        """
        return self._receive_message_queue
    
    def on_message(self, client, userdata, msg):
        """subscribe時に呼ばれる関数

        Args:
            client (_type_): _description_
            userdata (_type_): _description_
            msg (_type_): _description_
        """
        message = msg.payload
        topic = msg.topic

        if topic == self.TOPIC_CHAT:
            self.receive_chat(message)

    def receive_chat(self, m: str):
        """topicが"/chat"で受信したメッセージを処理する

        Args:
            message (str): 受信メッセージ
        """
        # 受信メッセージをdict型に変換し、名前とメッセージを取り出す
        try:
            json_message = json.loads(m)
        except (json.JSONDecodeError, KeyError) as e:
            print(e)

        # メッセージをキューに追加する
        self._receive_message_queue.append(json_message)
    
    def send_chat(self, username:str, message:str):
        """ユーザー名とメッセージから送信メッセージを作成し、トピック/chatでpublishする

        Args:
            username (str): ユーザー名
            message (str): 送信メッセージ
        """
        d = {'name': username, 'message': message}
        self.publish(self.TOPIC_CHAT, json.dumps(d))
        
    def get_queue_len(self):
        return len(self._receive_message_queue)
