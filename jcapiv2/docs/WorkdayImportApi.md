# jcapiv2.WorkdayImportApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workdays_authorize**](WorkdayImportApi.md#workdays_authorize) | **POST** /workdays/{workday_id}/auth | Authorize Workday
[**workdays_deauthorize**](WorkdayImportApi.md#workdays_deauthorize) | **DELETE** /workdays/{workday_id}/auth | Deauthorize Workday
[**workdays_get**](WorkdayImportApi.md#workdays_get) | **GET** /workdays/{id} | Get Workday
[**workdays_import**](WorkdayImportApi.md#workdays_import) | **POST** /workdays/{workday_id}/import | Workday Import
[**workdays_importresults**](WorkdayImportApi.md#workdays_importresults) | **GET** /workdays/{id}/import/{job_id}/results | List Import Results
[**workdays_list**](WorkdayImportApi.md#workdays_list) | **GET** /workdays | List Workdays
[**workdays_post**](WorkdayImportApi.md#workdays_post) | **POST** /workdays | Create new Workday
[**workdays_put**](WorkdayImportApi.md#workdays_put) | **PUT** /workdays/{id} | Update Workday
[**workdays_workers**](WorkdayImportApi.md#workdays_workers) | **GET** /workdays/{workday_id}/workers | List Workday Workers

# **workdays_authorize**
> workdays_authorize(workday_id, body=body, x_org_id=x_org_id)

Authorize Workday

This endpoint adds an authorization method to a workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/auth \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"auth\":{    \"basic\": {   \"username\": \"someDeveloper\",      \"password\": \"notTheRealPassword\"     }  } }'  ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
workday_id = 'workday_id_example' # str | 
body = jcapiv2.AuthInputObject() # AuthInputObject |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Authorize Workday
    api_instance.workdays_authorize(workday_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **body** | [**AuthInputObject**](AuthInputObject.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_deauthorize**
> workdays_deauthorize(workday_id, x_org_id=x_org_id)

Deauthorize Workday

Removes any and all authorization methods from the workday instance  ##### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/auth \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
workday_id = 'workday_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Deauthorize Workday
    api_instance.workdays_deauthorize(workday_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_deauthorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_get**
> WorkdayOutput workdays_get(id, x_org_id=x_org_id)

Get Workday

This endpoint will return  all the available information about an instance of Workday.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get Workday
    api_response = api_instance.workdays_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_import**
> JobId workdays_import(workday_id, body=body, x_org_id=x_org_id)

Workday Import

The endpoint allows you to create a Workday Import request.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/{WorkdayID}/import \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '[  {   \"email\":\"{email}\",   \"firstname\":\"{firstname}\",   \"lastname\":\"{firstname}\",   \"username\":\"{username}\",   \"attributes\":[    {\"name\":\"EmployeeID\",\"value\":\"0000\"},    {\"name\":\"WorkdayID\",\"value\":\"name.name\"}    ]     } ] ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
workday_id = 'workday_id_example' # str | 
body = [jcapiv2.BulkUserCreate()] # list[BulkUserCreate] |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Workday Import
    api_response = api_instance.workdays_import(workday_id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **body** | [**list[BulkUserCreate]**](BulkUserCreate.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**JobId**](JobId.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_importresults**
> list[JobWorkresult] workdays_importresults(id, job_id, limit=limit, skip=skip, x_org_id=x_org_id)

List Import Results

This endpoint provides a list of job results from the workday import and will contain all imported data from Workday.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/{WorkdayID}/import/{ImportJobID}/results \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
job_id = 'job_id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Import Results
    api_response = api_instance.workdays_importresults(id, job_id, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_importresults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **workdays_list**
> list[WorkdayOutput] workdays_list(fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)

List Workdays

This endpoint will return  all the available information about all your instances of Workday.  ##### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Workdays
    api_response = api_instance.workdays_list(fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[WorkdayOutput]**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_post**
> WorkdayOutput workdays_post(body=body, x_org_id=x_org_id)

Create new Workday

This endpoint allows you to create a new workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  Currently, only one instance is allowed and it must be `Workday Import`.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Workday2\",     \"reportUrl\":\"https://workday.com/ccx/service/customreport2/gms/user/reportname?format=json\",     \"auth\": {       \"basic\": {         \"username\": \"someDeveloper\",         \"password\": \"notTheRealPassword\"       }     }   }' ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.WorkdayInput() # WorkdayInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create new Workday
    api_response = api_instance.workdays_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkdayInput**](WorkdayInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_put**
> WorkdayOutput workdays_put(id, body=body, x_org_id=x_org_id)

Update Workday

This endpoint allows you to update the name and Custom Report URL for a Workday Instance.  Currently, the name can not be changed from the default of `Workday Import`.  ##### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/v2/workdays/{WorkdayID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"reportUrl\":\"{Report_URL}\",  \"name\":\"{Name}\" } ' ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv2.WorkdayFields() # WorkdayFields |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update Workday
    api_response = api_instance.workdays_put(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**WorkdayFields**](WorkdayFields.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_workers**
> list[WorkdayWorker] workdays_workers(workday_id, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)

List Workday Workers

This endpoint will return all of the data in your WorkDay Custom Report that has been associated with your WorkDay Instance in JumpCloud.  ##### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/v2/workdays/{WorkDayID}/workers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.WorkdayImportApi(jcapiv2.ApiClient(configuration))
workday_id = 'workday_id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Workday Workers
    api_response = api_instance.workdays_workers(workday_id, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[WorkdayWorker]**](WorkdayWorker.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

