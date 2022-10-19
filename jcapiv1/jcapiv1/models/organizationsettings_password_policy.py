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

class OrganizationsettingsPasswordPolicy(object):
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
        'allow_username_substring': 'bool',
        'days_after_expiration_to_self_recover': 'int',
        'days_before_expiration_to_force_reset': 'int',
        'effective_date': 'str',
        'enable_days_after_expiration_to_self_recover': 'bool',
        'enable_days_before_expiration_to_force_reset': 'bool',
        'enable_lockout_time_in_seconds': 'bool',
        'enable_max_history': 'bool',
        'enable_max_login_attempts': 'bool',
        'enable_min_change_period_in_days': 'bool',
        'enable_min_length': 'bool',
        'enable_password_expiration_in_days': 'bool',
        'enable_recovery_email': 'bool',
        'enable_reset_lockout_counter': 'bool',
        'grace_period_date': 'str',
        'lockout_time_in_seconds': 'int',
        'max_history': 'int',
        'max_login_attempts': 'int',
        'min_change_period_in_days': 'int',
        'min_length': 'int',
        'needs_lowercase': 'bool',
        'needs_numeric': 'bool',
        'needs_symbolic': 'bool',
        'needs_uppercase': 'bool',
        'password_expiration_in_days': 'int',
        'reset_lockout_counter_minutes': 'int'
    }

    attribute_map = {
        'allow_username_substring': 'allowUsernameSubstring',
        'days_after_expiration_to_self_recover': 'daysAfterExpirationToSelfRecover',
        'days_before_expiration_to_force_reset': 'daysBeforeExpirationToForceReset',
        'effective_date': 'effectiveDate',
        'enable_days_after_expiration_to_self_recover': 'enableDaysAfterExpirationToSelfRecover',
        'enable_days_before_expiration_to_force_reset': 'enableDaysBeforeExpirationToForceReset',
        'enable_lockout_time_in_seconds': 'enableLockoutTimeInSeconds',
        'enable_max_history': 'enableMaxHistory',
        'enable_max_login_attempts': 'enableMaxLoginAttempts',
        'enable_min_change_period_in_days': 'enableMinChangePeriodInDays',
        'enable_min_length': 'enableMinLength',
        'enable_password_expiration_in_days': 'enablePasswordExpirationInDays',
        'enable_recovery_email': 'enableRecoveryEmail',
        'enable_reset_lockout_counter': 'enableResetLockoutCounter',
        'grace_period_date': 'gracePeriodDate',
        'lockout_time_in_seconds': 'lockoutTimeInSeconds',
        'max_history': 'maxHistory',
        'max_login_attempts': 'maxLoginAttempts',
        'min_change_period_in_days': 'minChangePeriodInDays',
        'min_length': 'minLength',
        'needs_lowercase': 'needsLowercase',
        'needs_numeric': 'needsNumeric',
        'needs_symbolic': 'needsSymbolic',
        'needs_uppercase': 'needsUppercase',
        'password_expiration_in_days': 'passwordExpirationInDays',
        'reset_lockout_counter_minutes': 'resetLockoutCounterMinutes'
    }

    def __init__(self, allow_username_substring=None, days_after_expiration_to_self_recover=None, days_before_expiration_to_force_reset=None, effective_date=None, enable_days_after_expiration_to_self_recover=None, enable_days_before_expiration_to_force_reset=None, enable_lockout_time_in_seconds=None, enable_max_history=None, enable_max_login_attempts=None, enable_min_change_period_in_days=None, enable_min_length=None, enable_password_expiration_in_days=None, enable_recovery_email=None, enable_reset_lockout_counter=None, grace_period_date=None, lockout_time_in_seconds=None, max_history=None, max_login_attempts=None, min_change_period_in_days=None, min_length=None, needs_lowercase=None, needs_numeric=None, needs_symbolic=None, needs_uppercase=None, password_expiration_in_days=None, reset_lockout_counter_minutes=None):  # noqa: E501
        """OrganizationsettingsPasswordPolicy - a model defined in Swagger"""  # noqa: E501
        self._allow_username_substring = None
        self._days_after_expiration_to_self_recover = None
        self._days_before_expiration_to_force_reset = None
        self._effective_date = None
        self._enable_days_after_expiration_to_self_recover = None
        self._enable_days_before_expiration_to_force_reset = None
        self._enable_lockout_time_in_seconds = None
        self._enable_max_history = None
        self._enable_max_login_attempts = None
        self._enable_min_change_period_in_days = None
        self._enable_min_length = None
        self._enable_password_expiration_in_days = None
        self._enable_recovery_email = None
        self._enable_reset_lockout_counter = None
        self._grace_period_date = None
        self._lockout_time_in_seconds = None
        self._max_history = None
        self._max_login_attempts = None
        self._min_change_period_in_days = None
        self._min_length = None
        self._needs_lowercase = None
        self._needs_numeric = None
        self._needs_symbolic = None
        self._needs_uppercase = None
        self._password_expiration_in_days = None
        self._reset_lockout_counter_minutes = None
        self.discriminator = None
        if allow_username_substring is not None:
            self.allow_username_substring = allow_username_substring
        if days_after_expiration_to_self_recover is not None:
            self.days_after_expiration_to_self_recover = days_after_expiration_to_self_recover
        if days_before_expiration_to_force_reset is not None:
            self.days_before_expiration_to_force_reset = days_before_expiration_to_force_reset
        if effective_date is not None:
            self.effective_date = effective_date
        if enable_days_after_expiration_to_self_recover is not None:
            self.enable_days_after_expiration_to_self_recover = enable_days_after_expiration_to_self_recover
        if enable_days_before_expiration_to_force_reset is not None:
            self.enable_days_before_expiration_to_force_reset = enable_days_before_expiration_to_force_reset
        if enable_lockout_time_in_seconds is not None:
            self.enable_lockout_time_in_seconds = enable_lockout_time_in_seconds
        if enable_max_history is not None:
            self.enable_max_history = enable_max_history
        if enable_max_login_attempts is not None:
            self.enable_max_login_attempts = enable_max_login_attempts
        if enable_min_change_period_in_days is not None:
            self.enable_min_change_period_in_days = enable_min_change_period_in_days
        if enable_min_length is not None:
            self.enable_min_length = enable_min_length
        if enable_password_expiration_in_days is not None:
            self.enable_password_expiration_in_days = enable_password_expiration_in_days
        if enable_recovery_email is not None:
            self.enable_recovery_email = enable_recovery_email
        if enable_reset_lockout_counter is not None:
            self.enable_reset_lockout_counter = enable_reset_lockout_counter
        if grace_period_date is not None:
            self.grace_period_date = grace_period_date
        if lockout_time_in_seconds is not None:
            self.lockout_time_in_seconds = lockout_time_in_seconds
        if max_history is not None:
            self.max_history = max_history
        if max_login_attempts is not None:
            self.max_login_attempts = max_login_attempts
        if min_change_period_in_days is not None:
            self.min_change_period_in_days = min_change_period_in_days
        if min_length is not None:
            self.min_length = min_length
        if needs_lowercase is not None:
            self.needs_lowercase = needs_lowercase
        if needs_numeric is not None:
            self.needs_numeric = needs_numeric
        if needs_symbolic is not None:
            self.needs_symbolic = needs_symbolic
        if needs_uppercase is not None:
            self.needs_uppercase = needs_uppercase
        if password_expiration_in_days is not None:
            self.password_expiration_in_days = password_expiration_in_days
        if reset_lockout_counter_minutes is not None:
            self.reset_lockout_counter_minutes = reset_lockout_counter_minutes

    @property
    def allow_username_substring(self):
        """Gets the allow_username_substring of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The allow_username_substring of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._allow_username_substring

    @allow_username_substring.setter
    def allow_username_substring(self, allow_username_substring):
        """Sets the allow_username_substring of this OrganizationsettingsPasswordPolicy.


        :param allow_username_substring: The allow_username_substring of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._allow_username_substring = allow_username_substring

    @property
    def days_after_expiration_to_self_recover(self):
        """Gets the days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.  # noqa: E501

        Deprecated field used for the legacy grace period feature.  # noqa: E501

        :return: The days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._days_after_expiration_to_self_recover

    @days_after_expiration_to_self_recover.setter
    def days_after_expiration_to_self_recover(self, days_after_expiration_to_self_recover):
        """Sets the days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.

        Deprecated field used for the legacy grace period feature.  # noqa: E501

        :param days_after_expiration_to_self_recover: The days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._days_after_expiration_to_self_recover = days_after_expiration_to_self_recover

    @property
    def days_before_expiration_to_force_reset(self):
        """Gets the days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._days_before_expiration_to_force_reset

    @days_before_expiration_to_force_reset.setter
    def days_before_expiration_to_force_reset(self, days_before_expiration_to_force_reset):
        """Sets the days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.


        :param days_before_expiration_to_force_reset: The days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._days_before_expiration_to_force_reset = days_before_expiration_to_force_reset

    @property
    def effective_date(self):
        """Gets the effective_date of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The effective_date of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this OrganizationsettingsPasswordPolicy.


        :param effective_date: The effective_date of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: str
        """

        self._effective_date = effective_date

    @property
    def enable_days_after_expiration_to_self_recover(self):
        """Gets the enable_days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_days_after_expiration_to_self_recover

    @enable_days_after_expiration_to_self_recover.setter
    def enable_days_after_expiration_to_self_recover(self, enable_days_after_expiration_to_self_recover):
        """Sets the enable_days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.


        :param enable_days_after_expiration_to_self_recover: The enable_days_after_expiration_to_self_recover of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_days_after_expiration_to_self_recover = enable_days_after_expiration_to_self_recover

    @property
    def enable_days_before_expiration_to_force_reset(self):
        """Gets the enable_days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_days_before_expiration_to_force_reset

    @enable_days_before_expiration_to_force_reset.setter
    def enable_days_before_expiration_to_force_reset(self, enable_days_before_expiration_to_force_reset):
        """Sets the enable_days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.


        :param enable_days_before_expiration_to_force_reset: The enable_days_before_expiration_to_force_reset of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_days_before_expiration_to_force_reset = enable_days_before_expiration_to_force_reset

    @property
    def enable_lockout_time_in_seconds(self):
        """Gets the enable_lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_lockout_time_in_seconds

    @enable_lockout_time_in_seconds.setter
    def enable_lockout_time_in_seconds(self, enable_lockout_time_in_seconds):
        """Sets the enable_lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.


        :param enable_lockout_time_in_seconds: The enable_lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_lockout_time_in_seconds = enable_lockout_time_in_seconds

    @property
    def enable_max_history(self):
        """Gets the enable_max_history of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_max_history of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_max_history

    @enable_max_history.setter
    def enable_max_history(self, enable_max_history):
        """Sets the enable_max_history of this OrganizationsettingsPasswordPolicy.


        :param enable_max_history: The enable_max_history of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_max_history = enable_max_history

    @property
    def enable_max_login_attempts(self):
        """Gets the enable_max_login_attempts of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_max_login_attempts of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_max_login_attempts

    @enable_max_login_attempts.setter
    def enable_max_login_attempts(self, enable_max_login_attempts):
        """Sets the enable_max_login_attempts of this OrganizationsettingsPasswordPolicy.


        :param enable_max_login_attempts: The enable_max_login_attempts of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_max_login_attempts = enable_max_login_attempts

    @property
    def enable_min_change_period_in_days(self):
        """Gets the enable_min_change_period_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_min_change_period_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_min_change_period_in_days

    @enable_min_change_period_in_days.setter
    def enable_min_change_period_in_days(self, enable_min_change_period_in_days):
        """Sets the enable_min_change_period_in_days of this OrganizationsettingsPasswordPolicy.


        :param enable_min_change_period_in_days: The enable_min_change_period_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_min_change_period_in_days = enable_min_change_period_in_days

    @property
    def enable_min_length(self):
        """Gets the enable_min_length of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_min_length of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_min_length

    @enable_min_length.setter
    def enable_min_length(self, enable_min_length):
        """Sets the enable_min_length of this OrganizationsettingsPasswordPolicy.


        :param enable_min_length: The enable_min_length of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_min_length = enable_min_length

    @property
    def enable_password_expiration_in_days(self):
        """Gets the enable_password_expiration_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_password_expiration_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_password_expiration_in_days

    @enable_password_expiration_in_days.setter
    def enable_password_expiration_in_days(self, enable_password_expiration_in_days):
        """Sets the enable_password_expiration_in_days of this OrganizationsettingsPasswordPolicy.


        :param enable_password_expiration_in_days: The enable_password_expiration_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_password_expiration_in_days = enable_password_expiration_in_days

    @property
    def enable_recovery_email(self):
        """Gets the enable_recovery_email of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_recovery_email of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_recovery_email

    @enable_recovery_email.setter
    def enable_recovery_email(self, enable_recovery_email):
        """Sets the enable_recovery_email of this OrganizationsettingsPasswordPolicy.


        :param enable_recovery_email: The enable_recovery_email of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_recovery_email = enable_recovery_email

    @property
    def enable_reset_lockout_counter(self):
        """Gets the enable_reset_lockout_counter of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The enable_reset_lockout_counter of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_reset_lockout_counter

    @enable_reset_lockout_counter.setter
    def enable_reset_lockout_counter(self, enable_reset_lockout_counter):
        """Sets the enable_reset_lockout_counter of this OrganizationsettingsPasswordPolicy.


        :param enable_reset_lockout_counter: The enable_reset_lockout_counter of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._enable_reset_lockout_counter = enable_reset_lockout_counter

    @property
    def grace_period_date(self):
        """Gets the grace_period_date of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The grace_period_date of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: str
        """
        return self._grace_period_date

    @grace_period_date.setter
    def grace_period_date(self, grace_period_date):
        """Sets the grace_period_date of this OrganizationsettingsPasswordPolicy.


        :param grace_period_date: The grace_period_date of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: str
        """

        self._grace_period_date = grace_period_date

    @property
    def lockout_time_in_seconds(self):
        """Gets the lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._lockout_time_in_seconds

    @lockout_time_in_seconds.setter
    def lockout_time_in_seconds(self, lockout_time_in_seconds):
        """Sets the lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.


        :param lockout_time_in_seconds: The lockout_time_in_seconds of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._lockout_time_in_seconds = lockout_time_in_seconds

    @property
    def max_history(self):
        """Gets the max_history of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The max_history of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_history

    @max_history.setter
    def max_history(self, max_history):
        """Sets the max_history of this OrganizationsettingsPasswordPolicy.


        :param max_history: The max_history of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._max_history = max_history

    @property
    def max_login_attempts(self):
        """Gets the max_login_attempts of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The max_login_attempts of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._max_login_attempts

    @max_login_attempts.setter
    def max_login_attempts(self, max_login_attempts):
        """Sets the max_login_attempts of this OrganizationsettingsPasswordPolicy.


        :param max_login_attempts: The max_login_attempts of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._max_login_attempts = max_login_attempts

    @property
    def min_change_period_in_days(self):
        """Gets the min_change_period_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The min_change_period_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._min_change_period_in_days

    @min_change_period_in_days.setter
    def min_change_period_in_days(self, min_change_period_in_days):
        """Sets the min_change_period_in_days of this OrganizationsettingsPasswordPolicy.


        :param min_change_period_in_days: The min_change_period_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._min_change_period_in_days = min_change_period_in_days

    @property
    def min_length(self):
        """Gets the min_length of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The min_length of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this OrganizationsettingsPasswordPolicy.


        :param min_length: The min_length of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def needs_lowercase(self):
        """Gets the needs_lowercase of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The needs_lowercase of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._needs_lowercase

    @needs_lowercase.setter
    def needs_lowercase(self, needs_lowercase):
        """Sets the needs_lowercase of this OrganizationsettingsPasswordPolicy.


        :param needs_lowercase: The needs_lowercase of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._needs_lowercase = needs_lowercase

    @property
    def needs_numeric(self):
        """Gets the needs_numeric of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The needs_numeric of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._needs_numeric

    @needs_numeric.setter
    def needs_numeric(self, needs_numeric):
        """Sets the needs_numeric of this OrganizationsettingsPasswordPolicy.


        :param needs_numeric: The needs_numeric of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._needs_numeric = needs_numeric

    @property
    def needs_symbolic(self):
        """Gets the needs_symbolic of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The needs_symbolic of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._needs_symbolic

    @needs_symbolic.setter
    def needs_symbolic(self, needs_symbolic):
        """Sets the needs_symbolic of this OrganizationsettingsPasswordPolicy.


        :param needs_symbolic: The needs_symbolic of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._needs_symbolic = needs_symbolic

    @property
    def needs_uppercase(self):
        """Gets the needs_uppercase of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The needs_uppercase of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._needs_uppercase

    @needs_uppercase.setter
    def needs_uppercase(self, needs_uppercase):
        """Sets the needs_uppercase of this OrganizationsettingsPasswordPolicy.


        :param needs_uppercase: The needs_uppercase of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._needs_uppercase = needs_uppercase

    @property
    def password_expiration_in_days(self):
        """Gets the password_expiration_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The password_expiration_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._password_expiration_in_days

    @password_expiration_in_days.setter
    def password_expiration_in_days(self, password_expiration_in_days):
        """Sets the password_expiration_in_days of this OrganizationsettingsPasswordPolicy.


        :param password_expiration_in_days: The password_expiration_in_days of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._password_expiration_in_days = password_expiration_in_days

    @property
    def reset_lockout_counter_minutes(self):
        """Gets the reset_lockout_counter_minutes of this OrganizationsettingsPasswordPolicy.  # noqa: E501


        :return: The reset_lockout_counter_minutes of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._reset_lockout_counter_minutes

    @reset_lockout_counter_minutes.setter
    def reset_lockout_counter_minutes(self, reset_lockout_counter_minutes):
        """Sets the reset_lockout_counter_minutes of this OrganizationsettingsPasswordPolicy.


        :param reset_lockout_counter_minutes: The reset_lockout_counter_minutes of this OrganizationsettingsPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._reset_lockout_counter_minutes = reset_lockout_counter_minutes

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
        if issubclass(OrganizationsettingsPasswordPolicy, dict):
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
        if not isinstance(other, OrganizationsettingsPasswordPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
