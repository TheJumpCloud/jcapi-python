# jcapiv2.GroupsApi

All URIs are relative to *http://localhost:3004/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](GroupsApi.md#list) | **GET** /groups | List All Groups


# **list**
> list[Group] list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List All Groups

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GroupsApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List All Groups
    api_response = api_instance.list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

