#!/usr/bin/evn python3
"""
This module contains the Auth class which is responsible for managing API
authentication.
"""
from flask import request
from typing import List
from typing import List, TypeVar


class Auth:
    """
    class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Args:
            path (str): The path to check for authentication requirement.
            excluded_paths (List[str]): List of paths that are excluded from
            authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the 'Authorization' header from the request.

        Args:
            request (Request): The Flask request object. Defaults to None.

        Returns:
            str: The value of the 'Authorization' header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.

        Args:
            request (Request): The Flask request object. Defaults to None.

        Returns:
            TypeVar('User'): The current user.
        """
        return None
