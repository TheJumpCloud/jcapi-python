# jcapiv1.SearchApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_systems_post**](SearchApi.md#search_systems_post) | **POST** /search/systems | Search Systems
[**search_systemusers_post**](SearchApi.md#search_systemusers_post) | **POST** /search/systemusers | Search System Users


# **search_systems_post**
> Systemuserslist search_systems_post(content_type, accept, body=body, fields=fields, limit=limit, skip=skip)

Search Systems

Return Systems in multi-record format allowing for the passing of the 'filter' parameter. This WILL NOT allow you to add a new system.  To support advanced filtering you can use the `filter` parameter that can only be passed in the body of POST /api/search/* routes. The `filter` parameter must be passed as Content-Type application/json supports advanced filtering using the mongodb JSON query syntax.   The `filter` parameter is an object with a single property, either and or or with the value of the property being an array of query expressions.   This allows you to filter records using the logic of matching ALL or ANY records in the array of query expressions. If the and or or are not included the default behavior is to match ALL query expressions.   #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/search/systemsusers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{ \"filter\" :     {         \"or\" :             [                 {\"hostname\" : { \"$regex\" : \"^www\" }},                 {\"hostname\" : {\"$regex\" : \"^db\"}}             ]     }, \"fields\" : \"os hostname displayName\" }' ```

### Example 
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SearchApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Search() # Search |  (optional)
fields = '' # str | Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned.  (optional) (default to )
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # Search Systems
    api_response = api_instance.search_systems_post(content_type, accept, body=body, fields=fields, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_systems_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Search**](Search.md)|  | [optional] 
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**Systemuserslist**](Systemuserslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_systemusers_post**
> Systemuserslist search_systemusers_post(content_type, accept, body=body, fields=fields, limit=limit, skip=skip)

Search System Users

Return System Users in multi-record format allowing for the passing of the 'filter' parameter. This WILL NOT allow you to add a new system user.  To support advanced filtering you can use the `filter` parameter that can only be passed in the body of POST /api/search/* routes. The `filter` parameter must be passed as Content-Type application/json supports advanced filtering using the mongodb JSON query syntax.   The `filter` parameter is an object with a single property, either and or or with the value of the property being an array of query expressions.   This allows you to filter records using the logic of matching ALL or ANY records in the array of query expressions. If the and or or are not included the default behavior is to match ALL query expressions.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/search/systemsusers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{ \"filter\" : [{\"email\" : { \"$regex\" : \"gmail.com$\"}}], \"fields\" : \"email username sudo\" }' ```

### Example 
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
jcapiv1.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# jcapiv1.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.SearchApi()
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Search() # Search |  (optional)
fields = '' # str | Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned.  (optional) (default to )
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try: 
    # Search System Users
    api_response = api_instance.search_systemusers_post(content_type, accept, body=body, fields=fields, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_systemusers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Search**](Search.md)|  | [optional] 
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**Systemuserslist**](Systemuserslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

