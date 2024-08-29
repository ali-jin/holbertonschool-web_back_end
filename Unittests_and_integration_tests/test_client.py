#!/usr/bin/env python3
"""Unitttests for the clients file"""
import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test _public_repos_url """
        org_name = "google"
        repo_url = f"https://api.github.com/orgs/{org_name}"
        mock_org.return_value = {"repos_url": repo_url}
        github_org_client = GithubOrgClient(org_name)
        self.assertEqual(github_org_client._public_repos_url, repo_url)
