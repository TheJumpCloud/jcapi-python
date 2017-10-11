# jcapiv1.ApplicationsApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_list**](ApplicationsApi.md#applications_list) | **GET** /applications | Applications


# **applications_list**
> Applicationslist applications_list(content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort)

Applications

The endpoint is used to return all your SSO Applications.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.ApplicationsApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = 'fields_example' # str | The comma separated fileds included in the returned records. If omitted the default list of fields will be returned. (optional)
limit = 56 # int | The number of records to return at once. (optional)
skip = 56 # int | The offset into the records to return. (optional)
sort = 'The comma separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending.' # str |  (optional) (default to The comma separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending.)

try: 
    # Applications
    api_response = api_instance.applications_list(content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| The comma separated fileds included in the returned records. If omitted the default list of fields will be returned. | [optional] 
 **limit** | **int**| The number of records to return at once. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] 
 **sort** | **str**|  | [optional] [default to The comma separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending.]

### Return type

[**Applicationslist**](Applicationslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

