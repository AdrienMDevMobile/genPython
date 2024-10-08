# openapi_client.ProductsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_code_retrieve**](ProductsApi.md#products_code_retrieve) | **GET** /api/v1/products/code/{code} | 
[**products_list**](ProductsApi.md#products_list) | **GET** /api/v1/products | 
[**products_retrieve**](ProductsApi.md#products_retrieve) | **GET** /api/v1/products/{id} | 


# **products_code_retrieve**
> ProductFull products_code_retrieve(code)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.product_full import ProductFull
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
    api_instance = openapi_client.ProductsApi(api_client)
    code = 'code_example' # str | 

    try:
        api_response = api_instance.products_code_retrieve(code)
        print("The response of ProductsApi->products_code_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_code_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 

### Return type

[**ProductFull**](ProductFull.md)

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

# **products_list**
> PaginatedProductFullList products_list(brands__like=brands__like, brands_tags__contains=brands_tags__contains, categories_tags__contains=categories_tags__contains, code=code, ecoscore_grade=ecoscore_grade, labels_tags__contains=labels_tags__contains, nova_group=nova_group, nutriscore_grade=nutriscore_grade, order_by=order_by, page=page, price_count=price_count, price_count__gte=price_count__gte, price_count__lte=price_count__lte, product_name__like=product_name__like, size=size, source=source, unique_scans_n__gte=unique_scans_n__gte)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.paginated_product_full_list import PaginatedProductFullList
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
    api_instance = openapi_client.ProductsApi(api_client)
    brands__like = 'brands__like_example' # str |  (optional)
    brands_tags__contains = 'brands_tags__contains_example' # str |  (optional)
    categories_tags__contains = 'categories_tags__contains_example' # str |  (optional)
    code = 'code_example' # str |  (optional)
    ecoscore_grade = 'ecoscore_grade_example' # str |  (optional)
    labels_tags__contains = 'labels_tags__contains_example' # str |  (optional)
    nova_group = 56 # int |  (optional)
    nutriscore_grade = 'nutriscore_grade_example' # str |  (optional)
    order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    price_count = 56 # int |  (optional)
    price_count__gte = 56 # int |  (optional)
    price_count__lte = 56 # int |  (optional)
    product_name__like = 'product_name__like_example' # str |  (optional)
    size = 56 # int | Number of results to return per page. (optional)
    source = 'source_example' # str | * `off` - off * `obf` - obf * `opff` - opff * `opf` - opf * `off_pro` - off_pro (optional)
    unique_scans_n__gte = 56 # int |  (optional)

    try:
        api_response = api_instance.products_list(brands__like=brands__like, brands_tags__contains=brands_tags__contains, categories_tags__contains=categories_tags__contains, code=code, ecoscore_grade=ecoscore_grade, labels_tags__contains=labels_tags__contains, nova_group=nova_group, nutriscore_grade=nutriscore_grade, order_by=order_by, page=page, price_count=price_count, price_count__gte=price_count__gte, price_count__lte=price_count__lte, product_name__like=product_name__like, size=size, source=source, unique_scans_n__gte=unique_scans_n__gte)
        print("The response of ProductsApi->products_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brands__like** | **str**|  | [optional] 
 **brands_tags__contains** | **str**|  | [optional] 
 **categories_tags__contains** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **ecoscore_grade** | **str**|  | [optional] 
 **labels_tags__contains** | **str**|  | [optional] 
 **nova_group** | **int**|  | [optional] 
 **nutriscore_grade** | **str**|  | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **price_count** | **int**|  | [optional] 
 **price_count__gte** | **int**|  | [optional] 
 **price_count__lte** | **int**|  | [optional] 
 **product_name__like** | **str**|  | [optional] 
 **size** | **int**| Number of results to return per page. | [optional] 
 **source** | **str**| * &#x60;off&#x60; - off * &#x60;obf&#x60; - obf * &#x60;opff&#x60; - opff * &#x60;opf&#x60; - opf * &#x60;off_pro&#x60; - off_pro | [optional] 
 **unique_scans_n__gte** | **int**|  | [optional] 

### Return type

[**PaginatedProductFullList**](PaginatedProductFullList.md)

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

# **products_retrieve**
> ProductFull products_retrieve(id)



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import openapi_client
from openapi_client.models.product_full import ProductFull
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
    api_instance = openapi_client.ProductsApi(api_client)
    id = 56 # int | A unique integer value identifying this Product.

    try:
        api_response = api_instance.products_retrieve(id)
        print("The response of ProductsApi->products_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Product. | 

### Return type

[**ProductFull**](ProductFull.md)

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

