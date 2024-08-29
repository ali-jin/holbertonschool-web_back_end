#!/usr/bin/env python3
"""Unitttests for the clients file"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient Class """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test org """
        mock_get_json.return_value = {"name": org_name}
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client.org, {"name": org_name})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
