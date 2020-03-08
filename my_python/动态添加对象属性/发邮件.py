import smtplib   #发邮件的库
from email.mime.text import MIMEText #邮件文本

#SMTP 服务器
smtpserver = "smtp.163.com"
#发邮件的地址
sender = "cmfhot@163.com" #发邮件的地址
passwd = "w45957968"  #授权密码

#设置发送的内容

message = "Hello World! Nice to meet you"
#文本转换，由字符串转成文本
msg = MIMEText(message)
#邮件的标题
msg["Subject"] = "来自帅哥的问候1"
#发件人
msg["From"] = sender
#收件人地址
recipients = ["bingfenghot@sina.com","cmfhot@163.com","cmfhot@live.cn","609218900@qq.com"]
#创建SMTP服务器
mailServer = smtplib.SMTP(smtpserver,25)
#登录邮箱
mailServer.login(sender,passwd)
#发送邮件           (发件人，收件人    ，msg转成邮件用字符串格式）
mailServer.sendmail(sender,recipients,msg.as_string())
#退出邮箱
mailServer.quit()