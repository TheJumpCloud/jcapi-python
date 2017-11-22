# jcapiv2.LDAPServersApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_ldap_server_associations_list**](LDAPServersApi.md#graph_ldap_server_associations_list) | **GET** /ldapservers/{ldapserver_id}/associations | List the associations of a LDAP Server
[**graph_ldap_server_associations_post**](LDAPServersApi.md#graph_ldap_server_associations_post) | **POST** /ldapservers/{ldapserver_id}/associations | Manage the associations of a LDAP Server
[**graph_ldap_server_traverse_user**](LDAPServersApi.md#graph_ldap_server_traverse_user) | **GET** /ldapservers/{ldapserver_id}/users | List the Users associated with a LDAP Server
[**graph_ldap_server_traverse_user_group**](LDAPServersApi.md#graph_ldap_server_traverse_user_group) | **GET** /ldapservers/{ldapserver_id}/usergroups | List the User Groups associated with a LDAP Server
[**ldapservers_get**](LDAPServersApi.md#ldapservers_get) | **GET** /ldapservers/{id} | Get LDAP Server
[**ldapservers_list**](LDAPServersApi.md#ldapservers_list) | **GET** /ldapservers | List LDAP Servers


# **graph_ldap_server_associations_list**
> list[GraphConnection] graph_ldap_server_associations_list(ldapserver_id, targets, content_type, accept, limit=limit, skip=skip)

List the associations of a LDAP Server

This endpoint returns the _direct_ associations of this LDAP Server.  A direct association can be a non-homogenous relationship between 2 different objects. for example LDAP and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/ldapservers/{ldapserver_id}/associations?targets=user ```

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
api_instance = jcapiv2.LDAPServersApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
targets = ['targets_example'] # list[str] | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the associations of a LDAP Server
    api_response = api_instance.graph_ldap_server_associations_list(ldapserver_id, targets, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
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

# **graph_ldap_server_associations_post**
> graph_ldap_server_associations_post(ldapserver_id, content_type, accept, body=body)

Manage the associations of a LDAP Server

This endpoint allows you to manage the _direct_ associations of a LDAP Server.  A direct association can be a non-homogenous relationship between 2 different objects. for example LDAP and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/ldapservers/{ldapserver_id}/associations ```

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
api_instance = jcapiv2.LDAPServersApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.GraphManagementReq() # GraphManagementReq |  (optional)

try: 
    # Manage the associations of a LDAP Server
    api_instance.graph_ldap_server_associations_post(ldapserver_id, content_type, accept, body=body)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
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

# **graph_ldap_server_traverse_user**
> list[GraphObjectWithPaths] graph_ldap_server_traverse_user(ldapserver_id, content_type, accept, limit=limit, skip=skip)

List the Users associated with a LDAP Server

This endpoint will return Users associated with an LDAP server instance. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/ldapservers/{ldapserver_id}/users ```

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
api_instance = jcapiv2.LDAPServersApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the Users associated with a LDAP Server
    api_response = api_instance.graph_ldap_server_traverse_user(ldapserver_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
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

# **graph_ldap_server_traverse_user_group**
> list[GraphObjectWithPaths] graph_ldap_server_traverse_user_group(ldapserver_id, content_type, accept, limit=limit, skip=skip)

List the User Groups associated with a LDAP Server

This endpoint will return User Groups associated with a LDAP server instance. Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/ldapservers/{ldapserver_id}/usersgroups ```

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
api_instance = jcapiv2.LDAPServersApi()
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # List the User Groups associated with a LDAP Server
    api_response = api_instance.graph_ldap_server_traverse_user_group(ldapserver_id, content_type, accept, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
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

# **ldapservers_get**
> LdapServerOutput ldapservers_get(id, content_type, accept)

Get LDAP Server

This endpoint returns a specific LDAP server.

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
api_instance = jcapiv2.LDAPServersApi()
id = 'id_example' # str | Unique identifier of the LDAP server.
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)

try: 
    # Get LDAP Server
    api_response = api_instance.ldapservers_get(id, content_type, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->ldapservers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP server. | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]

### Return type

[**LdapServerOutput**](LdapServerOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_list**
> list[LdapServerOutput] ldapservers_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List LDAP Servers

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
api_instance = jcapiv2.LDAPServersApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str | Supported operators are: eq, ne, gt, ge, lt, le, between, search (optional) (default to )
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )

try: 
    # List LDAP Servers
    api_response = api_instance.ldapservers_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->ldapservers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**| Supported operators are: eq, ne, gt, ge, lt, le, between, search | [optional] [default to ]
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]

### Return type

[**list[LdapServerOutput]**](LdapServerOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

