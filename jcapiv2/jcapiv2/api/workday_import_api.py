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


class WorkdayImportApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def workdays_authorize(self, workday_id, **kwargs):  # noqa: E501
        """Authorize Workday  # noqa: E501

        This endpoint adds an authorization method to a workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/auth \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"auth\":{    \"basic\": {   \"username\": \"someDeveloper\",      \"password\": \"notTheRealPassword\"     }  } }'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_authorize(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param AuthInputObject body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_authorize_with_http_info(workday_id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_authorize_with_http_info(workday_id, **kwargs)  # noqa: E501
            return data

    def workdays_authorize_with_http_info(self, workday_id, **kwargs):  # noqa: E501
        """Authorize Workday  # noqa: E501

        This endpoint adds an authorization method to a workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/auth \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"auth\":{    \"basic\": {   \"username\": \"someDeveloper\",      \"password\": \"notTheRealPassword\"     }  } }'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_authorize_with_http_info(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param AuthInputObject body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workday_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_authorize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workday_id' is set
        if ('workday_id' not in params or
                params['workday_id'] is None):
            raise ValueError("Missing the required parameter `workday_id` when calling `workdays_authorize`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workday_id' in params:
            path_params['workday_id'] = params['workday_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/workdays/{workday_id}/auth', 'POST',
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

    def workdays_deauthorize(self, workday_id, **kwargs):  # noqa: E501
        """Deauthorize Workday  # noqa: E501

        Removes any and all authorization methods from the workday instance  ##### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/auth \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_deauthorize(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_deauthorize_with_http_info(workday_id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_deauthorize_with_http_info(workday_id, **kwargs)  # noqa: E501
            return data

    def workdays_deauthorize_with_http_info(self, workday_id, **kwargs):  # noqa: E501
        """Deauthorize Workday  # noqa: E501

        Removes any and all authorization methods from the workday instance  ##### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/auth \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_deauthorize_with_http_info(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workday_id', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_deauthorize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workday_id' is set
        if ('workday_id' not in params or
                params['workday_id'] is None):
            raise ValueError("Missing the required parameter `workday_id` when calling `workdays_deauthorize`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workday_id' in params:
            path_params['workday_id'] = params['workday_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/workdays/{workday_id}/auth', 'DELETE',
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

    def workdays_get(self, id, **kwargs):  # noqa: E501
        """Get Workday  # noqa: E501

        This endpoint will return  all the available information about an instance of Workday.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: WorkdayOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def workdays_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Workday  # noqa: E501

        This endpoint will return  all the available information about an instance of Workday.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: WorkdayOutput
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
                    " to method workdays_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `workdays_get`")  # noqa: E501

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
            '/workdays/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkdayOutput',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workdays_import(self, workday_id, **kwargs):  # noqa: E501
        """Workday Import  # noqa: E501

        The endpoint allows you to create a Workday Import request.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/{WorkdayID}/import \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '[  {   \"email\":\"{email}\",   \"firstname\":\"{firstname}\",   \"lastname\":\"{firstname}\",   \"username\":\"{username}\",   \"attributes\":[    {\"name\":\"EmployeeID\",\"value\":\"0000\"},    {\"name\":\"WorkdayID\",\"value\":\"name.name\"}    ]     } ] ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_import(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param list[BulkUserCreate] body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: JobId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_import_with_http_info(workday_id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_import_with_http_info(workday_id, **kwargs)  # noqa: E501
            return data

    def workdays_import_with_http_info(self, workday_id, **kwargs):  # noqa: E501
        """Workday Import  # noqa: E501

        The endpoint allows you to create a Workday Import request.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/{WorkdayID}/import \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '[  {   \"email\":\"{email}\",   \"firstname\":\"{firstname}\",   \"lastname\":\"{firstname}\",   \"username\":\"{username}\",   \"attributes\":[    {\"name\":\"EmployeeID\",\"value\":\"0000\"},    {\"name\":\"WorkdayID\",\"value\":\"name.name\"}    ]     } ] ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_import_with_http_info(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param list[BulkUserCreate] body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: JobId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workday_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workday_id' is set
        if ('workday_id' not in params or
                params['workday_id'] is None):
            raise ValueError("Missing the required parameter `workday_id` when calling `workdays_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workday_id' in params:
            path_params['workday_id'] = params['workday_id']  # noqa: E501

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
            '/workdays/{workday_id}/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workdays_importresults(self, id, job_id, **kwargs):  # noqa: E501
        """List Import Results  # noqa: E501

        This endpoint provides a list of job results from the workday import and will contain all imported data from Workday.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/{WorkdayID}/import/{ImportJobID}/results \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_importresults(id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str job_id: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[JobWorkresult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_importresults_with_http_info(id, job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_importresults_with_http_info(id, job_id, **kwargs)  # noqa: E501
            return data

    def workdays_importresults_with_http_info(self, id, job_id, **kwargs):  # noqa: E501
        """List Import Results  # noqa: E501

        This endpoint provides a list of job results from the workday import and will contain all imported data from Workday.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/{WorkdayID}/import/{ImportJobID}/results \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_importresults_with_http_info(id, job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str job_id: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[JobWorkresult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'job_id', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_importresults" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `workdays_importresults`")  # noqa: E501
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `workdays_importresults`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

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
            '/workdays/{id}/import/{job_id}/results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JobWorkresult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workdays_list(self, **kwargs):  # noqa: E501
        """List Workdays  # noqa: E501

        This endpoint will return  all the available information about all your instances of Workday.  ##### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[WorkdayOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.workdays_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def workdays_list_with_http_info(self, **kwargs):  # noqa: E501
        """List Workdays  # noqa: E501

        This endpoint will return  all the available information about all your instances of Workday.  ##### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[WorkdayOutput]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'limit', 'skip', 'sort', 'filter', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501

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
            '/workdays', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WorkdayOutput]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workdays_post(self, **kwargs):  # noqa: E501
        """Create new Workday  # noqa: E501

        This endpoint allows you to create a new workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  Currently, only one instance is allowed and it must be `Workday Import`.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Workday2\",     \"reportUrl\":\"https://workday.com/ccx/service/customreport2/gms/user/reportname?format=json\",     \"auth\": {       \"basic\": {         \"username\": \"someDeveloper\",         \"password\": \"notTheRealPassword\"       }     }   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkdayInput body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: WorkdayOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.workdays_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def workdays_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create new Workday  # noqa: E501

        This endpoint allows you to create a new workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  Currently, only one instance is allowed and it must be `Workday Import`.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Workday2\",     \"reportUrl\":\"https://workday.com/ccx/service/customreport2/gms/user/reportname?format=json\",     \"auth\": {       \"basic\": {         \"username\": \"someDeveloper\",         \"password\": \"notTheRealPassword\"       }     }   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WorkdayInput body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: WorkdayOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_post" % key
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
            '/workdays', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkdayOutput',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workdays_put(self, id, **kwargs):  # noqa: E501
        """Update Workday  # noqa: E501

        This endpoint allows you to update the name and Custom Report URL for a Workday Instance.  Currently, the name can not be changed from the default of `Workday Import`.  ##### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/v2/workdays/{WorkdayID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"reportUrl\":\"{Report_URL}\",  \"name\":\"{Name}\" } ' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_put(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param WorkdayFields body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: WorkdayOutput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_put_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_put_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def workdays_put_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Workday  # noqa: E501

        This endpoint allows you to update the name and Custom Report URL for a Workday Instance.  Currently, the name can not be changed from the default of `Workday Import`.  ##### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/v2/workdays/{WorkdayID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"reportUrl\":\"{Report_URL}\",  \"name\":\"{Name}\" } ' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_put_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param WorkdayFields body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: WorkdayOutput
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
                    " to method workdays_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `workdays_put`")  # noqa: E501

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
            '/workdays/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkdayOutput',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def workdays_workers(self, workday_id, **kwargs):  # noqa: E501
        """List Workday Workers  # noqa: E501

        This endpoint will return all of the data in your WorkDay Custom Report that has been associated with your WorkDay Instance in JumpCloud.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/workers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_workers(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[WorkdayWorker]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.workdays_workers_with_http_info(workday_id, **kwargs)  # noqa: E501
        else:
            (data) = self.workdays_workers_with_http_info(workday_id, **kwargs)  # noqa: E501
            return data

    def workdays_workers_with_http_info(self, workday_id, **kwargs):  # noqa: E501
        """List Workday Workers  # noqa: E501

        This endpoint will return all of the data in your WorkDay Custom Report that has been associated with your WorkDay Instance in JumpCloud.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/workers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.workdays_workers_with_http_info(workday_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workday_id: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[WorkdayWorker]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workday_id', 'limit', 'skip', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method workdays_workers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workday_id' is set
        if ('workday_id' not in params or
                params['workday_id'] is None):
            raise ValueError("Missing the required parameter `workday_id` when calling `workdays_workers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workday_id' in params:
            path_params['workday_id'] = params['workday_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

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
            '/workdays/{workday_id}/workers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WorkdayWorker]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
