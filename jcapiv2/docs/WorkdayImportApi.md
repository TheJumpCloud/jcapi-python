# jcapiv2.WorkdayImportApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workdays_authorize**](WorkdayImportApi.md#workdays_authorize) | **POST** /workdays/{workday_id}/auth | Authorize Workday
[**workdays_deauthorize**](WorkdayImportApi.md#workdays_deauthorize) | **DELETE** /workdays/{workday_id}/auth | Deauthorize Workday
[**workdays_delete**](WorkdayImportApi.md#workdays_delete) | **DELETE** /workdays/{id} | Delete Workday
[**workdays_get**](WorkdayImportApi.md#workdays_get) | **GET** /workdays/{id} | Get Workday
[**workdays_import**](WorkdayImportApi.md#workdays_import) | **POST** /workdays/{workday_id}/import | Workday Import
[**workdays_importresults**](WorkdayImportApi.md#workdays_importresults) | **GET** /workdays/{id}/import/{job_id}/results | List Import Results
[**workdays_list**](WorkdayImportApi.md#workdays_list) | **GET** /workdays | List Workdays
[**workdays_post**](WorkdayImportApi.md#workdays_post) | **POST** /workdays | Create new Workday
[**workdays_put**](WorkdayImportApi.md#workdays_put) | **PUT** /workdays/{id} | Update Workday
[**workdays_settings**](WorkdayImportApi.md#workdays_settings) | **GET** /workdays/settings | Get Workday Settings (incomplete)
[**workdays_workers**](WorkdayImportApi.md#workdays_workers) | **GET** /workdays/{workday_id}/workers | List Workday Workers


# **workdays_authorize**
> workdays_authorize(workday_id, content_type, accept, body=body, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.AuthInputObject() # AuthInputObject |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Authorize Workday
    api_instance.workdays_authorize(workday_id, content_type, accept, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**AuthInputObject**](AuthInputObject.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_deauthorize**
> workdays_deauthorize(workday_id, content_type, accept, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Deauthorize Workday
    api_instance.workdays_deauthorize(workday_id, content_type, accept, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_deauthorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_delete**
> object workdays_delete(id, content_type, accept, x_org_id=x_org_id)

Delete Workday

This endpoint allows you to delete an instance of Workday.  **This functionality is currently not enable for users.**

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Delete Workday
    api_response = api_instance.workdays_delete(id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

**object**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_get**
> WorkdayOutput workdays_get(id, content_type, accept, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Get Workday
    api_response = api_instance.workdays_get(id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_import**
> JobId workdays_import(workday_id, content_type, accept, body=body, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = [jcapiv2.BulkUserCreate()] # list[BulkUserCreate] |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Workday Import
    api_response = api_instance.workdays_import(workday_id, content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**list[BulkUserCreate]**](BulkUserCreate.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**JobId**](JobId.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_importresults**
> list[JobWorkresult] workdays_importresults(id, job_id, content_type, accept, limit=limit, skip=skip, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = '' # str |  (optional) (default to )

try:
    # List Import Results
    api_response = api_instance.workdays_importresults(id, job_id, content_type, accept, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_importresults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **job_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[JobWorkresult]**](JobWorkresult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_list**
> list[WorkdayOutput] workdays_list(content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = ['[]'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional) (default to [])
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
x_org_id = '' # str |  (optional) (default to )

try:
    # List Workdays
    api_response = api_instance.workdays_list(content_type, accept, fields=fields, limit=limit, skip=skip, sort=sort, filter=filter, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] [default to []]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[WorkdayOutput]**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_post**
> workdays_post(content_type, accept, body=body, x_org_id=x_org_id)

Create new Workday

This endpoint allows you to create a new workday instance.  You must supply a username and password for `Basic Authentication` that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.  Currently `O-Auth` isn't a supported authentication protocol for WorkDay, but will be in the future.  Currently, only one instance is allowed and it must be `Workday Import`.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/workdays/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{   \"name\": \"Workday2\",   \"reportUrl\":\"https://workday.com/ccx/service/customreport2/gms/user/reportname?format=json\",   \"auth\": {     \"basic\": {       \"username\": \"someDeveloper\",       \"password\": \"notTheRealPassword\"     }   } }' ```

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.WorkdayInput() # WorkdayInput |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Create new Workday
    api_instance.workdays_post(content_type, accept, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**WorkdayInput**](WorkdayInput.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_put**
> WorkdayOutput workdays_put(id, content_type, accept, body=body, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.WorkdayFields() # WorkdayFields |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Update Workday
    api_response = api_instance.workdays_put(id, content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**WorkdayFields**](WorkdayFields.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_settings**
> workdays_settings(content_type, accept, state=state, x_org_id=x_org_id)

Get Workday Settings (incomplete)

This endpoint allows you to obtain all settings needed for creating a workday instance, specifically the URL to initiate Basic Authentication with WorkDay.  **This functionality is currently not enable for users.**

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
state = 'state_example' # str |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Get Workday Settings (incomplete)
    api_instance.workdays_settings(content_type, accept, state=state, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **state** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_workers**
> list[WorkdayWorker] workdays_workers(workday_id, content_type, accept, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)

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
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])
x_org_id = '' # str |  (optional) (default to )

try:
    # List Workday Workers
    api_response = api_instance.workdays_workers(workday_id, content_type, accept, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayImportApi->workdays_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workday_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[WorkdayWorker]**](WorkdayWorker.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

