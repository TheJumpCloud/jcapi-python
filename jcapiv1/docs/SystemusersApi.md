# jcapiv1.SystemusersApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systemusers_delete**](SystemusersApi.md#systemusers_delete) | **DELETE** /systemusers/{id} | Delete a system user
[**systemusers_get**](SystemusersApi.md#systemusers_get) | **GET** /systemusers/{id} | List a system user
[**systemusers_list**](SystemusersApi.md#systemusers_list) | **GET** /systemusers | List all system users
[**systemusers_post**](SystemusersApi.md#systemusers_post) | **POST** /systemusers | Create a system user
[**systemusers_put**](SystemusersApi.md#systemusers_put) | **PUT** /systemusers/{id} | Update a system user
[**systemusers_systems_binding_list**](SystemusersApi.md#systemusers_systems_binding_list) | **GET** /systemusers/{id}/systems | List system user binding
[**systemusers_systems_binding_put**](SystemusersApi.md#systemusers_systems_binding_put) | **PUT** /systemusers/{id}/systems | Update a system user binding


# **systemusers_delete**
> Systemuserreturn systemusers_delete(id, content_type, accept)

Delete a system user

Delete a particular system user.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)

try: 
    # Delete a system user
    api_response = api_instance.systemusers_delete(id, content_type, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_get**
> Systemuser systemusers_get(id, content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort)

List a system user

Get a particular System User.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )

try: 
    # List a system user
    api_response = api_instance.systemusers_get(id, content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]

### Return type

[**Systemuser**](Systemuser.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_list**
> Systemuserslist systemusers_list(content_type, accept, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List all system users

Returns all systemusers.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List all system users
    api_response = api_instance.systemusers_list(content_type, accept, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**Systemuserslist**](Systemuserslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_post**
> Systemuserreturn systemusers_post(content_type, accept, body=body)

Create a system user

Create a new system user.  ### Example  #### Create a system user  This example assumes there is already a Tag named \"admins\" in your JumpCloud account.  ``` curl \\   -d '{\"email\" : \"bob@myco.com\", \"username\" : \"bob\", \"tags\" : [\"admins\"]}' \\   -X 'POST' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' \\   -H \"x-api-key: [YOUR_API_KEY_HERE]\" \\   \"https://console.jumpcloud.com/api/systemusers\"

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Systemuserputpost() # Systemuserputpost |  (optional)

try: 
    # Create a system user
    api_response = api_instance.systemusers_post(content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Systemuserputpost**](Systemuserputpost.md)|  | [optional] 

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_put**
> Systemuserreturn systemusers_put(id, content_type, accept, body=body)

Update a system user

Update a system user record and return the modified record.  ### Example  #### Add attributes to a System User  ``` curl \\  -X 'PUT' \\  -H 'Content-Type: application/json' \\  -H 'Accept: application/json' \\  -H \"x-api-key: [YOUR_API_KEY_HERE]\" \\  -d '{ \"attributes\" : [ { \"name\" : \"myhappyattribute\", \"value\" : \"myhappyattributevalue\" }] }' \\  \"https://console.jumpcloud.com/api/systemusers/:id\" ```

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Systemuserputpost() # Systemuserputpost |  (optional)

try: 
    # Update a system user
    api_response = api_instance.systemusers_put(id, content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Systemuserputpost**](Systemuserputpost.md)|  | [optional] 

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_systems_binding_list**
> object systemusers_systems_binding_list(id, content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort)

List system user binding

List system bindings for a specific system user in a system and user binding format.  ### Examples  #### List system bindings for specific system user  ``` curl \\   -H 'Content-Type: application/json' \\   -H \"x-api-key: [YOUR_API_KEY_HERE]\" \\   \"https://console.jumpcloud.com/api/systemusers/[SYSTEM_USER_ID_HERE]/systems\" ```

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )

try: 
    # List system user binding
    api_response = api_instance.systemusers_systems_binding_list(id, content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_systems_binding_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]

### Return type

**object**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_systems_binding_put**
> Usersystembinding systemusers_systems_binding_put(id, content_type, accept, body=body)

Update a system user binding

Adds or removes a system binding for a user.   This endpoint is only used for users still using JumpCloud Tags. If you are using JumpCloud Groups please refer to the documentation found [here](https://docs.jumpcloud.com/2.0/systems/manage-associations-of-a-system).  ### Example  #### Add (or remove) system to system user  ``` curl \\   -d '{ \"add\": [\"[SYSTEM_ID_TO_ADD_HERE]\"], \"remove\": [\"[SYSTEM_ID_TO_REMOVE_HERE]\"] }' \\   -X PUT \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' \\   -H \"x-api-key: [YOUR_API_KEY_HERE]\" \\   \"https://console.jumpcloud.com/api/systemusers/[SYSTEM_USER_ID_HERE]/systems\" ```

### Example 
```python
from __future__ import print_statement
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SystemusersApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Usersystembindingsput() # Usersystembindingsput |  (optional)

try: 
    # Update a system user binding
    api_response = api_instance.systemusers_systems_binding_put(id, content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_systems_binding_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Usersystembindingsput**](Usersystembindingsput.md)|  | [optional] 

### Return type

[**Usersystembinding**](Usersystembinding.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

