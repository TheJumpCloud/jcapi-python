# jcapiv1.DefaultApi

All URIs are relative to *http://localhost:3004/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**command_trigger_webhook_post**](DefaultApi.md#command_trigger_webhook_post) | **POST** /command/trigger/{webhook} | 
[**commandresults_get**](DefaultApi.md#commandresults_get) | **GET** /commandresults | 
[**commandresults_id_delete**](DefaultApi.md#commandresults_id_delete) | **DELETE** /commandresults/{id} | 
[**commandresults_id_get**](DefaultApi.md#commandresults_id_get) | **GET** /commandresults/{id} | 
[**commands_get**](DefaultApi.md#commands_get) | **GET** /commands/ | 
[**commands_id_delete**](DefaultApi.md#commands_id_delete) | **DELETE** /commands/{id} | 
[**commands_id_get**](DefaultApi.md#commands_id_get) | **GET** /commands/{id} | 
[**commands_id_put**](DefaultApi.md#commands_id_put) | **PUT** /commands/{id} | 
[**commands_post**](DefaultApi.md#commands_post) | **POST** /commands/ | 
[**search_systemusers_post**](DefaultApi.md#search_systemusers_post) | **POST** /search/systemusers | 
[**systems_system_id_systemusers_get**](DefaultApi.md#systems_system_id_systemusers_get) | **GET** /systems/{systemID}/systemusers | 
[**systems_system_id_systemusers_put**](DefaultApi.md#systems_system_id_systemusers_put) | **PUT** /systems/{systemID}/systemusers | 
[**systemusers_get**](DefaultApi.md#systemusers_get) | **GET** /systemusers | 
[**systemusers_id_delete**](DefaultApi.md#systemusers_id_delete) | **DELETE** /systemusers/{id} | 
[**systemusers_id_get**](DefaultApi.md#systemusers_id_get) | **GET** /systemusers/{id} | 
[**systemusers_id_put**](DefaultApi.md#systemusers_id_put) | **PUT** /systemusers/{id} | 
[**systemusers_post**](DefaultApi.md#systemusers_post) | **POST** /systemusers | 
[**systemusers_system_user_id_systems_get**](DefaultApi.md#systemusers_system_user_id_systems_get) | **GET** /systemusers/{systemUserID}/systems | 
[**systemusers_system_user_id_systems_put**](DefaultApi.md#systemusers_system_user_id_systems_put) | **PUT** /systemusers/{systemUserID}/systems | 


# **command_trigger_webhook_post**
> command_trigger_webhook_post(x_api_key, webhook)



Launch the command assigned to the specified webhook.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
webhook = 'webhook_example' # str | 

try: 
    api_instance.command_trigger_webhook_post(x_api_key, webhook)
except ApiException as e:
    print("Exception when calling DefaultApi->command_trigger_webhook_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **webhook** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commandresults_get**
> InlineResponse2002 commandresults_get(x_api_key)



Returns all command results for the org in multi-record format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 

try: 
    api_response = api_instance.commandresults_get(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commandresults_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commandresults_id_delete**
> commandresults_id_delete(x_api_key, id)



Deletes the command result with the given ID.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 

try: 
    api_instance.commandresults_id_delete(x_api_key, id)
except ApiException as e:
    print("Exception when calling DefaultApi->commandresults_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commandresults_id_get**
> Commandresults commandresults_id_get(x_api_key, id)



Get a command result from the ID in single-record format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 

try: 
    api_response = api_instance.commandresults_id_get(x_api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commandresults_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Commandresults**](Commandresults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_get**
> InlineResponse2001 commands_get(x_api_key)



Get saved commands in multi-record format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 

try: 
    api_response = api_instance.commands_get(x_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_id_delete**
> commands_id_delete(x_api_key, id)



Delete a saved command record by the command ID.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 

try: 
    api_instance.commands_id_delete(x_api_key, id)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_id_get**
> Commands commands_id_get(x_api_key, id)



Gets a single command record using the command ID.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 

try: 
    api_response = api_instance.commands_id_get(x_api_key, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Commands**](Commands.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_id_put**
> Commands commands_id_put(x_api_key, id, body)



Updates a saved command record from the command ID and returns the modified command record in single-record format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 
body = jcapiv1.Commands() # Commands | 

try: 
    api_response = api_instance.commands_id_put(x_api_key, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Commands**](Commands.md)|  | 

### Return type

[**Commands**](Commands.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commands_post**
> Commands commands_post(x_api_key, body)



Add a new saved command record and return the newly created saved command in a single-record format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
body = jcapiv1.Commands() # Commands | 

try: 
    api_response = api_instance.commands_post(x_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->commands_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **body** | [**Commands**](Commands.md)|  | 

### Return type

[**Commands**](Commands.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_systemusers_post**
> search_systemusers_post(x_api_key, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter, body=body)



Get System Users in multi-record format allowing for the passing of the 'filter' parameter.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fileds included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )
body = jcapiv1.Search() # Search |  (optional)

try: 
    api_instance.search_systemusers_post(x_api_key, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->search_systemusers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fileds included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]
 **body** | [**Search**](Search.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_systemusers_get**
> systems_system_id_systemusers_get(x_api_key, system_id)



List system user bindings for a specific system in a system and user binding format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
system_id = 'system_id_example' # str | 

try: 
    api_instance.systems_system_id_systemusers_get(x_api_key, system_id)
except ApiException as e:
    print("Exception when calling DefaultApi->systems_system_id_systemusers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **system_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_systemusers_put**
> systems_system_id_systemusers_put(x_api_key, system_id, body)



Adds or removes a user binding for a system.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
system_id = 'system_id_example' # str | 
body = jcapiv1.Systemuserbindings() # Systemuserbindings | Array of user ID's to be bound to the system.

try: 
    api_instance.systems_system_id_systemusers_put(x_api_key, system_id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->systems_system_id_systemusers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **system_id** | **str**|  | 
 **body** | [**Systemuserbindings**](Systemuserbindings.md)| Array of user ID&#39;s to be bound to the system. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_get**
> InlineResponse200 systemusers_get(x_api_key, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)



Get JumpCloud systemusers.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fileds included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    api_response = api_instance.systemusers_get(x_api_key, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fileds included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_id_delete**
> systemusers_id_delete(x_api_key, id)



Delete the system user with the given ID.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 

try: 
    api_instance.systemusers_id_delete(x_api_key, id)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_id_get**
> systemusers_id_get(x_api_key, id)



Get a System User record for User with the given ID.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 

try: 
    api_instance.systemusers_id_get(x_api_key, id)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_id_put**
> systemusers_id_put(x_api_key, id, data=data)



Update a system user record and return the modified record in single record format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
id = 'id_example' # str | 
data = jcapiv1.Data() # Data |  (optional)

try: 
    api_instance.systemusers_id_put(x_api_key, id, data=data)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**Data**](Data.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_post**
> SystemUser systemusers_post(x_api_key, data=data)



Add new System Users and return the record.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
data = jcapiv1.SystemUser() # SystemUser |  (optional)

try: 
    api_response = api_instance.systemusers_post(x_api_key, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **data** | [**SystemUser**](SystemUser.md)|  | [optional] 

### Return type

[**SystemUser**](SystemUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_system_user_id_systems_get**
> systemusers_system_user_id_systems_get(x_api_key, system_user_id)



List system bindings for a specific system user in a system and user binding format.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
system_user_id = 'system_user_id_example' # str | 

try: 
    api_instance.systemusers_system_user_id_systems_get(x_api_key, system_user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_system_user_id_systems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **system_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_system_user_id_systems_put**
> systemusers_system_user_id_systems_put(x_api_key, system_user_id, body)



Adds or removes a system binding for a user.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv1.DefaultApi()
x_api_key = 'x_api_key_example' # str | 
system_user_id = 'system_user_id_example' # str | 
body = jcapiv1.Systemuserbindings() # Systemuserbindings | Array of system ID's to be bound to the user.

try: 
    api_instance.systemusers_system_user_id_systems_put(x_api_key, system_user_id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_system_user_id_systems_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **system_user_id** | **str**|  | 
 **body** | [**Systemuserbindings**](Systemuserbindings.md)| Array of system ID&#39;s to be bound to the user. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

