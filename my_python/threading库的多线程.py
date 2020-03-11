# -*- coding: utf-8 -*-
import threading
from time import sleep

''' 普通单线程程序
def drawing():
    for i in range(10):
        print("正在进行第%s次画图"%i)
        sleep(1)

def Printing():
    for i in range(10):
        print("--正在进行第%s次打印"%i)
        sleep(1)

def starting():
    t1 = drawing()
    t2 = Printing()

if __name__ == '__main__':
    t3 = starting()
'''
'''普通多线程程序
def drawing():
    for i in range(10):
        print("正在进行第%s次画图"%i)
        sleep(1)

def Printing():
    for i in range(10):
        print("--正在进行第%s次打印"%i)
        sleep(1)

def starting():
    t1 = threading.Thread(target=drawing)
    t2 = threading.Thread(target=Printing)

    t1.start()
    t2.start()

if __name__ == '__main__':
    t3 = starting()
'''
'''以 Thread 为父类，创建子类'''


class drawing_thread(threading.Thread):
    def run(self):
        for i in range(10):
            print("正在进行第%s次画图" % i)
            sleep(1)

    print(threading.current_thread())  # 打印正在执行的线程的名称


class Printing_thread(threading.Thread):
    def run(self):
        for i in range(10):
            print("--正在进行第%s次打印" % i)
            sleep(1)

    print(threading.current_thread())  # 打印正在执行的线程的名称


def start():
    t1 = drawing_thread()
    t2 = Printing_thread()

    t1.start()
    t2.start()


if __name__ == '__main__':
    start()
    print(threading.current_thread())  # 打印正在执行的线程的名称


