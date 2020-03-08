import win32con
import win32api
from time import sleep


win32api.keybd_event(91,0,0,0) #按下键值为91（win键）的键
sleep(0.1)                #等系统反应
win32api.keybd_event(91,0,win32con.KEYEVENTF_KEYUP,0) #抬起按键


while True:
    win32api.keybd_event(91,0,0,0)
    sleep(0.1)
    win32api.keybd_event(77,0,0,0)  #77对应 D键
    sleep(0.1)
    win32api.keybd_event(91,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(77,0,win32con.KEYEVENTF_KEYUP,0)
    sleep(3)