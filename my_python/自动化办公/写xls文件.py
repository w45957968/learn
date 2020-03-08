from pyexcel_xls import save_data
from collections import OrderedDict
import re


def txtTXls(path):
    dic =OrderedDict()
    linelist = []
    with open(path,"r") as f:
        for line in f:
            linefile = re.split(" +",line.strip().replace("-"," "))

            linelist.append(linefile)
    dic.update({"sheet1":linelist})

    save_data(r"C:\Users\Administrator\Desktop\a2.xls",dic)

path = r"C:\Users\Administrator\Desktop\a2.txt"

txtTXls(path)