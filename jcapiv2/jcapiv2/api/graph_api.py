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


class GraphApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def graph_active_directory_associations_list(self, activedirectory_id, targets, **kwargs):  # noqa: E501
        """List the associations of an Active Directory instance  # noqa: E501

        This endpoint returns the direct associations of this Active Directory instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Active Directory and Users.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/activedirectories/{ActiveDirectory_ID}/associations?targets=user \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_associations_list(activedirectory_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: (required)
        :param list[str] targets: Targets which a \"active_directory\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_active_directory_associations_list_with_http_info(activedirectory_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_active_directory_associations_list_with_http_info(activedirectory_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_active_directory_associations_list_with_http_info(self, activedirectory_id, targets, **kwargs):  # noqa: E501
        """List the associations of an Active Directory instance  # noqa: E501

        This endpoint returns the direct associations of this Active Directory instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Active Directory and Users.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/activedirectories/{ActiveDirectory_ID}/associations?targets=user \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_associations_list_with_http_info(activedirectory_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: (required)
        :param list[str] targets: Targets which a \"active_directory\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activedirectory_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_active_directory_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activedirectory_id' is set
        if ('activedirectory_id' not in params or
                params['activedirectory_id'] is None):
            raise ValueError("Missing the required parameter `activedirectory_id` when calling `graph_active_directory_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_active_directory_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activedirectory_id' in params:
            path_params['activedirectory_id'] = params['activedirectory_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/activedirectories/{activedirectory_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_active_directory_associations_post(self, activedirectory_id, **kwargs):  # noqa: E501
        """Manage the associations of an Active Directory instance  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of an Active Directory instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Active Directory and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/activedirectories/{AD_Instance_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_associations_post(activedirectory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: (required)
        :param GraphOperationActiveDirectory body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_active_directory_associations_post_with_http_info(activedirectory_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_active_directory_associations_post_with_http_info(activedirectory_id, **kwargs)  # noqa: E501
            return data

    def graph_active_directory_associations_post_with_http_info(self, activedirectory_id, **kwargs):  # noqa: E501
        """Manage the associations of an Active Directory instance  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of an Active Directory instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Active Directory and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/activedirectories/{AD_Instance_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_associations_post_with_http_info(activedirectory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: (required)
        :param GraphOperationActiveDirectory body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activedirectory_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_active_directory_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activedirectory_id' is set
        if ('activedirectory_id' not in params or
                params['activedirectory_id'] is None):
            raise ValueError("Missing the required parameter `activedirectory_id` when calling `graph_active_directory_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activedirectory_id' in params:
            path_params['activedirectory_id'] = params['activedirectory_id']  # noqa: E501

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
            '/activedirectories/{activedirectory_id}/associations', 'POST',
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

    def graph_active_directory_traverse_user(self, activedirectory_id, **kwargs):  # noqa: E501
        """List the Users bound to an Active Directory instance  # noqa: E501

        This endpoint will return all Users bound to an Active Directory instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Active Directory instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Active Directory instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/activedirectories/{ActiveDirectory_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_traverse_user(activedirectory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: ObjectID of the Active Directory instance. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_active_directory_traverse_user_with_http_info(activedirectory_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_active_directory_traverse_user_with_http_info(activedirectory_id, **kwargs)  # noqa: E501
            return data

    def graph_active_directory_traverse_user_with_http_info(self, activedirectory_id, **kwargs):  # noqa: E501
        """List the Users bound to an Active Directory instance  # noqa: E501

        This endpoint will return all Users bound to an Active Directory instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Active Directory instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Active Directory instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/activedirectories/{ActiveDirectory_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_traverse_user_with_http_info(activedirectory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: ObjectID of the Active Directory instance. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activedirectory_id', 'filter', 'limit', 'x_org_id', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_active_directory_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activedirectory_id' is set
        if ('activedirectory_id' not in params or
                params['activedirectory_id'] is None):
            raise ValueError("Missing the required parameter `activedirectory_id` when calling `graph_active_directory_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activedirectory_id' in params:
            path_params['activedirectory_id'] = params['activedirectory_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
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
            '/activedirectories/{activedirectory_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_active_directory_traverse_user_group(self, activedirectory_id, **kwargs):  # noqa: E501
        """List the User Groups bound to an Active Directory instance  # noqa: E501

        This endpoint will return all Users Groups bound to an Active Directory instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Active Directory instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Active Directory instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/activedirectories/{ActiveDirectory_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_traverse_user_group(activedirectory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: ObjectID of the Active Directory instance. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_active_directory_traverse_user_group_with_http_info(activedirectory_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_active_directory_traverse_user_group_with_http_info(activedirectory_id, **kwargs)  # noqa: E501
            return data

    def graph_active_directory_traverse_user_group_with_http_info(self, activedirectory_id, **kwargs):  # noqa: E501
        """List the User Groups bound to an Active Directory instance  # noqa: E501

        This endpoint will return all Users Groups bound to an Active Directory instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Active Directory instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Active Directory instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/activedirectories/{ActiveDirectory_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_active_directory_traverse_user_group_with_http_info(activedirectory_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str activedirectory_id: ObjectID of the Active Directory instance. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activedirectory_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_active_directory_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activedirectory_id' is set
        if ('activedirectory_id' not in params or
                params['activedirectory_id'] is None):
            raise ValueError("Missing the required parameter `activedirectory_id` when calling `graph_active_directory_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activedirectory_id' in params:
            path_params['activedirectory_id'] = params['activedirectory_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/activedirectories/{activedirectory_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_application_associations_list(self, application_id, targets, **kwargs):  # noqa: E501
        """List the associations of an Application  # noqa: E501

        This endpoint will return the _direct_ associations of an Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Applications and User Groups.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/applications/{Application_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_associations_list(application_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param list[str] targets: Targets which a \"application\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_application_associations_list_with_http_info(application_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_application_associations_list_with_http_info(application_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_application_associations_list_with_http_info(self, application_id, targets, **kwargs):  # noqa: E501
        """List the associations of an Application  # noqa: E501

        This endpoint will return the _direct_ associations of an Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Applications and User Groups.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/applications/{Application_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_associations_list_with_http_info(application_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param list[str] targets: Targets which a \"application\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_application_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `graph_application_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_application_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/applications/{application_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_application_associations_post(self, application_id, **kwargs):  # noqa: E501
        """Manage the associations of an Application  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of an Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Application and User Groups.  #### Sample Request ``` curl -X POST 'https://console.jumpcloud.com/api/v2/applications/{Application_ID}/associations' \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_associations_post(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param GraphOperationApplication body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_application_associations_post_with_http_info(application_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_application_associations_post_with_http_info(application_id, **kwargs)  # noqa: E501
            return data

    def graph_application_associations_post_with_http_info(self, application_id, **kwargs):  # noqa: E501
        """Manage the associations of an Application  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of an Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Application and User Groups.  #### Sample Request ``` curl -X POST 'https://console.jumpcloud.com/api/v2/applications/{Application_ID}/associations' \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_associations_post_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param GraphOperationApplication body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_application_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `graph_application_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501

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
            '/applications/{application_id}/associations', 'POST',
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

    def graph_application_traverse_user(self, application_id, **kwargs):  # noqa: E501
        """List the Users bound to an Application  # noqa: E501

        This endpoint will return all Users bound to an Application, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Application to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Application.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/applications/{Application_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_traverse_user(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_application_traverse_user_with_http_info(application_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_application_traverse_user_with_http_info(application_id, **kwargs)  # noqa: E501
            return data

    def graph_application_traverse_user_with_http_info(self, application_id, **kwargs):  # noqa: E501
        """List the Users bound to an Application  # noqa: E501

        This endpoint will return all Users bound to an Application, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Application to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Application.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/applications/{Application_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_traverse_user_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_application_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `graph_application_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/applications/{application_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_application_traverse_user_group(self, application_id, **kwargs):  # noqa: E501
        """List the User Groups bound to an Application  # noqa: E501

        This endpoint will return all Users Groups bound to an Application, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates  each path from this Application to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Application.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/applications/{Application_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_traverse_user_group(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_application_traverse_user_group_with_http_info(application_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_application_traverse_user_group_with_http_info(application_id, **kwargs)  # noqa: E501
            return data

    def graph_application_traverse_user_group_with_http_info(self, application_id, **kwargs):  # noqa: E501
        """List the User Groups bound to an Application  # noqa: E501

        This endpoint will return all Users Groups bound to an Application, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates  each path from this Application to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Application.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/applications/{Application_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_application_traverse_user_group_with_http_info(application_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_id: ObjectID of the Application. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_application_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params or
                params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `graph_application_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_id' in params:
            path_params['application_id'] = params['application_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/applications/{application_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_command_associations_list(self, command_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Command  # noqa: E501

        This endpoint will return the _direct_ associations of this Command.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Commands and User Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_associations_list(command_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param list[str] targets: Targets which a \"command\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_command_associations_list_with_http_info(command_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_command_associations_list_with_http_info(command_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_command_associations_list_with_http_info(self, command_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Command  # noqa: E501

        This endpoint will return the _direct_ associations of this Command.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Commands and User Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_associations_list_with_http_info(command_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param list[str] targets: Targets which a \"command\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_command_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/commands/{command_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_command_associations_post(self, command_id, **kwargs):  # noqa: E501
        """Manage the associations of a Command  # noqa: E501

        This endpoint will allow you to manage the _direct_ associations of this Command.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Commands and User Groups.   #### Sample Request ```  curl -X POST https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"Group_ID\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_associations_post(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param GraphOperationCommand body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_command_associations_post_with_http_info(command_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_command_associations_post_with_http_info(command_id, **kwargs)  # noqa: E501
            return data

    def graph_command_associations_post_with_http_info(self, command_id, **kwargs):  # noqa: E501
        """Manage the associations of a Command  # noqa: E501

        This endpoint will allow you to manage the _direct_ associations of this Command.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Commands and User Groups.   #### Sample Request ```  curl -X POST https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"Group_ID\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_associations_post_with_http_info(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param GraphOperationCommand body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']  # noqa: E501

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
            '/commands/{command_id}/associations', 'POST',
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

    def graph_command_traverse_system(self, command_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Command  # noqa: E501

        This endpoint will return all Systems bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systems \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_traverse_system(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_command_traverse_system_with_http_info(command_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_command_traverse_system_with_http_info(command_id, **kwargs)  # noqa: E501
            return data

    def graph_command_traverse_system_with_http_info(self, command_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Command  # noqa: E501

        This endpoint will return all Systems bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systems \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_traverse_system_with_http_info(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_traverse_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/commands/{command_id}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_command_traverse_system_group(self, command_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a Command  # noqa: E501

        This endpoint will return all System Groups bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systemgroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_traverse_system_group(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_command_traverse_system_group_with_http_info(command_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_command_traverse_system_group_with_http_info(command_id, **kwargs)  # noqa: E501
            return data

    def graph_command_traverse_system_group_with_http_info(self, command_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a Command  # noqa: E501

        This endpoint will return all System Groups bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systemgroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_command_traverse_system_group_with_http_info(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_traverse_system_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/commands/{command_id}/systemgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_g_suite_associations_list(self, gsuite_id, targets, **kwargs):  # noqa: E501
        """List the associations of a G Suite instance  # noqa: E501

        This endpoint returns the _direct_ associations of this G Suite instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example G Suite and Users.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_associations_list(gsuite_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param list[str] targets: Targets which a \"g_suite\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_g_suite_associations_list_with_http_info(gsuite_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_g_suite_associations_list_with_http_info(gsuite_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_g_suite_associations_list_with_http_info(self, gsuite_id, targets, **kwargs):  # noqa: E501
        """List the associations of a G Suite instance  # noqa: E501

        This endpoint returns the _direct_ associations of this G Suite instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example G Suite and Users.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_associations_list_with_http_info(gsuite_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param list[str] targets: Targets which a \"g_suite\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gsuite_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_g_suite_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gsuite_id' is set
        if ('gsuite_id' not in params or
                params['gsuite_id'] is None):
            raise ValueError("Missing the required parameter `gsuite_id` when calling `graph_g_suite_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_g_suite_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gsuite_id' in params:
            path_params['gsuite_id'] = params['gsuite_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/gsuites/{gsuite_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_g_suite_associations_post(self, gsuite_id, **kwargs):  # noqa: E501
        """Manage the associations of a G Suite instance  # noqa: E501

        This endpoint returns the _direct_ associations of this G Suite instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example G Suite and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_associations_post(gsuite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param GraphOperationGSuite body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_g_suite_associations_post_with_http_info(gsuite_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_g_suite_associations_post_with_http_info(gsuite_id, **kwargs)  # noqa: E501
            return data

    def graph_g_suite_associations_post_with_http_info(self, gsuite_id, **kwargs):  # noqa: E501
        """Manage the associations of a G Suite instance  # noqa: E501

        This endpoint returns the _direct_ associations of this G Suite instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example G Suite and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_associations_post_with_http_info(gsuite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param GraphOperationGSuite body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gsuite_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_g_suite_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gsuite_id' is set
        if ('gsuite_id' not in params or
                params['gsuite_id'] is None):
            raise ValueError("Missing the required parameter `gsuite_id` when calling `graph_g_suite_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gsuite_id' in params:
            path_params['gsuite_id'] = params['gsuite_id']  # noqa: E501

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
            '/gsuites/{gsuite_id}/associations', 'POST',
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

    def graph_g_suite_traverse_user(self, gsuite_id, **kwargs):  # noqa: E501
        """List the Users bound to a G Suite instance  # noqa: E501

        This endpoint will return all Users bound to a G Suite instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this G Suite instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this G Suite instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_traverse_user(gsuite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_g_suite_traverse_user_with_http_info(gsuite_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_g_suite_traverse_user_with_http_info(gsuite_id, **kwargs)  # noqa: E501
            return data

    def graph_g_suite_traverse_user_with_http_info(self, gsuite_id, **kwargs):  # noqa: E501
        """List the Users bound to a G Suite instance  # noqa: E501

        This endpoint will return all Users bound to a G Suite instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this G Suite instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this G Suite instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_traverse_user_with_http_info(gsuite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gsuite_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_g_suite_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gsuite_id' is set
        if ('gsuite_id' not in params or
                params['gsuite_id'] is None):
            raise ValueError("Missing the required parameter `gsuite_id` when calling `graph_g_suite_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gsuite_id' in params:
            path_params['gsuite_id'] = params['gsuite_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/gsuites/{gsuite_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_g_suite_traverse_user_group(self, gsuite_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a G Suite instance  # noqa: E501

        This endpoint will return all User Groups bound to an G Suite instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this G Suite instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this G Suite instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{GSuite_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_traverse_user_group(gsuite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_g_suite_traverse_user_group_with_http_info(gsuite_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_g_suite_traverse_user_group_with_http_info(gsuite_id, **kwargs)  # noqa: E501
            return data

    def graph_g_suite_traverse_user_group_with_http_info(self, gsuite_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a G Suite instance  # noqa: E501

        This endpoint will return all User Groups bound to an G Suite instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this G Suite instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this G Suite instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{GSuite_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_g_suite_traverse_user_group_with_http_info(gsuite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gsuite_id: ObjectID of the G Suite instance. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gsuite_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_g_suite_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gsuite_id' is set
        if ('gsuite_id' not in params or
                params['gsuite_id'] is None):
            raise ValueError("Missing the required parameter `gsuite_id` when calling `graph_g_suite_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gsuite_id' in params:
            path_params['gsuite_id'] = params['gsuite_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/gsuites/{gsuite_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_ldap_server_associations_list(self, ldapserver_id, targets, **kwargs):  # noqa: E501
        """List the associations of a LDAP Server  # noqa: E501

        This endpoint returns the _direct_ associations of this LDAP Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example LDAP and Users.  #### Sample Request  ```  curl -X GET 'https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_associations_list(ldapserver_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param list[str] targets: Targets which a \"ldap_server\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_ldap_server_associations_list_with_http_info(ldapserver_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_ldap_server_associations_list_with_http_info(ldapserver_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_ldap_server_associations_list_with_http_info(self, ldapserver_id, targets, **kwargs):  # noqa: E501
        """List the associations of a LDAP Server  # noqa: E501

        This endpoint returns the _direct_ associations of this LDAP Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example LDAP and Users.  #### Sample Request  ```  curl -X GET 'https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_associations_list_with_http_info(ldapserver_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param list[str] targets: Targets which a \"ldap_server\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ldapserver_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_ldap_server_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ldapserver_id' is set
        if ('ldapserver_id' not in params or
                params['ldapserver_id'] is None):
            raise ValueError("Missing the required parameter `ldapserver_id` when calling `graph_ldap_server_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_ldap_server_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ldapserver_id' in params:
            path_params['ldapserver_id'] = params['ldapserver_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/ldapservers/{ldapserver_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_ldap_server_associations_post(self, ldapserver_id, **kwargs):  # noqa: E501
        """Manage the associations of a LDAP Server  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a LDAP Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example LDAP and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_associations_post(ldapserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param GraphOperationLdapServer body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_ldap_server_associations_post_with_http_info(ldapserver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_ldap_server_associations_post_with_http_info(ldapserver_id, **kwargs)  # noqa: E501
            return data

    def graph_ldap_server_associations_post_with_http_info(self, ldapserver_id, **kwargs):  # noqa: E501
        """Manage the associations of a LDAP Server  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a LDAP Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example LDAP and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_associations_post_with_http_info(ldapserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param GraphOperationLdapServer body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ldapserver_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_ldap_server_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ldapserver_id' is set
        if ('ldapserver_id' not in params or
                params['ldapserver_id'] is None):
            raise ValueError("Missing the required parameter `ldapserver_id` when calling `graph_ldap_server_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ldapserver_id' in params:
            path_params['ldapserver_id'] = params['ldapserver_id']  # noqa: E501

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
            '/ldapservers/{ldapserver_id}/associations', 'POST',
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

    def graph_ldap_server_traverse_user(self, ldapserver_id, **kwargs):  # noqa: E501
        """List the Users bound to a LDAP Server  # noqa: E501

        This endpoint will return all Users bound to an LDAP Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_traverse_user(ldapserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_ldap_server_traverse_user_with_http_info(ldapserver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_ldap_server_traverse_user_with_http_info(ldapserver_id, **kwargs)  # noqa: E501
            return data

    def graph_ldap_server_traverse_user_with_http_info(self, ldapserver_id, **kwargs):  # noqa: E501
        """List the Users bound to a LDAP Server  # noqa: E501

        This endpoint will return all Users bound to an LDAP Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_traverse_user_with_http_info(ldapserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ldapserver_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_ldap_server_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ldapserver_id' is set
        if ('ldapserver_id' not in params or
                params['ldapserver_id'] is None):
            raise ValueError("Missing the required parameter `ldapserver_id` when calling `graph_ldap_server_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ldapserver_id' in params:
            path_params['ldapserver_id'] = params['ldapserver_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/ldapservers/{ldapserver_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_ldap_server_traverse_user_group(self, ldapserver_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a LDAP Server  # noqa: E501

        This endpoint will return all Users Groups bound to a LDAP Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_traverse_user_group(ldapserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_ldap_server_traverse_user_group_with_http_info(ldapserver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_ldap_server_traverse_user_group_with_http_info(ldapserver_id, **kwargs)  # noqa: E501
            return data

    def graph_ldap_server_traverse_user_group_with_http_info(self, ldapserver_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a LDAP Server  # noqa: E501

        This endpoint will return all Users Groups bound to a LDAP Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_ldap_server_traverse_user_group_with_http_info(ldapserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ldapserver_id: ObjectID of the LDAP Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ldapserver_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_ldap_server_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ldapserver_id' is set
        if ('ldapserver_id' not in params or
                params['ldapserver_id'] is None):
            raise ValueError("Missing the required parameter `ldapserver_id` when calling `graph_ldap_server_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ldapserver_id' in params:
            path_params['ldapserver_id'] = params['ldapserver_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/ldapservers/{ldapserver_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_office365_associations_list(self, office365_id, targets, **kwargs):  # noqa: E501
        """List the associations of an Office 365 instance  # noqa: E501

        This endpoint returns _direct_ associations of an Office 365 instance.   A direct association can be a non-homogeneous relationship between 2 different objects, for example Office 365 and Users.  #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/associations?targets=user_group' \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_associations_list(office365_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param list[str] targets: Targets which a \"office_365\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_office365_associations_list_with_http_info(office365_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_office365_associations_list_with_http_info(office365_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_office365_associations_list_with_http_info(self, office365_id, targets, **kwargs):  # noqa: E501
        """List the associations of an Office 365 instance  # noqa: E501

        This endpoint returns _direct_ associations of an Office 365 instance.   A direct association can be a non-homogeneous relationship between 2 different objects, for example Office 365 and Users.  #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/associations?targets=user_group' \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_associations_list_with_http_info(office365_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param list[str] targets: Targets which a \"office_365\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params or
                params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_office365_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/office365s/{office365_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_office365_associations_post(self, office365_id, **kwargs):  # noqa: E501
        """Manage the associations of an Office 365 instance  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a Office 365 instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Office 365 and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_associations_post(office365_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param GraphOperationOffice365 body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_office365_associations_post_with_http_info(office365_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_office365_associations_post_with_http_info(office365_id, **kwargs)  # noqa: E501
            return data

    def graph_office365_associations_post_with_http_info(self, office365_id, **kwargs):  # noqa: E501
        """Manage the associations of an Office 365 instance  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a Office 365 instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Office 365 and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_associations_post_with_http_info(office365_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param GraphOperationOffice365 body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params or
                params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']  # noqa: E501

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
            '/office365s/{office365_id}/associations', 'POST',
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

    def graph_office365_traverse_user(self, office365_id, **kwargs):  # noqa: E501
        """List the Users bound to an Office 365 instance  # noqa: E501

        This endpoint will return all Users bound to an Office 365 instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_traverse_user(office365_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_office365_traverse_user_with_http_info(office365_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_office365_traverse_user_with_http_info(office365_id, **kwargs)  # noqa: E501
            return data

    def graph_office365_traverse_user_with_http_info(self, office365_id, **kwargs):  # noqa: E501
        """List the Users bound to an Office 365 instance  # noqa: E501

        This endpoint will return all Users bound to an Office 365 instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_traverse_user_with_http_info(office365_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params or
                params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/office365s/{office365_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_office365_traverse_user_group(self, office365_id, **kwargs):  # noqa: E501
        """List the User Groups bound to an Office 365 instance  # noqa: E501

        This endpoint will return all Users Groups bound to an Office 365 instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_traverse_user_group(office365_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_office365_traverse_user_group_with_http_info(office365_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_office365_traverse_user_group_with_http_info(office365_id, **kwargs)  # noqa: E501
            return data

    def graph_office365_traverse_user_group_with_http_info(self, office365_id, **kwargs):  # noqa: E501
        """List the User Groups bound to an Office 365 instance  # noqa: E501

        This endpoint will return all Users Groups bound to an Office 365 instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_office365_traverse_user_group_with_http_info(office365_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params or
                params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/office365s/{office365_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_associations_list(self, policy_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Policy  # noqa: E501

        This endpoint returns the _direct_ associations of a Policy.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policies and Systems.  #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/associations?targets=system_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_associations_list(policy_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Policy. (required)
        :param list[str] targets: Targets which a \"policy\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_associations_list_with_http_info(policy_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_associations_list_with_http_info(policy_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_policy_associations_list_with_http_info(self, policy_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Policy  # noqa: E501

        This endpoint returns the _direct_ associations of a Policy.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policies and Systems.  #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/associations?targets=system_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_associations_list_with_http_info(policy_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Policy. (required)
        :param list[str] targets: Targets which a \"policy\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `graph_policy_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_policy_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/policies/{policy_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_associations_post(self, policy_id, **kwargs):  # noqa: E501
        """Manage the associations of a Policy  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a Policy.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policies and Systems.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/associations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_associations_post(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Policy. (required)
        :param GraphOperationPolicy body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_associations_post_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_associations_post_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_associations_post_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Manage the associations of a Policy  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a Policy.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policies and Systems.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/associations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"{Group_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_associations_post_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Policy. (required)
        :param GraphOperationPolicy body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `graph_policy_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

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
            '/policies/{policy_id}/associations', 'POST',
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

    def graph_policy_group_associations_list(self, group_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Policy Group.  # noqa: E501

        This endpoint returns the _direct_ associations of this Policy Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policy Groups and Policies.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/associations?targets=system \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_associations_list(group_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param list[str] targets: Targets which a \"policy_group\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_associations_list_with_http_info(group_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_associations_list_with_http_info(group_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_associations_list_with_http_info(self, group_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Policy Group.  # noqa: E501

        This endpoint returns the _direct_ associations of this Policy Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policy Groups and Policies.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/associations?targets=system \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_associations_list_with_http_info(group_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param list[str] targets: Targets which a \"policy_group\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_policy_group_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/policygroups/{group_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_group_associations_post(self, group_id, **kwargs):  # noqa: E501
        """Manage the associations of a Policy Group  # noqa: E501

        This endpoint manages the _direct_ associations of this Policy Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policy Groups and Policies.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{SystemID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_associations_post(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param GraphOperationPolicyGroup body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_associations_post_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_associations_post_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_associations_post_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Manage the associations of a Policy Group  # noqa: E501

        This endpoint manages the _direct_ associations of this Policy Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Policy Groups and Policies.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{SystemID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_associations_post_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param GraphOperationPolicyGroup body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/policygroups/{group_id}/associations', 'POST',
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

    def graph_policy_group_members_list(self, group_id, **kwargs):  # noqa: E501
        """List the members of a Policy Group  # noqa: E501

        This endpoint returns the Policy members of a Policy Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_members_list(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_members_list_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_members_list_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_members_list_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the members of a Policy Group  # noqa: E501

        This endpoint returns the Policy members of a Policy Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_members_list_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_members_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_members_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/policygroups/{group_id}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_group_members_post(self, group_id, **kwargs):  # noqa: E501
        """Manage the members of a Policy Group  # noqa: E501

        This endpoint allows you to manage the Policy members of a Policy Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"policy\",     \"id\": \"{Policy_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_members_post(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param GraphOperationPolicyGroupMember body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_members_post_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_members_post_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_members_post_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Manage the members of a Policy Group  # noqa: E501

        This endpoint allows you to manage the Policy members of a Policy Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"policy\",     \"id\": \"{Policy_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_members_post_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param GraphOperationPolicyGroupMember body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_members_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_members_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/policygroups/{group_id}/members', 'POST',
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

    def graph_policy_group_membership(self, group_id, **kwargs):  # noqa: E501
        """List the Policy Group's membership  # noqa: E501

        This endpoint returns all Policy members that are a member of this Policy Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_membership(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_membership_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_membership_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_membership_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Policy Group's membership  # noqa: E501

        This endpoint returns all Policy members that are a member of this Policy Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_membership_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'filter', 'limit', 'skip', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_membership`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
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
            '/policygroups/{group_id}/membership', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_group_traverse_system(self, group_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Policy Group  # noqa: E501

        This endpoint will return all Systems bound to a Policy Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy Group to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Policy Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_traverse_system(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_traverse_system_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_traverse_system_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_traverse_system_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Policy Group  # noqa: E501

        This endpoint will return all Systems bound to a Policy Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy Group to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Policy Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_traverse_system_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_traverse_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/policygroups/{group_id}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_group_traverse_system_group(self, group_id, **kwargs):  # noqa: E501
        """List the System Groups bound to Policy Groups  # noqa: E501

        This endpoint will return all System Groups bound to a Policy Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy Group to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Policy Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_traverse_system_group(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_group_traverse_system_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_group_traverse_system_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_group_traverse_system_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the System Groups bound to Policy Groups  # noqa: E501

        This endpoint will return all System Groups bound to a Policy Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy Group to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Policy Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policygroups/{GroupID}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_group_traverse_system_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the Policy Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_group_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_policy_group_traverse_system_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/policygroups/{group_id}/systemgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_member_of(self, policy_id, **kwargs):  # noqa: E501
        """List the parent Groups of a Policy  # noqa: E501

        This endpoint returns all the Policy Groups a Policy is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_member_of(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Policy. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_member_of_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_member_of_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_member_of_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """List the parent Groups of a Policy  # noqa: E501

        This endpoint returns all the Policy Groups a Policy is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_member_of_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Policy. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'filter', 'limit', 'skip', '_date', 'authorization', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_member_of" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `graph_policy_member_of`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

        header_params = {}
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/policies/{policy_id}/memberof', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_traverse_system(self, policy_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Policy  # noqa: E501

        This endpoint will return all Systems bound to a Policy, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Policy.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_traverse_system(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_traverse_system_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_traverse_system_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_traverse_system_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Policy  # noqa: E501

        This endpoint will return all Systems bound to a Policy, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Policy.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_traverse_system_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `graph_policy_traverse_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/policies/{policy_id}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_policy_traverse_system_group(self, policy_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a Policy  # noqa: E501

        This endpoint will return all Systems Groups bound to a Policy, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Policy.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET  https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_traverse_system_group(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_policy_traverse_system_group_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_policy_traverse_system_group_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def graph_policy_traverse_system_group_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a Policy  # noqa: E501

        This endpoint will return all Systems Groups bound to a Policy, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Policy to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Policy.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET  https://console.jumpcloud.com/api/v2/policies/{Policy_ID}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_policy_traverse_system_group_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: ObjectID of the Command. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_policy_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `graph_policy_traverse_system_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policy_id'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/policies/{policy_id}/systemgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_radius_server_associations_list(self, radiusserver_id, targets, **kwargs):  # noqa: E501
        """List the associations of a RADIUS  Server  # noqa: E501

        This endpoint returns the _direct_ associations of a Radius Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Radius Servers and Users.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/radiusservers/{RADIUS_ID}/associations?targets=user_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_associations_list(radiusserver_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param list[str] targets: Targets which a \"radius_server\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_radius_server_associations_list_with_http_info(radiusserver_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_radius_server_associations_list_with_http_info(radiusserver_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_radius_server_associations_list_with_http_info(self, radiusserver_id, targets, **kwargs):  # noqa: E501
        """List the associations of a RADIUS  Server  # noqa: E501

        This endpoint returns the _direct_ associations of a Radius Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Radius Servers and Users.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/radiusservers/{RADIUS_ID}/associations?targets=user_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_associations_list_with_http_info(radiusserver_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param list[str] targets: Targets which a \"radius_server\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['radiusserver_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_radius_server_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'radiusserver_id' is set
        if ('radiusserver_id' not in params or
                params['radiusserver_id'] is None):
            raise ValueError("Missing the required parameter `radiusserver_id` when calling `graph_radius_server_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_radius_server_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'radiusserver_id' in params:
            path_params['radiusserver_id'] = params['radiusserver_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/radiusservers/{radiusserver_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_radius_server_associations_post(self, radiusserver_id, **kwargs):  # noqa: E501
        """Manage the associations of a RADIUS Server  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a Radius Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Radius Servers and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/radiusservers/{RADIUS_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{   \"type\":\"user\",  \"id\":\"{USER_ID}\",  \"op\":\"add\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_associations_post(radiusserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param GraphOperationRadiusServer body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_radius_server_associations_post_with_http_info(radiusserver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_radius_server_associations_post_with_http_info(radiusserver_id, **kwargs)  # noqa: E501
            return data

    def graph_radius_server_associations_post_with_http_info(self, radiusserver_id, **kwargs):  # noqa: E501
        """Manage the associations of a RADIUS Server  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a Radius Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Radius Servers and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/radiusservers/{RADIUS_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{   \"type\":\"user\",  \"id\":\"{USER_ID}\",  \"op\":\"add\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_associations_post_with_http_info(radiusserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param GraphOperationRadiusServer body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['radiusserver_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_radius_server_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'radiusserver_id' is set
        if ('radiusserver_id' not in params or
                params['radiusserver_id'] is None):
            raise ValueError("Missing the required parameter `radiusserver_id` when calling `graph_radius_server_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'radiusserver_id' in params:
            path_params['radiusserver_id'] = params['radiusserver_id']  # noqa: E501

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
            '/radiusservers/{radiusserver_id}/associations', 'POST',
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

    def graph_radius_server_traverse_user(self, radiusserver_id, **kwargs):  # noqa: E501
        """List the Users bound to a RADIUS  Server  # noqa: E501

        This endpoint will return all Users bound to a RADIUS Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this RADIUS server instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this RADIUS server instance.  See `/members` and `/associations` endpoints to manage those collections.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_traverse_user(radiusserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_radius_server_traverse_user_with_http_info(radiusserver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_radius_server_traverse_user_with_http_info(radiusserver_id, **kwargs)  # noqa: E501
            return data

    def graph_radius_server_traverse_user_with_http_info(self, radiusserver_id, **kwargs):  # noqa: E501
        """List the Users bound to a RADIUS  Server  # noqa: E501

        This endpoint will return all Users bound to a RADIUS Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this RADIUS server instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this RADIUS server instance.  See `/members` and `/associations` endpoints to manage those collections.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_traverse_user_with_http_info(radiusserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['radiusserver_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_radius_server_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'radiusserver_id' is set
        if ('radiusserver_id' not in params or
                params['radiusserver_id'] is None):
            raise ValueError("Missing the required parameter `radiusserver_id` when calling `graph_radius_server_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'radiusserver_id' in params:
            path_params['radiusserver_id'] = params['radiusserver_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/radiusservers/{radiusserver_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_radius_server_traverse_user_group(self, radiusserver_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a RADIUS  Server  # noqa: E501

        This endpoint will return all Users Groups bound to a RADIUS Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this RADIUS server instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this RADIUS server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/radiusservers/{RADIUS_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_traverse_user_group(radiusserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_radius_server_traverse_user_group_with_http_info(radiusserver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_radius_server_traverse_user_group_with_http_info(radiusserver_id, **kwargs)  # noqa: E501
            return data

    def graph_radius_server_traverse_user_group_with_http_info(self, radiusserver_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a RADIUS  Server  # noqa: E501

        This endpoint will return all Users Groups bound to a RADIUS Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this RADIUS server instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this RADIUS server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/radiusservers/{RADIUS_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_radius_server_traverse_user_group_with_http_info(radiusserver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str radiusserver_id: ObjectID of the Radius Server. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['radiusserver_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_radius_server_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'radiusserver_id' is set
        if ('radiusserver_id' not in params or
                params['radiusserver_id'] is None):
            raise ValueError("Missing the required parameter `radiusserver_id` when calling `graph_radius_server_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'radiusserver_id' in params:
            path_params['radiusserver_id'] = params['radiusserver_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/radiusservers/{radiusserver_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_softwareapps_associations_list(self, software_app_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Software Application  # noqa: E501

        This endpoint will return the _direct_ associations of a Software Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Software Application and System Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_associations_list(software_app_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param list[str] targets: Targets which a \"software_app\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_softwareapps_associations_list_with_http_info(software_app_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_softwareapps_associations_list_with_http_info(software_app_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_softwareapps_associations_list_with_http_info(self, software_app_id, targets, **kwargs):  # noqa: E501
        """List the associations of a Software Application  # noqa: E501

        This endpoint will return the _direct_ associations of a Software Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Software Application and System Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_associations_list_with_http_info(software_app_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param list[str] targets: Targets which a \"software_app\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['software_app_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_softwareapps_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'software_app_id' is set
        if ('software_app_id' not in params or
                params['software_app_id'] is None):
            raise ValueError("Missing the required parameter `software_app_id` when calling `graph_softwareapps_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_softwareapps_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_app_id' in params:
            path_params['software_app_id'] = params['software_app_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/softwareapps/{software_app_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_softwareapps_associations_post(self, software_app_id, **kwargs):  # noqa: E501
        """Manage the associations of a software application.  # noqa: E501

        This endpoint allows you to associate or disassociate a software application to a system or system group.  #### Sample Request ``` $ curl -X POST https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/associations \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{   \"id\": \"<object_id>\",   \"op\": \"add\",   \"type\": \"system\"  }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_associations_post(software_app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param GraphOperationSoftwareApp body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_softwareapps_associations_post_with_http_info(software_app_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_softwareapps_associations_post_with_http_info(software_app_id, **kwargs)  # noqa: E501
            return data

    def graph_softwareapps_associations_post_with_http_info(self, software_app_id, **kwargs):  # noqa: E501
        """Manage the associations of a software application.  # noqa: E501

        This endpoint allows you to associate or disassociate a software application to a system or system group.  #### Sample Request ``` $ curl -X POST https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/associations \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{   \"id\": \"<object_id>\",   \"op\": \"add\",   \"type\": \"system\"  }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_associations_post_with_http_info(software_app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param GraphOperationSoftwareApp body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['software_app_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_softwareapps_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'software_app_id' is set
        if ('software_app_id' not in params or
                params['software_app_id'] is None):
            raise ValueError("Missing the required parameter `software_app_id` when calling `graph_softwareapps_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_app_id' in params:
            path_params['software_app_id'] = params['software_app_id']  # noqa: E501

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
            '/softwareapps/{software_app_id}/associations', 'POST',
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

    def graph_softwareapps_traverse_system(self, software_app_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Software App.  # noqa: E501

        This endpoint will return all Systems bound to a Software App, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Software App to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Software App.  See `/associations` endpoint to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_traverse_system(software_app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_softwareapps_traverse_system_with_http_info(software_app_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_softwareapps_traverse_system_with_http_info(software_app_id, **kwargs)  # noqa: E501
            return data

    def graph_softwareapps_traverse_system_with_http_info(self, software_app_id, **kwargs):  # noqa: E501
        """List the Systems bound to a Software App.  # noqa: E501

        This endpoint will return all Systems bound to a Software App, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Software App to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Software App.  See `/associations` endpoint to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_traverse_system_with_http_info(software_app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['software_app_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_softwareapps_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'software_app_id' is set
        if ('software_app_id' not in params or
                params['software_app_id'] is None):
            raise ValueError("Missing the required parameter `software_app_id` when calling `graph_softwareapps_traverse_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_app_id' in params:
            path_params['software_app_id'] = params['software_app_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/softwareapps/{software_app_id}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_softwareapps_traverse_system_group(self, software_app_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a Software App.  # noqa: E501

        This endpoint will return all Systems Groups bound to a Software App, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Software App to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Software App.  See `/associations` endpoint to manage those collections.  #### Sample Request ``` curl -X GET  https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_traverse_system_group(software_app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_softwareapps_traverse_system_group_with_http_info(software_app_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_softwareapps_traverse_system_group_with_http_info(software_app_id, **kwargs)  # noqa: E501
            return data

    def graph_softwareapps_traverse_system_group_with_http_info(self, software_app_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a Software App.  # noqa: E501

        This endpoint will return all Systems Groups bound to a Software App, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Software App to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Software App.  See `/associations` endpoint to manage those collections.  #### Sample Request ``` curl -X GET  https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_softwareapps_traverse_system_group_with_http_info(software_app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str software_app_id: ObjectID of the Software App. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['software_app_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_softwareapps_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'software_app_id' is set
        if ('software_app_id' not in params or
                params['software_app_id'] is None):
            raise ValueError("Missing the required parameter `software_app_id` when calling `graph_softwareapps_traverse_system_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'software_app_id' in params:
            path_params['software_app_id'] = params['software_app_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/softwareapps/{software_app_id}/systemgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_associations_list(self, system_id, targets, **kwargs):  # noqa: E501
        """List the associations of a System  # noqa: E501

        This endpoint returns the _direct_ associations of a System.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Systems and Users.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/associations?targets=user \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_associations_list(system_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param list[str] targets: Targets which a \"system\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_associations_list_with_http_info(system_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_associations_list_with_http_info(system_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_system_associations_list_with_http_info(self, system_id, targets, **kwargs):  # noqa: E501
        """List the associations of a System  # noqa: E501

        This endpoint returns the _direct_ associations of a System.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Systems and Users.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/associations?targets=user \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_associations_list_with_http_info(system_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param list[str] targets: Targets which a \"system\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'targets', 'limit', 'skip', '_date', 'authorization', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_system_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

        header_params = {}
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/systems/{system_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_associations_post(self, system_id, **kwargs):  # noqa: E501
        """Manage associations of a System  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a System.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Systems and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systems/{System_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"attributes\": {       \"sudo\": {         \"enabled\": true,         \"withoutPassword\": false       }     },     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"UserID\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_associations_post(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param GraphOperationSystem body:
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_associations_post_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_associations_post_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_associations_post_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """Manage associations of a System  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a System.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Systems and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systems/{System_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"attributes\": {       \"sudo\": {         \"enabled\": true,         \"withoutPassword\": false       }     },     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"UserID\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_associations_post_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param GraphOperationSystem body:
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'body', '_date', 'authorization', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []

        header_params = {}
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/systems/{system_id}/associations', 'POST',
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

    def graph_system_group_associations_list(self, group_id, targets, **kwargs):  # noqa: E501
        """List the associations of a System Group  # noqa: E501

        This endpoint returns the _direct_ associations of a System Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example System Groups and Users.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/associations?targets=user \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_associations_list(group_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param list[str] targets: Targets which a \"system_group\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_associations_list_with_http_info(group_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_associations_list_with_http_info(group_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_system_group_associations_list_with_http_info(self, group_id, targets, **kwargs):  # noqa: E501
        """List the associations of a System Group  # noqa: E501

        This endpoint returns the _direct_ associations of a System Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example System Groups and Users.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/associations?targets=user \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_associations_list_with_http_info(group_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param list[str] targets: Targets which a \"system_group\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_system_group_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/systemgroups/{group_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_associations_post(self, group_id, **kwargs):  # noqa: E501
        """Manage the associations of a System Group  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a System Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example System Groups and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{UserID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_associations_post(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param GraphOperationSystemGroup body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_associations_post_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_associations_post_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_associations_post_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Manage the associations of a System Group  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a System Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example System Groups and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{UserID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_associations_post_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param GraphOperationSystemGroup body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/systemgroups/{group_id}/associations', 'POST',
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

    def graph_system_group_members_list(self, group_id, **kwargs):  # noqa: E501
        """List the members of a System Group  # noqa: E501

        This endpoint returns the system members of a System Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_members_list(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_members_list_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_members_list_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_members_list_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the members of a System Group  # noqa: E501

        This endpoint returns the system members of a System Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_members_list_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_members_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_members_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/systemgroups/{group_id}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_members_post(self, group_id, **kwargs):  # noqa: E501
        """Manage the members of a System Group  # noqa: E501

        This endpoint allows you to manage the system members of a System Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{System_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_members_post(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param GraphOperationSystemGroupMember body:
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_members_post_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_members_post_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_members_post_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Manage the members of a System Group  # noqa: E501

        This endpoint allows you to manage the system members of a System Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{System_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_members_post_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param GraphOperationSystemGroupMember body:
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body', '_date', 'authorization', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_members_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_members_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []

        header_params = {}
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/systemgroups/{group_id}/members', 'POST',
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

    def graph_system_group_membership(self, group_id, **kwargs):  # noqa: E501
        """List the System Group's membership  # noqa: E501

        This endpoint returns all Systems that are a member of this System Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_membership(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_membership_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_membership_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_membership_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the System Group's membership  # noqa: E501

        This endpoint returns all Systems that are a member of this System Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_membership_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'skip', 'sort', 'filter', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_membership`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
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
            '/systemgroups/{group_id}/membership', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_traverse_command(self, group_id, **kwargs):  # noqa: E501
        """List the Commands bound to a System Group  # noqa: E501

        This endpoint will return all Commands bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding Command; this array represents all grouping and/or associations that would have to be removed to deprovision the Command from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/commands \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_command(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_traverse_command_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_traverse_command_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_traverse_command_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Commands bound to a System Group  # noqa: E501

        This endpoint will return all Commands bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding Command; this array represents all grouping and/or associations that would have to be removed to deprovision the Command from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/commands \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_command_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_traverse_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_traverse_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systemgroups/{group_id}/commands', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_traverse_policy(self, group_id, **kwargs):  # noqa: E501
        """List the Policies bound to a System Group  # noqa: E501

        This endpoint will return all Policies bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding Policy; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  This endpoint is not public yet as we haven't finished the code.  ##### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/policies \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_policy(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_traverse_policy_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_traverse_policy_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_traverse_policy_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Policies bound to a System Group  # noqa: E501

        This endpoint will return all Policies bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding Policy; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  This endpoint is not public yet as we haven't finished the code.  ##### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/policies \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_policy_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_traverse_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_traverse_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systemgroups/{group_id}/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_traverse_policy_group(self, group_id, **kwargs):  # noqa: E501
        """List the Policy Groups bound to a System Group  # noqa: E501

        This endpoint will return all Policy Groups bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding Policy Group; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy Group from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/policygroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_policy_group(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_traverse_policy_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_traverse_policy_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_traverse_policy_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Policy Groups bound to a System Group  # noqa: E501

        This endpoint will return all Policy Groups bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding Policy Group; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy Group from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/policygroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_policy_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_traverse_policy_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_traverse_policy_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systemgroups/{group_id}/policygroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_traverse_user(self, group_id, **kwargs):  # noqa: E501
        """List the Users bound to a System Group  # noqa: E501

        This endpoint will return all Users bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_user(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_traverse_user_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_traverse_user_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_traverse_user_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Users bound to a System Group  # noqa: E501

        This endpoint will return all Users bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_user_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systemgroups/{group_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_group_traverse_user_group(self, group_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a System Group  # noqa: E501

        This endpoint will return all User Groups bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_user_group(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_group_traverse_user_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_group_traverse_user_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_system_group_traverse_user_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a System Group  # noqa: E501

        This endpoint will return all User Groups bound to a System Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System Group to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this System Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{GroupID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_group_traverse_user_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the System Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_group_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_system_group_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systemgroups/{group_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_member_of(self, system_id, **kwargs):  # noqa: E501
        """List the parent Groups of a System  # noqa: E501

        This endpoint returns all the System Groups a System is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_member_of(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_member_of_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_member_of_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_member_of_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the parent Groups of a System  # noqa: E501

        This endpoint returns all the System Groups a System is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_member_of_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'filter', 'limit', 'skip', '_date', 'authorization', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_member_of" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_member_of`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501

        header_params = {}
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
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
            '/systems/{system_id}/memberof', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_traverse_command(self, system_id, **kwargs):  # noqa: E501
        """List the Commands bound to a System  # noqa: E501

        This endpoint will return all Commands bound to a System, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding Command; this array represents all grouping and/or associations that would have to be removed to deprovision the Command from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/commands \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_command(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_traverse_command_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_traverse_command_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_traverse_command_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the Commands bound to a System  # noqa: E501

        This endpoint will return all Commands bound to a System, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding Command; this array represents all grouping and/or associations that would have to be removed to deprovision the Command from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/commands \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_command_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_traverse_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_traverse_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systems/{system_id}/commands', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_traverse_policy(self, system_id, **kwargs):  # noqa: E501
        """List the Policies bound to a System  # noqa: E501

        This endpoint will return all Policies bound to a System, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding Policy; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy from this System.  See `/members` and `/associations` endpoints to manage those collections.  This endpoint is not yet public as we have finish the code.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/{System_ID}/policies \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_policy(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_traverse_policy_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_traverse_policy_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_traverse_policy_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the Policies bound to a System  # noqa: E501

        This endpoint will return all Policies bound to a System, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding Policy; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy from this System.  See `/members` and `/associations` endpoints to manage those collections.  This endpoint is not yet public as we have finish the code.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/{System_ID}/policies \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_policy_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_traverse_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_traverse_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/systems/{system_id}/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_traverse_policy_group(self, system_id, **kwargs):  # noqa: E501
        """List the Policy Groups bound to a System  # noqa: E501

        This endpoint will return all Policy Groups bound to a System, either directly or indirectly essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding Policy Group; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy Group from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/policygroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_policy_group(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_traverse_policy_group_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_traverse_policy_group_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_traverse_policy_group_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the Policy Groups bound to a System  # noqa: E501

        This endpoint will return all Policy Groups bound to a System, either directly or indirectly essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding Policy Group; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy Group from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/policygroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_policy_group_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'limit', 'x_org_id', 'skip', '_date', 'authorization', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_traverse_policy_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_traverse_policy_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/systems/{system_id}/policygroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_traverse_user(self, system_id, **kwargs):  # noqa: E501
        """List the Users bound to a System  # noqa: E501

        This endpoint will return all Users bound to a System, either directly or indirectly essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_user(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_traverse_user_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_traverse_user_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_traverse_user_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the Users bound to a System  # noqa: E501

        This endpoint will return all Users bound to a System, either directly or indirectly essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_user_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'limit', 'x_org_id', 'skip', '_date', 'authorization', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_traverse_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/systems/{system_id}/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_system_traverse_user_group(self, system_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a System  # noqa: E501

        This endpoint will return all User Groups bound to a System, either directly or indirectly essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_user_group(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_system_traverse_user_group_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_system_traverse_user_group_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def graph_system_traverse_user_group_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the User Groups bound to a System  # noqa: E501

        This endpoint will return all User Groups bound to a System, either directly or indirectly essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this System to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_system_traverse_user_group_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param str _date: Current date header for the System Context API
        :param str authorization: Authorization header for the System Context API
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'limit', 'x_org_id', 'skip', '_date', 'authorization', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_system_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `graph_system_traverse_user_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501
        if '_date' in params:
            header_params['Date'] = params['_date']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/systems/{system_id}/usergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_associations_list(self, user_id, targets, **kwargs):  # noqa: E501
        """List the associations of a User  # noqa: E501

        This endpoint returns the _direct_ associations of a User.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Users and Systems.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/associations?targets=system_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_associations_list(user_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param list[str] targets: Targets which a \"user\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_associations_list_with_http_info(user_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_associations_list_with_http_info(user_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_user_associations_list_with_http_info(self, user_id, targets, **kwargs):  # noqa: E501
        """List the associations of a User  # noqa: E501

        This endpoint returns the _direct_ associations of a User.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Users and Systems.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/associations?targets=system_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_associations_list_with_http_info(user_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param list[str] targets: Targets which a \"user\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_user_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/users/{user_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_associations_post(self, user_id, **kwargs):  # noqa: E501
        """Manage the associations of a User  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a User.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Users and Systems.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/users/{UserID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"attributes\": {       \"sudo\": {       \"enabled\": true,         \"withoutPassword\": false       }     },     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"{GroupID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_associations_post(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param GraphOperationUser body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_associations_post_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_associations_post_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_associations_post_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Manage the associations of a User  # noqa: E501

        This endpoint allows you to manage the _direct_ associations of a User.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Users and Systems.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/users/{UserID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"attributes\": {       \"sudo\": {       \"enabled\": true,         \"withoutPassword\": false       }     },     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"{GroupID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_associations_post_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param GraphOperationUser body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

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
            '/users/{user_id}/associations', 'POST',
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

    def graph_user_group_associations_list(self, group_id, targets, **kwargs):  # noqa: E501
        """List the associations of a User Group.  # noqa: E501

        This endpoint returns the _direct_ associations of this User Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example User Groups and Users.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/associations?targets=system \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_associations_list(group_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param list[str] targets: Targets which a \"user_group\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_associations_list_with_http_info(group_id, targets, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_associations_list_with_http_info(group_id, targets, **kwargs)  # noqa: E501
            return data

    def graph_user_group_associations_list_with_http_info(self, group_id, targets, **kwargs):  # noqa: E501
        """List the associations of a User Group.  # noqa: E501

        This endpoint returns the _direct_ associations of this User Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example User Groups and Users.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/associations?targets=system \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_associations_list_with_http_info(group_id, targets, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param list[str] targets: Targets which a \"user_group\" can be associated to. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'targets', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_associations_list`")  # noqa: E501
        # verify the required parameter 'targets' is set
        if ('targets' not in params or
                params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_user_group_associations_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))  # noqa: E501
            collection_formats['targets'] = 'csv'  # noqa: E501
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
            '/usergroups/{group_id}/associations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_associations_post(self, group_id, **kwargs):  # noqa: E501
        """Manage the associations of a User Group  # noqa: E501

        This endpoint manages the _direct_ associations of this User Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example User Groups and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{SystemID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_associations_post(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param GraphOperationUserGroup body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_associations_post_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_associations_post_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_associations_post_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Manage the associations of a User Group  # noqa: E501

        This endpoint manages the _direct_ associations of this User Group.  A direct association can be a non-homogeneous relationship between 2 different objects, for example User Groups and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{SystemID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_associations_post_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param GraphOperationUserGroup body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_associations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/usergroups/{group_id}/associations', 'POST',
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

    def graph_user_group_members_list(self, group_id, **kwargs):  # noqa: E501
        """List the members of a User Group  # noqa: E501

        This endpoint returns the user members of a User Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_members_list(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_members_list_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_members_list_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_members_list_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the members of a User Group  # noqa: E501

        This endpoint returns the user members of a User Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_members_list_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_members_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_members_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/usergroups/{group_id}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphConnection]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_members_post(self, group_id, **kwargs):  # noqa: E501
        """Manage the members of a User Group  # noqa: E501

        This endpoint allows you to manage the user members of a User Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_members_post(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param GraphOperationUserGroupMember body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_members_post_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_members_post_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_members_post_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Manage the members of a User Group  # noqa: E501

        This endpoint allows you to manage the user members of a User Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_members_post_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param GraphOperationUserGroupMember body:
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_members_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_members_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

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
            '/usergroups/{group_id}/members', 'POST',
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

    def graph_user_group_membership(self, group_id, **kwargs):  # noqa: E501
        """List the User Group's membership  # noqa: E501

        This endpoint returns all users members that are a member of this User Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_membership(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_membership_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_membership_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_membership_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the User Group's membership  # noqa: E501

        This endpoint returns all users members that are a member of this User Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_membership_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'filter', 'limit', 'skip', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_membership`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
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
            '/usergroups/{group_id}/membership', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_active_directory(self, group_id, **kwargs):  # noqa: E501
        """List the Active Directories bound to a User Group  # noqa: E501

        This endpoint will return all Active Directory Instances bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Active Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Active Directory from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/activedirectories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_active_directory(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_active_directory_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_active_directory_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_active_directory_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Active Directories bound to a User Group  # noqa: E501

        This endpoint will return all Active Directory Instances bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Active Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Active Directory from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/activedirectories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_active_directory_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_active_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_active_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/activedirectories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_application(self, group_id, **kwargs):  # noqa: E501
        """List the Applications bound to a User Group  # noqa: E501

        This endpoint will return all Applications bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Application; this array represents all grouping and/or associations that would have to be removed to deprovision the Application from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_application(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_application_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_application_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_application_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Applications bound to a User Group  # noqa: E501

        This endpoint will return all Applications bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Application; this array represents all grouping and/or associations that would have to be removed to deprovision the Application from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_application_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_directory(self, group_id, **kwargs):  # noqa: E501
        """List the Directories bound to a User Group  # noqa: E501

        This endpoint will return all Directories bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Directories from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/directories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_directory(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_directory_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_directory_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_directory_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Directories bound to a User Group  # noqa: E501

        This endpoint will return all Directories bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Directories from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/directories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_directory_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/directories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_g_suite(self, group_id, **kwargs):  # noqa: E501
        """List the G Suite instances bound to a User Group  # noqa: E501

        This endpoint will return all G Suite Instances bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding G Suite instance; this array represents all grouping and/or associations that would have to be removed to deprovision the G Suite instance from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID/gsuites \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_g_suite(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_g_suite_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_g_suite_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_g_suite_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the G Suite instances bound to a User Group  # noqa: E501

        This endpoint will return all G Suite Instances bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding G Suite instance; this array represents all grouping and/or associations that would have to be removed to deprovision the G Suite instance from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID/gsuites \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_g_suite_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_g_suite" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_g_suite`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/gsuites', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_ldap_server(self, group_id, **kwargs):  # noqa: E501
        """List the LDAP Servers bound to a User Group  # noqa: E501

        This endpoint will return all LDAP Servers bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding LDAP Server; this array represents all grouping and/or associations that would have to be removed to deprovision the LDAP Server from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/ldapservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_ldap_server(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_ldap_server_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_ldap_server_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_ldap_server_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the LDAP Servers bound to a User Group  # noqa: E501

        This endpoint will return all LDAP Servers bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding LDAP Server; this array represents all grouping and/or associations that would have to be removed to deprovision the LDAP Server from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/ldapservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_ldap_server_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_ldap_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_ldap_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/ldapservers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_office365(self, group_id, **kwargs):  # noqa: E501
        """List the Office 365 instances bound to a User Group  # noqa: E501

        This endpoint will return all Office 365 instances bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Office 365 instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Office 365 instance from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/office365s \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_office365(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_office365_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_office365_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_office365_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Office 365 instances bound to a User Group  # noqa: E501

        This endpoint will return all Office 365 instances bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding Office 365 instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Office 365 instance from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/office365s \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_office365_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_office365" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_office365`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/office365s', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_radius_server(self, group_id, **kwargs):  # noqa: E501
        """List the RADIUS Servers bound to a User Group  # noqa: E501

        This endpoint will return all RADIUS servers bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding RADIUS Server; this array represents all grouping and/or associations that would have to be removed to deprovision the RADIUS Server from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/radiusservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_radius_server(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_radius_server_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_radius_server_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_radius_server_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the RADIUS Servers bound to a User Group  # noqa: E501

        This endpoint will return all RADIUS servers bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding RADIUS Server; this array represents all grouping and/or associations that would have to be removed to deprovision the RADIUS Server from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/radiusservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_radius_server_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_radius_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_radius_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/radiusservers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_system(self, group_id, **kwargs):  # noqa: E501
        """List the Systems bound to a User Group  # noqa: E501

        This endpoint will return all Systems bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_system(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_system_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_system_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_system_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the Systems bound to a User Group  # noqa: E501

        This endpoint will return all Systems bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_system_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_group_traverse_system_group(self, group_id, **kwargs):  # noqa: E501
        """List the System Groups bound to User Groups  # noqa: E501

        This endpoint will return all System Groups bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_system_group(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_group_traverse_system_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_group_traverse_system_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def graph_user_group_traverse_system_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """List the System Groups bound to User Groups  # noqa: E501

        This endpoint will return all System Groups bound to a User Group, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User Group to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this User Group.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/usergroups/{GroupID}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_group_traverse_system_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: ObjectID of the User Group. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_group_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `graph_user_group_traverse_system_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group_id'] = params['group_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/usergroups/{group_id}/systemgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_member_of(self, user_id, **kwargs):  # noqa: E501
        """List the parent Groups of a User  # noqa: E501

        This endpoint returns all the User Groups a User is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_member_of(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_member_of_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_member_of_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_member_of_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the parent Groups of a User  # noqa: E501

        This endpoint returns all the User Groups a User is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_member_of_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'filter', 'limit', 'skip', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_member_of" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_member_of`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
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
            '/users/{user_id}/memberof', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_active_directory(self, user_id, **kwargs):  # noqa: E501
        """List the Active Directory instances bound to a User  # noqa: E501

        This endpoint will return all Active Directory Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Active Directory instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Active Directory instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/activedirectories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_active_directory(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_active_directory_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_active_directory_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_active_directory_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the Active Directory instances bound to a User  # noqa: E501

        This endpoint will return all Active Directory Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Active Directory instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Active Directory instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/activedirectories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_active_directory_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'filter', 'limit', 'x_org_id', 'skip']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_active_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_active_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
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
            '/users/{user_id}/activedirectories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_application(self, user_id, **kwargs):  # noqa: E501
        """List the Applications bound to a User  # noqa: E501

        This endpoint will return all Applications bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Application; this array represents all grouping and/or associations that would have to be removed to deprovision the Application from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_application(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_application_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_application_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_application_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the Applications bound to a User  # noqa: E501

        This endpoint will return all Applications bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Application; this array represents all grouping and/or associations that would have to be removed to deprovision the Application from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_application_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_directory(self, user_id, **kwargs):  # noqa: E501
        """List the Directories bound to a User  # noqa: E501

        This endpoint will return all Directories bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Directory from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/directories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_directory(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_directory_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_directory_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_directory_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the Directories bound to a User  # noqa: E501

        This endpoint will return all Directories bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Directory from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/directories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_directory_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/directories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_g_suite(self, user_id, **kwargs):  # noqa: E501
        """List the G Suite instances bound to a User  # noqa: E501

        This endpoint will return all G-Suite Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding G Suite instance; this array represents all grouping and/or associations that would have to be removed to deprovision the G Suite instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/gsuites \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_g_suite(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_g_suite_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_g_suite_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_g_suite_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the G Suite instances bound to a User  # noqa: E501

        This endpoint will return all G-Suite Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding G Suite instance; this array represents all grouping and/or associations that would have to be removed to deprovision the G Suite instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/gsuites \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_g_suite_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_g_suite" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_g_suite`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/gsuites', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_ldap_server(self, user_id, **kwargs):  # noqa: E501
        """List the LDAP servers bound to a User  # noqa: E501

        This endpoint will return all LDAP Servers bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding LDAP Server; this array represents all grouping and/or associations that would have to be removed to deprovision the LDAP Server from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/ldapservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_ldap_server(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_ldap_server_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_ldap_server_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_ldap_server_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the LDAP servers bound to a User  # noqa: E501

        This endpoint will return all LDAP Servers bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding LDAP Server; this array represents all grouping and/or associations that would have to be removed to deprovision the LDAP Server from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/ldapservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_ldap_server_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_ldap_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_ldap_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/ldapservers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_office365(self, user_id, **kwargs):  # noqa: E501
        """List the Office 365 instances bound to a User  # noqa: E501

        This endpoint will return all Office 365 Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Office 365 instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Office 365 instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/office365s \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_office365(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_office365_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_office365_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_office365_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the Office 365 instances bound to a User  # noqa: E501

        This endpoint will return all Office 365 Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Office 365 instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Office 365 instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/office365s \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_office365_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_office365" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_office365`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/office365s', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_radius_server(self, user_id, **kwargs):  # noqa: E501
        """List the RADIUS Servers bound to a User  # noqa: E501

        This endpoint will return all RADIUS Servers bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding RADIUS Server; this array represents all grouping and/or associations that would have to be removed to deprovision the RADIUS Server from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/radiusservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_radius_server(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_radius_server_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_radius_server_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_radius_server_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the RADIUS Servers bound to a User  # noqa: E501

        This endpoint will return all RADIUS Servers bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding RADIUS Server; this array represents all grouping and/or associations that would have to be removed to deprovision the RADIUS Server from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/radiusservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_radius_server_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_radius_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_radius_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/radiusservers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_system(self, user_id, **kwargs):  # noqa: E501
        """List the Systems bound to a User  # noqa: E501

        This endpoint will return all Systems bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/systems\\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_system(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_system_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_system_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_system_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the Systems bound to a User  # noqa: E501

        This endpoint will return all Systems bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/systems\\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_system_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_system`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def graph_user_traverse_system_group(self, user_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a User  # noqa: E501

        This endpoint will return all System Groups bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/systemgroups\\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_system_group(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.graph_user_traverse_system_group_with_http_info(user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.graph_user_traverse_system_group_with_http_info(user_id, **kwargs)  # noqa: E501
            return data

    def graph_user_traverse_system_group_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """List the System Groups bound to a User  # noqa: E501

        This endpoint will return all System Groups bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/systemgroups\\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graph_user_traverse_system_group_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: ObjectID of the User. (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :param int skip: The offset into the records to return.
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'limit', 'x_org_id', 'skip', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_user_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `graph_user_traverse_system_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
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
            '/users/{user_id}/systemgroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GraphObjectWithPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def policystatuses_systems_list(self, system_id, **kwargs):  # noqa: E501
        """List the policy statuses for a system  # noqa: E501

        This endpoint returns the policy results for a particular system.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/policystatuses \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.policystatuses_systems_list(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[PolicyResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.policystatuses_systems_list_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.policystatuses_systems_list_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def policystatuses_systems_list_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """List the policy statuses for a system  # noqa: E501

        This endpoint returns the policy results for a particular system.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/systems/{System_ID}/policystatuses \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.policystatuses_systems_list_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str system_id: ObjectID of the System. (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param str x_org_id: Organization identifier that can be obtained from console settings.
        :return: list[PolicyResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id', 'fields', 'filter', 'limit', 'skip', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method policystatuses_systems_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `policystatuses_systems_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['system_id'] = params['system_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
            collection_formats['filter'] = 'csv'  # noqa: E501
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
            '/systems/{system_id}/policystatuses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PolicyResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
