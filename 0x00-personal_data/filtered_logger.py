#!/usr/bin/env python3
"""
filter datum module using re and logging
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record by obfuscating specified fields.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message with specified fields obfuscated.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


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
