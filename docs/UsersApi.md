# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_list**](UsersApi.md#users_list) | **GET** /api/v1/users | 


# **users_list**
> PaginatedUserList users_list(order_by=order_by, page=page, price_count=price_count, price_count__gte=price_count__gte, price_count__lte=price_count__lte, size=size)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.paginated_user_list import PaginatedUserList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsersApi(api_client)
    order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    price_count = 56 # int |  (optional)
    price_count__gte = 56 # int |  (optional)
    price_count__lte = 56 # int |  (optional)
    size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.users_list(order_by=order_by, page=page, price_count=price_count, price_count__gte=price_count__gte, price_count__lte=price_count__lte, size=size)
        print("The response of UsersApi->users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **price_count** | **int**|  | [optional] 
 **price_count__gte** | **int**|  | [optional] 
 **price_count__lte** | **int**|  | [optional] 
 **size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedUserList**](PaginatedUserList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

