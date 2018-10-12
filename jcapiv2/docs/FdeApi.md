# jcapiv2.FdeApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_get_fde_key**](FdeApi.md#systems_get_fde_key) | **GET** /systems/{system_id}/fdekey | Get System FDE Key


# **systems_get_fde_key**
> Systemfdekey systems_get_fde_key(system_id, x_org_id=x_org_id)

Get System FDE Key

This endpoint will return the current (latest) fde key saved for a system.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.FdeApi(jcapiv2.ApiClient(configuration))
system_id = 'system_id_example' # str | 
x_org_id = '' # str |  (optional) (default to )

try:
    # Get System FDE Key
    api_response = api_instance.systems_get_fde_key(system_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FdeApi->systems_get_fde_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**Systemfdekey**](Systemfdekey.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

