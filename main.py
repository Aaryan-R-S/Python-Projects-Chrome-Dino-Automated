# ---------------------- 1 -------------- Requirements
import time
import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
# pip install pyautogui, pillow

# ---------------------- 1 -------------- Funcs

def isCollide(data):
    for i in range(560, 620):                   
        for j in range(670, 710):
            if data[i, j] > 140:
                hitKey("up")
                return True
    for i in range(560, 620):                   
        for j in range(560, 600):
            if data[i, j] > 140:
                hitKey("down")
                hitKey("down")
                return True
    return False


def hitKey(key):
    pyautogui.keyDown(key)


# ---------------------- 1 -------------- Run
if __name__ == "__main__":
    time.sleep(2)
    hitKey("up")
    while True:
        img = ImageGrab.grab().convert('L')

        data = img.load()
        # print(asarray(image))               # uncomment import numpy

        isCollide(data)


        # ---- Draw rectangle ---
        # for i in range(490, 550):                   
        #     for j in range(660, 700):
        #             data[i, j] = 100   
                    
        # for i in range(490, 550):                   
        #     for j in range(560, 600):
        #             data[i, j] = 100   

        # img.show()
        # break
