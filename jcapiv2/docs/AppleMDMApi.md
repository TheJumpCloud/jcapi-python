# jcapiv2.AppleMDMApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applemdms_csrget**](AppleMDMApi.md#applemdms_csrget) | **GET** /applemdms/{apple_mdm_id}/csr | Get Apple MDM CSR Plist
[**applemdms_delete**](AppleMDMApi.md#applemdms_delete) | **DELETE** /applemdms/{id} | Delete an Apple MDM
[**applemdms_deletedevice**](AppleMDMApi.md#applemdms_deletedevice) | **DELETE** /applemdms/{apple_mdm_id}/devices/{device_id} | Remove an Apple MDM Device&#x27;s Enrollment
[**applemdms_depkeyget**](AppleMDMApi.md#applemdms_depkeyget) | **GET** /applemdms/{apple_mdm_id}/depkey | Get Apple MDM DEP Public Key
[**applemdms_devices_clear_activation_lock**](AppleMDMApi.md#applemdms_devices_clear_activation_lock) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/clearActivationLock | Clears the Activation Lock for a Device
[**applemdms_devices_refresh_activation_lock_information**](AppleMDMApi.md#applemdms_devices_refresh_activation_lock_information) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/refreshActivationLockInformation | Refresh activation lock information for a device
[**applemdms_deviceserase**](AppleMDMApi.md#applemdms_deviceserase) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/erase | Erase Device
[**applemdms_deviceslist**](AppleMDMApi.md#applemdms_deviceslist) | **GET** /applemdms/{apple_mdm_id}/devices | List AppleMDM Devices
[**applemdms_deviceslock**](AppleMDMApi.md#applemdms_deviceslock) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/lock | Lock Device
[**applemdms_devicesrestart**](AppleMDMApi.md#applemdms_devicesrestart) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/restart | Restart Device
[**applemdms_devicesshutdown**](AppleMDMApi.md#applemdms_devicesshutdown) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/shutdown | Shut Down Device
[**applemdms_enrollmentprofilesget**](AppleMDMApi.md#applemdms_enrollmentprofilesget) | **GET** /applemdms/{apple_mdm_id}/enrollmentprofiles/{id} | Get an Apple MDM Enrollment Profile
[**applemdms_enrollmentprofileslist**](AppleMDMApi.md#applemdms_enrollmentprofileslist) | **GET** /applemdms/{apple_mdm_id}/enrollmentprofiles | List Apple MDM Enrollment Profiles
[**applemdms_getdevice**](AppleMDMApi.md#applemdms_getdevice) | **GET** /applemdms/{apple_mdm_id}/devices/{device_id} | Details of an AppleMDM Device
[**applemdms_list**](AppleMDMApi.md#applemdms_list) | **GET** /applemdms | List Apple MDMs
[**applemdms_put**](AppleMDMApi.md#applemdms_put) | **PUT** /applemdms/{id} | Update an Apple MDM
[**applemdms_refreshdepdevices**](AppleMDMApi.md#applemdms_refreshdepdevices) | **POST** /applemdms/{apple_mdm_id}/refreshdepdevices | Refresh DEP Devices

# **applemdms_csrget**
> AppleMdmSignedCsrPlist applemdms_csrget(apple_mdm_id, x_org_id=x_org_id)

Get Apple MDM CSR Plist

Retrieves an Apple MDM signed CSR Plist for an organization.  The user must supply the returned plist to Apple for signing, and then provide the certificate provided by Apple back into the PUT API.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/csr \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get Apple MDM CSR Plist
    api_response = api_instance.applemdms_csrget(apple_mdm_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_csrget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AppleMdmSignedCsrPlist**](AppleMdmSignedCsrPlist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_delete**
> AppleMDM applemdms_delete(id, x_org_id=x_org_id)

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
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete an Apple MDM
    api_response = api_instance.applemdms_delete(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AppleMDM**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_deletedevice**
> AppleMdmDevice applemdms_deletedevice(apple_mdm_id, device_id, x_org_id=x_org_id)

Remove an Apple MDM Device's Enrollment

Remove a single Apple MDM device from MDM enrollment.  #### Sample Request ```   curl -X DELETE https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id} \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
device_id = 'device_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Remove an Apple MDM Device's Enrollment
    api_response = api_instance.applemdms_deletedevice(apple_mdm_id, device_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_deletedevice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AppleMdmDevice**](AppleMdmDevice.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_depkeyget**
> AppleMdmPublicKeyCert applemdms_depkeyget(apple_mdm_id, x_org_id=x_org_id)

Get Apple MDM DEP Public Key

Retrieves an Apple MDM DEP Public Key.

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
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get Apple MDM DEP Public Key
    api_response = api_instance.applemdms_depkeyget(apple_mdm_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_depkeyget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AppleMdmPublicKeyCert**](AppleMdmPublicKeyCert.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-pem-file

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_devices_clear_activation_lock**
> applemdms_devices_clear_activation_lock(apple_mdm_id, device_id, x_org_id=x_org_id)

Clears the Activation Lock for a Device

Clears the activation lock on the specified device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/clearActivationLock \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
device_id = 'device_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Clears the Activation Lock for a Device
    api_instance.applemdms_devices_clear_activation_lock(apple_mdm_id, device_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_devices_clear_activation_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_devices_refresh_activation_lock_information**
> applemdms_devices_refresh_activation_lock_information(apple_mdm_id, device_id, x_org_id=x_org_id)

Refresh activation lock information for a device

Refreshes the activation lock information for a device  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/refreshActivationLockInformation \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
device_id = 'device_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Refresh activation lock information for a device
    api_instance.applemdms_devices_refresh_activation_lock_information(apple_mdm_id, device_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_devices_refresh_activation_lock_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_deviceserase**
> applemdms_deviceserase(apple_mdm_id, device_id, body=body, x_org_id=x_org_id)

Erase Device

Erases a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/erase \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
device_id = 'device_id_example' # str | 
body = jcapiv2.DeviceIdEraseBody() # DeviceIdEraseBody |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Erase Device
    api_instance.applemdms_deviceserase(apple_mdm_id, device_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_deviceserase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **body** | [**DeviceIdEraseBody**](DeviceIdEraseBody.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_deviceslist**
> list[AppleMdmDevice] applemdms_deviceslist(apple_mdm_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter, sort=sort, x_total_count=x_total_count)

List AppleMDM Devices

Lists all Apple MDM devices.  The filter and sort queries will allow the following fields: `createdAt` `depRegistered` `enrolled` `id` `osVersion` `serialNumber` `udid`  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
x_total_count = 56 # int |  (optional)

try:
    # List AppleMDM Devices
    api_response = api_instance.applemdms_deviceslist(apple_mdm_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter, sort=sort, x_total_count=x_total_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_deviceslist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **x_total_count** | **int**|  | [optional] 

### Return type

[**list[AppleMdmDevice]**](AppleMdmDevice.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_deviceslock**
> applemdms_deviceslock(apple_mdm_id, device_id, body=body, x_org_id=x_org_id)

Lock Device

Locks a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/lock \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
device_id = 'device_id_example' # str | 
body = jcapiv2.DeviceIdLockBody() # DeviceIdLockBody |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Lock Device
    api_instance.applemdms_deviceslock(apple_mdm_id, device_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_deviceslock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **body** | [**DeviceIdLockBody**](DeviceIdLockBody.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_devicesrestart**
> applemdms_devicesrestart(apple_mdm_id, device_id, body=body, x_org_id=x_org_id)

Restart Device

Restarts a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/restart \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{\"kextPaths\": [\"Path1\", \"Path2\"]}' ```

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
device_id = 'device_id_example' # str | 
body = jcapiv2.DeviceIdRestartBody() # DeviceIdRestartBody |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Restart Device
    api_instance.applemdms_devicesrestart(apple_mdm_id, device_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_devicesrestart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **body** | [**DeviceIdRestartBody**](DeviceIdRestartBody.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_devicesshutdown**
> applemdms_devicesshutdown(apple_mdm_id, device_id, x_org_id=x_org_id)

Shut Down Device

Shuts down a DEP-enrolled device.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id}/shutdown \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
device_id = 'device_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Shut Down Device
    api_instance.applemdms_devicesshutdown(apple_mdm_id, device_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_devicesshutdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_enrollmentprofilesget**
> Mobileconfig applemdms_enrollmentprofilesget(apple_mdm_id, id, x_org_id=x_org_id)

Get an Apple MDM Enrollment Profile

Get an enrollment profile  Currently only requesting the mobileconfig is supported.  #### Sample Request  ``` curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles/{ID} \\   -H 'accept: application/x-apple-aspen-config' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get an Apple MDM Enrollment Profile
    api_response = api_instance.applemdms_enrollmentprofilesget(apple_mdm_id, id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_enrollmentprofilesget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**Mobileconfig**](Mobileconfig.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-apple-aspen-config

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_enrollmentprofileslist**
> list[AppleMDM] applemdms_enrollmentprofileslist(apple_mdm_id, x_org_id=x_org_id)

List Apple MDM Enrollment Profiles

Get a list of enrollment profiles for an apple mdm.  Note: currently only one enrollment profile is supported.  #### Sample Request ```  curl https://console.jumpcloud.com/api/v2/applemdms/{APPLE_MDM_ID}/enrollmentprofiles \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Apple MDM Enrollment Profiles
    api_response = api_instance.applemdms_enrollmentprofileslist(apple_mdm_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_enrollmentprofileslist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[AppleMDM]**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_getdevice**
> AppleMdmDevice applemdms_getdevice(apple_mdm_id, device_id, x_org_id=x_org_id)

Details of an AppleMDM Device

Gets a single Apple MDM device.  #### Sample Request ```   curl -X GET https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/devices/{device_id} \\   -H 'accept: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
device_id = 'device_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Details of an AppleMDM Device
    api_response = api_instance.applemdms_getdevice(apple_mdm_id, device_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_getdevice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **device_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AppleMdmDevice**](AppleMdmDevice.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_list**
> list[AppleMDM] applemdms_list(x_org_id=x_org_id)

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
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Apple MDMs
    api_response = api_instance.applemdms_list(x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[AppleMDM]**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_put**
> AppleMDM applemdms_put(id, body=body, x_org_id=x_org_id)

Update an Apple MDM

Updates an Apple MDM configuration.  This endpoint is used to supply JumpCloud with a signed certificate from Apple in order to finalize the setup and allow JumpCloud to manage your devices.  It may also be used to update the DEP Settings.  #### Sample Request ```   curl -X PUT https://console.jumpcloud.com/api/v2/applemdms/{ID} \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"MDM name\",     \"appleSignedCert\": \"{CERTIFICATE}\",     \"encryptedDepServerToken\": \"{SERVER_TOKEN}\",     \"dep\": {       \"welcomeScreen\": {         \"title\": \"Welcome\",         \"paragraph\": \"In just a few steps, you will be working securely from your Mac.\",         \"button\": \"continue\",       },     },   }' ```

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
id = 'id_example' # str | 
body = jcapiv2.AppleMdmPatchInput() # AppleMdmPatchInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Update an Apple MDM
    api_response = api_instance.applemdms_put(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AppleMdmPatchInput**](AppleMdmPatchInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**AppleMDM**](AppleMDM.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applemdms_refreshdepdevices**
> applemdms_refreshdepdevices(apple_mdm_id, x_org_id=x_org_id)

Refresh DEP Devices

Refreshes the list of devices that a JumpCloud admin has added to their virtual MDM in Apple Business Manager - ABM so that they can be DEP enrolled with JumpCloud.  #### Sample Request ```   curl -X POST https://console.jumpcloud.com/api/v2/applemdms/{apple_mdm_id}/refreshdepdevices \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{}' ```

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
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Refresh DEP Devices
    api_instance.applemdms_refreshdepdevices(apple_mdm_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling AppleMDMApi->applemdms_refreshdepdevices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_mdm_id** | **str**|  | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

