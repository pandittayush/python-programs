import pyautogui as spam
import time 

limit = ("Enter your limit: ")
Msg   =("Enter your Message: ")

i = 0

time.sleep(10)

while i<int(limit):
    spam.typewriter(Msg)
    spam.press("enter")

    i+=1
