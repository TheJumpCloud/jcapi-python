# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jcapiv1.api_client import ApiClient


class CommandsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def command_file_get(self, id, content_type, accept, **kwargs):  # noqa: E501
        """Get a Command File  # noqa: E501

        This endpoint returns the uploaded file(s) associated with a specific command.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/files/command/{commandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.command_file_get(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: Commandfilereturn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.command_file_get_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.command_file_get_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
            return data

    def command_file_get_with_http_info(self, id, content_type, accept, **kwargs):  # noqa: E501
        """Get a Command File  # noqa: E501

        This endpoint returns the uploaded file(s) associated with a specific command.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/files/command/{commandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.command_file_get_with_http_info(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: Commandfilereturn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept', 'fields', 'limit', 'skip', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method command_file_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `command_file_get`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `command_file_get`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `command_file_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/files/command/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Commandfilereturn',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def commands_delete(self, id, content_type, accept, **kwargs):  # noqa: E501
        """Delete a Command  # noqa: E501

        This endpoint deletes a specific command based on the Command ID.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_delete(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str x_org_id: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commands_delete_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.commands_delete_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
            return data

    def commands_delete_with_http_info(self, id, content_type, accept, **kwargs):  # noqa: E501
        """Delete a Command  # noqa: E501

        This endpoint deletes a specific command based on the Command ID.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_delete_with_http_info(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str x_org_id: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commands_delete`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_delete`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/commands/{id}', 'DELETE',
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

    def commands_get(self, id, content_type, accept, **kwargs):  # noqa: E501
        """List an individual Command  # noqa: E501

        This endpoint returns a specific command based on the command ID.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_get(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param str filter: A filter to apply to the query.
        :param str x_org_id: 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commands_get_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.commands_get_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
            return data

    def commands_get_with_http_info(self, id, content_type, accept, **kwargs):  # noqa: E501
        """List an individual Command  # noqa: E501

        This endpoint returns a specific command based on the command ID.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_get_with_http_info(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param str filter: A filter to apply to the query.
        :param str x_org_id: 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept', 'fields', 'filter', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commands_get`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_get`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/commands/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Command',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def commands_list(self, content_type, accept, **kwargs):  # noqa: E501
        """List All Commands  # noqa: E501

        This endpoint returns all commands.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_list(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param int skip: The offset into the records to return.
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :param str filter: A filter to apply to the query.
        :param str x_org_id: 
        :return: Commandslist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commands_list_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.commands_list_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def commands_list_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """List All Commands  # noqa: E501

        This endpoint returns all commands.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_list_with_http_info(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param int skip: The offset into the records to return.
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :param str filter: A filter to apply to the query.
        :param str x_org_id: 
        :return: Commandslist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'skip', 'fields', 'limit', 'sort', 'filter', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_list`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/commands/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Commandslist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def commands_post(self, content_type, accept, **kwargs):  # noqa: E501
        """Create A Command  # noqa: E501

        This endpoint allows you to create a new command.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/commands/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"name\":\"Test API Command\",  \"command\":\"String\",  \"user\":\"{UserID}\",  \"schedule\":\"\",  \"timeout\":\"100\" }'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_post(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :param str x_org_id: 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commands_post_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.commands_post_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def commands_post_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """Create A Command  # noqa: E501

        This endpoint allows you to create a new command.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/commands/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"name\":\"Test API Command\",  \"command\":\"String\",  \"user\":\"{UserID}\",  \"schedule\":\"\",  \"timeout\":\"100\" }'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_post_with_http_info(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :param str x_org_id: 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_post`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
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
            '/commands/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Command',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def commands_put(self, id, content_type, accept, **kwargs):  # noqa: E501
        """Update a Command  # noqa: E501

        This endpoint Updates a command based on the command ID and returns the modified command record.  #### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"name\":\"Test API Command\",  \"command\":\"String\",  \"user\":\"{UserID}\",  \"schedule\":\"\",  \"timeout\":\"100\" }'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_put(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :param str x_org_id: 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.commands_put_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.commands_put_with_http_info(id, content_type, accept, **kwargs)  # noqa: E501
            return data

    def commands_put_with_http_info(self, id, content_type, accept, **kwargs):  # noqa: E501
        """Update a Command  # noqa: E501

        This endpoint Updates a command based on the command ID and returns the modified command record.  #### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"name\":\"Test API Command\",  \"command\":\"String\",  \"user\":\"{UserID}\",  \"schedule\":\"\",  \"timeout\":\"100\" }'  ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.commands_put_with_http_info(id, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :param str x_org_id: 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commands_put`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_put`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
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
            '/commands/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Command',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
