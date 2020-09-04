import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from_addr = ''
password = ''
#to_addr = ['','']
to_addr = []
while True:
    a = input('收件人邮箱：')
    to_addrs.append(a)
    b = input('是否，n代表退出，任意键:')
    if b == 'n':
        break
print(to_addrs)

smtp_server = ''

msg = MIMEMultipart()
att = MIMEText(open('').read(),'plain','utf-8')
att['Content-Disposition'] = 'attachment; filename = "python_test"'
msg.attach(att)

msg = MIMEText('send by Python,what do you think?','plain','utf-8')
msg['From'] = Header('')
msg['To'] = Header('')
msg['Subject'] = Header()

server = smtplib.SMTP()
server.connect(smtp_server,25)

server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())

server.quit()