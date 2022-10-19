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

class SystemInsightsSystemInfo(object):
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
        'collection_time': 'str',
        'computer_name': 'str',
        'cpu_brand': 'str',
        'cpu_logical_cores': 'int',
        'cpu_microcode': 'str',
        'cpu_physical_cores': 'int',
        'cpu_subtype': 'str',
        'cpu_type': 'str',
        'hardware_model': 'str',
        'hardware_serial': 'str',
        'hardware_vendor': 'str',
        'hardware_version': 'str',
        'hostname': 'str',
        'local_hostname': 'str',
        'physical_memory': 'str',
        'system_id': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'computer_name': 'computer_name',
        'cpu_brand': 'cpu_brand',
        'cpu_logical_cores': 'cpu_logical_cores',
        'cpu_microcode': 'cpu_microcode',
        'cpu_physical_cores': 'cpu_physical_cores',
        'cpu_subtype': 'cpu_subtype',
        'cpu_type': 'cpu_type',
        'hardware_model': 'hardware_model',
        'hardware_serial': 'hardware_serial',
        'hardware_vendor': 'hardware_vendor',
        'hardware_version': 'hardware_version',
        'hostname': 'hostname',
        'local_hostname': 'local_hostname',
        'physical_memory': 'physical_memory',
        'system_id': 'system_id',
        'uuid': 'uuid'
    }

    def __init__(self, collection_time=None, computer_name=None, cpu_brand=None, cpu_logical_cores=None, cpu_microcode=None, cpu_physical_cores=None, cpu_subtype=None, cpu_type=None, hardware_model=None, hardware_serial=None, hardware_vendor=None, hardware_version=None, hostname=None, local_hostname=None, physical_memory=None, system_id=None, uuid=None):  # noqa: E501
        """SystemInsightsSystemInfo - a model defined in Swagger"""  # noqa: E501
        self._collection_time = None
        self._computer_name = None
        self._cpu_brand = None
        self._cpu_logical_cores = None
        self._cpu_microcode = None
        self._cpu_physical_cores = None
        self._cpu_subtype = None
        self._cpu_type = None
        self._hardware_model = None
        self._hardware_serial = None
        self._hardware_vendor = None
        self._hardware_version = None
        self._hostname = None
        self._local_hostname = None
        self._physical_memory = None
        self._system_id = None
        self._uuid = None
        self.discriminator = None
        if collection_time is not None:
            self.collection_time = collection_time
        if computer_name is not None:
            self.computer_name = computer_name
        if cpu_brand is not None:
            self.cpu_brand = cpu_brand
        if cpu_logical_cores is not None:
            self.cpu_logical_cores = cpu_logical_cores
        if cpu_microcode is not None:
            self.cpu_microcode = cpu_microcode
        if cpu_physical_cores is not None:
            self.cpu_physical_cores = cpu_physical_cores
        if cpu_subtype is not None:
            self.cpu_subtype = cpu_subtype
        if cpu_type is not None:
            self.cpu_type = cpu_type
        if hardware_model is not None:
            self.hardware_model = hardware_model
        if hardware_serial is not None:
            self.hardware_serial = hardware_serial
        if hardware_vendor is not None:
            self.hardware_vendor = hardware_vendor
        if hardware_version is not None:
            self.hardware_version = hardware_version
        if hostname is not None:
            self.hostname = hostname
        if local_hostname is not None:
            self.local_hostname = local_hostname
        if physical_memory is not None:
            self.physical_memory = physical_memory
        if system_id is not None:
            self.system_id = system_id
        if uuid is not None:
            self.uuid = uuid

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The collection_time of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsSystemInfo.


        :param collection_time: The collection_time of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def computer_name(self):
        """Gets the computer_name of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The computer_name of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this SystemInsightsSystemInfo.


        :param computer_name: The computer_name of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._computer_name = computer_name

    @property
    def cpu_brand(self):
        """Gets the cpu_brand of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The cpu_brand of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_brand

    @cpu_brand.setter
    def cpu_brand(self, cpu_brand):
        """Sets the cpu_brand of this SystemInsightsSystemInfo.


        :param cpu_brand: The cpu_brand of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._cpu_brand = cpu_brand

    @property
    def cpu_logical_cores(self):
        """Gets the cpu_logical_cores of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The cpu_logical_cores of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._cpu_logical_cores

    @cpu_logical_cores.setter
    def cpu_logical_cores(self, cpu_logical_cores):
        """Sets the cpu_logical_cores of this SystemInsightsSystemInfo.


        :param cpu_logical_cores: The cpu_logical_cores of this SystemInsightsSystemInfo.  # noqa: E501
        :type: int
        """

        self._cpu_logical_cores = cpu_logical_cores

    @property
    def cpu_microcode(self):
        """Gets the cpu_microcode of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The cpu_microcode of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_microcode

    @cpu_microcode.setter
    def cpu_microcode(self, cpu_microcode):
        """Sets the cpu_microcode of this SystemInsightsSystemInfo.


        :param cpu_microcode: The cpu_microcode of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._cpu_microcode = cpu_microcode

    @property
    def cpu_physical_cores(self):
        """Gets the cpu_physical_cores of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The cpu_physical_cores of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._cpu_physical_cores

    @cpu_physical_cores.setter
    def cpu_physical_cores(self, cpu_physical_cores):
        """Sets the cpu_physical_cores of this SystemInsightsSystemInfo.


        :param cpu_physical_cores: The cpu_physical_cores of this SystemInsightsSystemInfo.  # noqa: E501
        :type: int
        """

        self._cpu_physical_cores = cpu_physical_cores

    @property
    def cpu_subtype(self):
        """Gets the cpu_subtype of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The cpu_subtype of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_subtype

    @cpu_subtype.setter
    def cpu_subtype(self, cpu_subtype):
        """Sets the cpu_subtype of this SystemInsightsSystemInfo.


        :param cpu_subtype: The cpu_subtype of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._cpu_subtype = cpu_subtype

    @property
    def cpu_type(self):
        """Gets the cpu_type of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The cpu_type of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this SystemInsightsSystemInfo.


        :param cpu_type: The cpu_type of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._cpu_type = cpu_type

    @property
    def hardware_model(self):
        """Gets the hardware_model of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The hardware_model of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_model

    @hardware_model.setter
    def hardware_model(self, hardware_model):
        """Sets the hardware_model of this SystemInsightsSystemInfo.


        :param hardware_model: The hardware_model of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._hardware_model = hardware_model

    @property
    def hardware_serial(self):
        """Gets the hardware_serial of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The hardware_serial of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_serial

    @hardware_serial.setter
    def hardware_serial(self, hardware_serial):
        """Sets the hardware_serial of this SystemInsightsSystemInfo.


        :param hardware_serial: The hardware_serial of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._hardware_serial = hardware_serial

    @property
    def hardware_vendor(self):
        """Gets the hardware_vendor of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The hardware_vendor of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_vendor

    @hardware_vendor.setter
    def hardware_vendor(self, hardware_vendor):
        """Sets the hardware_vendor of this SystemInsightsSystemInfo.


        :param hardware_vendor: The hardware_vendor of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._hardware_vendor = hardware_vendor

    @property
    def hardware_version(self):
        """Gets the hardware_version of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The hardware_version of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_version

    @hardware_version.setter
    def hardware_version(self, hardware_version):
        """Sets the hardware_version of this SystemInsightsSystemInfo.


        :param hardware_version: The hardware_version of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._hardware_version = hardware_version

    @property
    def hostname(self):
        """Gets the hostname of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The hostname of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this SystemInsightsSystemInfo.


        :param hostname: The hostname of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def local_hostname(self):
        """Gets the local_hostname of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The local_hostname of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._local_hostname

    @local_hostname.setter
    def local_hostname(self, local_hostname):
        """Sets the local_hostname of this SystemInsightsSystemInfo.


        :param local_hostname: The local_hostname of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._local_hostname = local_hostname

    @property
    def physical_memory(self):
        """Gets the physical_memory of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The physical_memory of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._physical_memory

    @physical_memory.setter
    def physical_memory(self, physical_memory):
        """Sets the physical_memory of this SystemInsightsSystemInfo.


        :param physical_memory: The physical_memory of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._physical_memory = physical_memory

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The system_id of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsSystemInfo.


        :param system_id: The system_id of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def uuid(self):
        """Gets the uuid of this SystemInsightsSystemInfo.  # noqa: E501


        :return: The uuid of this SystemInsightsSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SystemInsightsSystemInfo.


        :param uuid: The uuid of this SystemInsightsSystemInfo.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(SystemInsightsSystemInfo, dict):
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
        if not isinstance(other, SystemInsightsSystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
