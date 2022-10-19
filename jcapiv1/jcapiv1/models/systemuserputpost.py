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

class Systemuserputpost(object):
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
        'account_locked': 'bool',
        'activated': 'bool',
        'addresses': 'list[SystemuserputpostAddresses]',
        'allow_public_key': 'bool',
        'alternate_email': 'str',
        'attributes': 'list[SystemuserputAttributes]',
        'company': 'str',
        'cost_center': 'str',
        'department': 'str',
        'description': 'str',
        'disable_device_max_login_attempts': 'bool',
        'displayname': 'str',
        'email': 'str',
        'employee_identifier': 'str',
        'employee_type': 'str',
        'enable_managed_uid': 'bool',
        'enable_user_portal_multifactor': 'bool',
        'external_dn': 'str',
        'external_password_expiration_date': 'datetime',
        'external_source_type': 'str',
        'externally_managed': 'bool',
        'firstname': 'str',
        'job_title': 'str',
        'lastname': 'str',
        'ldap_binding_user': 'bool',
        'location': 'str',
        'managed_apple_id': 'str',
        'manager': 'str',
        'mfa': 'Mfa',
        'middlename': 'str',
        'password': 'str',
        'password_never_expires': 'bool',
        'passwordless_sudo': 'bool',
        'phone_numbers': 'list[SystemuserputpostPhoneNumbers]',
        'public_key': 'str',
        'recovery_email': 'SystemuserputpostRecoveryEmail',
        'relationships': 'list[SystemuserputRelationships]',
        'samba_service_user': 'bool',
        'state': 'str',
        'sudo': 'bool',
        'suspended': 'bool',
        'tags': 'list[str]',
        'unix_guid': 'int',
        'unix_uid': 'int',
        'username': 'str'
    }

    attribute_map = {
        'account_locked': 'account_locked',
        'activated': 'activated',
        'addresses': 'addresses',
        'allow_public_key': 'allow_public_key',
        'alternate_email': 'alternateEmail',
        'attributes': 'attributes',
        'company': 'company',
        'cost_center': 'costCenter',
        'department': 'department',
        'description': 'description',
        'disable_device_max_login_attempts': 'disableDeviceMaxLoginAttempts',
        'displayname': 'displayname',
        'email': 'email',
        'employee_identifier': 'employeeIdentifier',
        'employee_type': 'employeeType',
        'enable_managed_uid': 'enable_managed_uid',
        'enable_user_portal_multifactor': 'enable_user_portal_multifactor',
        'external_dn': 'external_dn',
        'external_password_expiration_date': 'external_password_expiration_date',
        'external_source_type': 'external_source_type',
        'externally_managed': 'externally_managed',
        'firstname': 'firstname',
        'job_title': 'jobTitle',
        'lastname': 'lastname',
        'ldap_binding_user': 'ldap_binding_user',
        'location': 'location',
        'managed_apple_id': 'managedAppleId',
        'manager': 'manager',
        'mfa': 'mfa',
        'middlename': 'middlename',
        'password': 'password',
        'password_never_expires': 'password_never_expires',
        'passwordless_sudo': 'passwordless_sudo',
        'phone_numbers': 'phoneNumbers',
        'public_key': 'public_key',
        'recovery_email': 'recoveryEmail',
        'relationships': 'relationships',
        'samba_service_user': 'samba_service_user',
        'state': 'state',
        'sudo': 'sudo',
        'suspended': 'suspended',
        'tags': 'tags',
        'unix_guid': 'unix_guid',
        'unix_uid': 'unix_uid',
        'username': 'username'
    }

    def __init__(self, account_locked=None, activated=None, addresses=None, allow_public_key=None, alternate_email=None, attributes=None, company=None, cost_center=None, department=None, description=None, disable_device_max_login_attempts=None, displayname=None, email=None, employee_identifier=None, employee_type=None, enable_managed_uid=None, enable_user_portal_multifactor=None, external_dn=None, external_password_expiration_date=None, external_source_type=None, externally_managed=None, firstname=None, job_title=None, lastname=None, ldap_binding_user=None, location=None, managed_apple_id=None, manager=None, mfa=None, middlename=None, password=None, password_never_expires=None, passwordless_sudo=None, phone_numbers=None, public_key=None, recovery_email=None, relationships=None, samba_service_user=None, state=None, sudo=None, suspended=None, tags=None, unix_guid=None, unix_uid=None, username=None):  # noqa: E501
        """Systemuserputpost - a model defined in Swagger"""  # noqa: E501
        self._account_locked = None
        self._activated = None
        self._addresses = None
        self._allow_public_key = None
        self._alternate_email = None
        self._attributes = None
        self._company = None
        self._cost_center = None
        self._department = None
        self._description = None
        self._disable_device_max_login_attempts = None
        self._displayname = None
        self._email = None
        self._employee_identifier = None
        self._employee_type = None
        self._enable_managed_uid = None
        self._enable_user_portal_multifactor = None
        self._external_dn = None
        self._external_password_expiration_date = None
        self._external_source_type = None
        self._externally_managed = None
        self._firstname = None
        self._job_title = None
        self._lastname = None
        self._ldap_binding_user = None
        self._location = None
        self._managed_apple_id = None
        self._manager = None
        self._mfa = None
        self._middlename = None
        self._password = None
        self._password_never_expires = None
        self._passwordless_sudo = None
        self._phone_numbers = None
        self._public_key = None
        self._recovery_email = None
        self._relationships = None
        self._samba_service_user = None
        self._state = None
        self._sudo = None
        self._suspended = None
        self._tags = None
        self._unix_guid = None
        self._unix_uid = None
        self._username = None
        self.discriminator = None
        if account_locked is not None:
            self.account_locked = account_locked
        if activated is not None:
            self.activated = activated
        if addresses is not None:
            self.addresses = addresses
        if allow_public_key is not None:
            self.allow_public_key = allow_public_key
        if alternate_email is not None:
            self.alternate_email = alternate_email
        if attributes is not None:
            self.attributes = attributes
        if company is not None:
            self.company = company
        if cost_center is not None:
            self.cost_center = cost_center
        if department is not None:
            self.department = department
        if description is not None:
            self.description = description
        if disable_device_max_login_attempts is not None:
            self.disable_device_max_login_attempts = disable_device_max_login_attempts
        if displayname is not None:
            self.displayname = displayname
        self.email = email
        if employee_identifier is not None:
            self.employee_identifier = employee_identifier
        if employee_type is not None:
            self.employee_type = employee_type
        if enable_managed_uid is not None:
            self.enable_managed_uid = enable_managed_uid
        if enable_user_portal_multifactor is not None:
            self.enable_user_portal_multifactor = enable_user_portal_multifactor
        if external_dn is not None:
            self.external_dn = external_dn
        if external_password_expiration_date is not None:
            self.external_password_expiration_date = external_password_expiration_date
        if external_source_type is not None:
            self.external_source_type = external_source_type
        if externally_managed is not None:
            self.externally_managed = externally_managed
        if firstname is not None:
            self.firstname = firstname
        if job_title is not None:
            self.job_title = job_title
        if lastname is not None:
            self.lastname = lastname
        if ldap_binding_user is not None:
            self.ldap_binding_user = ldap_binding_user
        if location is not None:
            self.location = location
        if managed_apple_id is not None:
            self.managed_apple_id = managed_apple_id
        if manager is not None:
            self.manager = manager
        if mfa is not None:
            self.mfa = mfa
        if middlename is not None:
            self.middlename = middlename
        if password is not None:
            self.password = password
        if password_never_expires is not None:
            self.password_never_expires = password_never_expires
        if passwordless_sudo is not None:
            self.passwordless_sudo = passwordless_sudo
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if public_key is not None:
            self.public_key = public_key
        if recovery_email is not None:
            self.recovery_email = recovery_email
        if relationships is not None:
            self.relationships = relationships
        if samba_service_user is not None:
            self.samba_service_user = samba_service_user
        if state is not None:
            self.state = state
        if sudo is not None:
            self.sudo = sudo
        if suspended is not None:
            self.suspended = suspended
        if tags is not None:
            self.tags = tags
        if unix_guid is not None:
            self.unix_guid = unix_guid
        if unix_uid is not None:
            self.unix_uid = unix_uid
        self.username = username

    @property
    def account_locked(self):
        """Gets the account_locked of this Systemuserputpost.  # noqa: E501


        :return: The account_locked of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._account_locked

    @account_locked.setter
    def account_locked(self, account_locked):
        """Sets the account_locked of this Systemuserputpost.


        :param account_locked: The account_locked of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._account_locked = account_locked

    @property
    def activated(self):
        """Gets the activated of this Systemuserputpost.  # noqa: E501


        :return: The activated of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this Systemuserputpost.


        :param activated: The activated of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._activated = activated

    @property
    def addresses(self):
        """Gets the addresses of this Systemuserputpost.  # noqa: E501


        :return: The addresses of this Systemuserputpost.  # noqa: E501
        :rtype: list[SystemuserputpostAddresses]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Systemuserputpost.


        :param addresses: The addresses of this Systemuserputpost.  # noqa: E501
        :type: list[SystemuserputpostAddresses]
        """

        self._addresses = addresses

    @property
    def allow_public_key(self):
        """Gets the allow_public_key of this Systemuserputpost.  # noqa: E501


        :return: The allow_public_key of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._allow_public_key

    @allow_public_key.setter
    def allow_public_key(self, allow_public_key):
        """Sets the allow_public_key of this Systemuserputpost.


        :param allow_public_key: The allow_public_key of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._allow_public_key = allow_public_key

    @property
    def alternate_email(self):
        """Gets the alternate_email of this Systemuserputpost.  # noqa: E501


        :return: The alternate_email of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._alternate_email

    @alternate_email.setter
    def alternate_email(self, alternate_email):
        """Sets the alternate_email of this Systemuserputpost.


        :param alternate_email: The alternate_email of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._alternate_email = alternate_email

    @property
    def attributes(self):
        """Gets the attributes of this Systemuserputpost.  # noqa: E501


        :return: The attributes of this Systemuserputpost.  # noqa: E501
        :rtype: list[SystemuserputAttributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Systemuserputpost.


        :param attributes: The attributes of this Systemuserputpost.  # noqa: E501
        :type: list[SystemuserputAttributes]
        """

        self._attributes = attributes

    @property
    def company(self):
        """Gets the company of this Systemuserputpost.  # noqa: E501


        :return: The company of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Systemuserputpost.


        :param company: The company of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def cost_center(self):
        """Gets the cost_center of this Systemuserputpost.  # noqa: E501


        :return: The cost_center of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this Systemuserputpost.


        :param cost_center: The cost_center of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._cost_center = cost_center

    @property
    def department(self):
        """Gets the department of this Systemuserputpost.  # noqa: E501


        :return: The department of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Systemuserputpost.


        :param department: The department of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def description(self):
        """Gets the description of this Systemuserputpost.  # noqa: E501


        :return: The description of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Systemuserputpost.


        :param description: The description of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disable_device_max_login_attempts(self):
        """Gets the disable_device_max_login_attempts of this Systemuserputpost.  # noqa: E501


        :return: The disable_device_max_login_attempts of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._disable_device_max_login_attempts

    @disable_device_max_login_attempts.setter
    def disable_device_max_login_attempts(self, disable_device_max_login_attempts):
        """Sets the disable_device_max_login_attempts of this Systemuserputpost.


        :param disable_device_max_login_attempts: The disable_device_max_login_attempts of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._disable_device_max_login_attempts = disable_device_max_login_attempts

    @property
    def displayname(self):
        """Gets the displayname of this Systemuserputpost.  # noqa: E501


        :return: The displayname of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this Systemuserputpost.


        :param displayname: The displayname of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._displayname = displayname

    @property
    def email(self):
        """Gets the email of this Systemuserputpost.  # noqa: E501


        :return: The email of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Systemuserputpost.


        :param email: The email of this Systemuserputpost.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def employee_identifier(self):
        """Gets the employee_identifier of this Systemuserputpost.  # noqa: E501

        Must be unique per user.   # noqa: E501

        :return: The employee_identifier of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._employee_identifier

    @employee_identifier.setter
    def employee_identifier(self, employee_identifier):
        """Sets the employee_identifier of this Systemuserputpost.

        Must be unique per user.   # noqa: E501

        :param employee_identifier: The employee_identifier of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._employee_identifier = employee_identifier

    @property
    def employee_type(self):
        """Gets the employee_type of this Systemuserputpost.  # noqa: E501


        :return: The employee_type of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._employee_type

    @employee_type.setter
    def employee_type(self, employee_type):
        """Sets the employee_type of this Systemuserputpost.


        :param employee_type: The employee_type of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._employee_type = employee_type

    @property
    def enable_managed_uid(self):
        """Gets the enable_managed_uid of this Systemuserputpost.  # noqa: E501


        :return: The enable_managed_uid of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._enable_managed_uid

    @enable_managed_uid.setter
    def enable_managed_uid(self, enable_managed_uid):
        """Sets the enable_managed_uid of this Systemuserputpost.


        :param enable_managed_uid: The enable_managed_uid of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._enable_managed_uid = enable_managed_uid

    @property
    def enable_user_portal_multifactor(self):
        """Gets the enable_user_portal_multifactor of this Systemuserputpost.  # noqa: E501


        :return: The enable_user_portal_multifactor of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._enable_user_portal_multifactor

    @enable_user_portal_multifactor.setter
    def enable_user_portal_multifactor(self, enable_user_portal_multifactor):
        """Sets the enable_user_portal_multifactor of this Systemuserputpost.


        :param enable_user_portal_multifactor: The enable_user_portal_multifactor of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._enable_user_portal_multifactor = enable_user_portal_multifactor

    @property
    def external_dn(self):
        """Gets the external_dn of this Systemuserputpost.  # noqa: E501


        :return: The external_dn of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._external_dn

    @external_dn.setter
    def external_dn(self, external_dn):
        """Sets the external_dn of this Systemuserputpost.


        :param external_dn: The external_dn of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._external_dn = external_dn

    @property
    def external_password_expiration_date(self):
        """Gets the external_password_expiration_date of this Systemuserputpost.  # noqa: E501


        :return: The external_password_expiration_date of this Systemuserputpost.  # noqa: E501
        :rtype: datetime
        """
        return self._external_password_expiration_date

    @external_password_expiration_date.setter
    def external_password_expiration_date(self, external_password_expiration_date):
        """Sets the external_password_expiration_date of this Systemuserputpost.


        :param external_password_expiration_date: The external_password_expiration_date of this Systemuserputpost.  # noqa: E501
        :type: datetime
        """

        self._external_password_expiration_date = external_password_expiration_date

    @property
    def external_source_type(self):
        """Gets the external_source_type of this Systemuserputpost.  # noqa: E501


        :return: The external_source_type of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._external_source_type

    @external_source_type.setter
    def external_source_type(self, external_source_type):
        """Sets the external_source_type of this Systemuserputpost.


        :param external_source_type: The external_source_type of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._external_source_type = external_source_type

    @property
    def externally_managed(self):
        """Gets the externally_managed of this Systemuserputpost.  # noqa: E501


        :return: The externally_managed of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """Sets the externally_managed of this Systemuserputpost.


        :param externally_managed: The externally_managed of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def firstname(self):
        """Gets the firstname of this Systemuserputpost.  # noqa: E501


        :return: The firstname of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Systemuserputpost.


        :param firstname: The firstname of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def job_title(self):
        """Gets the job_title of this Systemuserputpost.  # noqa: E501


        :return: The job_title of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this Systemuserputpost.


        :param job_title: The job_title of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def lastname(self):
        """Gets the lastname of this Systemuserputpost.  # noqa: E501


        :return: The lastname of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this Systemuserputpost.


        :param lastname: The lastname of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def ldap_binding_user(self):
        """Gets the ldap_binding_user of this Systemuserputpost.  # noqa: E501


        :return: The ldap_binding_user of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._ldap_binding_user

    @ldap_binding_user.setter
    def ldap_binding_user(self, ldap_binding_user):
        """Sets the ldap_binding_user of this Systemuserputpost.


        :param ldap_binding_user: The ldap_binding_user of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._ldap_binding_user = ldap_binding_user

    @property
    def location(self):
        """Gets the location of this Systemuserputpost.  # noqa: E501


        :return: The location of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Systemuserputpost.


        :param location: The location of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def managed_apple_id(self):
        """Gets the managed_apple_id of this Systemuserputpost.  # noqa: E501


        :return: The managed_apple_id of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._managed_apple_id

    @managed_apple_id.setter
    def managed_apple_id(self, managed_apple_id):
        """Sets the managed_apple_id of this Systemuserputpost.


        :param managed_apple_id: The managed_apple_id of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._managed_apple_id = managed_apple_id

    @property
    def manager(self):
        """Gets the manager of this Systemuserputpost.  # noqa: E501

        Relation with another systemuser to identify the last as a manager.  # noqa: E501

        :return: The manager of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this Systemuserputpost.

        Relation with another systemuser to identify the last as a manager.  # noqa: E501

        :param manager: The manager of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def mfa(self):
        """Gets the mfa of this Systemuserputpost.  # noqa: E501


        :return: The mfa of this Systemuserputpost.  # noqa: E501
        :rtype: Mfa
        """
        return self._mfa

    @mfa.setter
    def mfa(self, mfa):
        """Sets the mfa of this Systemuserputpost.


        :param mfa: The mfa of this Systemuserputpost.  # noqa: E501
        :type: Mfa
        """

        self._mfa = mfa

    @property
    def middlename(self):
        """Gets the middlename of this Systemuserputpost.  # noqa: E501


        :return: The middlename of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """Sets the middlename of this Systemuserputpost.


        :param middlename: The middlename of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._middlename = middlename

    @property
    def password(self):
        """Gets the password of this Systemuserputpost.  # noqa: E501


        :return: The password of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Systemuserputpost.


        :param password: The password of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_never_expires(self):
        """Gets the password_never_expires of this Systemuserputpost.  # noqa: E501


        :return: The password_never_expires of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._password_never_expires

    @password_never_expires.setter
    def password_never_expires(self, password_never_expires):
        """Sets the password_never_expires of this Systemuserputpost.


        :param password_never_expires: The password_never_expires of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._password_never_expires = password_never_expires

    @property
    def passwordless_sudo(self):
        """Gets the passwordless_sudo of this Systemuserputpost.  # noqa: E501


        :return: The passwordless_sudo of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._passwordless_sudo

    @passwordless_sudo.setter
    def passwordless_sudo(self, passwordless_sudo):
        """Sets the passwordless_sudo of this Systemuserputpost.


        :param passwordless_sudo: The passwordless_sudo of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._passwordless_sudo = passwordless_sudo

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this Systemuserputpost.  # noqa: E501


        :return: The phone_numbers of this Systemuserputpost.  # noqa: E501
        :rtype: list[SystemuserputpostPhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this Systemuserputpost.


        :param phone_numbers: The phone_numbers of this Systemuserputpost.  # noqa: E501
        :type: list[SystemuserputpostPhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def public_key(self):
        """Gets the public_key of this Systemuserputpost.  # noqa: E501


        :return: The public_key of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Systemuserputpost.


        :param public_key: The public_key of this Systemuserputpost.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def recovery_email(self):
        """Gets the recovery_email of this Systemuserputpost.  # noqa: E501


        :return: The recovery_email of this Systemuserputpost.  # noqa: E501
        :rtype: SystemuserputpostRecoveryEmail
        """
        return self._recovery_email

    @recovery_email.setter
    def recovery_email(self, recovery_email):
        """Sets the recovery_email of this Systemuserputpost.


        :param recovery_email: The recovery_email of this Systemuserputpost.  # noqa: E501
        :type: SystemuserputpostRecoveryEmail
        """

        self._recovery_email = recovery_email

    @property
    def relationships(self):
        """Gets the relationships of this Systemuserputpost.  # noqa: E501


        :return: The relationships of this Systemuserputpost.  # noqa: E501
        :rtype: list[SystemuserputRelationships]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this Systemuserputpost.


        :param relationships: The relationships of this Systemuserputpost.  # noqa: E501
        :type: list[SystemuserputRelationships]
        """

        self._relationships = relationships

    @property
    def samba_service_user(self):
        """Gets the samba_service_user of this Systemuserputpost.  # noqa: E501


        :return: The samba_service_user of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._samba_service_user

    @samba_service_user.setter
    def samba_service_user(self, samba_service_user):
        """Sets the samba_service_user of this Systemuserputpost.


        :param samba_service_user: The samba_service_user of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._samba_service_user = samba_service_user

    @property
    def state(self):
        """Gets the state of this Systemuserputpost.  # noqa: E501


        :return: The state of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Systemuserputpost.


        :param state: The state of this Systemuserputpost.  # noqa: E501
        :type: str
        """
        allowed_values = ["STAGED", "ACTIVATED", "SUSPENDED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def sudo(self):
        """Gets the sudo of this Systemuserputpost.  # noqa: E501


        :return: The sudo of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._sudo

    @sudo.setter
    def sudo(self, sudo):
        """Sets the sudo of this Systemuserputpost.


        :param sudo: The sudo of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._sudo = sudo

    @property
    def suspended(self):
        """Gets the suspended of this Systemuserputpost.  # noqa: E501


        :return: The suspended of this Systemuserputpost.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this Systemuserputpost.


        :param suspended: The suspended of this Systemuserputpost.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def tags(self):
        """Gets the tags of this Systemuserputpost.  # noqa: E501


        :return: The tags of this Systemuserputpost.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Systemuserputpost.


        :param tags: The tags of this Systemuserputpost.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def unix_guid(self):
        """Gets the unix_guid of this Systemuserputpost.  # noqa: E501


        :return: The unix_guid of this Systemuserputpost.  # noqa: E501
        :rtype: int
        """
        return self._unix_guid

    @unix_guid.setter
    def unix_guid(self, unix_guid):
        """Sets the unix_guid of this Systemuserputpost.


        :param unix_guid: The unix_guid of this Systemuserputpost.  # noqa: E501
        :type: int
        """

        self._unix_guid = unix_guid

    @property
    def unix_uid(self):
        """Gets the unix_uid of this Systemuserputpost.  # noqa: E501


        :return: The unix_uid of this Systemuserputpost.  # noqa: E501
        :rtype: int
        """
        return self._unix_uid

    @unix_uid.setter
    def unix_uid(self, unix_uid):
        """Sets the unix_uid of this Systemuserputpost.


        :param unix_uid: The unix_uid of this Systemuserputpost.  # noqa: E501
        :type: int
        """

        self._unix_uid = unix_uid

    @property
    def username(self):
        """Gets the username of this Systemuserputpost.  # noqa: E501


        :return: The username of this Systemuserputpost.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Systemuserputpost.


        :param username: The username of this Systemuserputpost.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(Systemuserputpost, dict):
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
        if not isinstance(other, Systemuserputpost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
