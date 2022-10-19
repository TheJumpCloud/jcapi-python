# jcapiv1.SystemusersApi

All URIs are relative to *https://console.jumpcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sshkey_delete**](SystemusersApi.md#sshkey_delete) | **DELETE** /systemusers/{systemuser_id}/sshkeys/{id} | Delete a system user&#x27;s Public SSH Keys
[**sshkey_list**](SystemusersApi.md#sshkey_list) | **GET** /systemusers/{id}/sshkeys | List a system user&#x27;s public SSH keys
[**sshkey_post**](SystemusersApi.md#sshkey_post) | **POST** /systemusers/{id}/sshkeys | Create a system user&#x27;s Public SSH Key
[**systemusers_delete**](SystemusersApi.md#systemusers_delete) | **DELETE** /systemusers/{id} | Delete a system user
[**systemusers_expire**](SystemusersApi.md#systemusers_expire) | **POST** /systemusers/{id}/expire | Expire a system user&#x27;s password
[**systemusers_get**](SystemusersApi.md#systemusers_get) | **GET** /systemusers/{id} | List a system user
[**systemusers_list**](SystemusersApi.md#systemusers_list) | **GET** /systemusers | List all system users
[**systemusers_mfasync**](SystemusersApi.md#systemusers_mfasync) | **POST** /systemusers/{id}/mfasync | Sync a systemuser&#x27;s mfa enrollment status
[**systemusers_post**](SystemusersApi.md#systemusers_post) | **POST** /systemusers | Create a system user
[**systemusers_put**](SystemusersApi.md#systemusers_put) | **PUT** /systemusers/{id} | Update a system user
[**systemusers_resetmfa**](SystemusersApi.md#systemusers_resetmfa) | **POST** /systemusers/{id}/resetmfa | Reset a system user&#x27;s MFA token
[**systemusers_state_activate**](SystemusersApi.md#systemusers_state_activate) | **POST** /systemusers/{id}/state/activate | Activate System User
[**systemusers_unlock**](SystemusersApi.md#systemusers_unlock) | **POST** /systemusers/{id}/unlock | Unlock a system user

# **sshkey_delete**
> str sshkey_delete(systemuser_id, id, x_org_id=x_org_id)

Delete a system user's Public SSH Keys

This endpoint will delete a specific System User's SSH Key.

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
systemuser_id = 'systemuser_id_example' # str | 
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Delete a system user's Public SSH Keys
    api_response = api_instance.sshkey_delete(systemuser_id, id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->sshkey_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **systemuser_id** | **str**|  | 
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sshkey_list**
> list[Sshkeylist] sshkey_list(id, x_org_id=x_org_id)

List a system user's public SSH keys

This endpoint will return a specific System User's public SSH key.

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # List a system user's public SSH keys
    api_response = api_instance.sshkey_list(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->sshkey_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**list[Sshkeylist]**](Sshkeylist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sshkey_post**
> Sshkeylist sshkey_post(id, body=body, x_org_id=x_org_id)

Create a system user's Public SSH Key

This endpoint will create a specific System User's Public SSH Key.

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.Sshkeypost() # Sshkeypost |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Create a system user's Public SSH Key
    api_response = api_instance.sshkey_post(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->sshkey_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Sshkeypost**](Sshkeypost.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Sshkeylist**](Sshkeylist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_delete**
> Systemuserreturn systemusers_delete(id, x_org_id=x_org_id, cascade_manager=cascade_manager)

Delete a system user

This endpoint allows you to delete a particular system user.  #### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/systemusers/{UserID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)
cascade_manager = 'cascade_manager_example' # str | This is an optional flag that can be enabled on the DELETE call, DELETE /systemusers/{id}?cascade_manager=null. This parameter will clear the Manager attribute on all direct reports and then delete the account. (optional)

try:
    # Delete a system user
    api_response = api_instance.systemusers_delete(id, x_org_id=x_org_id, cascade_manager=cascade_manager)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 
 **cascade_manager** | **str**| This is an optional flag that can be enabled on the DELETE call, DELETE /systemusers/{id}?cascade_manager&#x3D;null. This parameter will clear the Manager attribute on all direct reports and then delete the account. | [optional] 

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_expire**
> str systemusers_expire(id, x_org_id=x_org_id)

Expire a system user's password

This endpoint allows you to expire a user's password.

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Expire a system user's password
    api_response = api_instance.systemusers_expire(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_expire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_get**
> Systemuserreturn systemusers_get(id, fields=fields, filter=filter, x_org_id=x_org_id)

List a system user

This endpoint returns a particular System User.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/systemusers/{UserID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str | Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  (optional)
filter = 'filter_example' # str | A filter to apply to the query. See the supported operators below. For more complex searches, see the related `/search/<domain>` endpoints, e.g. `/search/systems`.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** = Supported operators are: - `$eq` (equals) - `$ne` (does not equal) - `$gt` (is greater than) - `$gte` (is greater than or equal to) - `$lt` (is less than) - `$lte` (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the `$` will result in undefined behavior._  **value** = Populate with the value you want to search for. Is case sensitive.  **Examples** - `GET /users?filter=username:$eq:testuser` - `GET /systemusers?filter=password_expiration_date:$lte:2021-10-24` - `GET /systemusers?filter=department:$ne:Accounting` - `GET /systems?filter[0]=firstname:$eq:foo&filter[1]=lastname:$eq:bar` - this will    AND the filters together. - `GET /systems?filter[or][0]=lastname:$eq:foo&filter[or][1]=lastname:$eq:bar` - this will    OR the filters together. (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # List a system user
    api_response = api_instance.systemusers_get(id, fields=fields, filter=filter, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**| Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | **str**| A filter to apply to the query. See the supported operators below. For more complex searches, see the related &#x60;/search/&lt;domain&gt;&#x60; endpoints, e.g. &#x60;/search/systems&#x60;.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D; Supported operators are: - &#x60;$eq&#x60; (equals) - &#x60;$ne&#x60; (does not equal) - &#x60;$gt&#x60; (is greater than) - &#x60;$gte&#x60; (is greater than or equal to) - &#x60;$lt&#x60; (is less than) - &#x60;$lte&#x60; (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the &#x60;$&#x60; will result in undefined behavior._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive.  **Examples** - &#x60;GET /users?filter&#x3D;username:$eq:testuser&#x60; - &#x60;GET /systemusers?filter&#x3D;password_expiration_date:$lte:2021-10-24&#x60; - &#x60;GET /systemusers?filter&#x3D;department:$ne:Accounting&#x60; - &#x60;GET /systems?filter[0]&#x3D;firstname:$eq:foo&amp;filter[1]&#x3D;lastname:$eq:bar&#x60; - this will    AND the filters together. - &#x60;GET /systems?filter[or][0]&#x3D;lastname:$eq:foo&amp;filter[or][1]&#x3D;lastname:$eq:bar&#x60; - this will    OR the filters together. | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_list**
> Systemuserslist systemusers_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter, x_org_id=x_org_id, search=search)

List all system users

This endpoint returns all systemusers.  #### Sample Request  ``` curl -X GET https://console.jumpcloud.com/api/systemusers \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = 'sort_example' # str | The space separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
fields = 'fields_example' # str | The space separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional)
filter = 'filter_example' # str | A filter to apply to the query. See the supported operators below. For more complex searches, see the related `/search/<domain>` endpoints, e.g. `/search/systems`.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** = Supported operators are: - `$eq` (equals) - `$ne` (does not equal) - `$gt` (is greater than) - `$gte` (is greater than or equal to) - `$lt` (is less than) - `$lte` (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the `$` will result in undefined behavior._  **value** = Populate with the value you want to search for. Is case sensitive.  **Examples** - `GET /users?filter=username:$eq:testuser` - `GET /systemusers?filter=password_expiration_date:$lte:2021-10-24` - `GET /systemusers?filter=department:$ne:Accounting` - `GET /systems?filter[0]=firstname:$eq:foo&filter[1]=lastname:$eq:bar` - this will    AND the filters together. - `GET /systems?filter[or][0]=lastname:$eq:foo&filter[or][1]=lastname:$eq:bar` - this will    OR the filters together. (optional)
x_org_id = 'x_org_id_example' # str |  (optional)
search = 'search_example' # str | A nested object containing a `searchTerm` string or array of strings and a list of `fields` to search on. (optional)

try:
    # List all system users
    api_response = api_instance.systemusers_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter, x_org_id=x_org_id, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The space separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **fields** | **str**| The space separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] 
 **filter** | **str**| A filter to apply to the query. See the supported operators below. For more complex searches, see the related &#x60;/search/&lt;domain&gt;&#x60; endpoints, e.g. &#x60;/search/systems&#x60;.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D; Supported operators are: - &#x60;$eq&#x60; (equals) - &#x60;$ne&#x60; (does not equal) - &#x60;$gt&#x60; (is greater than) - &#x60;$gte&#x60; (is greater than or equal to) - &#x60;$lt&#x60; (is less than) - &#x60;$lte&#x60; (is less than or equal to)  _Note: v1 operators differ from v2 operators._  _Note: For v1 operators, excluding the &#x60;$&#x60; will result in undefined behavior._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive.  **Examples** - &#x60;GET /users?filter&#x3D;username:$eq:testuser&#x60; - &#x60;GET /systemusers?filter&#x3D;password_expiration_date:$lte:2021-10-24&#x60; - &#x60;GET /systemusers?filter&#x3D;department:$ne:Accounting&#x60; - &#x60;GET /systems?filter[0]&#x3D;firstname:$eq:foo&amp;filter[1]&#x3D;lastname:$eq:bar&#x60; - this will    AND the filters together. - &#x60;GET /systems?filter[or][0]&#x3D;lastname:$eq:foo&amp;filter[or][1]&#x3D;lastname:$eq:bar&#x60; - this will    OR the filters together. | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **search** | **str**| A nested object containing a &#x60;searchTerm&#x60; string or array of strings and a list of &#x60;fields&#x60; to search on. | [optional] 

### Return type

[**Systemuserslist**](Systemuserslist.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_mfasync**
> systemusers_mfasync(id)

Sync a systemuser's mfa enrollment status

This endpoint allows you to re-sync a user's mfa enrollment status  #### Sample Request ``` curl -X POST \\   https://console.jumpcloud.com/api/systemusers/{UserID}/mfasync \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\  ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Sync a systemuser's mfa enrollment status
    api_instance.systemusers_mfasync(id)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_mfasync: %s\n" % e)
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

# **systemusers_post**
> Systemuserreturn systemusers_post(body=body, x_org_id=x_org_id, full_validation_details=full_validation_details)

Create a system user

\"This endpoint allows you to create a new system user.  #### Default User State The `state` of the user can be explicitly passed in or omitted. If `state` is omitted from the request, then the user will get created using the value returned from the [Get an Organization](https://docs.jumpcloud.com/api/1.0/index.html#operation/organizations_get) endpoint. The default user state for manually created users is stored in `settings.newSystemUserStateDefaults.manualEntry`  These default state values can be changed in the admin portal settings or by using the [Update an Organization](https://docs.jumpcloud.com/api/1.0/index.html#operation/organization_put) endpoint.  #### Sample Request  ``` curl -X POST https://console.jumpcloud.com/api/systemusers \\ -H 'Accept: application/json' \\ -H 'Content-Type: application/json' \\ -H 'x-api-key: {API_KEY}' \\ -d '{       \"username\":\"{username}\",       \"email\":\"{email_address}\",       \"firstname\":\"{Name}\",       \"lastname\":\"{Name}\"     }' ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
body = jcapiv1.Systemuserputpost() # Systemuserputpost |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)
full_validation_details = 'full_validation_details_example' # str | Pass this query parameter when a client wants all validation errors to be returned with a detailed error response for the form field specified. The current form fields are allowed:  * `password`  #### Password validation flag Use the `password` validation flag to receive details on a possible bad request response ``` ?fullValidationDetails=password ``` Without the flag, default behavior will be a normal 400 with only a single validation string error #### Expected Behavior Clients can expect a list of validation error mappings for the validation query field in the details provided on the response: ``` {   \"code\": 400,   \"message\": \"Password validation fail\",   \"status\": \"INVALID_ARGUMENT\",   \"details\": [       {         \"fieldViolationsList\": [           {\"field\": \"password\", \"description\": \"specialCharacter\"}         ],         '@type': 'type.googleapis.com/google.rpc.BadRequest',       },   ], }, ``` (optional)

try:
    # Create a system user
    api_response = api_instance.systemusers_post(body=body, x_org_id=x_org_id, full_validation_details=full_validation_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Systemuserputpost**](Systemuserputpost.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **full_validation_details** | **str**| Pass this query parameter when a client wants all validation errors to be returned with a detailed error response for the form field specified. The current form fields are allowed:  * &#x60;password&#x60;  #### Password validation flag Use the &#x60;password&#x60; validation flag to receive details on a possible bad request response &#x60;&#x60;&#x60; ?fullValidationDetails&#x3D;password &#x60;&#x60;&#x60; Without the flag, default behavior will be a normal 400 with only a single validation string error #### Expected Behavior Clients can expect a list of validation error mappings for the validation query field in the details provided on the response: &#x60;&#x60;&#x60; {   \&quot;code\&quot;: 400,   \&quot;message\&quot;: \&quot;Password validation fail\&quot;,   \&quot;status\&quot;: \&quot;INVALID_ARGUMENT\&quot;,   \&quot;details\&quot;: [       {         \&quot;fieldViolationsList\&quot;: [           {\&quot;field\&quot;: \&quot;password\&quot;, \&quot;description\&quot;: \&quot;specialCharacter\&quot;}         ],         &#x27;@type&#x27;: &#x27;type.googleapis.com/google.rpc.BadRequest&#x27;,       },   ], }, &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_put**
> Systemuserreturn systemusers_put(id, body=body, x_org_id=x_org_id, full_validation_details=full_validation_details)

Update a system user

This endpoint allows you to update a system user.  #### Sample Request  ``` curl -X PUT https://console.jumpcloud.com/api/systemusers/{UserID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{  \"email\":\"{email_address}\",  \"firstname\":\"{Name}\",  \"lastname\":\"{Name}\" }' ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.Systemuserput() # Systemuserput |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)
full_validation_details = 'full_validation_details_example' # str | This endpoint can take in a query when a client wants all validation errors to be returned with error response for the form field specified, i.e. 'password' #### Password validation flag Use the \"password\" validation flag to receive details on a possible bad request response Without the `password` flag, default behavior will be a normal 400 with only a validation string message ``` ?fullValidationDetails=password ``` #### Expected Behavior Clients can expect a list of validation error mappings for the validation query field in the details provided on the response: ``` {   \"code\": 400,   \"message\": \"Password validation fail\",   \"status\": \"INVALID_ARGUMENT\",   \"details\": [       {         \"fieldViolationsList\": [{ \"field\": \"password\", \"description\": \"passwordHistory\" }],         '@type': 'type.googleapis.com/google.rpc.BadRequest',       },   ], }, ``` (optional)

try:
    # Update a system user
    api_response = api_instance.systemusers_put(id, body=body, x_org_id=x_org_id, full_validation_details=full_validation_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Systemuserput**](Systemuserput.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **full_validation_details** | **str**| This endpoint can take in a query when a client wants all validation errors to be returned with error response for the form field specified, i.e. &#x27;password&#x27; #### Password validation flag Use the \&quot;password\&quot; validation flag to receive details on a possible bad request response Without the &#x60;password&#x60; flag, default behavior will be a normal 400 with only a validation string message &#x60;&#x60;&#x60; ?fullValidationDetails&#x3D;password &#x60;&#x60;&#x60; #### Expected Behavior Clients can expect a list of validation error mappings for the validation query field in the details provided on the response: &#x60;&#x60;&#x60; {   \&quot;code\&quot;: 400,   \&quot;message\&quot;: \&quot;Password validation fail\&quot;,   \&quot;status\&quot;: \&quot;INVALID_ARGUMENT\&quot;,   \&quot;details\&quot;: [       {         \&quot;fieldViolationsList\&quot;: [{ \&quot;field\&quot;: \&quot;password\&quot;, \&quot;description\&quot;: \&quot;passwordHistory\&quot; }],         &#x27;@type&#x27;: &#x27;type.googleapis.com/google.rpc.BadRequest&#x27;,       },   ], }, &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Systemuserreturn**](Systemuserreturn.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_resetmfa**
> str systemusers_resetmfa(id, body=body, x_org_id=x_org_id)

Reset a system user's MFA token

This endpoint allows you to reset the TOTP key for a specified system user and put them in an TOTP MFA enrollment period. This will result in the user being prompted to setup TOTP MFA when logging into userportal. Please be aware that if the user does not complete TOTP MFA setup before the `exclusionUntil` date, they will be locked out of any resources that require TOTP MFA.  Please refer to our [Knowledge Base Article](https://support.jumpcloud.com/customer/en/portal/articles/2959138-using-multifactor-authentication-with-jumpcloud) on setting up MFA for more information.  #### Sample Request ``` curl -X POST \\   https://console.jumpcloud.com/api/systemusers/{UserID}/resetmfa \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{\"exclusion\": true, \"exclusionUntil\": \"{date-time}\"}'  ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.IdResetmfaBody() # IdResetmfaBody |  (optional)
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Reset a system user's MFA token
    api_response = api_instance.systemusers_resetmfa(id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_resetmfa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**IdResetmfaBody**](IdResetmfaBody.md)|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_state_activate**
> str systemusers_state_activate(id, body=body)

Activate System User

This endpoint changes the state of a STAGED user to ACTIVATED. #### Email Flag Use the \"email\" flag to determine whether or not to send a Welcome or Activation email to the newly activated user. Sending an empty body without the `email` flag, will send an email with default behavior (see the \"Behavior\" section below) ``` {} ``` Sending `email=true` flag will send an email with default behavior (see `Behavior` below) ``` { \"email\": true } ``` Populated email will override the default behavior and send to the specified email value ``` { \"email\": \"example@example.com\" } ``` Sending `email=false` will suppress sending the email ``` { \"email\": false } ``` #### Behavior Users with a password will be sent a Welcome email to:   - The address specified in `email` flag in the request   - If no `email` flag, the user's primary email address (default behavior) Users without a password will be sent an Activation email to:   - The address specified in `email` flag in the request   - If no `email` flag, the user's alternate email address (default behavior)   - If no alternate email address, the user's primary email address (default behavior)  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/systemusers/{id}/state/activate \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: <api-key>' \\   -d '{ \"email\": \"alternate-activation-email@email.com\" }'  ```

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv1.StateActivateBody() # StateActivateBody |  (optional)

try:
    # Activate System User
    api_response = api_instance.systemusers_state_activate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_state_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**StateActivateBody**](StateActivateBody.md)|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systemusers_unlock**
> str systemusers_unlock(id, x_org_id=x_org_id)

Unlock a system user

This endpoint allows you to unlock a user's account.

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
api_instance = jcapiv1.SystemusersApi(jcapiv1.ApiClient(configuration))
id = 'id_example' # str | 
x_org_id = 'x_org_id_example' # str |  (optional)

try:
    # Unlock a system user
    api_response = api_instance.systemusers_unlock(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_org_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

