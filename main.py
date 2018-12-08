#!/usr/bin/env python3

import threading
import sys
import tkinter as tk
import requests
from io import BytesIO

from PIL import Image, ImageTk, ImageOps, ImageDraw

import api

class Chat:

    def __init__(self, app, entry, threadId, users):
        self.usr = app.usr
        self.entry = entry
        self.threadId = threadId
        self.users = users
        self.app = app
        self.last_msgs = [] #Last message you read - Used for more efficient loading

    def get_msgs(self):
        msgs = self.usr.getMessages(self.threadId)
        if msgs != self.last_msgs:
            new_msgs = self.last_msgs
            for msg in msgs:
                if msg not in self.last_msgs:
                    new_msgs.append(msg)

            self.pending_msgs = new_msgs
            self.last_msgs = self.last_msgs + new_msgs

    def send_msg_entry(self):
        #Get text/clear Entry
        msg = self.entry.get()
        #TODO: Send message by thread id
        self.usr.sendMessage(self.users[0], msg) #Only send to usr

class App:

    def __init__(self):

        def attempt_login():
            self.root.title("WinstagramDM - Logging in")
            usr_name = usr_login.get()
            password = psswd.get()
            #disable editing while logging in
            usr_login.config(state="disabled")
            psswd.config(state="disabled")
            login.config(state="disabled")

            try:
                self.usr = api.User(usr_name, password)
                self.root.quit()
                self.logged_in = True

            except ValueError:
                psswd.delete(0, "end")

            if not self.logged_in:
                usr_login.config(state="normal")
                psswd.config(state="normal")
                login.config(state="normal")
                psswd.delete(0, "end")
                self.root.title("WinstagramDM - Login")
                #Resetup login thread to allow rerun
                self.login_thread = threading.Thread(target=attempt_login)
                self.login_thread.daemon = True
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

        self.location = "login"

        self.root = tk.Tk()
        self.root.title("WinstagramDM - Login")
        self.root.wm_iconbitmap('icon.ico')
        self.root.geometry(newGeometry=("500x500")) #Sizing
        self.root.minsize(500, 500)
        self.root.maxsize(500, 500)
        self.root.update()

        #Setup attempt_login thread
        self.login_thread = threading.Thread(target=attempt_login)
        self.login_thread.daemon = True
        self.logged_in = False

        usr_login = tk.Entry()
        usr_login.insert(0, "Username")
        usr_login.bind("<Button-1>", clear_entry)
        usr_login.bind("<Key>", clear_entry)
        usr_login.bind("<Return>",
                    lambda event: self.login_thread.start())
        usr_login.place(relx=.5, rely=.475, anchor="center")

        psswd = tk.Entry()
        psswd.insert(0, "Password")
        psswd.bind("<Button-1>", clear_entry_psswd)
        psswd.bind("<Key>", clear_entry_psswd)
        psswd.bind("<Return>",
                    lambda event: self.login_thread.start())
        psswd.place(relx=.5, rely=.525, anchor="center")

        login = tk.Button(command=lambda: self.login_thread.start())
        login["text"] = "Login"
        login.place(relx=.44, rely=.555)

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

        self.root.mainloop()
        #Clear icons
        usr_login.place_forget()
        psswd.place_forget()
        login.place_forget()
        self.homepage()

    def homepage(self):

        #BUG: Chats displayed not showing correct user

        def getChats():
            chats = []
            while True:

                if self.location != "homepage":
                    break

                new_chats = self.usr.getChats()

                if new_chats != chats:
                    chats = new_chats
                    self.pending_chats = []
                    for chat in new_chats:
                        #Get thread icon
                        response = requests.get(chat["thread_icon"])
                        font = ("Helvetica", 10)

                        if response.status_code == 200: #Check image received ok
                            tmp_win = tk.Tk()
                            tmp_img = Image.open(BytesIO(response.content))
                            tmp_img = tmp_img.resize((50, 50))
                            #Generate mask for circularising image
                            mask = Image.new("L", (50, 50), 0)
                            draw = ImageDraw.Draw(mask)
                            draw.ellipse((0, 0) + mask.size, fill=255)
                            tmp_img = ImageOps.fit(tmp_img, mask.size, centering=(.5, .5))
                            tmp_img.putalpha(mask)
                            image = ImageTk.PhotoImage(tmp_img)

                            chat_button = tk.Button(
                                self.root,
                                text='    ' + chat["thread_name"],#TODO: make label THREADNAME+\n+MOSTRECENTTEXT
                                command=lambda: self.convo_run(chat["thread_id"], chat["users"]),
                                font=font)

                            chat_button.image = image
                            chat_button.config(compound=tk.LEFT,
                                               image=image,
                                               anchor=tk.W,
                                               bd=1,
                                               highlightbackground="#333",
                                               bg="#111",
                                               fg="#ccc")

                        else:
                            chat_button = tk.Button(
                                self.root,
                                text='    ' + chat["thread_name"],
                                command=lambda: self.convo_run(chat["thread_id"], chat["users"]))

                            chat_button.config(
                                bd=1,
                                anchor=tk.W,
                                highlightbackground="#333",
                                bg="#111",
                                fg="#ccc"
                            )

                        self.pending_chats.append(chat_button)

        def update_chats():
            try:
                for chat_button in self.pending_chats:
                    chat_button.pack(fill=tk.X)
            except AttributeError:
                pass

            self.root.after(100, update_chats)

        self.location = "homepage" #Used for checking in threads

        #Setup window
        self.root.title("WinstagramDM - Homepage")
        self.root.maxsize(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.root.update()

        getChatsThread = threading.Thread(target=getChats)
        getChatsThread.daemon = True
        getChatsThread.start()

        # TODO: Use scrollbar
        self.root.after(1, update_chats) #update chat initial run
        self.root.mainloop()

    def convo_run(self, threadId, users):

        def update_msgs():
            #TODO: Update msgs
            self.root.after(100, update_msgs)

        #TODO: Make use self.root
        #TODO: Thread message sending

        self.location = "convorun"
        root = tk.Tk()

        msg_in = tk.Entry(root)
        msg_in.pack(side="bottom", fill="x")
        msg_in.focus_set()

        chat = Chat(self, msg_in, threadId, users)

        #Thread setup
        get_msg_thread = threading.Thread(target=chat.get_msgs)
        get_msg_thread.daemon = True
        get_msg_thread.start()

        #Bindings
        msg_in.bind("<Return>", lambda event: chat.send_msg_entry())

        self.root.after(100, update_msgs)
        root.mainloop()

        #TODO: get msgs, update position when new received, show back/targetusr/info in top, quit on back

def main():
    app = App()

if __name__ == "__main__":
    main()