# jcapiv2.PoliciesApi

All URIs are relative to *http://localhost:3004/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](PoliciesApi.md#delete) | **DELETE** /policies/{id} | Deletes a Policy.
[**policies_get**](PoliciesApi.md#policies_get) | **GET** /policies/{id} | Gets a specific Policy.
[**policies_list**](PoliciesApi.md#policies_list) | **GET** /policies | Lists all the policies.
[**policies_post**](PoliciesApi.md#policies_post) | **POST** /policies | Create a new Policy.
[**policytemplates_id_get**](PoliciesApi.md#policytemplates_id_get) | **GET** /policytemplates/{id} | Get a specific Policy Template.
[**policytemplates_list**](PoliciesApi.md#policytemplates_list) | **GET** /policytemplates | Lists all of the policy templates.
[**update**](PoliciesApi.md#update) | **PATCH** /policies/{id} | Update an existing Policy.


# **delete**
> str delete(id)

Deletes a Policy.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
id = 'id_example' # str | ObjectID of the Policy object.

try: 
    # Deletes a Policy.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the Policy object. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_get**
> Policy policies_get(id)

Gets a specific Policy.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
id = 'id_example' # str | ObjectID of the Policy object.

try: 
    # Gets a specific Policy.
    api_response = api_instance.policies_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the Policy object. | 

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_list**
> list[Policy] policies_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Lists all the policies.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Lists all the policies.
    api_response = api_instance.policies_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[Policy]**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_post**
> Policy policies_post(body)

Create a new Policy.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
body = jcapiv2.Policy() # Policy | 

try: 
    # Create a new Policy.
    api_response = api_instance.policies_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)|  | 

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policytemplates_id_get**
> PolicyTemplate policytemplates_id_get(id)

Get a specific Policy Template.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
id = 'id_example' # str | ObjectID of the Policy Template.

try: 
    # Get a specific Policy Template.
    api_response = api_instance.policytemplates_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policytemplates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the Policy Template. | 

### Return type

[**PolicyTemplate**](PolicyTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policytemplates_list**
> list[PolicyTemplate] policytemplates_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)

Lists all of the policy templates.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
limit = 10 # int | The number of records to return at once. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = '' # str | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to )
fields = '' # str | The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  (optional) (default to )
filter = '' # str |  (optional) (default to )

try: 
    # Lists all of the policy templates.
    api_response = api_instance.policytemplates_list(limit=limit, skip=skip, sort=sort, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->policytemplates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of records to return at once. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | **str**| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to ]
 **fields** | **str**| The comma separated fields included in the returned records. If omitted the default list of fields will be returned.  | [optional] [default to ]
 **filter** | **str**|  | [optional] [default to ]

### Return type

[**list[PolicyTemplate]**](PolicyTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Policy update(id, body)

Update an existing Policy.

### Example 
```python
from __future__ import print_statement
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.PoliciesApi()
id = 'id_example' # str | ObjectID of the Policy object.
body = jcapiv2.Policy() # Policy | 

try: 
    # Update an existing Policy.
    api_response = api_instance.update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ObjectID of the Policy object. | 
 **body** | [**Policy**](Policy.md)|  | 

### Return type

[**Policy**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

