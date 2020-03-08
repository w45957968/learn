
import win32con
import win32gui
import time
import random
import win32com.client

"""
while 1:
    winGoogle = win32gui.FindWindow("Chrome_WidgetWin_1", "爱资料在线工具-好用的在线工具箱 - Google Chrome")  # 获取窗体 传入参数:窗口类名，窗口标题
    # win32gui.ShowWindow(winGoogle, win32con.SW_HIDE)  # 隐藏窗口
    # time.sleep(2)
    # win32gui.ShowWindow(winGoogle, win32con.SW_SHOW)  # 显示窗口
    time.sleep(2)
    #控制窗体的位置
    #参数1：要控制的窗体
    #参数2：大致的方位，HWND_TOPMOST上方
    #参数3：位置x
    #参数3：位置Y
    #参数5：长度
    #参数6：宽度
    #参数7：win32con.SWP_SHOWWINDOW 意思是一直显示窗体
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(winGoogle,win32con.HWND_TOPMOST,x,y,500,500,win32con.SWP_SHOWWINDOW)
"""

"""语音识别
speaker = win32com.client.Dispatch("SAPI.SPVIOCE")
speaker.Speak("你真漂亮！")
"""