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

class SystemInsightsInterfaceDetails(object):
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
        'collisions': 'str',
        'connection_id': 'str',
        'connection_status': 'str',
        'description': 'str',
        'dhcp_enabled': 'int',
        'dhcp_lease_expires': 'str',
        'dhcp_lease_obtained': 'str',
        'dhcp_server': 'str',
        'dns_domain': 'str',
        'dns_domain_suffix_search_order': 'str',
        'dns_host_name': 'str',
        'dns_server_search_order': 'str',
        'enabled': 'int',
        'flags': 'int',
        'friendly_name': 'str',
        'ibytes': 'str',
        'idrops': 'str',
        'ierrors': 'str',
        'interface': 'str',
        'ipackets': 'str',
        'last_change': 'str',
        'link_speed': 'str',
        'mac': 'str',
        'manufacturer': 'str',
        'metric': 'int',
        'mtu': 'int',
        'obytes': 'str',
        'odrops': 'str',
        'oerrors': 'str',
        'opackets': 'str',
        'pci_slot': 'str',
        'physical_adapter': 'int',
        'service': 'str',
        'speed': 'int',
        'system_id': 'str',
        'type': 'int'
    }

    attribute_map = {
        'collisions': 'collisions',
        'connection_id': 'connection_id',
        'connection_status': 'connection_status',
        'description': 'description',
        'dhcp_enabled': 'dhcp_enabled',
        'dhcp_lease_expires': 'dhcp_lease_expires',
        'dhcp_lease_obtained': 'dhcp_lease_obtained',
        'dhcp_server': 'dhcp_server',
        'dns_domain': 'dns_domain',
        'dns_domain_suffix_search_order': 'dns_domain_suffix_search_order',
        'dns_host_name': 'dns_host_name',
        'dns_server_search_order': 'dns_server_search_order',
        'enabled': 'enabled',
        'flags': 'flags',
        'friendly_name': 'friendly_name',
        'ibytes': 'ibytes',
        'idrops': 'idrops',
        'ierrors': 'ierrors',
        'interface': 'interface',
        'ipackets': 'ipackets',
        'last_change': 'last_change',
        'link_speed': 'link_speed',
        'mac': 'mac',
        'manufacturer': 'manufacturer',
        'metric': 'metric',
        'mtu': 'mtu',
        'obytes': 'obytes',
        'odrops': 'odrops',
        'oerrors': 'oerrors',
        'opackets': 'opackets',
        'pci_slot': 'pci_slot',
        'physical_adapter': 'physical_adapter',
        'service': 'service',
        'speed': 'speed',
        'system_id': 'system_id',
        'type': 'type'
    }

    def __init__(self, collisions=None, connection_id=None, connection_status=None, description=None, dhcp_enabled=None, dhcp_lease_expires=None, dhcp_lease_obtained=None, dhcp_server=None, dns_domain=None, dns_domain_suffix_search_order=None, dns_host_name=None, dns_server_search_order=None, enabled=None, flags=None, friendly_name=None, ibytes=None, idrops=None, ierrors=None, interface=None, ipackets=None, last_change=None, link_speed=None, mac=None, manufacturer=None, metric=None, mtu=None, obytes=None, odrops=None, oerrors=None, opackets=None, pci_slot=None, physical_adapter=None, service=None, speed=None, system_id=None, type=None):  # noqa: E501
        """SystemInsightsInterfaceDetails - a model defined in Swagger"""  # noqa: E501
        self._collisions = None
        self._connection_id = None
        self._connection_status = None
        self._description = None
        self._dhcp_enabled = None
        self._dhcp_lease_expires = None
        self._dhcp_lease_obtained = None
        self._dhcp_server = None
        self._dns_domain = None
        self._dns_domain_suffix_search_order = None
        self._dns_host_name = None
        self._dns_server_search_order = None
        self._enabled = None
        self._flags = None
        self._friendly_name = None
        self._ibytes = None
        self._idrops = None
        self._ierrors = None
        self._interface = None
        self._ipackets = None
        self._last_change = None
        self._link_speed = None
        self._mac = None
        self._manufacturer = None
        self._metric = None
        self._mtu = None
        self._obytes = None
        self._odrops = None
        self._oerrors = None
        self._opackets = None
        self._pci_slot = None
        self._physical_adapter = None
        self._service = None
        self._speed = None
        self._system_id = None
        self._type = None
        self.discriminator = None
        if collisions is not None:
            self.collisions = collisions
        if connection_id is not None:
            self.connection_id = connection_id
        if connection_status is not None:
            self.connection_status = connection_status
        if description is not None:
            self.description = description
        if dhcp_enabled is not None:
            self.dhcp_enabled = dhcp_enabled
        if dhcp_lease_expires is not None:
            self.dhcp_lease_expires = dhcp_lease_expires
        if dhcp_lease_obtained is not None:
            self.dhcp_lease_obtained = dhcp_lease_obtained
        if dhcp_server is not None:
            self.dhcp_server = dhcp_server
        if dns_domain is not None:
            self.dns_domain = dns_domain
        if dns_domain_suffix_search_order is not None:
            self.dns_domain_suffix_search_order = dns_domain_suffix_search_order
        if dns_host_name is not None:
            self.dns_host_name = dns_host_name
        if dns_server_search_order is not None:
            self.dns_server_search_order = dns_server_search_order
        if enabled is not None:
            self.enabled = enabled
        if flags is not None:
            self.flags = flags
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if ibytes is not None:
            self.ibytes = ibytes
        if idrops is not None:
            self.idrops = idrops
        if ierrors is not None:
            self.ierrors = ierrors
        if interface is not None:
            self.interface = interface
        if ipackets is not None:
            self.ipackets = ipackets
        if last_change is not None:
            self.last_change = last_change
        if link_speed is not None:
            self.link_speed = link_speed
        if mac is not None:
            self.mac = mac
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if metric is not None:
            self.metric = metric
        if mtu is not None:
            self.mtu = mtu
        if obytes is not None:
            self.obytes = obytes
        if odrops is not None:
            self.odrops = odrops
        if oerrors is not None:
            self.oerrors = oerrors
        if opackets is not None:
            self.opackets = opackets
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if physical_adapter is not None:
            self.physical_adapter = physical_adapter
        if service is not None:
            self.service = service
        if speed is not None:
            self.speed = speed
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type

    @property
    def collisions(self):
        """Gets the collisions of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The collisions of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._collisions

    @collisions.setter
    def collisions(self, collisions):
        """Sets the collisions of this SystemInsightsInterfaceDetails.


        :param collisions: The collisions of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._collisions = collisions

    @property
    def connection_id(self):
        """Gets the connection_id of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The connection_id of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this SystemInsightsInterfaceDetails.


        :param connection_id: The connection_id of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def connection_status(self):
        """Gets the connection_status of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The connection_status of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this SystemInsightsInterfaceDetails.


        :param connection_status: The connection_status of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._connection_status = connection_status

    @property
    def description(self):
        """Gets the description of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The description of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemInsightsInterfaceDetails.


        :param description: The description of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dhcp_enabled(self):
        """Gets the dhcp_enabled of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dhcp_enabled of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._dhcp_enabled

    @dhcp_enabled.setter
    def dhcp_enabled(self, dhcp_enabled):
        """Sets the dhcp_enabled of this SystemInsightsInterfaceDetails.


        :param dhcp_enabled: The dhcp_enabled of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._dhcp_enabled = dhcp_enabled

    @property
    def dhcp_lease_expires(self):
        """Gets the dhcp_lease_expires of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dhcp_lease_expires of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_lease_expires

    @dhcp_lease_expires.setter
    def dhcp_lease_expires(self, dhcp_lease_expires):
        """Sets the dhcp_lease_expires of this SystemInsightsInterfaceDetails.


        :param dhcp_lease_expires: The dhcp_lease_expires of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dhcp_lease_expires = dhcp_lease_expires

    @property
    def dhcp_lease_obtained(self):
        """Gets the dhcp_lease_obtained of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dhcp_lease_obtained of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_lease_obtained

    @dhcp_lease_obtained.setter
    def dhcp_lease_obtained(self, dhcp_lease_obtained):
        """Sets the dhcp_lease_obtained of this SystemInsightsInterfaceDetails.


        :param dhcp_lease_obtained: The dhcp_lease_obtained of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dhcp_lease_obtained = dhcp_lease_obtained

    @property
    def dhcp_server(self):
        """Gets the dhcp_server of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dhcp_server of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_server

    @dhcp_server.setter
    def dhcp_server(self, dhcp_server):
        """Sets the dhcp_server of this SystemInsightsInterfaceDetails.


        :param dhcp_server: The dhcp_server of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dhcp_server = dhcp_server

    @property
    def dns_domain(self):
        """Gets the dns_domain of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dns_domain of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """Sets the dns_domain of this SystemInsightsInterfaceDetails.


        :param dns_domain: The dns_domain of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dns_domain = dns_domain

    @property
    def dns_domain_suffix_search_order(self):
        """Gets the dns_domain_suffix_search_order of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dns_domain_suffix_search_order of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dns_domain_suffix_search_order

    @dns_domain_suffix_search_order.setter
    def dns_domain_suffix_search_order(self, dns_domain_suffix_search_order):
        """Sets the dns_domain_suffix_search_order of this SystemInsightsInterfaceDetails.


        :param dns_domain_suffix_search_order: The dns_domain_suffix_search_order of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dns_domain_suffix_search_order = dns_domain_suffix_search_order

    @property
    def dns_host_name(self):
        """Gets the dns_host_name of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dns_host_name of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dns_host_name

    @dns_host_name.setter
    def dns_host_name(self, dns_host_name):
        """Sets the dns_host_name of this SystemInsightsInterfaceDetails.


        :param dns_host_name: The dns_host_name of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dns_host_name = dns_host_name

    @property
    def dns_server_search_order(self):
        """Gets the dns_server_search_order of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The dns_server_search_order of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._dns_server_search_order

    @dns_server_search_order.setter
    def dns_server_search_order(self, dns_server_search_order):
        """Sets the dns_server_search_order of this SystemInsightsInterfaceDetails.


        :param dns_server_search_order: The dns_server_search_order of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._dns_server_search_order = dns_server_search_order

    @property
    def enabled(self):
        """Gets the enabled of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The enabled of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SystemInsightsInterfaceDetails.


        :param enabled: The enabled of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._enabled = enabled

    @property
    def flags(self):
        """Gets the flags of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The flags of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this SystemInsightsInterfaceDetails.


        :param flags: The flags of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._flags = flags

    @property
    def friendly_name(self):
        """Gets the friendly_name of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The friendly_name of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this SystemInsightsInterfaceDetails.


        :param friendly_name: The friendly_name of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def ibytes(self):
        """Gets the ibytes of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The ibytes of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._ibytes

    @ibytes.setter
    def ibytes(self, ibytes):
        """Sets the ibytes of this SystemInsightsInterfaceDetails.


        :param ibytes: The ibytes of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._ibytes = ibytes

    @property
    def idrops(self):
        """Gets the idrops of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The idrops of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._idrops

    @idrops.setter
    def idrops(self, idrops):
        """Sets the idrops of this SystemInsightsInterfaceDetails.


        :param idrops: The idrops of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._idrops = idrops

    @property
    def ierrors(self):
        """Gets the ierrors of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The ierrors of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._ierrors

    @ierrors.setter
    def ierrors(self, ierrors):
        """Sets the ierrors of this SystemInsightsInterfaceDetails.


        :param ierrors: The ierrors of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._ierrors = ierrors

    @property
    def interface(self):
        """Gets the interface of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The interface of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this SystemInsightsInterfaceDetails.


        :param interface: The interface of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._interface = interface

    @property
    def ipackets(self):
        """Gets the ipackets of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The ipackets of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._ipackets

    @ipackets.setter
    def ipackets(self, ipackets):
        """Sets the ipackets of this SystemInsightsInterfaceDetails.


        :param ipackets: The ipackets of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._ipackets = ipackets

    @property
    def last_change(self):
        """Gets the last_change of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The last_change of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._last_change

    @last_change.setter
    def last_change(self, last_change):
        """Sets the last_change of this SystemInsightsInterfaceDetails.


        :param last_change: The last_change of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._last_change = last_change

    @property
    def link_speed(self):
        """Gets the link_speed of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The link_speed of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._link_speed

    @link_speed.setter
    def link_speed(self, link_speed):
        """Sets the link_speed of this SystemInsightsInterfaceDetails.


        :param link_speed: The link_speed of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._link_speed = link_speed

    @property
    def mac(self):
        """Gets the mac of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The mac of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this SystemInsightsInterfaceDetails.


        :param mac: The mac of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def manufacturer(self):
        """Gets the manufacturer of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The manufacturer of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this SystemInsightsInterfaceDetails.


        :param manufacturer: The manufacturer of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def metric(self):
        """Gets the metric of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The metric of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this SystemInsightsInterfaceDetails.


        :param metric: The metric of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._metric = metric

    @property
    def mtu(self):
        """Gets the mtu of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The mtu of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this SystemInsightsInterfaceDetails.


        :param mtu: The mtu of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def obytes(self):
        """Gets the obytes of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The obytes of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._obytes

    @obytes.setter
    def obytes(self, obytes):
        """Sets the obytes of this SystemInsightsInterfaceDetails.


        :param obytes: The obytes of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._obytes = obytes

    @property
    def odrops(self):
        """Gets the odrops of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The odrops of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._odrops

    @odrops.setter
    def odrops(self, odrops):
        """Sets the odrops of this SystemInsightsInterfaceDetails.


        :param odrops: The odrops of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._odrops = odrops

    @property
    def oerrors(self):
        """Gets the oerrors of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The oerrors of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._oerrors

    @oerrors.setter
    def oerrors(self, oerrors):
        """Sets the oerrors of this SystemInsightsInterfaceDetails.


        :param oerrors: The oerrors of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._oerrors = oerrors

    @property
    def opackets(self):
        """Gets the opackets of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The opackets of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._opackets

    @opackets.setter
    def opackets(self, opackets):
        """Sets the opackets of this SystemInsightsInterfaceDetails.


        :param opackets: The opackets of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._opackets = opackets

    @property
    def pci_slot(self):
        """Gets the pci_slot of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The pci_slot of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this SystemInsightsInterfaceDetails.


        :param pci_slot: The pci_slot of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def physical_adapter(self):
        """Gets the physical_adapter of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The physical_adapter of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._physical_adapter

    @physical_adapter.setter
    def physical_adapter(self, physical_adapter):
        """Sets the physical_adapter of this SystemInsightsInterfaceDetails.


        :param physical_adapter: The physical_adapter of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._physical_adapter = physical_adapter

    @property
    def service(self):
        """Gets the service of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The service of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SystemInsightsInterfaceDetails.


        :param service: The service of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def speed(self):
        """Gets the speed of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The speed of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this SystemInsightsInterfaceDetails.


        :param speed: The speed of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._speed = speed

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The system_id of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsInterfaceDetails.


        :param system_id: The system_id of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this SystemInsightsInterfaceDetails.  # noqa: E501


        :return: The type of this SystemInsightsInterfaceDetails.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsInterfaceDetails.


        :param type: The type of this SystemInsightsInterfaceDetails.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if issubclass(SystemInsightsInterfaceDetails, dict):
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
        if not isinstance(other, SystemInsightsInterfaceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
