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
                root.destroy()

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

        root = tk.Tk()
        root.title("WINstagram - Login")
        root.geometry(newGeometry=("500x500"))
        root.minsize(500, 500)
        root.maxsize(500, 500)
        root.update()

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
        root.configure(background="#000")
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
        root.bind("<Return>",
                  lambda event: attempt_login())

        root.mainloop()
        self.homepage()

    def homepage(self):

        def get_chats(self):
            return self.usr.api.getChats()

        #TODO: get chats/imgs as buttons in scrollable list

    def convo_run(self, target):

        root = tk.Tk()

        def get_msg_entry(): #Used for getting from entry
            return msg_in.get()

        def get_msgs(): #USed for getting messages in chat
            self.usr.api.getMessages()

        self.target = target

        chat = Chat(self.usr, target)

        msg_in = tk.Entry()
        msg_in.pack(side="bottom", fill="x")
        msg_in.focus_set()

        #Send msg binding
        root.bind("<Return>", lambda msg=get_msg_entry(): chat.send_msg_entry(msg))
        root.mainloop()

        #TODO: get msgs, update position when new received, show back/targetusr/info in top, quit on back

def main():
    app = App()

if __name__ == "__main__":
    main()