#!/usr/bin/env python3
""" Module for implementing a hash_password function """

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the given password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The hashed password.
    """
    password_bytes = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password
