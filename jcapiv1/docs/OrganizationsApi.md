# jcapiv1.OrganizationsApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_list**](OrganizationsApi.md#organization_list) | **GET** /organizations | Get Organization Details
[**organization_put**](OrganizationsApi.md#organization_put) | **PUT** /organizations/{id} | Update an Organization
[**organizations_get**](OrganizationsApi.md#organizations_get) | **GET** /organizations/{id} | Get an Organization


# **organization_list**
> Organizationslist organization_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, search=search)

Get Organization Details

This endpoint returns Organization Details.  #### Sample Request   ``` curl -X GET \\   https://console.jumpcloud.com/api/organizations \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.OrganizationsApi(jcapiv1.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional) (default to )
filter = 'filter_example' # str | A filter to apply to the query. (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending.  (optional) (default to )
search = 'search_example' # str | A nested object containing a string `searchTerm` and a list of `fields` to search on. (optional)

try:
    # Get Organization Details
    api_response = api_instance.organization_list(content_type, accept, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organization_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**| A filter to apply to the query. | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **search** | **str**| A nested object containing a string &#x60;searchTerm&#x60; and a list of &#x60;fields&#x60; to search on. | [optional] 

### Return type

[**Organizationslist**](Organizationslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_put**
> Organization organization_put(id, content_type, accept, body=body)

Update an Organization

This endpoint allows you to update an Organization.  Note: `passwordPolicy` settings are only used when `passwordCompliance` is set to \"custom\". We discourage the use of non-custom passwordCompliance values.  `hasStripeCustomerId` is deprecated and will be removed.  #### Sample Request  ``` curl -X PUT https://console.jumpcloud.com/api/organizations/{OrganizationID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{   \"settings\": {     \"contactName\": \"Admin Name\",     \"contactEmail\": \"admin@company.com\",     \"systemUsersCanEdit\":true,     \"passwordPolicy\": {       \"enableMaxHistory\": true,       \"maxHistory\": 3     }   } }' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.OrganizationsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv1.Body() # Body |  (optional)

try:
    # Update an Organization
    api_response = api_instance.organization_put(id, content_type, accept, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organization_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> InlineResponse2001 organizations_get(id, content_type, accept, fields=fields, filter=filter)

Get an Organization

This endpoint returns a particular Organization.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/organizations/{OrganizationID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv1
from jcapiv1.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv1.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv1.OrganizationsApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
fields = '' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional) (default to )
filter = 'filter_example' # str | A filter to apply to the query. (optional)

try:
    # Get an Organization
    api_response = api_instance.organizations_get(id, content_type, accept, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**| A filter to apply to the query. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

