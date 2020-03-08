class Person(object):
    def __init__(self,name,blood,gun):
        self.name = name
        self.blood = blood
        self.gun = gun
    def fire(self,person):
        self.person = person
        self.gun.shoot(self.name,self.person)

    def fillbullet(self,count):
        self.gun.bulletbox.count = count

