import pyautogui
import time

def _moveToAndClickPoint(point):
    pyautogui.moveTo(point)
    pyautogui.click()

def clickOnImage(imagePath):
    img = pyautogui.locateCenterOnScreen(imagePath)
    if img is not None:
        _moveToAndClickPoint(img)

def clickOnMultipleImage(imagePath):
    imgs = pyautogui.locateAllOnScreen(imagePath)
    for img in imgs:
        _moveToAndClickPoint(img)
        time.sleep(2)