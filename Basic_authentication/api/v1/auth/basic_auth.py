#!/usr/bin/env python3
"""
BasicAuth class
"""
from .auth import Auth


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
