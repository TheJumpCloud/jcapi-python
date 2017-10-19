# jcapiv2.SystemsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_system_associations_list**](SystemsApi.md#graph_system_associations_list) | **GET** /systems/{system_id}/associations | List the associations of a System
[**graph_system_associations_post**](SystemsApi.md#graph_system_associations_post) | **POST** /systems/{system_id}/associations | Manage associations of a System
[**graph_system_member_of**](SystemsApi.md#graph_system_member_of) | **GET** /systems/{system_id}/memberof | List the parent Groups of a System
[**graph_system_traverse_policy**](SystemsApi.md#graph_system_traverse_policy) | **GET** /systems/{system_id}/policies | List the Policies associated with a System
[**graph_system_traverse_user**](SystemsApi.md#graph_system_traverse_user) | **GET** /systems/{system_id}/users | List the Users associated with a System


# **graph_system_associations_list**
> list[GraphConnection] graph_system_associations_list(system_id, targets, content_type, accept, limit=limit, skip=skip, date=date, authorization=authorization)

List the associations of a System

This endpoint returns the _direct_ associations of a System.  A direct association can be a non-homogenous relationship between 2 different objects. for example Systems and Users.   #### Sample Request ``` https://console.jumpcloud.com/api/v2/systems/{system_id}/associations?targets=user ```

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
api_instance = jcapiv2.SystemsApi()
system_id = 'system_id_example' # str | ObjectID of the System.
targets = ['targets_example'] # list[str] | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
date = 'date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)

try: 
    # List the associations of a System
    api_response = api_instance.graph_system_associations_list(system_id, targets, content_type, accept, limit=limit, skip=skip, date=date, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->graph_system_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **targets** | [**list[str]**](str.md)|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_associations_post**
> graph_system_associations_post(system_id, content_type, accept, body=body, date=date, authorization=authorization)

Manage associations of a System

This endpoint allows you to manage the _direct_ associations of a System.  A direct association can be a non-homogenous relationship between 2 different objects. for example Systems and Users.   #### Sample Request ``` https://console.jumpcloud.com/api/v2/systems/{system_id}/associations ```

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
api_instance = jcapiv2.SystemsApi()
system_id = 'system_id_example' # str | ObjectID of the System.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.GraphManagementReq() # GraphManagementReq |  (optional)
date = 'date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)

try: 
    # Manage associations of a System
    api_instance.graph_system_associations_post(system_id, content_type, accept, body=body, date=date, authorization=authorization)
except ApiException as e:
    print("Exception when calling SystemsApi->graph_system_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | [optional] 
 **date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_member_of**
> list[GraphObjectWithPaths] graph_system_member_of(system_id, content_type, accept, limit=limit, skip=skip, date=date, authorization=authorization)

List the parent Groups of a System

This endpoint returns all the System Groups a System is a member of.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/systems/{system_id}/memberof ```

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
api_instance = jcapiv2.SystemsApi()
system_id = 'system_id_example' # str | ObjectID of the System.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
date = 'date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)

try: 
    # List the parent Groups of a System
    api_response = api_instance.graph_system_member_of(system_id, content_type, accept, limit=limit, skip=skip, date=date, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->graph_system_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_traverse_policy**
> list[GraphObjectWithPaths] graph_system_traverse_policy(system_id, content_type, accept, limit=limit, skip=skip)

List the Policies associated with a System

This endpoint will return Policies associated with a System. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this System to the corresponding Policy; this array represents all grouping and/or associations that would have to be removed to deprovision the Policy from this System.  See `/members` and `/associations` endpoints to manage those collections.  This endpoint is not yet public as we have finish the code.

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
api_instance = jcapiv2.SystemsApi()
system_id = 'system_id_example' # str | ObjectID of the System.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the Policies associated with a System
    api_response = api_instance.graph_system_traverse_policy(system_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->graph_system_traverse_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
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

# **graph_system_traverse_user**
> list[GraphObjectWithPaths] graph_system_traverse_user(system_id, content_type, accept, limit=limit, skip=skip, date=date, authorization=authorization)

List the Users associated with a System

This endpoint will return Users associated with a System. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this System to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this System.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/systems/{system_id}/users ```

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
api_instance = jcapiv2.SystemsApi()
system_id = 'system_id_example' # str | ObjectID of the System.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
date = 'date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)

try: 
    # List the Users associated with a System
    api_response = api_instance.graph_system_traverse_user(system_id, content_type, accept, limit=limit, skip=skip, date=date, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->graph_system_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

