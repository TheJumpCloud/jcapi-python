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

class SystemInsightsTpmInfo(object):
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
        'activated': 'float',
        'collection_time': 'str',
        'enabled': 'float',
        'manufacturer_id': 'float',
        'manufacturer_name': 'str',
        'manufacturer_version': 'str',
        'owned': 'float',
        'physical_presence_version': 'str',
        'product_name': 'str',
        'spec_version': 'str',
        'system_id': 'str'
    }

    attribute_map = {
        'activated': 'activated',
        'collection_time': 'collection_time',
        'enabled': 'enabled',
        'manufacturer_id': 'manufacturer_id',
        'manufacturer_name': 'manufacturer_name',
        'manufacturer_version': 'manufacturer_version',
        'owned': 'owned',
        'physical_presence_version': 'physical_presence_version',
        'product_name': 'product_name',
        'spec_version': 'spec_version',
        'system_id': 'system_id'
    }

    def __init__(self, activated=None, collection_time=None, enabled=None, manufacturer_id=None, manufacturer_name=None, manufacturer_version=None, owned=None, physical_presence_version=None, product_name=None, spec_version=None, system_id=None):  # noqa: E501
        """SystemInsightsTpmInfo - a model defined in Swagger"""  # noqa: E501
        self._activated = None
        self._collection_time = None
        self._enabled = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._manufacturer_version = None
        self._owned = None
        self._physical_presence_version = None
        self._product_name = None
        self._spec_version = None
        self._system_id = None
        self.discriminator = None
        if activated is not None:
            self.activated = activated
        if collection_time is not None:
            self.collection_time = collection_time
        if enabled is not None:
            self.enabled = enabled
        if manufacturer_id is not None:
            self.manufacturer_id = manufacturer_id
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if manufacturer_version is not None:
            self.manufacturer_version = manufacturer_version
        if owned is not None:
            self.owned = owned
        if physical_presence_version is not None:
            self.physical_presence_version = physical_presence_version
        if product_name is not None:
            self.product_name = product_name
        if spec_version is not None:
            self.spec_version = spec_version
        if system_id is not None:
            self.system_id = system_id

    @property
    def activated(self):
        """Gets the activated of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The activated of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: float
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this SystemInsightsTpmInfo.


        :param activated: The activated of this SystemInsightsTpmInfo.  # noqa: E501
        :type: float
        """

        self._activated = activated

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The collection_time of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsTpmInfo.


        :param collection_time: The collection_time of this SystemInsightsTpmInfo.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def enabled(self):
        """Gets the enabled of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The enabled of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: float
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SystemInsightsTpmInfo.


        :param enabled: The enabled of this SystemInsightsTpmInfo.  # noqa: E501
        :type: float
        """

        self._enabled = enabled

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The manufacturer_id of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: float
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this SystemInsightsTpmInfo.


        :param manufacturer_id: The manufacturer_id of this SystemInsightsTpmInfo.  # noqa: E501
        :type: float
        """

        self._manufacturer_id = manufacturer_id

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The manufacturer_name of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this SystemInsightsTpmInfo.


        :param manufacturer_name: The manufacturer_name of this SystemInsightsTpmInfo.  # noqa: E501
        :type: str
        """

        self._manufacturer_name = manufacturer_name

    @property
    def manufacturer_version(self):
        """Gets the manufacturer_version of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The manufacturer_version of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_version

    @manufacturer_version.setter
    def manufacturer_version(self, manufacturer_version):
        """Sets the manufacturer_version of this SystemInsightsTpmInfo.


        :param manufacturer_version: The manufacturer_version of this SystemInsightsTpmInfo.  # noqa: E501
        :type: str
        """

        self._manufacturer_version = manufacturer_version

    @property
    def owned(self):
        """Gets the owned of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The owned of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: float
        """
        return self._owned

    @owned.setter
    def owned(self, owned):
        """Sets the owned of this SystemInsightsTpmInfo.


        :param owned: The owned of this SystemInsightsTpmInfo.  # noqa: E501
        :type: float
        """

        self._owned = owned

    @property
    def physical_presence_version(self):
        """Gets the physical_presence_version of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The physical_presence_version of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._physical_presence_version

    @physical_presence_version.setter
    def physical_presence_version(self, physical_presence_version):
        """Sets the physical_presence_version of this SystemInsightsTpmInfo.


        :param physical_presence_version: The physical_presence_version of this SystemInsightsTpmInfo.  # noqa: E501
        :type: str
        """

        self._physical_presence_version = physical_presence_version

    @property
    def product_name(self):
        """Gets the product_name of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The product_name of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SystemInsightsTpmInfo.


        :param product_name: The product_name of this SystemInsightsTpmInfo.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def spec_version(self):
        """Gets the spec_version of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The spec_version of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._spec_version

    @spec_version.setter
    def spec_version(self, spec_version):
        """Sets the spec_version of this SystemInsightsTpmInfo.


        :param spec_version: The spec_version of this SystemInsightsTpmInfo.  # noqa: E501
        :type: str
        """

        self._spec_version = spec_version

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsTpmInfo.  # noqa: E501


        :return: The system_id of this SystemInsightsTpmInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsTpmInfo.


        :param system_id: The system_id of this SystemInsightsTpmInfo.  # noqa: E501
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
        if issubclass(SystemInsightsTpmInfo, dict):
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
        if not isinstance(other, SystemInsightsTpmInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
