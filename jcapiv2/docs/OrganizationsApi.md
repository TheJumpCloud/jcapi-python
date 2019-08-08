# jcapiv2.OrganizationsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**org_crypto_get**](OrganizationsApi.md#org_crypto_get) | **GET** /organizations/{id}/crypto | Get Crypto Settings
[**org_crypto_put**](OrganizationsApi.md#org_crypto_put) | **PUT** /organizations/{id}/crypto | Edit Crypto Settings


# **org_crypto_get**
> OrgCryptoSettings org_crypto_get(id, content_type, accept, fields=fields, filter=filter, x_org_id=x_org_id, skip=skip, sort=sort, limit=limit)

Get Crypto Settings

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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = ['[]'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional) (default to [])
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)

try:
    # Get Crypto Settings
    api_response = api_instance.org_crypto_get(id, content_type, accept, fields=fields, filter=filter, x_org_id=x_org_id, skip=skip, sort=sort, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->org_crypto_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] [default to []]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]

### Return type

[**OrgCryptoSettings**](OrgCryptoSettings.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_crypto_put**
> object org_crypto_put(id, content_type, accept, body=body, fields=fields, filter=filter, x_org_id=x_org_id, skip=skip, sort=sort, limit=limit)

Edit Crypto Settings

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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.OrgCryptoSettings() # OrgCryptoSettings |  (optional)
fields = ['[]'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional) (default to [])
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)

try:
    # Edit Crypto Settings
    api_response = api_instance.org_crypto_put(id, content_type, accept, body=body, fields=fields, filter=filter, x_org_id=x_org_id, skip=skip, sort=sort, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->org_crypto_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**OrgCryptoSettings**](OrgCryptoSettings.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] [default to []]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]

### Return type

**object**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

