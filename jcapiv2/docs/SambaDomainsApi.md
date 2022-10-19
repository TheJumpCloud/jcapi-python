# jcapiv2.SambaDomainsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ldapservers_samba_domains_delete**](SambaDomainsApi.md#ldapservers_samba_domains_delete) | **DELETE** /ldapservers/{ldapserver_id}/sambadomains/{id} | Delete Samba Domain
[**ldapservers_samba_domains_get**](SambaDomainsApi.md#ldapservers_samba_domains_get) | **GET** /ldapservers/{ldapserver_id}/sambadomains/{id} | Get Samba Domain
[**ldapservers_samba_domains_list**](SambaDomainsApi.md#ldapservers_samba_domains_list) | **GET** /ldapservers/{ldapserver_id}/sambadomains | List Samba Domains
[**ldapservers_samba_domains_post**](SambaDomainsApi.md#ldapservers_samba_domains_post) | **POST** /ldapservers/{ldapserver_id}/sambadomains | Create Samba Domain
[**ldapservers_samba_domains_put**](SambaDomainsApi.md#ldapservers_samba_domains_put) | **PUT** /ldapservers/{ldapserver_id}/sambadomains/{id} | Update Samba Domain

# **ldapservers_samba_domains_delete**
> str ldapservers_samba_domains_delete(ldapserver_id, id, x_org_id=x_org_id)

Delete Samba Domain

This endpoint allows you to delete a samba domain from an LDAP server.  ##### Sample Request ``` curl -X DELETE https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/sambadomains/{SAMBA_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.SambaDomainsApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | Unique identifier of the LDAP server.
id = 'id_example' # str | Unique identifier of the samba domain.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete Samba Domain
    api_response = api_instance.ldapservers_samba_domains_delete(ldapserver_id, id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SambaDomainsApi->ldapservers_samba_domains_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| Unique identifier of the LDAP server. | 
 **id** | **str**| Unique identifier of the samba domain. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_samba_domains_get**
> SambaDomainOutput ldapservers_samba_domains_get(ldapserver_id, id, x_org_id=x_org_id)

Get Samba Domain

This endpoint returns a specific samba domain for an LDAP server.  ##### Sample Request ``` curl -X GET \\   https://console.jumpcloud.com/api/v2/ldapservers/ldapservers/{LDAP_ID}/sambadomains/{SAMBA_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.SambaDomainsApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | Unique identifier of the LDAP server.
id = 'id_example' # str | Unique identifier of the samba domain.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get Samba Domain
    api_response = api_instance.ldapservers_samba_domains_get(ldapserver_id, id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SambaDomainsApi->ldapservers_samba_domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| Unique identifier of the LDAP server. | 
 **id** | **str**| Unique identifier of the samba domain. | 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**SambaDomainOutput**](SambaDomainOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_samba_domains_list**
> list[SambaDomainOutput] ldapservers_samba_domains_list(ldapserver_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)

List Samba Domains

This endpoint returns all samba domains for an LDAP server.  ##### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/sambadomains \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

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
api_instance = jcapiv2.SambaDomainsApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | Unique identifier of the LDAP server.
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Samba Domains
    api_response = api_instance.ldapservers_samba_domains_list(ldapserver_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SambaDomainsApi->ldapservers_samba_domains_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| Unique identifier of the LDAP server. | 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**list[SambaDomainOutput]**](SambaDomainOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_samba_domains_post**
> SambaDomainOutput ldapservers_samba_domains_post(ldapserver_id, body=body, x_org_id=x_org_id)

Create Samba Domain

This endpoint allows you to create a samba domain for an LDAP server.  ##### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/sambadomains \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"sid\":\"{SID_ID}\",     \"name\":\"{WORKGROUP_NAME}\"   }' ```

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
api_instance = jcapiv2.SambaDomainsApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | Unique identifier of the LDAP server.
body = jcapiv2.SambaDomainInput() # SambaDomainInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create Samba Domain
    api_response = api_instance.ldapservers_samba_domains_post(ldapserver_id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SambaDomainsApi->ldapservers_samba_domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| Unique identifier of the LDAP server. | 
 **body** | [**SambaDomainInput**](SambaDomainInput.md)|  | [optional] 
 **x_org_id** | **str**| Organization identifier that can be obtained from console settings. | [optional] 

### Return type

[**SambaDomainOutput**](SambaDomainOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldapservers_samba_domains_put**
> SambaDomainOutput ldapservers_samba_domains_put(ldapserver_id, id, body=body)

Update Samba Domain

This endpoint allows you to update the samba domain information for an LDAP server.  ##### Sample Request ``` curl -X PUT https://console.jumpcloud.com/api/v2/ldapservers/{LDAP_ID}/sambadomains/{SAMBA_ID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"sid\":\"{SID_ID}\",     \"name\":\"{WORKGROUP_NAME}\"   }' ```

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
api_instance = jcapiv2.SambaDomainsApi(jcapiv2.ApiClient(configuration))
ldapserver_id = 'ldapserver_id_example' # str | Unique identifier of the LDAP server.
id = 'id_example' # str | Unique identifier of the samba domain.
body = jcapiv2.SambaDomainInput() # SambaDomainInput |  (optional)

try:
    # Update Samba Domain
    api_response = api_instance.ldapservers_samba_domains_put(ldapserver_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SambaDomainsApi->ldapservers_samba_domains_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapserver_id** | **str**| Unique identifier of the LDAP server. | 
 **id** | **str**| Unique identifier of the samba domain. | 
 **body** | [**SambaDomainInput**](SambaDomainInput.md)|  | [optional] 

### Return type

[**SambaDomainOutput**](SambaDomainOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

