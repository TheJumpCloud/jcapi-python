# jcapiv1.CommandTriggersApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command_trigger_webhook_post**](CommandTriggersApi.md#command_trigger_webhook_post) | **POST** /command/trigger/{triggername} | Launch a command via a Trigger


# **command_trigger_webhook_post**
> command_trigger_webhook_post(triggername, content_type, accept, x_org_id=x_org_id)

Launch a command via a Trigger

This endpoint allows you to launch a command based on a defined trigger.  #### Sample Requests  **Launch a Command via a Trigger**  ``` curl --silent \\      -X 'POST' \\      -H \"x-api-key: {API_KEY}\" \\      \"https://console.jumpcloud.com/api/command/trigger/{TriggerName}\" ``` **Launch a Command via a Trigger passing a JSON object to the command** ``` curl --silent \\      -X 'POST' \\      -H \"x-api-key: {API_KEY}\" \\      -H 'Accept: application/json' \\      -H 'Content-Type: application/json' \\      -d '{ \"srcip\":\"192.168.2.32\", \"attack\":\"Cross Site Scripting Attempt\" }' \\      \"https://console.jumpcloud.com/api/command/trigger/{TriggerName}\" ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.CommandTriggersApi(jcapiv1.ApiClient(configuration))
triggername = 'triggername_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Launch a command via a Trigger
    api_instance.command_trigger_webhook_post(triggername, content_type, accept, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling CommandTriggersApi->command_trigger_webhook_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **triggername** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

