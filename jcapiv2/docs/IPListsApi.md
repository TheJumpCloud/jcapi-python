# jcapiv2.IPListsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iplists_delete**](IPListsApi.md#iplists_delete) | **DELETE** /iplists/{id} | Delete an IP list
[**iplists_get**](IPListsApi.md#iplists_get) | **GET** /iplists/{id} | Get an IP list
[**iplists_list**](IPListsApi.md#iplists_list) | **GET** /iplists | List IP Lists
[**iplists_patch**](IPListsApi.md#iplists_patch) | **PATCH** /iplists/{id} | Update an IP list
[**iplists_post**](IPListsApi.md#iplists_post) | **POST** /iplists | Create IP List
[**iplists_put**](IPListsApi.md#iplists_put) | **PUT** /iplists/{id} | Replace an IP list

# **iplists_delete**
> IPList iplists_delete(id, x_org_id=x_org_id)

Delete an IP list

Delete a specific IP list.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/iplists/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.IPListsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete an IP list
    api_response = api_instance.iplists_delete(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPListsApi->iplists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**IPList**](IPList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iplists_get**
> IPList iplists_get(id, x_org_id=x_org_id)

Get an IP list

Return a specific IP list.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/iplists/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.IPListsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get an IP list
    api_response = api_instance.iplists_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPListsApi->iplists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**IPList**](IPList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iplists_list**
> list[IPList] iplists_list(x_org_id=x_org_id, x_total_count=x_total_count, limit=limit, skip=skip, filter=filter, sort=sort)

List IP Lists

Retrieve all IP lists.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/iplists \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.IPListsApi(jcapiv2.ApiClient(configuration))
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
x_total_count = 56 # int |  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # List IP Lists
    api_response = api_instance.iplists_list(x_org_id=x_org_id, x_total_count=x_total_count, limit=limit, skip=skip, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPListsApi->iplists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **x_total_count** | **int**|  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[IPList]**](IPList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iplists_patch**
> IPList iplists_patch(id, body=body, x_org_id=x_org_id)

Update an IP list

Update a specific IP list.  #### Sample Request ``` curl -X PATCH https://console.jumpcloud.com/api/v2/iplists/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{\"name\": \"New IP List Name\"}' ```

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
api_instance = jcapiv2.IPListsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv2.IPListRequest() # IPListRequest |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update an IP list
    api_response = api_instance.iplists_patch(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPListsApi->iplists_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**IPListRequest**](IPListRequest.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**IPList**](IPList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iplists_post**
> IPList iplists_post(body=body, x_org_id=x_org_id)

Create IP List

Create an IP list.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/iplists \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Sample IP List\",     \"ips\": [       \"192.168.10.12\",       \"192.168.10.20 - 192.168.10.30\",       \"123.225.10.0/32\"     ]   }' ```

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
api_instance = jcapiv2.IPListsApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.IPListRequest() # IPListRequest |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create IP List
    api_response = api_instance.iplists_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPListsApi->iplists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPListRequest**](IPListRequest.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**IPList**](IPList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iplists_put**
> IPList iplists_put(id, body=body, x_org_id=x_org_id)

Replace an IP list

Replace a specific IP list.  #### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/v2/iplists/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Sample IP List\",     \"ips\": [       \"192.168.10.10\"     ]   }' ```

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
api_instance = jcapiv2.IPListsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv2.IPListRequest() # IPListRequest |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Replace an IP list
    api_response = api_instance.iplists_put(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPListsApi->iplists_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**IPListRequest**](IPListRequest.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**IPList**](IPList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

