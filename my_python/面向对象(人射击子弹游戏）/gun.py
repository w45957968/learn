import random
class Gun(object):
    def __init__(self,bulletbox):
        self.bulletbox = bulletbox
    def shoot(self,mastername,obj):
        self.mastername = mastername
        self.obj = obj
        if self.bulletbox.count == 0:
            print("没子弹了！")
        else:
            self.bulletbox.count -= 1
            if random.randrange(1,100) % 2 == 0:
                self.obj.blood -= 20
                print("%s射击,击中了%s，%s掉血20，还有%s发子弹"% (self.mastername,self.obj.name,self.obj.name,self.bulletbox.count))
            else:
                print("%s射击,未击中了%s，%s还有%s发子弹" % (self.mastername, self.obj.name, self.mastername, self.bulletbox.count))

