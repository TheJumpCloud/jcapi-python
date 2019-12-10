# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jcapiv1.models.organization import Organization  # noqa: F401,E501


class InlineResponse2001(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'organization': 'Organization',
        'provider': 'str'
    }

    attribute_map = {
        'organization': 'organization',
        'provider': 'provider'
    }

    def __init__(self, organization=None, provider=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501

        self._organization = None
        self._provider = None
        self.discriminator = None

        if organization is not None:
            self.organization = organization
        if provider is not None:
            self.provider = provider

    @property
    def organization(self):
        """Gets the organization of this InlineResponse2001.  # noqa: E501


        :return: The organization of this InlineResponse2001.  # noqa: E501
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this InlineResponse2001.


        :param organization: The organization of this InlineResponse2001.  # noqa: E501
        :type: Organization
        """

        self._organization = organization

    @property
    def provider(self):
        """Gets the provider of this InlineResponse2001.  # noqa: E501


        :return: The provider of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this InlineResponse2001.


        :param provider: The provider of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._provider = provider

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2001, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
