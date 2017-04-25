# jcapiv2.UserGroupsApi

All URIs are relative to *http://localhost:3004/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_delete**](UserGroupsApi.md#user_delete) | **DELETE** /usergroups/{id} | Delete a User Group
[**user_get**](UserGroupsApi.md#user_get) | **GET** /usergroups/{id} | View a User Group Detail
[**user_list**](UserGroupsApi.md#user_list) | **GET** /usergroups | List All Users Groups
[**user_patch**](UserGroupsApi.md#user_patch) | **PATCH** /usergroups/{id} | Partial Update a User Group
[**user_post**](UserGroupsApi.md#user_post) | **POST** /usergroups | Create a New User Group


# **user_delete**
> user_delete(id)

Delete a User Group

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.UserGroupsApi()
id = 'id_example' # str | ObjectID of the User Group.

try: 
    # Delete a User Group
    api_instance.user_delete(id)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the User Group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> UserGroup user_get(id)

View a User Group Detail

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.UserGroupsApi()
id = 'id_example' # str | ObjectID of the User Group.

try: 
    # View a User Group Detail
    api_response = api_instance.user_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the User Group. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_list**
> list[UserGroup] user_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List All Users Groups

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.UserGroupsApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List All Users Groups
    api_response = api_instance.user_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_patch**
> UserGroup user_patch(id, body)

Partial Update a User Group

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.UserGroupsApi()
id = 'id_example' # str | ObjectID of the User Group.
body = jcapiv2.UserGroupData() # UserGroupData | 

try: 
    # Partial Update a User Group
    api_response = api_instance.user_patch(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the User Group. | 
 **body** | [**UserGroupData**](UserGroupData.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> UserGroup user_post(body)

Create a New User Group

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.UserGroupsApi()
body = jcapiv2.UserGroupData() # UserGroupData | 

try: 
    # Create a New User Group
    api_response = api_instance.user_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupData**](UserGroupData.md)|  | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

