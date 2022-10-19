# jcapiv2.SCIMImportApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_users**](SCIMImportApi.md#import_users) | **GET** /applications/{application_id}/import/users | Get a list of users to import from an Application IdM service provider

# **import_users**
> ImportUsersResponse import_users(application_id, filter=filter, query=query, sort=sort, sort_order=sort_order, x_org_id=x_org_id, limit=limit, skip=skip)

Get a list of users to import from an Application IdM service provider

Get a list of users to import from an Application IdM service provider.

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
api_instance = jcapiv2.SCIMImportApi(jcapiv2.ApiClient(configuration))
application_id = 'application_id_example' # str | ObjectID of the Application.
filter = 'filter_example' # str | Filter users by a search term (optional)
query = 'query_example' # str | URL query to merge with the service provider request (optional)
sort = 'sort_example' # str | Sort users by supported fields (optional)
sort_order = 'asc' # str |  (optional) (default to asc)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # Get a list of users to import from an Application IdM service provider
    api_response = api_instance.import_users(application_id, filter=filter, query=query, sort=sort, sort_order=sort_order, x_org_id=x_org_id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMImportApi->import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| ObjectID of the Application. | 
 **filter** | **str**| Filter users by a search term | [optional] 
 **query** | **str**| URL query to merge with the service provider request | [optional] 
 **sort** | **str**| Sort users by supported fields | [optional] 
 **sort_order** | **str**|  | [optional] [default to asc]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**ImportUsersResponse**](ImportUsersResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

