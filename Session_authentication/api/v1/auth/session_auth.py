#!/usr/bin/env python3
"""
SessionAuth class
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id.

        Args:
            user_id (str, optional): The user id.

        Returns:
            str: The session id.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns User ID based on a Session ID.

        Args:
            session_id (str, optional): The id of the session.

        Returns:
            str: The value of the for the key session_id.
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
