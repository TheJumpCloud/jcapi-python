# jcapiv2.AuthenticationPoliciesApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authnpolicies_delete**](AuthenticationPoliciesApi.md#authnpolicies_delete) | **DELETE** /authn/policies/{id} | Delete Authentication Policy
[**authnpolicies_get**](AuthenticationPoliciesApi.md#authnpolicies_get) | **GET** /authn/policies/{id} | Get an authentication policy
[**authnpolicies_list**](AuthenticationPoliciesApi.md#authnpolicies_list) | **GET** /authn/policies | List Authentication Policies
[**authnpolicies_patch**](AuthenticationPoliciesApi.md#authnpolicies_patch) | **PATCH** /authn/policies/{id} | Patch Authentication Policy
[**authnpolicies_post**](AuthenticationPoliciesApi.md#authnpolicies_post) | **POST** /authn/policies | Create an Authentication Policy

# **authnpolicies_delete**
> AuthnPolicy authnpolicies_delete(id, x_org_id=x_org_id)

Delete Authentication Policy

Delete the specified authentication policy.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/authn/policies/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AuthenticationPoliciesApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the authentication policy
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete Authentication Policy
    api_response = api_instance.authnpolicies_delete(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->authnpolicies_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the authentication policy | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AuthnPolicy**](AuthnPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authnpolicies_get**
> AuthnPolicy authnpolicies_get(id, x_org_id=x_org_id)

Get an authentication policy

Return a specific authentication policy.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/authn/policies/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AuthenticationPoliciesApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the authentication policy
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get an authentication policy
    api_response = api_instance.authnpolicies_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->authnpolicies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the authentication policy | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AuthnPolicy**](AuthnPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authnpolicies_list**
> list[AuthnPolicy] authnpolicies_list(x_org_id=x_org_id, x_total_count=x_total_count, limit=limit, skip=skip, filter=filter, sort=sort)

List Authentication Policies

Get a list of all authentication policies.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/authn/policies \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AuthenticationPoliciesApi(jcapiv2.ApiClient(configuration))
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
x_total_count = 56 # int |  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # List Authentication Policies
    api_response = api_instance.authnpolicies_list(x_org_id=x_org_id, x_total_count=x_total_count, limit=limit, skip=skip, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->authnpolicies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **x_total_count** | **int**|  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**list[AuthnPolicy]**](AuthnPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authnpolicies_patch**
> AuthnPolicy authnpolicies_patch(id, body=body, x_org_id=x_org_id)

Patch Authentication Policy

Patch the specified authentication policy.  #### Sample Request ``` curl -X PATCH https://console.jumpcloud.com/api/v2/authn/policies/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{ \"disabled\": false }' ```

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
api_instance = jcapiv2.AuthenticationPoliciesApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | Unique identifier of the authentication policy
body = jcapiv2.AuthnPolicyInput() # AuthnPolicyInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Patch Authentication Policy
    api_response = api_instance.authnpolicies_patch(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->authnpolicies_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the authentication policy | 
 **body** | [**AuthnPolicyInput**](AuthnPolicyInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AuthnPolicy**](AuthnPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authnpolicies_post**
> AuthnPolicy authnpolicies_post(body=body, x_org_id=x_org_id)

Create an Authentication Policy

Create an authentication policy.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/authn/policies \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Sample Policy\",     \"disabled\": false,     \"effect\": {       \"action\": \"allow\"     },     \"targets\": {       \"users\": {         \"inclusions\": [\"ALL\"]       },       \"userGroups\": {         \"exclusions\": [{USER_GROUP_ID}]       },       \"resources\": [ {\"type\": \"user_portal\" } ]     },     \"conditions\":{       \"ipAddressIn\": [{IP_LIST_ID}]     }   }' ```

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
api_instance = jcapiv2.AuthenticationPoliciesApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.AuthnPolicyInput() # AuthnPolicyInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create an Authentication Policy
    api_response = api_instance.authnpolicies_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationPoliciesApi->authnpolicies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthnPolicyInput**](AuthnPolicyInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AuthnPolicy**](AuthnPolicy.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

