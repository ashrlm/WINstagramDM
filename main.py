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
        self.usr.api.sendMessage(self.target, text)

class App:

    def __init__(self):

        def attempt_login():
            usr_name = usr_login.get()
            password = psswd.get()
            if None in (usr_name, password) or usr_name == "Username" or psswd == "Password":
                return 1

            try:
                self.usr = api.User(usr_name, password)
                print(3)
                quit()
                root.destroy()
                App.homepage()

            except ValueError:
                print(2)
                return 1

        def clear_entry(event):
            event.widget.delete(0, "end")

        def clear_entry_psswd(event):
            clear_entry(event)
            event.widget.config(show="*")

        root = tk.Tk()

        usr_login = tk.Entry()
        usr_login.insert(0, "Username")
        usr_login.bind("<Button-1>", clear_entry)
        usr_login.grid(row=0, column=0)

        psswd = tk.Entry()
        psswd.insert(0, "Password")
        psswd.bind("<Button-1>", clear_entry_psswd)
        psswd.grid(column=1, row=0)

        #Error in below - Entry.get returning default value
        root.bind("<Return>",
                  lambda event: attempt_login())

        root.mainloop()

    def get_chats(self):
        pass

    def homepage(self):
        # TODO: Get list of chats, pfps, and last message, and display neatly
        # TOOD: Use each chat as a button that calls convo_run()
        pass

    def convo_run(self, target):

        root = tk.Tk()
        chat = Chat(self.usr, target)

        root.bind("<Return>", chat.send_msg) #TODO: Find some way of calling send_msg with these arguments

        msg_in = tk.Entry()
        msg_in.pack(side="bottom", fill="x")
        msg_in.focus_set()

        root.mainloop()

        #TODO: get msgs, update position when new received, show back/targetusr/info in top, quit on back

def main():
    app = App()

if __name__ == "__main__":
    main()