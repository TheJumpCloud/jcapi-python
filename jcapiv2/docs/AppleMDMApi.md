# jcapiv2.AppleMDMApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applemdms_delete**](AppleMDMApi.md#applemdms_delete) | **DELETE** /applemdms/{apple_mdm_id} | Delete an Apple MDM
[**applemdms_list**](AppleMDMApi.md#applemdms_list) | **GET** /applemdms | List Apple MDMs
[**applemdms_post**](AppleMDMApi.md#applemdms_post) | **POST** /applemdms | Create Apple MDM
[**applemdms_put**](AppleMDMApi.md#applemdms_put) | **PUT** /applemdms/{apple_mdm_id} | Update an Apple MDM
[**enrollmentprofiles_get**](AppleMDMApi.md#enrollmentprofiles_get) | **GET** /applemdms/{apple_mdm_id}/enrollmentprofiles/{enrollment_profile_id} | Get an Apple MDM Enrollment Profile
[**enrollmentprofiles_list**](AppleMDMApi.md#enrollmentprofiles_list) | **GET** /applemdms/{apple_mdm_id}/enrollmentprofiles | List Apple MDM Enrollment Profiles


# **applemdms_delete**
> AppleMDM applemdms_delete(apple_mdm_id, content_type, accept, x_org_id=x_org_id)

Delete an Apple MDM

Removes an Apple MDM configuration.  Warning: This is a destructive operation and will remove your Apple Push Certificates.  We will no longer be able to manage your devices and the only recovery option is to re-register all devices into MDM.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/applemdms/{id} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AppleMDMApi(jcapiv2.ApiClient(configuration))
apple_mdm_id = 'apple_mdm_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Delete an Apple MDM
    api_response = api_instance.applemdms_delete(apple_mdm_id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**AppleMDM**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_list**
> list[AppleMDM] applemdms_list(content_type, accept, x_org_id=x_org_id)

List Apple MDMs

Get a list of all Apple MDM configurations.  An empty topic indicates that a signed certificate from Apple has not been provided to the PUT endpoint yet.  Note: currently only one MDM configuration per organization is supported.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/applemdms \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AppleMDMApi(jcapiv2.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # List Apple MDMs
    api_response = api_instance.applemdms_list(content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[AppleMDM]**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_post**
> InlineResponse201 applemdms_post(content_type, accept, body=body, x_org_id=x_org_id)

Create Apple MDM

Creates an Apple MDM Enrollment for an organization. Only one enrollment per organization will be allowed.  Note that this is the first step in completly setting up an MDM Enrollment.  The user must supply the returned plist to Apple for signing, and then provide the certificate provided by Apple back into the PUT API.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/organizations/{Organization_ID}/mdm \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
api_instance = jcapiv2.AppleMDMApi(jcapiv2.ApiClient(configuration))
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.Body() # Body |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Create Apple MDM
    api_response = api_instance.applemdms_post(content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**Body**](Body.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_put**
> AppleMDM applemdms_put(apple_mdm_id, content_type, accept, body=body, x_org_id=x_org_id)

Update an Apple MDM

Updates an Apple MDM configuration.  This endpoint is used to supply JumpCloud with a signed certificate from Apple in order to finalize the setup and allow JumpCloud to manage your devices.  #### Sample Request ```   curl -X PUT https://console.jumpcloud.com/api/v2/applemdms/{ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"MDM name\",     \"appleSignedCert\": \"{CERTIFICATE}\"   }' ```

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
api_instance = jcapiv2.AppleMDMApi(jcapiv2.ApiClient(configuration))
apple_mdm_id = 'apple_mdm_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
body = jcapiv2.AppleMdmPatchInput() # AppleMdmPatchInput |  (optional)
x_org_id = '' # str |  (optional) (default to )

try:
    # Update an Apple MDM
    api_response = api_instance.applemdms_put(apple_mdm_id, content_type, accept, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **body** | [**AppleMdmPatchInput**](AppleMdmPatchInput.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**AppleMDM**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollmentprofiles_get**
> Mobileconfig enrollmentprofiles_get(apple_mdm_id, enrollment_profile_id, content_type, accept, x_org_id=x_org_id)

Get an Apple MDM Enrollment Profile

Get an enrollment profile  Currently only requesting the mobileconfig is supported.  #### Sample Request  ``` curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles/{ENROLLMENT_PROFILE_ID} \\   -H 'accept: application/x-apple-aspen-config' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AppleMDMApi(jcapiv2.ApiClient(configuration))
apple_mdm_id = 'apple_mdm_id_example' # str | 
enrollment_profile_id = 'enrollment_profile_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # Get an Apple MDM Enrollment Profile
    api_response = api_instance.enrollmentprofiles_get(apple_mdm_id, enrollment_profile_id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->enrollmentprofiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **enrollment_profile_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**Mobileconfig**](Mobileconfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-apple-aspen-config

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollmentprofiles_list**
> list[AppleMDM] enrollmentprofiles_list(apple_mdm_id, content_type, accept, x_org_id=x_org_id)

List Apple MDM Enrollment Profiles

Get a list of enrollment profiles for an apple mdm.  Note: currently only one enrollment profile is supported.  #### Sample Request ``` curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.AppleMDMApi(jcapiv2.ApiClient(configuration))
apple_mdm_id = 'apple_mdm_id_example' # str | 
content_type = 'application/json' # str |  (default to application/json)
accept = 'application/json' # str |  (default to application/json)
x_org_id = '' # str |  (optional) (default to )

try:
    # List Apple MDM Enrollment Profiles
    api_response = api_instance.enrollmentprofiles_list(apple_mdm_id, content_type, accept, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->enrollmentprofiles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **content_type** | **str**|  | [default to application/json]
 **accept** | **str**|  | [default to application/json]
 **x_org_id** | **str**|  | [optional] [default to ]

### Return type

[**list[AppleMDM]**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

