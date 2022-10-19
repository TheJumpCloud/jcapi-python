# jcapiv2.SoftwareAppsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_softwareapps_associations_list**](SoftwareAppsApi.md#graph_softwareapps_associations_list) | **GET** /softwareapps/{software_app_id}/associations | List the associations of a Software Application
[**graph_softwareapps_associations_post**](SoftwareAppsApi.md#graph_softwareapps_associations_post) | **POST** /softwareapps/{software_app_id}/associations | Manage the associations of a software application.
[**graph_softwareapps_traverse_system**](SoftwareAppsApi.md#graph_softwareapps_traverse_system) | **GET** /softwareapps/{software_app_id}/systems | List the Systems bound to a Software App.
[**graph_softwareapps_traverse_system_group**](SoftwareAppsApi.md#graph_softwareapps_traverse_system_group) | **GET** /softwareapps/{software_app_id}/systemgroups | List the System Groups bound to a Software App.
[**software_app_statuses_list**](SoftwareAppsApi.md#software_app_statuses_list) | **GET** /softwareapps/{software_app_id}/statuses | Get the status of the provided Software Application
[**software_apps_delete**](SoftwareAppsApi.md#software_apps_delete) | **DELETE** /softwareapps/{id} | Delete a configured Software Application
[**software_apps_get**](SoftwareAppsApi.md#software_apps_get) | **GET** /softwareapps/{id} | Retrieve a configured Software Application.
[**software_apps_list**](SoftwareAppsApi.md#software_apps_list) | **GET** /softwareapps | Get all configured Software Applications.
[**software_apps_post**](SoftwareAppsApi.md#software_apps_post) | **POST** /softwareapps | Create a Software Application that will be managed by JumpCloud.
[**software_apps_reclaim_licenses**](SoftwareAppsApi.md#software_apps_reclaim_licenses) | **POST** /softwareapps/{software_app_id}/reclaim-licenses | Reclaim Licenses for a Software Application.
[**software_apps_retry_installation**](SoftwareAppsApi.md#software_apps_retry_installation) | **POST** /softwareapps/{software_app_id}/retry-installation | Retry Installation for a Software Application
[**software_apps_update**](SoftwareAppsApi.md#software_apps_update) | **PUT** /softwareapps/{id} | Update a Software Application Configuration.

# **graph_softwareapps_associations_list**
> list[GraphConnection] graph_softwareapps_associations_list(software_app_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)

List the associations of a Software Application

This endpoint will return the _direct_ associations of a Software Application. A direct association can be a non-homogeneous relationship between 2 different objects, for example Software Application and System Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
software_app_id = 'software_app_id_example' # str | ObjectID of the Software App.
targets = ['targets_example'] # list[str] | Targets which a \"software_app\" can be associated to.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the associations of a Software Application
    api_response = api_instance.graph_softwareapps_associations_list(software_app_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->graph_softwareapps_associations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_app_id** | **str**| ObjectID of the Software App. | 
 **targets** | [**list[str]**](str.md)| Targets which a \&quot;software_app\&quot; can be associated to. | 
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

# **graph_softwareapps_associations_post**
> graph_softwareapps_associations_post(software_app_id, body=body, x_org_id=x_org_id)

Manage the associations of a software application.

This endpoint allows you to associate or disassociate a software application to a system or system group.  #### Sample Request ``` $ curl -X POST https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/associations \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{   \"id\": \"<object_id>\",   \"op\": \"add\",   \"type\": \"system\"  }' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
software_app_id = 'software_app_id_example' # str | ObjectID of the Software App.
body = jcapiv2.GraphOperationSoftwareApp() # GraphOperationSoftwareApp |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Manage the associations of a software application.
    api_instance.graph_softwareapps_associations_post(software_app_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->graph_softwareapps_associations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_app_id** | **str**| ObjectID of the Software App. | 
 **body** | [**GraphOperationSoftwareApp**](GraphOperationSoftwareApp.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_softwareapps_traverse_system**
> list[GraphObjectWithPaths] graph_softwareapps_traverse_system(software_app_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the Systems bound to a Software App.

This endpoint will return all Systems bound to a Software App, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Software App to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Software App.  See `/associations` endpoint to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/systems \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
software_app_id = 'software_app_id_example' # str | ObjectID of the Software App.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the Systems bound to a Software App.
    api_response = api_instance.graph_softwareapps_traverse_system(software_app_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->graph_softwareapps_traverse_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_app_id** | **str**| ObjectID of the Software App. | 
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

# **graph_softwareapps_traverse_system_group**
> list[GraphObjectWithPaths] graph_softwareapps_traverse_system_group(software_app_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)

List the System Groups bound to a Software App.

This endpoint will return all Systems Groups bound to a Software App, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Software App to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Software App.  See `/associations` endpoint to manage those collections.  #### Sample Request ``` curl -X GET  https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/systemgroups \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
software_app_id = 'software_app_id_example' # str | ObjectID of the Software App.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the System Groups bound to a Software App.
    api_response = api_instance.graph_softwareapps_traverse_system_group(software_app_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->graph_softwareapps_traverse_system_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_app_id** | **str**| ObjectID of the Software App. | 
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

# **software_app_statuses_list**
> list[SoftwareAppStatus] software_app_statuses_list(software_app_id, x_org_id=x_org_id, filter=filter, limit=limit, skip=skip, sort=sort)

Get the status of the provided Software Application

This endpoint allows you to get the status of the provided Software Application on associated JumpCloud systems.  #### Sample Request ``` $ curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/statuses \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
software_app_id = 'software_app_id_example' # str | ObjectID of the Software App.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # Get the status of the provided Software Application
    api_response = api_instance.software_app_statuses_list(software_app_id, x_org_id=x_org_id, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_app_statuses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_app_id** | **str**| ObjectID of the Software App. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[SoftwareAppStatus]**](SoftwareAppStatus.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_delete**
> software_apps_delete(id, x_org_id=x_org_id)

Delete a configured Software Application

Removes a Software Application configuration.  Warning: This is a destructive operation and will unmanage the application on all affected systems.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/softwareapps/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete a configured Software Application
    api_instance.software_apps_delete(id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_get**
> SoftwareApp software_apps_get(id, x_org_id=x_org_id)

Retrieve a configured Software Application.

Retrieves a Software Application. The optional isConfigEnabled and appConfiguration apple_vpp attributes are populated in this response.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/softwareapps/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Retrieve a configured Software Application.
    api_response = api_instance.software_apps_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**SoftwareApp**](SoftwareApp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_list**
> list[SoftwareApp] software_apps_list(x_org_id=x_org_id, filter=filter, limit=limit, skip=skip, sort=sort)

Get all configured Software Applications.

This endpoint allows you to get all configured Software Applications that will be managed by JumpCloud on associated JumpCloud systems. The optional isConfigEnabled and appConfiguration apple_vpp attributes are not included in the response.  #### Sample Request ``` $ curl -X GET https://console.jumpcloud.com/api/v2/softwareapps \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # Get all configured Software Applications.
    api_response = api_instance.software_apps_list(x_org_id=x_org_id, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[SoftwareApp]**](SoftwareApp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_post**
> SoftwareApp software_apps_post(body=body, x_org_id=x_org_id)

Create a Software Application that will be managed by JumpCloud.

This endpoint allows you to create a Software Application that will be managed by JumpCloud on associated JumpCloud systems. The optional isConfigEnabled and appConfiguration apple_vpp attributes are not included in the response.  #### Sample Request ``` $ curl -X POST https://console.jumpcloud.com/api/v2/softwareapps \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{   \"displayName\": \"Adobe Reader\",   \"settings\": [{\"packageId\": \"adobereader\"}] }' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.SoftwareApp() # SoftwareApp |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create a Software Application that will be managed by JumpCloud.
    api_response = api_instance.software_apps_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SoftwareApp**](SoftwareApp.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**SoftwareApp**](SoftwareApp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_reclaim_licenses**
> SoftwareAppReclaimLicenses software_apps_reclaim_licenses(software_app_id)

Reclaim Licenses for a Software Application.

This endpoint allows you to reclaim the licenses from a software app associated with devices that are deleted. #### Sample Request ``` $ curl -X POST https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/reclaim-licenses \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
software_app_id = 'software_app_id_example' # str | 

try:
    # Reclaim Licenses for a Software Application.
    api_response = api_instance.software_apps_reclaim_licenses(software_app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_reclaim_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_app_id** | **str**|  | 

### Return type

[**SoftwareAppReclaimLicenses**](SoftwareAppReclaimLicenses.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_retry_installation**
> software_apps_retry_installation(body, software_app_id)

Retry Installation for a Software Application

This endpoints initiates an installation retry of an Apple VPP App for the provided system IDs #### Sample Request ``` $ curl -X POST https://console.jumpcloud.com/api/v2/softwareapps/{software_app_id}/retry-installation \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{\"system_ids\": \"{<system_id_1>, <system_id_2>, ...}\"}' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.SoftwareAppsRetryInstallationRequest() # SoftwareAppsRetryInstallationRequest | 
software_app_id = 'software_app_id_example' # str | 

try:
    # Retry Installation for a Software Application
    api_instance.software_apps_retry_installation(body, software_app_id)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_retry_installation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SoftwareAppsRetryInstallationRequest**](SoftwareAppsRetryInstallationRequest.md)|  | 
 **software_app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_apps_update**
> SoftwareApp software_apps_update(id, body=body, x_org_id=x_org_id)

Update a Software Application Configuration.

This endpoint updates a specific Software Application configuration for the organization. displayName can be changed alone if no settings are provided. If a setting is provided, it should include all its information since this endpoint will update all the settings' fields. The optional isConfigEnabled and appConfiguration apple_vpp attributes are not included in the response.  #### Sample Request - displayName only ```  curl -X PUT https://console.jumpcloud.com/api/v2/softwareapps/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"displayName\": \"My Software App\"   }' ```  #### Sample Request - all attributes ```  curl -X PUT https://console.jumpcloud.com/api/v2/softwareapps/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"displayName\": \"My Software App\",     \"settings\": [       {         \"packageId\": \"123456\",         \"autoUpdate\": false,         \"allowUpdateDelay\": false,         \"packageManager\": \"APPLE_VPP\",         \"locationObjectId\": \"123456789012123456789012\",         \"location\": \"123456\",         \"desiredState\": \"Install\",         \"appleVpp\": {           \"appConfiguration\": \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?><!DOCTYPE plist PUBLIC \\\"-//Apple//DTD PLIST 1.0//EN\\\" \\\"http://www.apple.com/DTDs/PropertyList-1.0.dtd\\\"><plist version=\\\"1.0\\\"><dict><key>MyKey</key><string>My String</string></dict></plist>\",           \"assignedLicenses\": 20,           \"availableLicenses\": 10,           \"details\": {},           \"isConfigEnabled\": true,           \"supportedDeviceFamilies\": [             \"IPAD\",             \"MAC\"           ],           \"totalLicenses\": 30         },         \"packageSubtitle\": \"My package subtitle\",         \"packageVersion\": \"1.2.3\",         \"packageKind\": \"software-package\",         \"assetKind\": \"software\",         \"assetSha256Size\": 256,         \"assetSha256Strings\": [           \"a123b123c123d123\"         ],         \"description\": \"My app description\"       }     ]   }' ```

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
api_instance = jcapiv2.SoftwareAppsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv2.SoftwareApp() # SoftwareApp |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update a Software Application Configuration.
    api_response = api_instance.software_apps_update(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareAppsApi->software_apps_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SoftwareApp**](SoftwareApp.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**SoftwareApp**](SoftwareApp.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

