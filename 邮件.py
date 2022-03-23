# 邮件发送
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 登录
smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtp_obj.login("1940811706@qq.com", "hhedfoqqrizxfbfi")

# 设置邮件内容

msg = MIMEText("这是我自己给自己发送的邮件", "plain", "utf-8")
msg["From"] = Header("我就是我", "utf-8")  # 发送者
msg["To"] = Header("你是谁", "utf-8")  # 接受者
msg["Subject"] = Header("我自己的信", "utf-8")  # 主题

# 发邮件

smtp_obj.sendmail("1940811706@qq.com", ["lm20000223@163.com"], msg.as_string())
