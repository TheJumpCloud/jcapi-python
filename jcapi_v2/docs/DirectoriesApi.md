# jcapiv2.DirectoriesApi

All URIs are relative to *http://localhost:3004/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](DirectoriesApi.md#list) | **GET** /directories | List All Directories, which consist of G Suites, LDAP Servers and Office 365s. 


# **list**
> list[Directory] list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List All Directories, which consist of G Suites, LDAP Servers and Office 365s. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.DirectoriesApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List All Directories, which consist of G Suites, LDAP Servers and Office 365s. 
    api_response = api_instance.list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoriesApi->list: %s\n" % e)
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

[**list[Directory]**](Directory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

