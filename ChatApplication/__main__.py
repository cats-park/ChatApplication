#!/usr/bin/env python3
import json
import sys

import threading
import time

import config

from mymqttclient import MyMqttClient
from mywindow import MyWindow

MAX_LEN = 10
username:str

mqtt_client:MyMqttClient = None
my_window:MyWindow = None


def queue_monitoring():
    global mqtt_client, my_window, username
    mqtt_queue_len = 0
    send_queue_len = 0
    while True:
        if mqtt_client is None or my_window is None:
            return
        mlen = mqtt_client.get_queue_len()
        slen = my_window.get_queue_len()
        # mqtt queue
        if mqtt_queue_len < mlen:
            # queueのサイズが増加した
            m_list = mqtt_client.receive_message_queue
            for i in range(mqtt_queue_len, mlen):
                name = m_list[i]['name']
                message = m_list[i]['message']
                # 自分のメッセージは表示しない
                if name != username:
                    my_window.add_text(name, message)
            mqtt_queue_len = mlen
        # send queue
        if send_queue_len < slen:
            # queueのサイズが増加した
            s_list = my_window.send_message_queue
            for i in range(send_queue_len, slen):
                message = s_list[i]
                mqtt_client.send_chat(username, message)
            send_queue_len = slen
        time.sleep(0.5)

def main(): 
    global mqtt_client, my_window, username
    # 引数の名前をセットする
    args = sys.argv
    username = args[1]
    # MQTTクライアントの設定をし、subscribeを開始する
    mqtt_client = MyMqttClient()
    mqtt_client.connect(host=config.broker_address)
    mqtt_client.add_subdcribe_topic('/chat')
    mqtt_client.start_loop_start()
    
    # ウインドウを作成する
    my_window = MyWindow(username)
    my_window.create_window(400, 300)
    
    # キューを監視するメソッドをスレッド実行
    thread1 = threading.Thread(target=queue_monitoring)
    thread1.start()

    # ウインドウを表示する
    my_window.display_window()

if __name__ == '__main__':
    main()
