# jcapiv2.OrganizationsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**administrator_organizations_create_by_administrator**](OrganizationsApi.md#administrator_organizations_create_by_administrator) | **POST** /administrators/{id}/organizationlinks | Allow Adminstrator access to an Organization.
[**administrator_organizations_list_by_administrator**](OrganizationsApi.md#administrator_organizations_list_by_administrator) | **GET** /administrators/{id}/organizationlinks | List the association links between an Administrator and Organizations.
[**administrator_organizations_list_by_organization**](OrganizationsApi.md#administrator_organizations_list_by_organization) | **GET** /organizations/{id}/administratorlinks | List the association links between an Organization and Administrators.
[**administrator_organizations_remove_by_administrator**](OrganizationsApi.md#administrator_organizations_remove_by_administrator) | **DELETE** /administrators/{administrator_id}/organizationlinks/{id} | Remove association between an Administrator and an Organization.
[**organizations_list_cases**](OrganizationsApi.md#organizations_list_cases) | **GET** /organizations/cases | Get all cases (Support/Feature requests) for organization

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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
body = jcapiv2.AdministratorOrganizationLinkReq() # AdministratorOrganizationLinkReq |  (optional)

try:
    # Allow Adminstrator access to an Organization.
    api_response = api_instance.administrator_organizations_create_by_administrator(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->administrator_organizations_create_by_administrator: %s\n" % e)
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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List the association links between an Administrator and Organizations.
    api_response = api_instance.administrator_organizations_list_by_administrator(id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->administrator_organizations_list_by_administrator: %s\n" % e)
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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List the association links between an Organization and Administrators.
    api_response = api_instance.administrator_organizations_list_by_organization(id, limit=limit, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->administrator_organizations_list_by_organization: %s\n" % e)
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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
administrator_id = 'administrator_id_example' # str | 
id = 'id_example' # str | 

try:
    # Remove association between an Administrator and an Organization.
    api_instance.administrator_organizations_remove_by_administrator(administrator_id, id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->administrator_organizations_remove_by_administrator: %s\n" % e)
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

# **organizations_list_cases**
> OrganizationCasesResponse organizations_list_cases(skip=skip, sort=sort, limit=limit)

Get all cases (Support/Feature requests) for organization

This endpoint returns the cases (Support/Feature requests) for the organization

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
api_instance = jcapiv2.OrganizationsApi(jcapiv2.ApiClient(configuration))
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)

try:
    # Get all cases (Support/Feature requests) for organization
    api_response = api_instance.organizations_list_cases(skip=skip, sort=sort, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_list_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] 
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]

### Return type

[**OrganizationCasesResponse**](OrganizationCasesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

