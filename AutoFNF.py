import pyautogui as pyg
import keyboard
import time
import threading

#Pencet "M" untuk mulai
def mulai():
    while True:
        if(keyboard.is_pressed('m')):
            break
        else:
            pass

def pencet(x):
    pyg.keyDown(x)
    time.sleep(0.1)
    pyg.keyUp(x)

def tahan(x, diam):
    while diam == False:
        pyg.keyDown(x)
    pyg.keyUp(x)

print("Kalau sudah dibuka gamenya pencat M untuk mulai!")
mulai()
