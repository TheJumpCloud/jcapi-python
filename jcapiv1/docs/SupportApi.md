# jcapiv1.SupportApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**case_post**](SupportApi.md#case_post) | **POST** /api/cases | Create a Case


# **case_post**
> InlineResponse200 case_post(content_type, accept, body=body)

Create a Case

This endpoint allows you to open a support case.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/cases \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"subject\":\"{subject}\",  \"description\":\"{description}\",  \"firstname\":\"{firstname}\",  \"lastname\":\"{lastname}\" }' ```

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
api_instance = jcapiv1.SupportApi(jcapiv1.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Case() # Case |  (optional)

try:
    # Create a Case
    api_response = api_instance.case_post(content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportApi->case_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Case**](Case.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

