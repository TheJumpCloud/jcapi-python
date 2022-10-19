# jcapiv2.CustomEmailsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_emails_create**](CustomEmailsApi.md#custom_emails_create) | **POST** /customemails | Create custom email configuration
[**custom_emails_destroy**](CustomEmailsApi.md#custom_emails_destroy) | **DELETE** /customemails/{custom_email_type} | Delete custom email configuration
[**custom_emails_get_templates**](CustomEmailsApi.md#custom_emails_get_templates) | **GET** /customemail/templates | List custom email templates
[**custom_emails_read**](CustomEmailsApi.md#custom_emails_read) | **GET** /customemails/{custom_email_type} | Get custom email configuration
[**custom_emails_update**](CustomEmailsApi.md#custom_emails_update) | **PUT** /customemails/{custom_email_type} | Update custom email configuration

# **custom_emails_create**
> CustomEmail custom_emails_create(body=body, x_org_id=x_org_id)

Create custom email configuration

Create the custom email configuration for the specified custom email type

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
api_instance = jcapiv2.CustomEmailsApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.CustomEmail() # CustomEmail |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create custom email configuration
    api_response = api_instance.custom_emails_create(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEmailsApi->custom_emails_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomEmail**](CustomEmail.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**CustomEmail**](CustomEmail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_emails_destroy**
> custom_emails_destroy(custom_email_type, x_org_id=x_org_id)

Delete custom email configuration

Delete the custom email configuration for the specified custom email type

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
api_instance = jcapiv2.CustomEmailsApi(jcapiv2.ApiClient(configuration))
custom_email_type = 'custom_email_type_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete custom email configuration
    api_instance.custom_emails_destroy(custom_email_type, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling CustomEmailsApi->custom_emails_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_email_type** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_emails_get_templates**
> list[CustomEmailTemplate] custom_emails_get_templates()

List custom email templates

Get the list of custom email templates

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
api_instance = jcapiv2.CustomEmailsApi(jcapiv2.ApiClient(configuration))

try:
    # List custom email templates
    api_response = api_instance.custom_emails_get_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEmailsApi->custom_emails_get_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomEmailTemplate]**](CustomEmailTemplate.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_emails_read**
> CustomEmail custom_emails_read(custom_email_type, x_org_id=x_org_id)

Get custom email configuration

Get the custom email configuration for the specified custom email type

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
api_instance = jcapiv2.CustomEmailsApi(jcapiv2.ApiClient(configuration))
custom_email_type = 'custom_email_type_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get custom email configuration
    api_response = api_instance.custom_emails_read(custom_email_type, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEmailsApi->custom_emails_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_email_type** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**CustomEmail**](CustomEmail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_emails_update**
> CustomEmail custom_emails_update(custom_email_type, body=body, x_org_id=x_org_id)

Update custom email configuration

Update the custom email configuration for the specified custom email type

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
api_instance = jcapiv2.CustomEmailsApi(jcapiv2.ApiClient(configuration))
custom_email_type = 'custom_email_type_example' # str | 
body = jcapiv2.CustomEmail() # CustomEmail |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update custom email configuration
    api_response = api_instance.custom_emails_update(custom_email_type, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEmailsApi->custom_emails_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_email_type** | **str**|  | 
 **body** | [**CustomEmail**](CustomEmail.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**CustomEmail**](CustomEmail.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

