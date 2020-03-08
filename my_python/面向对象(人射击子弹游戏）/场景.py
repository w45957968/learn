from person import Person
from gun import Gun
from bulletbox import Bulletbox
import random
from time import sleep
bulletbox = Bulletbox(10)
gun = Gun(bulletbox)

per = Person("alex",100,gun)
p2 = Person("rice",100,Gun(Bulletbox(10)))
while p2.blood > 0 and per.blood > 0:
    sleep(3)
    if random.randrange(1,100) % 2 == 0:
        per.fire(p2)
    else:
        p2.fire(per)
    sleep(1)

    if p2.gun.bulletbox.count == 0:
        cho = input("{}已经没有子弹了，但还有血量{},是否用20的血换一发子弹(Y/N)：".format(p2.name,p2.blood))
        if cho.upper() == "Y":
            p2.gun.bulletbox.count = 1
            p2.blood -= 20
        else:
            continue
    elif per.gun.bulletbox.count == 0:
        cho = input("{}已经没有子弹了，但还有血量{},是否用20的血换一发子弹(Y/N)：".format(per.name,per.blood))
        if cho.upper() == "Y":
            per.gun.bulletbox.count = 1
            per.blood -= 20
        else:
            continue



else:
    if p2.blood == 0:
        print("%s被%s击杀，游戏结束！"%(p2.name,per.name))
    else:
        print("%s被%s击杀，游戏结束！" % (per.name, p2.name))
