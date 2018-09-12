# jcapiv2.FdeApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_get_fde_key**](FdeApi.md#systems_get_fde_key) | **GET** /systems/{system_id}/fdekey | Get System FDE Key


# **systems_get_fde_key**
> InlineResponse200 systems_get_fde_key(system_id)

Get System FDE Key

Public is OFF on purpose, this is not intended to be published  Retrieve the current (latest) fde key saved for this system.

### Example 
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.FdeApi()
system_id = 'system_id_example' # str | 

try: 
    # Get System FDE Key
    api_response = api_instance.systems_get_fde_key(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FdeApi->systems_get_fde_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

