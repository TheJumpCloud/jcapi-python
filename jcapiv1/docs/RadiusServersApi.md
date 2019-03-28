# jcapiv1.RadiusServersApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**radius_servers_list**](RadiusServersApi.md#radius_servers_list) | **GET** /radiusservers | List Radius Servers
[**radius_servers_post**](RadiusServersApi.md#radius_servers_post) | **POST** /radiusservers | Create a Radius Server
[**radius_servers_put**](RadiusServersApi.md#radius_servers_put) | **PUT** /radiusservers:id | Update Radius Servers


# **radius_servers_list**
> Radiusserverslist radius_servers_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)

List Radius Servers

This endpoint allows you to get a list of all RADIUS servers in your organization.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/radiusservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\ ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.RadiusServersApi(jcapiv1.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional) (default to )
filter = 'filter_example' # str | A filter to apply to the query. (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending.  (optional) (default to )
x_org_id = '' # str |  (optional) (default to )

try:
    # List Radius Servers
    api_response = api_instance.radius_servers_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusServersApi->radius_servers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**| A filter to apply to the query. | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**Radiusserverslist**](Radiusserverslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radius_servers_post**
> Radiusserverslist radius_servers_post(content_type, accept, body=body, x_org_id=x_org_id)

Create a Radius Server

This endpoint allows you to create RADIUS servers in your organization.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/radiusservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"{test_radius}\",     \"networkSourceIp\": \"{0.0.0.0}\",     \"sharedSecret\":\"{secretpassword}\" }' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.RadiusServersApi(jcapiv1.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Radiusserverpost() # Radiusserverpost |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Create a Radius Server
    api_response = api_instance.radius_servers_post(content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusServersApi->radius_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Radiusserverpost**](Radiusserverpost.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**Radiusserverslist**](Radiusserverslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radius_servers_put**
> Radiusserverput radius_servers_put(content_type, accept, body=body, x_org_id=x_org_id)

Update Radius Servers

This endpoint allows you to update RADIUS servers in your organization.  ####  ``` curl -X PUT https://console.jumpcloud.com/api/radiusservers/{ServerID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"{name_update}\",     \"networkSourceIp\": \"{0.0.0.0}\" }' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.RadiusServersApi(jcapiv1.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Body() # Body |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Update Radius Servers
    api_response = api_instance.radius_servers_put(content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadiusServersApi->radius_servers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Body**](Body.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**Radiusserverput**](Radiusserverput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

