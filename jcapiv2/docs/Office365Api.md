# jcapiv2.Office365Api

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_office365_associations_list**](Office365Api.md#graph_office365_associations_list) | **GET** /office365s/{office365_id}/associations | List the associations of an Office 365 instance
[**graph_office365_associations_post**](Office365Api.md#graph_office365_associations_post) | **POST** /office365s/{office365_id}/associations | Manage the associations of an Office 365 instance
[**graph_office365_traverse_user**](Office365Api.md#graph_office365_traverse_user) | **GET** /office365s/{office365_id}/users | List the Users bound to an Office 365 instance
[**graph_office365_traverse_user_group**](Office365Api.md#graph_office365_traverse_user_group) | **GET** /office365s/{office365_id}/usergroups | List the User Groups bound to an Office 365 instance
[**office365s_get**](Office365Api.md#office365s_get) | **GET** /office365s/{office365_id} | Get Office 365 instance
[**office365s_list_import_users**](Office365Api.md#office365s_list_import_users) | **GET** /office365s/{office365_id}/import/users | Get a list of users to import from an Office 365 instance
[**office365s_patch**](Office365Api.md#office365s_patch) | **PATCH** /office365s/{office365_id} | Update existing Office 365 instance.
[**translation_rules_office365_delete**](Office365Api.md#translation_rules_office365_delete) | **DELETE** /office365s/{office365_id}/translationrules/{id} | Deletes a Office 365 translation rule
[**translation_rules_office365_get**](Office365Api.md#translation_rules_office365_get) | **GET** /office365s/{office365_id}/translationrules/{id} | Gets a specific Office 365 translation rule
[**translation_rules_office365_list**](Office365Api.md#translation_rules_office365_list) | **GET** /office365s/{office365_id}/translationrules | List all the Office 365 Translation Rules
[**translation_rules_office365_post**](Office365Api.md#translation_rules_office365_post) | **POST** /office365s/{office365_id}/translationrules | Create a new Office 365 Translation Rule

# **graph_office365_associations_list**
> list[GraphConnection] graph_office365_associations_list(office365_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)

List the associations of an Office 365 instance

This endpoint returns _direct_ associations of an Office 365 instance.   A direct association can be a non-homogeneous relationship between 2 different objects, for example Office 365 and Users.  #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/associations?targets=user_group' \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
targets = ['targets_example'] # list[str] | Targets which a \"office_365\" can be associated to.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the associations of an Office 365 instance
    api_response = api_instance.graph_office365_associations_list(office365_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
 **targets** | [**list[str]**](str.md)| Targets which a \&quot;office_365\&quot; can be associated to. | 
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

# **graph_office365_associations_post**
> graph_office365_associations_post(office365_id, body=body, x_org_id=x_org_id)

Manage the associations of an Office 365 instance

This endpoint allows you to manage the _direct_ associations of a Office 365 instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example Office 365 and Users.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/associations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
body = jcapiv2.GraphOperationOffice365() # GraphOperationOffice365 |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Manage the associations of an Office 365 instance
    api_instance.graph_office365_associations_post(office365_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
 **body** | [**GraphOperationOffice365**](GraphOperationOffice365.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_office365_traverse_user**
> list[GraphObjectWithPaths] graph_office365_traverse_user(office365_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Users bound to an Office 365 instance

This endpoint will return all Users bound to an Office 365 instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID}/users \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 suite.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the Users bound to an Office 365 instance
    api_response = api_instance.graph_office365_traverse_user(office365_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 suite. | 
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

# **graph_office365_traverse_user_group**
> list[GraphObjectWithPaths] graph_office365_traverse_user_group(office365_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the User Groups bound to an Office 365 instance

This endpoint will return all Users Groups bound to an Office 365 instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID/usergroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 suite.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the User Groups bound to an Office 365 instance
    api_response = api_instance.graph_office365_traverse_user_group(office365_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->graph_office365_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 suite. | 
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

# **office365s_get**
> Office365Output office365s_get(office365_id, x_org_id=x_org_id)

Get Office 365 instance

This endpoint returns a specific Office 365 instance.  #####  Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'  ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get Office 365 instance
    api_response = api_instance.office365s_get(office365_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->office365s_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**Office365Output**](Office365Output.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office365s_list_import_users**
> InlineResponse20011 office365s_list_import_users(office365_id, consistency_level=consistency_level, top=top, skip_token=skip_token, filter=filter, search=search, orderby=orderby, count=count)

Get a list of users to import from an Office 365 instance

Lists Office 365 users available for import.

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | 
consistency_level = 'consistency_level_example' # str | Defines the consistency header for O365 requests. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#request-headers (optional)
top = 56 # int | Office 365 API maximum number of results per page. See https://docs.microsoft.com/en-us/graph/paging. (optional)
skip_token = 'skip_token_example' # str | Office 365 API token used to access the next page of results. See https://docs.microsoft.com/en-us/graph/paging. (optional)
filter = 'filter_example' # str | Office 365 API filter parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)
search = 'search_example' # str | Office 365 API search parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)
orderby = 'orderby_example' # str | Office 365 API orderby parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)
count = true # bool | Office 365 API count parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http#optional-query-parameters. (optional)

try:
    # Get a list of users to import from an Office 365 instance
    api_response = api_instance.office365s_list_import_users(office365_id, consistency_level=consistency_level, top=top, skip_token=skip_token, filter=filter, search=search, orderby=orderby, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->office365s_list_import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**|  | 
 **consistency_level** | **str**| Defines the consistency header for O365 requests. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#request-headers | [optional] 
 **top** | **int**| Office 365 API maximum number of results per page. See https://docs.microsoft.com/en-us/graph/paging. | [optional] 
 **skip_token** | **str**| Office 365 API token used to access the next page of results. See https://docs.microsoft.com/en-us/graph/paging. | [optional] 
 **filter** | **str**| Office 365 API filter parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 
 **search** | **str**| Office 365 API search parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 
 **orderby** | **str**| Office 365 API orderby parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 
 **count** | **bool**| Office 365 API count parameter. See https://docs.microsoft.com/en-us/graph/api/user-list?view&#x3D;graph-rest-1.0&amp;tabs&#x3D;http#optional-query-parameters. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office365s_patch**
> Office365Output office365s_patch(office365_id, body=body, x_org_id=x_org_id)

Update existing Office 365 instance.

This endpoint allows updating some attributes of an Office 365 instance.  #####  Sample Request  ``` curl -X PATCH https://console.jumpcloud.com/api/v2/office365s/{OFFICE365_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"userLockoutAction\": \"maintain\",     \"userPasswordExpirationAction\": \"suspend\"   }' ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | ObjectID of the Office 365 instance.
body = jcapiv2.Office365PatchInput() # Office365PatchInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update existing Office 365 instance.
    api_response = api_instance.office365s_patch(office365_id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->office365s_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**| ObjectID of the Office 365 instance. | 
 **body** | [**Office365PatchInput**](Office365PatchInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**Office365Output**](Office365Output.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_office365_delete**
> translation_rules_office365_delete(office365_id, id)

Deletes a Office 365 translation rule

This endpoint allows you to delete a translation rule for a specific Office 365 instance. These rules specify how JumpCloud attributes translate to [Microsoft Graph](https://developer.microsoft.com/en-us/graph) attributes.  #### Sample Request  ``` curl -X DELETE https://console.jumpcloud.com/api/v2/office365s/{office365_id}/translationrules/{id} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | 
id = 'id_example' # str | 

try:
    # Deletes a Office 365 translation rule
    api_instance.translation_rules_office365_delete(office365_id, id)
except ApiException as e:
    print("Exception when calling Office365Api->translation_rules_office365_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_office365_get**
> Office365TranslationRule translation_rules_office365_get(office365_id, id)

Gets a specific Office 365 translation rule

This endpoint returns a specific translation rule for a specific Office 365 instance. These rules specify how JumpCloud attributes translate to [Microsoft Graph](https://developer.microsoft.com/en-us/graph) attributes.  ###### Sample Request  ```   curl -X GET https://console.jumpcloud.com/api/v2/office365s/{office365_id}/translationrules/{id} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | 
id = 'id_example' # str | 

try:
    # Gets a specific Office 365 translation rule
    api_response = api_instance.translation_rules_office365_get(office365_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->translation_rules_office365_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Office365TranslationRule**](Office365TranslationRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_office365_list**
> list[Office365TranslationRule] translation_rules_office365_list(office365_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List all the Office 365 Translation Rules

This endpoint returns all translation rules for a specific Office 365 instance. These rules specify how JumpCloud attributes translate to [Microsoft Graph](https://developer.microsoft.com/en-us/graph) attributes.  ##### Sample Request  ```  curl -X GET  https://console.jumpcloud.com/api/v2/office365s/{office365_id}/translationrules \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | 
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # List all the Office 365 Translation Rules
    api_response = api_instance.translation_rules_office365_list(office365_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->translation_rules_office365_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**|  | 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[Office365TranslationRule]**](Office365TranslationRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_office365_post**
> Office365TranslationRule translation_rules_office365_post(office365_id, body=body)

Create a new Office 365 Translation Rule

This endpoint allows you to create a translation rule for a specific Office 365 instance. These rules specify how JumpCloud attributes translate to [Microsoft Graph](https://developer.microsoft.com/en-us/graph) attributes.  ##### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/office365s/{office365_id}/translationrules \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     {Translation Rule Parameters}   }' ```

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
api_instance = jcapiv2.Office365Api(jcapiv2.ApiClient(configuration))
office365_id = 'office365_id_example' # str | 
body = jcapiv2.Office365TranslationRuleRequest() # Office365TranslationRuleRequest |  (optional)

try:
    # Create a new Office 365 Translation Rule
    api_response = api_instance.translation_rules_office365_post(office365_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Office365Api->translation_rules_office365_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office365_id** | **str**|  | 
 **body** | [**Office365TranslationRuleRequest**](Office365TranslationRuleRequest.md)|  | [optional] 

### Return type

[**Office365TranslationRule**](Office365TranslationRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

