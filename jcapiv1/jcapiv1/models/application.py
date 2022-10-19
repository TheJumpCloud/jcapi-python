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

class Application(object):
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
        'id': 'str',
        'active': 'bool',
        'beta': 'bool',
        'color': 'str',
        'config': 'ApplicationConfig',
        'created': 'str',
        'database_attributes': 'list[object]',
        'description': 'str',
        'display_label': 'str',
        'display_name': 'str',
        'learn_more': 'str',
        'logo': 'ApplicationLogo',
        'name': 'str',
        'organization': 'str',
        'sso': 'Sso',
        'sso_url': 'str'
    }

    attribute_map = {
        'id': '_id',
        'active': 'active',
        'beta': 'beta',
        'color': 'color',
        'config': 'config',
        'created': 'created',
        'database_attributes': 'databaseAttributes',
        'description': 'description',
        'display_label': 'displayLabel',
        'display_name': 'displayName',
        'learn_more': 'learnMore',
        'logo': 'logo',
        'name': 'name',
        'organization': 'organization',
        'sso': 'sso',
        'sso_url': 'ssoUrl'
    }

    def __init__(self, id=None, active=None, beta=None, color=None, config=None, created=None, database_attributes=None, description=None, display_label=None, display_name=None, learn_more=None, logo=None, name=None, organization=None, sso=None, sso_url=None):  # noqa: E501
        """Application - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._active = None
        self._beta = None
        self._color = None
        self._config = None
        self._created = None
        self._database_attributes = None
        self._description = None
        self._display_label = None
        self._display_name = None
        self._learn_more = None
        self._logo = None
        self._name = None
        self._organization = None
        self._sso = None
        self._sso_url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if beta is not None:
            self.beta = beta
        if color is not None:
            self.color = color
        self.config = config
        if created is not None:
            self.created = created
        if database_attributes is not None:
            self.database_attributes = database_attributes
        if description is not None:
            self.description = description
        if display_label is not None:
            self.display_label = display_label
        if display_name is not None:
            self.display_name = display_name
        if learn_more is not None:
            self.learn_more = learn_more
        if logo is not None:
            self.logo = logo
        self.name = name
        if organization is not None:
            self.organization = organization
        if sso is not None:
            self.sso = sso
        self.sso_url = sso_url

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501


        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.


        :param id: The id of this Application.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this Application.  # noqa: E501


        :return: The active of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Application.


        :param active: The active of this Application.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def beta(self):
        """Gets the beta of this Application.  # noqa: E501


        :return: The beta of this Application.  # noqa: E501
        :rtype: bool
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """Sets the beta of this Application.


        :param beta: The beta of this Application.  # noqa: E501
        :type: bool
        """

        self._beta = beta

    @property
    def color(self):
        """Gets the color of this Application.  # noqa: E501


        :return: The color of this Application.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Application.


        :param color: The color of this Application.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "#202D38", "#005466", "#3E8696", "#006CAC", "#0617AC", "#7C6ADA", "#D5779D", "#9E2F00", "#FFB000", "#58C469", "#57C49F", "#FF6C03"]  # noqa: E501
        if color not in allowed_values:
            raise ValueError(
                "Invalid value for `color` ({0}), must be one of {1}"  # noqa: E501
                .format(color, allowed_values)
            )

        self._color = color

    @property
    def config(self):
        """Gets the config of this Application.  # noqa: E501


        :return: The config of this Application.  # noqa: E501
        :rtype: ApplicationConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Application.


        :param config: The config of this Application.  # noqa: E501
        :type: ApplicationConfig
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def created(self):
        """Gets the created of this Application.  # noqa: E501


        :return: The created of this Application.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Application.


        :param created: The created of this Application.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def database_attributes(self):
        """Gets the database_attributes of this Application.  # noqa: E501


        :return: The database_attributes of this Application.  # noqa: E501
        :rtype: list[object]
        """
        return self._database_attributes

    @database_attributes.setter
    def database_attributes(self, database_attributes):
        """Sets the database_attributes of this Application.


        :param database_attributes: The database_attributes of this Application.  # noqa: E501
        :type: list[object]
        """

        self._database_attributes = database_attributes

    @property
    def description(self):
        """Gets the description of this Application.  # noqa: E501


        :return: The description of this Application.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Application.


        :param description: The description of this Application.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_label(self):
        """Gets the display_label of this Application.  # noqa: E501


        :return: The display_label of this Application.  # noqa: E501
        :rtype: str
        """
        return self._display_label

    @display_label.setter
    def display_label(self, display_label):
        """Sets the display_label of this Application.


        :param display_label: The display_label of this Application.  # noqa: E501
        :type: str
        """

        self._display_label = display_label

    @property
    def display_name(self):
        """Gets the display_name of this Application.  # noqa: E501


        :return: The display_name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Application.


        :param display_name: The display_name of this Application.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def learn_more(self):
        """Gets the learn_more of this Application.  # noqa: E501


        :return: The learn_more of this Application.  # noqa: E501
        :rtype: str
        """
        return self._learn_more

    @learn_more.setter
    def learn_more(self, learn_more):
        """Sets the learn_more of this Application.


        :param learn_more: The learn_more of this Application.  # noqa: E501
        :type: str
        """

        self._learn_more = learn_more

    @property
    def logo(self):
        """Gets the logo of this Application.  # noqa: E501


        :return: The logo of this Application.  # noqa: E501
        :rtype: ApplicationLogo
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Application.


        :param logo: The logo of this Application.  # noqa: E501
        :type: ApplicationLogo
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this Application.  # noqa: E501


        :return: The name of this Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Application.


        :param name: The name of this Application.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this Application.  # noqa: E501


        :return: The organization of this Application.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Application.


        :param organization: The organization of this Application.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def sso(self):
        """Gets the sso of this Application.  # noqa: E501


        :return: The sso of this Application.  # noqa: E501
        :rtype: Sso
        """
        return self._sso

    @sso.setter
    def sso(self, sso):
        """Sets the sso of this Application.


        :param sso: The sso of this Application.  # noqa: E501
        :type: Sso
        """

        self._sso = sso

    @property
    def sso_url(self):
        """Gets the sso_url of this Application.  # noqa: E501


        :return: The sso_url of this Application.  # noqa: E501
        :rtype: str
        """
        return self._sso_url

    @sso_url.setter
    def sso_url(self, sso_url):
        """Sets the sso_url of this Application.


        :param sso_url: The sso_url of this Application.  # noqa: E501
        :type: str
        """
        if sso_url is None:
            raise ValueError("Invalid value for `sso_url`, must not be `None`")  # noqa: E501

        self._sso_url = sso_url

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
        if issubclass(Application, dict):
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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
