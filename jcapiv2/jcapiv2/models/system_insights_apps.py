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


class SystemInsightsApps(object):
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
        'name': 'str',
        'path': 'str',
        'bundle_executable': 'str',
        'bundle_identifier': 'str',
        'bundle_name': 'str',
        'bundle_short_version': 'str',
        'bundle_version': 'str',
        'bundle_package_type': 'str',
        'environment': 'str',
        'element': 'str',
        'compiler': 'str',
        'development_region': 'str',
        'display_name': 'str',
        'info_string': 'str',
        'minimum_system_version': 'str',
        'category': 'str',
        'applescript_enabled': 'str',
        'copyright': 'str',
        'last_opened_time': 'float',
        'jc_collection_time': 'str',
        'jc_system_id': 'str',
        'jc_organization_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'bundle_executable': 'bundle_executable',
        'bundle_identifier': 'bundle_identifier',
        'bundle_name': 'bundle_name',
        'bundle_short_version': 'bundle_short_version',
        'bundle_version': 'bundle_version',
        'bundle_package_type': 'bundle_package_type',
        'environment': 'environment',
        'element': 'element',
        'compiler': 'compiler',
        'development_region': 'development_region',
        'display_name': 'display_name',
        'info_string': 'info_string',
        'minimum_system_version': 'minimum_system_version',
        'category': 'category',
        'applescript_enabled': 'applescript_enabled',
        'copyright': 'copyright',
        'last_opened_time': 'last_opened_time',
        'jc_collection_time': 'jc_collection_time',
        'jc_system_id': 'jc_system_id',
        'jc_organization_id': 'jc_organization_id'
    }

    def __init__(self, name=None, path=None, bundle_executable=None, bundle_identifier=None, bundle_name=None, bundle_short_version=None, bundle_version=None, bundle_package_type=None, environment=None, element=None, compiler=None, development_region=None, display_name=None, info_string=None, minimum_system_version=None, category=None, applescript_enabled=None, copyright=None, last_opened_time=None, jc_collection_time=None, jc_system_id=None, jc_organization_id=None):  # noqa: E501
        """SystemInsightsApps - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._path = None
        self._bundle_executable = None
        self._bundle_identifier = None
        self._bundle_name = None
        self._bundle_short_version = None
        self._bundle_version = None
        self._bundle_package_type = None
        self._environment = None
        self._element = None
        self._compiler = None
        self._development_region = None
        self._display_name = None
        self._info_string = None
        self._minimum_system_version = None
        self._category = None
        self._applescript_enabled = None
        self._copyright = None
        self._last_opened_time = None
        self._jc_collection_time = None
        self._jc_system_id = None
        self._jc_organization_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if bundle_executable is not None:
            self.bundle_executable = bundle_executable
        if bundle_identifier is not None:
            self.bundle_identifier = bundle_identifier
        if bundle_name is not None:
            self.bundle_name = bundle_name
        if bundle_short_version is not None:
            self.bundle_short_version = bundle_short_version
        if bundle_version is not None:
            self.bundle_version = bundle_version
        if bundle_package_type is not None:
            self.bundle_package_type = bundle_package_type
        if environment is not None:
            self.environment = environment
        if element is not None:
            self.element = element
        if compiler is not None:
            self.compiler = compiler
        if development_region is not None:
            self.development_region = development_region
        if display_name is not None:
            self.display_name = display_name
        if info_string is not None:
            self.info_string = info_string
        if minimum_system_version is not None:
            self.minimum_system_version = minimum_system_version
        if category is not None:
            self.category = category
        if applescript_enabled is not None:
            self.applescript_enabled = applescript_enabled
        if copyright is not None:
            self.copyright = copyright
        if last_opened_time is not None:
            self.last_opened_time = last_opened_time
        if jc_collection_time is not None:
            self.jc_collection_time = jc_collection_time
        if jc_system_id is not None:
            self.jc_system_id = jc_system_id
        if jc_organization_id is not None:
            self.jc_organization_id = jc_organization_id

    @property
    def name(self):
        """Gets the name of this SystemInsightsApps.  # noqa: E501


        :return: The name of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsApps.


        :param name: The name of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SystemInsightsApps.  # noqa: E501


        :return: The path of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsApps.


        :param path: The path of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def bundle_executable(self):
        """Gets the bundle_executable of this SystemInsightsApps.  # noqa: E501


        :return: The bundle_executable of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_executable

    @bundle_executable.setter
    def bundle_executable(self, bundle_executable):
        """Sets the bundle_executable of this SystemInsightsApps.


        :param bundle_executable: The bundle_executable of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._bundle_executable = bundle_executable

    @property
    def bundle_identifier(self):
        """Gets the bundle_identifier of this SystemInsightsApps.  # noqa: E501


        :return: The bundle_identifier of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_identifier

    @bundle_identifier.setter
    def bundle_identifier(self, bundle_identifier):
        """Sets the bundle_identifier of this SystemInsightsApps.


        :param bundle_identifier: The bundle_identifier of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._bundle_identifier = bundle_identifier

    @property
    def bundle_name(self):
        """Gets the bundle_name of this SystemInsightsApps.  # noqa: E501


        :return: The bundle_name of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, bundle_name):
        """Sets the bundle_name of this SystemInsightsApps.


        :param bundle_name: The bundle_name of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._bundle_name = bundle_name

    @property
    def bundle_short_version(self):
        """Gets the bundle_short_version of this SystemInsightsApps.  # noqa: E501


        :return: The bundle_short_version of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_short_version

    @bundle_short_version.setter
    def bundle_short_version(self, bundle_short_version):
        """Sets the bundle_short_version of this SystemInsightsApps.


        :param bundle_short_version: The bundle_short_version of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._bundle_short_version = bundle_short_version

    @property
    def bundle_version(self):
        """Gets the bundle_version of this SystemInsightsApps.  # noqa: E501


        :return: The bundle_version of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_version

    @bundle_version.setter
    def bundle_version(self, bundle_version):
        """Sets the bundle_version of this SystemInsightsApps.


        :param bundle_version: The bundle_version of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._bundle_version = bundle_version

    @property
    def bundle_package_type(self):
        """Gets the bundle_package_type of this SystemInsightsApps.  # noqa: E501


        :return: The bundle_package_type of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_package_type

    @bundle_package_type.setter
    def bundle_package_type(self, bundle_package_type):
        """Sets the bundle_package_type of this SystemInsightsApps.


        :param bundle_package_type: The bundle_package_type of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._bundle_package_type = bundle_package_type

    @property
    def environment(self):
        """Gets the environment of this SystemInsightsApps.  # noqa: E501


        :return: The environment of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this SystemInsightsApps.


        :param environment: The environment of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._environment = environment

    @property
    def element(self):
        """Gets the element of this SystemInsightsApps.  # noqa: E501


        :return: The element of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._element

    @element.setter
    def element(self, element):
        """Sets the element of this SystemInsightsApps.


        :param element: The element of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._element = element

    @property
    def compiler(self):
        """Gets the compiler of this SystemInsightsApps.  # noqa: E501


        :return: The compiler of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._compiler

    @compiler.setter
    def compiler(self, compiler):
        """Sets the compiler of this SystemInsightsApps.


        :param compiler: The compiler of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._compiler = compiler

    @property
    def development_region(self):
        """Gets the development_region of this SystemInsightsApps.  # noqa: E501


        :return: The development_region of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._development_region

    @development_region.setter
    def development_region(self, development_region):
        """Sets the development_region of this SystemInsightsApps.


        :param development_region: The development_region of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._development_region = development_region

    @property
    def display_name(self):
        """Gets the display_name of this SystemInsightsApps.  # noqa: E501


        :return: The display_name of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SystemInsightsApps.


        :param display_name: The display_name of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def info_string(self):
        """Gets the info_string of this SystemInsightsApps.  # noqa: E501


        :return: The info_string of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._info_string

    @info_string.setter
    def info_string(self, info_string):
        """Sets the info_string of this SystemInsightsApps.


        :param info_string: The info_string of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._info_string = info_string

    @property
    def minimum_system_version(self):
        """Gets the minimum_system_version of this SystemInsightsApps.  # noqa: E501


        :return: The minimum_system_version of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._minimum_system_version

    @minimum_system_version.setter
    def minimum_system_version(self, minimum_system_version):
        """Sets the minimum_system_version of this SystemInsightsApps.


        :param minimum_system_version: The minimum_system_version of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._minimum_system_version = minimum_system_version

    @property
    def category(self):
        """Gets the category of this SystemInsightsApps.  # noqa: E501


        :return: The category of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SystemInsightsApps.


        :param category: The category of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def applescript_enabled(self):
        """Gets the applescript_enabled of this SystemInsightsApps.  # noqa: E501


        :return: The applescript_enabled of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._applescript_enabled

    @applescript_enabled.setter
    def applescript_enabled(self, applescript_enabled):
        """Sets the applescript_enabled of this SystemInsightsApps.


        :param applescript_enabled: The applescript_enabled of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._applescript_enabled = applescript_enabled

    @property
    def copyright(self):
        """Gets the copyright of this SystemInsightsApps.  # noqa: E501


        :return: The copyright of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this SystemInsightsApps.


        :param copyright: The copyright of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def last_opened_time(self):
        """Gets the last_opened_time of this SystemInsightsApps.  # noqa: E501


        :return: The last_opened_time of this SystemInsightsApps.  # noqa: E501
        :rtype: float
        """
        return self._last_opened_time

    @last_opened_time.setter
    def last_opened_time(self, last_opened_time):
        """Sets the last_opened_time of this SystemInsightsApps.


        :param last_opened_time: The last_opened_time of this SystemInsightsApps.  # noqa: E501
        :type: float
        """

        self._last_opened_time = last_opened_time

    @property
    def jc_collection_time(self):
        """Gets the jc_collection_time of this SystemInsightsApps.  # noqa: E501


        :return: The jc_collection_time of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._jc_collection_time

    @jc_collection_time.setter
    def jc_collection_time(self, jc_collection_time):
        """Sets the jc_collection_time of this SystemInsightsApps.


        :param jc_collection_time: The jc_collection_time of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._jc_collection_time = jc_collection_time

    @property
    def jc_system_id(self):
        """Gets the jc_system_id of this SystemInsightsApps.  # noqa: E501


        :return: The jc_system_id of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._jc_system_id

    @jc_system_id.setter
    def jc_system_id(self, jc_system_id):
        """Sets the jc_system_id of this SystemInsightsApps.


        :param jc_system_id: The jc_system_id of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._jc_system_id = jc_system_id

    @property
    def jc_organization_id(self):
        """Gets the jc_organization_id of this SystemInsightsApps.  # noqa: E501


        :return: The jc_organization_id of this SystemInsightsApps.  # noqa: E501
        :rtype: str
        """
        return self._jc_organization_id

    @jc_organization_id.setter
    def jc_organization_id(self, jc_organization_id):
        """Sets the jc_organization_id of this SystemInsightsApps.


        :param jc_organization_id: The jc_organization_id of this SystemInsightsApps.  # noqa: E501
        :type: str
        """

        self._jc_organization_id = jc_organization_id

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
        if issubclass(SystemInsightsApps, dict):
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
        if not isinstance(other, SystemInsightsApps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
