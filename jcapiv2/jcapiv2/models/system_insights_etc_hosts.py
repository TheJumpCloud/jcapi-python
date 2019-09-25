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


class SystemInsightsEtcHosts(object):
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
        'address': 'str',
        'collection_time': 'str',
        'hostnames': 'str',
        'system_id': 'str'
    }

    attribute_map = {
        'address': 'address',
        'collection_time': 'collection_time',
        'hostnames': 'hostnames',
        'system_id': 'system_id'
    }

    def __init__(self, address=None, collection_time=None, hostnames=None, system_id=None):  # noqa: E501
        """SystemInsightsEtcHosts - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._collection_time = None
        self._hostnames = None
        self._system_id = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if collection_time is not None:
            self.collection_time = collection_time
        if hostnames is not None:
            self.hostnames = hostnames
        if system_id is not None:
            self.system_id = system_id

    @property
    def address(self):
        """Gets the address of this SystemInsightsEtcHosts.  # noqa: E501


        :return: The address of this SystemInsightsEtcHosts.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SystemInsightsEtcHosts.


        :param address: The address of this SystemInsightsEtcHosts.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsEtcHosts.  # noqa: E501


        :return: The collection_time of this SystemInsightsEtcHosts.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsEtcHosts.


        :param collection_time: The collection_time of this SystemInsightsEtcHosts.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def hostnames(self):
        """Gets the hostnames of this SystemInsightsEtcHosts.  # noqa: E501


        :return: The hostnames of this SystemInsightsEtcHosts.  # noqa: E501
        :rtype: str
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """Sets the hostnames of this SystemInsightsEtcHosts.


        :param hostnames: The hostnames of this SystemInsightsEtcHosts.  # noqa: E501
        :type: str
        """

        self._hostnames = hostnames

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsEtcHosts.  # noqa: E501


        :return: The system_id of this SystemInsightsEtcHosts.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsEtcHosts.


        :param system_id: The system_id of this SystemInsightsEtcHosts.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

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
        if issubclass(SystemInsightsEtcHosts, dict):
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
        if not isinstance(other, SystemInsightsEtcHosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
