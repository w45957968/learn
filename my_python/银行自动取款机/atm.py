import random
import time
import pickle

def loadInfo():
    f = open("userInfo.txt","rb")
    return pickle.load(f)
    f.close()
def downInfo(info):
    f = open("userInfo.txt","wb")
    pickle.dump(info,f)
    f.close()

class Atm(object):

    # def __init__(self):
    #     self.__condition = False   #登陆状态查询

    # def logout(self):
    #     self.__condition = True
    #
    # def login(self):
    #     self.__condition = False

    def creatUser(self):
        # if self.__condition == False:
        print("开户.......")
        personName = input("请输入你的姓名：")
        personID = int(input("请输入您的身份号码"))
        userpwd = int(input("请输入您的密码"))
        while True :
            if int(input("请确认密码：")) == userpwd :
                break
            elif int(input("请确认密码：")) != userpwd :
                pass
        print("您的帐号正在生成中........")
        time.sleep(2)
        userID = random.randrange(10000, 99999)
        print("您的账号为：%s" % userID)
        print("！！！请牢记您的帐号！！！")
        money = int(input("请存入您的金额"))
        userInfo = loadInfo()  # 读取用户信息
        time.sleep(2)
        userInfo[userID] = [personName, personID, userpwd, money,"T"]
        downInfo(userInfo)  # 存储用户信息
        time.sleep(2)
        print("恭喜您存入成功，您的帐户还有余额%.2f"%money)
        time.sleep(3)
            # self.__condition == True
        # else:
        #     print("请您退出后在执行此操作.......")
        #     return

    def searchInfo(self):
        userId = self.verifyUser()
        if userId:
            userInfo = loadInfo()
            print("欢迎尊敬的%s，您的账户还有余额%.2f" % (userInfo[userId][0], userInfo[userId][3]))
            time.sleep(3)
        else:
            print("************************************************")

        return -1

    def withdrawal(self):
        print("取款............")
        userId = self.verifyUser()
        if userId:
            userInfo = loadInfo()
            moneyDrawal = int(input("请输入您的取款金额："))
            print("正在为您取款中.........")
            time.sleep(2)
            if moneyDrawal > userInfo[userId][3]:
                print("您的账户余额不足，现已为您取出所有账户余额%.2f"% userInfo[userId][3])
                userInfo[userId][3] = 0
            elif moneyDrawal <= userInfo[userId][3]:
                userInfo[userId][3] -= moneyDrawal
                print("已为您取出现金%.2f，账户还有余额%.2f"% (moneyDrawal,userInfo[userId][3]))

            time.sleep(3)
            downInfo(userInfo)

        return -1

    def deposit(self):
        print("存款............")
        userId = self.verifyUser()
        if userId :
            userInfo = loadInfo()
            moneydeposit = int(input("请在存钞口放入您要存入的金额："))
            print("正在为您存款中.........")
            time.sleep(2)
            userInfo[userId][3] += moneydeposit
            print("以为您存入现金%.2f，您的账户余额为%.2f"% (moneydeposit,userInfo[userId][3]))
            time.sleep(3)
            downInfo(userInfo)

        return -1

    def transferAccounts(self):
        print("转账............")
        userId = self.verifyUser()
        if userId :
            userInfo = loadInfo()
            count1 = 0

            while count1 < 3:
                transId = int(input("请输入您要汇入的账户ID:"))
                count1 += 1
                if transId in userInfo:
                    moneyTran = int(input("请输入您要汇出的金额："))
                    if moneyTran > userInfo[userId][3]:
                        print("您的账户余额不足，将为您转出所有账户余额%.2f，转入账户为%s"%(userInfo[userId][3],transId))
                        userInfo[userId][3] = 0


                    elif moneyTran <= userInfo[userId][3]:
                        userInfo[userId][3] -= moneyTran
                        print("已为您转出现金%.2f，转入账户为%s，您的账户余额为%.2f"%(moneyTran,transId,userInfo[userId][3]))

                    userInfo[transId][3] += moneyTran
                    downInfo(userInfo)
                    break
                else:
                    print("您要汇入的账户不存在.......")
                    time.sleep(2)

            time.sleep(3)
            return -1

    def changePassword(self):
        print("改密............")
        userId = self.verifyUser()
        if userId :
            userInfo = loadInfo()
            count = 0
            pwdChange = int(input("请输入您的新密码："))
            while count < 3 :
                count += 1
                pwdCheck = int(input("请再次确认您的密码："))
                if pwdChange == pwdCheck:
                    print("您的密码已修改成功")
                    userInfo[userId][2] =pwdChange
                    downInfo(userInfo)
                    time.sleep(3)
                    break
                else:
                    print("您输入的密码和第一次不一样。")
                    time.sleep(2)

            return -1


    def lockUser(self):
        print("锁定............")
        userId = self.verifyUser()
        if userId :
            userInfo = loadInfo()
            print("您的账户%s,正在锁定中，请稍后....."% userId)
            time.sleep(2)
            userInfo[userId][-1] = "F"
            print("您的账户已锁定成功")
            downInfo(userInfo)
            time.sleep(3)

        return -1
    def unlockUser(self):
        print("解锁............")
        userId = int(input("请输入您的账户ID:"))
        userInfo = loadInfo()
        if userId in userInfo:
            if userInfo[userId][-1] == "F":
                count = 0
                while count < 3 :
                    count += 1
                    perID = int(input("请输入您的身份证号码:"))
                    if perID == userInfo[userId][1] :
                        print("您的账户正在解锁中，请稍后.....")
                        time.sleep(2)
                        userInfo[userId][-1] = "T"
                        print("您的账户已经解锁成功！")
                        downInfo(userInfo)
                        break
            else:
                print("您的账户没有锁定，不需要解锁。")
        else:
            print("您输入的账户不存在........")

        time.sleep(3)
        return -1
    def makeANewCard(self):
        print("补卡............")
        userId = int(input("请输入您的账户ID:"))
        userInfo = loadInfo()
        if userId in userInfo :
            check = input("您是否确认补办ID为%s的卡，不卡后原账户将消除（Y/N）").upper()

            if check == "Y" :
                count = 0
                while count < 3 :
                    count += 1
                    perID = int(input("请输入您的身份证号码:"))
                    if perID == userInfo[userId][1] :
                        print("您的新账户正在生成中，请稍后.....")
                        time.sleep(2)
                        userIdNew = random.randrange(10000,99999)
                        userInfo[userId][-1] = "T"
                        userInfo[userIdNew] = userInfo[userId]
                        userInfo.pop(userId)
                        print("您的新账户为%s，请牢记，原账户已删除，原账户余额已汇入新账户中！"% userIdNew)
                        downInfo(userInfo)
                        break

        else :
            print("您输入的账户不存在........")

        time.sleep(3)
        return -1

    def closeUser(self):
        print("销户............")
        userId = self.verifyUser()
        if userId :
            userInfo = loadInfo()
            check = input("您是否确认销户（Y/N）:").upper()
            if check == "Y":
                print("您的账户余额为%.2f，现在为您全部取出中...."% userInfo[userId][-2])
                time.sleep(2)
                userInfo.pop(userId)
                print("您的账户已销户")
                downInfo(userInfo)

        time.sleep(3)
        return -1

    def quit(self):
        print("退出............")

    def verifyUser(self):
        count = 0
        userId = int(input("请输入您的账号："))
        userInfo = loadInfo()
        if userId in userInfo:
            if userInfo[userId][4] == "T":
                while count < 3 :
                    count += 1
                    userpwd = int(input("请输入您的密码："))
                    if userpwd == userInfo[userId][2] :
                        return userId
                        break
                    else :
                        print("您输入的密码有误")
                else :
                    print("您的密码已连续输错三次，账户已锁定")
                    time.sleep(3)
                    userInfo[userId][4] = "F"
                    downInfo(userInfo)
                    return 0
            elif userInfo[userId][4] == "F" :
                print("您的账户已锁定不能登陆，请解锁后再试")
                time.sleep(3)
                return 0
        # elif not userId in userInfo:
        else:
            print("您的账户不存在，请核对后再试")
            time.sleep(3)
            return 0


if __name__ == '__main__':
    atm = Atm()
    # atm.creatUser()
    atm.searchInfo()