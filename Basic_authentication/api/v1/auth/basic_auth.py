#!/usr/bin/env python3
"""
BasicAuth class
"""
import base64
from .auth import Auth
from typing import Tuple


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the base64 encoded authorization header.

        Args:
            authorization_header (str): The authorization header.

        Returns:
            str: The base64 encoded authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a base64-encoded authorization header.

        Args:
            base64_authorization_header (str):The base64-encoded
                    authorization header.

        Returns:
            str: The decoded authorization header as a string,
                    or None if decoding fails.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            message_bytes = base64.b64decode(base64_authorization_header)
            return message_bytes.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extracts the username and password from a decoded base64
            authorization header.

        Args:
            decoded_base64_authorization_header (str): The decoded base64
                authorization header.

        Returns:
            tuple: A tuple containing the username and password extracted
                from the authorization header.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))
