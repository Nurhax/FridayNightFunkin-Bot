from pyautogui import *
import pyautogui as pyg
import time as tm
import threading
import keyboard as key

berhenti = False

tm.sleep(1)

def pencet(x):
    pyg.keyDown(x)
    tm.sleep(2)
    pyg.keyUp(x)


ungu = [194, 75, 153]
biru =[0, 255, 255]
ijo = [18, 250, 5]
merah = [249,  57, 63]

y = 239
kiri = [510,y]
bawah = [583,y]
atas = [646,y]
kanan = [725,y]

def cekKiri():
    while True and berhenti == False:
        if (pyg.pixel(kiri[0],kiri[1])[0] == ungu[0] and pyg.pixel(kiri[0],kiri[1])[1] == ungu[1] and pyg.pixel(kiri[0],kiri[1])[2] == ungu[2]):
            pencet('left')

def cekBawah():
    while True and berhenti == False:
        if (pyg.pixel(bawah[0],bawah[1])[0] == biru[0] and pyg.pixel(bawah[0],bawah[1])[1] == biru[1] and pyg.pixel(bawah[0],bawah[1])[2] == biru[2]):
            pencet('down')

def cekAtas():
    while True and berhenti == False:
        if (pyg.pixel(atas[0],atas[1])[0] == ijo[0] and pyg.pixel(atas[0],atas[1])[1] == ijo[1] and pyg.pixel(atas[0],atas[1])[2] == ijo[2]):
            pencet('up')

def cekKanan():
    while True and berhenti == False:
        if (pyg.pixel(kanan[0],kanan[1])[0] == merah[0] and pyg.pixel(kanan[0],kanan[1])[1] == merah[1] and pyg.pixel(kanan[0],kanan[1])[2] == merah[2]):
            pencet('right')

def Berhenti(cekBerhenti):
    while True:
        if key.is_pressed('z') == True:
            break
        

def ThreadingStart():
    threading.Thread(target=cekKiri, daemon=True).start()
    threading.Thread(target=cekBawah, daemon=True).start()
    threading.Thread(target=cekAtas, daemon=True).start()
    threading.Thread(target=cekKanan, daemon=True).start()


print("Pencet Z Kalau Mau Berhenti!")
ThreadingStart()
Berhenti(berhenti)

    







    

    

   

    

