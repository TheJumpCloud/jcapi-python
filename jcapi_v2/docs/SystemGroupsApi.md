# jcapiv2.SystemGroupsApi

All URIs are relative to *http://localhost:3004/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_delete**](SystemGroupsApi.md#system_delete) | **DELETE** /systemgroups/{id} | Delete a System Group
[**system_get**](SystemGroupsApi.md#system_get) | **GET** /systemgroups/{id} | View a System Group Detail
[**system_group_members_post**](SystemGroupsApi.md#system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage members of a System Group
[**system_list**](SystemGroupsApi.md#system_list) | **GET** /systemgroups | List All Systems Groups
[**system_patch**](SystemGroupsApi.md#system_patch) | **PATCH** /systemgroups/{id} | Partial Update a System Group
[**system_post**](SystemGroupsApi.md#system_post) | **POST** /systemgroups | Create a New System Group


# **system_delete**
> system_delete(id)

Delete a System Group

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemGroupsApi()
id = 'id_example' # str | ObjectID of the System Group.

try: 
    # Delete a System Group
    api_instance.system_delete(id)
except ApiException as e:
    print("Exception when calling SystemGroupsApi->system_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the System Group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get**
> SystemGroup system_get(id)

View a System Group Detail

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemGroupsApi()
id = 'id_example' # str | ObjectID of the System Group.

try: 
    # View a System Group Detail
    api_response = api_instance.system_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupsApi->system_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the System Group. | 

### Return type

[**SystemGroup**](SystemGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_members_post**
> system_group_members_post(group_id, body)

Manage members of a System Group

This manages the _direct_ children (Systems and System Groups) of a group.  A System Group can contain Systems and System Groups. No cycles are allowed; i.e.  if Group A contains Group B then Group B cannot also contain Group A, including any deeper nested relationships. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemGroupsApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage members of a System Group
    api_instance.system_group_members_post(group_id, body)
except ApiException as e:
    print("Exception when calling SystemGroupsApi->system_group_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_list**
> list[SystemGroup] system_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List All Systems Groups

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemGroupsApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List All Systems Groups
    api_response = api_instance.system_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupsApi->system_list: %s\n" % e)
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

[**list[SystemGroup]**](SystemGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_patch**
> SystemGroup system_patch(id, body)

Partial Update a System Group

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemGroupsApi()
id = 'id_example' # str | ObjectID of the System Group.
body = jcapiv2.SystemGroupData() # SystemGroupData | 

try: 
    # Partial Update a System Group
    api_response = api_instance.system_patch(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupsApi->system_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the System Group. | 
 **body** | [**SystemGroupData**](SystemGroupData.md)|  | 

### Return type

[**SystemGroup**](SystemGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_post**
> SystemGroup system_post(body)

Create a New System Group

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemGroupsApi()
body = jcapiv2.SystemGroupData() # SystemGroupData | 

try: 
    # Create a New System Group
    api_response = api_instance.system_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupsApi->system_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemGroupData**](SystemGroupData.md)|  | 

### Return type

[**SystemGroup**](SystemGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

