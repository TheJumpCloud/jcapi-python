# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Mfa(object):
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
        'exclusion': 'bool',
        'exclusion_until': 'datetime',
        'configured': 'bool'
    }

    attribute_map = {
        'exclusion': 'exclusion',
        'exclusion_until': 'exclusionUntil',
        'configured': 'configured'
    }

    def __init__(self, exclusion=None, exclusion_until=None, configured=None):  # noqa: E501
        """Mfa - a model defined in Swagger"""  # noqa: E501

        self._exclusion = None
        self._exclusion_until = None
        self._configured = None
        self.discriminator = None

        if exclusion is not None:
            self.exclusion = exclusion
        if exclusion_until is not None:
            self.exclusion_until = exclusion_until
        if configured is not None:
            self.configured = configured

    @property
    def exclusion(self):
        """Gets the exclusion of this Mfa.  # noqa: E501


        :return: The exclusion of this Mfa.  # noqa: E501
        :rtype: bool
        """
        return self._exclusion

    @exclusion.setter
    def exclusion(self, exclusion):
        """Sets the exclusion of this Mfa.


        :param exclusion: The exclusion of this Mfa.  # noqa: E501
        :type: bool
        """

        self._exclusion = exclusion

    @property
    def exclusion_until(self):
        """Gets the exclusion_until of this Mfa.  # noqa: E501


        :return: The exclusion_until of this Mfa.  # noqa: E501
        :rtype: datetime
        """
        return self._exclusion_until

    @exclusion_until.setter
    def exclusion_until(self, exclusion_until):
        """Sets the exclusion_until of this Mfa.


        :param exclusion_until: The exclusion_until of this Mfa.  # noqa: E501
        :type: datetime
        """

        self._exclusion_until = exclusion_until

    @property
    def configured(self):
        """Gets the configured of this Mfa.  # noqa: E501


        :return: The configured of this Mfa.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this Mfa.


        :param configured: The configured of this Mfa.  # noqa: E501
        :type: bool
        """

        self._configured = configured

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
        if issubclass(Mfa, dict):
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
        if not isinstance(other, Mfa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other