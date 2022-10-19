# coding: utf-8

"""
    JumpCloud API

    # Overview  JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, and system users.  # API Key  ## Access Your API Key  To locate your API Key:  1. Log into the [JumpCloud Admin Console](https://console.jumpcloud.com/). 2. Go to the username drop down located in the top-right of the Console. 3. Retrieve your API key from API Settings.  ## API Key Considerations  This API key is associated to the currently logged in administrator. Other admins will have different API keys.  **WARNING** Please keep this API key secret, as it grants full access to any data accessible via your JumpCloud console account.  You can also reset your API key in the same location in the JumpCloud Admin Console.  ## Recycling or Resetting Your API Key  In order to revoke access with the current API key, simply reset your API key. This will render all calls using the previous API key inaccessible.  Your API key will be passed in as a header with the header name \"x-api-key\".  ```bash curl -H \"x-api-key: [YOUR_API_KEY_HERE]\" \"https://console.jumpcloud.com/api/systemusers\" ```  # System Context  * [Introduction](#introduction) * [Supported endpoints](#supported-endpoints) * [Response codes](#response-codes) * [Authentication](#authentication) * [Additional examples](#additional-examples) * [Third party](#third-party)  ## Introduction  JumpCloud System Context Authorization is an alternative way to authenticate with a subset of JumpCloud's REST APIs. Using this method, a system can manage its information and resource associations, allowing modern auto provisioning environments to scale as needed.  **Notes:**   * The following documentation applies to Linux Operating Systems only.  * Systems that have been automatically enrolled using Apple's Device Enrollment Program (DEP) or systems enrolled using the User Portal install are not eligible to use the System Context API to prevent unauthorized access to system groups and resources. If a script that utilizes the System Context API is invoked on a system enrolled in this way, it will display an error.  ## Supported Endpoints  JumpCloud System Context Authorization can be used in conjunction with Systems endpoints found in the V1 API and certain System Group endpoints found in the v2 API.  * A system may fetch, alter, and delete metadata about itself, including manipulating a system's Group and Systemuser associations,   * `/api/systems/{system_id}` | [`GET`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_get) [`PUT`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_put) * A system may delete itself from your JumpCloud organization   * `/api/systems/{system_id}` | [`DELETE`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_delete) * A system may fetch its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/memberof` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembership)   * `/api/v2/systems/{system_id}/associations` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsList)   * `/api/v2/systems/{system_id}/users` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemTraverseUser) * A system may alter its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/associations` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsPost) * A system may alter its System Group associations   * `/api/v2/systemgroups/{group_id}/members` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembersPost)     * _NOTE_ If a system attempts to alter the system group membership of a different system the request will be rejected  ## Response Codes  If endpoints other than those described above are called using the System Context API, the server will return a `401` response.  ## Authentication  To allow for secure access to our APIs, you must authenticate each API request. JumpCloud System Context Authorization uses [HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures-00) to authenticate API requests. The HTTP Signatures sent with each request are similar to the signatures used by the Amazon Web Services REST API. To help with the request-signing process, we have provided an [example bash script](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh). This example API request simply requests the entire system record. You must be root, or have permissions to access the contents of the `/opt/jc` directory to generate a signature.  Here is a breakdown of the example script with explanations.  First, the script extracts the systemKey from the JSON formatted `/opt/jc/jcagent.conf` file.  ```bash #!/bin/bash conf=\"`cat /opt/jc/jcagent.conf`\" regex=\"systemKey\\\":\\\"(\\w+)\\\"\"  if [[ $conf =~ $regex ]] ; then   systemKey=\"${BASH_REMATCH[1]}\" fi ```  Then, the script retrieves the current date in the correct format.  ```bash now=`date -u \"+%a, %d %h %Y %H:%M:%S GMT\"`; ```  Next, we build a signing string to demonstrate the expected signature format. The signed string must consist of the [request-line](https://tools.ietf.org/html/rfc2616#page-35) and the date header, separated by a newline character.  ```bash signstr=\"GET /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" ```  The next step is to calculate and apply the signature. This is a two-step process:  1. Create a signature from the signing string using the JumpCloud Agent private key: ``printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key`` 2. Then Base64-encode the signature string and trim off the newline characters: ``| openssl enc -e -a | tr -d '\\n'``  The combined steps above result in:  ```bash signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ; ```  Finally, we make sure the API call sending the signature has the same Authorization and Date header values, HTTP method, and URL that were used in the signing string.  ```bash curl -iq \\   -H \"Accept: application/json\" \\   -H \"Content-Type: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Input Data  All PUT and POST methods should use the HTTP Content-Type header with a value of 'application/json'. PUT methods are used for updating a record. POST methods are used to create a record.  The following example demonstrates how to update the `displayName` of the system.  ```bash signstr=\"PUT /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ;  curl -iq \\   -d \"{\\\"displayName\\\" : \\\"updated-system-name-1\\\"}\" \\   -X \"PUT\" \\   -H \"Content-Type: application/json\" \\   -H \"Accept: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Output Data  All results will be formatted as JSON.  Here is an abbreviated example of response output:  ```json {   \"_id\": \"525ee96f52e144993e000015\",   \"agentServer\": \"lappy386\",   \"agentVersion\": \"0.9.42\",   \"arch\": \"x86_64\",   \"connectionKey\": \"127.0.0.1_51812\",   \"displayName\": \"ubuntu-1204\",   \"firstContact\": \"2013-10-16T19:30:55.611Z\",   \"hostname\": \"ubuntu-1204\"   ... ```  ## Additional Examples  ### Signing Authentication Example  This example demonstrates how to make an authenticated request to fetch the JumpCloud record for this system.  [SigningExample.sh](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh)  ### Shutdown Hook  This example demonstrates how to make an authenticated request on system shutdown. Using an init.d script registered at run level 0, you can call the System Context API as the system is shutting down.  [Instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) is an example of an init.d script that only runs at system shutdown.  After customizing the [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) script, you should install it on the system(s) running the JumpCloud agent.  1. Copy the modified [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) to `/etc/init.d/instance-shutdown`. 2. On Ubuntu systems, run `update-rc.d instance-shutdown defaults`. On RedHat/CentOS systems, run `chkconfig --add instance-shutdown`.  ## Third Party  ### Chef Cookbooks  [https://github.com/nshenry03/jumpcloud](https://github.com/nshenry03/jumpcloud)  [https://github.com/cjs226/jumpcloud](https://github.com/cjs226/jumpcloud)  # Multi-Tenant Portal Headers  Multi-Tenant Organization API Headers are available for JumpCloud Admins to use when making API requests from Organizations that have multiple managed organizations.  The `x-org-id` is a required header for all multi-tenant admins when making API requests to JumpCloud. This header will define to which organization you would like to make the request.  **NOTE** Single Tenant Admins do not need to provide this header when making an API request.  ## Header Value  `x-org-id`  ## API Response Codes  * `400` Malformed ID. * `400` x-org-id and Organization path ID do not match. * `401` ID not included for multi-tenant admin * `403` ID included on unsupported route. * `404` Organization ID Not Found.  ```bash curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -H 'x-org-id: {ORG_ID}'  ```  ## To Obtain an Individual Organization ID via the UI  As a prerequisite, your Primary Organization will need to be setup for Multi-Tenancy. This provides access to the Multi-Tenant Organization Admin Portal.  1. Log into JumpCloud [Admin Console](https://console.jumpcloud.com). If you are a multi-tenant Admin, you will automatically be routed to the Multi-Tenant Admin Portal. 2. From the Multi-Tenant Portal's primary navigation bar, select the Organization you'd like to access. 3. You will automatically be routed to that Organization's Admin Console. 4. Go to Settings in the sub-tenant's primary navigation. 5. You can obtain your Organization ID below your Organization's Contact Information on the Settings page.  ## To Obtain All Organization IDs via the API  * You can make an API request to this endpoint using the API key of your Primary Organization.  `https://console.jumpcloud.com/api/organizations/` This will return all your managed organizations.  ```bash curl -X GET \\   https://console.jumpcloud.com/api/organizations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # SDKs  You can find language specific SDKs that can help you kickstart your Integration with JumpCloud in the following GitHub repositories:  * [Python](https://github.com/TheJumpCloud/jcapi-python) * [Go](https://github.com/TheJumpCloud/jcapi-go) * [Ruby](https://github.com/TheJumpCloud/jcapi-ruby) * [Java](https://github.com/TheJumpCloud/jcapi-java)   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@jumpcloud.com
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
        'schedule_year': 'int',
        'shell': 'str',
        'sudo': 'bool',
        'systems': 'list[str]',
        'template': 'str',
        'time_to_live_seconds': 'int',
        'timeout': 'str',
        'trigger': 'str',
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
        'schedule_year': 'scheduleYear',
        'shell': 'shell',
        'sudo': 'sudo',
        'systems': 'systems',
        'template': 'template',
        'time_to_live_seconds': 'timeToLiveSeconds',
        'timeout': 'timeout',
        'trigger': 'trigger',
        'user': 'user'
    }

    def __init__(self, command=None, command_runners=None, command_type='linux', files=None, launch_type=None, listens_to=None, name=None, organization=None, schedule=None, schedule_repeat_type=None, schedule_year=None, shell=None, sudo=None, systems=None, template=None, time_to_live_seconds=None, timeout=None, trigger=None, user=None):  # noqa: E501
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
        self._schedule_year = None
        self._shell = None
        self._sudo = None
        self._systems = None
        self._template = None
        self._time_to_live_seconds = None
        self._timeout = None
        self._trigger = None
        self._user = None
        self.discriminator = None
        self.command = command
        if command_runners is not None:
            self.command_runners = command_runners
        self.command_type = command_type
        if files is not None:
            self.files = files
        if launch_type is not None:
            self.launch_type = launch_type
        if listens_to is not None:
            self.listens_to = listens_to
        self.name = name
        if organization is not None:
            self.organization = organization
        if schedule is not None:
            self.schedule = schedule
        if schedule_repeat_type is not None:
            self.schedule_repeat_type = schedule_repeat_type
        if schedule_year is not None:
            self.schedule_year = schedule_year
        if shell is not None:
            self.shell = shell
        if sudo is not None:
            self.sudo = sudo
        if systems is not None:
            self.systems = systems
        if template is not None:
            self.template = template
        if time_to_live_seconds is not None:
            self.time_to_live_seconds = time_to_live_seconds
        if timeout is not None:
            self.timeout = timeout
        if trigger is not None:
            self.trigger = trigger
        if user is not None:
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
        if command_type is None:
            raise ValueError("Invalid value for `command_type`, must not be `None`")  # noqa: E501

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


        :return: The listens_to of this Command.  # noqa: E501
        :rtype: str
        """
        return self._listens_to

    @listens_to.setter
    def listens_to(self, listens_to):
        """Sets the listens_to of this Command.


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
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

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
    def schedule_year(self):
        """Gets the schedule_year of this Command.  # noqa: E501

        The year that a scheduled command will launch in.  # noqa: E501

        :return: The schedule_year of this Command.  # noqa: E501
        :rtype: int
        """
        return self._schedule_year

    @schedule_year.setter
    def schedule_year(self, schedule_year):
        """Sets the schedule_year of this Command.

        The year that a scheduled command will launch in.  # noqa: E501

        :param schedule_year: The schedule_year of this Command.  # noqa: E501
        :type: int
        """

        self._schedule_year = schedule_year

    @property
    def shell(self):
        """Gets the shell of this Command.  # noqa: E501

        The shell used to run the command.  # noqa: E501

        :return: The shell of this Command.  # noqa: E501
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this Command.

        The shell used to run the command.  # noqa: E501

        :param shell: The shell of this Command.  # noqa: E501
        :type: str
        """

        self._shell = shell

    @property
    def sudo(self):
        """Gets the sudo of this Command.  # noqa: E501


        :return: The sudo of this Command.  # noqa: E501
        :rtype: bool
        """
        return self._sudo

    @sudo.setter
    def sudo(self, sudo):
        """Sets the sudo of this Command.


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
    def template(self):
        """Gets the template of this Command.  # noqa: E501

        The template this command was created from  # noqa: E501

        :return: The template of this Command.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Command.

        The template this command was created from  # noqa: E501

        :param template: The template of this Command.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def time_to_live_seconds(self):
        """Gets the time_to_live_seconds of this Command.  # noqa: E501

        Time in seconds a command can wait in the queue to be run before timing out  # noqa: E501

        :return: The time_to_live_seconds of this Command.  # noqa: E501
        :rtype: int
        """
        return self._time_to_live_seconds

    @time_to_live_seconds.setter
    def time_to_live_seconds(self, time_to_live_seconds):
        """Sets the time_to_live_seconds of this Command.

        Time in seconds a command can wait in the queue to be run before timing out  # noqa: E501

        :param time_to_live_seconds: The time_to_live_seconds of this Command.  # noqa: E501
        :type: int
        """

        self._time_to_live_seconds = time_to_live_seconds

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
    def trigger(self):
        """Gets the trigger of this Command.  # noqa: E501

        The name of the command trigger.  # noqa: E501

        :return: The trigger of this Command.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Command.

        The name of the command trigger.  # noqa: E501

        :param trigger: The trigger of this Command.  # noqa: E501
        :type: str
        """

        self._trigger = trigger

    @property
    def user(self):
        """Gets the user of this Command.  # noqa: E501

        The ID of the system user to run the command as. This field is required when creating a command with a commandType of \"mac\" or \"linux\".  # noqa: E501

        :return: The user of this Command.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Command.

        The ID of the system user to run the command as. This field is required when creating a command with a commandType of \"mac\" or \"linux\".  # noqa: E501

        :param user: The user of this Command.  # noqa: E501
        :type: str
        """

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
