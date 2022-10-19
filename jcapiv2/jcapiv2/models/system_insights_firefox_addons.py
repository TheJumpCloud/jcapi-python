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

class SystemInsightsFirefoxAddons(object):
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
        'active': 'int',
        'autoupdate': 'int',
        'collection_time': 'str',
        'creator': 'str',
        'description': 'str',
        'disabled': 'int',
        'identifier': 'str',
        'location': 'str',
        'name': 'str',
        'path': 'str',
        'source_url': 'str',
        'system_id': 'str',
        'type': 'str',
        'uid': 'str',
        'version': 'str',
        'visible': 'int'
    }

    attribute_map = {
        'active': 'active',
        'autoupdate': 'autoupdate',
        'collection_time': 'collection_time',
        'creator': 'creator',
        'description': 'description',
        'disabled': 'disabled',
        'identifier': 'identifier',
        'location': 'location',
        'name': 'name',
        'path': 'path',
        'source_url': 'source_url',
        'system_id': 'system_id',
        'type': 'type',
        'uid': 'uid',
        'version': 'version',
        'visible': 'visible'
    }

    def __init__(self, active=None, autoupdate=None, collection_time=None, creator=None, description=None, disabled=None, identifier=None, location=None, name=None, path=None, source_url=None, system_id=None, type=None, uid=None, version=None, visible=None):  # noqa: E501
        """SystemInsightsFirefoxAddons - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._autoupdate = None
        self._collection_time = None
        self._creator = None
        self._description = None
        self._disabled = None
        self._identifier = None
        self._location = None
        self._name = None
        self._path = None
        self._source_url = None
        self._system_id = None
        self._type = None
        self._uid = None
        self._version = None
        self._visible = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if autoupdate is not None:
            self.autoupdate = autoupdate
        if collection_time is not None:
            self.collection_time = collection_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if disabled is not None:
            self.disabled = disabled
        if identifier is not None:
            self.identifier = identifier
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if source_url is not None:
            self.source_url = source_url
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid
        if version is not None:
            self.version = version
        if visible is not None:
            self.visible = visible

    @property
    def active(self):
        """Gets the active of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The active of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SystemInsightsFirefoxAddons.


        :param active: The active of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._active = active

    @property
    def autoupdate(self):
        """Gets the autoupdate of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The autoupdate of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._autoupdate

    @autoupdate.setter
    def autoupdate(self, autoupdate):
        """Sets the autoupdate of this SystemInsightsFirefoxAddons.


        :param autoupdate: The autoupdate of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._autoupdate = autoupdate

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The collection_time of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsFirefoxAddons.


        :param collection_time: The collection_time of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def creator(self):
        """Gets the creator of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The creator of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this SystemInsightsFirefoxAddons.


        :param creator: The creator of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The description of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemInsightsFirefoxAddons.


        :param description: The description of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The disabled of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SystemInsightsFirefoxAddons.


        :param disabled: The disabled of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._disabled = disabled

    @property
    def identifier(self):
        """Gets the identifier of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The identifier of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this SystemInsightsFirefoxAddons.


        :param identifier: The identifier of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def location(self):
        """Gets the location of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The location of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SystemInsightsFirefoxAddons.


        :param location: The location of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The name of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsFirefoxAddons.


        :param name: The name of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The path of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsFirefoxAddons.


        :param path: The path of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def source_url(self):
        """Gets the source_url of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The source_url of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this SystemInsightsFirefoxAddons.


        :param source_url: The source_url of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The system_id of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsFirefoxAddons.


        :param system_id: The system_id of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The type of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsFirefoxAddons.


        :param type: The type of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The uid of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SystemInsightsFirefoxAddons.


        :param uid: The uid of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def version(self):
        """Gets the version of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The version of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInsightsFirefoxAddons.


        :param version: The version of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def visible(self):
        """Gets the visible of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The visible of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this SystemInsightsFirefoxAddons.


        :param visible: The visible of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._visible = visible

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
        if issubclass(SystemInsightsFirefoxAddons, dict):
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
        if not isinstance(other, SystemInsightsFirefoxAddons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
