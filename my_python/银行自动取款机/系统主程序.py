"""
人
类名：Person
属性：姓名 身份证号 电话号 卡

卡
类名：Card
属性：卡号 密码 余额
行为:

提款机
类名：ATM
属性
行为：开户 查询 取款 存储 转账 改密 锁定 解锁 补卡 销户 退出

界面
类名： View
属性：
行为：管理员界面  登录  客户界面

银行
类名：Bank
属性：用户列表 提款机

"""
from view import View
from atm import Atm
import time
import random
#71096  15088
def main():
    view = View()
    atm = Atm()
    view.admin_view()
    if view.adminlogin() == -1:
        return -1
    print("登陆成功.........")
    time.sleep(2)
    while 1:
        view.guest_view()
        option = input("请选择您的操作：")
        if option == "1":
            atm.creatUser()
        elif option == "2":
            atm.searchInfo()
        elif option == "3":
            atm.withdrawal()
        elif option == "4":
            atm.deposit()
        elif option == "5":
            atm.transferAccounts()
        elif option == "6":
            atm.changePassword()
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            atm.makeANewCard()
        elif option == "0":
            atm.closeUser()
        elif option == "q" or option == "Q":
            if view.adminlogin() == "a":
                print("系统正在退出中....")
                time.sleep(2)
                break

        elif option == "a" or option == "A":
            if view.adminlogin() == -1:
                pass







if __name__ == "__main__":
    main()
