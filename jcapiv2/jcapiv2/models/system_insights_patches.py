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


class SystemInsightsPatches(object):
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
        'caption': 'str',
        'collection_time': 'str',
        'csname': 'str',
        'description': 'str',
        'fix_comments': 'str',
        'hotfix_id': 'str',
        'install_date': 'str',
        'installed_by': 'str',
        'installed_on': 'str',
        'system_id': 'str'
    }

    attribute_map = {
        'caption': 'caption',
        'collection_time': 'collection_time',
        'csname': 'csname',
        'description': 'description',
        'fix_comments': 'fix_comments',
        'hotfix_id': 'hotfix_id',
        'install_date': 'install_date',
        'installed_by': 'installed_by',
        'installed_on': 'installed_on',
        'system_id': 'system_id'
    }

    def __init__(self, caption=None, collection_time=None, csname=None, description=None, fix_comments=None, hotfix_id=None, install_date=None, installed_by=None, installed_on=None, system_id=None):  # noqa: E501
        """SystemInsightsPatches - a model defined in Swagger"""  # noqa: E501

        self._caption = None
        self._collection_time = None
        self._csname = None
        self._description = None
        self._fix_comments = None
        self._hotfix_id = None
        self._install_date = None
        self._installed_by = None
        self._installed_on = None
        self._system_id = None
        self.discriminator = None

        if caption is not None:
            self.caption = caption
        if collection_time is not None:
            self.collection_time = collection_time
        if csname is not None:
            self.csname = csname
        if description is not None:
            self.description = description
        if fix_comments is not None:
            self.fix_comments = fix_comments
        if hotfix_id is not None:
            self.hotfix_id = hotfix_id
        if install_date is not None:
            self.install_date = install_date
        if installed_by is not None:
            self.installed_by = installed_by
        if installed_on is not None:
            self.installed_on = installed_on
        if system_id is not None:
            self.system_id = system_id

    @property
    def caption(self):
        """Gets the caption of this SystemInsightsPatches.  # noqa: E501


        :return: The caption of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this SystemInsightsPatches.


        :param caption: The caption of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsPatches.  # noqa: E501


        :return: The collection_time of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsPatches.


        :param collection_time: The collection_time of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def csname(self):
        """Gets the csname of this SystemInsightsPatches.  # noqa: E501


        :return: The csname of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._csname

    @csname.setter
    def csname(self, csname):
        """Sets the csname of this SystemInsightsPatches.


        :param csname: The csname of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._csname = csname

    @property
    def description(self):
        """Gets the description of this SystemInsightsPatches.  # noqa: E501


        :return: The description of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemInsightsPatches.


        :param description: The description of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def fix_comments(self):
        """Gets the fix_comments of this SystemInsightsPatches.  # noqa: E501


        :return: The fix_comments of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._fix_comments

    @fix_comments.setter
    def fix_comments(self, fix_comments):
        """Sets the fix_comments of this SystemInsightsPatches.


        :param fix_comments: The fix_comments of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._fix_comments = fix_comments

    @property
    def hotfix_id(self):
        """Gets the hotfix_id of this SystemInsightsPatches.  # noqa: E501


        :return: The hotfix_id of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._hotfix_id

    @hotfix_id.setter
    def hotfix_id(self, hotfix_id):
        """Sets the hotfix_id of this SystemInsightsPatches.


        :param hotfix_id: The hotfix_id of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._hotfix_id = hotfix_id

    @property
    def install_date(self):
        """Gets the install_date of this SystemInsightsPatches.  # noqa: E501


        :return: The install_date of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._install_date

    @install_date.setter
    def install_date(self, install_date):
        """Sets the install_date of this SystemInsightsPatches.


        :param install_date: The install_date of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._install_date = install_date

    @property
    def installed_by(self):
        """Gets the installed_by of this SystemInsightsPatches.  # noqa: E501


        :return: The installed_by of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._installed_by

    @installed_by.setter
    def installed_by(self, installed_by):
        """Sets the installed_by of this SystemInsightsPatches.


        :param installed_by: The installed_by of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._installed_by = installed_by

    @property
    def installed_on(self):
        """Gets the installed_on of this SystemInsightsPatches.  # noqa: E501


        :return: The installed_on of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._installed_on

    @installed_on.setter
    def installed_on(self, installed_on):
        """Sets the installed_on of this SystemInsightsPatches.


        :param installed_on: The installed_on of this SystemInsightsPatches.  # noqa: E501
        :type: str
        """

        self._installed_on = installed_on

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsPatches.  # noqa: E501


        :return: The system_id of this SystemInsightsPatches.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsPatches.


        :param system_id: The system_id of this SystemInsightsPatches.  # noqa: E501
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
        if issubclass(SystemInsightsPatches, dict):
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
        if not isinstance(other, SystemInsightsPatches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other