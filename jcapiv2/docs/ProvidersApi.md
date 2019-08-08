# jcapiv2.ProvidersApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_list_administrators**](ProvidersApi.md#providers_list_administrators) | **GET** /providers/{provider_id}/administrators | List Provider Administrators
[**providers_post_admins**](ProvidersApi.md#providers_post_admins) | **POST** /providers/{provider_id}/administrators | Create a new Provider Administrator


# **providers_list_administrators**
> InlineResponse2001 providers_list_administrators(provider_id, content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List Provider Administrators

This endpoint returns a list of the Administrators associated with the Provider.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/providers/{ProviderID}/administrators \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.ProvidersApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = ['[]'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional) (default to [])
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])

try:
    # List Provider Administrators
    api_response = api_instance.providers_list_administrators(provider_id, content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_list_administrators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] [default to []]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_post_admins**
> Administrator providers_post_admins(provider_id, content_type, accept, body=body)

Create a new Provider Administrator

This endpoint allows you to create a provider administrator. You must be associated to the provider to use this route.  **Sample Request**  ``` curl -X POST https://console.jumpcloud.com/api/v2/providers/{ProviderID}/administrators \\     -H 'Accept: application/json' \\     -H 'Context-Type: application/json' \\     -H 'x-api-key: {API_KEY}' \\     -d '{       \"email\":\"{ADMIN_EMAIL}\"     }' ```

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
api_instance = jcapiv2.ProvidersApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.ProviderAdminReq() # ProviderAdminReq |  (optional)

try:
    # Create a new Provider Administrator
    api_response = api_instance.providers_post_admins(provider_id, content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_post_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**ProviderAdminReq**](ProviderAdminReq.md)|  | [optional] 

### Return type

[**Administrator**](Administrator.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

