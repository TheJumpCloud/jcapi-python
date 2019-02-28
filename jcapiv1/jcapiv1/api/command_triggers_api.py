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


class CommandTriggersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def command_trigger_webhook_post(self, triggername, content_type, accept, **kwargs):  # noqa: E501
        """Launch a command via a Trigger  # noqa: E501

        This endpoint allows you to launch a command based on a defined trigger.  #### Sample Requests  **Launch a Command via a Trigger**  ``` curl --silent \\      -X 'POST' \\      -H \"x-api-key: {API_KEY}\" \\      \"https://console.jumpcloud.com/api/command/trigger/{TriggerName}\" ``` **Launch a Command via a Trigger passing a JSON object to the command** ``` curl --silent \\      -X 'POST' \\      -H \"x-api-key: {API_KEY}\" \\      -H 'Accept: application/json' \\      -H 'Content-Type: application/json' \\      -d '{ \"srcip\":\"192.168.2.32\", \"attack\":\"Cross Site Scripting Attempt\" }' \\      \"https://console.jumpcloud.com/api/command/trigger/{TriggerName}\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.command_trigger_webhook_post(triggername, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str triggername: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str x_org_id: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.command_trigger_webhook_post_with_http_info(triggername, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.command_trigger_webhook_post_with_http_info(triggername, content_type, accept, **kwargs)  # noqa: E501
            return data

    def command_trigger_webhook_post_with_http_info(self, triggername, content_type, accept, **kwargs):  # noqa: E501
        """Launch a command via a Trigger  # noqa: E501

        This endpoint allows you to launch a command based on a defined trigger.  #### Sample Requests  **Launch a Command via a Trigger**  ``` curl --silent \\      -X 'POST' \\      -H \"x-api-key: {API_KEY}\" \\      \"https://console.jumpcloud.com/api/command/trigger/{TriggerName}\" ``` **Launch a Command via a Trigger passing a JSON object to the command** ``` curl --silent \\      -X 'POST' \\      -H \"x-api-key: {API_KEY}\" \\      -H 'Accept: application/json' \\      -H 'Content-Type: application/json' \\      -d '{ \"srcip\":\"192.168.2.32\", \"attack\":\"Cross Site Scripting Attempt\" }' \\      \"https://console.jumpcloud.com/api/command/trigger/{TriggerName}\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.command_trigger_webhook_post_with_http_info(triggername, content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str triggername: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str x_org_id: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['triggername', 'content_type', 'accept', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method command_trigger_webhook_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'triggername' is set
        if ('triggername' not in params or
                params['triggername'] is None):
            raise ValueError("Missing the required parameter `triggername` when calling `command_trigger_webhook_post`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `command_trigger_webhook_post`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `command_trigger_webhook_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'triggername' in params:
            path_params['triggername'] = params['triggername']  # noqa: E501

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
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/command/trigger/{triggername}', 'POST',
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
