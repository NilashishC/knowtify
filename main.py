#!/usr/bin/python3

import knowtify
from time import sleep


"""

    This tool is aimed to notify a user of any new emails via SMS
    ===================================================================
    Copyright (c) 2018 Nilashish Chakraborty

"""

if __name__ == '__main__':
    # Read host, email, mobile, password, mailbox from a JSON file
    # Create a new object of type knowtify for each entry
    # Call notifier() on each object

    obj = knowtify.Knowtify('imap.gmail.com', 'nilashishc.social@gmail.com',
                            '8017535758', 'Badsha*2018fm', 'Inbox')
    print("Starting Service....")
    while True:
        obj.notifier()
        sleep(60)
