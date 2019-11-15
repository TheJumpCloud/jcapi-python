# jcapiv2.DefaultApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jc_enrollment_profiles_delete**](DefaultApi.md#jc_enrollment_profiles_delete) | **DELETE** /enrollmentprofiles/{enrollment_profile_id} | Delete Enrollment Profile
[**jc_enrollment_profiles_get**](DefaultApi.md#jc_enrollment_profiles_get) | **GET** /enrollmentprofiles/{enrollment_profile_id} | Get Enrollment Profile
[**jc_enrollment_profiles_list**](DefaultApi.md#jc_enrollment_profiles_list) | **GET** /enrollmentprofiles | List Enrollment Profiles
[**jc_enrollment_profiles_post**](DefaultApi.md#jc_enrollment_profiles_post) | **POST** /enrollmentprofiles | Create new Enrollment Profile
[**jc_enrollment_profiles_put**](DefaultApi.md#jc_enrollment_profiles_put) | **PUT** /enrollmentprofiles/{enrollment_profile_id} | Update Enrollment Profile


# **jc_enrollment_profiles_delete**
> JcEnrollmentProfile jc_enrollment_profiles_delete(enrollment_profile_id)

Delete Enrollment Profile

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
api_instance = jcapiv2.DefaultApi(jcapiv2.ApiClient(configuration))
enrollment_profile_id = 'enrollment_profile_id_example' # str | 

try:
    # Delete Enrollment Profile
    api_response = api_instance.jc_enrollment_profiles_delete(enrollment_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->jc_enrollment_profiles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_profile_id** | **str**|  | 

### Return type

[**JcEnrollmentProfile**](JcEnrollmentProfile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jc_enrollment_profiles_get**
> ERRORUNKNOWN jc_enrollment_profiles_get(enrollment_profile_id, body=body)

Get Enrollment Profile

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
api_instance = jcapiv2.DefaultApi(jcapiv2.ApiClient(configuration))
enrollment_profile_id = 'enrollment_profile_id_example' # str | 
body = jcapiv2.JcEnrollmentProfile() # JcEnrollmentProfile |  (optional)

try:
    # Get Enrollment Profile
    api_response = api_instance.jc_enrollment_profiles_get(enrollment_profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->jc_enrollment_profiles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_profile_id** | **str**|  | 
 **body** | [**JcEnrollmentProfile**](JcEnrollmentProfile.md)|  | [optional] 

### Return type

[**ERRORUNKNOWN**](ERRORUNKNOWN.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jc_enrollment_profiles_list**
> list[JcEnrollmentProfile] jc_enrollment_profiles_list(limit=limit, skip=skip)

List Enrollment Profiles

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
api_instance = jcapiv2.DefaultApi(jcapiv2.ApiClient(configuration))
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List Enrollment Profiles
    api_response = api_instance.jc_enrollment_profiles_list(limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->jc_enrollment_profiles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[JcEnrollmentProfile]**](JcEnrollmentProfile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jc_enrollment_profiles_post**
> JcEnrollmentProfile jc_enrollment_profiles_post(body=body)

Create new Enrollment Profile

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
api_instance = jcapiv2.DefaultApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.Body1() # Body1 |  (optional)

try:
    # Create new Enrollment Profile
    api_response = api_instance.jc_enrollment_profiles_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->jc_enrollment_profiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**JcEnrollmentProfile**](JcEnrollmentProfile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jc_enrollment_profiles_put**
> JcEnrollmentProfile jc_enrollment_profiles_put(enrollment_profile_id, body=body)

Update Enrollment Profile

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
api_instance = jcapiv2.DefaultApi(jcapiv2.ApiClient(configuration))
enrollment_profile_id = 'enrollment_profile_id_example' # str | 
body = jcapiv2.Body2() # Body2 |  (optional)

try:
    # Update Enrollment Profile
    api_response = api_instance.jc_enrollment_profiles_put(enrollment_profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->jc_enrollment_profiles_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_profile_id** | **str**|  | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**JcEnrollmentProfile**](JcEnrollmentProfile.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

