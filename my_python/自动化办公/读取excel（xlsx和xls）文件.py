from collections import OrderedDict     #OrderdDict 有序字典
from pyexcel_xls import get_data

def readXlsAndXlsx(path):
    dic = OrderedDict()

    #抓取数据
    xdata = get_data(path)
    print("".center(100,"*"))
    print(xdata)
    print("".center(100, "*"))
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

# path = r"C:\Users\Administrator\Desktop\洛阳户籍1.17-21.xls"
path = r"C:\Users\Administrator\Desktop\洛阳户籍.xlsx"
dic = readXlsAndXlsx(path)
print(dic)