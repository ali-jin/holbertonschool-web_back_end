#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method
        """
        if path is None or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method

        Returns:
            _type_: _description_
        """
        return None

    def session_cookie(self, request=None):
        """ Make the cookie session.

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")

        return request.cookies.get(session_name)
