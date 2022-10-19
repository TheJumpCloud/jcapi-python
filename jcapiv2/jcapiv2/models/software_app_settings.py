# coding: utf-8

"""
    JumpCloud API

    # Overview  JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # Directory Objects  This API offers the ability to interact with some of our core features; otherwise known as Directory Objects. The Directory Objects are:  * Commands * Policies * Policy Groups * Applications * Systems * Users * User Groups * System Groups * Radius Servers * Directories: Office 365, LDAP,G-Suite, Active Directory * Duo accounts and applications.  The Directory Object is an important concept to understand in order to successfully use JumpCloud API.  ## JumpCloud Graph  We've also introduced the concept of the JumpCloud Graph along with  Directory Objects. The Graph is a powerful aspect of our platform which will enable you to associate objects with each other, or establish membership for certain objects to become members of other objects.  Specific `GET` endpoints will allow you to traverse the JumpCloud Graph to return all indirect and directly bound objects in your organization.  | ![alt text](https://s3.amazonaws.com/jumpcloud-kb/Knowledge+Base+Photos/API+Docs/jumpcloud_graph.png \"JumpCloud Graph Model Example\") | |:--:| | **This diagram highlights our association and membership model as it relates to Directory Objects.** |  # API Key  ## Access Your API Key  To locate your API Key:  1. Log into the [JumpCloud Admin Console](https://console.jumpcloud.com/). 2. Go to the username drop down located in the top-right of the Console. 3. Retrieve your API key from API Settings.  ## API Key Considerations  This API key is associated to the currently logged in administrator. Other admins will have different API keys.  **WARNING** Please keep this API key secret, as it grants full access to any data accessible via your JumpCloud console account.  You can also reset your API key in the same location in the JumpCloud Admin Console.  ## Recycling or Resetting Your API Key  In order to revoke access with the current API key, simply reset your API key. This will render all calls using the previous API key inaccessible.  Your API key will be passed in as a header with the header name \"x-api-key\".  ```bash curl -H \"x-api-key: [YOUR_API_KEY_HERE]\" \"https://console.jumpcloud.com/api/v2/systemgroups\" ```  # System Context  * [Introduction](#introduction) * [Supported endpoints](#supported-endpoints) * [Response codes](#response-codes) * [Authentication](#authentication) * [Additional examples](#additional-examples) * [Third party](#third-party)  ## Introduction  JumpCloud System Context Authorization is an alternative way to authenticate with a subset of JumpCloud's REST APIs. Using this method, a system can manage its information and resource associations, allowing modern auto provisioning environments to scale as needed.  **Notes:**   * The following documentation applies to Linux Operating Systems only.  * Systems that have been automatically enrolled using Apple's Device Enrollment Program (DEP) or systems enrolled using the User Portal install are not eligible to use the System Context API to prevent unauthorized access to system groups and resources. If a script that utilizes the System Context API is invoked on a system enrolled in this way, it will display an error.  ## Supported Endpoints  JumpCloud System Context Authorization can be used in conjunction with Systems endpoints found in the V1 API and certain System Group endpoints found in the v2 API.  * A system may fetch, alter, and delete metadata about itself, including manipulating a system's Group and Systemuser associations,   * `/api/systems/{system_id}` | [`GET`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_get) [`PUT`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_put) * A system may delete itself from your JumpCloud organization   * `/api/systems/{system_id}` | [`DELETE`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_delete) * A system may fetch its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/memberof` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembership)   * `/api/v2/systems/{system_id}/associations` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsList)   * `/api/v2/systems/{system_id}/users` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemTraverseUser) * A system may alter its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/associations` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsPost) * A system may alter its System Group associations   * `/api/v2/systemgroups/{group_id}/members` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembersPost)     * _NOTE_ If a system attempts to alter the system group membership of a different system the request will be rejected  ## Response Codes  If endpoints other than those described above are called using the System Context API, the server will return a `401` response.  ## Authentication  To allow for secure access to our APIs, you must authenticate each API request. JumpCloud System Context Authorization uses [HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures-00) to authenticate API requests. The HTTP Signatures sent with each request are similar to the signatures used by the Amazon Web Services REST API. To help with the request-signing process, we have provided an [example bash script](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh). This example API request simply requests the entire system record. You must be root, or have permissions to access the contents of the `/opt/jc` directory to generate a signature.  Here is a breakdown of the example script with explanations.  First, the script extracts the systemKey from the JSON formatted `/opt/jc/jcagent.conf` file.  ```bash #!/bin/bash conf=\"`cat /opt/jc/jcagent.conf`\" regex=\"systemKey\\\":\\\"(\\w+)\\\"\"  if [[ $conf =~ $regex ]] ; then   systemKey=\"${BASH_REMATCH[1]}\" fi ```  Then, the script retrieves the current date in the correct format.  ```bash now=`date -u \"+%a, %d %h %Y %H:%M:%S GMT\"`; ```  Next, we build a signing string to demonstrate the expected signature format. The signed string must consist of the [request-line](https://tools.ietf.org/html/rfc2616#page-35) and the date header, separated by a newline character.  ```bash signstr=\"GET /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" ```  The next step is to calculate and apply the signature. This is a two-step process:  1. Create a signature from the signing string using the JumpCloud Agent private key: ``printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key`` 2. Then Base64-encode the signature string and trim off the newline characters: ``| openssl enc -e -a | tr -d '\\n'``  The combined steps above result in:  ```bash signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ; ```  Finally, we make sure the API call sending the signature has the same Authorization and Date header values, HTTP method, and URL that were used in the signing string.  ```bash curl -iq \\   -H \"Accept: application/json\" \\   -H \"Content-Type: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Input Data  All PUT and POST methods should use the HTTP Content-Type header with a value of 'application/json'. PUT methods are used for updating a record. POST methods are used to create a record.  The following example demonstrates how to update the `displayName` of the system.  ```bash signstr=\"PUT /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ;  curl -iq \\   -d \"{\\\"displayName\\\" : \\\"updated-system-name-1\\\"}\" \\   -X \"PUT\" \\   -H \"Content-Type: application/json\" \\   -H \"Accept: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Output Data  All results will be formatted as JSON.  Here is an abbreviated example of response output:  ```json {   \"_id\": \"525ee96f52e144993e000015\",   \"agentServer\": \"lappy386\",   \"agentVersion\": \"0.9.42\",   \"arch\": \"x86_64\",   \"connectionKey\": \"127.0.0.1_51812\",   \"displayName\": \"ubuntu-1204\",   \"firstContact\": \"2013-10-16T19:30:55.611Z\",   \"hostname\": \"ubuntu-1204\"   ... ```  ## Additional Examples  ### Signing Authentication Example  This example demonstrates how to make an authenticated request to fetch the JumpCloud record for this system.  [SigningExample.sh](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh)  ### Shutdown Hook  This example demonstrates how to make an authenticated request on system shutdown. Using an init.d script registered at run level 0, you can call the System Context API as the system is shutting down.  [Instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) is an example of an init.d script that only runs at system shutdown.  After customizing the [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) script, you should install it on the system(s) running the JumpCloud agent.  1. Copy the modified [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) to `/etc/init.d/instance-shutdown`. 2. On Ubuntu systems, run `update-rc.d instance-shutdown defaults`. On RedHat/CentOS systems, run `chkconfig --add instance-shutdown`.  ## Third Party  ### Chef Cookbooks  [https://github.com/nshenry03/jumpcloud](https://github.com/nshenry03/jumpcloud)  [https://github.com/cjs226/jumpcloud](https://github.com/cjs226/jumpcloud)  # Multi-Tenant Portal Headers  Multi-Tenant Organization API Headers are available for JumpCloud Admins to use when making API requests from Organizations that have multiple managed organizations.  The `x-org-id` is a required header for all multi-tenant admins when making API requests to JumpCloud. This header will define to which organization you would like to make the request.  **NOTE** Single Tenant Admins do not need to provide this header when making an API request.  ## Header Value  `x-org-id`  ## API Response Codes  * `400` Malformed ID. * `400` x-org-id and Organization path ID do not match. * `401` ID not included for multi-tenant admin * `403` ID included on unsupported route. * `404` Organization ID Not Found.  ```bash curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -H 'x-org-id: {ORG_ID}'  ```  ## To Obtain an Individual Organization ID via the UI  As a prerequisite, your Primary Organization will need to be setup for Multi-Tenancy. This provides access to the Multi-Tenant Organization Admin Portal.  1. Log into JumpCloud [Admin Console](https://console.jumpcloud.com). If you are a multi-tenant Admin, you will automatically be routed to the Multi-Tenant Admin Portal. 2. From the Multi-Tenant Portal's primary navigation bar, select the Organization you'd like to access. 3. You will automatically be routed to that Organization's Admin Console. 4. Go to Settings in the sub-tenant's primary navigation. 5. You can obtain your Organization ID below your Organization's Contact Information on the Settings page.  ## To Obtain All Organization IDs via the API  * You can make an API request to this endpoint using the API key of your Primary Organization.  `https://console.jumpcloud.com/api/organizations/` This will return all your managed organizations.  ```bash curl -X GET \\   https://console.jumpcloud.com/api/organizations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # SDKs  You can find language specific SDKs that can help you kickstart your Integration with JumpCloud in the following GitHub repositories:  * [Python](https://github.com/TheJumpCloud/jcapi-python) * [Go](https://github.com/TheJumpCloud/jcapi-go) * [Ruby](https://github.com/TheJumpCloud/jcapi-ruby) * [Java](https://github.com/TheJumpCloud/jcapi-java)   # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@jumpcloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SoftwareAppSettings(object):
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
        'allow_update_delay': 'bool',
        'apple_vpp': 'SoftwareAppAppleVpp',
        'asset_kind': 'str',
        'asset_sha256_size': 'int',
        'asset_sha256_strings': 'list[str]',
        'auto_update': 'bool',
        'description': 'str',
        'desired_state': 'str',
        'location': 'str',
        'location_object_id': 'str',
        'package_id': 'str',
        'package_kind': 'str',
        'package_manager': 'str',
        'package_subtitle': 'str',
        'package_version': 'str'
    }

    attribute_map = {
        'allow_update_delay': 'allowUpdateDelay',
        'apple_vpp': 'appleVpp',
        'asset_kind': 'assetKind',
        'asset_sha256_size': 'assetSha256Size',
        'asset_sha256_strings': 'assetSha256Strings',
        'auto_update': 'autoUpdate',
        'description': 'description',
        'desired_state': 'desiredState',
        'location': 'location',
        'location_object_id': 'locationObjectId',
        'package_id': 'packageId',
        'package_kind': 'packageKind',
        'package_manager': 'packageManager',
        'package_subtitle': 'packageSubtitle',
        'package_version': 'packageVersion'
    }

    def __init__(self, allow_update_delay=False, apple_vpp=None, asset_kind=None, asset_sha256_size=None, asset_sha256_strings=None, auto_update=False, description=None, desired_state=None, location=None, location_object_id=None, package_id=None, package_kind=None, package_manager=None, package_subtitle=None, package_version=None):  # noqa: E501
        """SoftwareAppSettings - a model defined in Swagger"""  # noqa: E501
        self._allow_update_delay = None
        self._apple_vpp = None
        self._asset_kind = None
        self._asset_sha256_size = None
        self._asset_sha256_strings = None
        self._auto_update = None
        self._description = None
        self._desired_state = None
        self._location = None
        self._location_object_id = None
        self._package_id = None
        self._package_kind = None
        self._package_manager = None
        self._package_subtitle = None
        self._package_version = None
        self.discriminator = None
        if allow_update_delay is not None:
            self.allow_update_delay = allow_update_delay
        if apple_vpp is not None:
            self.apple_vpp = apple_vpp
        if asset_kind is not None:
            self.asset_kind = asset_kind
        if asset_sha256_size is not None:
            self.asset_sha256_size = asset_sha256_size
        if asset_sha256_strings is not None:
            self.asset_sha256_strings = asset_sha256_strings
        if auto_update is not None:
            self.auto_update = auto_update
        if description is not None:
            self.description = description
        if desired_state is not None:
            self.desired_state = desired_state
        if location is not None:
            self.location = location
        if location_object_id is not None:
            self.location_object_id = location_object_id
        if package_id is not None:
            self.package_id = package_id
        if package_kind is not None:
            self.package_kind = package_kind
        if package_manager is not None:
            self.package_manager = package_manager
        if package_subtitle is not None:
            self.package_subtitle = package_subtitle
        if package_version is not None:
            self.package_version = package_version

    @property
    def allow_update_delay(self):
        """Gets the allow_update_delay of this SoftwareAppSettings.  # noqa: E501


        :return: The allow_update_delay of this SoftwareAppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_update_delay

    @allow_update_delay.setter
    def allow_update_delay(self, allow_update_delay):
        """Sets the allow_update_delay of this SoftwareAppSettings.


        :param allow_update_delay: The allow_update_delay of this SoftwareAppSettings.  # noqa: E501
        :type: bool
        """

        self._allow_update_delay = allow_update_delay

    @property
    def apple_vpp(self):
        """Gets the apple_vpp of this SoftwareAppSettings.  # noqa: E501


        :return: The apple_vpp of this SoftwareAppSettings.  # noqa: E501
        :rtype: SoftwareAppAppleVpp
        """
        return self._apple_vpp

    @apple_vpp.setter
    def apple_vpp(self, apple_vpp):
        """Sets the apple_vpp of this SoftwareAppSettings.


        :param apple_vpp: The apple_vpp of this SoftwareAppSettings.  # noqa: E501
        :type: SoftwareAppAppleVpp
        """

        self._apple_vpp = apple_vpp

    @property
    def asset_kind(self):
        """Gets the asset_kind of this SoftwareAppSettings.  # noqa: E501

        The manifest asset kind (ex: software).  # noqa: E501

        :return: The asset_kind of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._asset_kind

    @asset_kind.setter
    def asset_kind(self, asset_kind):
        """Sets the asset_kind of this SoftwareAppSettings.

        The manifest asset kind (ex: software).  # noqa: E501

        :param asset_kind: The asset_kind of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._asset_kind = asset_kind

    @property
    def asset_sha256_size(self):
        """Gets the asset_sha256_size of this SoftwareAppSettings.  # noqa: E501

        The incremental size to use for summing the package as it is downloaded.  # noqa: E501

        :return: The asset_sha256_size of this SoftwareAppSettings.  # noqa: E501
        :rtype: int
        """
        return self._asset_sha256_size

    @asset_sha256_size.setter
    def asset_sha256_size(self, asset_sha256_size):
        """Sets the asset_sha256_size of this SoftwareAppSettings.

        The incremental size to use for summing the package as it is downloaded.  # noqa: E501

        :param asset_sha256_size: The asset_sha256_size of this SoftwareAppSettings.  # noqa: E501
        :type: int
        """

        self._asset_sha256_size = asset_sha256_size

    @property
    def asset_sha256_strings(self):
        """Gets the asset_sha256_strings of this SoftwareAppSettings.  # noqa: E501

        The array of checksums, one each for the hash size up to the total size of the package.  # noqa: E501

        :return: The asset_sha256_strings of this SoftwareAppSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._asset_sha256_strings

    @asset_sha256_strings.setter
    def asset_sha256_strings(self, asset_sha256_strings):
        """Sets the asset_sha256_strings of this SoftwareAppSettings.

        The array of checksums, one each for the hash size up to the total size of the package.  # noqa: E501

        :param asset_sha256_strings: The asset_sha256_strings of this SoftwareAppSettings.  # noqa: E501
        :type: list[str]
        """

        self._asset_sha256_strings = asset_sha256_strings

    @property
    def auto_update(self):
        """Gets the auto_update of this SoftwareAppSettings.  # noqa: E501


        :return: The auto_update of this SoftwareAppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """Sets the auto_update of this SoftwareAppSettings.


        :param auto_update: The auto_update of this SoftwareAppSettings.  # noqa: E501
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def description(self):
        """Gets the description of this SoftwareAppSettings.  # noqa: E501

        The software app description.  # noqa: E501

        :return: The description of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SoftwareAppSettings.

        The software app description.  # noqa: E501

        :param description: The description of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def desired_state(self):
        """Gets the desired_state of this SoftwareAppSettings.  # noqa: E501

        State of Install or Uninstall  # noqa: E501

        :return: The desired_state of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """Sets the desired_state of this SoftwareAppSettings.

        State of Install or Uninstall  # noqa: E501

        :param desired_state: The desired_state of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._desired_state = desired_state

    @property
    def location(self):
        """Gets the location of this SoftwareAppSettings.  # noqa: E501

        Repository where the app is located within the package manager  # noqa: E501

        :return: The location of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SoftwareAppSettings.

        Repository where the app is located within the package manager  # noqa: E501

        :param location: The location of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def location_object_id(self):
        """Gets the location_object_id of this SoftwareAppSettings.  # noqa: E501

        ID of the repository where the app is located within the package manager  # noqa: E501

        :return: The location_object_id of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._location_object_id

    @location_object_id.setter
    def location_object_id(self, location_object_id):
        """Sets the location_object_id of this SoftwareAppSettings.

        ID of the repository where the app is located within the package manager  # noqa: E501

        :param location_object_id: The location_object_id of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._location_object_id = location_object_id

    @property
    def package_id(self):
        """Gets the package_id of this SoftwareAppSettings.  # noqa: E501


        :return: The package_id of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this SoftwareAppSettings.


        :param package_id: The package_id of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._package_id = package_id

    @property
    def package_kind(self):
        """Gets the package_kind of this SoftwareAppSettings.  # noqa: E501

        The package manifest kind (ex: software-package).  # noqa: E501

        :return: The package_kind of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._package_kind

    @package_kind.setter
    def package_kind(self, package_kind):
        """Sets the package_kind of this SoftwareAppSettings.

        The package manifest kind (ex: software-package).  # noqa: E501

        :param package_kind: The package_kind of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._package_kind = package_kind

    @property
    def package_manager(self):
        """Gets the package_manager of this SoftwareAppSettings.  # noqa: E501

        App store serving the app: APPLE_VPP, CHOCOLATEY, etc.  # noqa: E501

        :return: The package_manager of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._package_manager

    @package_manager.setter
    def package_manager(self, package_manager):
        """Sets the package_manager of this SoftwareAppSettings.

        App store serving the app: APPLE_VPP, CHOCOLATEY, etc.  # noqa: E501

        :param package_manager: The package_manager of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._package_manager = package_manager

    @property
    def package_subtitle(self):
        """Gets the package_subtitle of this SoftwareAppSettings.  # noqa: E501

        The package manifest subtitle.  # noqa: E501

        :return: The package_subtitle of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._package_subtitle

    @package_subtitle.setter
    def package_subtitle(self, package_subtitle):
        """Sets the package_subtitle of this SoftwareAppSettings.

        The package manifest subtitle.  # noqa: E501

        :param package_subtitle: The package_subtitle of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._package_subtitle = package_subtitle

    @property
    def package_version(self):
        """Gets the package_version of this SoftwareAppSettings.  # noqa: E501

        The package manifest version.  # noqa: E501

        :return: The package_version of this SoftwareAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this SoftwareAppSettings.

        The package manifest version.  # noqa: E501

        :param package_version: The package_version of this SoftwareAppSettings.  # noqa: E501
        :type: str
        """

        self._package_version = package_version

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
        if issubclass(SoftwareAppSettings, dict):
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
        if not isinstance(other, SoftwareAppSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
