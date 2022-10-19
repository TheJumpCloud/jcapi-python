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


class SystemInsightsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def systeminsights_list_alf(self, **kwargs):  # noqa: E501
        """List System Insights ALF  # noqa: E501

        Valid filter fields are `system_id` and `global_state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_alf(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param int limit:
        :return: list[SystemInsightsAlf]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_alf_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_alf_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_alf_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights ALF  # noqa: E501

        Valid filter fields are `system_id` and `global_state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_alf_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param int limit:
        :return: list[SystemInsightsAlf]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'filter', 'skip', 'sort', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_alf" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/alf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAlf]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_alf_exceptions(self, **kwargs):  # noqa: E501
        """List System Insights ALF Exceptions  # noqa: E501

        Valid filter fields are `system_id` and `state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_alf_exceptions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param int limit:
        :return: list[SystemInsightsAlfExceptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_alf_exceptions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_alf_exceptions_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_alf_exceptions_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights ALF Exceptions  # noqa: E501

        Valid filter fields are `system_id` and `state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_alf_exceptions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param int limit:
        :return: list[SystemInsightsAlfExceptions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'filter', 'skip', 'sort', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_alf_exceptions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/alf_exceptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAlfExceptions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_alf_explicit_auths(self, **kwargs):  # noqa: E501
        """List System Insights ALF Explicit Authentications  # noqa: E501

        Valid filter fields are `system_id` and `process`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_alf_explicit_auths(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param int limit:
        :return: list[SystemInsightsAlfExplicitAuths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_alf_explicit_auths_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_alf_explicit_auths_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_alf_explicit_auths_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights ALF Explicit Authentications  # noqa: E501

        Valid filter fields are `system_id` and `process`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_alf_explicit_auths_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param int limit:
        :return: list[SystemInsightsAlfExplicitAuths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'filter', 'skip', 'sort', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_alf_explicit_auths" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/alf_explicit_auths', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAlfExplicitAuths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_appcompat_shims(self, **kwargs):  # noqa: E501
        """List System Insights Application Compatibility Shims  # noqa: E501

        Valid filter fields are `system_id` and `enabled`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_appcompat_shims(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsAppcompatShims]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_appcompat_shims_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_appcompat_shims_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_appcompat_shims_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Application Compatibility Shims  # noqa: E501

        Valid filter fields are `system_id` and `enabled`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_appcompat_shims_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsAppcompatShims]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_appcompat_shims" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/appcompat_shims', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAppcompatShims]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_apps(self, **kwargs):  # noqa: E501
        """List System Insights Apps  # noqa: E501

        Lists all apps for macOS devices. For Windows devices, use [List System Insights Programs](#operation/systeminsights_list_programs).  Valid filter fields are `system_id` and `bundle_name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_apps(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsApps]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_apps_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_apps_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_apps_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Apps  # noqa: E501

        Lists all apps for macOS devices. For Windows devices, use [List System Insights Programs](#operation/systeminsights_list_programs).  Valid filter fields are `system_id` and `bundle_name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_apps_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsApps]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_apps" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/apps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsApps]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_authorized_keys(self, **kwargs):  # noqa: E501
        """List System Insights Authorized Keys  # noqa: E501

        Valid filter fields are `system_id` and `uid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_authorized_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsAuthorizedKeys]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_authorized_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_authorized_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_authorized_keys_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Authorized Keys  # noqa: E501

        Valid filter fields are `system_id` and `uid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_authorized_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsAuthorizedKeys]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_authorized_keys" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/authorized_keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAuthorizedKeys]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_azure_instance_metadata(self, **kwargs):  # noqa: E501
        """List System Insights Azure Instance Metadata  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_azure_instance_metadata(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsAzureInstanceMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_azure_instance_metadata_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_azure_instance_metadata_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_azure_instance_metadata_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Azure Instance Metadata  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_azure_instance_metadata_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsAzureInstanceMetadata]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_azure_instance_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/azure_instance_metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAzureInstanceMetadata]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_azure_instance_tags(self, **kwargs):  # noqa: E501
        """List System Insights Azure Instance Tags  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_azure_instance_tags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsAzureInstanceTags]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_azure_instance_tags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_azure_instance_tags_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_azure_instance_tags_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Azure Instance Tags  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_azure_instance_tags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsAzureInstanceTags]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_azure_instance_tags" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/azure_instance_tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsAzureInstanceTags]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_battery(self, **kwargs):  # noqa: E501
        """List System Insights Battery  # noqa: E501

        Valid filter fields are `system_id` and `health`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_battery(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsBattery]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_battery_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_battery_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_battery_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Battery  # noqa: E501

        Valid filter fields are `system_id` and `health`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_battery_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsBattery]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_battery" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/battery', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsBattery]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_bitlocker_info(self, **kwargs):  # noqa: E501
        """List System Insights Bitlocker Info  # noqa: E501

        Valid filter fields are `system_id` and `protection_status`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_bitlocker_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsBitlockerInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_bitlocker_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_bitlocker_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_bitlocker_info_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Bitlocker Info  # noqa: E501

        Valid filter fields are `system_id` and `protection_status`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_bitlocker_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsBitlockerInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_bitlocker_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/bitlocker_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsBitlockerInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_browser_plugins(self, **kwargs):  # noqa: E501
        """List System Insights Browser Plugins  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_browser_plugins(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsBrowserPlugins]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_browser_plugins_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_browser_plugins_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_browser_plugins_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Browser Plugins  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_browser_plugins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsBrowserPlugins]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_browser_plugins" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/browser_plugins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsBrowserPlugins]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_certificates(self, **kwargs):  # noqa: E501
        """List System Insights Certificates  # noqa: E501

        Valid filter fields are `system_id` and `common_name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_certificates(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` Note: You can only filter by `system_id` and `common_name` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsCertificates]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_certificates_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_certificates_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_certificates_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Certificates  # noqa: E501

        Valid filter fields are `system_id` and `common_name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_certificates_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` Note: You can only filter by `system_id` and `common_name` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsCertificates]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_certificates" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/certificates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsCertificates]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_chassis_info(self, **kwargs):  # noqa: E501
        """List System Insights Chassis Info  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_chassis_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsChassisInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_chassis_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_chassis_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_chassis_info_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Chassis Info  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_chassis_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsChassisInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_chassis_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/chassis_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsChassisInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_chrome_extensions(self, **kwargs):  # noqa: E501
        """List System Insights Chrome Extensions  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_chrome_extensions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsChromeExtensions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_chrome_extensions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_chrome_extensions_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_chrome_extensions_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Chrome Extensions  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_chrome_extensions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsChromeExtensions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_chrome_extensions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/chrome_extensions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsChromeExtensions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_connectivity(self, **kwargs):  # noqa: E501
        """List System Insights Connectivity  # noqa: E501

        The only valid filter field is `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_connectivity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsConnectivity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_connectivity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_connectivity_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_connectivity_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Connectivity  # noqa: E501

        The only valid filter field is `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_connectivity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsConnectivity]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_connectivity" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/connectivity', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsConnectivity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_crashes(self, **kwargs):  # noqa: E501
        """List System Insights Crashes  # noqa: E501

        Valid filter fields are `system_id` and `identifier`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_crashes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsCrashes]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_crashes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_crashes_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_crashes_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Crashes  # noqa: E501

        Valid filter fields are `system_id` and `identifier`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_crashes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsCrashes]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_crashes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/crashes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsCrashes]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_cups_destinations(self, **kwargs):  # noqa: E501
        """List System Insights CUPS Destinations  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_cups_destinations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsCupsDestinations]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_cups_destinations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_cups_destinations_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_cups_destinations_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights CUPS Destinations  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_cups_destinations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsCupsDestinations]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_cups_destinations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/cups_destinations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsCupsDestinations]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_disk_encryption(self, **kwargs):  # noqa: E501
        """List System Insights Disk Encryption  # noqa: E501

        Valid filter fields are `system_id` and `encryption_status`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_disk_encryption(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsDiskEncryption]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_disk_encryption_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_disk_encryption_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_disk_encryption_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Disk Encryption  # noqa: E501

        Valid filter fields are `system_id` and `encryption_status`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_disk_encryption_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsDiskEncryption]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_disk_encryption" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/disk_encryption', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsDiskEncryption]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_disk_info(self, **kwargs):  # noqa: E501
        """List System Insights Disk Info  # noqa: E501

        Valid filter fields are `system_id` and `disk_index`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_disk_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsDiskInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_disk_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_disk_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_disk_info_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Disk Info  # noqa: E501

        Valid filter fields are `system_id` and `disk_index`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_disk_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsDiskInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_disk_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/disk_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsDiskInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_dns_resolvers(self, **kwargs):  # noqa: E501
        """List System Insights DNS Resolvers  # noqa: E501

        Valid filter fields are `system_id` and `type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_dns_resolvers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsDnsResolvers]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_dns_resolvers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_dns_resolvers_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_dns_resolvers_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights DNS Resolvers  # noqa: E501

        Valid filter fields are `system_id` and `type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_dns_resolvers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsDnsResolvers]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_dns_resolvers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/dns_resolvers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsDnsResolvers]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_etc_hosts(self, **kwargs):  # noqa: E501
        """List System Insights Etc Hosts  # noqa: E501

        Valid filter fields are `system_id` and `address`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_etc_hosts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsEtcHosts]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_etc_hosts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_etc_hosts_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_etc_hosts_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Etc Hosts  # noqa: E501

        Valid filter fields are `system_id` and `address`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_etc_hosts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsEtcHosts]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_etc_hosts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/etc_hosts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsEtcHosts]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_firefox_addons(self, **kwargs):  # noqa: E501
        """List System Insights Firefox Addons  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_firefox_addons(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsFirefoxAddons]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_firefox_addons_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_firefox_addons_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_firefox_addons_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Firefox Addons  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_firefox_addons_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsFirefoxAddons]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_firefox_addons" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/firefox_addons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsFirefoxAddons]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_groups(self, **kwargs):  # noqa: E501
        """List System Insights Groups  # noqa: E501

        Valid filter fields are `system_id` and `groupname`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsGroups]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Groups  # noqa: E501

        Valid filter fields are `system_id` and `groupname`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsGroups]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsGroups]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_ie_extensions(self, **kwargs):  # noqa: E501
        """List System Insights IE Extensions  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_ie_extensions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsIeExtensions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_ie_extensions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_ie_extensions_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_ie_extensions_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights IE Extensions  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_ie_extensions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsIeExtensions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_ie_extensions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/ie_extensions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsIeExtensions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_interface_addresses(self, **kwargs):  # noqa: E501
        """List System Insights Interface Addresses  # noqa: E501

        Valid filter fields are `system_id` and `address`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_interface_addresses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsInterfaceAddresses]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_interface_addresses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_interface_addresses_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_interface_addresses_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Interface Addresses  # noqa: E501

        Valid filter fields are `system_id` and `address`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_interface_addresses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsInterfaceAddresses]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_interface_addresses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/interface_addresses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsInterfaceAddresses]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_interface_details(self, **kwargs):  # noqa: E501
        """List System Insights Interface Details  # noqa: E501

        Valid filter fields are `system_id` and `interface`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_interface_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsInterfaceDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_interface_details_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_interface_details_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_interface_details_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Interface Details  # noqa: E501

        Valid filter fields are `system_id` and `interface`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_interface_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsInterfaceDetails]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_interface_details" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/interface_details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsInterfaceDetails]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_kernel_info(self, **kwargs):  # noqa: E501
        """List System Insights Kernel Info  # noqa: E501

        Valid filter fields are `system_id` and `version`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_kernel_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsKernelInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_kernel_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_kernel_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_kernel_info_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Kernel Info  # noqa: E501

        Valid filter fields are `system_id` and `version`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_kernel_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsKernelInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_kernel_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/kernel_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsKernelInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_launchd(self, **kwargs):  # noqa: E501
        """List System Insights Launchd  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_launchd(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsLaunchd]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_launchd_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_launchd_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_launchd_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Launchd  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_launchd_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsLaunchd]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_launchd" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/launchd', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsLaunchd]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_linux_packages(self, **kwargs):  # noqa: E501
        """List System Insights Linux Packages  # noqa: E501

        Lists all programs for Linux devices. For macOS devices, use [List System Insights System Apps](#operation/systeminsights_list_apps). For windows devices, use [List System Insights System Apps](#operation/systeminsights_list_programs).  Valid filter fields are `name` and `package_format`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_linux_packages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsLinuxPackages]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_linux_packages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_linux_packages_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_linux_packages_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Linux Packages  # noqa: E501

        Lists all programs for Linux devices. For macOS devices, use [List System Insights System Apps](#operation/systeminsights_list_apps). For windows devices, use [List System Insights System Apps](#operation/systeminsights_list_programs).  Valid filter fields are `name` and `package_format`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_linux_packages_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsLinuxPackages]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_linux_packages" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/linux_packages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsLinuxPackages]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_logged_in_users(self, **kwargs):  # noqa: E501
        """List System Insights Logged-In Users  # noqa: E501

        Valid filter fields are `system_id` and `user`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_logged_in_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsLoggedInUsers]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_logged_in_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_logged_in_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_logged_in_users_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Logged-In Users  # noqa: E501

        Valid filter fields are `system_id` and `user`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_logged_in_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsLoggedInUsers]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_logged_in_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/logged_in_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsLoggedInUsers]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_logical_drives(self, **kwargs):  # noqa: E501
        """List System Insights Logical Drives  # noqa: E501

        Valid filter fields are `system_id` and `device_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_logical_drives(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsLogicalDrives]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_logical_drives_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_logical_drives_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_logical_drives_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Logical Drives  # noqa: E501

        Valid filter fields are `system_id` and `device_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_logical_drives_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsLogicalDrives]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_logical_drives" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/logical_drives', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsLogicalDrives]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_managed_policies(self, **kwargs):  # noqa: E501
        """List System Insights Managed Policies  # noqa: E501

        Valid filter fields are `system_id` and `domain`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_managed_policies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsManagedPolicies]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_managed_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_managed_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_managed_policies_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Managed Policies  # noqa: E501

        Valid filter fields are `system_id` and `domain`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_managed_policies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsManagedPolicies]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_managed_policies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/managed_policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsManagedPolicies]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_mounts(self, **kwargs):  # noqa: E501
        """List System Insights Mounts  # noqa: E501

        Valid filter fields are `system_id` and `path`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_mounts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsMounts]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_mounts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_mounts_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_mounts_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Mounts  # noqa: E501

        Valid filter fields are `system_id` and `path`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_mounts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsMounts]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_mounts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/mounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsMounts]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_os_version(self, **kwargs):  # noqa: E501
        """List System Insights OS Version  # noqa: E501

        Valid filter fields are `system_id` and `version`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_os_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsOsVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_os_version_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_os_version_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_os_version_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights OS Version  # noqa: E501

        Valid filter fields are `system_id` and `version`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_os_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsOsVersion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_os_version" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/os_version', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsOsVersion]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_patches(self, **kwargs):  # noqa: E501
        """List System Insights Patches  # noqa: E501

        Valid filter fields are `system_id` and `hotfix_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_patches(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsPatches]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_patches_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_patches_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_patches_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Patches  # noqa: E501

        Valid filter fields are `system_id` and `hotfix_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_patches_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsPatches]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_patches" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/patches', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsPatches]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_programs(self, **kwargs):  # noqa: E501
        """List System Insights Programs  # noqa: E501

        Lists all programs for Windows devices. For macOS devices, use [List System Insights Apps](#operation/systeminsights_list_apps).  Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_programs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsPrograms]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_programs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_programs_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_programs_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Programs  # noqa: E501

        Lists all programs for Windows devices. For macOS devices, use [List System Insights Apps](#operation/systeminsights_list_apps).  Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_programs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsPrograms]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_programs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/programs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsPrograms]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_python_packages(self, **kwargs):  # noqa: E501
        """List System Insights Python Packages  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_python_packages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsPythonPackages]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_python_packages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_python_packages_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_python_packages_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Python Packages  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_python_packages_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsPythonPackages]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_python_packages" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/python_packages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsPythonPackages]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_safari_extensions(self, **kwargs):  # noqa: E501
        """List System Insights Safari Extensions  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_safari_extensions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSafariExtensions]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_safari_extensions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_safari_extensions_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_safari_extensions_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Safari Extensions  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_safari_extensions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSafariExtensions]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_safari_extensions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/safari_extensions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSafariExtensions]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_scheduled_tasks(self, **kwargs):  # noqa: E501
        """List System Insights Scheduled Tasks  # noqa: E501

        Valid filter fields are `system_id` and `enabled`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_scheduled_tasks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsScheduledTasks]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_scheduled_tasks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_scheduled_tasks_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_scheduled_tasks_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Scheduled Tasks  # noqa: E501

        Valid filter fields are `system_id` and `enabled`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_scheduled_tasks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsScheduledTasks]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_scheduled_tasks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/scheduled_tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsScheduledTasks]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_secureboot(self, **kwargs):  # noqa: E501
        """List System Insights Secure Boot  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_secureboot(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSecureboot]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_secureboot_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_secureboot_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_secureboot_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Secure Boot  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_secureboot_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSecureboot]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_secureboot" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/secureboot', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSecureboot]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_services(self, **kwargs):  # noqa: E501
        """List System Insights Services  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_services(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsServices]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_services_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_services_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_services_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Services  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_services_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsServices]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_services" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/services', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsServices]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_shadow(self, **kwargs):  # noqa: E501
        """LIst System Insights Shadow  # noqa: E501

        Valid filter fields are `system_id` and `username`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_shadow(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsShadow]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_shadow_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_shadow_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_shadow_with_http_info(self, **kwargs):  # noqa: E501
        """LIst System Insights Shadow  # noqa: E501

        Valid filter fields are `system_id` and `username`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_shadow_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsShadow]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_shadow" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/shadow', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsShadow]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_shared_folders(self, **kwargs):  # noqa: E501
        """List System Insights Shared Folders  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_shared_folders(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSharedFolders]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_shared_folders_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_shared_folders_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_shared_folders_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Shared Folders  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_shared_folders_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSharedFolders]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_shared_folders" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/shared_folders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSharedFolders]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_shared_resources(self, **kwargs):  # noqa: E501
        """List System Insights Shared Resources  # noqa: E501

        Valid filter fields are `system_id` and `type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_shared_resources(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSharedResources]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_shared_resources_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_shared_resources_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_shared_resources_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Shared Resources  # noqa: E501

        Valid filter fields are `system_id` and `type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_shared_resources_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSharedResources]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_shared_resources" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/shared_resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSharedResources]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_sharing_preferences(self, **kwargs):  # noqa: E501
        """List System Insights Sharing Preferences  # noqa: E501

        Only valid filed field is `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_sharing_preferences(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSharingPreferences]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_sharing_preferences_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_sharing_preferences_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_sharing_preferences_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Sharing Preferences  # noqa: E501

        Only valid filed field is `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_sharing_preferences_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSharingPreferences]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_sharing_preferences" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/sharing_preferences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSharingPreferences]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_sip_config(self, **kwargs):  # noqa: E501
        """List System Insights SIP Config  # noqa: E501

        Valid filter fields are `system_id` and `enabled`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_sip_config(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSipConfig]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_sip_config_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_sip_config_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_sip_config_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights SIP Config  # noqa: E501

        Valid filter fields are `system_id` and `enabled`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_sip_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsSipConfig]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_sip_config" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/sip_config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSipConfig]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_startup_items(self, **kwargs):  # noqa: E501
        """List System Insights Startup Items  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_startup_items(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsStartupItems]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_startup_items_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_startup_items_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_startup_items_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Startup Items  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_startup_items_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsStartupItems]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_startup_items" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/startup_items', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsStartupItems]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_system_controls(self, **kwargs):  # noqa: E501
        """List System Insights System Control  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_system_controls(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` Note: You can only filter by `system_id` and `name` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSystemControls]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_system_controls_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_system_controls_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_system_controls_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights System Control  # noqa: E501

        Valid filter fields are `system_id` and `name`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_system_controls_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` Note: You can only filter by `system_id` and `name` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSystemControls]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_system_controls" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/system_controls', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSystemControls]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_system_info(self, **kwargs):  # noqa: E501
        """List System Insights System Info  # noqa: E501

        Valid filter fields are `system_id` and `cpu_subtype`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_system_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSystemInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_system_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_system_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_system_info_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights System Info  # noqa: E501

        Valid filter fields are `system_id` and `cpu_subtype`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_system_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsSystemInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_system_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/system_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsSystemInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_tpm_info(self, **kwargs):  # noqa: E501
        """List System Insights TPM Info  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_tpm_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsTpmInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_tpm_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_tpm_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_tpm_info_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights TPM Info  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_tpm_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsTpmInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_tpm_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/tpm_info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsTpmInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_uptime(self, **kwargs):  # noqa: E501
        """List System Insights Uptime  # noqa: E501

        Valid filter fields are `system_id` and `days`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_uptime(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, gte, in. e.g: Filter for single value: `filter=field:gte:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsUptime]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_uptime_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_uptime_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_uptime_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Uptime  # noqa: E501

        Valid filter fields are `system_id` and `days`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_uptime_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, gte, in. e.g: Filter for single value: `filter=field:gte:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsUptime]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_uptime" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/uptime', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsUptime]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_usb_devices(self, **kwargs):  # noqa: E501
        """List System Insights USB Devices  # noqa: E501

        Valid filter fields are `system_id` and `model`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_usb_devices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsUsbDevices]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_usb_devices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_usb_devices_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_usb_devices_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights USB Devices  # noqa: E501

        Valid filter fields are `system_id` and `model`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_usb_devices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsUsbDevices]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_usb_devices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/usb_devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsUsbDevices]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_user_groups(self, **kwargs):  # noqa: E501
        """List System Insights User Groups  # noqa: E501

        Only valid filter field is `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_user_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsUserGroups]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_user_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_user_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_user_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights User Groups  # noqa: E501

        Only valid filter field is `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_user_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsUserGroups]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_user_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/user_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsUserGroups]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_user_ssh_keys(self, **kwargs):  # noqa: E501
        """List System Insights User SSH Keys  # noqa: E501

        Valid filter fields are `system_id` and `uid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_user_ssh_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsUserSshKeys]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_user_ssh_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_user_ssh_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_user_ssh_keys_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights User SSH Keys  # noqa: E501

        Valid filter fields are `system_id` and `uid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_user_ssh_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param int limit:
        :return: list[SystemInsightsUserSshKeys]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_org_id', 'skip', 'sort', 'filter', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_user_ssh_keys" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/user_ssh_keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsUserSshKeys]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_userassist(self, **kwargs):  # noqa: E501
        """List System Insights User Assist  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_userassist(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsUserassist]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_userassist_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_userassist_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_userassist_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights User Assist  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_userassist_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsUserassist]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_userassist" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/userassist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsUserassist]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_users(self, **kwargs):  # noqa: E501
        """List System Insights Users  # noqa: E501

        Valid filter fields are `system_id` and `username`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_users(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsUsers]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_users_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_users_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_users_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Users  # noqa: E501

        Valid filter fields are `system_id` and `username`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsUsers]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_users" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsUsers]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_wifi_networks(self, **kwargs):  # noqa: E501
        """List System Insights WiFi Networks  # noqa: E501

        Valid filter fields are `system_id` and `security_type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_wifi_networks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWifiNetworks]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_wifi_networks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_wifi_networks_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_wifi_networks_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights WiFi Networks  # noqa: E501

        Valid filter fields are `system_id` and `security_type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_wifi_networks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWifiNetworks]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_wifi_networks" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/wifi_networks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsWifiNetworks]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_wifi_status(self, **kwargs):  # noqa: E501
        """List System Insights WiFi Status  # noqa: E501

        Valid filter fields are `system_id` and `security_type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_wifi_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWifiStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_wifi_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_wifi_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_wifi_status_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights WiFi Status  # noqa: E501

        Valid filter fields are `system_id` and `security_type`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_wifi_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWifiStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_wifi_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/wifi_status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsWifiStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_windows_security_center(self, **kwargs):  # noqa: E501
        """List System Insights Windows Security Center  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_windows_security_center(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWindowsSecurityCenter]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_windows_security_center_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_windows_security_center_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_windows_security_center_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Windows Security Center  # noqa: E501

        Valid filter fields are `system_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_windows_security_center_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWindowsSecurityCenter]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_windows_security_center" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systeminsights/windows_security_center', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsWindowsSecurityCenter]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systeminsights_list_windows_security_products(self, **kwargs):  # noqa: E501
        """List System Insights Windows Security Products  # noqa: E501

        Valid filter fields are `system_id` and `state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_windows_security_products(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWindowsSecurityProducts]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systeminsights_list_windows_security_products_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.systeminsights_list_windows_security_products_with_http_info(**kwargs)  # noqa: E501
            return data

    def systeminsights_list_windows_security_products_with_http_info(self, **kwargs):  # noqa: E501
        """List System Insights Windows Security Products  # noqa: E501

        Valid filter fields are `system_id` and `state`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systeminsights_list_windows_security_products_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. e.g: Sort by single field: `sort=field` Sort descending by single field: `sort=-field` Sort by multiple fields: `sort=field1,-field2,field3` 
        :param list[str] filter: Supported operators are: eq, in. e.g: Filter for single value: `filter=field:eq:value` Filter for any value in a list: (note \"pipe\" character: `|` separating values) `filter=field:in:value1|value2|value3` 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int limit:
        :return: list[SystemInsightsWindowsSecurityProducts]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['skip', 'sort', 'filter', 'x_org_id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systeminsights_list_windows_security_products" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/systeminsights/windows_security_products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SystemInsightsWindowsSecurityProducts]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
