# jcapiv2.GraphApi

All URIs are relative to *http://localhost:3004/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_associations_list**](GraphApi.md#application_associations_list) | **GET** /applications/{application_id}/associations | List associations of a application
[**application_associations_post**](GraphApi.md#application_associations_post) | **POST** /applications/{application_id}/associations | Manage associations of an Application
[**application_server_traverse_user**](GraphApi.md#application_server_traverse_user) | **GET** /applications/{application_id}/users | Get the Users an Application is associated with.
[**application_traverse_user_groups**](GraphApi.md#application_traverse_user_groups) | **GET** /applications/{application_id}/usergroups | Get the User Groups an Application is associated with.
[**command_associations_list**](GraphApi.md#command_associations_list) | **GET** /commands/{command_id}/associations | List associations of a command
[**command_associations_post**](GraphApi.md#command_associations_post) | **POST** /commands/{command_id}/associations | Manage associations of a Command
[**command_traverse_system**](GraphApi.md#command_traverse_system) | **GET** /commands/{command_id}/systems | Get the Systems an Command is associated with.
[**command_traverse_system_group**](GraphApi.md#command_traverse_system_group) | **GET** /commands/{command_id}/systemgroups | Get the System Groups an Command is associated with.
[**g_suite_associations_list**](GraphApi.md#g_suite_associations_list) | **GET** /gsuites/{gsuite_id}/associations | List associations of a G Suite instance.
[**g_suite_associations_post**](GraphApi.md#g_suite_associations_post) | **POST** /gsuites/{gsuite_id}/associations | Manage associations of a G Suite instance.
[**g_suite_traverse_user**](GraphApi.md#g_suite_traverse_user) | **GET** /gsuites/{gsuite_id}/users | Get the Users a G Suite instance is associated with.
[**g_suite_traverse_user_group**](GraphApi.md#g_suite_traverse_user_group) | **GET** /gsuites/{gsuite_id}/usergroups | Get the User Groups a G Suite instance is associated with.
[**ldap_server_associations_list**](GraphApi.md#ldap_server_associations_list) | **GET** /ldapservers/{ldapserver_id}/associations | List associations of a LDAP Server
[**ldap_server_associations_post**](GraphApi.md#ldap_server_associations_post) | **POST** /ldapservers/{ldapserver_id}/associations | Manage associations of a LDAP Server
[**ldap_server_traverse_user**](GraphApi.md#ldap_server_traverse_user) | **GET** /ldapservers/{ldapserver_id}/users | Get the Users a LDAP Server is associated with.
[**ldap_server_traverse_user_group**](GraphApi.md#ldap_server_traverse_user_group) | **GET** /ldapservers/{ldapserver_id}/usergroups | Get the User Groups a LDAP Server is associated with.
[**office365_associations_list**](GraphApi.md#office365_associations_list) | **GET** /office365s/{office365_id}/associations | List associations of a Office 365 instance.
[**office365_associations_post**](GraphApi.md#office365_associations_post) | **POST** /office365s/{office365_id}/associations | Manage associations of a Office 365 suite.
[**office365_traverse_user**](GraphApi.md#office365_traverse_user) | **GET** /office365s/{office365_id}/users | Get the Users a Office 365 instance is associated with.
[**office365_traverse_user_group**](GraphApi.md#office365_traverse_user_group) | **GET** /office365s/{office365_id}/usergroups | Get the User Groups a Office 365 instance is associated with.
[**radius_server_associations_list**](GraphApi.md#radius_server_associations_list) | **GET** /radiusservers/{radiusserver_id}/associations | List associations of a Radius Server
[**radius_server_associations_post**](GraphApi.md#radius_server_associations_post) | **POST** /radiusservers/{radiusserver_id}/associations | Manage associations of a Radius Server
[**radius_server_traverse_user**](GraphApi.md#radius_server_traverse_user) | **GET** /radiusservers/{radiusserver_id}/users | Get the Users a Radius Server is associated with.
[**radius_server_traverse_user_group**](GraphApi.md#radius_server_traverse_user_group) | **GET** /radiusservers/{radiusserver_id}/usergroups | Get the User Groups a Radius Server is associated with.
[**system_associations_list**](GraphApi.md#system_associations_list) | **GET** /systems/{system_id}/associations | List associations of a System
[**system_associations_post**](GraphApi.md#system_associations_post) | **POST** /systems/{system_id}/associations | Manage associations of a System
[**system_group_associations_list**](GraphApi.md#system_group_associations_list) | **GET** /systemgroups/{group_id}/associations | List associations of a System Group.
[**system_group_associations_post**](GraphApi.md#system_group_associations_post) | **POST** /systemgroups/{group_id}/associations | Manage associations of a System Group
[**system_group_member_of**](GraphApi.md#system_group_member_of) | **GET** /systemgroups/{group_id}/memberof | Get System Group&#39;s groups it is a member of.
[**system_group_members_list**](GraphApi.md#system_group_members_list) | **GET** /systemgroups/{group_id}/members | List members of a System Group
[**system_group_membership**](GraphApi.md#system_group_membership) | **GET** /systemgroups/{group_id}/membership | Get System and System Group&#39;s who are members of this group.
[**system_group_traverse_user**](GraphApi.md#system_group_traverse_user) | **GET** /systemgroups/{group_id}/users | Get the Users a System Group is associated with.
[**system_group_traverse_user_group**](GraphApi.md#system_group_traverse_user_group) | **GET** /systemgroups/{group_id}/usergroups | Get the User Groups a System Group is associated with.
[**system_member_of**](GraphApi.md#system_member_of) | **GET** /systems/{system_id}/memberof | Get System&#39;s groups it is a member of.
[**system_traverse_user**](GraphApi.md#system_traverse_user) | **GET** /systems/{system_id}/users | Get the Users a System is associated with.
[**user_associations_list**](GraphApi.md#user_associations_list) | **GET** /users/{user_id}/associations | List associations of a User.
[**user_associations_post**](GraphApi.md#user_associations_post) | **POST** /users/{user_id}/associations | Manage associations of a User
[**user_group_associations_list**](GraphApi.md#user_group_associations_list) | **GET** /usergroups/{group_id}/associations | List associations of a User Group.
[**user_group_associations_post**](GraphApi.md#user_group_associations_post) | **POST** /usergroups/{group_id}/associations | Manage associations of a User Group
[**user_group_member_of**](GraphApi.md#user_group_member_of) | **GET** /usergroups/{group_id}/memberof | Get User Group&#39;s groups it is a member of.
[**user_group_members_list**](GraphApi.md#user_group_members_list) | **GET** /usergroups/{group_id}/members | List members of a User Group
[**user_group_members_post**](GraphApi.md#user_group_members_post) | **POST** /usergroups/{group_id}/members | Manage members of a User Group
[**user_group_membership**](GraphApi.md#user_group_membership) | **GET** /usergroups/{group_id}/membership | Get User and User Group&#39;s who are members of this group.
[**user_group_traverse_application**](GraphApi.md#user_group_traverse_application) | **GET** /usergroups/{group_id}/applications | Get the Applications a User Group is associated with.
[**user_group_traverse_directory**](GraphApi.md#user_group_traverse_directory) | **GET** /usergroups/{group_id}/directories | Get the Directories a User Group is associated with.
[**user_group_traverse_g_suite**](GraphApi.md#user_group_traverse_g_suite) | **GET** /usergroups/{group_id}/gsuites | Get the G Suite instance a User Group is associated with.
[**user_group_traverse_ldap_server**](GraphApi.md#user_group_traverse_ldap_server) | **GET** /usergroups/{group_id}/ldapservers | Get the LDAP Servers a User Group is associated with.
[**user_group_traverse_office365**](GraphApi.md#user_group_traverse_office365) | **GET** /usergroups/{group_id}/office365s | Get the Office 365 instance a User Group is associated with.
[**user_group_traverse_radius_server**](GraphApi.md#user_group_traverse_radius_server) | **GET** /usergroups/{group_id}/radiusservers | Get the Radius Servers a User Group is associated with.
[**user_group_traverse_system**](GraphApi.md#user_group_traverse_system) | **GET** /usergroups/{group_id}/systems | Get the Systems a User Group is associated with.
[**user_group_traverse_system_group**](GraphApi.md#user_group_traverse_system_group) | **GET** /usergroups/{group_id}/systemgroups | Get the System Groups a User Group is associatedwith.
[**user_member_of**](GraphApi.md#user_member_of) | **GET** /users/{user_id}/memberof | Get Users&#39;s groups it is a member of.
[**user_traverse_application**](GraphApi.md#user_traverse_application) | **GET** /users/{user_id}/applications | Get the Applications a User is associated with.
[**user_traverse_directory**](GraphApi.md#user_traverse_directory) | **GET** /users/{user_id}/directories | Get the Directories a User is associated with.
[**user_traverse_g_suite**](GraphApi.md#user_traverse_g_suite) | **GET** /users/{user_id}/gsuites | Get the G Suite instance a User is associated with.
[**user_traverse_ldap_server**](GraphApi.md#user_traverse_ldap_server) | **GET** /users/{user_id}/ldapservers | Get the LDAP Servers a User is associated with.
[**user_traverse_office365**](GraphApi.md#user_traverse_office365) | **GET** /users/{user_id}/office365s | Get the Office 365 instance a User is associated with.
[**user_traverse_radius_server**](GraphApi.md#user_traverse_radius_server) | **GET** /users/{user_id}/radiusservers | Get the Radius Servers a User is associated with.
[**user_traverse_system**](GraphApi.md#user_traverse_system) | **GET** /users/{user_id}/systems | Get the Systems a User is associated with.


# **application_associations_list**
> list[GraphConnection] application_associations_list(application_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a application

This lists the _direct_ associations of this Application. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
application_id = 'application_id_example' # str | ObjectID of the Application.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a application
    api_response = api_instance.application_associations_list(application_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->application_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| ObjectID of the Application. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_associations_post**
> application_associations_post(application_id, body)

Manage associations of an Application

This manages the _direct_ associations of an Application 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
application_id = 'application_id_example' # str | ObjectID of the Application.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of an Application
    api_instance.application_associations_post(application_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->application_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| ObjectID of the Application. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_server_traverse_user**
> list[GraphObjectWithPaths] application_server_traverse_user(application_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users an Application is associated with.

**read-only**  This endpoint follows the grouping and associations from this Application to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this Application to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this Application. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
application_id = 'application_id_example' # str | ObjectID of the Application.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users an Application is associated with.
    api_response = api_instance.application_server_traverse_user(application_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->application_server_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| ObjectID of the Application. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_traverse_user_groups**
> list[GraphObjectWithPaths] application_traverse_user_groups(application_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the User Groups an Application is associated with.

**read-only**  This endpoint follows the grouping and associations from this Application to any User Groups it is connected to. It is arranged as a hash of User Group IDs for easy lookup.  It also contains a `path` array that describes each path from this Application to the corresponding User Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that User Group from this Application. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
application_id = 'application_id_example' # str | ObjectID of the Application.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the User Groups an Application is associated with.
    api_response = api_instance.application_traverse_user_groups(application_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->application_traverse_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| ObjectID of the Application. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_associations_list**
> list[GraphConnection] command_associations_list(command_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a command

This lists the _direct_ associations of this Command. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a command
    api_response = api_instance.command_associations_list(command_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->command_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_associations_post**
> command_associations_post(command_id, body)

Manage associations of a Command

This manages the _direct_ associations of a Command 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a Command
    api_instance.command_associations_post(command_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->command_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_traverse_system**
> list[GraphObjectWithPaths] command_traverse_system(command_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Systems an Command is associated with.

**read-only**  This endpoint follows the grouping and associations from this Command to any Systems it is connected to. It is arranged as a hash of System IDs for easy lookup.  It also contains a `path` array that describes each path from this Command to the corresponding System; this array reprents all grouping and/or associations that would have to be removed to deprovision that System from this Command. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Systems an Command is associated with.
    api_response = api_instance.command_traverse_system(command_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->command_traverse_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **command_traverse_system_group**
> list[GraphObjectWithPaths] command_traverse_system_group(command_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the System Groups an Command is associated with.

**read-only**  This endpoint follows the grouping and associations from this Command to any System Groups it is connected to. It is arranged as a hash of System Group IDs for easy lookup.  It also contains a `path` array that describes each path from this Command to the corresponding System Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that System Group from this Command. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
command_id = 'command_id_example' # str | ObjectID of the Command.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the System Groups an Command is associated with.
    api_response = api_instance.command_traverse_system_group(command_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->command_traverse_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command_id** | **str**| ObjectID of the Command. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_suite_associations_list**
> list[GraphConnection] g_suite_associations_list(gsuite_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a G Suite instance.

This lists the _direct_ associations of this G Suite instance. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a G Suite instance.
    api_response = api_instance.g_suite_associations_list(gsuite_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->g_suite_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_suite_associations_post**
> g_suite_associations_post(gsuite_id, body)

Manage associations of a G Suite instance.

This manages the _direct_ associations of a G Suite instance. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a G Suite instance.
    api_instance.g_suite_associations_post(gsuite_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->g_suite_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_suite_traverse_user**
> list[GraphObjectWithPaths] g_suite_traverse_user(gsuite_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users a G Suite instance is associated with.

**read-only**  This endpoint follows the grouping and associations from this G Suite instance to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this G Suite instance to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this G Suite instance. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users a G Suite instance is associated with.
    api_response = api_instance.g_suite_traverse_user(gsuite_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->g_suite_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_suite_traverse_user_group**
> list[GraphObjectWithPaths] g_suite_traverse_user_group(gsuite_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the User Groups a G Suite instance is associated with.

**read-only**  This endpoint follows the grouping and associations from this G Suite instance to any User Groups it is connected to. It is arranged as a hash of User Group IDs for easy lookup.  It also contains a `path` array that describes each path from this G Suite instance to the corresponding User Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that User Group from this G Suite instance. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the User Groups a G Suite instance is associated with.
    api_response = api_instance.g_suite_traverse_user_group(gsuite_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->g_suite_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_server_associations_list**
> list[GraphConnection] ldap_server_associations_list(ldapserver_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a LDAP Server

This lists the _direct_ associations of this LDAP Server. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a LDAP Server
    api_response = api_instance.ldap_server_associations_list(ldapserver_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->ldap_server_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_server_associations_post**
> ldap_server_associations_post(ldapserver_id, body)

Manage associations of a LDAP Server

This manages the _direct_ associations of a LDAP Server 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a LDAP Server
    api_instance.ldap_server_associations_post(ldapserver_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->ldap_server_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_server_traverse_user**
> list[GraphObjectWithPaths] ldap_server_traverse_user(ldapserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users a LDAP Server is associated with.

**read-only**  This endpoint follows the grouping and associations from this LDAP Server to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this LDAP Server to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this LDAP Server. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users a LDAP Server is associated with.
    api_response = api_instance.ldap_server_traverse_user(ldapserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->ldap_server_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_server_traverse_user_group**
> list[GraphObjectWithPaths] ldap_server_traverse_user_group(ldapserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the User Groups a LDAP Server is associated with.

**read-only**  This endpoint follows the grouping and associations from this LDAP Server to any User Groups it is connected to. It is arranged as a hash of User Group IDs for easy lookup.  It also contains a `path` array that describes each path from this LDAP Server to the corresponding User Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that User Group from this LDAP Server. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the User Groups a LDAP Server is associated with.
    api_response = api_instance.ldap_server_traverse_user_group(ldapserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->ldap_server_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office365_associations_list**
> list[GraphConnection] office365_associations_list(office365_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a Office 365 instance.

This lists the _direct_ associations of this Office 365 instance. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a Office 365 instance.
    api_response = api_instance.office365_associations_list(office365_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->office365_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office365_associations_post**
> office365_associations_post(office365_id, body)

Manage associations of a Office 365 suite.

This manages the _direct_ associations of a Office 365 suite. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a Office 365 suite.
    api_instance.office365_associations_post(office365_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->office365_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office365_traverse_user**
> list[GraphObjectWithPaths] office365_traverse_user(office365_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users a Office 365 instance is associated with.

**read-only**  This endpoint follows the grouping and associations from this Office 365 instance to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this Office 365 instance to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this Office 365 instance. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 suite.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users a Office 365 instance is associated with.
    api_response = api_instance.office365_traverse_user(office365_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->office365_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 suite. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office365_traverse_user_group**
> list[GraphObjectWithPaths] office365_traverse_user_group(office365_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the User Groups a Office 365 instance is associated with.

**read-only**  This endpoint follows the grouping and associations from this Office 365 instance to any User Groups it is connected to. It is arranged as a hash of User Group IDs for easy lookup.  It also contains a `path` array that describes each path from this Office 365 instance to the corresponding User Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that User Group from this Office 365 instance. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 suite.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the User Groups a Office 365 instance is associated with.
    api_response = api_instance.office365_traverse_user_group(office365_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->office365_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 suite. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radius_server_associations_list**
> list[GraphConnection] radius_server_associations_list(radiusserver_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a Radius Server

This lists the _direct_ associations of this Radius Server. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
radiusserver_id = 'radiusserver_id_example' # str | ObjectID of the Radius Server.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a Radius Server
    api_response = api_instance.radius_server_associations_list(radiusserver_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->radius_server_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radiusserver_id** | **str**| ObjectID of the Radius Server. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radius_server_associations_post**
> radius_server_associations_post(radiusserver_id, body)

Manage associations of a Radius Server

This manages the _direct_ associations of a Radius Server 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
radiusserver_id = 'radiusserver_id_example' # str | ObjectID of the Radius Server.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a Radius Server
    api_instance.radius_server_associations_post(radiusserver_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->radius_server_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radiusserver_id** | **str**| ObjectID of the Radius Server. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radius_server_traverse_user**
> list[GraphObjectWithPaths] radius_server_traverse_user(radiusserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users a Radius Server is associated with.

**read-only**  This endpoint follows the grouping and associations from this Radius Server to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this Radius Server to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this Radius Server. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
radiusserver_id = 'radiusserver_id_example' # str | ObjectID of the Radius Server.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users a Radius Server is associated with.
    api_response = api_instance.radius_server_traverse_user(radiusserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->radius_server_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radiusserver_id** | **str**| ObjectID of the Radius Server. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radius_server_traverse_user_group**
> list[GraphObjectWithPaths] radius_server_traverse_user_group(radiusserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the User Groups a Radius Server is associated with.

**read-only**  This endpoint follows the grouping and associations from this Radius Server to any User Groups it is connected to. It is arranged as a hash of User Group IDs for easy lookup.  It also contains a `path` array that describes each path from this Radius Server to the corresponding User Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that User Group from this Radius Server. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
radiusserver_id = 'radiusserver_id_example' # str | ObjectID of the Radius Server.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the User Groups a Radius Server is associated with.
    api_response = api_instance.radius_server_traverse_user_group(radiusserver_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->radius_server_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radiusserver_id** | **str**| ObjectID of the Radius Server. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_associations_list**
> list[GraphConnection] system_associations_list(system_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a System

This lists the _direct_ associations of this System. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
system_id = 'system_id_example' # str | ObjectID of the System.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a System
    api_response = api_instance.system_associations_list(system_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_associations_post**
> system_associations_post(system_id, body)

Manage associations of a System

This manages the _direct_ associations (non-Systems and System Groups) of a system. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
system_id = 'system_id_example' # str | ObjectID of the System.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a System
    api_instance.system_associations_post(system_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->system_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_associations_list**
> list[GraphConnection] system_group_associations_list(group_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a System Group.

This lists the _direct_ associations of this System Group. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a System Group.
    api_response = api_instance.system_group_associations_list(group_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_associations_post**
> system_group_associations_post(group_id, body)

Manage associations of a System Group

This manages the _direct_ associations (non-Systems and System Groups) of a group. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a System Group
    api_instance.system_group_associations_post(group_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_associations_post: %s\n" % e)
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

# **system_group_member_of**
> list[GraphObjectWithPaths] system_group_member_of(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get System Group's groups it is a member of.

This lists all groups a system group is a member of. That is to say it includes nested group member of relationships as well. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get System Group's groups it is a member of.
    api_response = api_instance.system_group_member_of(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_members_list**
> list[GraphConnection] system_group_members_list(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List members of a System Group

This lists the _direct_ children (Systems and System Groups) of this group. That is to say it does not recurse through children groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List members of a System Group
    api_response = api_instance.system_group_members_list(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_members_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_membership**
> list[GraphObjectWithPaths] system_group_membership(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get System and System Group's who are members of this group.

This lists all the systems and system groups that are a member of this system group. That is to say it includes nested group members of relationships as well. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get System and System Group's who are members of this group.
    api_response = api_instance.system_group_membership(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_traverse_user**
> list[GraphObjectWithPaths] system_group_traverse_user(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users a System Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this System Group to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this System Group to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this System Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users a System Group is associated with.
    api_response = api_instance.system_group_traverse_user(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_group_traverse_user_group**
> list[GraphObjectWithPaths] system_group_traverse_user_group(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the User Groups a System Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this System Group to any User Groups it is connected to. It is arranged as a hash of User Group IDs for easy lookup.  It also contains a `path` array that describes each path from this System Group to the corresponding User Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that User Group from this System Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the System Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the User Groups a System Group is associated with.
    api_response = api_instance.system_group_traverse_user_group(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_group_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the System Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_member_of**
> list[GraphObjectWithPaths] system_member_of(system_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get System's groups it is a member of.

This lists all groups a system is a member of. That is to say it includes nested group member of relationships as well. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
system_id = 'system_id_example' # str | ObjectID of the System.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get System's groups it is a member of.
    api_response = api_instance.system_member_of(system_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_traverse_user**
> list[GraphObjectWithPaths] system_traverse_user(system_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Users a System is associated with.

**read-only**  This endpoint follows the grouping and associations from this System to any Users it is connected to. It is arranged as a hash of User IDs for easy lookup.  It also contains a `path` array that describes each path from this System to the corresponding User; this array reprents all grouping and/or associations that would have to be removed to deprovision that User from this System. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
system_id = 'system_id_example' # str | ObjectID of the System.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Users a System is associated with.
    api_response = api_instance.system_traverse_user(system_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->system_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ObjectID of the System. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_associations_list**
> list[GraphConnection] user_associations_list(user_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a User.

This lists the _direct_ associations of this User. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a User.
    api_response = api_instance.user_associations_list(user_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_associations_post**
> user_associations_post(user_id, body)

Manage associations of a User

This manages the _direct_ associations (non-Users and User Groups) of a user. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a User
    api_instance.user_associations_post(user_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->user_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_associations_list**
> list[GraphConnection] user_group_associations_list(group_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List associations of a User Group.

This lists the _direct_ associations of this User Group. That is to say it does not traverse through Groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
targets = ['targets_example'] # list[str] | 
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List associations of a User Group.
    api_response = api_instance.user_group_associations_list(group_id, targets, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **targets** | [**list[str]**](str.md)|  | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_associations_post**
> user_group_associations_post(group_id, body)

Manage associations of a User Group

This manages the _direct_ associations (non-Users and User Groups) of a group. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage associations of a User Group
    api_instance.user_group_associations_post(group_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_member_of**
> list[GraphObjectWithPaths] user_group_member_of(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get User Group's groups it is a member of.

This lists all groups a User Group is a member of. That is to say it includes nested group member of relationships as well. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get User Group's groups it is a member of.
    api_response = api_instance.user_group_member_of(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_members_list**
> list[GraphConnection] user_group_members_list(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

List members of a User Group

This lists the _direct_ children (Users and User Groups) of this group. That is to say it does not recurse through children groups.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # List members of a User Group
    api_response = api_instance.user_group_members_list(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_members_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphConnection]**](GraphConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_members_post**
> user_group_members_post(group_id, body)

Manage members of a User Group

This manages the _direct_ children (Users and User Groups) of a group.  A User Group can contain Users and User Groups. No cycles are allowed; i.e.  if Group A contains Group B then Group B cannot also contain Group A, including any deeper nested relationships. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
body = jcapiv2.GraphManagementReq() # GraphManagementReq | 

try: 
    # Manage members of a User Group
    api_instance.user_group_members_post(group_id, body)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **body** | [**GraphManagementReq**](GraphManagementReq.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_membership**
> list[GraphObjectWithPaths] user_group_membership(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get User and User Group's who are members of this group.

This lists all the users and user groups that are a member of this user group. That is to say it includes nested group members of relationships as well. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get User and User Group's who are members of this group.
    api_response = api_instance.user_group_membership(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_application**
> list[GraphObjectWithPaths] user_group_traverse_application(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Applications a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any Applications it is connected to. It is arranged as a hash of Application IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding Application; this array reprents all grouping and/or associations that would have to be removed to deprovision that Application from this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Applications a User Group is associated with.
    api_response = api_instance.user_group_traverse_application(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_directory**
> list[GraphObjectWithPaths] user_group_traverse_directory(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Directories a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any Directory (G Suite, LDAP or Office 365) it is connected to. It is arranged as a hash of Directory IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding Directory; this array reprents all grouping and/or associations that would have to be removed to deprovision that Directory instance from this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Directories a User Group is associated with.
    api_response = api_instance.user_group_traverse_directory(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_g_suite**
> list[GraphObjectWithPaths] user_group_traverse_g_suite(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the G Suite instance a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any G Suite instance it is connected to. It is arranged as a hash of G Suite instance IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding G Suite instance this array reprents all grouping and/or associations that would have to be removed to deprovision that G Suite instancefrom this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the G Suite instance a User Group is associated with.
    api_response = api_instance.user_group_traverse_g_suite(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_g_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_ldap_server**
> list[GraphObjectWithPaths] user_group_traverse_ldap_server(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the LDAP Servers a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any LDAP Servers it is connected to. It is arranged as a hash of LDAP Server IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding LDAP Server; this array reprents all grouping and/or associations that would have to be removed to deprovision that LDAP Server from this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the LDAP Servers a User Group is associated with.
    api_response = api_instance.user_group_traverse_ldap_server(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_office365**
> list[GraphObjectWithPaths] user_group_traverse_office365(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Office 365 instance a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any Office 365 instance it is connected to. It is arranged as a hash of Office 365 instance IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding Office 365 instance this array reprents all grouping and/or associations that would have to be removed to deprovision that Office 365 instancefrom this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Office 365 instance a User Group is associated with.
    api_response = api_instance.user_group_traverse_office365(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_office365: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_radius_server**
> list[GraphObjectWithPaths] user_group_traverse_radius_server(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Radius Servers a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any Radius Servers it is connected to. It is arranged as a hash of Radius Server IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding Radius Server; this array reprents all grouping and/or associations that would have to be removed to deprovision that Radius Server from this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Radius Servers a User Group is associated with.
    api_response = api_instance.user_group_traverse_radius_server(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_system**
> list[GraphObjectWithPaths] user_group_traverse_system(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Systems a User Group is associated with.

**read-only**  This endpoint follows the grouping and associations from this User Group to any Systems it is connected to. It is arranged as a hash of System IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding System; this array reprents all grouping and/or associations that would have to be removed to deprovision that System from this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Systems a User Group is associated with.
    api_response = api_instance.user_group_traverse_system(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_traverse_system_group**
> list[GraphObjectWithPaths] user_group_traverse_system_group(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the System Groups a User Group is associatedwith.

**read-only**  This endpoint follows the grouping and associations from this User Group to any System Groups it is connected to. It is arranged as a hash of System Group IDs for easy lookup.  It also contains a `path` array that describes each path from this User Group to the corresponding System Group; this array reprents all grouping and/or associations that would have to be removed to deprovision that System Group from this User Group. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
group_id = 'group_id_example' # str | ObjectID of the User Group.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the System Groups a User Group is associatedwith.
    api_response = api_instance.user_group_traverse_system_group(group_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_group_traverse_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| ObjectID of the User Group. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_member_of**
> list[GraphObjectWithPaths] user_member_of(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get Users's groups it is a member of.

This lists all groups a user is a member of. That is to say it includes nested group member of relationships as well. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get Users's groups it is a member of.
    api_response = api_instance.user_member_of(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_application**
> list[GraphObjectWithPaths] user_traverse_application(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Applications a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any Applications it is connected to.  It also contains a `path` array that describes each path from this User to the corresponding Application; this array reprents all grouping and/or associations that would have to be removed to deprovision that Application from this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Applications a User is associated with.
    api_response = api_instance.user_traverse_application(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_directory**
> list[GraphObjectWithPaths] user_traverse_directory(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Directories a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any Directory (G Suite, LDAP or Office 365) it is connected to. It is arranged as a hash of Directory IDs for easy lookup.  It also contains a `path` array that describes each path from this User to the corresponding Directory; this array reprents all grouping and/or associations that would have to be removed to deprovision that Directory instance from this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Directories a User is associated with.
    api_response = api_instance.user_traverse_directory(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_g_suite**
> list[GraphObjectWithPaths] user_traverse_g_suite(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the G Suite instance a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any G Suite instance it is connected to. It is arranged as a hash of G Suite instance IDs for easy lookup.  It also contains a `path` array that describes each path from this User to the corresponding G Suite instance this array reprents all grouping and/or associations that would have to be removed to deprovision that G Suite instancefrom this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the G Suite instance a User is associated with.
    api_response = api_instance.user_traverse_g_suite(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_g_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_ldap_server**
> list[GraphObjectWithPaths] user_traverse_ldap_server(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the LDAP Servers a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any LDAP Servers it is connected to. It is arranged as a hash of LDAP Server IDs for easy lookup.  It also contains a `path` array that describes each path from this User to the corresponding LDAP Server; this array reprents all grouping and/or associations that would have to be removed to deprovision that LDAP Server from this User . See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the LDAP Servers a User is associated with.
    api_response = api_instance.user_traverse_ldap_server(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_ldap_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_office365**
> list[GraphObjectWithPaths] user_traverse_office365(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Office 365 instance a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any Office 365 instance it is connected to. It is arranged as a hash of Office 365 instance IDs for easy lookup.  It also contains a `path` array that describes each path from this User to the corresponding Office 365 instance this array reprents all grouping and/or associations that would have to be removed to deprovision that Office 365 instancefrom this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Office 365 instance a User is associated with.
    api_response = api_instance.user_traverse_office365(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_office365: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_radius_server**
> list[GraphObjectWithPaths] user_traverse_radius_server(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Radius Servers a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any Radius Servers it is connected to.  It also contains a `path` array that describes each path from this User to the corresponding Radius Server; this array reprents all grouping and/or associations that would have to be removed to deprovision that Radius Server from this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Radius Servers a User is associated with.
    api_response = api_instance.user_traverse_radius_server(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_radius_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_traverse_system**
> list[GraphObjectWithPaths] user_traverse_system(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Get the Systems a User is associated with.

**read-only**  This endpoint follows the grouping and associations from this User to any Systems it is connected to.  It also contains a `path` array that describes each path from this User to the corresponding System; this array reprents all grouping and/or associations that would have to be removed to deprovision that System from this User. See `/members` and `/associations` endpoints to manage those collections. 

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GraphApi()
user_id = 'user_id_example' # str | ObjectID of the User.
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Get the Systems a User is associated with.
    api_response = api_instance.user_traverse_system(user_id, limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->user_traverse_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ObjectID of the User. | 
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

