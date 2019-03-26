# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv2
from jcapiv2.api.active_directory_api import ActiveDirectoryApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestActiveDirectoryApi(unittest.TestCase):
    """ActiveDirectoryApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.active_directory_api.ActiveDirectoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activedirectories_agents_list(self):
        """Test case for activedirectories_agents_list

        List Active Directory Agents  # noqa: E501
        """
        pass

    def test_activedirectories_agents_post(self):
        """Test case for activedirectories_agents_post

        Create a new Active Directory Agent  # noqa: E501
        """
        pass

    def test_activedirectories_delete(self):
        """Test case for activedirectories_delete

        Delete an Active Directory  # noqa: E501
        """
        pass

    def test_activedirectories_get(self):
        """Test case for activedirectories_get

        Get an Active Directory  # noqa: E501
        """
        pass

    def test_activedirectories_list(self):
        """Test case for activedirectories_list

        List Active Directories  # noqa: E501
        """
        pass

    def test_activedirectories_post(self):
        """Test case for activedirectories_post

        Create a new Active Directory  # noqa: E501
        """
        pass

    def test_graph_active_directory_associations_list(self):
        """Test case for graph_active_directory_associations_list

        List the associations of an Active Directory instance  # noqa: E501
        """
        pass

    def test_graph_active_directory_associations_post(self):
        """Test case for graph_active_directory_associations_post

        Manage the associations of an Active Directory instance  # noqa: E501
        """
        pass

    def test_graph_active_directory_traverse_user_group(self):
        """Test case for graph_active_directory_traverse_user_group

        List the User Groups bound to an Active Directory instance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
