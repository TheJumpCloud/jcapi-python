# jcapiv1.CommandsApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command_file_get**](CommandsApi.md#command_file_get) | **GET** /files/command/{id} | Get a Command File
[**commands_delete**](CommandsApi.md#commands_delete) | **DELETE** /commands/{id} | Delete a Command
[**commands_get**](CommandsApi.md#commands_get) | **GET** /commands/{id} | List an individual Command
[**commands_get_results**](CommandsApi.md#commands_get_results) | **GET** /commands/{id}/results | Get results for a specific command
[**commands_list**](CommandsApi.md#commands_list) | **GET** /commands | List All Commands
[**commands_post**](CommandsApi.md#commands_post) | **POST** /commands | Create A Command
[**commands_put**](CommandsApi.md#commands_put) | **PUT** /commands/{id} | Update a Command

# **command_file_get**
> Commandfilereturn command_file_get(id, fields=fields, limit=limit, x_org_id=x_org_id, skip=skip)

Get a Command File

This endpoint returns the uploaded file(s) associated with a specific command.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/files/command/{commandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str |  (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # Get a Command File
    api_response = api_instance.command_file_get(id, fields=fields, limit=limit, x_org_id=x_org_id, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->command_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**Commandfilereturn**](Commandfilereturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_delete**
> Command commands_delete(id, x_org_id=x_org_id)

Delete a Command

This endpoint deletes a specific command based on the Command ID.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Delete a Command
    api_response = api_instance.commands_delete(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->commands_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Command**](Command.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_get**
> Command commands_get(id, fields=fields, x_org_id=x_org_id)

List an individual Command

This endpoint returns a specific command based on the command ID.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # List an individual Command
    api_response = api_instance.commands_get(id, fields=fields, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->commands_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Command**](Command.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_get_results**
> list[Commandresult] commands_get_results(id)

Get results for a specific command

This endpoint returns results for a specific command.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/{id}/results \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ````

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get results for a specific command
    api_response = api_instance.commands_get_results(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->commands_get_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[Commandresult]**](Commandresult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_list**
> Commandslist commands_list(fields=fields, filter=filter, limit=limit, x_org_id=x_org_id, skip=skip, sort=sort)

List All Commands

This endpoint returns all commands.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/commands/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
fields = 'fields_example' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional)
filter = 'filter_example' # str | A filter to apply to the query. See the supported operators below. For more complex searches, see the related `/search/<domain>` endpoints, e.g. `/search/systems`.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** = Supported operators are: - `$eq` (equals) - `$ne` (does not equal) - `$gt` (is greater than) - `$gte` (is greater than or equal to) - `$lt` (is less than) - `$lte` (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the `$` will result in undefined behavior._  **value** = Populate with the value you want to search for. Is case sensitive.  **Examples** - `GET /users?filter=username:$eq:testuser` - `GET /systemusers?filter=password_expiration_date:$lte:2021-10-24` - `GET /systemusers?filter=department:$ne:Accounting` - `GET /systems?filter[0]=firstname:$eq:foo&filter[1]=lastname:$eq:bar` - this will    AND the filters together. - `GET /systems?filter[or][0]=lastname:$eq:foo&filter[or][1]=lastname:$eq:bar` - this will    OR the filters together. (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str |  (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = 'sort_example' # str | Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending.  (optional)

try:
    # List All Commands
    api_response = api_instance.commands_list(fields=fields, filter=filter, limit=limit, x_org_id=x_org_id, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->commands_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | **str**| A filter to apply to the query. See the supported operators below. For more complex searches, see the related &#x60;/search/&lt;domain&gt;&#x60; endpoints, e.g. &#x60;/search/systems&#x60;.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D; Supported operators are: - &#x60;$eq&#x60; (equals) - &#x60;$ne&#x60; (does not equal) - &#x60;$gt&#x60; (is greater than) - &#x60;$gte&#x60; (is greater than or equal to) - &#x60;$lt&#x60; (is less than) - &#x60;$lte&#x60; (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the &#x60;$&#x60; will result in undefined behavior._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive.  **Examples** - &#x60;GET /users?filter&#x3D;username:$eq:testuser&#x60; - &#x60;GET /systemusers?filter&#x3D;password_expiration_date:$lte:2021-10-24&#x60; - &#x60;GET /systemusers?filter&#x3D;department:$ne:Accounting&#x60; - &#x60;GET /systems?filter[0]&#x3D;firstname:$eq:foo&amp;filter[1]&#x3D;lastname:$eq:bar&#x60; - this will    AND the filters together. - &#x60;GET /systems?filter[or][0]&#x3D;lastname:$eq:foo&amp;filter[or][1]&#x3D;lastname:$eq:bar&#x60; - this will    OR the filters together. | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**Commandslist**](Commandslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_post**
> Command commands_post(body=body, x_org_id=x_org_id)

Create A Command

This endpoint allows you to create a new command.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/commands/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"name\":\"Test API Command\",  \"command\":\"String\",  \"user\":\"{UserID}\",  \"schedule\":\"\",  \"timeout\":\"100\" }'  ```

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
body = jcapiv1.Command() # Command |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Create A Command
    api_response = api_instance.commands_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->commands_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Command**](Command.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Command**](Command.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_put**
> Command commands_put(id, body=body, x_org_id=x_org_id)

Update a Command

This endpoint Updates a command based on the command ID and returns the modified command record.  #### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/commands/{CommandID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"name\":\"Test API Command\",  \"command\":\"String\",  \"user\":\"{UserID}\",  \"schedule\":\"\",  \"timeout\":\"100\" }'  ```

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
api_instance = jcapiv1.CommandsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.Command() # Command |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Update a Command
    api_response = api_instance.commands_put(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->commands_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Command**](Command.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Command**](Command.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

