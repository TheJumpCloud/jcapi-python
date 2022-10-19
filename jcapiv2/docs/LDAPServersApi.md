# jcapiv2.LDAPServersApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_ldap_server_associations_list**](LDAPServersApi.md#graph_ldap_server_associations_list) | **GET** /ldapservers/{ldapserver_id}/associations | List the associations of a LDAP Server
[**graph_ldap_server_associations_post**](LDAPServersApi.md#graph_ldap_server_associations_post) | **POST** /ldapservers/{ldapserver_id}/associations | Manage the associations of a LDAP Server
[**graph_ldap_server_traverse_user**](LDAPServersApi.md#graph_ldap_server_traverse_user) | **GET** /ldapservers/{ldapserver_id}/users | List the Users bound to a LDAP Server
[**graph_ldap_server_traverse_user_group**](LDAPServersApi.md#graph_ldap_server_traverse_user_group) | **GET** /ldapservers/{ldapserver_id}/usergroups | List the User Groups bound to a LDAP Server
[**ldapservers_get**](LDAPServersApi.md#ldapservers_get) | **GET** /ldapservers/{id} | Get LDAP Server
[**ldapservers_list**](LDAPServersApi.md#ldapservers_list) | **GET** /ldapservers | List LDAP Servers
[**ldapservers_patch**](LDAPServersApi.md#ldapservers_patch) | **PATCH** /ldapservers/{id} | Update existing LDAP server

# **graph_ldap_server_associations_list**
> list[GraphConnection] graph_ldap_server_associations_list(ldapserver_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)

List the associations of a LDAP Server

This endpoint returns the _direct_ associations of this LDAP Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example LDAP and Users.  #### Sample Request  ```  curl -X GET 'https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
targets = ['targets_example'] # list[str] | Targets which a \"ldap_server\" can be associated to.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the associations of a LDAP Server
    api_response = api_instance.graph_ldap_server_associations_list(ldapserver_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **targets** | [**list[str]**](str.md)| Targets which a \&quot;ldap_server\&quot; can be associated to. | 
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

# **graph_ldap_server_associations_post**
> graph_ldap_server_associations_post(ldapserver_id, body=body, x_org_id=x_org_id)

Manage the associations of a LDAP Server

This endpoint allows you to manage the _direct_ associations of a LDAP Server.  A direct association can be a non-homogeneous relationship between 2 different objects, for example LDAP and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user\",     \"id\": \"{User_ID}\"   }' ```

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
body = jcapiv2.GraphOperationLdapServer() # GraphOperationLdapServer |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Manage the associations of a LDAP Server
    api_instance.graph_ldap_server_associations_post(ldapserver_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **body** | [**GraphOperationLdapServer**](GraphOperationLdapServer.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_ldap_server_traverse_user**
> list[GraphObjectWithPaths] graph_ldap_server_traverse_user(ldapserver_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Users bound to a LDAP Server

This endpoint will return all Users bound to an LDAP Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the Users bound to a LDAP Server
    api_response = api_instance.graph_ldap_server_traverse_user(ldapserver_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_ldap_server_traverse_user_group**
> list[GraphObjectWithPaths] graph_ldap_server_traverse_user_group(ldapserver_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the User Groups bound to a LDAP Server

This endpoint will return all Users Groups bound to a LDAP Server, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this LDAP server instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this LDAP server instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | ObjectID of the LDAP Server.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the User Groups bound to a LDAP Server
    api_response = api_instance.graph_ldap_server_traverse_user_group(ldapserver_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->graph_ldap_server_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| ObjectID of the LDAP Server. | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 

### Return type

[**list[GraphObjectWithPaths]**](GraphObjectWithPaths.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_get**
> LdapServerOutput ldapservers_get(id, x_org_id=x_org_id)

Get LDAP Server

This endpoint returns a specific LDAP server.  ##### Sample Request  ```  curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the LDAP server.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get LDAP Server
    api_response = api_instance.ldapservers_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->ldapservers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP server. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**LdapServerOutput**](LdapServerOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_list**
> list[LdapServerOutput] ldapservers_list(fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)

List LDAP Servers

This endpoint returns the object IDs of your LDAP servers.   ##### Sample Request  ```   curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List LDAP Servers
    api_response = api_instance.ldapservers_list(fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->ldapservers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[LdapServerOutput]**](LdapServerOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_patch**
> InlineResponse20010 ldapservers_patch(id, body=body, x_org_id=x_org_id)

Update existing LDAP server

This endpoint allows updating some attributes of an LDAP server.  Sample Request  ``` curl -X PATCH https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"userLockoutAction\": \"remove\",     \"userPasswordExpirationAction\": \"disable\"   }' ```

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
api_instance = jcapiv2.LDAPServersApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the LDAP server.
body = jcapiv2.LdapserversIdBody() # LdapserversIdBody |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update existing LDAP server
    api_response = api_instance.ldapservers_patch(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LDAPServersApi->ldapservers_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP server. | 
 **body** | [**LdapserversIdBody**](LdapserversIdBody.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

