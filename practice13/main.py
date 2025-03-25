import random
import subprocess
import webbrowser
import subprocess
import threading
import time




# pycharm
#chrome
#linkovi

# subprocess.Popen(["/opt/pycharm-2024.3.3/bin/pycharm"])

# %s on the end of the line merges two links together

# webbrowser.get("/usr/bin/google-chrome-stable %s").open("https://google.com")
# subprocess.Popen(["/usr/bin/google-chrome-stable"])

#na svakih 10 sekundi da se prikaze poruka / notifikacija


# def notifyit():
#     threading.Timer(10.0, notifyit).start()
#     subprocess.run(["notify-send", "Hello", messages[0]])
#
#
# notifyit()
#




messages = [
    "Take a break",
    "Too tired take a break",
    "Go make a rest"
]

while True:
    subprocess.run(["notify-send", "Hello", random.choice (messages)])
    time.sleep(3)
