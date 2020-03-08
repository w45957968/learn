

import time
import datetime
#time 模块
time_stamp = time.time()
print(time_stamp)
lo_time = time.localtime(time_stamp)
gl_time = time.gmtime(time_stamp)
print(lo_time)
print(gl_time)
print(time.mktime(lo_time))
print(time.mktime(gl_time))
print(time.asctime())
print(time.strftime("%Y-%m_%d %H:%M:%S",time.localtime()))
print(time.strftime("%Y-%m_%d %X",time.localtime()))
print(time.strptime("2020-02_14 14:55:22","%Y-%m_%d %X"))
#datatime 模块
print(datetime.datetime.now())
print(datetime.datetime.today())
print(datetime.date.today())
print(datetime.time())



