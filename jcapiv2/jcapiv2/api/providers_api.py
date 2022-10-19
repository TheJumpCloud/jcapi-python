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


class ProvidersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def autotask_create_configuration(self, provider_id, **kwargs):  # noqa: E501
        """Creates a new Autotask integration for the provider  # noqa: E501

        Creates a new Autotask integration for the provider. You must be associated with the provider to use this route. A 422 Unprocessable Entity response means the server failed to validate with Autotask.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_create_configuration(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param AutotaskIntegrationReq body:
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_create_configuration_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_create_configuration_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def autotask_create_configuration_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Creates a new Autotask integration for the provider  # noqa: E501

        Creates a new Autotask integration for the provider. You must be associated with the provider to use this route. A 422 Unprocessable Entity response means the server failed to validate with Autotask.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_create_configuration_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param AutotaskIntegrationReq body:
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_create_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `autotask_create_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/providers/{provider_id}/integrations/autotask', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_delete_configuration(self, uuid, **kwargs):  # noqa: E501
        """Delete Autotask Integration  # noqa: E501

        Removes a Autotask integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_delete_configuration(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_delete_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_delete_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_delete_configuration_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Delete Autotask Integration  # noqa: E501

        Removes a Autotask integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_delete_configuration_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_delete_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_delete_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}', 'DELETE',
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

    def autotask_get_configuration(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Integration Configuration  # noqa: E501

        Retrieves configuration for given Autotask integration id. You must be associated to the provider the integration is tied to in order to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_get_configuration(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: AutotaskIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_get_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_get_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_get_configuration_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Integration Configuration  # noqa: E501

        Retrieves configuration for given Autotask integration id. You must be associated to the provider the integration is tied to in order to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_get_configuration_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: AutotaskIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_get_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_get_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskIntegration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_patch_mappings(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete Autotask Mappings  # noqa: E501

        Create, edit, and/or delete mappings between Jumpcloud organizations and Autotask companies/contracts/services. You must be associated to the same provider as the Autotask integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_patch_mappings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param AutotaskMappingRequest body:
        :return: AutotaskMappingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_patch_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_patch_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_patch_mappings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete Autotask Mappings  # noqa: E501

        Create, edit, and/or delete mappings between Jumpcloud organizations and Autotask companies/contracts/services. You must be associated to the same provider as the Autotask integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_patch_mappings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param AutotaskMappingRequest body:
        :return: AutotaskMappingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_patch_mappings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_patch_mappings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/integrations/autotask/{UUID}/mappings', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskMappingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_patch_settings(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete Autotask Integration settings  # noqa: E501

        Create, edit, and/or delete Autotask settings. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_patch_settings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param AutotaskSettingsPatchReq body:
        :return: AutotaskSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_patch_settings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_patch_settings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_patch_settings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete Autotask Integration settings  # noqa: E501

        Create, edit, and/or delete Autotask settings. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_patch_settings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param AutotaskSettingsPatchReq body:
        :return: AutotaskSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_patch_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_patch_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/integrations/autotask/{UUID}/settings', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_all_alert_configuration_options(self, provider_id, **kwargs):  # noqa: E501
        """Get all Autotask ticketing alert configuration options for a provider  # noqa: E501

        Get all Autotask ticketing alert configuration options for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_all_alert_configuration_options(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: AutotaskTicketingAlertConfigurationOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_all_alert_configuration_options_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_all_alert_configuration_options_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_all_alert_configuration_options_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Get all Autotask ticketing alert configuration options for a provider  # noqa: E501

        Get all Autotask ticketing alert configuration options for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_all_alert_configuration_options_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: AutotaskTicketingAlertConfigurationOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_all_alert_configuration_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `autotask_retrieve_all_alert_configuration_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/integrations/autotask/alerts/configuration/options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskTicketingAlertConfigurationOptions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_all_alert_configurations(self, provider_id, **kwargs):  # noqa: E501
        """Get all Autotask ticketing alert configurations for a provider  # noqa: E501

        Get all Autotask ticketing alert configurations for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_all_alert_configurations(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: AutotaskTicketingAlertConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_all_alert_configurations_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_all_alert_configurations_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_all_alert_configurations_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Get all Autotask ticketing alert configurations for a provider  # noqa: E501

        Get all Autotask ticketing alert configurations for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_all_alert_configurations_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: AutotaskTicketingAlertConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_all_alert_configurations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `autotask_retrieve_all_alert_configurations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/integrations/autotask/alerts/configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskTicketingAlertConfigurationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_companies(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Companies  # noqa: E501

        Retrieves a list of Autotask companies for the given Autotask id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_companies(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: AutotaskCompanyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_companies_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_companies_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_companies_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Companies  # noqa: E501

        Retrieves a list of Autotask companies for the given Autotask id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_companies_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: AutotaskCompanyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_companies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_companies`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/companies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskCompanyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_company_types(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Company Types  # noqa: E501

        Retrieves a list of user defined company types from Autotask for the given Autotask id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_company_types(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: AutotaskCompanyTypeResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_company_types_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_company_types_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_company_types_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Company Types  # noqa: E501

        Retrieves a list of user defined company types from Autotask for the given Autotask id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_company_types_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: AutotaskCompanyTypeResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_company_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_company_types`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/companytypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskCompanyTypeResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_contracts(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Contracts  # noqa: E501

        Retrieves a list of Autotask contracts for the given Autotask integration id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_contracts(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_contracts_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_contracts_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_contracts_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Contracts  # noqa: E501

        Retrieves a list of Autotask contracts for the given Autotask integration id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_contracts_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_contracts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/contracts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_contracts_fields(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Contract Fields  # noqa: E501

        Retrieves a list of Autotask contract fields for the given Autotask integration id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_contracts_fields(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_contracts_fields_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_contracts_fields_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_contracts_fields_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Contract Fields  # noqa: E501

        Retrieves a list of Autotask contract fields for the given Autotask integration id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_contracts_fields_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_contracts_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_contracts_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/contracts/fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_mappings(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask mappings  # noqa: E501

        Retrieves the list of mappings for this Autotask integration. You must be associated to the same provider as the Autotask integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_mappings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_mappings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask mappings  # noqa: E501

        Retrieves the list of mappings for this Autotask integration. You must be associated to the same provider as the Autotask integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_mappings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_mappings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_mappings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/mappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_services(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Contract Services  # noqa: E501

        Retrieves a list of Autotask contract services for the given Autotask integration id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_services(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_services_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_services_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_services_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Contract Services  # noqa: E501

        Retrieves a list of Autotask contract services for the given Autotask integration id. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_services_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_services" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_services`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/contracts/services', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_retrieve_settings(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Integration settings  # noqa: E501

        Retrieve the Autotask integration settings. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_settings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: AutotaskSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_retrieve_settings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_retrieve_settings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_retrieve_settings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve Autotask Integration settings  # noqa: E501

        Retrieve the Autotask integration settings. You must be associated to the same provider as the Autotask integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_retrieve_settings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: AutotaskSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_retrieve_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_retrieve_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/autotask/{UUID}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_update_alert_configuration(self, provider_id, alert_uuid, **kwargs):  # noqa: E501
        """Update an Autotask ticketing alert's configuration  # noqa: E501

        Update an Autotask ticketing alert's configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_update_alert_configuration(provider_id, alert_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str alert_uuid: (required)
        :param AutotaskTicketingAlertConfigurationRequest body:
        :return: AutotaskTicketingAlertConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_update_alert_configuration_with_http_info(provider_id, alert_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_update_alert_configuration_with_http_info(provider_id, alert_uuid, **kwargs)  # noqa: E501
            return data

    def autotask_update_alert_configuration_with_http_info(self, provider_id, alert_uuid, **kwargs):  # noqa: E501
        """Update an Autotask ticketing alert's configuration  # noqa: E501

        Update an Autotask ticketing alert's configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_update_alert_configuration_with_http_info(provider_id, alert_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str alert_uuid: (required)
        :param AutotaskTicketingAlertConfigurationRequest body:
        :return: AutotaskTicketingAlertConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'alert_uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_update_alert_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `autotask_update_alert_configuration`")  # noqa: E501
        # verify the required parameter 'alert_uuid' is set
        if ('alert_uuid' not in params or
                params['alert_uuid'] is None):
            raise ValueError("Missing the required parameter `alert_uuid` when calling `autotask_update_alert_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501
        if 'alert_uuid' in params:
            path_params['alert_UUID'] = params['alert_uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/providers/{provider_id}/integrations/autotask/alerts/{alert_UUID}/configuration', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskTicketingAlertConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def autotask_update_configuration(self, uuid, **kwargs):  # noqa: E501
        """Update Autotask Integration configuration  # noqa: E501

        Update the Autotask integration configuration. A 422 Unprocessable Entity response means the server failed to validate with Autotask.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_update_configuration(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param AutotaskIntegrationPatchReq body:
        :return: AutotaskIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.autotask_update_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.autotask_update_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def autotask_update_configuration_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Update Autotask Integration configuration  # noqa: E501

        Update the Autotask integration configuration. A 422 Unprocessable Entity response means the server failed to validate with Autotask.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.autotask_update_configuration_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param AutotaskIntegrationPatchReq body:
        :return: AutotaskIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method autotask_update_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `autotask_update_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/integrations/autotask/{UUID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AutotaskIntegration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_create_configuration(self, provider_id, **kwargs):  # noqa: E501
        """Creates a new ConnectWise integration for the provider  # noqa: E501

        Creates a new ConnectWise integration for the provider. You must be associated with the provider to use this route. A 422 Unprocessable Entity response means the server failed to validate with ConnectWise.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_create_configuration(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param ConnectwiseIntegrationReq body:
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_create_configuration_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_create_configuration_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def connectwise_create_configuration_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Creates a new ConnectWise integration for the provider  # noqa: E501

        Creates a new ConnectWise integration for the provider. You must be associated with the provider to use this route. A 422 Unprocessable Entity response means the server failed to validate with ConnectWise.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_create_configuration_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param ConnectwiseIntegrationReq body:
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_create_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `connectwise_create_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/providers/{provider_id}/integrations/connectwise', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse201',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_delete_configuration(self, uuid, **kwargs):  # noqa: E501
        """Delete ConnectWise Integration  # noqa: E501

        Removes a ConnectWise integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_delete_configuration(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_delete_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_delete_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_delete_configuration_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Delete ConnectWise Integration  # noqa: E501

        Removes a ConnectWise integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_delete_configuration_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_delete_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_delete_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}', 'DELETE',
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

    def connectwise_get_configuration(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Integration Configuration  # noqa: E501

        Retrieves configuration for given ConnectWise integration id. You must be associated to the provider the integration is tied to in order to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_get_configuration(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: ConnectwiseIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_get_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_get_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_get_configuration_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Integration Configuration  # noqa: E501

        Retrieves configuration for given ConnectWise integration id. You must be associated to the provider the integration is tied to in order to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_get_configuration_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: ConnectwiseIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_get_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_get_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectwiseIntegration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_patch_mappings(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete ConnectWise Mappings  # noqa: E501

        Create, edit, and/or delete mappings between Jumpcloud organizations and ConnectWise companies/agreements/additions. You must be associated to the same provider as the ConnectWise integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_patch_mappings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param ConnectWiseMappingRequest body:
        :return: ConnectWiseMappingRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_patch_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_patch_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_patch_mappings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete ConnectWise Mappings  # noqa: E501

        Create, edit, and/or delete mappings between Jumpcloud organizations and ConnectWise companies/agreements/additions. You must be associated to the same provider as the ConnectWise integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_patch_mappings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param ConnectWiseMappingRequest body:
        :return: ConnectWiseMappingRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_patch_mappings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_patch_mappings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/integrations/connectwise/{UUID}/mappings', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWiseMappingRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_patch_settings(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete ConnectWise Integration settings  # noqa: E501

        Create, edit, and/or delete ConnectWiseIntegration settings. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_patch_settings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param ConnectWiseSettingsPatchReq body:
        :return: ConnectWiseSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_patch_settings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_patch_settings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_patch_settings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Create, edit, and/or delete ConnectWise Integration settings  # noqa: E501

        Create, edit, and/or delete ConnectWiseIntegration settings. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_patch_settings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param ConnectWiseSettingsPatchReq body:
        :return: ConnectWiseSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_patch_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_patch_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/integrations/connectwise/{UUID}/settings', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWiseSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_additions(self, uuid, agreement_id, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Additions  # noqa: E501

        Retrieves a list of ConnectWise additions for the given ConnectWise id and Agreement id. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_additions(uuid, agreement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param str agreement_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_additions_with_http_info(uuid, agreement_id, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_additions_with_http_info(uuid, agreement_id, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_additions_with_http_info(self, uuid, agreement_id, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Additions  # noqa: E501

        Retrieves a list of ConnectWise additions for the given ConnectWise id and Agreement id. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_additions_with_http_info(uuid, agreement_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param str agreement_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'agreement_id', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_additions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_retrieve_additions`")  # noqa: E501
        # verify the required parameter 'agreement_id' is set
        if ('agreement_id' not in params or
                params['agreement_id'] is None):
            raise ValueError("Missing the required parameter `agreement_id` when calling `connectwise_retrieve_additions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501
        if 'agreement_id' in params:
            path_params['agreement_ID'] = params['agreement_id']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}/agreements/{agreement_ID}/additions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_agreements(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Agreements  # noqa: E501

        Retrieves a list of ConnectWise agreements for the given ConnectWise id. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_agreements(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_agreements_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_agreements_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_agreements_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Agreements  # noqa: E501

        Retrieves a list of ConnectWise agreements for the given ConnectWise id. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_agreements_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_agreements" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_retrieve_agreements`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}/agreements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_all_alert_configuration_options(self, provider_id, **kwargs):  # noqa: E501
        """Get all ConnectWise ticketing alert configuration options for a provider  # noqa: E501

        Get all ConnectWise ticketing alert configuration options for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_all_alert_configuration_options(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: ConnectWiseTicketingAlertConfigurationOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_all_alert_configuration_options_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_all_alert_configuration_options_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_all_alert_configuration_options_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Get all ConnectWise ticketing alert configuration options for a provider  # noqa: E501

        Get all ConnectWise ticketing alert configuration options for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_all_alert_configuration_options_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: ConnectWiseTicketingAlertConfigurationOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_all_alert_configuration_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `connectwise_retrieve_all_alert_configuration_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/integrations/connectwise/alerts/configuration/options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWiseTicketingAlertConfigurationOptions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_all_alert_configurations(self, provider_id, **kwargs):  # noqa: E501
        """Get all ConnectWise ticketing alert configurations for a provider  # noqa: E501

        Get all ConnectWise ticketing alert configurations for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_all_alert_configurations(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: ConnectWiseTicketingAlertConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_all_alert_configurations_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_all_alert_configurations_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_all_alert_configurations_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Get all ConnectWise ticketing alert configurations for a provider  # noqa: E501

        Get all ConnectWise ticketing alert configurations for a provider.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_all_alert_configurations_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: ConnectWiseTicketingAlertConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_all_alert_configurations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `connectwise_retrieve_all_alert_configurations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/integrations/connectwise/alerts/configuration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWiseTicketingAlertConfigurationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_companies(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Companies  # noqa: E501

        Retrieves a list of ConnectWise companies for the given ConnectWise id. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_companies(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: ConnectwiseCompanyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_companies_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_companies_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_companies_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Companies  # noqa: E501

        Retrieves a list of ConnectWise companies for the given ConnectWise id. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_companies_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: ConnectwiseCompanyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_companies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_retrieve_companies`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}/companies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectwiseCompanyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_company_types(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Company Types  # noqa: E501

        Retrieves a list of user defined company types from ConnectWise for the given ConnectWise id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_company_types(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: ConnectwiseCompanyTypeResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_company_types_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_company_types_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_company_types_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Company Types  # noqa: E501

        Retrieves a list of user defined company types from ConnectWise for the given ConnectWise id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_company_types_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: ConnectwiseCompanyTypeResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_company_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_retrieve_company_types`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}/companytypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectwiseCompanyTypeResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_mappings(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise mappings  # noqa: E501

        Retrieves the list of mappings for this ConnectWise integration. You must be associated to the same provider as the ConnectWise integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_mappings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_mappings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_mappings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise mappings  # noqa: E501

        Retrieves the list of mappings for this ConnectWise integration. You must be associated to the same provider as the ConnectWise integration to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_mappings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_mappings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_retrieve_mappings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}/mappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_retrieve_settings(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Integration settings  # noqa: E501

        Retrieve the ConnectWise integration settings. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_settings(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: ConnectWiseSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_retrieve_settings_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_retrieve_settings_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_retrieve_settings_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Retrieve ConnectWise Integration settings  # noqa: E501

        Retrieve the ConnectWise integration settings. You must be associated to the same provider as the ConnectWise integration to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_retrieve_settings_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :return: ConnectWiseSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_retrieve_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_retrieve_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/connectwise/{UUID}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWiseSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_update_alert_configuration(self, provider_id, alert_uuid, **kwargs):  # noqa: E501
        """Update a ConnectWise ticketing alert's configuration  # noqa: E501

        Update a ConnectWise ticketing alert's configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_update_alert_configuration(provider_id, alert_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str alert_uuid: (required)
        :param ConnectWiseTicketingAlertConfigurationRequest body:
        :return: ConnectWiseTicketingAlertConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_update_alert_configuration_with_http_info(provider_id, alert_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_update_alert_configuration_with_http_info(provider_id, alert_uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_update_alert_configuration_with_http_info(self, provider_id, alert_uuid, **kwargs):  # noqa: E501
        """Update a ConnectWise ticketing alert's configuration  # noqa: E501

        Update a ConnectWise ticketing alert's configuration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_update_alert_configuration_with_http_info(provider_id, alert_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str alert_uuid: (required)
        :param ConnectWiseTicketingAlertConfigurationRequest body:
        :return: ConnectWiseTicketingAlertConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'alert_uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_update_alert_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `connectwise_update_alert_configuration`")  # noqa: E501
        # verify the required parameter 'alert_uuid' is set
        if ('alert_uuid' not in params or
                params['alert_uuid'] is None):
            raise ValueError("Missing the required parameter `alert_uuid` when calling `connectwise_update_alert_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501
        if 'alert_uuid' in params:
            path_params['alert_UUID'] = params['alert_uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/providers/{provider_id}/integrations/connectwise/alerts/{alert_UUID}/configuration', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectWiseTicketingAlertConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def connectwise_update_configuration(self, uuid, **kwargs):  # noqa: E501
        """Update ConnectWise Integration configuration  # noqa: E501

        Update the ConnectWise integration configuration. A 422 Unprocessable Entity response means the server failed to validate with ConnectWise.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_update_configuration(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param ConnectwiseIntegrationPatchReq body:
        :return: ConnectwiseIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.connectwise_update_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.connectwise_update_configuration_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def connectwise_update_configuration_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Update ConnectWise Integration configuration  # noqa: E501

        Update the ConnectWise integration configuration. A 422 Unprocessable Entity response means the server failed to validate with ConnectWise.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connectwise_update_configuration_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param ConnectwiseIntegrationPatchReq body:
        :return: ConnectwiseIntegration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connectwise_update_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `connectwise_update_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/integrations/connectwise/{UUID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConnectwiseIntegration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mtp_integration_retrieve_alerts(self, provider_id, **kwargs):  # noqa: E501
        """Get all ticketing alerts available for a provider's ticketing integration.  # noqa: E501

        Get all ticketing alerts available for a provider's ticketing integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mtp_integration_retrieve_alerts(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: TicketingIntegrationAlertsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mtp_integration_retrieve_alerts_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.mtp_integration_retrieve_alerts_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def mtp_integration_retrieve_alerts_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Get all ticketing alerts available for a provider's ticketing integration.  # noqa: E501

        Get all ticketing alerts available for a provider's ticketing integration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mtp_integration_retrieve_alerts_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :return: TicketingIntegrationAlertsResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mtp_integration_retrieve_alerts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `mtp_integration_retrieve_alerts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/integrations/ticketing/alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TicketingIntegrationAlertsResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mtp_integration_retrieve_sync_errors(self, uuid, integration_type, **kwargs):  # noqa: E501
        """Retrieve Recent Integration Sync Errors  # noqa: E501

        Retrieves recent sync errors for given integration type and integration id. You must be associated to the provider the integration is tied to in order to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mtp_integration_retrieve_sync_errors(uuid, integration_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param str integration_type: (required)
        :return: IntegrationSyncErrorResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mtp_integration_retrieve_sync_errors_with_http_info(uuid, integration_type, **kwargs)  # noqa: E501
        else:
            (data) = self.mtp_integration_retrieve_sync_errors_with_http_info(uuid, integration_type, **kwargs)  # noqa: E501
            return data

    def mtp_integration_retrieve_sync_errors_with_http_info(self, uuid, integration_type, **kwargs):  # noqa: E501
        """Retrieve Recent Integration Sync Errors  # noqa: E501

        Retrieves recent sync errors for given integration type and integration id. You must be associated to the provider the integration is tied to in order to use this api.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mtp_integration_retrieve_sync_errors_with_http_info(uuid, integration_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param str integration_type: (required)
        :return: IntegrationSyncErrorResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'integration_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mtp_integration_retrieve_sync_errors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `mtp_integration_retrieve_sync_errors`")  # noqa: E501
        # verify the required parameter 'integration_type' is set
        if ('integration_type' not in params or
                params['integration_type'] is None):
            raise ValueError("Missing the required parameter `integration_type` when calling `mtp_integration_retrieve_sync_errors`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['UUID'] = params['uuid']  # noqa: E501
        if 'integration_type' in params:
            path_params['integration_type'] = params['integration_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/integrations/{integration_type}/{UUID}/errors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationSyncErrorResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def provider_organizations_update_org(self, provider_id, id, **kwargs):  # noqa: E501
        """Update Provider Organization  # noqa: E501

        This endpoint updates a provider's organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.provider_organizations_update_org(provider_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str id: (required)
        :param Organization body:
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.provider_organizations_update_org_with_http_info(provider_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.provider_organizations_update_org_with_http_info(provider_id, id, **kwargs)  # noqa: E501
            return data

    def provider_organizations_update_org_with_http_info(self, provider_id, id, **kwargs):  # noqa: E501
        """Update Provider Organization  # noqa: E501

        This endpoint updates a provider's organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.provider_organizations_update_org_with_http_info(provider_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str id: (required)
        :param Organization body:
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method provider_organizations_update_org" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `provider_organizations_update_org`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `provider_organizations_update_org`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/providers/{provider_id}/organizations/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_get_provider(self, provider_id, **kwargs):  # noqa: E501
        """Retrieve Provider  # noqa: E501

        This endpoint returns details about a provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_get_provider(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :return: Provider
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_get_provider_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_get_provider_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def providers_get_provider_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Retrieve Provider  # noqa: E501

        This endpoint returns details about a provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_get_provider_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :return: Provider
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_get_provider" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_get_provider`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Provider',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_list_administrators(self, provider_id, **kwargs):  # noqa: E501
        """List Provider Administrators  # noqa: E501

        This endpoint returns a list of the Administrators associated with the Provider. You must be associated with the provider to use this route.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_list_administrators(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_list_administrators_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_list_administrators_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def providers_list_administrators_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """List Provider Administrators  # noqa: E501

        This endpoint returns a list of the Administrators associated with the Provider. You must be associated with the provider to use this route.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_list_administrators_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_list_administrators" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_list_administrators`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/administrators', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_list_organizations(self, provider_id, **kwargs):  # noqa: E501
        """List Provider Organizations  # noqa: E501

        This endpoint returns a list of the Organizations associated with the Provider. You must be associated with the provider to use this route.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_list_organizations(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_list_organizations_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_list_organizations_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def providers_list_organizations_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """List Provider Organizations  # noqa: E501

        This endpoint returns a list of the Organizations associated with the Provider. You must be associated with the provider to use this route.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_list_organizations_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted, the default list of fields will be returned. 
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'fields', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_list_organizations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_list_organizations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/organizations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_post_admins(self, provider_id, **kwargs):  # noqa: E501
        """Create a new Provider Administrator  # noqa: E501

        This endpoint allows you to create a provider administrator. You must be associated with the provider to use this route. You must provide either `role` or `roleName`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_post_admins(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param ProviderAdminReq body:
        :return: Administrator
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_post_admins_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_post_admins_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def providers_post_admins_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Create a new Provider Administrator  # noqa: E501

        This endpoint allows you to create a provider administrator. You must be associated with the provider to use this route. You must provide either `role` or `roleName`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_post_admins_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param ProviderAdminReq body:
        :return: Administrator
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_post_admins" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_post_admins`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/providers/{provider_id}/administrators', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Administrator',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_remove_administrator(self, provider_id, id, **kwargs):  # noqa: E501
        """Delete Provider Administrator  # noqa: E501

        This endpoint removes an Administrator associated with the Provider. You must be associated with the provider to use this route.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_remove_administrator(provider_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_remove_administrator_with_http_info(provider_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_remove_administrator_with_http_info(provider_id, id, **kwargs)  # noqa: E501
            return data

    def providers_remove_administrator_with_http_info(self, provider_id, id, **kwargs):  # noqa: E501
        """Delete Provider Administrator  # noqa: E501

        This endpoint removes an Administrator associated with the Provider. You must be associated with the provider to use this route.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_remove_administrator_with_http_info(provider_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_remove_administrator" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_remove_administrator`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `providers_remove_administrator`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/administrators/{id}', 'DELETE',
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

    def providers_retrieve_integrations(self, provider_id, **kwargs):  # noqa: E501
        """Retrieve Integrations for Provider  # noqa: E501

        Retrieves a list of integrations this provider has configured. You must be associated to the provider to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_retrieve_integrations(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: IntegrationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_retrieve_integrations_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_retrieve_integrations_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def providers_retrieve_integrations_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """Retrieve Integrations for Provider  # noqa: E501

        Retrieves a list of integrations this provider has configured. You must be associated to the provider to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_retrieve_integrations_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param list[str] filter: A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group`
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: IntegrationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'filter', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_retrieve_integrations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_retrieve_integrations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/integrations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IntegrationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_retrieve_invoice(self, provider_id, id, **kwargs):  # noqa: E501
        """Download a provider's invoice.  # noqa: E501

        Retrieves an invoice for this provider. You must be associated to the provider to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_retrieve_invoice(provider_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_retrieve_invoice_with_http_info(provider_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_retrieve_invoice_with_http_info(provider_id, id, **kwargs)  # noqa: E501
            return data

    def providers_retrieve_invoice_with_http_info(self, provider_id, id, **kwargs):  # noqa: E501
        """Download a provider's invoice.  # noqa: E501

        Retrieves an invoice for this provider. You must be associated to the provider to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_retrieve_invoice_with_http_info(provider_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param str id: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_retrieve_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_retrieve_invoice`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `providers_retrieve_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501
        if 'id' in params:
            path_params['ID'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/invoices/{ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def providers_retrieve_invoices(self, provider_id, **kwargs):  # noqa: E501
        """List a provider's invoices.  # noqa: E501

        Retrieves a list of invoices for this provider. You must be associated to the provider to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_retrieve_invoices(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param int limit: The number of records to return at once. Limited to 100.
        :return: ProviderInvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.providers_retrieve_invoices_with_http_info(provider_id, **kwargs)  # noqa: E501
        else:
            (data) = self.providers_retrieve_invoices_with_http_info(provider_id, **kwargs)  # noqa: E501
            return data

    def providers_retrieve_invoices_with_http_info(self, provider_id, **kwargs):  # noqa: E501
        """List a provider's invoices.  # noqa: E501

        Retrieves a list of invoices for this provider. You must be associated to the provider to use this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.providers_retrieve_invoices_with_http_info(provider_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_id: (required)
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :param int limit: The number of records to return at once. Limited to 100.
        :return: ProviderInvoiceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_id', 'skip', 'sort', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method providers_retrieve_invoices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_id' is set
        if ('provider_id' not in params or
                params['provider_id'] is None):
            raise ValueError("Missing the required parameter `provider_id` when calling `providers_retrieve_invoices`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'provider_id' in params:
            path_params['provider_id'] = params['provider_id']  # noqa: E501

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
            collection_formats['sort'] = 'csv'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/providers/{provider_id}/invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProviderInvoiceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
