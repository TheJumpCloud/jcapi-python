# jcapiv2.GSuiteApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_g_suite_associations_list**](GSuiteApi.md#graph_g_suite_associations_list) | **GET** /gsuites/{gsuite_id}/associations | List the associations of a G Suite instance
[**graph_g_suite_associations_post**](GSuiteApi.md#graph_g_suite_associations_post) | **POST** /gsuites/{gsuite_id}/associations | Manage the associations of a G Suite instance
[**graph_g_suite_traverse_user**](GSuiteApi.md#graph_g_suite_traverse_user) | **GET** /gsuites/{gsuite_id}/users | List the Users bound to a G Suite instance
[**graph_g_suite_traverse_user_group**](GSuiteApi.md#graph_g_suite_traverse_user_group) | **GET** /gsuites/{gsuite_id}/usergroups | List the User Groups bound to a G Suite instance
[**gsuites_get**](GSuiteApi.md#gsuites_get) | **GET** /gsuites/{id} | Get G Suite
[**gsuites_list_import_jumpcloud_users**](GSuiteApi.md#gsuites_list_import_jumpcloud_users) | **GET** /gsuites/{gsuite_id}/import/jumpcloudusers | Get a list of users in Jumpcloud format to import from a Google Workspace account.
[**gsuites_list_import_users**](GSuiteApi.md#gsuites_list_import_users) | **GET** /gsuites/{gsuite_id}/import/users | Get a list of users to import from a G Suite instance
[**gsuites_patch**](GSuiteApi.md#gsuites_patch) | **PATCH** /gsuites/{id} | Update existing G Suite
[**translation_rules_g_suite_delete**](GSuiteApi.md#translation_rules_g_suite_delete) | **DELETE** /gsuites/{gsuite_id}/translationrules/{id} | Deletes a G Suite translation rule
[**translation_rules_g_suite_get**](GSuiteApi.md#translation_rules_g_suite_get) | **GET** /gsuites/{gsuite_id}/translationrules/{id} | Gets a specific G Suite translation rule
[**translation_rules_g_suite_list**](GSuiteApi.md#translation_rules_g_suite_list) | **GET** /gsuites/{gsuite_id}/translationrules | List all the G Suite Translation Rules
[**translation_rules_g_suite_post**](GSuiteApi.md#translation_rules_g_suite_post) | **POST** /gsuites/{gsuite_id}/translationrules | Create a new G Suite Translation Rule

# **graph_g_suite_associations_list**
> list[GraphConnection] graph_g_suite_associations_list(gsuite_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)

List the associations of a G Suite instance

This endpoint returns the _direct_ associations of this G Suite instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example G Suite and Users.   #### Sample Request ``` curl -X GET 'https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/associations?targets=user_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
targets = ['targets_example'] # list[str] | Targets which a \"g_suite\" can be associated to.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the associations of a G Suite instance
    api_response = api_instance.graph_g_suite_associations_list(gsuite_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->graph_g_suite_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
 **targets** | [**list[str]**](str.md)| Targets which a \&quot;g_suite\&quot; can be associated to. | 
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

# **graph_g_suite_associations_post**
> graph_g_suite_associations_post(gsuite_id, body=body, x_org_id=x_org_id)

Manage the associations of a G Suite instance

This endpoint returns the _direct_ associations of this G Suite instance.  A direct association can be a non-homogeneous relationship between 2 different objects, for example G Suite and Users.   #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"user_group\",     \"id\": \"{Group_ID}\"   }' ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
body = jcapiv2.GraphOperationGSuite() # GraphOperationGSuite |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Manage the associations of a G Suite instance
    api_instance.graph_g_suite_associations_post(gsuite_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling GSuiteApi->graph_g_suite_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
 **body** | [**GraphOperationGSuite**](GraphOperationGSuite.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_g_suite_traverse_user**
> list[GraphObjectWithPaths] graph_g_suite_traverse_user(gsuite_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Users bound to a G Suite instance

This endpoint will return all Users bound to a G Suite instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this G Suite instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this G Suite instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{Gsuite_ID}/users \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the Users bound to a G Suite instance
    api_response = api_instance.graph_g_suite_traverse_user(gsuite_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->graph_g_suite_traverse_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
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

# **graph_g_suite_traverse_user_group**
> list[GraphObjectWithPaths] graph_g_suite_traverse_user_group(gsuite_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the User Groups bound to a G Suite instance

This endpoint will return all User Groups bound to an G Suite instance, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this G Suite instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this G Suite instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{GSuite_ID}/usergroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | ObjectID of the G Suite instance.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the User Groups bound to a G Suite instance
    api_response = api_instance.graph_g_suite_traverse_user_group(gsuite_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->graph_g_suite_traverse_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**| ObjectID of the G Suite instance. | 
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

# **gsuites_get**
> GsuiteOutput gsuites_get(id, x_org_id=x_org_id)

Get G Suite

This endpoint returns a specific G Suite.  ##### Sample Request  ```  curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{GSUITE_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the GSuite.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get G Suite
    api_response = api_instance.gsuites_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->gsuites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the GSuite. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**GsuiteOutput**](GsuiteOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gsuites_list_import_jumpcloud_users**
> InlineResponse2001 gsuites_list_import_jumpcloud_users(gsuite_id, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)

Get a list of users in Jumpcloud format to import from a Google Workspace account.

Lists available G Suite users for import, translated to the Jumpcloud user schema.

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
max_results = 56 # int | Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
order_by = 'order_by_example' # str | Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
page_token = 'page_token_example' # str | Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
query = 'query_example' # str | Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. (optional)
sort_order = 'sort_order_example' # str | Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)

try:
    # Get a list of users in Jumpcloud format to import from a Google Workspace account.
    api_response = api_instance.gsuites_list_import_jumpcloud_users(gsuite_id, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->gsuites_list_import_jumpcloud_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **max_results** | **int**| Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **order_by** | **str**| Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **page_token** | **str**| Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **query** | **str**| Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. | [optional] 
 **sort_order** | **str**| Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gsuites_list_import_users**
> InlineResponse2002 gsuites_list_import_users(gsuite_id, limit=limit, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)

Get a list of users to import from a G Suite instance

Lists G Suite users available for import.

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
max_results = 56 # int | Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
order_by = 'order_by_example' # str | Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
page_token = 'page_token_example' # str | Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)
query = 'query_example' # str | Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. (optional)
sort_order = 'sort_order_example' # str | Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. (optional)

try:
    # Get a list of users to import from a G Suite instance
    api_response = api_instance.gsuites_list_import_users(gsuite_id, limit=limit, max_results=max_results, order_by=order_by, page_token=page_token, query=query, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->gsuites_list_import_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **max_results** | **int**| Google Directory API maximum number of results per page. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **order_by** | **str**| Google Directory API sort field parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **page_token** | **str**| Google Directory API token used to access the next page of results. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 
 **query** | **str**| Google Directory API search parameter. See https://developers.google.com/admin-sdk/directory/v1/guides/search-users. | [optional] 
 **sort_order** | **str**| Google Directory API sort direction parameter. See https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gsuites_patch**
> GsuiteOutput gsuites_patch(id, body=body, x_org_id=x_org_id)

Update existing G Suite

This endpoint allows updating some attributes of a G Suite.  ##### Sample Request  ``` curl -X PATCH https://console.jumpcloud.com/api/v2/gsuites/{GSUITE_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"userLockoutAction\": \"suspend\",     \"userPasswordExpirationAction\": \"maintain\"   }' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.GSuiteApi()
id = 'id_example' # str | Unique identifier of the GSuite.
body = jcapiv2.GsuitePatchInput() # GsuitePatchInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update existing G Suite
    api_response = api_instance.gsuites_patch(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->gsuites_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the GSuite. | 
 **body** | [**GsuitePatchInput**](GsuitePatchInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**GsuiteOutput**](GsuiteOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_g_suite_delete**
> translation_rules_g_suite_delete(gsuite_id, id)

Deletes a G Suite translation rule

This endpoint allows you to delete a translation rule for a specific G Suite instance. These rules specify how JumpCloud attributes translate to [G Suite Admin SDK](https://developers.google.com/admin-sdk/directory/) attributes.  #### Sample Request  ``` curl -X DELETE https://console.jumpcloud.com/api/v2/gsuites/{gsuite_id}/translationrules/{id} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
id = 'id_example' # str | 

try:
    # Deletes a G Suite translation rule
    api_instance.translation_rules_g_suite_delete(gsuite_id, id)
except ApiException as e:
    print("Exception when calling GSuiteApi->translation_rules_g_suite_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_g_suite_get**
> GSuiteTranslationRule translation_rules_g_suite_get(gsuite_id, id)

Gets a specific G Suite translation rule

This endpoint returns a specific translation rule for a specific G Suite instance. These rules specify how JumpCloud attributes translate to [G Suite Admin SDK](https://developers.google.com/admin-sdk/directory/) attributes.  ###### Sample Request  ```   curl -X GET https://console.jumpcloud.com/api/v2/gsuites/{gsuite_id}/translationrules/{id} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
id = 'id_example' # str | 

try:
    # Gets a specific G Suite translation rule
    api_response = api_instance.translation_rules_g_suite_get(gsuite_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->translation_rules_g_suite_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GSuiteTranslationRule**](GSuiteTranslationRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_g_suite_list**
> list[GSuiteTranslationRule] translation_rules_g_suite_list(gsuite_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List all the G Suite Translation Rules

This endpoint returns all graph translation rules for a specific G Suite instance. These rules specify how JumpCloud attributes translate to [G Suite Admin SDK](https://developers.google.com/admin-sdk/directory/) attributes.  ##### Sample Request  ```  curl -X GET  https://console.jumpcloud.com/api/v2/gsuites/{gsuite_id}/translationrules \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # List all the G Suite Translation Rules
    api_response = api_instance.translation_rules_g_suite_list(gsuite_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->translation_rules_g_suite_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[GSuiteTranslationRule]**](GSuiteTranslationRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_rules_g_suite_post**
> GSuiteTranslationRule translation_rules_g_suite_post(gsuite_id, body=body)

Create a new G Suite Translation Rule

This endpoint allows you to create a translation rule for a specific G Suite instance. These rules specify how JumpCloud attributes translate to [G Suite Admin SDK](https://developers.google.com/admin-sdk/directory/) attributes.  ##### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/gsuites/{gsuite_id}/translationrules \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     {Translation Rule Parameters}   }' ```

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
api_instance = jcapiv2.GSuiteApi(jcapiv2.ApiClient(configuration))
gsuite_id = 'gsuite_id_example' # str | 
body = jcapiv2.GSuiteTranslationRuleRequest() # GSuiteTranslationRuleRequest |  (optional)

try:
    # Create a new G Suite Translation Rule
    api_response = api_instance.translation_rules_g_suite_post(gsuite_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GSuiteApi->translation_rules_g_suite_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gsuite_id** | **str**|  | 
 **body** | [**GSuiteTranslationRuleRequest**](GSuiteTranslationRuleRequest.md)|  | [optional] 

### Return type

[**GSuiteTranslationRule**](GSuiteTranslationRule.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

