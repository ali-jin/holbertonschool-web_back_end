#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Verify if path is in the excluded paths list

        Args:
            path (str): The path to verify
            excluded_paths (List[str]): The list of excluded paths

        Returns:
            bool: boolean respnse
        """
        if path is None or not excluded_paths:
            return True

        path = path + '/' if path[-1] != '/' else path

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Returns:
            _type_: _description_
        """
        return None
