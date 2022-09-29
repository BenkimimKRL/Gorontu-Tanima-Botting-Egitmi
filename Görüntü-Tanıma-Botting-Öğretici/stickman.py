#Demin bahsetigim Alan pencere yada bölgesel alan hesaplama programında diyelim buldugumuz yada yapmak istedigimiz alanın konumunu region=(150,175,350,600)kısmına yazıyoruz
#Bu komut dosyası stickman.png görüntüsünü verdiğimiz bölgede bulur ve görüp göremeyeceğini size söyler

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('stickman.png', region=(150,175,350,600), grayscale=True, confidence=0.8) != None:
        print("onu görebiliyorum")
        time.sleep(0.5)
    else:
        print("onu göremiyorum")
        time.sleep(0.5)
