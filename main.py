import os
from tkinter import *
from tkinter import filedialog as filed  
from win32con import SW_HIDE,SW_NORMAL 
import win32gui
import keyboard
import time



def hidden():
    print('hidden start')
    pid = win32gui.GetForegroundWindow() 
    win32gui.ShowWindow(pid , SW_HIDE) 
    print('hidden end')
    


def de_perivet():
    print('de_perivet')
    global file
    if file: 
        with open(file_name, 'wb') as t:
            t.write(file)
            file = None
    global a
    a = 0


def perivet():    
    global file_name
    file_name = filed.askopenfilename()
    if file_name == '':
        raise(ValueError('select one file'))
    
    print('end get file_name')
    with open(file_name, 'rb') as f:
        global file
        file = f.read()
    
    os.remove(file_name)
    print('end remove file')
    keyboard.add_hotkey('alt+x', de_perivet) 
    hidden()

a = 1
perivet()

while a:
    time.sleep(1)