# jcapiv1.UsersApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_totpreset_begin**](UsersApi.md#admin_totpreset_begin) | **POST** /users/resettotp/{id} | Administrator TOTP Reset Initiation
[**users_put**](UsersApi.md#users_put) | **PUT** /users/{id} | Update a user
[**users_reactivate_get**](UsersApi.md#users_reactivate_get) | **GET** /users/reactivate/{id} | Administrator Password Reset Initiation

# **admin_totpreset_begin**
> admin_totpreset_begin(id)

Administrator TOTP Reset Initiation

This endpoint initiates a TOTP reset for an admin. This request does not accept a body.

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
api_instance = jcapiv1.UsersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Administrator TOTP Reset Initiation
    api_instance.admin_totpreset_begin(id)
except ApiException as e:
    print("Exception when calling UsersApi->admin_totpreset_begin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_put**
> Userreturn users_put(id, body=body, x_org_id=x_org_id)

Update a user

This endpoint allows you to update a user.

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
api_instance = jcapiv1.UsersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.Userput() # Userput |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Update a user
    api_response = api_instance.users_put(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Userput**](Userput.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Userreturn**](Userreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_reactivate_get**
> users_reactivate_get(id)

Administrator Password Reset Initiation

This endpoint triggers the sending of a reactivation e-mail to an administrator.

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
api_instance = jcapiv1.UsersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Administrator Password Reset Initiation
    api_instance.users_reactivate_get(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_reactivate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

