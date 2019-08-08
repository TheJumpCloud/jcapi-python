# jcapiv2.SystemInsightsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systeminsights_list_apps**](SystemInsightsApi.md#systeminsights_list_apps) | **GET** /systeminsights/apps | List System Insights Apps
[**systeminsights_list_apps_0**](SystemInsightsApi.md#systeminsights_list_apps_0) | **GET** /systeminsights/{jc_system_id}/apps | List System Insights System Apps
[**systeminsights_list_browser_plugins**](SystemInsightsApi.md#systeminsights_list_browser_plugins) | **GET** /systeminsights/{jc_system_id}/browser_plugins | List System Insights System Browser Plugins
[**systeminsights_list_browser_plugins_0**](SystemInsightsApi.md#systeminsights_list_browser_plugins_0) | **GET** /systeminsights/browser_plugins | List System Insights Browser Plugins
[**systeminsights_list_chrome_extensions**](SystemInsightsApi.md#systeminsights_list_chrome_extensions) | **GET** /systeminsights/{jc_system_id}/chrome_extensions | List System Insights System Chrome Extensions
[**systeminsights_list_chrome_extensions_0**](SystemInsightsApi.md#systeminsights_list_chrome_extensions_0) | **GET** /systeminsights/chrome_extensions | List System Insights Chrome Extensions
[**systeminsights_list_disk_encryption**](SystemInsightsApi.md#systeminsights_list_disk_encryption) | **GET** /systeminsights/disk_encryption | List System Insights Disk Encryption
[**systeminsights_list_disk_encryption_0**](SystemInsightsApi.md#systeminsights_list_disk_encryption_0) | **GET** /systeminsights/{jc_system_id}/disk_encryption | List System Insights System Disk Encryption
[**systeminsights_list_firefox_addons**](SystemInsightsApi.md#systeminsights_list_firefox_addons) | **GET** /systeminsights/firefox_addons | List System Insights Firefox Addons
[**systeminsights_list_firefox_addons_0**](SystemInsightsApi.md#systeminsights_list_firefox_addons_0) | **GET** /systeminsights/{jc_system_id}/firefox_addons | List System Insights System Firefox Addons
[**systeminsights_list_groups**](SystemInsightsApi.md#systeminsights_list_groups) | **GET** /systeminsights/groups | List System Insights Groups
[**systeminsights_list_groups_0**](SystemInsightsApi.md#systeminsights_list_groups_0) | **GET** /systeminsights/{jc_system_id}/groups | List System Insights System Groups
[**systeminsights_list_interface_addresses**](SystemInsightsApi.md#systeminsights_list_interface_addresses) | **GET** /systeminsights/interface_addresses | List System Insights Interface Addresses
[**systeminsights_list_interface_addresses_0**](SystemInsightsApi.md#systeminsights_list_interface_addresses_0) | **GET** /systeminsights/{jc_system_id}/interface_addresses | List System Insights System Interface Addresses
[**systeminsights_list_mounts**](SystemInsightsApi.md#systeminsights_list_mounts) | **GET** /systeminsights/mounts | List System Insights Mounts
[**systeminsights_list_mounts_0**](SystemInsightsApi.md#systeminsights_list_mounts_0) | **GET** /systeminsights/{jc_system_id}/mounts | List System Insights System Mounts
[**systeminsights_list_os_version**](SystemInsightsApi.md#systeminsights_list_os_version) | **GET** /systeminsights/{jc_system_id}/os_version | List System Insights System OS Version
[**systeminsights_list_os_version_0**](SystemInsightsApi.md#systeminsights_list_os_version_0) | **GET** /systeminsights/os_version | List System Insights OS Version
[**systeminsights_list_safari_extensions**](SystemInsightsApi.md#systeminsights_list_safari_extensions) | **GET** /systeminsights/{jc_system_id}/safari_extensions | List System Insights System Safari Extensions
[**systeminsights_list_safari_extensions_0**](SystemInsightsApi.md#systeminsights_list_safari_extensions_0) | **GET** /systeminsights/safari_extensions | List System Insights Safari Extensions
[**systeminsights_list_system_info**](SystemInsightsApi.md#systeminsights_list_system_info) | **GET** /systeminsights/system_info | List System Insights System Info
[**systeminsights_list_system_info_0**](SystemInsightsApi.md#systeminsights_list_system_info_0) | **GET** /systeminsights/{jc_system_id}/system_info | List System Insights System System Info
[**systeminsights_list_users**](SystemInsightsApi.md#systeminsights_list_users) | **GET** /systeminsights/users | List System Insights Users
[**systeminsights_list_users_0**](SystemInsightsApi.md#systeminsights_list_users_0) | **GET** /systeminsights/{jc_system_id}/users | List System Insights System Users


# **systeminsights_list_apps**
> list[SystemInsightsApps] systeminsights_list_apps(limit=limit, skip=skip, filter=filter)

List System Insights Apps

Valid filter fields are `jc_system_id` and `bundle_name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Apps
    api_response = api_instance.systeminsights_list_apps(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsApps]**](SystemInsightsApps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_apps_0**
> list[SystemInsightsApps] systeminsights_list_apps_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Apps

Valid filter fields are `bundle_name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Apps
    api_response = api_instance.systeminsights_list_apps_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_apps_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsApps]**](SystemInsightsApps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_browser_plugins**
> list[SystemInsightsBrowserPlugins] systeminsights_list_browser_plugins(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Browser Plugins

Valid filter fields are `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Browser Plugins
    api_response = api_instance.systeminsights_list_browser_plugins(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_browser_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsBrowserPlugins]**](SystemInsightsBrowserPlugins.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_browser_plugins_0**
> list[SystemInsightsBrowserPlugins] systeminsights_list_browser_plugins_0(limit=limit, skip=skip, filter=filter)

List System Insights Browser Plugins

Valid filter fields are `jc_system_id` and `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Browser Plugins
    api_response = api_instance.systeminsights_list_browser_plugins_0(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_browser_plugins_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsBrowserPlugins]**](SystemInsightsBrowserPlugins.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_chrome_extensions**
> list[SystemInsightsChromeExtensions] systeminsights_list_chrome_extensions(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Chrome Extensions

Valid filter fields are `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Chrome Extensions
    api_response = api_instance.systeminsights_list_chrome_extensions(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_chrome_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsChromeExtensions]**](SystemInsightsChromeExtensions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_chrome_extensions_0**
> list[SystemInsightsChromeExtensions] systeminsights_list_chrome_extensions_0(limit=limit, skip=skip, filter=filter)

List System Insights Chrome Extensions

Valid filter fields are `jc_system_id` and `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Chrome Extensions
    api_response = api_instance.systeminsights_list_chrome_extensions_0(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_chrome_extensions_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsChromeExtensions]**](SystemInsightsChromeExtensions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_disk_encryption**
> list[SystemInsightsDiskEncryption] systeminsights_list_disk_encryption(limit=limit, skip=skip, filter=filter)

List System Insights Disk Encryption

Valid filter fields are `jc_system_id` and `encryption_status`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Disk Encryption
    api_response = api_instance.systeminsights_list_disk_encryption(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_disk_encryption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsDiskEncryption]**](SystemInsightsDiskEncryption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_disk_encryption_0**
> list[SystemInsightsDiskEncryption] systeminsights_list_disk_encryption_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Disk Encryption

Valid filter fields are `encryption_status`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Disk Encryption
    api_response = api_instance.systeminsights_list_disk_encryption_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_disk_encryption_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsDiskEncryption]**](SystemInsightsDiskEncryption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_firefox_addons**
> list[SystemInsightsFirefoxAddons] systeminsights_list_firefox_addons(limit=limit, skip=skip, filter=filter)

List System Insights Firefox Addons

Valid filter fields are `jc_system_id` and `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Firefox Addons
    api_response = api_instance.systeminsights_list_firefox_addons(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_firefox_addons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsFirefoxAddons]**](SystemInsightsFirefoxAddons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_firefox_addons_0**
> list[SystemInsightsFirefoxAddons] systeminsights_list_firefox_addons_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Firefox Addons

Valid filter fields are `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Firefox Addons
    api_response = api_instance.systeminsights_list_firefox_addons_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_firefox_addons_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsFirefoxAddons]**](SystemInsightsFirefoxAddons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_groups**
> list[SystemInsightsGroups] systeminsights_list_groups(limit=limit, skip=skip, filter=filter)

List System Insights Groups

Valid filter fields are `jc_system_id` and `groupname`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Groups
    api_response = api_instance.systeminsights_list_groups(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsGroups]**](SystemInsightsGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_groups_0**
> list[SystemInsightsGroups] systeminsights_list_groups_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Groups

Valid filter fields are `groupname`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Groups
    api_response = api_instance.systeminsights_list_groups_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_groups_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsGroups]**](SystemInsightsGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_interface_addresses**
> list[SystemInsightsInterfaceAddresses] systeminsights_list_interface_addresses(limit=limit, skip=skip, filter=filter)

List System Insights Interface Addresses

Valid filter fields are `jc_system_id` and `address`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Interface Addresses
    api_response = api_instance.systeminsights_list_interface_addresses(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_interface_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsInterfaceAddresses]**](SystemInsightsInterfaceAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_interface_addresses_0**
> list[SystemInsightsInterfaceAddresses] systeminsights_list_interface_addresses_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Interface Addresses

Valid filter fields are `address`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Interface Addresses
    api_response = api_instance.systeminsights_list_interface_addresses_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_interface_addresses_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsInterfaceAddresses]**](SystemInsightsInterfaceAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_mounts**
> list[SystemInsightsMounts] systeminsights_list_mounts(limit=limit, skip=skip, filter=filter)

List System Insights Mounts

Valid filter fields are `jc_system_id` and `path`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Mounts
    api_response = api_instance.systeminsights_list_mounts(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_mounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsMounts]**](SystemInsightsMounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_mounts_0**
> list[SystemInsightsMounts] systeminsights_list_mounts_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Mounts

Valid filter fields are `path`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Mounts
    api_response = api_instance.systeminsights_list_mounts_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_mounts_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsMounts]**](SystemInsightsMounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_os_version**
> list[SystemInsightsOsVersion] systeminsights_list_os_version(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System OS Version

Valid filter fields are `version`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System OS Version
    api_response = api_instance.systeminsights_list_os_version(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_os_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsOsVersion]**](SystemInsightsOsVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_os_version_0**
> list[SystemInsightsOsVersion] systeminsights_list_os_version_0(limit=limit, skip=skip, filter=filter)

List System Insights OS Version

Valid filter fields are `jc_system_id` and `version`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights OS Version
    api_response = api_instance.systeminsights_list_os_version_0(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_os_version_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsOsVersion]**](SystemInsightsOsVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_safari_extensions**
> list[SystemInsightsSafariExtensions] systeminsights_list_safari_extensions(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Safari Extensions

Valid filter fields are `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Safari Extensions
    api_response = api_instance.systeminsights_list_safari_extensions(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_safari_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsSafariExtensions]**](SystemInsightsSafariExtensions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_safari_extensions_0**
> list[SystemInsightsSafariExtensions] systeminsights_list_safari_extensions_0(limit=limit, skip=skip, filter=filter)

List System Insights Safari Extensions

Valid filter fields are `jc_system_id` and `name`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Safari Extensions
    api_response = api_instance.systeminsights_list_safari_extensions_0(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_safari_extensions_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsSafariExtensions]**](SystemInsightsSafariExtensions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_system_info**
> list[SystemInsightsSystemInfo] systeminsights_list_system_info(limit=limit, skip=skip, filter=filter)

List System Insights System Info

Valid filter fields are `jc_system_id` and `cpu_subtype`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Info
    api_response = api_instance.systeminsights_list_system_info(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_system_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsSystemInfo]**](SystemInsightsSystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_system_info_0**
> list[SystemInsightsSystemInfo] systeminsights_list_system_info_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System System Info

Valid filter fields are `cpu_subtype`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System System Info
    api_response = api_instance.systeminsights_list_system_info_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_system_info_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsSystemInfo]**](SystemInsightsSystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_users**
> list[SystemInsightsUsers] systeminsights_list_users(limit=limit, skip=skip, filter=filter)

List System Insights Users

Valid filter fields are `jc_system_id` and `username`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights Users
    api_response = api_instance.systeminsights_list_users(limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsUsers]**](SystemInsightsUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminsights_list_users_0**
> list[SystemInsightsUsers] systeminsights_list_users_0(jc_system_id, limit=limit, skip=skip, filter=filter)

List System Insights System Users

Valid filter fields are `username`.

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SystemInsightsApi()
jc_system_id = 'jc_system_id_example' # str | 
limit = 10 # int |  (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['[]'] # list[str] | Supported operators are: eq (optional) (default to [])

try:
    # List System Insights System Users
    api_response = api_instance.systeminsights_list_users_0(jc_system_id, limit=limit, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemInsightsApi->systeminsights_list_users_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jc_system_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq | [optional] [default to []]

### Return type

[**list[SystemInsightsUsers]**](SystemInsightsUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

