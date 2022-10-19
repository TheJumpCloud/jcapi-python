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

class System(object):
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
        'id': 'str',
        'active': 'bool',
        'agent_version': 'str',
        'allow_multi_factor_authentication': 'bool',
        'allow_public_key_authentication': 'bool',
        'allow_ssh_password_authentication': 'bool',
        'allow_ssh_root_login': 'bool',
        'amazon_instance_id': 'str',
        'arch': 'str',
        'azure_ad_joined': 'bool',
        'built_in_commands': 'list[SystemBuiltInCommands]',
        'connection_history': 'list[object]',
        'created': 'datetime',
        'description': 'str',
        'display_manager': 'str',
        'display_name': 'str',
        'domain_info': 'SystemDomainInfo',
        'fde': 'Fde',
        'file_system': 'str',
        'has_service_account': 'bool',
        'hostname': 'str',
        'last_contact': 'datetime',
        'mdm': 'SystemMdm',
        'modify_sshd_config': 'bool',
        'network_interfaces': 'list[SystemNetworkInterfaces]',
        'organization': 'str',
        'os': 'str',
        'os_family': 'str',
        'os_version_detail': 'SystemOsVersionDetail',
        'provision_metadata': 'SystemProvisionMetadata',
        'remote_ip': 'str',
        'serial_number': 'str',
        'service_account_state': 'SystemServiceAccountState',
        'ssh_root_enabled': 'bool',
        'sshd_params': 'list[SystemSshdParams]',
        'system_insights': 'SystemSystemInsights',
        'system_timezone': 'int',
        'tags': 'list[str]',
        'template_name': 'str',
        'user_metrics': 'list[SystemUserMetrics]',
        'version': 'str'
    }

    attribute_map = {
        'id': '_id',
        'active': 'active',
        'agent_version': 'agentVersion',
        'allow_multi_factor_authentication': 'allowMultiFactorAuthentication',
        'allow_public_key_authentication': 'allowPublicKeyAuthentication',
        'allow_ssh_password_authentication': 'allowSshPasswordAuthentication',
        'allow_ssh_root_login': 'allowSshRootLogin',
        'amazon_instance_id': 'amazonInstanceID',
        'arch': 'arch',
        'azure_ad_joined': 'azureAdJoined',
        'built_in_commands': 'builtInCommands',
        'connection_history': 'connectionHistory',
        'created': 'created',
        'description': 'description',
        'display_manager': 'displayManager',
        'display_name': 'displayName',
        'domain_info': 'domainInfo',
        'fde': 'fde',
        'file_system': 'fileSystem',
        'has_service_account': 'hasServiceAccount',
        'hostname': 'hostname',
        'last_contact': 'lastContact',
        'mdm': 'mdm',
        'modify_sshd_config': 'modifySSHDConfig',
        'network_interfaces': 'networkInterfaces',
        'organization': 'organization',
        'os': 'os',
        'os_family': 'osFamily',
        'os_version_detail': 'osVersionDetail',
        'provision_metadata': 'provisionMetadata',
        'remote_ip': 'remoteIP',
        'serial_number': 'serialNumber',
        'service_account_state': 'serviceAccountState',
        'ssh_root_enabled': 'sshRootEnabled',
        'sshd_params': 'sshdParams',
        'system_insights': 'systemInsights',
        'system_timezone': 'systemTimezone',
        'tags': 'tags',
        'template_name': 'templateName',
        'user_metrics': 'userMetrics',
        'version': 'version'
    }

    def __init__(self, id=None, active=None, agent_version=None, allow_multi_factor_authentication=None, allow_public_key_authentication=None, allow_ssh_password_authentication=None, allow_ssh_root_login=None, amazon_instance_id=None, arch=None, azure_ad_joined=None, built_in_commands=None, connection_history=None, created=None, description=None, display_manager=None, display_name=None, domain_info=None, fde=None, file_system=None, has_service_account=None, hostname=None, last_contact=None, mdm=None, modify_sshd_config=None, network_interfaces=None, organization=None, os=None, os_family=None, os_version_detail=None, provision_metadata=None, remote_ip=None, serial_number=None, service_account_state=None, ssh_root_enabled=None, sshd_params=None, system_insights=None, system_timezone=None, tags=None, template_name=None, user_metrics=None, version=None):  # noqa: E501
        """System - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._active = None
        self._agent_version = None
        self._allow_multi_factor_authentication = None
        self._allow_public_key_authentication = None
        self._allow_ssh_password_authentication = None
        self._allow_ssh_root_login = None
        self._amazon_instance_id = None
        self._arch = None
        self._azure_ad_joined = None
        self._built_in_commands = None
        self._connection_history = None
        self._created = None
        self._description = None
        self._display_manager = None
        self._display_name = None
        self._domain_info = None
        self._fde = None
        self._file_system = None
        self._has_service_account = None
        self._hostname = None
        self._last_contact = None
        self._mdm = None
        self._modify_sshd_config = None
        self._network_interfaces = None
        self._organization = None
        self._os = None
        self._os_family = None
        self._os_version_detail = None
        self._provision_metadata = None
        self._remote_ip = None
        self._serial_number = None
        self._service_account_state = None
        self._ssh_root_enabled = None
        self._sshd_params = None
        self._system_insights = None
        self._system_timezone = None
        self._tags = None
        self._template_name = None
        self._user_metrics = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if agent_version is not None:
            self.agent_version = agent_version
        if allow_multi_factor_authentication is not None:
            self.allow_multi_factor_authentication = allow_multi_factor_authentication
        if allow_public_key_authentication is not None:
            self.allow_public_key_authentication = allow_public_key_authentication
        if allow_ssh_password_authentication is not None:
            self.allow_ssh_password_authentication = allow_ssh_password_authentication
        if allow_ssh_root_login is not None:
            self.allow_ssh_root_login = allow_ssh_root_login
        if amazon_instance_id is not None:
            self.amazon_instance_id = amazon_instance_id
        if arch is not None:
            self.arch = arch
        if azure_ad_joined is not None:
            self.azure_ad_joined = azure_ad_joined
        if built_in_commands is not None:
            self.built_in_commands = built_in_commands
        if connection_history is not None:
            self.connection_history = connection_history
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if display_manager is not None:
            self.display_manager = display_manager
        if display_name is not None:
            self.display_name = display_name
        if domain_info is not None:
            self.domain_info = domain_info
        if fde is not None:
            self.fde = fde
        if file_system is not None:
            self.file_system = file_system
        if has_service_account is not None:
            self.has_service_account = has_service_account
        if hostname is not None:
            self.hostname = hostname
        if last_contact is not None:
            self.last_contact = last_contact
        if mdm is not None:
            self.mdm = mdm
        if modify_sshd_config is not None:
            self.modify_sshd_config = modify_sshd_config
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if organization is not None:
            self.organization = organization
        if os is not None:
            self.os = os
        if os_family is not None:
            self.os_family = os_family
        if os_version_detail is not None:
            self.os_version_detail = os_version_detail
        if provision_metadata is not None:
            self.provision_metadata = provision_metadata
        if remote_ip is not None:
            self.remote_ip = remote_ip
        if serial_number is not None:
            self.serial_number = serial_number
        if service_account_state is not None:
            self.service_account_state = service_account_state
        if ssh_root_enabled is not None:
            self.ssh_root_enabled = ssh_root_enabled
        if sshd_params is not None:
            self.sshd_params = sshd_params
        if system_insights is not None:
            self.system_insights = system_insights
        if system_timezone is not None:
            self.system_timezone = system_timezone
        if tags is not None:
            self.tags = tags
        if template_name is not None:
            self.template_name = template_name
        if user_metrics is not None:
            self.user_metrics = user_metrics
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this System.  # noqa: E501


        :return: The id of this System.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this System.


        :param id: The id of this System.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this System.  # noqa: E501


        :return: The active of this System.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this System.


        :param active: The active of this System.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def agent_version(self):
        """Gets the agent_version of this System.  # noqa: E501


        :return: The agent_version of this System.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this System.


        :param agent_version: The agent_version of this System.  # noqa: E501
        :type: str
        """

        self._agent_version = agent_version

    @property
    def allow_multi_factor_authentication(self):
        """Gets the allow_multi_factor_authentication of this System.  # noqa: E501


        :return: The allow_multi_factor_authentication of this System.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multi_factor_authentication

    @allow_multi_factor_authentication.setter
    def allow_multi_factor_authentication(self, allow_multi_factor_authentication):
        """Sets the allow_multi_factor_authentication of this System.


        :param allow_multi_factor_authentication: The allow_multi_factor_authentication of this System.  # noqa: E501
        :type: bool
        """

        self._allow_multi_factor_authentication = allow_multi_factor_authentication

    @property
    def allow_public_key_authentication(self):
        """Gets the allow_public_key_authentication of this System.  # noqa: E501


        :return: The allow_public_key_authentication of this System.  # noqa: E501
        :rtype: bool
        """
        return self._allow_public_key_authentication

    @allow_public_key_authentication.setter
    def allow_public_key_authentication(self, allow_public_key_authentication):
        """Sets the allow_public_key_authentication of this System.


        :param allow_public_key_authentication: The allow_public_key_authentication of this System.  # noqa: E501
        :type: bool
        """

        self._allow_public_key_authentication = allow_public_key_authentication

    @property
    def allow_ssh_password_authentication(self):
        """Gets the allow_ssh_password_authentication of this System.  # noqa: E501


        :return: The allow_ssh_password_authentication of this System.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssh_password_authentication

    @allow_ssh_password_authentication.setter
    def allow_ssh_password_authentication(self, allow_ssh_password_authentication):
        """Sets the allow_ssh_password_authentication of this System.


        :param allow_ssh_password_authentication: The allow_ssh_password_authentication of this System.  # noqa: E501
        :type: bool
        """

        self._allow_ssh_password_authentication = allow_ssh_password_authentication

    @property
    def allow_ssh_root_login(self):
        """Gets the allow_ssh_root_login of this System.  # noqa: E501


        :return: The allow_ssh_root_login of this System.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssh_root_login

    @allow_ssh_root_login.setter
    def allow_ssh_root_login(self, allow_ssh_root_login):
        """Sets the allow_ssh_root_login of this System.


        :param allow_ssh_root_login: The allow_ssh_root_login of this System.  # noqa: E501
        :type: bool
        """

        self._allow_ssh_root_login = allow_ssh_root_login

    @property
    def amazon_instance_id(self):
        """Gets the amazon_instance_id of this System.  # noqa: E501


        :return: The amazon_instance_id of this System.  # noqa: E501
        :rtype: str
        """
        return self._amazon_instance_id

    @amazon_instance_id.setter
    def amazon_instance_id(self, amazon_instance_id):
        """Sets the amazon_instance_id of this System.


        :param amazon_instance_id: The amazon_instance_id of this System.  # noqa: E501
        :type: str
        """

        self._amazon_instance_id = amazon_instance_id

    @property
    def arch(self):
        """Gets the arch of this System.  # noqa: E501


        :return: The arch of this System.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this System.


        :param arch: The arch of this System.  # noqa: E501
        :type: str
        """

        self._arch = arch

    @property
    def azure_ad_joined(self):
        """Gets the azure_ad_joined of this System.  # noqa: E501


        :return: The azure_ad_joined of this System.  # noqa: E501
        :rtype: bool
        """
        return self._azure_ad_joined

    @azure_ad_joined.setter
    def azure_ad_joined(self, azure_ad_joined):
        """Sets the azure_ad_joined of this System.


        :param azure_ad_joined: The azure_ad_joined of this System.  # noqa: E501
        :type: bool
        """

        self._azure_ad_joined = azure_ad_joined

    @property
    def built_in_commands(self):
        """Gets the built_in_commands of this System.  # noqa: E501


        :return: The built_in_commands of this System.  # noqa: E501
        :rtype: list[SystemBuiltInCommands]
        """
        return self._built_in_commands

    @built_in_commands.setter
    def built_in_commands(self, built_in_commands):
        """Sets the built_in_commands of this System.


        :param built_in_commands: The built_in_commands of this System.  # noqa: E501
        :type: list[SystemBuiltInCommands]
        """

        self._built_in_commands = built_in_commands

    @property
    def connection_history(self):
        """Gets the connection_history of this System.  # noqa: E501


        :return: The connection_history of this System.  # noqa: E501
        :rtype: list[object]
        """
        return self._connection_history

    @connection_history.setter
    def connection_history(self, connection_history):
        """Sets the connection_history of this System.


        :param connection_history: The connection_history of this System.  # noqa: E501
        :type: list[object]
        """

        self._connection_history = connection_history

    @property
    def created(self):
        """Gets the created of this System.  # noqa: E501


        :return: The created of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this System.


        :param created: The created of this System.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this System.  # noqa: E501


        :return: The description of this System.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this System.


        :param description: The description of this System.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_manager(self):
        """Gets the display_manager of this System.  # noqa: E501


        :return: The display_manager of this System.  # noqa: E501
        :rtype: str
        """
        return self._display_manager

    @display_manager.setter
    def display_manager(self, display_manager):
        """Sets the display_manager of this System.


        :param display_manager: The display_manager of this System.  # noqa: E501
        :type: str
        """

        self._display_manager = display_manager

    @property
    def display_name(self):
        """Gets the display_name of this System.  # noqa: E501


        :return: The display_name of this System.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this System.


        :param display_name: The display_name of this System.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def domain_info(self):
        """Gets the domain_info of this System.  # noqa: E501


        :return: The domain_info of this System.  # noqa: E501
        :rtype: SystemDomainInfo
        """
        return self._domain_info

    @domain_info.setter
    def domain_info(self, domain_info):
        """Sets the domain_info of this System.


        :param domain_info: The domain_info of this System.  # noqa: E501
        :type: SystemDomainInfo
        """

        self._domain_info = domain_info

    @property
    def fde(self):
        """Gets the fde of this System.  # noqa: E501


        :return: The fde of this System.  # noqa: E501
        :rtype: Fde
        """
        return self._fde

    @fde.setter
    def fde(self, fde):
        """Sets the fde of this System.


        :param fde: The fde of this System.  # noqa: E501
        :type: Fde
        """

        self._fde = fde

    @property
    def file_system(self):
        """Gets the file_system of this System.  # noqa: E501


        :return: The file_system of this System.  # noqa: E501
        :rtype: str
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """Sets the file_system of this System.


        :param file_system: The file_system of this System.  # noqa: E501
        :type: str
        """

        self._file_system = file_system

    @property
    def has_service_account(self):
        """Gets the has_service_account of this System.  # noqa: E501


        :return: The has_service_account of this System.  # noqa: E501
        :rtype: bool
        """
        return self._has_service_account

    @has_service_account.setter
    def has_service_account(self, has_service_account):
        """Sets the has_service_account of this System.


        :param has_service_account: The has_service_account of this System.  # noqa: E501
        :type: bool
        """

        self._has_service_account = has_service_account

    @property
    def hostname(self):
        """Gets the hostname of this System.  # noqa: E501


        :return: The hostname of this System.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this System.


        :param hostname: The hostname of this System.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def last_contact(self):
        """Gets the last_contact of this System.  # noqa: E501


        :return: The last_contact of this System.  # noqa: E501
        :rtype: datetime
        """
        return self._last_contact

    @last_contact.setter
    def last_contact(self, last_contact):
        """Sets the last_contact of this System.


        :param last_contact: The last_contact of this System.  # noqa: E501
        :type: datetime
        """

        self._last_contact = last_contact

    @property
    def mdm(self):
        """Gets the mdm of this System.  # noqa: E501


        :return: The mdm of this System.  # noqa: E501
        :rtype: SystemMdm
        """
        return self._mdm

    @mdm.setter
    def mdm(self, mdm):
        """Sets the mdm of this System.


        :param mdm: The mdm of this System.  # noqa: E501
        :type: SystemMdm
        """

        self._mdm = mdm

    @property
    def modify_sshd_config(self):
        """Gets the modify_sshd_config of this System.  # noqa: E501


        :return: The modify_sshd_config of this System.  # noqa: E501
        :rtype: bool
        """
        return self._modify_sshd_config

    @modify_sshd_config.setter
    def modify_sshd_config(self, modify_sshd_config):
        """Sets the modify_sshd_config of this System.


        :param modify_sshd_config: The modify_sshd_config of this System.  # noqa: E501
        :type: bool
        """

        self._modify_sshd_config = modify_sshd_config

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this System.  # noqa: E501


        :return: The network_interfaces of this System.  # noqa: E501
        :rtype: list[SystemNetworkInterfaces]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this System.


        :param network_interfaces: The network_interfaces of this System.  # noqa: E501
        :type: list[SystemNetworkInterfaces]
        """

        self._network_interfaces = network_interfaces

    @property
    def organization(self):
        """Gets the organization of this System.  # noqa: E501


        :return: The organization of this System.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this System.


        :param organization: The organization of this System.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def os(self):
        """Gets the os of this System.  # noqa: E501


        :return: The os of this System.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this System.


        :param os: The os of this System.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def os_family(self):
        """Gets the os_family of this System.  # noqa: E501


        :return: The os_family of this System.  # noqa: E501
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """Sets the os_family of this System.


        :param os_family: The os_family of this System.  # noqa: E501
        :type: str
        """

        self._os_family = os_family

    @property
    def os_version_detail(self):
        """Gets the os_version_detail of this System.  # noqa: E501


        :return: The os_version_detail of this System.  # noqa: E501
        :rtype: SystemOsVersionDetail
        """
        return self._os_version_detail

    @os_version_detail.setter
    def os_version_detail(self, os_version_detail):
        """Sets the os_version_detail of this System.


        :param os_version_detail: The os_version_detail of this System.  # noqa: E501
        :type: SystemOsVersionDetail
        """

        self._os_version_detail = os_version_detail

    @property
    def provision_metadata(self):
        """Gets the provision_metadata of this System.  # noqa: E501


        :return: The provision_metadata of this System.  # noqa: E501
        :rtype: SystemProvisionMetadata
        """
        return self._provision_metadata

    @provision_metadata.setter
    def provision_metadata(self, provision_metadata):
        """Sets the provision_metadata of this System.


        :param provision_metadata: The provision_metadata of this System.  # noqa: E501
        :type: SystemProvisionMetadata
        """

        self._provision_metadata = provision_metadata

    @property
    def remote_ip(self):
        """Gets the remote_ip of this System.  # noqa: E501


        :return: The remote_ip of this System.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this System.


        :param remote_ip: The remote_ip of this System.  # noqa: E501
        :type: str
        """

        self._remote_ip = remote_ip

    @property
    def serial_number(self):
        """Gets the serial_number of this System.  # noqa: E501


        :return: The serial_number of this System.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this System.


        :param serial_number: The serial_number of this System.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def service_account_state(self):
        """Gets the service_account_state of this System.  # noqa: E501


        :return: The service_account_state of this System.  # noqa: E501
        :rtype: SystemServiceAccountState
        """
        return self._service_account_state

    @service_account_state.setter
    def service_account_state(self, service_account_state):
        """Sets the service_account_state of this System.


        :param service_account_state: The service_account_state of this System.  # noqa: E501
        :type: SystemServiceAccountState
        """

        self._service_account_state = service_account_state

    @property
    def ssh_root_enabled(self):
        """Gets the ssh_root_enabled of this System.  # noqa: E501


        :return: The ssh_root_enabled of this System.  # noqa: E501
        :rtype: bool
        """
        return self._ssh_root_enabled

    @ssh_root_enabled.setter
    def ssh_root_enabled(self, ssh_root_enabled):
        """Sets the ssh_root_enabled of this System.


        :param ssh_root_enabled: The ssh_root_enabled of this System.  # noqa: E501
        :type: bool
        """

        self._ssh_root_enabled = ssh_root_enabled

    @property
    def sshd_params(self):
        """Gets the sshd_params of this System.  # noqa: E501


        :return: The sshd_params of this System.  # noqa: E501
        :rtype: list[SystemSshdParams]
        """
        return self._sshd_params

    @sshd_params.setter
    def sshd_params(self, sshd_params):
        """Sets the sshd_params of this System.


        :param sshd_params: The sshd_params of this System.  # noqa: E501
        :type: list[SystemSshdParams]
        """

        self._sshd_params = sshd_params

    @property
    def system_insights(self):
        """Gets the system_insights of this System.  # noqa: E501


        :return: The system_insights of this System.  # noqa: E501
        :rtype: SystemSystemInsights
        """
        return self._system_insights

    @system_insights.setter
    def system_insights(self, system_insights):
        """Sets the system_insights of this System.


        :param system_insights: The system_insights of this System.  # noqa: E501
        :type: SystemSystemInsights
        """

        self._system_insights = system_insights

    @property
    def system_timezone(self):
        """Gets the system_timezone of this System.  # noqa: E501


        :return: The system_timezone of this System.  # noqa: E501
        :rtype: int
        """
        return self._system_timezone

    @system_timezone.setter
    def system_timezone(self, system_timezone):
        """Sets the system_timezone of this System.


        :param system_timezone: The system_timezone of this System.  # noqa: E501
        :type: int
        """

        self._system_timezone = system_timezone

    @property
    def tags(self):
        """Gets the tags of this System.  # noqa: E501


        :return: The tags of this System.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this System.


        :param tags: The tags of this System.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def template_name(self):
        """Gets the template_name of this System.  # noqa: E501


        :return: The template_name of this System.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this System.


        :param template_name: The template_name of this System.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def user_metrics(self):
        """Gets the user_metrics of this System.  # noqa: E501


        :return: The user_metrics of this System.  # noqa: E501
        :rtype: list[SystemUserMetrics]
        """
        return self._user_metrics

    @user_metrics.setter
    def user_metrics(self, user_metrics):
        """Sets the user_metrics of this System.


        :param user_metrics: The user_metrics of this System.  # noqa: E501
        :type: list[SystemUserMetrics]
        """

        self._user_metrics = user_metrics

    @property
    def version(self):
        """Gets the version of this System.  # noqa: E501


        :return: The version of this System.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this System.


        :param version: The version of this System.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(System, dict):
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
        if not isinstance(other, System):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
