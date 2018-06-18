# jcapiv2.SystemGroupMembersMembershipApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_system_group_member_of**](SystemGroupMembersMembershipApi.md#graph_system_group_member_of) | **GET** /systemgroups/{group_id}/memberof | List the System Group&#39;s parents
[**graph_system_group_members_list**](SystemGroupMembersMembershipApi.md#graph_system_group_members_list) | **GET** /systemgroups/{group_id}/members | List the members of a System Group
[**graph_system_group_members_post**](SystemGroupMembersMembershipApi.md#graph_system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage the members of a System Group
[**graph_system_group_membership**](SystemGroupMembersMembershipApi.md#graph_system_group_membership) | **GET** /systemgroups/{group_id}/membership | List the System Group&#39;s membership


# **graph_system_group_member_of**
> list[GraphObjectWithPaths] graph_system_group_member_of(group_id, content_type, accept, filter=filter, limit=limit, skip=skip, sort=sort)

List the System Group's parents

This endpoint returns all System Groups a System Group is a member of.  This endpoint is not yet public as we haven't completed the code yet.

### Example 
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
filter = ['filter_example'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try: 
    # List the System Group's parents
    api_response = api_instance.graph_system_group_member_of(group_id, content_type, accept, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_group_members_list**
> list[GraphConnection] graph_system_group_members_list(group_id, content_type, accept, limit=limit, skip=skip)

List the members of a System Group

This endpoint returns the system members of a System Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

### Example 
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the members of a System Group
    api_response = api_instance.graph_system_group_members_list(group_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_members_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_group_members_post**
> graph_system_group_members_post(group_id, content_type, accept, body=body, date=date, authorization=authorization)

Manage the members of a System Group

This endpoint allows you to manage the system members of a System Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{System_ID\" }' ```

### Example 
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.SystemGroupMembersReq() # SystemGroupMembersReq |  (optional)
date = 'date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)

try: 
    # Manage the members of a System Group
    api_instance.graph_system_group_members_post(group_id, content_type, accept, body=body, date=date, authorization=authorization)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**SystemGroupMembersReq**](SystemGroupMembersReq.md)|  | [optional] 
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

# **graph_system_group_membership**
> list[GraphObjectWithPaths] graph_system_group_membership(group_id, content_type, accept, limit=limit, skip=skip, sort=sort, filter=filter)

List the System Group's membership

This endpoint returns all Systems that are a member of this System Group.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID/membership \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

### Example 
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv2.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv2.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
filter = ['filter_example'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional)

try: 
    # List the System Group's membership
    api_response = api_instance.graph_system_group_membership(group_id, content_type, accept, limit=limit, skip=skip, sort=sort, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

