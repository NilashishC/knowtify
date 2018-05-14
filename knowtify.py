#!/usr/bin/python3

import imaplib
import email

"""

    This class implements Knowtify. For each (email, mobile number) pair
    in the input JSON file, main.py would create an object of this class
    and call the notifier() function.
    ===================================================================
    Copyright (c) 2018 Nilashish Chakraborty

"""


class Knowtify:

    """
        This class implements Knowtify. For each (email, mobile number) pair
        in the input JSON file, main.py would create an object of this class
        and call notifier().
    """

    def __init__(self, host, email, mobile, passwd, mailbox):
        """
            Initializes an object of knowtify class with email and the
            associated mobile number.
        """
        if self.__sanitizeEmail(email):
            if self.__sanitizeMobile(mobile):
                self.__host = host
                self.__email = email
                self.__number = mobile
                self.__passwd = passwd
                self.__mailbox = mailbox
                self.__isValidInput = True
            else:
                # Log invalid mobile
                print('Invalid Mobile')
                self.__isValidInput = False
        else:
            # Log invalid email
            print('Invalid Email')
            self.__isValidInput = False

    def __sanitizeMobile(self, email):
        """
            This function would attempt to check if the extracted email
            from the JSON file is syntactically valid or not.
        """
        return True

    def __sanitizeEmail(self, mobile):
        """
            This function would attempt to check if the extracted number
            from the JSON file is syntactically valid or not.
        """
        return True

    def notifier(self):

        if self.__isValidInput:

            # Log that validation was successful
            print ('Email & Number Validation Successful...')
            rv, unread = 0, 0

            try:
                mail = imaplib.IMAP4_SSL(self.__host)
                mail.login(self.__email, self.__passwd)
                mail.select(self.__mailbox)
                rv, unread = mail.search(None, 'unSeen')

            except imaplib.IMAP4.error as e:
                print("Exception Encountered : {0}".format(e))

            else:
                # Log that 'Login was Successful'
                print('Login Successful...')
                print('---------------------------------------')
                if rv == 'OK':
                    for e_num in unread[0].split():
                        rv, data = mail.fetch(e_num, '(RFC822)')

                        # raw_email = data[0][1]
                        # print(raw_email)
                        email_decoded = data[0][1].decode("utf-8")
                        # print(email_decoded)
                        email_msg = email.message_from_string(email_decoded)
                        # print(email_message)
                        print('FROM : {0}'.format(email_msg['FROM']))
                        print('SUBJECT : {0}'.format(email_msg['SUBJECT']))
                        print('DATE : {0}'.format(email_msg['DATE']))
                        print('----------------------------------------------')
                else:
                    # Log rv was not 'OK'
                    print("RV was not OK")
                    pass

        else:
            # Log that notifier was called but because of validation failure
            # no action was taken
            print("No further action was taken because email or Mobile \
                  validation failed")
