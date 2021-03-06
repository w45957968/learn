# -*- coding: utf-8 -*-
import threading
import time
import random

money_totle = 1000
glock = threading.Lock()


class Product_thread(threading.Thread):

    def run(self):
        global money_totle, glock
        while True:
            glock.acquire()
            money_rad = random.randint(0, 1000)
            money_totle += money_rad
            print("生产者%s生产了%s元，现共有钱%s元" % (threading.current_thread(), money_rad, money_totle))
            glock.release()
            time.sleep(0.1)


class Consumer_thread(threading.Thread):
    def run(self):
        global money_totle,glock
        while True:
            money_rad = random.randint(0,1000)
            glock.acquire()
            if money_totle >= money_rad:
                money_totle -= money_rad
                print("消费者%s消费了%s元，剩余%s元"%(threading.current_thread(),money_rad,money_totle))
                glock.release()
            else:
                print("消费者%s需要消费%s元，余额为%s元，余额不足"%(threading.current_thread(),money_rad,money_totle))
                glock.release()
            time.sleep(1)



class pro(threading.Thread):
    def run(self):
        for i in range(1,6):
            t = Consumer_thread(name="消费者{}".format(i))
            t.start()

class cun(threading.Thread):
    def run(self):
        for i in range(1, 2):
            t = Product_thread(name="生产者{}".format(i))
            t.start()


def start():
    t = pro()
    t2 =cun()
    t.start()
    t2.start()


if __name__ == '__main__':
    start()
