from types import MethodType
class Person(object):
    __slots__ = ("name","age","speak")    #限制对象动态添加属性或方法的范围
    def __init__(self):
        pass

per = Person()
per.name = "alex"  #动态添加对象属性
print(per.name)
def say(self):
    print("%s say 'Hello'"%(self.name))
per.sperk = MethodType(say,per)   #动态添加方法
per.sperk()

