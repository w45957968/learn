# -*- coding: utf-8 -*-

from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        print("sunck is a %s man--%s，父进程%s"% (str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == '__main__':
    p = Process(target=run,args=("nice",))
    p.start()
    while True:
        print("主进程启动--%s" % os.getpid())
        sleep(2)