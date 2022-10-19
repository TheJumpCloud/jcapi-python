# jcapiv2.BulkJobRequestsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_user_states_create**](BulkJobRequestsApi.md#bulk_user_states_create) | **POST** /bulk/userstates | Create Scheduled Userstate Job
[**bulk_user_states_delete**](BulkJobRequestsApi.md#bulk_user_states_delete) | **DELETE** /bulk/userstates/{id} | Delete Scheduled Userstate Job
[**bulk_user_states_get_next_scheduled**](BulkJobRequestsApi.md#bulk_user_states_get_next_scheduled) | **GET** /bulk/userstates/eventlist/next | Gets the next scheduled state change for each user in a list of system users
[**bulk_user_states_list**](BulkJobRequestsApi.md#bulk_user_states_list) | **GET** /bulk/userstates | List Scheduled Userstate Change Jobs
[**bulk_users_create**](BulkJobRequestsApi.md#bulk_users_create) | **POST** /bulk/users | Bulk Users Create
[**bulk_users_create_results**](BulkJobRequestsApi.md#bulk_users_create_results) | **GET** /bulk/users/{job_id}/results | List Bulk Users Results
[**bulk_users_update**](BulkJobRequestsApi.md#bulk_users_update) | **PATCH** /bulk/users | Bulk Users Update

# **bulk_user_states_create**
> list[ScheduledUserstateResult] bulk_user_states_create(body=body, x_org_id=x_org_id)

Create Scheduled Userstate Job

This endpoint allows you to create scheduled statechange jobs. #### Sample Request ``` curl -X POST \"https://console.jumpcloud.com/api/v2/bulk/userstates\" \\   -H 'x-api-key: {API_KEY}' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' \\   -d '{     \"user_ids\": [\"{User_ID_1}\", \"{User_ID_2}\", \"{User_ID_3}\"],     \"state\": \"SUSPENDED\",     \"start_date\": \"2000-01-01T00:00:00.000Z\"   }' ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.BulkScheduledStatechangeCreate() # BulkScheduledStatechangeCreate |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create Scheduled Userstate Job
    api_response = api_instance.bulk_user_states_create(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_user_states_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkScheduledStatechangeCreate**](BulkScheduledStatechangeCreate.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[ScheduledUserstateResult]**](ScheduledUserstateResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_states_delete**
> bulk_user_states_delete(id, x_org_id=x_org_id)

Delete Scheduled Userstate Job

This endpoint deletes a scheduled statechange job. #### Sample Request ``` curl -X DELETE \"https://console.jumpcloud.com/api/v2/bulk/userstates/{ScheduledJob_ID}\" \\   -H 'x-api-key: {API_KEY}' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the scheduled statechange job.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete Scheduled Userstate Job
    api_instance.bulk_user_states_delete(id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_user_states_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the scheduled statechange job. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_states_get_next_scheduled**
> InlineResponse200 bulk_user_states_get_next_scheduled(users, limit=limit, skip=skip)

Gets the next scheduled state change for each user in a list of system users

This endpoint is used to lookup the next upcoming scheduled state change for each user in the given list. The users parameter is limited to 100 items per request. #### Sample Request ``` curl -X GET \"https://console.jumpcloud.com/api/v2/bulk/userstates/eventlist/next?users={UserID1},{UserID2},{UserID3}\" \\   -H 'x-api-key: {API_KEY}' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
users = ['users_example'] # list[str] | A list of system user IDs
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # Gets the next scheduled state change for each user in a list of system users
    api_response = api_instance.bulk_user_states_get_next_scheduled(users, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_user_states_get_next_scheduled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users** | [**list[str]**](str.md)| A list of system user IDs | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_user_states_list**
> list[ScheduledUserstateResult] bulk_user_states_list(limit=limit, filter=filter, skip=skip, x_org_id=x_org_id, userid=userid)

List Scheduled Userstate Change Jobs

The endpoint allows you to list scheduled statechange jobs. #### Sample Request ``` curl -X GET \"https://console.jumpcloud.com/api/v2/bulk/userstates\" \\   -H 'x-api-key: {API_KEY}' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
userid = 'userid_example' # str | The systemuser id to filter by. (optional)

try:
    # List Scheduled Userstate Change Jobs
    api_response = api_instance.bulk_user_states_list(limit=limit, filter=filter, skip=skip, x_org_id=x_org_id, userid=userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_user_states_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **userid** | **str**| The systemuser id to filter by. | [optional] 

### Return type

[**list[ScheduledUserstateResult]**](ScheduledUserstateResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_users_create**
> JobId bulk_users_create(body=body, x_org_id=x_org_id, creation_source=creation_source)

Bulk Users Create

The endpoint allows you to create a bulk job to asynchronously create users. See [Create a System User](https://docs.jumpcloud.com/api/1.0/index.html#operation/systemusers_post) for the full list of attributes.  #### Default User State The `state` of each user in the request can be explicitly passed in or omitted. If `state` is omitted, then the user will get created using the value returned from the [Get an Organization](https://docs.jumpcloud.com/api/1.0/index.html#operation/organizations_get) endpoint. The default user state for bulk created users depends on the `creation-source` header. For `creation-source:jumpcloud:bulk` the default state is stored in `settings.newSystemUserStateDefaults.csvImport`. For other `creation-source` header values, the default state is stored in `settings.newSystemUserStateDefaults.applicationImport`  These default state values can be changed in the admin portal settings or by using the [Update an Organization](https://docs.jumpcloud.com/api/1.0/index.html#operation/organization_put) endpoint.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/bulk/users \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '[   {     \"email\":\"{email}\",     \"firstname\":\"{firstname}\",     \"lastname\":\"{firstname}\",     \"username\":\"{username}\",     \"attributes\":[       {         \"name\":\"EmployeeID\",         \"value\":\"0000\"       },       {         \"name\":\"Custom\",         \"value\":\"attribute\"       }     ]   } ]' ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
body = [jcapiv2.BulkUserCreate()] # list[BulkUserCreate] |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
creation_source = 'jumpcloud:bulk' # str | Defines the creation-source header for gapps, o365 and workdays requests. If the header isn't sent, the default value is `jumpcloud:bulk`, if you send the header with a malformed value you receive a 400 error.  (optional) (default to jumpcloud:bulk)

try:
    # Bulk Users Create
    api_response = api_instance.bulk_users_create(body=body, x_org_id=x_org_id, creation_source=creation_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BulkUserCreate]**](BulkUserCreate.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **creation_source** | **str**| Defines the creation-source header for gapps, o365 and workdays requests. If the header isn&#x27;t sent, the default value is &#x60;jumpcloud:bulk&#x60;, if you send the header with a malformed value you receive a 400 error.  | [optional] [default to jumpcloud:bulk]

### Return type

[**JobId**](JobId.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_users_create_results**
> list[JobWorkresult] bulk_users_create_results(job_id, limit=limit, skip=skip, x_org_id=x_org_id)

List Bulk Users Results

This endpoint will return the results of particular user import or update job request.  #### Sample Request ``` curl -X GET \\   https://console.jumpcloud.com/api/v2/bulk/users/{ImportJobID}/results \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
job_id = 'job_id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Bulk Users Results
    api_response = api_instance.bulk_users_create_results(job_id, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_users_create_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[JobWorkresult]**](JobWorkresult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_users_update**
> JobId bulk_users_update(body=body, x_org_id=x_org_id)

Bulk Users Update

The endpoint allows you to create a bulk job to asynchronously update users. See [Update a System User](https://docs.jumpcloud.com/api/1.0/index.html#operation/systemusers_put) for full list of attributes.  #### Sample Request  ``` curl -X PATCH https://console.jumpcloud.com/api/v2/bulk/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '[  {    \"id\":\"5be9fb4ddb01290001e85109\",   \"firstname\":\"{UPDATED_FIRSTNAME}\",   \"department\":\"{UPDATED_DEPARTMENT}\",   \"attributes\":[    {\"name\":\"Custom\",\"value\":\"{ATTRIBUTE_VALUE}\"}   ]  },  {    \"id\":\"5be9fb4ddb01290001e85109\",   \"firstname\":\"{UPDATED_FIRSTNAME}\",   \"costCenter\":\"{UPDATED_COST_CENTER}\",   \"phoneNumbers\":[    {\"type\":\"home\",\"number\":\"{HOME_PHONE_NUMBER}\"},    {\"type\":\"work\",\"number\":\"{WORK_PHONE_NUMBER}\"}   ]  } ] ```

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
api_instance = jcapiv2.BulkJobRequestsApi(jcapiv2.ApiClient(configuration))
body = [jcapiv2.BulkUserUpdate()] # list[BulkUserUpdate] |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Bulk Users Update
    api_response = api_instance.bulk_users_update(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkJobRequestsApi->bulk_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BulkUserUpdate]**](BulkUserUpdate.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**JobId**](JobId.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

