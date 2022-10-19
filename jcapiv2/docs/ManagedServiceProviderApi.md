# jcapiv2.ManagedServiceProviderApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**administrator_organizations_create_by_administrator**](ManagedServiceProviderApi.md#administrator_organizations_create_by_administrator) | **POST** /administrators/{id}/organizationlinks | Allow Adminstrator access to an Organization.
[**administrator_organizations_list_by_administrator**](ManagedServiceProviderApi.md#administrator_organizations_list_by_administrator) | **GET** /administrators/{id}/organizationlinks | List the association links between an Administrator and Organizations.
[**administrator_organizations_list_by_organization**](ManagedServiceProviderApi.md#administrator_organizations_list_by_organization) | **GET** /organizations/{id}/administratorlinks | List the association links between an Organization and Administrators.
[**administrator_organizations_remove_by_administrator**](ManagedServiceProviderApi.md#administrator_organizations_remove_by_administrator) | **DELETE** /administrators/{administrator_id}/organizationlinks/{id} | Remove association between an Administrator and an Organization.
[**provider_organizations_update_org**](ManagedServiceProviderApi.md#provider_organizations_update_org) | **PUT** /providers/{provider_id}/organizations/{id} | Update Provider Organization
[**providers_get_provider**](ManagedServiceProviderApi.md#providers_get_provider) | **GET** /providers/{provider_id} | Retrieve Provider
[**providers_list_administrators**](ManagedServiceProviderApi.md#providers_list_administrators) | **GET** /providers/{provider_id}/administrators | List Provider Administrators
[**providers_list_organizations**](ManagedServiceProviderApi.md#providers_list_organizations) | **GET** /providers/{provider_id}/organizations | List Provider Organizations
[**providers_post_admins**](ManagedServiceProviderApi.md#providers_post_admins) | **POST** /providers/{provider_id}/administrators | Create a new Provider Administrator
[**providers_retrieve_invoice**](ManagedServiceProviderApi.md#providers_retrieve_invoice) | **GET** /providers/{provider_id}/invoices/{ID} | Download a provider&#x27;s invoice.
[**providers_retrieve_invoices**](ManagedServiceProviderApi.md#providers_retrieve_invoices) | **GET** /providers/{provider_id}/invoices | List a provider&#x27;s invoices.

# **administrator_organizations_create_by_administrator**
> AdministratorOrganizationLink administrator_organizations_create_by_administrator(id, body=body)

Allow Adminstrator access to an Organization.

This endpoint allows you to grant Administrator access to an Organization.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv2.AdministratorOrganizationLinkReq() # AdministratorOrganizationLinkReq |  (optional)

try:
    # Allow Adminstrator access to an Organization.
    api_response = api_instance.administrator_organizations_create_by_administrator(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->administrator_organizations_create_by_administrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**AdministratorOrganizationLinkReq**](AdministratorOrganizationLinkReq.md)|  | [optional] 

### Return type

[**AdministratorOrganizationLink**](AdministratorOrganizationLink.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **administrator_organizations_list_by_administrator**
> list[AdministratorOrganizationLink] administrator_organizations_list_by_administrator(id, limit=limit, skip=skip)

List the association links between an Administrator and Organizations.

This endpoint returns the association links between an Administrator and Organizations.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List the association links between an Administrator and Organizations.
    api_response = api_instance.administrator_organizations_list_by_administrator(id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->administrator_organizations_list_by_administrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[AdministratorOrganizationLink]**](AdministratorOrganizationLink.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **administrator_organizations_list_by_organization**
> list[AdministratorOrganizationLink] administrator_organizations_list_by_organization(id, limit=limit, skip=skip)

List the association links between an Organization and Administrators.

This endpoint returns the association links between an Organization and Administrators.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List the association links between an Organization and Administrators.
    api_response = api_instance.administrator_organizations_list_by_organization(id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->administrator_organizations_list_by_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]

### Return type

[**list[AdministratorOrganizationLink]**](AdministratorOrganizationLink.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **administrator_organizations_remove_by_administrator**
> administrator_organizations_remove_by_administrator(administrator_id, id)

Remove association between an Administrator and an Organization.

This endpoint removes the association link between an Administrator and an Organization.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
administrator_id = 'administrator_id_example' # str | 
id = 'id_example' # str | 

try:
    # Remove association between an Administrator and an Organization.
    api_instance.administrator_organizations_remove_by_administrator(administrator_id, id)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->administrator_organizations_remove_by_administrator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **administrator_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_organizations_update_org**
> Organization provider_organizations_update_org(provider_id, id, body=body)

Update Provider Organization

This endpoint updates a provider's organization

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
id = 'id_example' # str | 
body = jcapiv2.Organization() # Organization |  (optional)

try:
    # Update Provider Organization
    api_response = api_instance.provider_organizations_update_org(provider_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->provider_organizations_update_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Organization**](Organization.md)|  | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_get_provider**
> Provider providers_get_provider(provider_id, fields=fields)

Retrieve Provider

This endpoint returns details about a provider

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)

try:
    # Retrieve Provider
    api_response = api_instance.providers_get_provider(provider_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->providers_get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 

### Return type

[**Provider**](Provider.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_list_administrators**
> InlineResponse20012 providers_list_administrators(provider_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List Provider Administrators

This endpoint returns a list of the Administrators associated with the Provider. You must be associated with the provider to use this route.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # List Provider Administrators
    api_response = api_instance.providers_list_administrators(provider_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->providers_list_administrators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_list_organizations**
> InlineResponse20013 providers_list_organizations(provider_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List Provider Organizations

This endpoint returns a list of the Organizations associated with the Provider. You must be associated with the provider to use this route.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)

try:
    # List Provider Organizations
    api_response = api_instance.providers_list_organizations(provider_id, fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->providers_list_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **fields** | [**list[str]**](str.md)| The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  | [optional] 
 **filter** | [**list[str]**](str.md)| A filter to apply to the query.  **Filter structure**: &#x60;&lt;field&gt;:&lt;operator&gt;:&lt;value&gt;&#x60;.  **field** &#x3D; Populate with a valid field from an endpoint response.  **operator** &#x3D;  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** &#x3D; Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** &#x60;GET /api/v2/groups?filter&#x3D;name:eq:Test+Group&#x60; | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_post_admins**
> Administrator providers_post_admins(provider_id, body=body)

Create a new Provider Administrator

This endpoint allows you to create a provider administrator. You must be associated with the provider to use this route. You must provide either `role` or `roleName`.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
body = jcapiv2.ProviderAdminReq() # ProviderAdminReq |  (optional)

try:
    # Create a new Provider Administrator
    api_response = api_instance.providers_post_admins(provider_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->providers_post_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **body** | [**ProviderAdminReq**](ProviderAdminReq.md)|  | [optional] 

### Return type

[**Administrator**](Administrator.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_retrieve_invoice**
> str providers_retrieve_invoice(provider_id, id)

Download a provider's invoice.

Retrieves an invoice for this provider. You must be associated to the provider to use this endpoint.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
id = 'id_example' # str | 

try:
    # Download a provider's invoice.
    api_response = api_instance.providers_retrieve_invoice(provider_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->providers_retrieve_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_retrieve_invoices**
> ProviderInvoiceResponse providers_retrieve_invoices(provider_id, skip=skip, sort=sort, limit=limit)

List a provider's invoices.

Retrieves a list of invoices for this provider. You must be associated to the provider to use this endpoint.

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
api_instance = jcapiv2.ManagedServiceProviderApi(jcapiv2.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)

try:
    # List a provider's invoices.
    api_response = api_instance.providers_retrieve_invoices(provider_id, skip=skip, sort=sort, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServiceProviderApi->providers_retrieve_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]

### Return type

[**ProviderInvoiceResponse**](ProviderInvoiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

