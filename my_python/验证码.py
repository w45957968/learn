def verifycode(request):
    #引入绘图魔模块
    from PIL import Image,ImageDraw,ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20,100)),(random.randrange(20,100)),(random.randrange(20,100))
    width = 100
    height = 50
    #创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point（）函数绘制噪点
    for i in range(0,200):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,(random.randrange(0,255)))
        draw.point(xy,fill)
    #定义验证码的被选值
    str_list = '''1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'''
    #字体库
    font_stype = ['Arial','Ebrima','Bahnschrift','Calibri','Candara','Gadugi']
    # 随机选取4个值作为验证码
    str = ''
    for i in range(0,4):
        #构建字体对象
        font = ImageFont.truetype(r'C:\Windows\Fonts\%s.ttf'%(random.choice(font_stype)),40)
        # font = ImageFont.truetype(r'C:\Windows\Fonts\Gadugi.ttf',40)
        #构建字体颜色
        fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
        #随机取一个字符
        str_rand = random.choice(str_list)
        str += str_rand
        #确定绘制字符的横向位置
        if i == 0:
            x = 5
        else:
            x = 25*i
        # 绘制一个字
        draw.text((x,0),str_rand,font=font,fill=fontcolor)

    #释放画笔
    del draw
    #存入session，用于作进一步验证
    #request.session['verifycode']= str
    #内存文件操作
    # import io
    # buf = io.BinaryIO()
    #将图片保存在内存中，文件类型为png
    # im.save(buf,'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    # return HttpResponse(buf.getvalue(),'image/png')
    im.save(str+'.png','png')
    print(str)

verifycode('')