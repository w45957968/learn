# -*- coding: utf-8 -*-
import pymysql

#创建数据库对象
conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "c123",
    port = 3306,
    database = "xiciip"
)
#创建一个游标
cursor = conn.cursor()

#插入数据的语法
#insert into 表名(标签1，标签2，标签3，标签4) values(数据1，数据2，数据3，数据4)

'''
sql = """
     insert into biaoming(标签1，标签2，标签3，标签4) values(%s,%s,%s,%s)   
"""
cursor.execute(sql,(数据1，数据2，数据3，数据4))

cursor.commit()

'''
'''
sql = """
      select 标签1，标签2 from 表名 where (条件如id = 2)  # select * from 表名
"""
cursor.execute(sql)
res = cursor.fetchone()

fetchone 取一条数据  fetchall 取所有数据 fetchmany() 按顺序去指定条数据
'''
# sql = """delete from 表名 where id=1"""  删除数据
# sql = """update  表名 set 标签名=数据 where id=2"""