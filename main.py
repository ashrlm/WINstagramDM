import time
import os
import getpass

import logic

def main():
    print("Welcome to WINstagram. Currently all this is is a chat client, but it will become a full IG client!")
    print("Modes")
    print("1: Bot mode")
    print("2: Chat mode")
    while True:
        try:
            usr = logic.User(input("Username: "), getpass.getpass())
            break
            
        except ValueError:
            pass
            
    while True:
        mode = input("Mode: ")
        if mode == '1':
            target = input("Target: ")
            text = input("Message Text: ")
            inf = input("Endless: ")
            if inf:
                delay = input("Delay between messages: ")
                if not delay:
                    delay = 0
                    
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
            
            continue
        
        elif mode == '2':
            print("Unavaliable")
        
        else:
            print("Invalid mode")
    

if __name__ == "__main__":
    main()