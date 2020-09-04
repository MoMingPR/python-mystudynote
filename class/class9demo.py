import smtplib
#SMTP ---- simple mail transfer protocol

server.connect(host,post)
#指定连接的邮箱服务器
host:
post:#端口，25
server.login(username,password)
username:
password:#授权码

server.sendmail(sender,to_addr,mag.as_string())

server.quit()

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
MIMEText(msg,type,chartsetutf-8)
#模板