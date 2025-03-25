import time
import threading
import subprocess
import random
import webbrowser

messages = [
    "Take a break",
    "Too tired take a break",
    "Go make a rest"
]

subprocess.Popen(["/opt/pycharm-2024.3.3/bin/pycharm"])


webbrowser.get("/usr/bin/google-chrome-stable %s").open("https://itmentorstva.com")


def notifications():
    while True:
        subprocess.run(["notify-send", "Hello", random.choice(messages)])
        time.sleep(600)

notification_thread = threading.Thread(target=notifications)
notification_thread.start()


print("prosao vjezbu")