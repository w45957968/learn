# **python学习练习库**
## python学习全记录
-[x] 记录1 —— 2020/03/08
  
  
   - 一. 今天学习内容Git 及 Github 的基本操作及使用。
  
     - 1.Git 的下载与安装。
  
     - 2.在Pycharm 中使用对Github 中的库的PULL 与PUSH。
  
     - 3.Github 中建设仓库的操作
  
     - 4.Github 中加入项目以及项目更新的操作     
 -[x] 记录2 —— 2020/03/09
    
    
   - 一.通过PIL库对图片的操作。
   
     - 1.图片的打开与显示
      ```
     from PIL import Image
     image = Image.open("1.jpg")
     image.format   |   image.size      |  image.mode
     图片的格式(JPEG)| 图片的大小(800,800)| 图片的颜色属性(RGB)
     image.show()   # 显示图片
     ```
     - 2.图片的额裁剪
      ```
     rect = 0,0,800,700  # 起点(0,0) 终点(800,700)
     image1 = image.crop(rect)
     image1.show()
      ```
     - 3.生成缩略图
       - 方法一 ——使用thumbnail方法
       ```
       size = 300,300
       image1 = image.thumbnail(size)
       image1.show()
       ```
       - 方法二 ——使用resize方法
        ```
       size = 300,300
       image2 = image.resize(size)
       image2.show()
       ```  
     - 4.图片的粘贴融合
      ```
     image1 = Image.open("1.jpg")
     image2 = Image.open("2.jpg")
     rect = 0,0,800,700
     image3 = image2.crop(rect)
     image4 = image.paste(image3,(0,0))  # image(底片).paste(image3(要粘贴的图片),(起始位置))
     ``` 
     - 5.图片的旋转与翻转
      ```
     image1 = image.rotate(90)  # 图片逆时针旋转90° rotate 方法旋转方向逆时针
     image1.show()
     image2 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 图片翻转——左右翻转
     image2.show()
     ```
     - 6.像素操作
      ```
     单个像素点的操作——将点(x,y)的颜色变为绿色
     image.putpixel((x,y),(0,255,0))```
     image.show()
     一片区域的像素点的操作——将一片区域的颜色变为绿色
     for x in range(80,300):
            for y in range(100,400):
                    image.putpixel((x,y),(0,255,0))
     
     image.show()
     ```
     - 7.给图片添加滤镜
      ```
     form PIL import Image.Filter
     image.filter(Image.Filter.CONTOUR).show()
     ```
