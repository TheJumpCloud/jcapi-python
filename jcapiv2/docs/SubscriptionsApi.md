# jcapiv2.SubscriptionsApi

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_get**](SubscriptionsApi.md#subscriptions_get) | **GET** /subscriptions | Lists all the Pricing &amp; Packaging Subscriptions

# **subscriptions_get**
> list[Subscription] subscriptions_get()

Lists all the Pricing & Packaging Subscriptions

This endpoint returns all pricing & packaging subscriptions.  ##### Sample Request  ```  curl -X GET  https://console.jumpcloud.com/api/v2/subscriptions \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}'   ```

### Example
```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jcapiv2.SubscriptionsApi()

try:
    # Lists all the Pricing & Packaging Subscriptions
    api_response = api_instance.subscriptions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

