# jcapiv2.LogosApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logos_get**](LogosApi.md#logos_get) | **GET** /logos/{id} | Get the logo associated with the specified id

# **logos_get**
> str logos_get(id)

Get the logo associated with the specified id

Return the logo image associated with the specified id

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.LogosApi()
id = 'id_example' # str | 

try:
    # Get the logo associated with the specified id
    api_response = api_instance.logos_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogosApi->logos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif, image/jpeg, image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

