#!/usr/bin/env python3
"""
filter datum module using re and logging
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): A list of strings representing the fields to be
        obfuscated.
        redaction (str): The string used for obfuscation.
        message (str): The log message to be filtered.
        separator (str): The separator used to separate the fields in the log
        message.

    Returns:
        str: The filtered log message with specified fields obfuscated.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
