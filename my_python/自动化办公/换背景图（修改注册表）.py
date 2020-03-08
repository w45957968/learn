import win32api
import win32con
import win32gui
#正常方法
#win键 + R  ----> regedit  ----> HKEY_CURRENT_USER  ---->  Control panel ----> Desktop

def changeWallPager(path):
    #打开注册表 找到要修改的的注册表的目录
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Comtral Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    #找到对应的注册表       （ ，注册表名称（墙纸类型），0，注册表类型，2——拉伸 0——居中 6——适应 10——填充
    win32api.RegSetValueEx(reg_key,"WallPageStyle",0,win32con.REG_SZ,"6")
    #设置墙纸
    # win32api.RegSetValueEx(reg_key,"WallPager")

    #                                          设置墙纸         墙纸路径       设置立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)



path = r""
