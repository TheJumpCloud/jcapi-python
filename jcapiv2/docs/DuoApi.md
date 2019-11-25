# jcapiv2.DuoApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**duo_account_delete**](DuoApi.md#duo_account_delete) | **DELETE** /duo/accounts/{id} | Delete a Duo Account
[**duo_account_get**](DuoApi.md#duo_account_get) | **GET** /duo/accounts/{id} | Get a Duo Acount
[**duo_account_list**](DuoApi.md#duo_account_list) | **GET** /duo/accounts | List Duo Acounts
[**duo_account_post**](DuoApi.md#duo_account_post) | **POST** /duo/accounts | Create Duo Account
[**duo_application_delete**](DuoApi.md#duo_application_delete) | **DELETE** /duo/accounts/{account_id}/applications/{application_id} | Delete a Duo Application
[**duo_application_get**](DuoApi.md#duo_application_get) | **GET** /duo/accounts/{account_id}/applications/{application_id} | Get a Duo application
[**duo_application_list**](DuoApi.md#duo_application_list) | **GET** /duo/accounts/{account_id}/applications | List Duo Applications
[**duo_application_post**](DuoApi.md#duo_application_post) | **POST** /duo/accounts/{account_id}/applications | Create Duo Application
[**duo_application_update**](DuoApi.md#duo_application_update) | **PUT** /duo/accounts/{account_id}/applications/{application_id} | Update Duo Application


# **duo_account_delete**
> DuoAccount duo_account_delete(id, content_type, accept, x_org_id=x_org_id)

Delete a Duo Account

Removes the specified Duo account, an error will be returned if the account has some Duo application used in a protected resource.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/duo/accounts/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | ObjectID of the Duo Account
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Delete a Duo Account
    api_response = api_instance.duo_account_delete(id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the Duo Account | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoAccount**](DuoAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_account_get**
> DuoAccount duo_account_get(id, content_type, accept, x_org_id=x_org_id)

Get a Duo Acount

This endpoint returns a specific Duo account.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/duo/accounts/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | ObjectID of the Duo Account
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Get a Duo Acount
    api_response = api_instance.duo_account_get(id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the Duo Account | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoAccount**](DuoAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_account_list**
> list[DuoAccount] duo_account_list(content_type, accept, x_org_id=x_org_id)

List Duo Acounts

This endpoint returns all the Duo accounts for your organization. Note: There can currently only be one Duo account for your organization.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/duo/accounts \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # List Duo Acounts
    api_response = api_instance.duo_account_list(content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[DuoAccount]**](DuoAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_account_post**
> DuoAccount duo_account_post(content_type, accept, x_org_id=x_org_id)

Create Duo Account

Registers a Duo account for an organization. Only one Duo account will be allowed, in case an organization has a Duo account already a 409 (Conflict) code will be returned.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/duo/accounts \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Create Duo Account
    api_response = api_instance.duo_account_post(content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoAccount**](DuoAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_delete**
> DuoApplication duo_application_delete(account_id, application_id, content_type, accept, x_org_id=x_org_id)

Delete a Duo Application

Deletes the specified Duo application, an error will be returned if the application is used in a protected resource.  #### Sample Request ```   curl -X DELETE https://console.jumpcloud.com/api/v2/duo/accounts/{ACCOUNT_ID}/applications/{APPLICATION_ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}'' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
account_id = 'account_id_example' # str | 
application_id = 'application_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Delete a Duo Application
    api_response = api_instance.duo_application_delete(account_id, application_id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_application_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **application_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoApplication**](DuoApplication.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_get**
> DuoApplication duo_application_get(account_id, application_id, content_type, accept, x_org_id=x_org_id)

Get a Duo application

This endpoint returns a specific Duo application that is associated with the specified Duo account.  #### Sample Request ```   curl https://console.jumpcloud.com/api/v2/duo/accounts/{ACCOUNT_ID}/applications/{APPLICATION_ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
account_id = 'account_id_example' # str | 
application_id = 'application_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Get a Duo application
    api_response = api_instance.duo_application_get(account_id, application_id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_application_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **application_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoApplication**](DuoApplication.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_list**
> list[DuoApplication] duo_application_list(account_id, content_type, accept, x_org_id=x_org_id)

List Duo Applications

This endpoint returns all the Duo applications for the specified Duo account. Note: There can currently only be one Duo application for your organization.  #### Sample Request ```   curl https://console.jumpcloud.com/api/v2/duo/accounts/{ACCOUNT_ID}/applications \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
account_id = 'account_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # List Duo Applications
    api_response = api_instance.duo_application_list(account_id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_application_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[DuoApplication]**](DuoApplication.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_post**
> DuoApplication duo_application_post(account_id, content_type, accept, body=body, x_org_id=x_org_id)

Create Duo Application

Creates a Duo application for your organization and the specified account.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/duo/accounts/{ACCOUNT_ID}/applications \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Application Name\",     \"apiHost\": \"api-1234.duosecurity.com\",     \"integrationKey\": \"1234\",     \"secretKey\": \"5678\"   }' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
account_id = 'account_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.DuoApplicationReq() # DuoApplicationReq |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Create Duo Application
    api_response = api_instance.duo_application_post(account_id, content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_application_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**DuoApplicationReq**](DuoApplicationReq.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoApplication**](DuoApplication.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_update**
> DuoApplication duo_application_update(account_id, application_id, content_type, accept, body=body, x_org_id=x_org_id)

Update Duo Application

Updates the specified Duo application.  #### Sample Request ```   curl -X PUT https://console.jumpcloud.com/api/v2/duo/accounts/{ACCOUNT_ID}/applications/{APPLICATION_ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Application Name\",     \"apiHost\": \"api-1234.duosecurity.com\",     \"integrationKey\": \"1234\",     \"secretKey\": \"5678\"   }' ```

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
api_instance = jcapiv2.DuoApi(jcapiv2.ApiClient(configuration))
account_id = 'account_id_example' # str | 
application_id = 'application_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.DuoApplicationUpdateReq() # DuoApplicationUpdateReq |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Update Duo Application
    api_response = api_instance.duo_application_update(account_id, application_id, content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_application_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **application_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**DuoApplicationUpdateReq**](DuoApplicationUpdateReq.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoApplication**](DuoApplication.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

