# jcapiv2.CommandsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_command_associations_list**](CommandsApi.md#graph_command_associations_list) | **GET** /commands/{command_id}/associations | List the associations of a Command
[**graph_command_associations_post**](CommandsApi.md#graph_command_associations_post) | **POST** /commands/{command_id}/associations | Manage the associations of a Command
[**graph_command_traverse_system**](CommandsApi.md#graph_command_traverse_system) | **GET** /commands/{command_id}/systems | List the Systems associated with a Command
[**graph_command_traverse_system_group**](CommandsApi.md#graph_command_traverse_system_group) | **GET** /commands/{command_id}/systemgroups | List the System Groups associated with a Command


# **graph_command_associations_list**
> list[GraphConnection] graph_command_associations_list(command_id, targets, content_type, accept, limit=limit, skip=skip)

List the associations of a Command

This endpoint will return the _direct_ associations of this Command.  A direct association can be a non-homogenous relationship between 2 different objects. for example Commands and User Groups.   #### Sample Request ``` https://console.jumpcloud.com/api/v2/commands/{command_id}/associations?targets=user_group ```

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.CommandsApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
targets = ['targets_example'] # list[str] | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the associations of a Command
    api_response = api_instance.graph_command_associations_list(command_id, targets, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->graph_command_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **targets** | [**list[str]**](str.md)|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_command_associations_post**
> graph_command_associations_post(command_id, content_type, accept, body=body)

Manage the associations of a Command

This endpoint will allow you to manage the _direct_ associations of this Command.  A direct association can be a non-homogenous relationship between 2 different objects. for example Commands and User Groups.   #### Sample Request ``` https://console.jumpcloud.com/api/v2/commands/{command_id}/associations

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.CommandsApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.GraphManagementReq() # GraphManagementReq |  (optional)

try: 
    # Manage the associations of a Command
    api_instance.graph_command_associations_post(command_id, content_type, accept, body=body)
except ApiException as e:
    print("Exception when calling CommandsApi->graph_command_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_command_traverse_system**
> list[GraphObjectWithPaths] graph_command_traverse_system(command_id, content_type, accept, limit=limit, skip=skip)

List the Systems associated with a Command

This endpoint will return Systems associated with a Command. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Command to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/commands/{command_id}/systems ```

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.CommandsApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the Systems associated with a Command
    api_response = api_instance.graph_command_traverse_system(command_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->graph_command_traverse_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_command_traverse_system_group**
> list[GraphObjectWithPaths] graph_command_traverse_system_group(command_id, content_type, accept, limit=limit, skip=skip)

List the System Groups associated with a Command

This endpoint will return System Groups associated with a Command. Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Command to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/commands/{command_id}/systemsgroups ```

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.CommandsApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the System Groups associated with a Command
    api_response = api_instance.graph_command_traverse_system_group(command_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandsApi->graph_command_traverse_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

