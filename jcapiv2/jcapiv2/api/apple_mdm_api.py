# coding: utf-8

"""
    JumpCloud API

    # Overview  JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # Directory Objects  This API offers the ability to interact with some of our core features; otherwise known as Directory Objects. The Directory Objects are:  * Commands * Policies * Policy Groups * Applications * Systems * Users * User Groups * System Groups * Radius Servers * Directories: Office 365, LDAP,G-Suite, Active Directory * Duo accounts and applications.  The Directory Object is an important concept to understand in order to successfully use JumpCloud API.  ## JumpCloud Graph  We've also introduced the concept of the JumpCloud Graph along with  Directory Objects. The Graph is a powerful aspect of our platform which will enable you to associate objects with each other, or establish membership for certain objects to become members of other objects.  Specific `GET` endpoints will allow you to traverse the JumpCloud Graph to return all indirect and directly bound objects in your organization.  | ![alt text](https://s3.amazonaws.com/jumpcloud-kb/Knowledge+Base+Photos/API+Docs/jumpcloud_graph.png \"JumpCloud Graph Model Example\") | |:--:| | **This diagram highlights our association and membership model as it relates to Directory Objects.** |  # API Key  ## Access Your API Key  To locate your API Key:  1. Log into the [JumpCloud Admin Console](https://console.jumpcloud.com/). 2. Go to the username drop down located in the top-right of the Console. 3. Retrieve your API key from API Settings.  ## API Key Considerations  This API key is associated to the currently logged in administrator. Other admins will have different API keys.  **WARNING** Please keep this API key secret, as it grants full access to any data accessible via your JumpCloud console account.  You can also reset your API key in the same location in the JumpCloud Admin Console.  ## Recycling or Resetting Your API Key  In order to revoke access with the current API key, simply reset your API key. This will render all calls using the previous API key inaccessible.  Your API key will be passed in as a header with the header name \"x-api-key\".  ```bash curl -H \"x-api-key: [YOUR_API_KEY_HERE]\" \"https://console.jumpcloud.com/api/v2/systemgroups\" ```  # System Context  * [Introduction](#introduction) * [Supported endpoints](#supported-endpoints) * [Response codes](#response-codes) * [Authentication](#authentication) * [Additional examples](#additional-examples) * [Third party](#third-party)  ## Introduction  JumpCloud System Context Authorization is an alternative way to authenticate with a subset of JumpCloud's REST APIs. Using this method, a system can manage its information and resource associations, allowing modern auto provisioning environments to scale as needed.  **Notes:**   * The following documentation applies to Linux Operating Systems only.  * Systems that have been automatically enrolled using Apple's Device Enrollment Program (DEP) or systems enrolled using the User Portal install are not eligible to use the System Context API to prevent unauthorized access to system groups and resources. If a script that utilizes the System Context API is invoked on a system enrolled in this way, it will display an error.  ## Supported Endpoints  JumpCloud System Context Authorization can be used in conjunction with Systems endpoints found in the V1 API and certain System Group endpoints found in the v2 API.  * A system may fetch, alter, and delete metadata about itself, including manipulating a system's Group and Systemuser associations,   * `/api/systems/{system_id}` | [`GET`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_get) [`PUT`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_put) * A system may delete itself from your JumpCloud organization   * `/api/systems/{system_id}` | [`DELETE`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_delete) * A system may fetch its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/memberof` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembership)   * `/api/v2/systems/{system_id}/associations` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsList)   * `/api/v2/systems/{system_id}/users` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemTraverseUser) * A system may alter its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/associations` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsPost) * A system may alter its System Group associations   * `/api/v2/systemgroups/{group_id}/members` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembersPost)     * _NOTE_ If a system attempts to alter the system group membership of a different system the request will be rejected  ## Response Codes  If endpoints other than those described above are called using the System Context API, the server will return a `401` response.  ## Authentication  To allow for secure access to our APIs, you must authenticate each API request. JumpCloud System Context Authorization uses [HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures-00) to authenticate API requests. The HTTP Signatures sent with each request are similar to the signatures used by the Amazon Web Services REST API. To help with the request-signing process, we have provided an [example bash script](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh). This example API request simply requests the entire system record. You must be root, or have permissions to access the contents of the `/opt/jc` directory to generate a signature.  Here is a breakdown of the example script with explanations.  First, the script extracts the systemKey from the JSON formatted `/opt/jc/jcagent.conf` file.  ```bash #!/bin/bash conf=\"`cat /opt/jc/jcagent.conf`\" regex=\"systemKey\\\":\\\"(\\w+)\\\"\"  if [[ $conf =~ $regex ]] ; then   systemKey=\"${BASH_REMATCH[1]}\" fi ```  Then, the script retrieves the current date in the correct format.  ```bash now=`date -u \"+%a, %d %h %Y %H:%M:%S GMT\"`; ```  Next, we build a signing string to demonstrate the expected signature format. The signed string must consist of the [request-line](https://tools.ietf.org/html/rfc2616#page-35) and the date header, separated by a newline character.  ```bash signstr=\"GET /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" ```  The next step is to calculate and apply the signature. This is a two-step process:  1. Create a signature from the signing string using the JumpCloud Agent private key: ``printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key`` 2. Then Base64-encode the signature string and trim off the newline characters: ``| openssl enc -e -a | tr -d '\\n'``  The combined steps above result in:  ```bash signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ; ```  Finally, we make sure the API call sending the signature has the same Authorization and Date header values, HTTP method, and URL that were used in the signing string.  ```bash curl -iq \\   -H \"Accept: application/json\" \\   -H \"Content-Type: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Input Data  All PUT and POST methods should use the HTTP Content-Type header with a value of 'application/json'. PUT methods are used for updating a record. POST methods are used to create a record.  The following example demonstrates how to update the `displayName` of the system.  ```bash signstr=\"PUT /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ;  curl -iq \\   -d \"{\\\"displayName\\\" : \\\"updated-system-name-1\\\"}\" \\   -X \"PUT\" \\   -H \"Content-Type: application/json\" \\   -H \"Accept: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Output Data  All results will be formatted as JSON.  Here is an abbreviated example of response output:  ```json {   \"_id\": \"525ee96f52e144993e000015\",   \"agentServer\": \"lappy386\",   \"agentVersion\": \"0.9.42\",   \"arch\": \"x86_64\",   \"connectionKey\": \"127.0.0.1_51812\",   \"displayName\": \"ubuntu-1204\",   \"firstContact\": \"2013-10-16T19:30:55.611Z\",   \"hostname\": \"ubuntu-1204\"   ... ```  ## Additional Examples  ### Signing Authentication Example  This example demonstrates how to make an authenticated request to fetch the JumpCloud record for this system.  [SigningExample.sh](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh)  ### Shutdown Hook  This example demonstrates how to make an authenticated request on system shutdown. Using an init.d script registered at run level 0, you can call the System Context API as the system is shutting down.  [Instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) is an example of an init.d script that only runs at system shutdown.  After customizing the [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) script, you should install it on the system(s) running the JumpCloud agent.  1. Copy the modified [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) to `/etc/init.d/instance-shutdown`. 2. On Ubuntu systems, run `update-rc.d instance-shutdown defaults`. On RedHat/CentOS systems, run `chkconfig --add instance-shutdown`.  ## Third Party  ### Chef Cookbooks  [https://github.com/nshenry03/jumpcloud](https://github.com/nshenry03/jumpcloud)  [https://github.com/cjs226/jumpcloud](https://github.com/cjs226/jumpcloud)  # Multi-Tenant Portal Headers  Multi-Tenant Organization API Headers are available for JumpCloud Admins to use when making API requests from Organizations that have multiple managed organizations.  The `x-org-id` is a required header for all multi-tenant admins when making API requests to JumpCloud. This header will define to which organization you would like to make the request.  **NOTE** Single Tenant Admins do not need to provide this header when making an API request.  ## Header Value  `x-org-id`  ## API Response Codes  * `400` Malformed ID. * `400` x-org-id and Organization path ID do not match. * `401` ID not included for multi-tenant admin * `403` ID included on unsupported route. * `404` Organization ID Not Found.  ```bash curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -H 'x-org-id: {ORG_ID}'  ```  ## To Obtain an Individual Organization ID via the UI  As a prerequisite, your Primary Organization will need to be setup for Multi-Tenancy. This provides access to the Multi-Tenant Organization Admin Portal.  1. Log into JumpCloud [Admin Console](https://console.jumpcloud.com). If you are a multi-tenant Admin, you will automatically be routed to the Multi-Tenant Admin Portal. 2. From the Multi-Tenant Portal's primary navigation bar, select the Organization you'd like to access. 3. You will automatically be routed to that Organization's Admin Console. 4. Go to Settings in the sub-tenant's primary navigation. 5. You can obtain your Organization ID below your Organization's Contact Information on the Settings page.  ## To Obtain All Organization IDs via the API  * You can make an API request to this endpoint using the API key of your Primary Organization.  `https://console.jumpcloud.com/api/organizations/` This will return all your managed organizations.  ```bash curl -X GET \\   https://console.jumpcloud.com/api/organizations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # SDKs  You can find language specific SDKs that can help you kickstart your Integration with JumpCloud in the following GitHub repositories:  * [Python](https://github.com/TheJumpCloud/jcapi-python) * [Go](https://github.com/TheJumpCloud/jcapi-go) * [Ruby](https://github.com/TheJumpCloud/jcapi-ruby) * [Java](https://github.com/TheJumpCloud/jcapi-java)   # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@jumpcloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jcapiv2.api_client import ApiClient


class AppleMDMApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def applemdms_csrget(self, apple_mdm_id, **kwargs):  # noqa: E501
        """Get Apple MDM CSR Plist  # noqa: E501

        Retrieves an Apple MDM signed CSR Plist for an organization.  The user must supply the returned plist to Apple for signing, and then provide the certificate provided by Apple back into the PUT API.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/csr \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_csrget(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmSignedCsrPlist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_csrget_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_csrget_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
            return data

    def applemdms_csrget_with_http_info(self, apple_mdm_id, **kwargs):  # noqa: E501
        """Get Apple MDM CSR Plist  # noqa: E501

        Retrieves an Apple MDM signed CSR Plist for an organization.  The user must supply the returned plist to Apple for signing, and then provide the certificate provided by Apple back into the PUT API.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/csr \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_csrget_with_http_info(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmSignedCsrPlist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_csrget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_csrget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/csr', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppleMdmSignedCsrPlist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_delete(self, id, **kwargs):  # noqa: E501
        """Delete an Apple MDM  # noqa: E501

        Removes an Apple MDM configuration.  Warning: This is a destructive operation and will remove your Apple Push Certificates.  We will no longer be able to manage your devices and the only recovery option is to re-register all devices into MDM.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/applemdms/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMDM
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def applemdms_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete an Apple MDM  # noqa: E501

        Removes an Apple MDM configuration.  Warning: This is a destructive operation and will remove your Apple Push Certificates.  We will no longer be able to manage your devices and the only recovery option is to re-register all devices into MDM.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/applemdms/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMDM
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `applemdms_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppleMDM',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_deletedevice(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Remove an Apple MDM Device's Enrollment  # noqa: E501

        Remove a single Apple MDM device from MDM enrollment.  #### Sample Request ```   curl -X DELETE https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id} \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deletedevice(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_deletedevice_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_deletedevice_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_deletedevice_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Remove an Apple MDM Device's Enrollment  # noqa: E501

        Remove a single Apple MDM device from MDM enrollment.  #### Sample Request ```   curl -X DELETE https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id} \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deletedevice_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_deletedevice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_deletedevice`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_deletedevice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppleMdmDevice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_depkeyget(self, apple_mdm_id, **kwargs):  # noqa: E501
        """Get Apple MDM DEP Public Key  # noqa: E501

        Retrieves an Apple MDM DEP Public Key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_depkeyget(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmPublicKeyCert
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_depkeyget_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_depkeyget_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
            return data

    def applemdms_depkeyget_with_http_info(self, apple_mdm_id, **kwargs):  # noqa: E501
        """Get Apple MDM DEP Public Key  # noqa: E501

        Retrieves an Apple MDM DEP Public Key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_depkeyget_with_http_info(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmPublicKeyCert
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_depkeyget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_depkeyget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-pem-file'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/depkey', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppleMdmPublicKeyCert',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_devices_clear_activation_lock(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Clears the Activation Lock for a Device  # noqa: E501

        Clears the activation lock on the specified device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/clearActivationLock \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devices_clear_activation_lock(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_devices_clear_activation_lock_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_devices_clear_activation_lock_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_devices_clear_activation_lock_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Clears the Activation Lock for a Device  # noqa: E501

        Clears the activation lock on the specified device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/clearActivationLock \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devices_clear_activation_lock_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_devices_clear_activation_lock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_devices_clear_activation_lock`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_devices_clear_activation_lock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}/clearActivationLock', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_devices_refresh_activation_lock_information(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Refresh activation lock information for a device  # noqa: E501

        Refreshes the activation lock information for a device  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/refreshActivationLockInformation \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devices_refresh_activation_lock_information(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_devices_refresh_activation_lock_information_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_devices_refresh_activation_lock_information_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_devices_refresh_activation_lock_information_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Refresh activation lock information for a device  # noqa: E501

        Refreshes the activation lock information for a device  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/refreshActivationLockInformation \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devices_refresh_activation_lock_information_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_devices_refresh_activation_lock_information" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_devices_refresh_activation_lock_information`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_devices_refresh_activation_lock_information`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}/refreshActivationLockInformation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_deviceserase(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Erase Device  # noqa: E501

        Erases a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/erase \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deviceserase(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param DeviceIdEraseBody body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_deviceserase_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_deviceserase_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_deviceserase_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Erase Device  # noqa: E501

        Erases a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/erase \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deviceserase_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param DeviceIdEraseBody body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_deviceserase" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_deviceserase`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_deviceserase`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}/erase', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_deviceslist(self, apple_mdm_id, **kwargs):  # noqa: E501
        """List AppleMDM Devices  # noqa: E501

        Lists all Apple MDM devices.  The filter and sort queries will allow the following fields: `createdAt` `depRegistered` `enrolled` `id` `osVersion` `serialNumber` `udid`  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deviceslist(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param int x_total_count:
        :return: list[AppleMdmDevice]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_deviceslist_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_deviceslist_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
            return data

    def applemdms_deviceslist_with_http_info(self, apple_mdm_id, **kwargs):  # noqa: E501
        """List AppleMDM Devices  # noqa: E501

        Lists all Apple MDM devices.  The filter and sort queries will allow the following fields: `createdAt` `depRegistered` `enrolled` `id` `osVersion` `serialNumber` `udid`  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deviceslist_with_http_info(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param int x_total_count:
        :return: list[AppleMdmDevice]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'limit', 'x_org_id', 'skip', 'filter', 'sort', 'x_total_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_deviceslist" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_deviceslist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501
        if 'x_total_count' in params:
            header_params['x-total-count'] = params['x_total_count']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AppleMdmDevice]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_deviceslock(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Lock Device  # noqa: E501

        Locks a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/lock \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deviceslock(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param DeviceIdLockBody body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_deviceslock_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_deviceslock_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_deviceslock_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Lock Device  # noqa: E501

        Locks a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/lock \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_deviceslock_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param DeviceIdLockBody body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_deviceslock" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_deviceslock`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_deviceslock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}/lock', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_devicesrestart(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Restart Device  # noqa: E501

        Restarts a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/restart \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{\"kextPaths\": [\"Path1\", \"Path2\"]}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devicesrestart(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param DeviceIdRestartBody body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_devicesrestart_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_devicesrestart_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_devicesrestart_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Restart Device  # noqa: E501

        Restarts a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/restart \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{\"kextPaths\": [\"Path1\", \"Path2\"]}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devicesrestart_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param DeviceIdRestartBody body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_devicesrestart" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_devicesrestart`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_devicesrestart`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}/restart', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_devicesshutdown(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Shut Down Device  # noqa: E501

        Shuts down a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/shutdown \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devicesshutdown(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_devicesshutdown_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_devicesshutdown_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_devicesshutdown_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Shut Down Device  # noqa: E501

        Shuts down a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/shutdown \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_devicesshutdown_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_devicesshutdown" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_devicesshutdown`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_devicesshutdown`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}/shutdown', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_enrollmentprofilesget(self, apple_mdm_id, id, **kwargs):  # noqa: E501
        """Get an Apple MDM Enrollment Profile  # noqa: E501

        Get an enrollment profile  Currently only requesting the mobileconfig is supported.  #### Sample Request  ``` curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles/{ID} \\   -H 'accept: application/x-apple-aspen-config' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_enrollmentprofilesget(apple_mdm_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: Mobileconfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_enrollmentprofilesget_with_http_info(apple_mdm_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_enrollmentprofilesget_with_http_info(apple_mdm_id, id, **kwargs)  # noqa: E501
            return data

    def applemdms_enrollmentprofilesget_with_http_info(self, apple_mdm_id, id, **kwargs):  # noqa: E501
        """Get an Apple MDM Enrollment Profile  # noqa: E501

        Get an enrollment profile  Currently only requesting the mobileconfig is supported.  #### Sample Request  ``` curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles/{ID} \\   -H 'accept: application/x-apple-aspen-config' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_enrollmentprofilesget_with_http_info(apple_mdm_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: Mobileconfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_enrollmentprofilesget" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_enrollmentprofilesget`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `applemdms_enrollmentprofilesget`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-apple-aspen-config'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/enrollmentprofiles/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Mobileconfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_enrollmentprofileslist(self, apple_mdm_id, **kwargs):  # noqa: E501
        """List Apple MDM Enrollment Profiles  # noqa: E501

        Get a list of enrollment profiles for an apple mdm.  Note: currently only one enrollment profile is supported.  #### Sample Request ```  curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_enrollmentprofileslist(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[AppleMDM]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_enrollmentprofileslist_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_enrollmentprofileslist_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
            return data

    def applemdms_enrollmentprofileslist_with_http_info(self, apple_mdm_id, **kwargs):  # noqa: E501
        """List Apple MDM Enrollment Profiles  # noqa: E501

        Get a list of enrollment profiles for an apple mdm.  Note: currently only one enrollment profile is supported.  #### Sample Request ```  curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_enrollmentprofileslist_with_http_info(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[AppleMDM]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_enrollmentprofileslist" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_enrollmentprofileslist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/enrollmentprofiles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AppleMDM]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_getdevice(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Details of an AppleMDM Device  # noqa: E501

        Gets a single Apple MDM device.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id} \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_getdevice(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_getdevice_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_getdevice_with_http_info(apple_mdm_id, device_id, **kwargs)  # noqa: E501
            return data

    def applemdms_getdevice_with_http_info(self, apple_mdm_id, device_id, **kwargs):  # noqa: E501
        """Details of an AppleMDM Device  # noqa: E501

        Gets a single Apple MDM device.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id} \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_getdevice_with_http_info(apple_mdm_id, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str device_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMdmDevice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'device_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_getdevice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_getdevice`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `applemdms_getdevice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501
        if 'device_id' in params:
            path_params['device_id'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/devices/{device_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppleMdmDevice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_list(self, **kwargs):  # noqa: E501
        """List Apple MDMs  # noqa: E501

        Get a list of all Apple MDM configurations.  An empty topic indicates that a signed certificate from Apple has not been provided to the PUT endpoint yet.  Note: currently only one MDM configuration per organization is supported.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/applemdms \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[AppleMDM]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def applemdms_list_with_http_info(self, **kwargs):  # noqa: E501
        """List Apple MDMs  # noqa: E501

        Get a list of all Apple MDM configurations.  An empty topic indicates that a signed certificate from Apple has not been provided to the PUT endpoint yet.  Note: currently only one MDM configuration per organization is supported.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/applemdms \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[AppleMDM]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AppleMDM]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_put(self, id, **kwargs):  # noqa: E501
        """Update an Apple MDM  # noqa: E501

        Updates an Apple MDM configuration.  This endpoint is used to supply JumpCloud with a signed certificate from Apple in order to finalize the setup and allow JumpCloud to manage your devices.  It may also be used to update the DEP Settings.  #### Sample Request ```   curl -X PUT https://console.jumpcloud.com/api/v2/applemdms/{ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"MDM name\",     \"appleSignedCert\": \"{CERTIFICATE}\",     \"encryptedDepServerToken\": \"{SERVER_TOKEN}\",     \"dep\": {       \"welcomeScreen\": {         \"title\": \"Welcome\",         \"paragraph\": \"In just a few steps, you will be working securely from your Mac.\",         \"button\": \"continue\",       },     },   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_put(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param AppleMdmPatchInput body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMDM
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_put_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_put_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def applemdms_put_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update an Apple MDM  # noqa: E501

        Updates an Apple MDM configuration.  This endpoint is used to supply JumpCloud with a signed certificate from Apple in order to finalize the setup and allow JumpCloud to manage your devices.  It may also be used to update the DEP Settings.  #### Sample Request ```   curl -X PUT https://console.jumpcloud.com/api/v2/applemdms/{ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"MDM name\",     \"appleSignedCert\": \"{CERTIFICATE}\",     \"encryptedDepServerToken\": \"{SERVER_TOKEN}\",     \"dep\": {       \"welcomeScreen\": {         \"title\": \"Welcome\",         \"paragraph\": \"In just a few steps, you will be working securely from your Mac.\",         \"button\": \"continue\",       },     },   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_put_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param AppleMdmPatchInput body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: AppleMDM
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `applemdms_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AppleMDM',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def applemdms_refreshdepdevices(self, apple_mdm_id, **kwargs):  # noqa: E501
        """Refresh DEP Devices  # noqa: E501

        Refreshes the list of devices that a JumpCloud admin has added to their virtual MDM in Apple Business Manager - ABM so that they can be DEP enrolled with JumpCloud.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/refreshdepdevices \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_refreshdepdevices(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.applemdms_refreshdepdevices_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.applemdms_refreshdepdevices_with_http_info(apple_mdm_id, **kwargs)  # noqa: E501
            return data

    def applemdms_refreshdepdevices_with_http_info(self, apple_mdm_id, **kwargs):  # noqa: E501
        """Refresh DEP Devices  # noqa: E501

        Refreshes the list of devices that a JumpCloud admin has added to their virtual MDM in Apple Business Manager - ABM so that they can be DEP enrolled with JumpCloud.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/refreshdepdevices \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.applemdms_refreshdepdevices_with_http_info(apple_mdm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str apple_mdm_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['apple_mdm_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applemdms_refreshdepdevices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'apple_mdm_id' is set
        if ('apple_mdm_id' not in params or
                params['apple_mdm_id'] is None):
            raise ValueError("Missing the required parameter `apple_mdm_id` when calling `applemdms_refreshdepdevices`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'apple_mdm_id' in params:
            path_params['apple_mdm_id'] = params['apple_mdm_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/applemdms/{apple_mdm_id}/refreshdepdevices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
