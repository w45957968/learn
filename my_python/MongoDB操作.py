# -*- coding: utf-8 -*-
import pymongo

#建立链接mongodb的对象
client = pymongo.MongoClient("127.0.0.1",port=27017)

#建立或者链接数据库（如有 zhihu 这个数据库，就链接，如果没有就创建
db = client.zhihu

#获取数据库中的集合（该数据库中的表，如果悠久链接，没有就创建）
collection = db.qa
'''
#写入数据 写入一条数据
collection.insert_one({'username':'riec','age':17,'M/F':'F'})  #两个一样

#写入数据  写入多条数据
collection.insert_many(
    [{
        'username':'rain',
        'age':18,
        'M/F':'M'
    },
    {
        'username':'sunck',
        'age':19,
        'M/F':'F'
    }]
)
'''
#查询数据
#查询所有数据
'''cursor = collection.find() #1.建立一个游标对象
for i in cursor:
    print(i)'''
#查询一条数据
'''result = collection.find_one() #result 在这里不是对象了,会返回第一条数据
print(result)
result = collection.find_one({'age' : 18}) #可以指定返回指定条件的数据
print(result)'''

#更新数据
#更新一条数据，必须给出要更新数据的条件
# collection.update_one({'user':'alex'},{'$set':{'user':'--alex--'}})

#更新多条数据
# collection.update_many({'username':'riec'},{'$set':{'username':'--rice--'}})

#删除数据
#删除一条数据
collection.delete_one({'user':'--alex--'})

#删除多条数据
collection.delete_many({'username':'--rice--'})