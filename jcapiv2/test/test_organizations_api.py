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
from jcapiv2.api.organizations_api import OrganizationsApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.organizations_api.OrganizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_org_crypto_get(self):
        """Test case for org_crypto_get

        Get Crypto Settings  # noqa: E501
        """
        pass

    def test_org_crypto_put(self):
        """Test case for org_crypto_put

        Edit Crypto Settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()