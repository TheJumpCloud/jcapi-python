# jcapi.DefaultApi

All URIs are relative to *http://localhost:3004/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systemusers_get**](DefaultApi.md#systemusers_get) | **GET** /systemusers | Get JumpCloud systemusers.


# **systemusers_get**
> InlineResponse200 systemusers_get(x_api_key=x_api_key, limit=limit)

Get JumpCloud systemusers.

### Example 
```python
from __future__ import print_statement
import time
import jcapi
from jcapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapi.DefaultApi()
x_api_key = 'x_api_key_example' # str |  (optional)
limit = 56 # int |  (optional)

try: 
    # Get JumpCloud systemusers.
    api_response = api_instance.systemusers_get(x_api_key=x_api_key, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

