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

    def send_msg(self):
        self.usr.api.sendMessage(self.target, text) #TODO: Get variable within method from other class

class App:

    def __init__(self):

        def attempt_login():
            usr_name = usr_login.get()
            password = psswd.get()
            if None in (usr_name, password) or usr_name == "Username" or psswd == "Password":
                return 1

            try:
                self.usr = api.User(usr_name, password)
                self.root.quit()
                self.homepage()

            except ValueError:
                psswd.delete(0, "end")

        def clear_entry(event):
            try:
                self.usr_name_cleared

            except AttributeError:
                event.widget.delete(0, "end")
                self.usr_name_cleared = True

        def clear_entry_psswd(event):
            try:
                self.psswd_cleared
                event.widget.config(show="*")

            except AttributeError:
                event.widget.delete(0, "end")
                self.psswd_cleared = True
                event.widget.config(show="*")

            event.widget.config(show="*")

        self.root = tk.Tk()
        self.root.title("WINstagram - Login")
        self.root.geometry(newGeometry=("500x500"))
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.update()

        usr_login = tk.Entry()
        usr_login.insert(0, "Username")
        usr_login.bind("<Button-1>", clear_entry)
        usr_login.bind("<Key>", clear_entry)
        usr_login.place(relx=.5, rely=.475, anchor="center")

        psswd = tk.Entry()
        psswd.insert(0, "Password")
        psswd.bind("<Button-1>", clear_entry_psswd)
        psswd.bind("<Key>", clear_entry_psswd)
        psswd.place(relx=.5, rely=.525, anchor="center")

        login = tk.Button()
        login["text"] = "Login"
        login.bind("<Button-1>",
                    lambda event: attempt_login())
        login.bind("<Key>",
                    lambda event: attempt_login())
        login.place(relx=.5, rely=.5815, anchor="center")

        #Styling
        font = ("Helvetica", 13)
        self.root.configure(background="#000")
        usr_login.configure(
                            background="#222",
                            fg="#ddd",
                            bd=0,
                            font=font)
        psswd.configure(background="#222",
                        fg="#ddd",
                        bd=0,
                        font=font)
        login.configure(background="#222",
                        fg="#ddd",
                        bd=0,
                        font=font)


        #Binding for login
        self.root.bind("<Return>",
                  lambda event: attempt_login())

        self.root.mainloop()

    def get_chats(self):
        return self.usr.api.getMessages()

    def homepage(self):
        # TODO: Get list of chats, pfps, and last message, and display neatly
        # TOOD: Use each chat as a button that calls convo_run()
        pass

    def convo_run(self, target):

        def get_msg():
            return msg_in.get()

        self.target = target

        chat = Chat(self.usr, target)

        self.root.bind("<Return>", lambda msg=get_msg(): chat.send_msg(msg)) #TODO: Find some way of calling send_msg with these arguments

        msg_in = tk.Entry()
        msg_in.pack(side="bottom", fill="x")
        msg_in.focus_set()

        self.root.mainloop()

        #TODO: get msgs, update position when new received, show back/targetusr/info in top, quit on back

def main():
    app = App()

if __name__ == "__main__":
    main()