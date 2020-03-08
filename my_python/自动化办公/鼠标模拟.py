import win32api
import win32con
from time import sleep


#设置鼠标的位置
win32api.SetCursorPos([500,400])
sleep(0.1)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)

sleep(0.1)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)