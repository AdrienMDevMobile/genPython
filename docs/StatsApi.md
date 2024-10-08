# openapi_client.StatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_retrieve**](StatsApi.md#stats_retrieve) | **GET** /api/v1/stats | 


# **stats_retrieve**
> TotalStats stats_retrieve()



### Example


```python
import openapi_client
from openapi_client.models.total_stats import TotalStats
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatsApi(api_client)

    try:
        api_response = api_instance.stats_retrieve()
        print("The response of StatsApi->stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->stats_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TotalStats**](TotalStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

