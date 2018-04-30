#!/usr/bin/python3

import imaplib
import email
import getpass
import time


"""

    This tool is aimed to notify a user of any new emails via SMS
    ===================================================================
    Copyright (c) 2018 Nilashish Chakraborty

"""


def runService():
    mail.select('Inbox')
    rv, unread = mail.search(None, 'unSeen')

    if rv != 'OK':
        print("Error")

    for e_num in unread[0].split():
        rv, data = mail.fetch(e_num, '(RFC822)')

        # raw_email = data[0][1]
        # print(raw_email)
        email_decoded = data[0][1].decode("utf-8")
        # print(email_decoded)
        email_message = email.message_from_string(email_decoded)
        # print(email_message)
        print('FROM : {0}'.format(email_message['FROM']))
        print('SUBJECT : {0}'.format(email_message['SUBJECT']))
        print('DATE : {0}'.format(email_message['DATE']))
        print('--------------------------------------------------')


if __name__ == '__main__':

    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    mail.login(input('Email Id: '), getpass.getpass())

    print('Fetching unread emails....')
    print('*********************************************************')

    while True:
        runService()
        time.sleep(60)
