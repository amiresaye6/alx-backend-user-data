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
