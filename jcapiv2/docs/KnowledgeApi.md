# jcapiv2.KnowledgeApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**knowledge_articles_list**](KnowledgeApi.md#knowledge_articles_list) | **GET** /knowledge/articles | List Knowledge Articles
[**knowledge_salesforce_list**](KnowledgeApi.md#knowledge_salesforce_list) | **GET** /knowledge/salesforce | List Knowledge Articles


# **knowledge_articles_list**
> SalesforceKnowledgeListOutput knowledge_articles_list(filter=filter, skip=skip, sort=sort, limit=limit)

List Knowledge Articles

This endpoint returns a list of knowledge articles hosted in salesforce.  ``` Sample Request curl -X GET https://console.jumpcloud.com/api/v2/knowledge/articles \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.KnowledgeApi(jcapiv2.ApiClient(configuration))
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])
limit = 10 # int |  (optional) (default to 10)

try:
    # List Knowledge Articles
    api_response = api_instance.knowledge_articles_list(filter=filter, skip=skip, sort=sort, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->knowledge_articles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**SalesforceKnowledgeListOutput**](SalesforceKnowledgeListOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **knowledge_salesforce_list**
> SalesforceKnowledgeListOutput knowledge_salesforce_list(fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)

List Knowledge Articles

This endpoint returns a list of knowledge articles hosted in salesforce.  ``` Sample Request curl -X GET https://console.jumpcloud.com/api/v2/knowledge/articles \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```

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
api_instance = jcapiv2.KnowledgeApi(jcapiv2.ApiClient(configuration))
fields = ['[\"id\",\"body\",\"title\",\"publishedDate\"]'] # list[str] |  (optional) (default to ["id","body","title","publishedDate"])
filter = ['[]'] # list[str] | Supported operators are: eq, ne, gt, ge, lt, le, between, search, in (optional) (default to [])
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['[]'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional) (default to [])

try:
    # List Knowledge Articles
    api_response = api_instance.knowledge_salesforce_list(fields=fields, filter=filter, limit=limit, skip=skip, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KnowledgeApi->knowledge_salesforce_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)|  | [optional] [default to [&quot;id&quot;,&quot;body&quot;,&quot;title&quot;,&quot;publishedDate&quot;]]
 **filter** | [**list[str]**](str.md)| Supported operators are: eq, ne, gt, ge, lt, le, between, search, in | [optional] [default to []]
 **limit** | **int**| The number of records to return at once. Limited to 100. | [optional] [default to 10]
 **skip** | **int**| The offset into the records to return. | [optional] [default to 0]
 **sort** | [**list[str]**](str.md)| The comma separated fields used to sort the collection. Default sort is ascending, prefix with &#x60;-&#x60; to sort descending.  | [optional] [default to []]

### Return type

[**SalesforceKnowledgeListOutput**](SalesforceKnowledgeListOutput.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

