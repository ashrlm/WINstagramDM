#!/usr/bin/env python3

import time
import os
import getpass

import api

def main():
    print("Welcome to WINstagram. Currently all this is is a chat client, but it will become a full IG client!")
    print("Modes")
    print("1: Bot mode")
    print("2: Chat mode")
    while True:
        try:
            usr = api.User(input("Username: "), getpass.getpass())
            break

        except ValueError:
            pass

    while True:
        mode = input("Mode: ")
        if mode == '1':
            target = input("Target: ")
            text = input("Message Text: ")
            inf = input("Endless: ")
            if inf != None:
                while True:
                    try:
                        delay = int(input("Delay between messages: "))
                        break

                    except ValueError:
                        print("Invalid time")

                while True:
                    try:
                        usr.sendMessage(target, text)
                        time.sleep(delay)
                    except KeyboardInterrupt:
                        break

                continue

            else:
                num_iters = input("Number of Messages: ")
                for i in range(int(num_iters)):
                    usr.sendMessage(target, text)


            print('')
            continue

        elif mode == '2':
            receiver = input("Who to chat with: ") #Get chat with
            #TODO: Get messages in chat - Need to convert to GUI for display
            while True:
                try:
                    msg = input(">>> ")
                    usr.sendMessage(receiver, msg)

                except KeyboardInterrupt: #Allow user to leave chat with Ctrl-C
                    break

        else:
            print("Invalid mode")


if __name__ == "__main__":
    main()
