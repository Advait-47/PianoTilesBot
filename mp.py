from time import sleep
import numpy as np
from PIL import ImageGrab as ig
import pyautogui as pag
import cv2 as cv
import multiprocessing as mp
import os

# while True:
#     print(pag.position())
#     sleep(1)
sleep(3)
global score
score = 0
c1 = 600
c2 = 708
c3 = 819
c4 = 926
rownum = 734
pixval = 50


def col1():
    while True:
        if(pag.pixel(c1, rownum)[0] < pixval and score < 500):
            pag.click(c1, rownum)
            score += 1
        elif(pag.pixel(c1, rownum)[0] < pixval):
            pag.click(c1, rownum)
            score += 1


def col2():
    while True:
        if(pag.pixel(c2, rownum)[0] < pixval and score < 500):
            pag.click(c2, rownum)
            score += 1
        elif(pag.pixel(c2, rownum+20)[0] < pixval):
            pag.click(c2, rownum+20)
            score += 1


def col3():
    while True:
        if(pag.pixel(c3, rownum+20)[0] < pixval and score < 500):
            pag.click(c3, rownum+20)
            score += 1
        elif(pag.pixel(c3, rownum+20)[0] < pixval):
            pag.click(c3, rownum+20)
            score += 1


def col4():
    while True:
        if(pag.pixel(c4, rownum+20)[0] < pixval and score < 500):
            pag.click(c4, rownum+20)
            score += 1
        elif(pag.pixel(c4, rownum+20)[0] < pixval):
            pag.click(c4, rownum+20)
            score += 1


if __name__ == "__main__":
    p1 = mp.Process(target=col1)
    p2 = mp.Process(target=col2)
    p3 = mp.Process(target=col3)
    p4 = mp.Process(target=col4)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
