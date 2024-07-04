#!/usr/bin/env python3
"""
filter datum module using re and logging
"""
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(r'({}=)[^{}]+'.format(field, separator),
                         r'\1{}'.format(redaction), message)
    return message


# # test
# fields = ["password", "date_of_birth", 'email']
# messages = [
# "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
# "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
#     ]

# for message in messages:
#     print(filter_datum(fields, 'xxx', message, ';'))
