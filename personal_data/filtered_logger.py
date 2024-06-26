#!/usr/bin/env python3
"""
A module that returns logs
"""

from typing import List
import re
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

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
    fields: List[str], redaction: str, message: str, separator: str
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


def get_logger() -> logging.Logger:
    """
    Create and return a logging.Logger object.

    Returns:
        logging.Logger: The created logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Create and return a MySQL connection.

    Returns:
        mysql.connector.connection.MySQLConnection: The MySQL connection.
    """
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        user=db_username, password=db_password, host=db_host, database=db_name
    )


def main():
    """
    Main function of the script.

    Returns:
        None
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    logger = get_logger()
    for row in cursor:
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; " + \
            f"ssn={row[3]}; password={row[4]}; ip={row[5]}; last_login=" + \
            f"{row[6]}; user_agent={row[7]};"
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
