# **python学习练习库**
## python学习全记录
-[x] 记录 DAY1 —— 2020/3/8
  
  
 - 一. 今天学习内容Git 及 Github 的基本操作及使用。
  
    - 1.Git 的下载与安装。
  
    - 2.在Pycharm 中使用对Github 中的库的PULL 与PUSH。
  
    - 3.Github 中建设仓库的操作
  
    - 4.Github 中加入项目以及项目更新的操作     
      

-[x] 记录 DAY2 —— 2020/03/09


  - 一. 图片操作——PIL库的学习。

    - 1.库的导入与图片的打开。
      ```
      from PIL inmport Image
      image = Image.open("路径\图片.jpg")
      image.format   |   image.size    |  image.mode
      图片格式(JPEG) | 图片大小(700,700) | 图片颜色属性(RGB)
      image.show() # 显示图片
      ```
    - 2.图片的裁剪。
      ```
      rect = 50,50,750,750 # 两点裁剪，起点(50,50)，终点(750,750)
      image.crop(rect).show() # 按点裁剪图片并显示。  
      ```
    - 3.缩略图。单词记忆——thumbnail（缩略图）
      - 方法一
      ```
      size = 4000,400 #缩略图的大小
      image_thumbnail = image.thumbnail(size) # 制造缩略图
      image_thumbnail.show()
      ```
      - 方法二
      ```
      size = 100,100
      image_thumbnail = image.resize(size)
      image_thumbnail.show() 
      ```
    - 4.图片的粘贴融合。
      ```
      image1 = Image.open("1.jpg")
      image2 = Image.open("2.jpg")
      rect = 0,0,800,700
      image3 = image2.crop(rect) # 对图片2进行裁剪
      image4 = image1.paste(image3,(0,0)) # 粘贴图片 image1(底片).paste(要粘贴的图片，(位置))
      ```
    - 5.图片的旋转、翻转。
      ```
      image.rotate(90).show() # 图片逆时针旋转90°  注：rotate 方法旋转方向逆时针
      image.transpose(Image.FLIP_LEFT_RIGHT).show() # 图片反转 ，方法 左右翻转
      ```
    - 6.像素操作。
      ```
      改变一个点的像素颜色
      image.putpixel((x,y),(0,255,0)) # 将点(x,y)的颜色变为绿色
      改变一片区域的像素颜色为绿色
      for x in range(80,200):
            for y in range(90,300):
                image.putpixel((x,y),(0,255,0))
      
      image.show()
      ```  
    - 7.给图片添加滤镜
      ```
      form PIL import Image,Image.Filter
      image.filter(Image.Filter.CONTOUR).show()
      ```   
       
       
    
    
      
        