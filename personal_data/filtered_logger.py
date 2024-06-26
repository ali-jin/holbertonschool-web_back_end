#!/usr/bin/env python3
"""
A module that returns logs
"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialisation

        Args:
            fields (List[str]): list of fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the logs record

        Args:
            record (logging.LogRecord): logs record to be formatted

        Returns:
            str: The formatted message
        """
        format_message = super().format(record)

        return filter_datum(self.fields,
                            self.REDACTION,
                            format_message,
                            self.SEPARATOR)


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """Replace occurrences of certain field values

    Args:
        fields (List[str]): list of fields to obfuscate
        redaction (str): string by what the field will be obfuscated
        message (str): string representing the log line
        separator (str): character is separating all fields in the log line

    Returns:
        str: _description_
    """
    for field in fields:
        pattern = f"{field}=[^;]*?{separator}"
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)

    return message
