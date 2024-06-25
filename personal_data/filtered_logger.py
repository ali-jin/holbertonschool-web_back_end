#!/usr/bin/env python3
"""
A module that returns logs
"""
from typing import List
import re


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

    return(message)
