import pyautogui
import webbrowser
import time
import random

url = "https://presearch.org"

x=1

while (x<=400):

    webbrowser.get("Firefox").open(url, new=0, autoraise=True)

    time.sleep(2)

    WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
    word = random.choice(WORDS)
    correct = word
    pyautogui.typewrite(correct)


    time.sleep(0.5)

    pyautogui.hotkey("enter")

    time.sleep(5.5)

    pyautogui.hotkey('Command', 'w')

    print (x)

    x = x+1

print ("Finish")

