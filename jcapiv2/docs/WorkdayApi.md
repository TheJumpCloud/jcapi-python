# jcapiv2.WorkdayApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workdays_authorize**](WorkdayApi.md#workdays_authorize) | **POST** /workdays/{id}/authorize | Authorize Workday
[**workdays_deauthorize**](WorkdayApi.md#workdays_deauthorize) | **POST** /workdays/{id}/deauthorize | Deauthorize Workday
[**workdays_delete**](WorkdayApi.md#workdays_delete) | **DELETE** /workdays/{id} | Delete Workday
[**workdays_get**](WorkdayApi.md#workdays_get) | **GET** /workdays/{id} | Get Workday
[**workdays_list**](WorkdayApi.md#workdays_list) | **GET** /workdays | List Workdays
[**workdays_post**](WorkdayApi.md#workdays_post) | **POST** /workdays | Create new Workday
[**workdays_put**](WorkdayApi.md#workdays_put) | **PUT** /workdays/{id} | Update Workday
[**workdays_report**](WorkdayApi.md#workdays_report) | **GET** /workdays/{id}/report | Get Workday Report Results
[**workdays_settings**](WorkdayApi.md#workdays_settings) | **GET** /workdays/settings | Get Workday Settings


# **workdays_authorize**
> workdays_authorize(id, content_type, accept, body=body)

Authorize Workday

Adds an authorization method to a workday instance

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
api_instance = jcapiv2.WorkdayApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.AuthInput() # AuthInput |  (optional)

try: 
    # Authorize Workday
    api_instance.workdays_authorize(id, content_type, accept, body=body)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_authorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**AuthInput**](AuthInput.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_deauthorize**
> workdays_deauthorize(id, content_type, accept)

Deauthorize Workday

Removes any and all authorization methods from the workday instance

### Example 
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.WorkdayApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)

try: 
    # Deauthorize Workday
    api_instance.workdays_deauthorize(id, content_type, accept)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_deauthorize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_delete**
> object workdays_delete(id, content_type, accept)

Delete Workday

This endpoint allows you to delete an instance of Workday.

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
api_instance = jcapiv2.WorkdayApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)

try: 
    # Delete Workday
    api_response = api_instance.workdays_delete(id, content_type, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]

### Return type

**object**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_get**
> WorkdayOutput workdays_get(id, content_type, accept)

Get Workday

This endpoint will return  all the available information about an instance of Workday.

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
api_instance = jcapiv2.WorkdayApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)

try: 
    # Get Workday
    api_response = api_instance.workdays_get(id, content_type, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_list**
> list[WorkdayOutput] workdays_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List Workdays

This endpoint will return  all the available information about all your instances of Workday.

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
api_instance = jcapiv2.WorkdayApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str | Supported operators are: eq, ne, gt, ge, lt, le, between, search (optional) (default to )
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )

try: 
    # List Workdays
    api_response = api_instance.workdays_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_list: %s\n" % e)
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

[**list[WorkdayOutput]**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_post**
> WorkdayOutput workdays_post(content_type, accept, body=body)

Create new Workday

This endpoint allows you to create a new workday instance.  You must supply a username and password for Basic Authentication that is the same as your WorkDay Integrator System User.  Failure to provide these credentials  will result in the request being rejected.

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
api_instance = jcapiv2.WorkdayApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.Body1() # Body1 |  (optional)

try: 
    # Create new Workday
    api_response = api_instance.workdays_post(content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_put**
> WorkdayOutput workdays_put(id, content_type, accept, body=body)

Update Workday

This endpoint allows you to update the name and Custom Report URL for a Workday Instance.

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
api_instance = jcapiv2.WorkdayApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.Body() # Body |  (optional)

try: 
    # Update Workday
    api_response = api_instance.workdays_put(id, content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**WorkdayOutput**](WorkdayOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_report**
> WorkdayReportResult workdays_report(id, content_type, accept, fields=fields, filter=filter, sort=sort, skip=skip)

Get Workday Report Results

This endpoint will return all of the data available in your WorkDay Custom Report that has been associated with your WorkDay Instance.

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
api_instance = jcapiv2.WorkdayApi()
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str | Supported operators are: eq, ne, gt, ge, lt, le, between, search (optional) (default to )
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # Get Workday Report Results
    api_response = api_instance.workdays_report(id, content_type, accept, fields=fields, filter=filter, sort=sort, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**| Supported operators are: eq, ne, gt, ge, lt, le, between, search | [optional] [default to ]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**WorkdayReportResult**](WorkdayReportResult.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workdays_settings**
> InlineResponse200 workdays_settings(content_type, accept, state=state)

Get Workday Settings

This endpoint allows you to obtain all settings needed for creating a workday instance, specifically the URL to initiate Basic Authentication with WorkDay.

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
api_instance = jcapiv2.WorkdayApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
state = 'state_example' # str |  (optional)

try: 
    # Get Workday Settings
    api_response = api_instance.workdays_settings(content_type, accept, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkdayApi->workdays_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **state** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

