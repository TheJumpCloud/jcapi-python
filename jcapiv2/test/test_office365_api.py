# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv2
from jcapiv2.rest import ApiException
from jcapiv2.apis.office365_api import Office365Api


class TestOffice365Api(unittest.TestCase):
    """ Office365Api unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.office365_api.Office365Api()

    def tearDown(self):
        pass

    def test_graph_office365_associations_list(self):
        """
        Test case for graph_office365_associations_list

        List the associations of an Office 365 instance
        """
        pass

    def test_graph_office365_associations_post(self):
        """
        Test case for graph_office365_associations_post

        Manage the associations of an Office 365 instance
        """
        pass

    def test_graph_office365_traverse_user(self):
        """
        Test case for graph_office365_traverse_user

        List the Users bound to an Office 365 instance
        """
        pass

    def test_graph_office365_traverse_user_group(self):
        """
        Test case for graph_office365_traverse_user_group

        List the User Groups bound to an Office 365 instance
        """
        pass


if __name__ == '__main__':
    unittest.main()
