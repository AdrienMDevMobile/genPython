# openapi_client.LocationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_create**](LocationsApi.md#locations_create) | **POST** /api/v1/locations | 
[**locations_list**](LocationsApi.md#locations_list) | **GET** /api/v1/locations | 
[**locations_osm_retrieve**](LocationsApi.md#locations_osm_retrieve) | **GET** /api/v1/locations/osm/{osm_type}/{osm_id} | 
[**locations_retrieve**](LocationsApi.md#locations_retrieve) | **GET** /api/v1/locations/{id} | 


# **locations_create**
> LocationCreate locations_create(location_create)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.location_create import LocationCreate
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
    api_instance = openapi_client.LocationsApi(api_client)
    location_create = openapi_client.LocationCreate() # LocationCreate | 

    try:
        api_response = api_instance.locations_create(location_create)
        print("The response of LocationsApi->locations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_create** | [**LocationCreate**](LocationCreate.md)|  | 

### Return type

[**LocationCreate**](LocationCreate.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_list**
> PaginatedLocationList locations_list(order_by=order_by, osm_address_city__like=osm_address_city__like, osm_address_country__like=osm_address_country__like, osm_name__like=osm_name__like, page=page, price_count=price_count, price_count__gte=price_count__gte, price_count__lte=price_count__lte, size=size)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.paginated_location_list import PaginatedLocationList
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
    api_instance = openapi_client.LocationsApi(api_client)
    order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
    osm_address_city__like = 'osm_address_city__like_example' # str |  (optional)
    osm_address_country__like = 'osm_address_country__like_example' # str |  (optional)
    osm_name__like = 'osm_name__like_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    price_count = 56 # int |  (optional)
    price_count__gte = 56 # int |  (optional)
    price_count__lte = 56 # int |  (optional)
    size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.locations_list(order_by=order_by, osm_address_city__like=osm_address_city__like, osm_address_country__like=osm_address_country__like, osm_name__like=osm_name__like, page=page, price_count=price_count, price_count__gte=price_count__gte, price_count__lte=price_count__lte, size=size)
        print("The response of LocationsApi->locations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **osm_address_city__like** | **str**|  | [optional] 
 **osm_address_country__like** | **str**|  | [optional] 
 **osm_name__like** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **price_count** | **int**|  | [optional] 
 **price_count__gte** | **int**|  | [optional] 
 **price_count__lte** | **int**|  | [optional] 
 **size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedLocationList**](PaginatedLocationList.md)

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

# **locations_osm_retrieve**
> Location locations_osm_retrieve(osm_id, osm_type)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsApi(api_client)
    osm_id = 'osm_id_example' # str | 
    osm_type = 'osm_type_example' # str | 

    try:
        api_response = api_instance.locations_osm_retrieve(osm_id, osm_type)
        print("The response of LocationsApi->locations_osm_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_osm_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **osm_id** | **str**|  | 
 **osm_type** | **str**|  | 

### Return type

[**Location**](Location.md)

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

# **locations_retrieve**
> Location locations_retrieve(id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.location import Location
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
    api_instance = openapi_client.LocationsApi(api_client)
    id = 56 # int | A unique integer value identifying this Location.

    try:
        api_response = api_instance.locations_retrieve(id)
        print("The response of LocationsApi->locations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Location. | 

### Return type

[**Location**](Location.md)

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

