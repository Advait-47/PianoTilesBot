from time import sleep
import numpy as np
from PIL import ImageGrab as ig
import pyautogui as pag
import mouse
import cv2 as cv

# while True:
#     print(pag.position())
#     sleep(1)
sleep(3)

# capline = 989
# spos = (676, capline-1, 1102, capline+1)
# fpos = np.array([0, int((spos[2]-spos[0])/3), int((spos[2]-spos[0])/3*2),
#                  int(spos[2]-spos[0])-1])
# pcolors = [50, 50, 50]
# score = 0
# c1 = 600
# c2 = 708
# c3 = 819
# c4 = 926
c = np.array([600, 708, 819, 926])
rownum = 874
interval = 62
pag.PAUSE = 0
pixval = 50
while True:
    for i in c:
        i = int(i)
        if(pag.pixel(i, rownum)[0] < pixval):
            pag.click(i, rownum)

#     if(pag.pixel(c1, rownum+((score//500)*20))[0] < pixval):
#         pag.click(c1, rownum+(((score//500)*10)))
#         score += 1
#         continue
#     if(pag.pixel(c2, rownum+((score//500)*20))[0] < pixval):
#         pag.click(c2, rownum+(((score//500)*20)))
#         score += 1
#         continue
#     if(pag.pixel(c3, rownum+((score//500)*20))[0] < pixval):
#         pag.click(c3, rownum+(((score//500)*20)))
#         score += 1
#         continue
#     if(pag.pixel(c4, rownum+((score//500)*20))[0] < pixval):
#         pag.click(c4, rownum+(((score//500)*20)))
#         score += 1
#         continue

# # img = ig.grab(bbox=spos)
# # arrimg = np.array(img)
# # gimg = cv.cvtColor(arrimg, cv.COLOR_BGR2GRAY)
# # print(np.count_nonzero(gimg))
# # arrgimg = np.reshape(gimg, (2, 426))

# # fimg = np.reshape(cv.cvtColor(np.array(ig.grab(bbox=spos)),
# #                  cv.COLOR_BGR2GRAY), (2, 426))
# # print(arrgimg)
# # i = input()


# # while True:
# #     for i in fpos:
# #         img = ig.grab(bbox=spos)
# #         # fimg = cv.cvtColor(np.array(ig.grab(bbox=spos)),
# #         #                    cv.COLOR_BGR2GRAY)
# #         if((np.array(img.getpixel((i, 1))) < np.array(pcolors)).any()):
# #             # if((fimg[0][i] < 120)):
# #             # pag.moveTo(spos[0]+i, capline)
# #             pag.click(x=spos[0]+i, y=capline)
# #             break
# #         # sleep(0.1)
