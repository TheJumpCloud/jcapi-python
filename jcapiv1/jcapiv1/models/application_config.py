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

from jcapiv1.models.application_config_acs_url import ApplicationConfigAcsUrl  # noqa: F401,E501
from jcapiv1.models.application_config_constant_attributes import ApplicationConfigConstantAttributes  # noqa: F401,E501
from jcapiv1.models.application_config_database_attributes import ApplicationConfigDatabaseAttributes  # noqa: F401,E501


class ApplicationConfig(object):
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
        'acs_url': 'ApplicationConfigAcsUrl',
        'constant_attributes': 'ApplicationConfigConstantAttributes',
        'database_attributes': 'ApplicationConfigDatabaseAttributes',
        'idp_certificate': 'ApplicationConfigAcsUrl',
        'idp_entity_id': 'ApplicationConfigAcsUrl',
        'sp_entity_id': 'ApplicationConfigAcsUrl'
    }

    attribute_map = {
        'acs_url': 'acsUrl',
        'constant_attributes': 'constantAttributes',
        'database_attributes': 'databaseAttributes',
        'idp_certificate': 'idpCertificate',
        'idp_entity_id': 'idpEntityId',
        'sp_entity_id': 'spEntityId'
    }

    def __init__(self, acs_url=None, constant_attributes=None, database_attributes=None, idp_certificate=None, idp_entity_id=None, sp_entity_id=None):  # noqa: E501
        """ApplicationConfig - a model defined in Swagger"""  # noqa: E501

        self._acs_url = None
        self._constant_attributes = None
        self._database_attributes = None
        self._idp_certificate = None
        self._idp_entity_id = None
        self._sp_entity_id = None
        self.discriminator = None

        if acs_url is not None:
            self.acs_url = acs_url
        if constant_attributes is not None:
            self.constant_attributes = constant_attributes
        if database_attributes is not None:
            self.database_attributes = database_attributes
        if idp_certificate is not None:
            self.idp_certificate = idp_certificate
        if idp_entity_id is not None:
            self.idp_entity_id = idp_entity_id
        if sp_entity_id is not None:
            self.sp_entity_id = sp_entity_id

    @property
    def acs_url(self):
        """Gets the acs_url of this ApplicationConfig.  # noqa: E501


        :return: The acs_url of this ApplicationConfig.  # noqa: E501
        :rtype: ApplicationConfigAcsUrl
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """Sets the acs_url of this ApplicationConfig.


        :param acs_url: The acs_url of this ApplicationConfig.  # noqa: E501
        :type: ApplicationConfigAcsUrl
        """

        self._acs_url = acs_url

    @property
    def constant_attributes(self):
        """Gets the constant_attributes of this ApplicationConfig.  # noqa: E501


        :return: The constant_attributes of this ApplicationConfig.  # noqa: E501
        :rtype: ApplicationConfigConstantAttributes
        """
        return self._constant_attributes

    @constant_attributes.setter
    def constant_attributes(self, constant_attributes):
        """Sets the constant_attributes of this ApplicationConfig.


        :param constant_attributes: The constant_attributes of this ApplicationConfig.  # noqa: E501
        :type: ApplicationConfigConstantAttributes
        """

        self._constant_attributes = constant_attributes

    @property
    def database_attributes(self):
        """Gets the database_attributes of this ApplicationConfig.  # noqa: E501


        :return: The database_attributes of this ApplicationConfig.  # noqa: E501
        :rtype: ApplicationConfigDatabaseAttributes
        """
        return self._database_attributes

    @database_attributes.setter
    def database_attributes(self, database_attributes):
        """Sets the database_attributes of this ApplicationConfig.


        :param database_attributes: The database_attributes of this ApplicationConfig.  # noqa: E501
        :type: ApplicationConfigDatabaseAttributes
        """

        self._database_attributes = database_attributes

    @property
    def idp_certificate(self):
        """Gets the idp_certificate of this ApplicationConfig.  # noqa: E501


        :return: The idp_certificate of this ApplicationConfig.  # noqa: E501
        :rtype: ApplicationConfigAcsUrl
        """
        return self._idp_certificate

    @idp_certificate.setter
    def idp_certificate(self, idp_certificate):
        """Sets the idp_certificate of this ApplicationConfig.


        :param idp_certificate: The idp_certificate of this ApplicationConfig.  # noqa: E501
        :type: ApplicationConfigAcsUrl
        """

        self._idp_certificate = idp_certificate

    @property
    def idp_entity_id(self):
        """Gets the idp_entity_id of this ApplicationConfig.  # noqa: E501


        :return: The idp_entity_id of this ApplicationConfig.  # noqa: E501
        :rtype: ApplicationConfigAcsUrl
        """
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, idp_entity_id):
        """Sets the idp_entity_id of this ApplicationConfig.


        :param idp_entity_id: The idp_entity_id of this ApplicationConfig.  # noqa: E501
        :type: ApplicationConfigAcsUrl
        """

        self._idp_entity_id = idp_entity_id

    @property
    def sp_entity_id(self):
        """Gets the sp_entity_id of this ApplicationConfig.  # noqa: E501


        :return: The sp_entity_id of this ApplicationConfig.  # noqa: E501
        :rtype: ApplicationConfigAcsUrl
        """
        return self._sp_entity_id

    @sp_entity_id.setter
    def sp_entity_id(self, sp_entity_id):
        """Sets the sp_entity_id of this ApplicationConfig.


        :param sp_entity_id: The sp_entity_id of this ApplicationConfig.  # noqa: E501
        :type: ApplicationConfigAcsUrl
        """

        self._sp_entity_id = sp_entity_id

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
        if issubclass(ApplicationConfig, dict):
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
        if not isinstance(other, ApplicationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
