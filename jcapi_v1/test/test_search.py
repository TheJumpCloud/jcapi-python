# coding: utf-8

"""
    JumpCloud Directory API

    JumpCloud RESTful APIs for the headless operation of core functions

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv1
from jcapiv1.rest import ApiException
from jcapiv1.models.search import Search


class TestSearch(unittest.TestCase):
    """ Search unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearch(self):
        """
        Test Search
        """
        model = jcapiv1.models.search.Search()


if __name__ == '__main__':
    unittest.main()
