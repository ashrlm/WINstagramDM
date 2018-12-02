#!/usr/bin/env python3

import tkinter as tk

import api

class Chat:

    def __init__(self, usr, target):
        self.usr = usr
        self.target = target
        self.prev_msg = None #Last message you read - Used for highlighting

    def get_msgs(self, target):
        pass #TODO: get msgs

    def send_msg(self, text):
        pass #TODO: Send msg

class App:

    def login(self):
        # TODO: login
        pass

    def get_chats(self):
        pass

    def homepage(self):
        # TODO: Get list of chats, pfps, and last message, and display neatly
        # TOOD: Use each chat as a button that calls convo_run()
        pass

    def convo_run(self, target):

        root = tk.Tk()

        root.bind("<Return>", send_msg) #TODO: Find some way of calling send_msg with these arguments

        msg_in = tk.Entry()
        msg_in.pack(side="bottom", fill="x")
        msg_in.focus_set()

        root.mainloop()

        #TODO: get msgs, update position when new received, show back/targetusr/info in top, quit on back

def main():
    app = App()
    app.login()
    app.homepage()

if __name__ == "__main__":
    main()