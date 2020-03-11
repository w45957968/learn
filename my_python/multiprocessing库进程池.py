# -*- coding: utf-8 -*-
import time,os,random
from multiprocessing import Pool


def run(i):
    starttime = time.time()
    print("进程%d开始，进程ID为%s"%(i+1,os.getpid()))
    time.sleep(random.choice([1,2,3])  )
    endtime = time.time()
    print("进程%s结束，耗时%.2f"%(i+1,endtime-starttime))

if __name__ == '__main__':
    print("主进程开始")
    starttime = time.time()
    pp = Pool()  #括号填进程数，一般为系统的核心数，不填默认为系统核心数
    for i in range(16):
        pp.apply_async(run,args=(i,))
    pp.close()
    pp.join()
    endtime = time.time()
    print("主进程结束%.2f"%(endtime-starttime))