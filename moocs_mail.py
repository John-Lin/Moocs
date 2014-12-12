# -*- coding: utf-8 -*-
import smtplib
import csv
import time

subject = "【2014計算機網路概論 - NTHU MOOCs 清華大學磨課師課程】"
bcc = ['xxxx@gmail.com']
text = '''同學您好：

感謝您修習本學期的 【NTHU MOOCs 清華大學磨課師課程 - 2014計算機網路概論】

在此恭喜您以優異的成績通過本課程，並且將獲得「清華大學磨課師課程」給予的修課證書乙張

「請回信告訴我們您的真實姓名」以方便我們製作證書

證書是在線上以下載形式發放，請密切注意平台訊息！



國立清華大學 高速網路實驗室 助教群 敬上'''


def get_mail_list(fileobj):
    mail_list = []
    for row in csv.reader(fileobj):
        if row[1] != '':
            mail_list.append(row[1])
    fileobj.close()
    return mail_list


def send_email(subject, text, bcc):
    gmail_user = "Gmail_address"
    gmail_pwd = "Gmail_password"
    FROM = 'Gmail_address'
    BCC = bcc
    # must be a list
    TO = []
    SUBJECT = subject
    TEXT = text

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, BCC, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


if __name__ == '__main__':
    f1 = open('pass_mail_list.csv')
    pass_mail_list = get_mail_list(f1)
    group_one = pass_mail_list[0:90]
    group_two = pass_mail_list[90:180]
    group_three = pass_mail_list[180:270]
    group_four = pass_mail_list[270:360]
    group_five = pass_mail_list[360:450]
    group_six = pass_mail_list[450:]

    # print len(group_one)
    # print len(group_two)
    # print len(group_three)
    # print len(group_four)
    # print len(group_five)
    # print len(group_six)
    # print len(pass_mail_list)

    pass_group = [group_one, group_two, group_three,
                  group_four, group_five, group_six]
    counter = 0
    for item in pass_group:
        counter += 1
        print "Group %d :" % (counter)
        print item
        send_email(subject, text, item)
        time.sleep(60)

    # send_email(subject, text, bcc)
