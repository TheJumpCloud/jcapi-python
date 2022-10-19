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

class Organizationsettings(object):
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
        'agent_version': 'str',
        'beta_features': 'object',
        'contact_email': 'str',
        'contact_name': 'str',
        'device_identification_enabled': 'bool',
        'disable_command_runner': 'bool',
        'disable_google_login': 'bool',
        'disable_ldap': 'bool',
        'disable_um': 'bool',
        'display_preferences': 'OrganizationsettingsDisplayPreferences',
        'duplicate_ldap_groups': 'bool',
        'email_disclaimer': 'str',
        'enable_google_apps': 'bool',
        'enable_managed_uid': 'bool',
        'enable_o365': 'bool',
        'enable_user_portal_agent_install': 'bool',
        'features': 'OrganizationsettingsFeatures',
        'growth_data': 'object',
        'logo': 'str',
        'name': 'str',
        'new_system_user_state_defaults': 'OrganizationsettingsNewSystemUserStateDefaults',
        'password_compliance': 'str',
        'password_policy': 'OrganizationsettingsPasswordPolicy',
        'pending_delete': 'bool',
        'show_intro': 'bool',
        'system_user_password_expiration_in_days': 'int',
        'system_users_can_edit': 'bool',
        'system_users_cap': 'int',
        'trusted_app_config': 'TrustedappConfigGet',
        'user_portal': 'OrganizationsettingsUserPortal'
    }

    attribute_map = {
        'agent_version': 'agentVersion',
        'beta_features': 'betaFeatures',
        'contact_email': 'contactEmail',
        'contact_name': 'contactName',
        'device_identification_enabled': 'deviceIdentificationEnabled',
        'disable_command_runner': 'disableCommandRunner',
        'disable_google_login': 'disableGoogleLogin',
        'disable_ldap': 'disableLdap',
        'disable_um': 'disableUM',
        'display_preferences': 'displayPreferences',
        'duplicate_ldap_groups': 'duplicateLDAPGroups',
        'email_disclaimer': 'emailDisclaimer',
        'enable_google_apps': 'enableGoogleApps',
        'enable_managed_uid': 'enableManagedUID',
        'enable_o365': 'enableO365',
        'enable_user_portal_agent_install': 'enableUserPortalAgentInstall',
        'features': 'features',
        'growth_data': 'growthData',
        'logo': 'logo',
        'name': 'name',
        'new_system_user_state_defaults': 'newSystemUserStateDefaults',
        'password_compliance': 'passwordCompliance',
        'password_policy': 'passwordPolicy',
        'pending_delete': 'pendingDelete',
        'show_intro': 'showIntro',
        'system_user_password_expiration_in_days': 'systemUserPasswordExpirationInDays',
        'system_users_can_edit': 'systemUsersCanEdit',
        'system_users_cap': 'systemUsersCap',
        'trusted_app_config': 'trustedAppConfig',
        'user_portal': 'userPortal'
    }

    def __init__(self, agent_version=None, beta_features=None, contact_email=None, contact_name=None, device_identification_enabled=None, disable_command_runner=None, disable_google_login=None, disable_ldap=None, disable_um=None, display_preferences=None, duplicate_ldap_groups=None, email_disclaimer=None, enable_google_apps=None, enable_managed_uid=None, enable_o365=None, enable_user_portal_agent_install=None, features=None, growth_data=None, logo=None, name=None, new_system_user_state_defaults=None, password_compliance=None, password_policy=None, pending_delete=None, show_intro=None, system_user_password_expiration_in_days=None, system_users_can_edit=None, system_users_cap=None, trusted_app_config=None, user_portal=None):  # noqa: E501
        """Organizationsettings - a model defined in Swagger"""  # noqa: E501
        self._agent_version = None
        self._beta_features = None
        self._contact_email = None
        self._contact_name = None
        self._device_identification_enabled = None
        self._disable_command_runner = None
        self._disable_google_login = None
        self._disable_ldap = None
        self._disable_um = None
        self._display_preferences = None
        self._duplicate_ldap_groups = None
        self._email_disclaimer = None
        self._enable_google_apps = None
        self._enable_managed_uid = None
        self._enable_o365 = None
        self._enable_user_portal_agent_install = None
        self._features = None
        self._growth_data = None
        self._logo = None
        self._name = None
        self._new_system_user_state_defaults = None
        self._password_compliance = None
        self._password_policy = None
        self._pending_delete = None
        self._show_intro = None
        self._system_user_password_expiration_in_days = None
        self._system_users_can_edit = None
        self._system_users_cap = None
        self._trusted_app_config = None
        self._user_portal = None
        self.discriminator = None
        if agent_version is not None:
            self.agent_version = agent_version
        if beta_features is not None:
            self.beta_features = beta_features
        if contact_email is not None:
            self.contact_email = contact_email
        if contact_name is not None:
            self.contact_name = contact_name
        if device_identification_enabled is not None:
            self.device_identification_enabled = device_identification_enabled
        if disable_command_runner is not None:
            self.disable_command_runner = disable_command_runner
        if disable_google_login is not None:
            self.disable_google_login = disable_google_login
        if disable_ldap is not None:
            self.disable_ldap = disable_ldap
        if disable_um is not None:
            self.disable_um = disable_um
        if display_preferences is not None:
            self.display_preferences = display_preferences
        if duplicate_ldap_groups is not None:
            self.duplicate_ldap_groups = duplicate_ldap_groups
        if email_disclaimer is not None:
            self.email_disclaimer = email_disclaimer
        if enable_google_apps is not None:
            self.enable_google_apps = enable_google_apps
        if enable_managed_uid is not None:
            self.enable_managed_uid = enable_managed_uid
        if enable_o365 is not None:
            self.enable_o365 = enable_o365
        if enable_user_portal_agent_install is not None:
            self.enable_user_portal_agent_install = enable_user_portal_agent_install
        if features is not None:
            self.features = features
        if growth_data is not None:
            self.growth_data = growth_data
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if new_system_user_state_defaults is not None:
            self.new_system_user_state_defaults = new_system_user_state_defaults
        if password_compliance is not None:
            self.password_compliance = password_compliance
        if password_policy is not None:
            self.password_policy = password_policy
        if pending_delete is not None:
            self.pending_delete = pending_delete
        if show_intro is not None:
            self.show_intro = show_intro
        if system_user_password_expiration_in_days is not None:
            self.system_user_password_expiration_in_days = system_user_password_expiration_in_days
        if system_users_can_edit is not None:
            self.system_users_can_edit = system_users_can_edit
        if system_users_cap is not None:
            self.system_users_cap = system_users_cap
        if trusted_app_config is not None:
            self.trusted_app_config = trusted_app_config
        if user_portal is not None:
            self.user_portal = user_portal

    @property
    def agent_version(self):
        """Gets the agent_version of this Organizationsettings.  # noqa: E501


        :return: The agent_version of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this Organizationsettings.


        :param agent_version: The agent_version of this Organizationsettings.  # noqa: E501
        :type: str
        """

        self._agent_version = agent_version

    @property
    def beta_features(self):
        """Gets the beta_features of this Organizationsettings.  # noqa: E501


        :return: The beta_features of this Organizationsettings.  # noqa: E501
        :rtype: object
        """
        return self._beta_features

    @beta_features.setter
    def beta_features(self, beta_features):
        """Sets the beta_features of this Organizationsettings.


        :param beta_features: The beta_features of this Organizationsettings.  # noqa: E501
        :type: object
        """

        self._beta_features = beta_features

    @property
    def contact_email(self):
        """Gets the contact_email of this Organizationsettings.  # noqa: E501


        :return: The contact_email of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._contact_email

    @contact_email.setter
    def contact_email(self, contact_email):
        """Sets the contact_email of this Organizationsettings.


        :param contact_email: The contact_email of this Organizationsettings.  # noqa: E501
        :type: str
        """

        self._contact_email = contact_email

    @property
    def contact_name(self):
        """Gets the contact_name of this Organizationsettings.  # noqa: E501


        :return: The contact_name of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this Organizationsettings.


        :param contact_name: The contact_name of this Organizationsettings.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def device_identification_enabled(self):
        """Gets the device_identification_enabled of this Organizationsettings.  # noqa: E501


        :return: The device_identification_enabled of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._device_identification_enabled

    @device_identification_enabled.setter
    def device_identification_enabled(self, device_identification_enabled):
        """Sets the device_identification_enabled of this Organizationsettings.


        :param device_identification_enabled: The device_identification_enabled of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._device_identification_enabled = device_identification_enabled

    @property
    def disable_command_runner(self):
        """Gets the disable_command_runner of this Organizationsettings.  # noqa: E501


        :return: The disable_command_runner of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._disable_command_runner

    @disable_command_runner.setter
    def disable_command_runner(self, disable_command_runner):
        """Sets the disable_command_runner of this Organizationsettings.


        :param disable_command_runner: The disable_command_runner of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._disable_command_runner = disable_command_runner

    @property
    def disable_google_login(self):
        """Gets the disable_google_login of this Organizationsettings.  # noqa: E501


        :return: The disable_google_login of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._disable_google_login

    @disable_google_login.setter
    def disable_google_login(self, disable_google_login):
        """Sets the disable_google_login of this Organizationsettings.


        :param disable_google_login: The disable_google_login of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._disable_google_login = disable_google_login

    @property
    def disable_ldap(self):
        """Gets the disable_ldap of this Organizationsettings.  # noqa: E501


        :return: The disable_ldap of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._disable_ldap

    @disable_ldap.setter
    def disable_ldap(self, disable_ldap):
        """Sets the disable_ldap of this Organizationsettings.


        :param disable_ldap: The disable_ldap of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._disable_ldap = disable_ldap

    @property
    def disable_um(self):
        """Gets the disable_um of this Organizationsettings.  # noqa: E501


        :return: The disable_um of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._disable_um

    @disable_um.setter
    def disable_um(self, disable_um):
        """Sets the disable_um of this Organizationsettings.


        :param disable_um: The disable_um of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._disable_um = disable_um

    @property
    def display_preferences(self):
        """Gets the display_preferences of this Organizationsettings.  # noqa: E501


        :return: The display_preferences of this Organizationsettings.  # noqa: E501
        :rtype: OrganizationsettingsDisplayPreferences
        """
        return self._display_preferences

    @display_preferences.setter
    def display_preferences(self, display_preferences):
        """Sets the display_preferences of this Organizationsettings.


        :param display_preferences: The display_preferences of this Organizationsettings.  # noqa: E501
        :type: OrganizationsettingsDisplayPreferences
        """

        self._display_preferences = display_preferences

    @property
    def duplicate_ldap_groups(self):
        """Gets the duplicate_ldap_groups of this Organizationsettings.  # noqa: E501


        :return: The duplicate_ldap_groups of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._duplicate_ldap_groups

    @duplicate_ldap_groups.setter
    def duplicate_ldap_groups(self, duplicate_ldap_groups):
        """Sets the duplicate_ldap_groups of this Organizationsettings.


        :param duplicate_ldap_groups: The duplicate_ldap_groups of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._duplicate_ldap_groups = duplicate_ldap_groups

    @property
    def email_disclaimer(self):
        """Gets the email_disclaimer of this Organizationsettings.  # noqa: E501


        :return: The email_disclaimer of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._email_disclaimer

    @email_disclaimer.setter
    def email_disclaimer(self, email_disclaimer):
        """Sets the email_disclaimer of this Organizationsettings.


        :param email_disclaimer: The email_disclaimer of this Organizationsettings.  # noqa: E501
        :type: str
        """

        self._email_disclaimer = email_disclaimer

    @property
    def enable_google_apps(self):
        """Gets the enable_google_apps of this Organizationsettings.  # noqa: E501


        :return: The enable_google_apps of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_google_apps

    @enable_google_apps.setter
    def enable_google_apps(self, enable_google_apps):
        """Sets the enable_google_apps of this Organizationsettings.


        :param enable_google_apps: The enable_google_apps of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._enable_google_apps = enable_google_apps

    @property
    def enable_managed_uid(self):
        """Gets the enable_managed_uid of this Organizationsettings.  # noqa: E501


        :return: The enable_managed_uid of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_managed_uid

    @enable_managed_uid.setter
    def enable_managed_uid(self, enable_managed_uid):
        """Sets the enable_managed_uid of this Organizationsettings.


        :param enable_managed_uid: The enable_managed_uid of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._enable_managed_uid = enable_managed_uid

    @property
    def enable_o365(self):
        """Gets the enable_o365 of this Organizationsettings.  # noqa: E501


        :return: The enable_o365 of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_o365

    @enable_o365.setter
    def enable_o365(self, enable_o365):
        """Sets the enable_o365 of this Organizationsettings.


        :param enable_o365: The enable_o365 of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._enable_o365 = enable_o365

    @property
    def enable_user_portal_agent_install(self):
        """Gets the enable_user_portal_agent_install of this Organizationsettings.  # noqa: E501


        :return: The enable_user_portal_agent_install of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_user_portal_agent_install

    @enable_user_portal_agent_install.setter
    def enable_user_portal_agent_install(self, enable_user_portal_agent_install):
        """Sets the enable_user_portal_agent_install of this Organizationsettings.


        :param enable_user_portal_agent_install: The enable_user_portal_agent_install of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._enable_user_portal_agent_install = enable_user_portal_agent_install

    @property
    def features(self):
        """Gets the features of this Organizationsettings.  # noqa: E501


        :return: The features of this Organizationsettings.  # noqa: E501
        :rtype: OrganizationsettingsFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Organizationsettings.


        :param features: The features of this Organizationsettings.  # noqa: E501
        :type: OrganizationsettingsFeatures
        """

        self._features = features

    @property
    def growth_data(self):
        """Gets the growth_data of this Organizationsettings.  # noqa: E501

        Object containing Optimizely experimentIds and states corresponding to them  # noqa: E501

        :return: The growth_data of this Organizationsettings.  # noqa: E501
        :rtype: object
        """
        return self._growth_data

    @growth_data.setter
    def growth_data(self, growth_data):
        """Sets the growth_data of this Organizationsettings.

        Object containing Optimizely experimentIds and states corresponding to them  # noqa: E501

        :param growth_data: The growth_data of this Organizationsettings.  # noqa: E501
        :type: object
        """

        self._growth_data = growth_data

    @property
    def logo(self):
        """Gets the logo of this Organizationsettings.  # noqa: E501


        :return: The logo of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Organizationsettings.


        :param logo: The logo of this Organizationsettings.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this Organizationsettings.  # noqa: E501


        :return: The name of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organizationsettings.


        :param name: The name of this Organizationsettings.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def new_system_user_state_defaults(self):
        """Gets the new_system_user_state_defaults of this Organizationsettings.  # noqa: E501


        :return: The new_system_user_state_defaults of this Organizationsettings.  # noqa: E501
        :rtype: OrganizationsettingsNewSystemUserStateDefaults
        """
        return self._new_system_user_state_defaults

    @new_system_user_state_defaults.setter
    def new_system_user_state_defaults(self, new_system_user_state_defaults):
        """Sets the new_system_user_state_defaults of this Organizationsettings.


        :param new_system_user_state_defaults: The new_system_user_state_defaults of this Organizationsettings.  # noqa: E501
        :type: OrganizationsettingsNewSystemUserStateDefaults
        """

        self._new_system_user_state_defaults = new_system_user_state_defaults

    @property
    def password_compliance(self):
        """Gets the password_compliance of this Organizationsettings.  # noqa: E501


        :return: The password_compliance of this Organizationsettings.  # noqa: E501
        :rtype: str
        """
        return self._password_compliance

    @password_compliance.setter
    def password_compliance(self, password_compliance):
        """Sets the password_compliance of this Organizationsettings.


        :param password_compliance: The password_compliance of this Organizationsettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["custom", "pci3", "windows"]  # noqa: E501
        if password_compliance not in allowed_values:
            raise ValueError(
                "Invalid value for `password_compliance` ({0}), must be one of {1}"  # noqa: E501
                .format(password_compliance, allowed_values)
            )

        self._password_compliance = password_compliance

    @property
    def password_policy(self):
        """Gets the password_policy of this Organizationsettings.  # noqa: E501


        :return: The password_policy of this Organizationsettings.  # noqa: E501
        :rtype: OrganizationsettingsPasswordPolicy
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """Sets the password_policy of this Organizationsettings.


        :param password_policy: The password_policy of this Organizationsettings.  # noqa: E501
        :type: OrganizationsettingsPasswordPolicy
        """

        self._password_policy = password_policy

    @property
    def pending_delete(self):
        """Gets the pending_delete of this Organizationsettings.  # noqa: E501


        :return: The pending_delete of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._pending_delete

    @pending_delete.setter
    def pending_delete(self, pending_delete):
        """Sets the pending_delete of this Organizationsettings.


        :param pending_delete: The pending_delete of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._pending_delete = pending_delete

    @property
    def show_intro(self):
        """Gets the show_intro of this Organizationsettings.  # noqa: E501


        :return: The show_intro of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_intro

    @show_intro.setter
    def show_intro(self, show_intro):
        """Sets the show_intro of this Organizationsettings.


        :param show_intro: The show_intro of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._show_intro = show_intro

    @property
    def system_user_password_expiration_in_days(self):
        """Gets the system_user_password_expiration_in_days of this Organizationsettings.  # noqa: E501


        :return: The system_user_password_expiration_in_days of this Organizationsettings.  # noqa: E501
        :rtype: int
        """
        return self._system_user_password_expiration_in_days

    @system_user_password_expiration_in_days.setter
    def system_user_password_expiration_in_days(self, system_user_password_expiration_in_days):
        """Sets the system_user_password_expiration_in_days of this Organizationsettings.


        :param system_user_password_expiration_in_days: The system_user_password_expiration_in_days of this Organizationsettings.  # noqa: E501
        :type: int
        """

        self._system_user_password_expiration_in_days = system_user_password_expiration_in_days

    @property
    def system_users_can_edit(self):
        """Gets the system_users_can_edit of this Organizationsettings.  # noqa: E501


        :return: The system_users_can_edit of this Organizationsettings.  # noqa: E501
        :rtype: bool
        """
        return self._system_users_can_edit

    @system_users_can_edit.setter
    def system_users_can_edit(self, system_users_can_edit):
        """Sets the system_users_can_edit of this Organizationsettings.


        :param system_users_can_edit: The system_users_can_edit of this Organizationsettings.  # noqa: E501
        :type: bool
        """

        self._system_users_can_edit = system_users_can_edit

    @property
    def system_users_cap(self):
        """Gets the system_users_cap of this Organizationsettings.  # noqa: E501


        :return: The system_users_cap of this Organizationsettings.  # noqa: E501
        :rtype: int
        """
        return self._system_users_cap

    @system_users_cap.setter
    def system_users_cap(self, system_users_cap):
        """Sets the system_users_cap of this Organizationsettings.


        :param system_users_cap: The system_users_cap of this Organizationsettings.  # noqa: E501
        :type: int
        """

        self._system_users_cap = system_users_cap

    @property
    def trusted_app_config(self):
        """Gets the trusted_app_config of this Organizationsettings.  # noqa: E501


        :return: The trusted_app_config of this Organizationsettings.  # noqa: E501
        :rtype: TrustedappConfigGet
        """
        return self._trusted_app_config

    @trusted_app_config.setter
    def trusted_app_config(self, trusted_app_config):
        """Sets the trusted_app_config of this Organizationsettings.


        :param trusted_app_config: The trusted_app_config of this Organizationsettings.  # noqa: E501
        :type: TrustedappConfigGet
        """

        self._trusted_app_config = trusted_app_config

    @property
    def user_portal(self):
        """Gets the user_portal of this Organizationsettings.  # noqa: E501


        :return: The user_portal of this Organizationsettings.  # noqa: E501
        :rtype: OrganizationsettingsUserPortal
        """
        return self._user_portal

    @user_portal.setter
    def user_portal(self, user_portal):
        """Sets the user_portal of this Organizationsettings.


        :param user_portal: The user_portal of this Organizationsettings.  # noqa: E501
        :type: OrganizationsettingsUserPortal
        """

        self._user_portal = user_portal

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
        if issubclass(Organizationsettings, dict):
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
        if not isinstance(other, Organizationsettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
