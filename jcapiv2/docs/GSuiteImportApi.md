# jcapiv2.GSuiteImportApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gsuites_list_import_jumpcloud_users**](GSuiteImportApi.md#gsuites_list_import_jumpcloud_users) | **GET** /gsuites/{gsuite_id}/import/jumpcloudusers | Get a list of users in Jumpcloud format to import from a Google Workspace account.
[**gsuites_list_import_users**](GSuiteImportApi.md#gsuites_list_import_users) | **GET** /gsuites/{gsuite_id}/import/users | Get a list of users to import from a G Suite instance

# **gsuites_list_import_jumpcloud_users**
> InlineResponse2001 gsuites_list_import_jumpcloud_users(gsuite_id, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)

Get a list of users in Jumpcloud format to import from a Google Workspace account.

Lists available G Suite users for import, translated to the Jumpcloud user schema.

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
api_instance = jcapiv2.GSuiteImportApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
max_results = 56 # int | Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
order_by = 'order_by_example' # str | Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
page_token = 'page_token_example' # str | Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
query = 'query_example' # str | Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. (optional)
sort_order = 'sort_order_example' # str | Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)

try:
    # Get a list of users in Jumpcloud format to import from a Google Workspace account.
    api_response = api_instance.gsuites_list_import_jumpcloud_users(gsuite_id, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteImportApi->gsuites_list_import_jumpcloud_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **max_results** | **int**| Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **order_by** | **str**| Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **page_token** | **str**| Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **query** | **str**| Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. | [optional] 
 **sort_order** | **str**| Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gsuites_list_import_users**
> InlineResponse2002 gsuites_list_import_users(gsuite_id, limit=limit, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)

Get a list of users to import from a G Suite instance

Lists G Suite users available for import.

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
api_instance = jcapiv2.GSuiteImportApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
max_results = 56 # int | Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
order_by = 'order_by_example' # str | Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
page_token = 'page_token_example' # str | Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
query = 'query_example' # str | Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. (optional)
sort_order = 'sort_order_example' # str | Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)

try:
    # Get a list of users to import from a G Suite instance
    api_response = api_instance.gsuites_list_import_users(gsuite_id, limit=limit, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteImportApi->gsuites_list_import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **max_results** | **int**| Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **order_by** | **str**| Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **page_token** | **str**| Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **query** | **str**| Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. | [optional] 
 **sort_order** | **str**| Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

