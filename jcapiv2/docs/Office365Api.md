# jcapiv2.Office365Api

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_office365_associations_list**](Office365Api.md#graph_office365_associations_list) | **GET** /office365s/{office365_id}/associations | List the associations of an Office 365 instance
[**graph_office365_associations_post**](Office365Api.md#graph_office365_associations_post) | **POST** /office365s/{office365_id}/associations | Manage the associations of an Office 365 instance
[**graph_office365_traverse_user**](Office365Api.md#graph_office365_traverse_user) | **GET** /office365s/{office365_id}/users | List the Users associated with an Office 365 instance
[**graph_office365_traverse_user_group**](Office365Api.md#graph_office365_traverse_user_group) | **GET** /office365s/{office365_id}/usergroups | List the User Groups associated with an Office 365 instance


# **graph_office365_associations_list**
> list[GraphConnection] graph_office365_associations_list(office365_id, targets, content_type, accept, limit=limit, skip=skip)

List the associations of an Office 365 instance

This endpoint returns _direct_ associations of an Office 365 instance.   A direct association can be a non-homogenous relationship between 2 different objects. for example Office 365 and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/associations?targets=user ```

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
api_instance = jcapiv2.Office365Api()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
targets = ['targets_example'] # list[str] | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the associations of an Office 365 instance
    api_response = api_instance.graph_office365_associations_list(office365_id, targets, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
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

# **graph_office365_associations_post**
> graph_office365_associations_post(office365_id, content_type, accept, body=body)

Manage the associations of an Office 365 instance

This endpoint allows you to manage the _direct_ associations of a Office 365 instance.  A direct association can be a non-homogenous relationship between 2 different objects. for example Office 365 and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/associations ```

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
api_instance = jcapiv2.Office365Api()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.GraphManagementReq() # GraphManagementReq |  (optional)

try: 
    # Manage the associations of an Office 365 instance
    api_instance.graph_office365_associations_post(office365_id, content_type, accept, body=body)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
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

# **graph_office365_traverse_user**
> list[GraphObjectWithPaths] graph_office365_traverse_user(office365_id, content_type, accept, limit=limit, skip=skip)

List the Users associated with an Office 365 instance

This endpoint will return Users associated with an Office 365 instance. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/users ```

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
api_instance = jcapiv2.Office365Api()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 suite.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the Users associated with an Office 365 instance
    api_response = api_instance.graph_office365_traverse_user(office365_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 suite. | 
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

# **graph_office365_traverse_user_group**
> list[GraphObjectWithPaths] graph_office365_traverse_user_group(office365_id, content_type, accept, limit=limit, skip=skip)

List the User Groups associated with an Office 365 instance

This endpoint will return User Groups associated with an Office 365 instance. Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/usergroups ```

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
api_instance = jcapiv2.Office365Api()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 suite.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the User Groups associated with an Office 365 instance
    api_response = api_instance.graph_office365_traverse_user_group(office365_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 suite. | 
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

