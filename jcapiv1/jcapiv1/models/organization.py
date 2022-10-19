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

class Organization(object):
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
        'accounts_receivable': 'str',
        'created': 'str',
        'display_name': 'str',
        'entitlement': 'Organizationentitlement',
        'has_credit_card': 'bool',
        'has_stripe_customer_id': 'bool',
        'last_estimate_calculation_time_stamp': 'str',
        'last_sfdc_sync_status': 'object',
        'logo_url': 'str',
        'provider': 'str',
        'settings': 'Organizationsettings',
        'total_billing_estimate': 'int'
    }

    attribute_map = {
        'id': '_id',
        'accounts_receivable': 'accountsReceivable',
        'created': 'created',
        'display_name': 'displayName',
        'entitlement': 'entitlement',
        'has_credit_card': 'hasCreditCard',
        'has_stripe_customer_id': 'hasStripeCustomerId',
        'last_estimate_calculation_time_stamp': 'lastEstimateCalculationTimeStamp',
        'last_sfdc_sync_status': 'lastSfdcSyncStatus',
        'logo_url': 'logoUrl',
        'provider': 'provider',
        'settings': 'settings',
        'total_billing_estimate': 'totalBillingEstimate'
    }

    def __init__(self, id=None, accounts_receivable=None, created=None, display_name=None, entitlement=None, has_credit_card=None, has_stripe_customer_id=None, last_estimate_calculation_time_stamp=None, last_sfdc_sync_status=None, logo_url=None, provider=None, settings=None, total_billing_estimate=None):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._accounts_receivable = None
        self._created = None
        self._display_name = None
        self._entitlement = None
        self._has_credit_card = None
        self._has_stripe_customer_id = None
        self._last_estimate_calculation_time_stamp = None
        self._last_sfdc_sync_status = None
        self._logo_url = None
        self._provider = None
        self._settings = None
        self._total_billing_estimate = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if accounts_receivable is not None:
            self.accounts_receivable = accounts_receivable
        if created is not None:
            self.created = created
        if display_name is not None:
            self.display_name = display_name
        if entitlement is not None:
            self.entitlement = entitlement
        if has_credit_card is not None:
            self.has_credit_card = has_credit_card
        if has_stripe_customer_id is not None:
            self.has_stripe_customer_id = has_stripe_customer_id
        if last_estimate_calculation_time_stamp is not None:
            self.last_estimate_calculation_time_stamp = last_estimate_calculation_time_stamp
        if last_sfdc_sync_status is not None:
            self.last_sfdc_sync_status = last_sfdc_sync_status
        if logo_url is not None:
            self.logo_url = logo_url
        if provider is not None:
            self.provider = provider
        if settings is not None:
            self.settings = settings
        if total_billing_estimate is not None:
            self.total_billing_estimate = total_billing_estimate

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501


        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.


        :param id: The id of this Organization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def accounts_receivable(self):
        """Gets the accounts_receivable of this Organization.  # noqa: E501


        :return: The accounts_receivable of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._accounts_receivable

    @accounts_receivable.setter
    def accounts_receivable(self, accounts_receivable):
        """Sets the accounts_receivable of this Organization.


        :param accounts_receivable: The accounts_receivable of this Organization.  # noqa: E501
        :type: str
        """

        self._accounts_receivable = accounts_receivable

    @property
    def created(self):
        """Gets the created of this Organization.  # noqa: E501


        :return: The created of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Organization.


        :param created: The created of this Organization.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def display_name(self):
        """Gets the display_name of this Organization.  # noqa: E501


        :return: The display_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Organization.


        :param display_name: The display_name of this Organization.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def entitlement(self):
        """Gets the entitlement of this Organization.  # noqa: E501


        :return: The entitlement of this Organization.  # noqa: E501
        :rtype: Organizationentitlement
        """
        return self._entitlement

    @entitlement.setter
    def entitlement(self, entitlement):
        """Sets the entitlement of this Organization.


        :param entitlement: The entitlement of this Organization.  # noqa: E501
        :type: Organizationentitlement
        """

        self._entitlement = entitlement

    @property
    def has_credit_card(self):
        """Gets the has_credit_card of this Organization.  # noqa: E501


        :return: The has_credit_card of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._has_credit_card

    @has_credit_card.setter
    def has_credit_card(self, has_credit_card):
        """Sets the has_credit_card of this Organization.


        :param has_credit_card: The has_credit_card of this Organization.  # noqa: E501
        :type: bool
        """

        self._has_credit_card = has_credit_card

    @property
    def has_stripe_customer_id(self):
        """Gets the has_stripe_customer_id of this Organization.  # noqa: E501


        :return: The has_stripe_customer_id of this Organization.  # noqa: E501
        :rtype: bool
        """
        return self._has_stripe_customer_id

    @has_stripe_customer_id.setter
    def has_stripe_customer_id(self, has_stripe_customer_id):
        """Sets the has_stripe_customer_id of this Organization.


        :param has_stripe_customer_id: The has_stripe_customer_id of this Organization.  # noqa: E501
        :type: bool
        """

        self._has_stripe_customer_id = has_stripe_customer_id

    @property
    def last_estimate_calculation_time_stamp(self):
        """Gets the last_estimate_calculation_time_stamp of this Organization.  # noqa: E501


        :return: The last_estimate_calculation_time_stamp of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._last_estimate_calculation_time_stamp

    @last_estimate_calculation_time_stamp.setter
    def last_estimate_calculation_time_stamp(self, last_estimate_calculation_time_stamp):
        """Sets the last_estimate_calculation_time_stamp of this Organization.


        :param last_estimate_calculation_time_stamp: The last_estimate_calculation_time_stamp of this Organization.  # noqa: E501
        :type: str
        """

        self._last_estimate_calculation_time_stamp = last_estimate_calculation_time_stamp

    @property
    def last_sfdc_sync_status(self):
        """Gets the last_sfdc_sync_status of this Organization.  # noqa: E501


        :return: The last_sfdc_sync_status of this Organization.  # noqa: E501
        :rtype: object
        """
        return self._last_sfdc_sync_status

    @last_sfdc_sync_status.setter
    def last_sfdc_sync_status(self, last_sfdc_sync_status):
        """Sets the last_sfdc_sync_status of this Organization.


        :param last_sfdc_sync_status: The last_sfdc_sync_status of this Organization.  # noqa: E501
        :type: object
        """

        self._last_sfdc_sync_status = last_sfdc_sync_status

    @property
    def logo_url(self):
        """Gets the logo_url of this Organization.  # noqa: E501


        :return: The logo_url of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Organization.


        :param logo_url: The logo_url of this Organization.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def provider(self):
        """Gets the provider of this Organization.  # noqa: E501


        :return: The provider of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Organization.


        :param provider: The provider of this Organization.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def settings(self):
        """Gets the settings of this Organization.  # noqa: E501


        :return: The settings of this Organization.  # noqa: E501
        :rtype: Organizationsettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Organization.


        :param settings: The settings of this Organization.  # noqa: E501
        :type: Organizationsettings
        """

        self._settings = settings

    @property
    def total_billing_estimate(self):
        """Gets the total_billing_estimate of this Organization.  # noqa: E501


        :return: The total_billing_estimate of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._total_billing_estimate

    @total_billing_estimate.setter
    def total_billing_estimate(self, total_billing_estimate):
        """Sets the total_billing_estimate of this Organization.


        :param total_billing_estimate: The total_billing_estimate of this Organization.  # noqa: E501
        :type: int
        """

        self._total_billing_estimate = total_billing_estimate

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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
