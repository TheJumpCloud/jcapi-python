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

class SystemInsightsAzureInstanceMetadata(object):
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
        'location': 'str',
        'name': 'str',
        'offer': 'str',
        'os_type': 'str',
        'placement_group_id': 'str',
        'platform_fault_domain': 'str',
        'platform_update_domain': 'str',
        'publisher': 'str',
        'resource_group_name': 'str',
        'sku': 'str',
        'subscription_id': 'str',
        'system_id': 'str',
        'version': 'str',
        'vm_id': 'str',
        'vm_scale_set_name': 'str',
        'vm_size': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'location': 'location',
        'name': 'name',
        'offer': 'offer',
        'os_type': 'os_type',
        'placement_group_id': 'placement_group_id',
        'platform_fault_domain': 'platform_fault_domain',
        'platform_update_domain': 'platform_update_domain',
        'publisher': 'publisher',
        'resource_group_name': 'resource_group_name',
        'sku': 'sku',
        'subscription_id': 'subscription_id',
        'system_id': 'system_id',
        'version': 'version',
        'vm_id': 'vm_id',
        'vm_scale_set_name': 'vm_scale_set_name',
        'vm_size': 'vm_size',
        'zone': 'zone'
    }

    def __init__(self, collection_time=None, location=None, name=None, offer=None, os_type=None, placement_group_id=None, platform_fault_domain=None, platform_update_domain=None, publisher=None, resource_group_name=None, sku=None, subscription_id=None, system_id=None, version=None, vm_id=None, vm_scale_set_name=None, vm_size=None, zone=None):  # noqa: E501
        """SystemInsightsAzureInstanceMetadata - a model defined in Swagger"""  # noqa: E501
        self._collection_time = None
        self._location = None
        self._name = None
        self._offer = None
        self._os_type = None
        self._placement_group_id = None
        self._platform_fault_domain = None
        self._platform_update_domain = None
        self._publisher = None
        self._resource_group_name = None
        self._sku = None
        self._subscription_id = None
        self._system_id = None
        self._version = None
        self._vm_id = None
        self._vm_scale_set_name = None
        self._vm_size = None
        self._zone = None
        self.discriminator = None
        if collection_time is not None:
            self.collection_time = collection_time
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if offer is not None:
            self.offer = offer
        if os_type is not None:
            self.os_type = os_type
        if placement_group_id is not None:
            self.placement_group_id = placement_group_id
        if platform_fault_domain is not None:
            self.platform_fault_domain = platform_fault_domain
        if platform_update_domain is not None:
            self.platform_update_domain = platform_update_domain
        if publisher is not None:
            self.publisher = publisher
        if resource_group_name is not None:
            self.resource_group_name = resource_group_name
        if sku is not None:
            self.sku = sku
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if system_id is not None:
            self.system_id = system_id
        if version is not None:
            self.version = version
        if vm_id is not None:
            self.vm_id = vm_id
        if vm_scale_set_name is not None:
            self.vm_scale_set_name = vm_scale_set_name
        if vm_size is not None:
            self.vm_size = vm_size
        if zone is not None:
            self.zone = zone

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The collection_time of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsAzureInstanceMetadata.


        :param collection_time: The collection_time of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def location(self):
        """Gets the location of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The location of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SystemInsightsAzureInstanceMetadata.


        :param location: The location of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsAzureInstanceMetadata.


        :param name: The name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def offer(self):
        """Gets the offer of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The offer of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this SystemInsightsAzureInstanceMetadata.


        :param offer: The offer of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._offer = offer

    @property
    def os_type(self):
        """Gets the os_type of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The os_type of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this SystemInsightsAzureInstanceMetadata.


        :param os_type: The os_type of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def placement_group_id(self):
        """Gets the placement_group_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The placement_group_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._placement_group_id

    @placement_group_id.setter
    def placement_group_id(self, placement_group_id):
        """Sets the placement_group_id of this SystemInsightsAzureInstanceMetadata.


        :param placement_group_id: The placement_group_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._placement_group_id = placement_group_id

    @property
    def platform_fault_domain(self):
        """Gets the platform_fault_domain of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The platform_fault_domain of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._platform_fault_domain

    @platform_fault_domain.setter
    def platform_fault_domain(self, platform_fault_domain):
        """Sets the platform_fault_domain of this SystemInsightsAzureInstanceMetadata.


        :param platform_fault_domain: The platform_fault_domain of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._platform_fault_domain = platform_fault_domain

    @property
    def platform_update_domain(self):
        """Gets the platform_update_domain of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The platform_update_domain of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._platform_update_domain

    @platform_update_domain.setter
    def platform_update_domain(self, platform_update_domain):
        """Sets the platform_update_domain of this SystemInsightsAzureInstanceMetadata.


        :param platform_update_domain: The platform_update_domain of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._platform_update_domain = platform_update_domain

    @property
    def publisher(self):
        """Gets the publisher of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The publisher of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this SystemInsightsAzureInstanceMetadata.


        :param publisher: The publisher of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._publisher = publisher

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The resource_group_name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this SystemInsightsAzureInstanceMetadata.


        :param resource_group_name: The resource_group_name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._resource_group_name = resource_group_name

    @property
    def sku(self):
        """Gets the sku of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The sku of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this SystemInsightsAzureInstanceMetadata.


        :param sku: The sku of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The subscription_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SystemInsightsAzureInstanceMetadata.


        :param subscription_id: The subscription_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The system_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsAzureInstanceMetadata.


        :param system_id: The system_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def version(self):
        """Gets the version of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The version of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInsightsAzureInstanceMetadata.


        :param version: The version of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def vm_id(self):
        """Gets the vm_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The vm_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this SystemInsightsAzureInstanceMetadata.


        :param vm_id: The vm_id of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._vm_id = vm_id

    @property
    def vm_scale_set_name(self):
        """Gets the vm_scale_set_name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The vm_scale_set_name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._vm_scale_set_name

    @vm_scale_set_name.setter
    def vm_scale_set_name(self, vm_scale_set_name):
        """Sets the vm_scale_set_name of this SystemInsightsAzureInstanceMetadata.


        :param vm_scale_set_name: The vm_scale_set_name of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._vm_scale_set_name = vm_scale_set_name

    @property
    def vm_size(self):
        """Gets the vm_size of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The vm_size of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._vm_size

    @vm_size.setter
    def vm_size(self, vm_size):
        """Sets the vm_size of this SystemInsightsAzureInstanceMetadata.


        :param vm_size: The vm_size of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._vm_size = vm_size

    @property
    def zone(self):
        """Gets the zone of this SystemInsightsAzureInstanceMetadata.  # noqa: E501


        :return: The zone of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this SystemInsightsAzureInstanceMetadata.


        :param zone: The zone of this SystemInsightsAzureInstanceMetadata.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if issubclass(SystemInsightsAzureInstanceMetadata, dict):
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
        if not isinstance(other, SystemInsightsAzureInstanceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
