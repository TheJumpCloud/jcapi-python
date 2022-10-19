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
> Application applications_delete(id, x_org_id=x_org_id)

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
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Delete an Application
    api_response = api_instance.applications_delete(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_get**
> Application applications_get(id, x_org_id=x_org_id)

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
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Get an Application
    api_response = api_instance.applications_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_list**
> Applicationslist applications_list(fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)

Applications

The endpoint returns all your SSO / SAML Applications.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
fields = 'fields_example' # str | The space separated fields included in the returned records. If omitted the default list of fields will be returned. (optional)
limit = 56 # int | The number of records to return at once. (optional)
skip = 56 # int | The offset into the records to return. (optional)
sort = 'name' # str | The space separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending. (optional) (default to name)
filter = 'filter_example' # str | A filter to apply to the query. See the supported operators below. For more complex searches, see the related `/search/<domain>` endpoints, e.g. `/search/systems`.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** = Supported operators are: - `$eq` (equals) - `$ne` (does not equal) - `$gt` (is greater than) - `$gte` (is greater than or equal to) - `$lt` (is less than) - `$lte` (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the `$` will result in undefined behavior._  **value** = Populate with the value you want to search for. Is case sensitive.  **Examples** - `GET /users?filter=username:$eq:testuser` - `GET /systemusers?filter=password_expiration_date:$lte:2021-10-24` - `GET /systemusers?filter=department:$ne:Accounting` - `GET /systems?filter[0]=firstname:$eq:foo&filter[1]=lastname:$eq:bar` - this will    AND the filters together. - `GET /systems?filter[or][0]=lastname:$eq:foo&filter[or][1]=lastname:$eq:bar` - this will    OR the filters together. (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Applications
    api_response = api_instance.applications_list(fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| The space separated fields included in the returned records. If omitted the default list of fields will be returned. | [optional] 
 **limit** | **int**| The number of records to return at once. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] 
 **sort** | **str**| The space separated fields used to sort the collection. Default sort is ascending, prefix with - to sort descending. | [optional] [default to name]
 **filter** | **str**| A filter to apply to the query. See the supported operators below. For more complex searches, see the related &#x60;/search/&lt;domain&gt;&#x60; endpoints, e.g. &#x60;/search/systems&#x60;.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D; Supported operators are: - &#x60;$eq&#x60; (equals) - &#x60;$ne&#x60; (does not equal) - &#x60;$gt&#x60; (is greater than) - &#x60;$gte&#x60; (is greater than or equal to) - &#x60;$lt&#x60; (is less than) - &#x60;$lte&#x60; (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the &#x60;$&#x60; will result in undefined behavior._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive.  **Examples** - &#x60;GET /users?filter&#x3D;username:$eq:testuser&#x60; - &#x60;GET /systemusers?filter&#x3D;password_expiration_date:$lte:2021-10-24&#x60; - &#x60;GET /systemusers?filter&#x3D;department:$ne:Accounting&#x60; - &#x60;GET /systems?filter[0]&#x3D;firstname:$eq:foo&amp;filter[1]&#x3D;lastname:$eq:bar&#x60; - this will    AND the filters together. - &#x60;GET /systems?filter[or][0]&#x3D;lastname:$eq:foo&amp;filter[or][1]&#x3D;lastname:$eq:bar&#x60; - this will    OR the filters together. | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Applicationslist**](Applicationslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_post**
> Application applications_post(body=body, x_org_id=x_org_id)

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
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Create an Application
    api_response = api_instance.applications_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Application**](Application.md)|  | [optional] 
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
> Application applications_put(id, body=body, x_org_id=x_org_id)

Update an Application

The endpoint updates a SSO / SAML Application. Any fields not provided will be reset or created with default values.

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
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Update an Application
    api_response = api_instance.applications_put(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->applications_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Application**](Application.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

