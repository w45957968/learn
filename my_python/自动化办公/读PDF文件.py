import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextState


def readPDF(path):
    #pdf文件会以二进制打开
    f = open(path,"rb")
    #创建一个pdf文件分析器
    parser = PDFParser(f)

    pdfFile = PDFDocument()

    #链接分析器和PDF文件对象
    parser.set_document(pdfFile)
    #提供初始化密码
    pdfFile.initialize()

    #检测文档是否提供TXT转换
    if not pdfFile.is_extractable:
        raise PDFTextState
    else:
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备的对象
        laparams = LAParams()
        devicce = PDFPageAggregator(manager,laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager,devicce)
    #开始循环处理，每次处理一页
    for page in pdfFile.get_pages():
        interpreter.process_page(page)

        layout = devicce.get_result()
        for x in layout:
            if (isinstance(x,LTTextBoxHorizontal)):  #判断x 是否是 LTTextBoxHorizontal 类型的
                with open(toPath,"a") as f1:
                    str = x.get_text()
                    print(str)
                    f1.write(str+"\n")

path = r"C:\Users\Administrator\Desktop\个人信用报告.pdf"
toPath = r"C:\Users\Administrator\Desktop\个人信用报告.txt"
readPDF(path)

