# openapi-client
Open Prices API allows you to add product prices

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.0 (api)
- Package version: 1.0.0
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://world.openfoodfacts.org](https://world.openfoodfacts.org)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    api_instance = openapi_client.ApiApi(api_client)
    format = 'format_example' # str |  (optional)
    lang = 'lang_example' # str |  (optional)

    try:
        api_response = api_instance.api_schema_retrieve(format=format, lang=lang)
        print("The response of ApiApi->api_schema_retrieve:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiApi->api_schema_retrieve: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**api_schema_retrieve**](docs/ApiApi.md#api_schema_retrieve) | **GET** /api/schema | 
*AuthApi* | [**auth_create**](docs/AuthApi.md#auth_create) | **POST** /api/v1/auth | 
*AuthApi* | [**session_destroy**](docs/AuthApi.md#session_destroy) | **DELETE** /api/v1/session | 
*AuthApi* | [**session_retrieve**](docs/AuthApi.md#session_retrieve) | **GET** /api/v1/session | 
*LocationsApi* | [**locations_create**](docs/LocationsApi.md#locations_create) | **POST** /api/v1/locations | 
*LocationsApi* | [**locations_list**](docs/LocationsApi.md#locations_list) | **GET** /api/v1/locations | 
*LocationsApi* | [**locations_osm_retrieve**](docs/LocationsApi.md#locations_osm_retrieve) | **GET** /api/v1/locations/osm/{osm_type}/{osm_id} | 
*LocationsApi* | [**locations_retrieve**](docs/LocationsApi.md#locations_retrieve) | **GET** /api/v1/locations/{id} | 
*PricesApi* | [**prices_create**](docs/PricesApi.md#prices_create) | **POST** /api/v1/prices | 
*PricesApi* | [**prices_destroy**](docs/PricesApi.md#prices_destroy) | **DELETE** /api/v1/prices/{id} | 
*PricesApi* | [**prices_list**](docs/PricesApi.md#prices_list) | **GET** /api/v1/prices | 
*PricesApi* | [**prices_partial_update**](docs/PricesApi.md#prices_partial_update) | **PATCH** /api/v1/prices/{id} | 
*PricesApi* | [**prices_retrieve**](docs/PricesApi.md#prices_retrieve) | **GET** /api/v1/prices/{id} | 
*PricesApi* | [**prices_stats_retrieve**](docs/PricesApi.md#prices_stats_retrieve) | **GET** /api/v1/prices/stats | 
*ProductsApi* | [**products_code_retrieve**](docs/ProductsApi.md#products_code_retrieve) | **GET** /api/v1/products/code/{code} | 
*ProductsApi* | [**products_list**](docs/ProductsApi.md#products_list) | **GET** /api/v1/products | 
*ProductsApi* | [**products_retrieve**](docs/ProductsApi.md#products_retrieve) | **GET** /api/v1/products/{id} | 
*ProofsApi* | [**proofs_destroy**](docs/ProofsApi.md#proofs_destroy) | **DELETE** /api/v1/proofs/{id} | 
*ProofsApi* | [**proofs_list**](docs/ProofsApi.md#proofs_list) | **GET** /api/v1/proofs | 
*ProofsApi* | [**proofs_partial_update**](docs/ProofsApi.md#proofs_partial_update) | **PATCH** /api/v1/proofs/{id} | 
*ProofsApi* | [**proofs_retrieve**](docs/ProofsApi.md#proofs_retrieve) | **GET** /api/v1/proofs/{id} | 
*ProofsApi* | [**proofs_upload_create**](docs/ProofsApi.md#proofs_upload_create) | **POST** /api/v1/proofs/upload | 
*StatsApi* | [**stats_retrieve**](docs/StatsApi.md#stats_retrieve) | **GET** /api/v1/stats | 
*StatusApi* | [**status_retrieve**](docs/StatusApi.md#status_retrieve) | **GET** /api/v1/status | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /api/v1/users | 


## Documentation For Models

 - [BlankEnum](docs/BlankEnum.md)
 - [CurrencyEnum](docs/CurrencyEnum.md)
 - [Location](docs/Location.md)
 - [LocationCreate](docs/LocationCreate.md)
 - [LocationOsmTypeEnum](docs/LocationOsmTypeEnum.md)
 - [Login](docs/Login.md)
 - [NullEnum](docs/NullEnum.md)
 - [PaginatedLocationList](docs/PaginatedLocationList.md)
 - [PaginatedPriceFullList](docs/PaginatedPriceFullList.md)
 - [PaginatedProductFullList](docs/PaginatedProductFullList.md)
 - [PaginatedProofFullList](docs/PaginatedProofFullList.md)
 - [PaginatedUserList](docs/PaginatedUserList.md)
 - [PatchedPriceUpdate](docs/PatchedPriceUpdate.md)
 - [PatchedPriceUpdateCurrency](docs/PatchedPriceUpdateCurrency.md)
 - [PatchedPriceUpdatePricePer](docs/PatchedPriceUpdatePricePer.md)
 - [PatchedProofUpdate](docs/PatchedProofUpdate.md)
 - [PriceCreate](docs/PriceCreate.md)
 - [PriceCreateLocationOsmType](docs/PriceCreateLocationOsmType.md)
 - [PriceFull](docs/PriceFull.md)
 - [PricePerEnum](docs/PricePerEnum.md)
 - [PriceStats](docs/PriceStats.md)
 - [PriceUpdate](docs/PriceUpdate.md)
 - [ProductFull](docs/ProductFull.md)
 - [ProductFullSource](docs/ProductFullSource.md)
 - [Proof](docs/Proof.md)
 - [ProofFull](docs/ProofFull.md)
 - [ProofUpdate](docs/ProofUpdate.md)
 - [SessionFull](docs/SessionFull.md)
 - [SessionResponse](docs/SessionResponse.md)
 - [SourceEnum](docs/SourceEnum.md)
 - [Status](docs/Status.md)
 - [TotalStats](docs/TotalStats.md)
 - [TypeEnum](docs/TypeEnum.md)
 - [User](docs/User.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="basicAuth"></a>
### basicAuth

- **Type**: HTTP basic authentication

<a id="cookieAuth"></a>
### cookieAuth

- **Type**: API key
- **API key parameter name**: opsession
- **Location**: 


## Author

contact@openfoodfacts.org


