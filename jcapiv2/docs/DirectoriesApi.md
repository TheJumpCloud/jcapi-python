# jcapiv2.DirectoriesApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directories_list**](DirectoriesApi.md#directories_list) | **GET** /directories | List All Directories

# **directories_list**
> list[Directory] directories_list(fields=fields, limit=limit, sort=sort, skip=skip, x_org_id=x_org_id)

List All Directories

This endpoint returns all active directories (LDAP, O365 Suite, G-Suite).  #### Sample Request ```  curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.DirectoriesApi(jcapiv2.ApiClient(configuration))
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List All Directories
    api_response = api_instance.directories_list(fields=fields, limit=limit, sort=sort, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->directories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[Directory]**](Directory.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

