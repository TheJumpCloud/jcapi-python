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


class SystemInsightsSystemControls(object):
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
        'collection_time': 'str',
        'config_value': 'str',
        'current_value': 'str',
        'field_name': 'str',
        'name': 'str',
        'oid': 'str',
        'subsystem': 'str',
        'system_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'config_value': 'config_value',
        'current_value': 'current_value',
        'field_name': 'field_name',
        'name': 'name',
        'oid': 'oid',
        'subsystem': 'subsystem',
        'system_id': 'system_id',
        'type': 'type'
    }

    def __init__(self, collection_time=None, config_value=None, current_value=None, field_name=None, name=None, oid=None, subsystem=None, system_id=None, type=None):  # noqa: E501
        """SystemInsightsSystemControls - a model defined in Swagger"""  # noqa: E501

        self._collection_time = None
        self._config_value = None
        self._current_value = None
        self._field_name = None
        self._name = None
        self._oid = None
        self._subsystem = None
        self._system_id = None
        self._type = None
        self.discriminator = None

        if collection_time is not None:
            self.collection_time = collection_time
        if config_value is not None:
            self.config_value = config_value
        if current_value is not None:
            self.current_value = current_value
        if field_name is not None:
            self.field_name = field_name
        if name is not None:
            self.name = name
        if oid is not None:
            self.oid = oid
        if subsystem is not None:
            self.subsystem = subsystem
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsSystemControls.  # noqa: E501


        :return: The collection_time of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsSystemControls.


        :param collection_time: The collection_time of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def config_value(self):
        """Gets the config_value of this SystemInsightsSystemControls.  # noqa: E501


        :return: The config_value of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        """Sets the config_value of this SystemInsightsSystemControls.


        :param config_value: The config_value of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._config_value = config_value

    @property
    def current_value(self):
        """Gets the current_value of this SystemInsightsSystemControls.  # noqa: E501


        :return: The current_value of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this SystemInsightsSystemControls.


        :param current_value: The current_value of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._current_value = current_value

    @property
    def field_name(self):
        """Gets the field_name of this SystemInsightsSystemControls.  # noqa: E501


        :return: The field_name of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this SystemInsightsSystemControls.


        :param field_name: The field_name of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def name(self):
        """Gets the name of this SystemInsightsSystemControls.  # noqa: E501


        :return: The name of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsSystemControls.


        :param name: The name of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oid(self):
        """Gets the oid of this SystemInsightsSystemControls.  # noqa: E501


        :return: The oid of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this SystemInsightsSystemControls.


        :param oid: The oid of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def subsystem(self):
        """Gets the subsystem of this SystemInsightsSystemControls.  # noqa: E501


        :return: The subsystem of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._subsystem

    @subsystem.setter
    def subsystem(self, subsystem):
        """Sets the subsystem of this SystemInsightsSystemControls.


        :param subsystem: The subsystem of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._subsystem = subsystem

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsSystemControls.  # noqa: E501


        :return: The system_id of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsSystemControls.


        :param system_id: The system_id of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this SystemInsightsSystemControls.  # noqa: E501


        :return: The type of this SystemInsightsSystemControls.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsSystemControls.


        :param type: The type of this SystemInsightsSystemControls.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(SystemInsightsSystemControls, dict):
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
        if not isinstance(other, SystemInsightsSystemControls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
