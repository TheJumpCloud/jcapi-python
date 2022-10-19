# jcapiv2.SystemGroupMembersMembershipApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_system_group_members_list**](SystemGroupMembersMembershipApi.md#graph_system_group_members_list) | **GET** /systemgroups/{group_id}/members | List the members of a System Group
[**graph_system_group_members_post**](SystemGroupMembersMembershipApi.md#graph_system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage the members of a System Group
[**graph_system_group_membership**](SystemGroupMembersMembershipApi.md#graph_system_group_membership) | **GET** /systemgroups/{group_id}/membership | List the System Group&#x27;s membership

# **graph_system_group_members_list**
> list[GraphConnection] graph_system_group_members_list(group_id, limit=limit, skip=skip, x_org_id=x_org_id)

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
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi(jcapiv2.ApiClient(configuration))
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the members of a System Group
    api_response = api_instance.graph_system_group_members_list(group_id, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_members_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_group_members_post**
> graph_system_group_members_post(group_id, body=body, _date=_date, authorization=authorization, x_org_id=x_org_id)

Manage the members of a System Group

This endpoint allows you to manage the system members of a System Group.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/systemgroups/{Group_ID}/members \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system\",     \"id\": \"{System_ID}\"   }' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi(jcapiv2.ApiClient(configuration))
group_id = 'group_id_example' # str | ObjectID of the System Group.
body = jcapiv2.GraphOperationSystemGroupMember() # GraphOperationSystemGroupMember |  (optional)
_date = '_date_example' # str | Current date header for the System Context API (optional)
authorization = 'authorization_example' # str | Authorization header for the System Context API (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Manage the members of a System Group
    api_instance.graph_system_group_members_post(group_id, body=body, _date=_date, authorization=authorization, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **body** | [**GraphOperationSystemGroupMember**](GraphOperationSystemGroupMember.md)|  | [optional] 
 **_date** | **str**| Current date header for the System Context API | [optional] 
 **authorization** | **str**| Authorization header for the System Context API | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_system_group_membership**
> list[GraphObjectWithPaths] graph_system_group_membership(group_id, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)

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
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.SystemGroupMembersMembershipApi(jcapiv2.ApiClient(configuration))
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the System Group's membership
    api_response = api_instance.graph_system_group_membership(group_id, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemGroupMembersMembershipApi->graph_system_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

