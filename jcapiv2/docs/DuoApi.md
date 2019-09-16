# jcapiv2.DuoApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**duo_account_get**](DuoApi.md#duo_account_get) | **GET** /duo/accounts/{id} | Get a Duo Acount
[**duo_account_list**](DuoApi.md#duo_account_list) | **GET** /duo/accounts | List Duo Acounts
[**duo_account_post**](DuoApi.md#duo_account_post) | **POST** /duo/accounts | Create Duo Account
[**duo_application_get**](DuoApi.md#duo_application_get) | **GET** /duo/accounts/{account_id}/applications/{application_id} | Get a Duo application
[**duo_application_list**](DuoApi.md#duo_application_list) | **GET** /duo/accounts/{account_id}/applications | List Duo Applications
[**duo_application_post**](DuoApi.md#duo_application_post) | **POST** /duo/accounts/{account_id}/applications | Create Duo Application


# **duo_account_get**
> DuoAccount duo_account_get(id, content_type, accept, x_org_id=x_org_id)

Get a Duo Acount

#### Sample Request ``` curl https://console.jumpcloud.com/api/v2/duo/accounts/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\ ```

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
> list[DuoAccount] duo_account_list(x_api_key, content_type, accept=accept, x_org_id=x_org_id)

List Duo Acounts

#### Sample Request ``` curl https://console.jumpcloud.com/api/v2/duo/accounts \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\ ```

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
x_api_key = 'x_api_key_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'accept_example' # str |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # List Duo Acounts
    api_response = api_instance.duo_account_list(x_api_key, content_type, accept=accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**list[DuoAccount]**](DuoAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_account_post**
> DuoAccount duo_account_post(content_type, accept, body=body, x_org_id=x_org_id)

Create Duo Account

Registers a Duo account for an organization. Only one Duo account will be allowed, in case an organization has a Duo account already a 409 (Conflict) code will be returned.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/duo/accounts \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"registrationApplication\": {       \"apiHost\": \"api-1234.duosecurity.com\",       \"integrationKey\": \"1234\",       \"secretKey\": \"5678\"     }   }' ```

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
body = jcapiv2.DuoRegistrationApplicationReq() # DuoRegistrationApplicationReq |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Create Duo Account
    api_response = api_instance.duo_account_post(content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuoApi->duo_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**DuoRegistrationApplicationReq**](DuoRegistrationApplicationReq.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**DuoAccount**](DuoAccount.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_get**
> DuoApplication duo_application_get(account_id, application_id, content_type, accept, x_org_id=x_org_id)

Get a Duo application

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.DuoApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_list**
> list[DuoApplication] duo_application_list(account_id, content_type, accept, x_org_id=x_org_id)

List Duo Applications

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.DuoApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duo_application_post**
> DuoApplication duo_application_post(account_id, content_type, accept, body=body, x_org_id=x_org_id)

Create Duo Application

Creates a Duo application for an organization and its account.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/duo/accounts/obj-id-123/applications \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"Application Name\",     \"apiHost\": \"api-1234.duosecurity.com\",     \"integrationKey\": \"1234\",     \"secretKey\": \"5678\"   }' ```

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.DuoApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

