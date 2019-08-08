# jcapiv2.UsersApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_user_associations_list**](UsersApi.md#graph_user_associations_list) | **GET** /users/{user_id}/associations | List the associations of a User
[**graph_user_associations_post**](UsersApi.md#graph_user_associations_post) | **POST** /users/{user_id}/associations | Manage the associations of a User
[**graph_user_member_of**](UsersApi.md#graph_user_member_of) | **GET** /users/{user_id}/memberof | List the parent Groups of a User
[**graph_user_traverse_application**](UsersApi.md#graph_user_traverse_application) | **GET** /users/{user_id}/applications | List the Applications bound to a User
[**graph_user_traverse_directory**](UsersApi.md#graph_user_traverse_directory) | **GET** /users/{user_id}/directories | List the Directories bound to a User
[**graph_user_traverse_g_suite**](UsersApi.md#graph_user_traverse_g_suite) | **GET** /users/{user_id}/gsuites | List the G Suite instances bound to a User
[**graph_user_traverse_ldap_server**](UsersApi.md#graph_user_traverse_ldap_server) | **GET** /users/{user_id}/ldapservers | List the LDAP servers bound to a User
[**graph_user_traverse_office365**](UsersApi.md#graph_user_traverse_office365) | **GET** /users/{user_id}/office365s | List the Office 365 instances bound to a User
[**graph_user_traverse_radius_server**](UsersApi.md#graph_user_traverse_radius_server) | **GET** /users/{user_id}/radiusservers | List the RADIUS Servers bound to a User
[**graph_user_traverse_system**](UsersApi.md#graph_user_traverse_system) | **GET** /users/{user_id}/systems | List the Systems bound to a User
[**graph_user_traverse_system_group**](UsersApi.md#graph_user_traverse_system_group) | **GET** /users/{user_id}/systemgroups | List the System Groups bound to a User
[**users_send_emails**](UsersApi.md#users_send_emails) | **POST** /users/{user_id}/emails | Send User Emails


# **graph_user_associations_list**
> list[GraphConnection] graph_user_associations_list(user_id, content_type, accept, targets, limit=limit, skip=skip, x_org_id=x_org_id)

List the associations of a User

This endpoint returns the _direct_ associations of a User.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Users and Systems.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/associations?targets=system_group \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = '' # str |  (optional) (default to )

try:
    # List the associations of a User
    api_response = api_instance.graph_user_associations_list(user_id, content_type, accept, targets, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_associations_post**
> graph_user_associations_post(user_id, content_type, accept, body=body, x_org_id=x_org_id)

Manage the associations of a User

This endpoint allows you to manage the _direct_ associations of a User.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Users and Systems.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/users/{UserID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{    \"attributes\": {       \"sudo\": {          \"enabled\": true,          \"withoutPassword\": false       }    },    \"op\": \"add\",    \"type\": \"system_group\",    \"id\": \"{GroupID}\" }'

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.UserGraphManagementReq() # UserGraphManagementReq |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Manage the associations of a User
    api_instance.graph_user_associations_post(user_id, content_type, accept, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**UserGraphManagementReq**](UserGraphManagementReq.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_member_of**
> list[GraphObjectWithPaths] graph_user_member_of(user_id, content_type, accept, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)

List the parent Groups of a User

This endpoint returns all the User Groups a User is a member of.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/memberof \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])
x_org_id = '' # str |  (optional) (default to )

try:
    # List the parent Groups of a User
    api_response = api_instance.graph_user_member_of(user_id, content_type, accept, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_application**
> list[GraphObjectWithPaths] graph_user_traverse_application(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Applications bound to a User

This endpoint will return all Applications bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Application; this array represents all grouping and/or associations that would have to be removed to deprovision the Application from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/applications \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the Applications bound to a User
    api_response = api_instance.graph_user_traverse_application(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_directory**
> list[GraphObjectWithPaths] graph_user_traverse_directory(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Directories bound to a User

This endpoint will return all Directories bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Directory; this array represents all grouping and/or associations that would have to be removed to deprovision the Directory from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/directories \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the Directories bound to a User
    api_response = api_instance.graph_user_traverse_directory(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_g_suite**
> list[GraphObjectWithPaths] graph_user_traverse_g_suite(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the G Suite instances bound to a User

This endpoint will return all G-Suite Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding G Suite instance; this array represents all grouping and/or associations that would have to be removed to deprovision the G Suite instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/gsuites \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the G Suite instances bound to a User
    api_response = api_instance.graph_user_traverse_g_suite(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_g_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_ldap_server**
> list[GraphObjectWithPaths] graph_user_traverse_ldap_server(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the LDAP servers bound to a User

This endpoint will return all LDAP Servers bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding LDAP Server; this array represents all grouping and/or associations that would have to be removed to deprovision the LDAP Server from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/ldapservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the LDAP servers bound to a User
    api_response = api_instance.graph_user_traverse_ldap_server(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_office365**
> list[GraphObjectWithPaths] graph_user_traverse_office365(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Office 365 instances bound to a User

This endpoint will return all Office 365 Instances bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding Office 365 instance; this array represents all grouping and/or associations that would have to be removed to deprovision the Office 365 instance from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/office365s \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the Office 365 instances bound to a User
    api_response = api_instance.graph_user_traverse_office365(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_office365: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_radius_server**
> list[GraphObjectWithPaths] graph_user_traverse_radius_server(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the RADIUS Servers bound to a User

This endpoint will return all RADIUS Servers bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding RADIUS Server; this array represents all grouping and/or associations that would have to be removed to deprovision the RADIUS Server from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/radiusservers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the RADIUS Servers bound to a User
    api_response = api_instance.graph_user_traverse_radius_server(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_system**
> list[GraphObjectWithPaths] graph_user_traverse_system(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Systems bound to a User

This endpoint will return all Systems bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/systems\\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the Systems bound to a User
    api_response = api_instance.graph_user_traverse_system(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_user_traverse_system_group**
> list[GraphObjectWithPaths] graph_user_traverse_system_group(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the System Groups bound to a User

This endpoint will return all System Groups bound to a User, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this User to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this User.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/users/{UserID}/systemgroups\\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = '' # str |  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])

try:
    # List the System Groups bound to a User
    api_response = api_instance.graph_user_traverse_system_group(user_id, content_type, accept, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->graph_user_traverse_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**|  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_send_emails**
> users_send_emails(user_id, content_type, accept, body=body, x_org_id=x_org_id)

Send User Emails

This endpoint allows you to send a specific email to a user without waiting for or triggering a workflow.

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
api_instance = jcapiv2.UsersApi(jcapiv2.ApiClient(configuration))
user_id = 'user_id_example' # str | ObjectID of the User.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.Emailrequest() # Emailrequest |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Send User Emails
    api_instance.users_send_emails(user_id, content_type, accept, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_send_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Emailrequest**](Emailrequest.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

