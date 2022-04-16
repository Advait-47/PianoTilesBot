from time import sleep
import numpy as np
from PIL import ImageGrab as ig
import win32api
import win32con
import pyautogui as pag
import time

# while True:
#     print(pag.position())
#     sleep(1)
sleep(3)
c = np.array([665, 765, 865, 965])  # https://poki.com/en/g/piano-tiles-2
rownum = 561
# c = np.array([600, 708, 819, 926]) # https://www.silvergames.com/en/piano-tiles
#rownum = 874
pixval = 50

pag.PAUSE = 0


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while True:
    for i in c:
        # print(type(i))
        i = int(i)
        if(pag.pixel(i, rownum)[2] < pixval):
            click(i, rownum)
            sleep(0.01)
            continue
