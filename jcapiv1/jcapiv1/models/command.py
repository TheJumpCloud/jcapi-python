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


class Command(object):
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
        'command': 'str',
        'command_runners': 'list[str]',
        'command_type': 'str',
        'files': 'list[str]',
        'launch_type': 'str',
        'listens_to': 'str',
        'name': 'str',
        'organization': 'str',
        'schedule': 'str',
        'schedule_repeat_type': 'str',
        'sudo': 'bool',
        'systems': 'list[str]',
        'timeout': 'str',
        'user': 'str'
    }

    attribute_map = {
        'command': 'command',
        'command_runners': 'commandRunners',
        'command_type': 'commandType',
        'files': 'files',
        'launch_type': 'launchType',
        'listens_to': 'listensTo',
        'name': 'name',
        'organization': 'organization',
        'schedule': 'schedule',
        'schedule_repeat_type': 'scheduleRepeatType',
        'sudo': 'sudo',
        'systems': 'systems',
        'timeout': 'timeout',
        'user': 'user'
    }

    def __init__(self, command=None, command_runners=None, command_type=None, files=None, launch_type=None, listens_to=None, name=None, organization=None, schedule=None, schedule_repeat_type=None, sudo=None, systems=None, timeout=None, user=None):  # noqa: E501
        """Command - a model defined in Swagger"""  # noqa: E501

        self._command = None
        self._command_runners = None
        self._command_type = None
        self._files = None
        self._launch_type = None
        self._listens_to = None
        self._name = None
        self._organization = None
        self._schedule = None
        self._schedule_repeat_type = None
        self._sudo = None
        self._systems = None
        self._timeout = None
        self._user = None
        self.discriminator = None

        self.command = command
        if command_runners is not None:
            self.command_runners = command_runners
        if command_type is not None:
            self.command_type = command_type
        if files is not None:
            self.files = files
        if launch_type is not None:
            self.launch_type = launch_type
        if listens_to is not None:
            self.listens_to = listens_to
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if schedule is not None:
            self.schedule = schedule
        if schedule_repeat_type is not None:
            self.schedule_repeat_type = schedule_repeat_type
        if sudo is not None:
            self.sudo = sudo
        if systems is not None:
            self.systems = systems
        if timeout is not None:
            self.timeout = timeout
        self.user = user

    @property
    def command(self):
        """Gets the command of this Command.  # noqa: E501

        The command to execute on the server.  # noqa: E501

        :return: The command of this Command.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this Command.

        The command to execute on the server.  # noqa: E501

        :param command: The command of this Command.  # noqa: E501
        :type: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def command_runners(self):
        """Gets the command_runners of this Command.  # noqa: E501

        An array of IDs of the Command Runner Users that can execute this command.  # noqa: E501

        :return: The command_runners of this Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._command_runners

    @command_runners.setter
    def command_runners(self, command_runners):
        """Sets the command_runners of this Command.

        An array of IDs of the Command Runner Users that can execute this command.  # noqa: E501

        :param command_runners: The command_runners of this Command.  # noqa: E501
        :type: list[str]
        """

        self._command_runners = command_runners

    @property
    def command_type(self):
        """Gets the command_type of this Command.  # noqa: E501

        The Command OS  # noqa: E501

        :return: The command_type of this Command.  # noqa: E501
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this Command.

        The Command OS  # noqa: E501

        :param command_type: The command_type of this Command.  # noqa: E501
        :type: str
        """

        self._command_type = command_type

    @property
    def files(self):
        """Gets the files of this Command.  # noqa: E501

        An array of file IDs to include with the command.  # noqa: E501

        :return: The files of this Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Command.

        An array of file IDs to include with the command.  # noqa: E501

        :param files: The files of this Command.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def launch_type(self):
        """Gets the launch_type of this Command.  # noqa: E501

        How the command will execute.  # noqa: E501

        :return: The launch_type of this Command.  # noqa: E501
        :rtype: str
        """
        return self._launch_type

    @launch_type.setter
    def launch_type(self, launch_type):
        """Sets the launch_type of this Command.

        How the command will execute.  # noqa: E501

        :param launch_type: The launch_type of this Command.  # noqa: E501
        :type: str
        """

        self._launch_type = launch_type

    @property
    def listens_to(self):
        """Gets the listens_to of this Command.  # noqa: E501

          # noqa: E501

        :return: The listens_to of this Command.  # noqa: E501
        :rtype: str
        """
        return self._listens_to

    @listens_to.setter
    def listens_to(self, listens_to):
        """Sets the listens_to of this Command.

          # noqa: E501

        :param listens_to: The listens_to of this Command.  # noqa: E501
        :type: str
        """

        self._listens_to = listens_to

    @property
    def name(self):
        """Gets the name of this Command.  # noqa: E501


        :return: The name of this Command.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Command.


        :param name: The name of this Command.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this Command.  # noqa: E501

        The ID of the organization.  # noqa: E501

        :return: The organization of this Command.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Command.

        The ID of the organization.  # noqa: E501

        :param organization: The organization of this Command.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def schedule(self):
        """Gets the schedule of this Command.  # noqa: E501

        A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately.   # noqa: E501

        :return: The schedule of this Command.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Command.

        A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately.   # noqa: E501

        :param schedule: The schedule of this Command.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def schedule_repeat_type(self):
        """Gets the schedule_repeat_type of this Command.  # noqa: E501

        When the command will repeat.  # noqa: E501

        :return: The schedule_repeat_type of this Command.  # noqa: E501
        :rtype: str
        """
        return self._schedule_repeat_type

    @schedule_repeat_type.setter
    def schedule_repeat_type(self, schedule_repeat_type):
        """Sets the schedule_repeat_type of this Command.

        When the command will repeat.  # noqa: E501

        :param schedule_repeat_type: The schedule_repeat_type of this Command.  # noqa: E501
        :type: str
        """

        self._schedule_repeat_type = schedule_repeat_type

    @property
    def sudo(self):
        """Gets the sudo of this Command.  # noqa: E501

          # noqa: E501

        :return: The sudo of this Command.  # noqa: E501
        :rtype: bool
        """
        return self._sudo

    @sudo.setter
    def sudo(self, sudo):
        """Sets the sudo of this Command.

          # noqa: E501

        :param sudo: The sudo of this Command.  # noqa: E501
        :type: bool
        """

        self._sudo = sudo

    @property
    def systems(self):
        """Gets the systems of this Command.  # noqa: E501

        An array of system IDs to run the command on. Not available if you are using Groups.  # noqa: E501

        :return: The systems of this Command.  # noqa: E501
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this Command.

        An array of system IDs to run the command on. Not available if you are using Groups.  # noqa: E501

        :param systems: The systems of this Command.  # noqa: E501
        :type: list[str]
        """

        self._systems = systems

    @property
    def timeout(self):
        """Gets the timeout of this Command.  # noqa: E501

        The time in seconds to allow the command to run for.  # noqa: E501

        :return: The timeout of this Command.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Command.

        The time in seconds to allow the command to run for.  # noqa: E501

        :param timeout: The timeout of this Command.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def user(self):
        """Gets the user of this Command.  # noqa: E501

        The ID of the system user to run the command as.  # noqa: E501

        :return: The user of this Command.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Command.

        The ID of the system user to run the command as.  # noqa: E501

        :param user: The user of this Command.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(Command, dict):
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
        if not isinstance(other, Command):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
