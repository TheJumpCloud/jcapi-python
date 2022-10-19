# jcapiv2.Office365ImportApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**office365s_list_import_users**](Office365ImportApi.md#office365s_list_import_users) | **GET** /office365s/{office365_id}/import/users | Get a list of users to import from an Office 365 instance

# **office365s_list_import_users**
> InlineResponse20011 office365s_list_import_users(office365_id, consistency_level=consistency_level, top=top, skip_token=skip_token, filter=filter, search=search, orderby=orderby, count=count)

Get a list of users to import from an Office 365 instance

Lists Office 365 users available for import.

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
api_instance = jcapiv2.Office365ImportApi(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | 
consistency_level = 'consistency_level_example' # str | Defines the consistency header for O365 requests. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#request-headers (optional)
top = 56 # int | Office 365 API maximum number of results per page. See https://docs.microsoft.com/en-us/graph/paging. (optional)
skip_token = 'skip_token_example' # str | Office 365 API token used to access the next page of results. See https://docs.microsoft.com/en-us/graph/paging. (optional)
filter = 'filter_example' # str | Office 365 API filter parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)
search = 'search_example' # str | Office 365 API search parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)
orderby = 'orderby_example' # str | Office 365 API orderby parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)
count = true # bool | Office 365 API count parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)

try:
    # Get a list of users to import from an Office 365 instance
    api_response = api_instance.office365s_list_import_users(office365_id, consistency_level=consistency_level, top=top, skip_token=skip_token, filter=filter, search=search, orderby=orderby, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365ImportApi->office365s_list_import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**|  | 
 **consistency_level** | **str**| Defines the consistency header for O365 requests. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#request-headers | [optional] 
 **top** | **int**| Office 365 API maximum number of results per page. See https://docs.microsoft.com/en-us/graph/paging. | [optional] 
 **skip_token** | **str**| Office 365 API token used to access the next page of results. See https://docs.microsoft.com/en-us/graph/paging. | [optional] 
 **filter** | **str**| Office 365 API filter parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 
 **search** | **str**| Office 365 API search parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 
 **orderby** | **str**| Office 365 API orderby parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 
 **count** | **bool**| Office 365 API count parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

