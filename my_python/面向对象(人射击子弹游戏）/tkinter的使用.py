import tkinter

#创建主窗口

win = tkinter.Tk()
#设置标题
win.title("创作者： Reborn")
#设置大小和位置  "长 x 宽 + 左边距离 + 上边距离"
win.geometry("400x400+200+200")
#添加控件
"""
#Label:标签控件可以显示文本                  参数
#1、父窗口
#2、文本
#3、背景色  可忽略
#4、字体颜色  可忽略
#5、字体即字体大小，元组格式  可忽略
#6、设置标签的宽度  可忽略
#7、设置标签的高度（具体测试）可忽略
#8、设置文字宽度，超出时换行 可忽略
#9、设置文字自动换行后的对齐方式，默认居中 可忽略
#10、设置文字在标签中的位置，上北下南左东右西 center 居中，可以组合ne东北等（n/s/e/w）
"""

label = tkinter.Label(win,
                      text="标签1",
                      bg="blue",
                      fg="red",
                      font=("黑体",20),
                      width=10,
                      height=2,
                      wraplength=100,
                      justify="left",
                      anchor="n")
#显示标签到窗口
label.pack()


#按钮 button
button = tkinter.Button(win,text="按钮")
button.pack()



win.mainloop()