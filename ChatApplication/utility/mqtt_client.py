#!/usr/bin/env python3

import paho.mqtt.client as mqtt

class MqttClient:
    # Init
    def __init__(self):
        # MQTTの接続設定
        self.mqtt_client = mqtt.Client()
        # 接続時のコールバック関数の登録
        self.mqtt_client.on_connect = self.on_connect
        # 切断時のコールバックを登録
        self.mqtt_client.on_disconnect = self.on_disconnect
        # メッセージ受信時のコールバック関数の登録
        self.mqtt_client.on_message = self.on_message
        # メッセージ送信時のコールバック関数の登録
        self.mqtt_client.on_publish = self.on_publish

    def connect(self, host:str = '127.0.0.1', port:int = 1883, keep_alive:int = 60):
        print('Mqtt connect')
        self.mqtt_client.connect(host, port, keep_alive)

    def start_loop_forever(self):
        print('start loop_forever')
        # NOTE: 現在の処理の流れの中でループする
        self.mqtt_client.loop_forever()

    def start_loop_start(self):
        print('start loop_start')
        # NOTE: 新しいスレッドでループする
        self.mqtt_client.loop_start()

    def add_subdcribe_topic(self, topic):
        print('Add subscribe topic: {}'.format(topic))
        self.mqtt_client.subscribe(topic)

    def publish(self, topic, message):
        self.mqtt_client.publish(topic, message)

    def on_connect(self, client, userdata, flag, rc):
        print("Connected with result code " + str(rc))

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")
            self.mqtt_client.loop_stop()

    # メッセージが届いたときの処理
    def on_message(self, client, userdata, msg):
        # msg.topicにトピック名が，msg.payloadに届いたデータ本体が入っている
        # print("Received message '" + str(msg.payload) +
        #       "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))
        pass

    def on_publish(self, client, userdata, mid):
        # do nothing
        pass

pass