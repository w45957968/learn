import time
class View(object):
    # def __init__(self,admin,password):

    def admin_view(self):
        print("*********************************************************")
        print("*                                                       *")
        print("*                                                       *")
        print("*                  欢迎光临曹氏银行                       *")
        print("*                                                       *")
        print("*                                                       *")
        print("*                                                       *")
        print("*********************************************************")



    def guest_view(self):
        print("*********************************************************")
        print("*                  欢迎光临曹氏银行                       *")
        print("*********************************************************")
        print("*          开户 （1）           查询 （2)                *")
        print("*          取款 （3）           存款 （4)                *")
        print("*          转账 （5）           改密 （6)                *")
        print("*          锁定 （7）           解锁 （8)                *")
        print("*          补卡 （9）           销户 （0)                *")
        print("*          退出 （Q）         管理员登陆（A）             *")
        print("*********************************************************")

    def adminlogin(self):
        admin_in = input("系统账户：")
        password_in = input("系统密码：")
        if admin_in != "admin" or password_in != "45957968" :
            print("系统错误......")
            time.sleep(2)
            print("aghuigdfhguiougSDKNGUHsidJFHDCUVGBKLNDFUVBVBNJKCGsFgjfdbhdfgjigngah\n"
                  "asdjivhsihgadfgihdfagihuadfgihghioaihgihohhfdghfhdihioadfghidfhgioa\n"
                  "adfgjiefghiohdfghiohiohdfhgiohiohiofgojihihihhphihphophdfghphphphhp\n"
                  "...................................................................\n"
                  "...................................................................\n"
                  "................")
            time.sleep(2)
            return -1
        elif admin_in == "admin" or password_in == "45957968" :

            return "a"