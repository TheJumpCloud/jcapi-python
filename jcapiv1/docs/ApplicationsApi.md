# jcapiv1.ApplicationsApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_delete**](ApplicationsApi.md#applications_delete) | **DELETE** /applications/{id} | Delete an Application
[**applications_get**](ApplicationsApi.md#applications_get) | **GET** /applications/{id} | Get an Application
[**applications_list**](ApplicationsApi.md#applications_list) | **GET** /applications | Applications
[**applications_post**](ApplicationsApi.md#applications_post) | **POST** /applications | Create an Application
[**applications_put**](ApplicationsApi.md#applications_put) | **PUT** /applications/{id} | Update an Application


# **applications_delete**
> Application applications_delete(id, content_type=content_type, accept=accept, x_org_id=x_org_id)

Delete an Application

The endpoint deletes an SSO / SAML Application.

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
api_instance = jcapiv1.ApplicationsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Delete an Application
    api_response = api_instance.applications_delete(id, content_type=content_type, accept=accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_get**
> Application applications_get(id, content_type=content_type, accept=accept, x_org_id=x_org_id)

Get an Application

The endpoint retrieves an SSO / SAML Application.

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
api_instance = jcapiv1.ApplicationsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
content_type = 'content_type_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Get an Application
    api_response = api_instance.applications_get(id, content_type=content_type, accept=accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_list**
> Applicationslist applications_list(content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)

Applications

The endpoint returns all your SSO / SAML Applications.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv1.ApplicationsApi(jcapiv1.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = 'fields_example' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned. (optional)
limit = 56 # int | The number of records to return at once. (optional)
skip = 56 # int | The offset into the records to return. (optional)
sort = 'The comma separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending.' # str |  (optional) (default to The comma separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending.)
filter = 'filter_example' # str | A filter to apply to the query. (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Applications
    api_response = api_instance.applications_list(content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned. | [optional] 
 **limit** | **int**| The number of records to return at once. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] 
 **sort** | **str**|  | [optional] [default to The comma separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending.]
 **filter** | **str**| A filter to apply to the query. | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**Applicationslist**](Applicationslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_post**
> Application applications_post(body=body, content_type=content_type, accept=accept, x_org_id=x_org_id)

Create an Application

The endpoint adds a new SSO / SAML Applications.

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
api_instance = jcapiv1.ApplicationsApi(jcapiv1.ApiClient(configuration))
body = jcapiv1.Application() # Application |  (optional)
content_type = 'content_type_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Create an Application
    api_response = api_instance.applications_post(body=body, content_type=content_type, accept=accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Application**](Application.md)|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_put**
> Application applications_put(id, body=body, content_type=content_type, accept=accept, x_org_id=x_org_id)

Update an Application

The endpoint updates a SSO / SAML Application.

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
api_instance = jcapiv1.ApplicationsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.Application() # Application |  (optional)
content_type = 'content_type_example' # str |  (optional)
accept = 'accept_example' # str |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Update an Application
    api_response = api_instance.applications_put(id, body=body, content_type=content_type, accept=accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Application**](Application.md)|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

