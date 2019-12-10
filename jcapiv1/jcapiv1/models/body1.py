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


class Body1(object):
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
        'mfa': 'str',
        'name': 'str',
        'network_source_ip': 'str',
        'tags': 'list[str]',
        'user_lockout_action': 'str',
        'user_password_expiration_action': 'str'
    }

    attribute_map = {
        'mfa': 'mfa',
        'name': 'name',
        'network_source_ip': 'networkSourceIp',
        'tags': 'tags',
        'user_lockout_action': 'userLockoutAction',
        'user_password_expiration_action': 'userPasswordExpirationAction'
    }

    def __init__(self, mfa=None, name=None, network_source_ip=None, tags=None, user_lockout_action=None, user_password_expiration_action=None):  # noqa: E501
        """Body1 - a model defined in Swagger"""  # noqa: E501

        self._mfa = None
        self._name = None
        self._network_source_ip = None
        self._tags = None
        self._user_lockout_action = None
        self._user_password_expiration_action = None
        self.discriminator = None

        if mfa is not None:
            self.mfa = mfa
        self.name = name
        self.network_source_ip = network_source_ip
        if tags is not None:
            self.tags = tags
        if user_lockout_action is not None:
            self.user_lockout_action = user_lockout_action
        if user_password_expiration_action is not None:
            self.user_password_expiration_action = user_password_expiration_action

    @property
    def mfa(self):
        """Gets the mfa of this Body1.  # noqa: E501


        :return: The mfa of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._mfa

    @mfa.setter
    def mfa(self, mfa):
        """Sets the mfa of this Body1.


        :param mfa: The mfa of this Body1.  # noqa: E501
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "REQUIRED", "ALWAYS"]  # noqa: E501
        if mfa not in allowed_values:
            raise ValueError(
                "Invalid value for `mfa` ({0}), must be one of {1}"  # noqa: E501
                .format(mfa, allowed_values)
            )

        self._mfa = mfa

    @property
    def name(self):
        """Gets the name of this Body1.  # noqa: E501


        :return: The name of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body1.


        :param name: The name of this Body1.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def network_source_ip(self):
        """Gets the network_source_ip of this Body1.  # noqa: E501


        :return: The network_source_ip of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._network_source_ip

    @network_source_ip.setter
    def network_source_ip(self, network_source_ip):
        """Sets the network_source_ip of this Body1.


        :param network_source_ip: The network_source_ip of this Body1.  # noqa: E501
        :type: str
        """
        if network_source_ip is None:
            raise ValueError("Invalid value for `network_source_ip`, must not be `None`")  # noqa: E501

        self._network_source_ip = network_source_ip

    @property
    def tags(self):
        """Gets the tags of this Body1.  # noqa: E501


        :return: The tags of this Body1.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Body1.


        :param tags: The tags of this Body1.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def user_lockout_action(self):
        """Gets the user_lockout_action of this Body1.  # noqa: E501


        :return: The user_lockout_action of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._user_lockout_action

    @user_lockout_action.setter
    def user_lockout_action(self, user_lockout_action):
        """Sets the user_lockout_action of this Body1.


        :param user_lockout_action: The user_lockout_action of this Body1.  # noqa: E501
        :type: str
        """

        self._user_lockout_action = user_lockout_action

    @property
    def user_password_expiration_action(self):
        """Gets the user_password_expiration_action of this Body1.  # noqa: E501


        :return: The user_password_expiration_action of this Body1.  # noqa: E501
        :rtype: str
        """
        return self._user_password_expiration_action

    @user_password_expiration_action.setter
    def user_password_expiration_action(self, user_password_expiration_action):
        """Sets the user_password_expiration_action of this Body1.


        :param user_password_expiration_action: The user_password_expiration_action of this Body1.  # noqa: E501
        :type: str
        """

        self._user_password_expiration_action = user_password_expiration_action

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
        if issubclass(Body1, dict):
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
        if not isinstance(other, Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
