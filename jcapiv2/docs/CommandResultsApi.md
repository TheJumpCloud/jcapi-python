# jcapiv2.CommandResultsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commands_list_results_by_workflow**](CommandResultsApi.md#commands_list_results_by_workflow) | **GET** /commandresult/workflows | List all Command Results by Workflow

# **commands_list_results_by_workflow**
> CommandResultList commands_list_results_by_workflow(x_org_id=x_org_id, limit=limit, filter=filter, skip=skip)

List all Command Results by Workflow

This endpoint returns all command results, grouped by workflowInstanceId.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commandresult/workflows \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key:{API_KEY}'   ```

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
api_instance = jcapiv2.CommandResultsApi(jcapiv2.ApiClient(configuration))
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
limit = 10 # int |  (optional) (default to 10)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List all Command Results by Workflow
    api_response = api_instance.commands_list_results_by_workflow(x_org_id=x_org_id, limit=limit, filter=filter, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommandResultsApi->commands_list_results_by_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**CommandResultList**](CommandResultList.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

