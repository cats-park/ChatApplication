# MQTTチャットアプリ

## 概要

- MQTT通信を用いてメッセージのやりとりを行う
- tkinterを用いてウインドウを作成し、受信したメッセージを表示する

## 実行手順

1. config.pyのbroker_addressを設定する
2. 実行する

    ```bash
    # usernameは適宜入力する
    $ python ChatApplication {username}
    ```

## 完成イメージ

![完成イメージ](gif/イメージ.gif)

## MQTT情報

- トピック
  - /chat
- メッセージフォーマット

  ```json
  {
      "name": "name",
      "message": "message"
  }
  ```

## 作成手順

1. mosquittoをインストールする
2. mqtt brokerとmqtt clientが使用できるようにする
3. mosquitto_sub,mosquitto_pubコマンドを使ってMQTT通信できることを確認する
4. 実装する
5. 動作確認をする
