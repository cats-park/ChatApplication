#!/usr/bin/env python3

import tkinter as tk


class MyWindow:
    root_window: tk.Tk
    edit_box: tk.Entry
    frame2: tk.Frame
    
    MAX_LEN = 10
    
    _username:str
    _send_message_queue = []
    
    def __init__(self, name:str):
        print('__init__')
        self.username = name
    
    @property
    def username(self):
        print('Called username\'s getter')
        return self._username
    
    @username.setter
    def username(self, username):
        print('Called username\'s setter')
        self._username = username
        
    @property
    def send_message_queue(self):
        return self._send_message_queue
        
    def create_window(self, width:int, height:int):
        """ウインドウを作成する
        """
        # Tkクラス生成
        self.root_window = tk.Tk()
        # 画面サイズ
        self.root_window.geometry('{}x{}'.format(width, height))
        # 画面タイトル
        self.root_window.title('サンプル画面')
        # frame1の設定
        frame1 = tk.Frame(self.root_window, pady='30')
        # エントリー
        self.edit_box = tk.Entry(frame1, width='20')
        self.edit_box.grid()
        # 投稿ボタン
        send_btn = tk.Button(frame1, text='投稿する', command=self.send_message)
        send_btn.grid()
        frame1.pack()
        # frame2の設定
        self.frame2 = tk.Frame(self.root_window, width=400,height=300, padx=30, bg='#fff')
        self.frame2.pack()
        # frame3の設定
        frame3 = tk.Frame(self.root_window, pady=30)
        # クリアボタン
        clear_btn = tk.Button(frame3, text='クリア', command=self.clear_content)
        clear_btn.grid()
        frame3.pack()
    
    def display_window(self):
        """ウインドウを表示する
        """
        try:
            self.root_window.mainloop()
        except NameError as e:
            print(e)

    def add_text(self, name:str, message:str, position='left'):
        """テキストを表示する

        Args:
            name (str): 名前
            message (str): メッセージ
            position (str): 位置(right or left)
        """

        # 表示数がMAX_LENの場合、表示しない
        display_len = len(self.frame2.winfo_children())
        if display_len == self.MAX_LEN:
            return
        
        # 表示するテキストを作成
        if position == 'right':
            txt = '{} : {}'.format(message, name)
            anchor = 'e'
        elif position == 'left':
            txt = '{} : {}'.format(name, message)
            anchor = 'w'
        else:
            print('ERROR: Invalid value')
        # ラベルを作成しframe2に追加する
        l = tk.Label(self.frame2, text=txt, width=30, bg='#fff', anchor=anchor)
        l.grid()
        
    def send_message(self):
        """入力されたメッセージを取得し、キューに追加する
        """
        # メッセージを取得する
        m = self.edit_box.get()
        # 未入力の場合は以降の処理をせずに終了する
        if m == '':
            return
        # メッセージをキューに追加する
        self._send_message_queue.append(m)
        # 自分のメッセージを表示させる
        self.add_text(self._username, m, 'right')
        # エントリーのテキストを削除する
        self.clear_edit_box()

    def clear_edit_box(self):
        """エントリーのテキスト削除
        """
        self.edit_box.delete(0, tk.END)

    def clear_content(self):
        """frame2内のコンテンツを消す
        """
        children = self.frame2.winfo_children()
        for child in children:
            child.destroy()

    def get_queue_len(self):
        """キューのサイズを返す

        Returns:
            int: キューのサイズ
        """
        return len(self._send_message_queue)

