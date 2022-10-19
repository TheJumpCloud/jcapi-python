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

class SystemInsightsWifiNetworks(object):
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
        'auto_login': 'float',
        'captive_portal': 'float',
        'collection_time': 'str',
        'disabled': 'float',
        'last_connected': 'float',
        'network_name': 'str',
        'passpoint': 'float',
        'possibly_hidden': 'float',
        'roaming': 'float',
        'roaming_profile': 'str',
        'security_type': 'str',
        'ssid': 'str',
        'system_id': 'str',
        'temporarily_disabled': 'float'
    }

    attribute_map = {
        'auto_login': 'auto_login',
        'captive_portal': 'captive_portal',
        'collection_time': 'collection_time',
        'disabled': 'disabled',
        'last_connected': 'last_connected',
        'network_name': 'network_name',
        'passpoint': 'passpoint',
        'possibly_hidden': 'possibly_hidden',
        'roaming': 'roaming',
        'roaming_profile': 'roaming_profile',
        'security_type': 'security_type',
        'ssid': 'ssid',
        'system_id': 'system_id',
        'temporarily_disabled': 'temporarily_disabled'
    }

    def __init__(self, auto_login=None, captive_portal=None, collection_time=None, disabled=None, last_connected=None, network_name=None, passpoint=None, possibly_hidden=None, roaming=None, roaming_profile=None, security_type=None, ssid=None, system_id=None, temporarily_disabled=None):  # noqa: E501
        """SystemInsightsWifiNetworks - a model defined in Swagger"""  # noqa: E501
        self._auto_login = None
        self._captive_portal = None
        self._collection_time = None
        self._disabled = None
        self._last_connected = None
        self._network_name = None
        self._passpoint = None
        self._possibly_hidden = None
        self._roaming = None
        self._roaming_profile = None
        self._security_type = None
        self._ssid = None
        self._system_id = None
        self._temporarily_disabled = None
        self.discriminator = None
        if auto_login is not None:
            self.auto_login = auto_login
        if captive_portal is not None:
            self.captive_portal = captive_portal
        if collection_time is not None:
            self.collection_time = collection_time
        if disabled is not None:
            self.disabled = disabled
        if last_connected is not None:
            self.last_connected = last_connected
        if network_name is not None:
            self.network_name = network_name
        if passpoint is not None:
            self.passpoint = passpoint
        if possibly_hidden is not None:
            self.possibly_hidden = possibly_hidden
        if roaming is not None:
            self.roaming = roaming
        if roaming_profile is not None:
            self.roaming_profile = roaming_profile
        if security_type is not None:
            self.security_type = security_type
        if ssid is not None:
            self.ssid = ssid
        if system_id is not None:
            self.system_id = system_id
        if temporarily_disabled is not None:
            self.temporarily_disabled = temporarily_disabled

    @property
    def auto_login(self):
        """Gets the auto_login of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The auto_login of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._auto_login

    @auto_login.setter
    def auto_login(self, auto_login):
        """Sets the auto_login of this SystemInsightsWifiNetworks.


        :param auto_login: The auto_login of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._auto_login = auto_login

    @property
    def captive_portal(self):
        """Gets the captive_portal of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The captive_portal of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._captive_portal

    @captive_portal.setter
    def captive_portal(self, captive_portal):
        """Sets the captive_portal of this SystemInsightsWifiNetworks.


        :param captive_portal: The captive_portal of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._captive_portal = captive_portal

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The collection_time of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsWifiNetworks.


        :param collection_time: The collection_time of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def disabled(self):
        """Gets the disabled of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The disabled of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SystemInsightsWifiNetworks.


        :param disabled: The disabled of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._disabled = disabled

    @property
    def last_connected(self):
        """Gets the last_connected of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The last_connected of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._last_connected

    @last_connected.setter
    def last_connected(self, last_connected):
        """Sets the last_connected of this SystemInsightsWifiNetworks.


        :param last_connected: The last_connected of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._last_connected = last_connected

    @property
    def network_name(self):
        """Gets the network_name of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The network_name of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """Sets the network_name of this SystemInsightsWifiNetworks.


        :param network_name: The network_name of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: str
        """

        self._network_name = network_name

    @property
    def passpoint(self):
        """Gets the passpoint of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The passpoint of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._passpoint

    @passpoint.setter
    def passpoint(self, passpoint):
        """Sets the passpoint of this SystemInsightsWifiNetworks.


        :param passpoint: The passpoint of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._passpoint = passpoint

    @property
    def possibly_hidden(self):
        """Gets the possibly_hidden of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The possibly_hidden of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._possibly_hidden

    @possibly_hidden.setter
    def possibly_hidden(self, possibly_hidden):
        """Sets the possibly_hidden of this SystemInsightsWifiNetworks.


        :param possibly_hidden: The possibly_hidden of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._possibly_hidden = possibly_hidden

    @property
    def roaming(self):
        """Gets the roaming of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The roaming of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._roaming

    @roaming.setter
    def roaming(self, roaming):
        """Sets the roaming of this SystemInsightsWifiNetworks.


        :param roaming: The roaming of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._roaming = roaming

    @property
    def roaming_profile(self):
        """Gets the roaming_profile of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The roaming_profile of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: str
        """
        return self._roaming_profile

    @roaming_profile.setter
    def roaming_profile(self, roaming_profile):
        """Sets the roaming_profile of this SystemInsightsWifiNetworks.


        :param roaming_profile: The roaming_profile of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: str
        """

        self._roaming_profile = roaming_profile

    @property
    def security_type(self):
        """Gets the security_type of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The security_type of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this SystemInsightsWifiNetworks.


        :param security_type: The security_type of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: str
        """

        self._security_type = security_type

    @property
    def ssid(self):
        """Gets the ssid of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The ssid of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this SystemInsightsWifiNetworks.


        :param ssid: The ssid of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The system_id of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsWifiNetworks.


        :param system_id: The system_id of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def temporarily_disabled(self):
        """Gets the temporarily_disabled of this SystemInsightsWifiNetworks.  # noqa: E501


        :return: The temporarily_disabled of this SystemInsightsWifiNetworks.  # noqa: E501
        :rtype: float
        """
        return self._temporarily_disabled

    @temporarily_disabled.setter
    def temporarily_disabled(self, temporarily_disabled):
        """Sets the temporarily_disabled of this SystemInsightsWifiNetworks.


        :param temporarily_disabled: The temporarily_disabled of this SystemInsightsWifiNetworks.  # noqa: E501
        :type: float
        """

        self._temporarily_disabled = temporarily_disabled

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
        if issubclass(SystemInsightsWifiNetworks, dict):
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
        if not isinstance(other, SystemInsightsWifiNetworks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
