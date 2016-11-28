#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import threading


def sendemail():
    user = 'xxx'
    password = 'xxx'
    content = '您好，欢迎来到Python的世界'
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["andy", user])
    msg['To'] = formataddr(['wang', '332850419@qq.com'])
    msg['Subject'] = 'Python测试'

    server = smtplib.SMTP()
    try:
        server.connect('smtp.163.com', 25)
    except Exception as err:
        print('连接失败', err)
        exit()
    else:
        print('连接成功')
    server.starttls()
    server.login(user, password)
    server.sendmail(user, ['332850419@qq.com'], msg.as_string())
    server.quit()


tread = threading.Thread(target=sendemail())
tread.setDaemon(True)
tread.start()
