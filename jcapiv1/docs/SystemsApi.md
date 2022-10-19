# jcapiv1.SystemsApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_command_builtin_erase**](SystemsApi.md#systems_command_builtin_erase) | **POST** /systems/{system_id}/command/builtin/erase | Erase a System
[**systems_command_builtin_lock**](SystemsApi.md#systems_command_builtin_lock) | **POST** /systems/{system_id}/command/builtin/lock | Lock a System
[**systems_command_builtin_restart**](SystemsApi.md#systems_command_builtin_restart) | **POST** /systems/{system_id}/command/builtin/restart | Restart a System
[**systems_command_builtin_shutdown**](SystemsApi.md#systems_command_builtin_shutdown) | **POST** /systems/{system_id}/command/builtin/shutdown | Shutdown a System
[**systems_delete**](SystemsApi.md#systems_delete) | **DELETE** /systems/{id} | Delete a System
[**systems_get**](SystemsApi.md#systems_get) | **GET** /systems/{id} | List an individual system
[**systems_list**](SystemsApi.md#systems_list) | **GET** /systems | List All Systems
[**systems_put**](SystemsApi.md#systems_put) | **PUT** /systems/{id} | Update a system

# **systems_command_builtin_erase**
> systems_command_builtin_erase(system_id, x_org_id=x_org_id)

Erase a System

This endpoint allows you to run the erase command on the specified device. If a device is offline, the command will be run when the device becomes available.  #### Sample Request ``` curl -X POST \\   https://console.jumpcloud.com/api/systems/{system_id}/command/builtin/erase \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d {} ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
system_id = 'system_id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Erase a System
    api_instance.systems_command_builtin_erase(system_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_command_builtin_erase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_command_builtin_lock**
> systems_command_builtin_lock(system_id, x_org_id=x_org_id)

Lock a System

This endpoint allows you to run the lock command on the specified device. If a device is offline, the command will be run when the device becomes available.  #### Sample Request ``` curl -X POST \\   https://console.jumpcloud.com/api/systems/{system_id}/command/builtin/lock \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d {} ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
system_id = 'system_id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Lock a System
    api_instance.systems_command_builtin_lock(system_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_command_builtin_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_command_builtin_restart**
> systems_command_builtin_restart(system_id, x_org_id=x_org_id)

Restart a System

This endpoint allows you to run the restart command on the specified device. If a device is offline, the command will be run when the device becomes available.  #### Sample Request ``` curl -X POST \\   https://console.jumpcloud.com/api/systems/{system_id}/command/builtin/restart \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d {} ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
system_id = 'system_id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Restart a System
    api_instance.systems_command_builtin_restart(system_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_command_builtin_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_command_builtin_shutdown**
> systems_command_builtin_shutdown(system_id, x_org_id=x_org_id)

Shutdown a System

This endpoint allows you to run the shutdown command on the specified device. If a device is offline, the command will be run when the device becomes available.  #### Sample Request ``` curl -X POST \\   https://console.jumpcloud.com/api/systems/{system_id}/command/builtin/shutdown \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d {} ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
system_id = 'system_id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Shutdown a System
    api_instance.systems_command_builtin_shutdown(system_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_command_builtin_shutdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_delete**
> System systems_delete(id, _date=_date, authorization=authorization, x_org_id=x_org_id)

Delete a System

This endpoint allows you to delete a system. This command will cause the system to uninstall the JumpCloud agent from its self which can can take about a minute. If the system is not connected to JumpCloud the system record will simply be removed.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/systems/{SystemID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
_date = '_date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Delete a System
    api_response = api_instance.systems_delete(id, _date=_date, authorization=authorization, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **_date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**System**](System.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_get**
> System systems_get(id, fields=fields, filter=filter, _date=_date, authorization=authorization, x_org_id=x_org_id)

List an individual system

This endpoint returns an individual system.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/systems/{SystemID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional)
filter = 'filter_example' # str | A filter to apply to the query. See the supported operators below. For more complex searches, see the related `/search/<domain>` endpoints, e.g. `/search/systems`.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** = Supported operators are: - `$eq` (equals) - `$ne` (does not equal) - `$gt` (is greater than) - `$gte` (is greater than or equal to) - `$lt` (is less than) - `$lte` (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the `$` will result in undefined behavior._  **value** = Populate with the value you want to search for. Is case sensitive.  **Examples** - `GET /users?filter=username:$eq:testuser` - `GET /systemusers?filter=password_expiration_date:$lte:2021-10-24` - `GET /systemusers?filter=department:$ne:Accounting` - `GET /systems?filter[0]=firstname:$eq:foo&filter[1]=lastname:$eq:bar` - this will    AND the filters together. - `GET /systems?filter[or][0]=lastname:$eq:foo&filter[or][1]=lastname:$eq:bar` - this will    OR the filters together. (optional)
_date = '_date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # List an individual system
    api_response = api_instance.systems_get(id, fields=fields, filter=filter, _date=_date, authorization=authorization, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | **str**| A filter to apply to the query. See the supported operators below. For more complex searches, see the related &#x60;/search/&lt;domain&gt;&#x60; endpoints, e.g. &#x60;/search/systems&#x60;.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D; Supported operators are: - &#x60;$eq&#x60; (equals) - &#x60;$ne&#x60; (does not equal) - &#x60;$gt&#x60; (is greater than) - &#x60;$gte&#x60; (is greater than or equal to) - &#x60;$lt&#x60; (is less than) - &#x60;$lte&#x60; (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the &#x60;$&#x60; will result in undefined behavior._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive.  **Examples** - &#x60;GET /users?filter&#x3D;username:$eq:testuser&#x60; - &#x60;GET /systemusers?filter&#x3D;password_expiration_date:$lte:2021-10-24&#x60; - &#x60;GET /systemusers?filter&#x3D;department:$ne:Accounting&#x60; - &#x60;GET /systems?filter[0]&#x3D;firstname:$eq:foo&amp;filter[1]&#x3D;lastname:$eq:bar&#x60; - this will    AND the filters together. - &#x60;GET /systems?filter[or][0]&#x3D;lastname:$eq:foo&amp;filter[or][1]&#x3D;lastname:$eq:bar&#x60; - this will    OR the filters together. | [optional] 
 **_date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**System**](System.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_list**
> Systemslist systems_list(fields=fields, limit=limit, x_org_id=x_org_id, search=search, skip=skip, sort=sort, filter=filter)

List All Systems

This endpoint returns all Systems.  #### Sample Requests ``` curl -X GET https://console.jumpcloud.com/api/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
fields = 'fields_example' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str |  (optional)
search = 'search_example' # str | A nested object containing a `searchTerm` string or array of strings and a list of `fields` to search on. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = 'sort_example' # str | Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending.  (optional)
filter = 'filter_example' # str | A filter to apply to the query. See the supported operators below. For more complex searches, see the related `/search/<domain>` endpoints, e.g. `/search/systems`.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** = Supported operators are: - `$eq` (equals) - `$ne` (does not equal) - `$gt` (is greater than) - `$gte` (is greater than or equal to) - `$lt` (is less than) - `$lte` (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the `$` will result in undefined behavior._  **value** = Populate with the value you want to search for. Is case sensitive.  **Examples** - `GET /users?filter=username:$eq:testuser` - `GET /systemusers?filter=password_expiration_date:$lte:2021-10-24` - `GET /systemusers?filter=department:$ne:Accounting` - `GET /systems?filter[0]=firstname:$eq:foo&filter[1]=lastname:$eq:bar` - this will    AND the filters together. - `GET /systems?filter[or][0]=lastname:$eq:foo&filter[or][1]=lastname:$eq:bar` - this will    OR the filters together. (optional)

try:
    # List All Systems
    api_response = api_instance.systems_list(fields=fields, limit=limit, x_org_id=x_org_id, search=search, skip=skip, sort=sort, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] 
 **search** | **str**| A nested object containing a &#x60;searchTerm&#x60; string or array of strings and a list of &#x60;fields&#x60; to search on. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **filter** | **str**| A filter to apply to the query. See the supported operators below. For more complex searches, see the related &#x60;/search/&lt;domain&gt;&#x60; endpoints, e.g. &#x60;/search/systems&#x60;.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D; Supported operators are: - &#x60;$eq&#x60; (equals) - &#x60;$ne&#x60; (does not equal) - &#x60;$gt&#x60; (is greater than) - &#x60;$gte&#x60; (is greater than or equal to) - &#x60;$lt&#x60; (is less than) - &#x60;$lte&#x60; (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the &#x60;$&#x60; will result in undefined behavior._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive.  **Examples** - &#x60;GET /users?filter&#x3D;username:$eq:testuser&#x60; - &#x60;GET /systemusers?filter&#x3D;password_expiration_date:$lte:2021-10-24&#x60; - &#x60;GET /systemusers?filter&#x3D;department:$ne:Accounting&#x60; - &#x60;GET /systems?filter[0]&#x3D;firstname:$eq:foo&amp;filter[1]&#x3D;lastname:$eq:bar&#x60; - this will    AND the filters together. - &#x60;GET /systems?filter[or][0]&#x3D;lastname:$eq:foo&amp;filter[or][1]&#x3D;lastname:$eq:bar&#x60; - this will    OR the filters together. | [optional] 

### Return type

[**Systemslist**](Systemslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_put**
> System systems_put(id, body=body, _date=_date, authorization=authorization, x_org_id=x_org_id)

Update a system

This endpoint allows you to update a system.  #### Sample Request  ``` curl -X PUT https://console.jumpcloud.com/api/systems/{SystemID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"displayName\":\"Name_Update\",  \"allowSshPasswordAuthentication\":\"true\",  \"allowSshRootLogin\":\"true\",  \"allowMultiFactorAuthentication\":\"true\",  \"allowPublicKeyAuthentication\":\"false\" }' ```

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
api_instance = jcapiv1.SystemsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.Systemput() # Systemput |  (optional)
_date = '_date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Update a system
    api_response = api_instance.systems_put(id, body=body, _date=_date, authorization=authorization, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Systemput**](Systemput.md)|  | [optional] 
 **_date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**System**](System.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

