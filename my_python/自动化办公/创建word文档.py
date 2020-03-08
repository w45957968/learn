import win32com
import win32com.client
import os
from time import sleep


def createWord(filename,name):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True  #让文档可见

    #创建文档

    doc = word.Documents.Add()

    #写内容
    #从头开始写
    r = doc.Range(0,0)
    r.InsertAfter("亲爱的%s：\n"% name)
    r.InsertAfter("                \n")
    r.InsertAfter("    I miss you。。。。。 \n")
    r.InsertAfter("I miss you。。。。。 \n")
    sleep(0.1)
    #存储文件
    doc.SaveAs(filename)
    sleep(0.1)
    #关闭文件
    doc.Close()
    sleep(0.1)
    #关闭APP

    word.Quit()






names = ["张三","李四","王五","赵六"]

for name in names:
    path = r"C:\Users\Administrator\Desktop\words"
    filename = os.path.join(path,name + ".doc")
    createWord(filename,name)