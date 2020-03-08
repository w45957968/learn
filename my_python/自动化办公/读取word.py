import win32com
import win32com.client

def readAndWriteWord(path,topath):
    # 调用系统WORD的功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开文件
    rdoc = mw.Documents.Open(path)
    rdoc.SaveAs(topath,2)    # 2 表示为txt文件
    for par in rdoc.Paragraphs:
        line = par.Range.Text
        print(line)

    #关闭文件
    rdoc.Close()
    #退出word
    mw.Quit()



path = r"C:\Users\Administrator\Desktop\免费简历 黑白.doc"
topath = r"C:\Users\Administrator\Desktop\免费简历.txt"
readAndWriteWord(path,topath)