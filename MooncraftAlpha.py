updateRate = 0.1
from pythmc import ChatLink
import time
import os
import subprocess
chat = ChatLink()
lastText = "N/A"
os.chdir("dectalk/")
isChat = 0
while True:
    lastMessage = chat.get_history(limit=1)
    for message in lastMessage:
        if message.content != lastText:
            msg = message.content
            if msg.__contains__("> "): # Default + Single-Arrow Formatting
                isChat = 1
                msgSplit = msg.split("> ")[1]
            elif msg.__contains__(": "): # Hypixel Formatting
                isChat = 1
                msgSplit = msg.split(": ")[1]
            if isChat == 1:
                print(msgSplit)
                cmd = 'say.exe "'+msgSplit+'"'
                subprocess.Popen(cmd)
                lastText = message.content
                isChat = 0
    time.sleep(updateRate)
