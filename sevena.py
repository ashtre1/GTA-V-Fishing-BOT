import cv2
import numpy as np
import pyautogui
import keyboard
from pynput.mouse import Controller as Controller
from pynput.mouse import Button
import time
import tkinter as tk
import random
from win32gui import GetWindowText, GetForegroundWindow
from tkinter import *




print("SevenA GTA:V BOT")
TriggerBot_Status = False
AntiAfk_Status = False
Enabled = True

def balikcalis(ftimes):
    for x in range(ftimes):
        k = 0.153 + ((x ** 0.5) / 400)

        keyboard.press("up")
        print (k)
        time.sleep(k)
        keyboard.release("up")
        print("balik tutuluyor")
        img = pyautogui.screenshot(region=(955, 1000, 30, 70))
        img = np.array(img)
        frame = np.array(img).sum()
        print('colorValue: ' + str(frame))
        r = 200.0 / img.shape[1]
        dim = (200, int(img.shape[0] * r))
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("screenshot", img)
        time.sleep(0.1)



def AntiAfk_Move():
    time.sleep(5)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        mouse = Controller()
        keyboard.press("ı")
        time.sleep(0.1)
        keyboard.release("ı")
        print('Envanter açıldı')
    time.sleep(0.2)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        pyautogui.dragTo(610, 530, button='left', duration=0.2)
        print('Mouse oltanın üstüne getirildi')
    time.sleep(0.2)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        pyautogui.click(button='right')
        print('Oltaya tıklandı')
    time.sleep(0.2)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        pyautogui.dragTo(630, 550, button='left', duration=0.2)
        print('Mouse oltayı kullan yazısının üstüne getirildi')
    time.sleep(0.35)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        pyautogui.click(button='left')
        print('Oltaya tıklandı')
    time.sleep(0.2)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        keyboard.press("ı")
        time.sleep(0.1)
        keyboard.release("ı")
        print('Envanter kapatildi')
    time.sleep(0.2)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        balikcalis(30)
    time.sleep(50)

window = Tk()

window.title("SevenA")
w = 250
h = 350

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.configure(background="#010221")


lbl = Label(window, bg="#010221", fg="#07aaaf", font=5, text="Oto Balık", padx = 30, pady = 10)

lbl.grid(column=0, row=0)

lbl2 = Label(window, bg="#010221", fg="#07aaaf", font=5, text="Devre Dışı")

def AntiAFK_ChangeStatus():
    global AntiAfk_Status
    if AntiAfk_Status == True:
        lbl2.configure(text= "Devre Dışı")
        AntiAfk_Status = False
        print("BOT Devre Dışı")
    else:
        lbl2.configure(text= "Aktif")
        AntiAfk_Status = True
        print("BOT Aktif")

lbl2.grid(column=1, row=0)

btn = Button(window, bg="#010221", fg="#07aaaf", text="Tıkla", command=AntiAFK_ChangeStatus)

btn.grid(column=0, row=1)


#---------------------------------------------------

def looping():


    if keyboard.is_pressed('k'):
        AntiAFK_ChangeStatus()
        time.sleep(1.05)
        
    window.after(100, looping)
    current_window = (GetWindowText(GetForegroundWindow()))
    if current_window.find("alt:V") != -1:
        if AntiAfk_Status == True:
            AntiAfk_Move()

window.after(100, looping)
window.mainloop()


