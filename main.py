#!/usr/bin/env python3

import threading
import tkinter as tk

import api

class Chat:

    def __init__(self, app, threadId):
        self.usr = app.usr
        self.threadId = threadId
        self.app = app
        self.last_msgs = None #Last message you read - Used for highlighting

    def get_msgs(self):
        msgs = self.usr.getMessages(threadId)
        if msgs != self.last_msgs:
            new_msgs = self.last_msgs
            for msg in msgs:
                if msg not in self.last_msgs:
                    new_msgs.append(msg)

            self.pending_msgs = new_msgs
            self.last_msgs = self.last_msgs + new_msgs

    def send_msg(self):
        self.usr.api.sendMessage(self.target, text) #TODO: Get variable within method from other class

class App:

    def __init__(self):

        def attempt_login():
            root.title("WinstagramDM - Logging in")
            usr_name = usr_login.get()
            password = psswd.get()
            #disable editing while logging in
            usr_login.config(state="disabled")
            psswd.config(state="disabled")
            login.config(state="disabled")

            try:
                self.usr = api.User(usr_name, password)
                root.destroy()
                self.logged_in = True

            except ValueError:
                psswd.delete(0, "end")

            if not self.logged_in:
                usr_login.config(state="normal")
                psswd.config(state="normal")
                login.config(state="normal")
                psswd.delete(0, "end")
                root.title("WinstagramDM - Login")
                #Resetup login thread to allow rerun
                self.login_thread = threading.Thread(target=attempt_login)
                return 1

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
        root.title("WinstagramDM - Login")
        root.wm_iconbitmap('icon.ico')
        root.geometry(newGeometry=("500x500")) #Sizing
        root.minsize(500, 500)
        root.maxsize(500, 500)
        root.update()

        #Setup attempt_login thread
        self.login_thread = threading.Thread(target=attempt_login)
        self.logged_in = False

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
                    lambda event: self.login_thread.start())
        login.bind("<Key>",
                    lambda event: self.login_thread.start())
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
                  lambda event: self.login_thread.start())

        root.mainloop()
        self.homepage()

    def homepage(self):

        def get_chats():
            return self.usr.getChats()

        root = tk.Tk()
        root.title("WinstagramDM - Homepage")
        root.wm_iconbitmap('icon.ico')
        root.geometry(newGeometry=("500x500")) #Sizing
        root.minsize(500, 500)
        root.update()

        #setup messages
        for chat in get_chats():
            chat_button = tk.Button(
                root,
                compound=tk.LEFT,
                image=None, #TODO: Read image from url
                text=chat["thread_name"],
                command=lambda: self.convo_run(chat["thread_id"]))

            chat_button.pack(fill=tk.X)

        root.mainloop()

        #TODO: get chats/imgs as buttons in scrollable list

    def convo_run(self, threadId):

        def get_msg_entry(): #Used for getting from entry
            return msg_in.get()

        def update_msgs():
            #TODO: Update msgs
            root.after(500, update_msgs())

        root = tk.Tk()

        chat = Chat(self, threadId)

        msg_in = tk.Entry()
        msg_in.pack(side="bottom", fill="x")
        msg_in.focus_set()

        #Thread setup
        get_msg_thread = threading.Thread(target=chat.get_msgs())
        get_msg_thread.start()

        #Bindings
        root.bind("<Return>", lambda msg=get_msg_entry(): chat.send_msg_entry(msg))

        root.after(500, update_msgs)
        root.mainloop()

        #TODO: get msgs, update position when new received, show back/targetusr/info in top, quit on back

def main():
    app = App()

if __name__ == "__main__":
    main()