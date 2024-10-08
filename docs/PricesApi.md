# openapi_client.PricesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prices_create**](PricesApi.md#prices_create) | **POST** /api/v1/prices | 
[**prices_destroy**](PricesApi.md#prices_destroy) | **DELETE** /api/v1/prices/{id} | 
[**prices_list**](PricesApi.md#prices_list) | **GET** /api/v1/prices | 
[**prices_partial_update**](PricesApi.md#prices_partial_update) | **PATCH** /api/v1/prices/{id} | 
[**prices_retrieve**](PricesApi.md#prices_retrieve) | **GET** /api/v1/prices/{id} | 
[**prices_stats_retrieve**](PricesApi.md#prices_stats_retrieve) | **GET** /api/v1/prices/stats | 


# **prices_create**
> PriceCreate prices_create(price_create)



### Example


```python
import openapi_client
from openapi_client.models.price_create import PriceCreate
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
    api_instance = openapi_client.PricesApi(api_client)
    price_create = openapi_client.PriceCreate() # PriceCreate | 

    try:
        api_response = api_instance.prices_create(price_create)
        print("The response of PricesApi->prices_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_create** | [**PriceCreate**](PriceCreate.md)|  | 

### Return type

[**PriceCreate**](PriceCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_destroy**
> prices_destroy(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.PricesApi(api_client)
    id = 56 # int | A unique integer value identifying this Price.

    try:
        api_instance.prices_destroy(id)
    except Exception as e:
        print("Exception when calling PricesApi->prices_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Price. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_list**
> PaginatedPriceFullList prices_list(category_tag=category_tag, created__gte=created__gte, created__lte=created__lte, currency=currency, var_date=var_date, date__gt=date__gt, date__gte=date__gte, date__lt=date__lt, date__lte=date__lte, date__month=date__month, date__year=date__year, labels_tags__contains=labels_tags__contains, location_id=location_id, location_id__isnull=location_id__isnull, location_osm_id=location_osm_id, location_osm_type=location_osm_type, order_by=order_by, origins_tags__contains=origins_tags__contains, owner=owner, page=page, price=price, price__gt=price__gt, price__gte=price__gte, price__lt=price__lt, price__lte=price__lte, price_is_discounted=price_is_discounted, product_code=product_code, product_id=product_id, product_id__isnull=product_id__isnull, proof_id=proof_id, proof_id__isnull=proof_id__isnull, size=size)



### Example


```python
import openapi_client
from openapi_client.models.paginated_price_full_list import PaginatedPriceFullList
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
    api_instance = openapi_client.PricesApi(api_client)
    category_tag = 'category_tag_example' # str |  (optional)
    created__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    currency = 'currency_example' # str | * `ADP` - ADP * `AED` - AED * `AFA` - AFA * `AFN` - AFN * `ALK` - ALK * `ALL` - ALL * `AMD` - AMD * `ANG` - ANG * `AOA` - AOA * `AOK` - AOK * `AON` - AON * `AOR` - AOR * `ARA` - ARA * `ARL` - ARL * `ARM` - ARM * `ARP` - ARP * `ARS` - ARS * `ATS` - ATS * `AUD` - AUD * `AWG` - AWG * `AZM` - AZM * `AZN` - AZN * `BAD` - BAD * `BAM` - BAM * `BAN` - BAN * `BBD` - BBD * `BDT` - BDT * `BEC` - BEC * `BEF` - BEF * `BEL` - BEL * `BGL` - BGL * `BGM` - BGM * `BGN` - BGN * `BGO` - BGO * `BHD` - BHD * `BIF` - BIF * `BMD` - BMD * `BND` - BND * `BOB` - BOB * `BOL` - BOL * `BOP` - BOP * `BOV` - BOV * `BRB` - BRB * `BRC` - BRC * `BRE` - BRE * `BRL` - BRL * `BRN` - BRN * `BRR` - BRR * `BRZ` - BRZ * `BSD` - BSD * `BTN` - BTN * `BUK` - BUK * `BWP` - BWP * `BYB` - BYB * `BYN` - BYN * `BYR` - BYR * `BZD` - BZD * `CAD` - CAD * `CDF` - CDF * `CHE` - CHE * `CHF` - CHF * `CHW` - CHW * `CLE` - CLE * `CLF` - CLF * `CLP` - CLP * `CNH` - CNH * `CNX` - CNX * `CNY` - CNY * `COP` - COP * `COU` - COU * `CRC` - CRC * `CSD` - CSD * `CSK` - CSK * `CUC` - CUC * `CUP` - CUP * `CVE` - CVE * `CYP` - CYP * `CZK` - CZK * `DDM` - DDM * `DEM` - DEM * `DJF` - DJF * `DKK` - DKK * `DOP` - DOP * `DZD` - DZD * `ECS` - ECS * `ECV` - ECV * `EEK` - EEK * `EGP` - EGP * `ERN` - ERN * `ESA` - ESA * `ESB` - ESB * `ESP` - ESP * `ETB` - ETB * `EUR` - EUR * `FIM` - FIM * `FJD` - FJD * `FKP` - FKP * `FRF` - FRF * `GBP` - GBP * `GEK` - GEK * `GEL` - GEL * `GHC` - GHC * `GHS` - GHS * `GIP` - GIP * `GMD` - GMD * `GNF` - GNF * `GNS` - GNS * `GQE` - GQE * `GRD` - GRD * `GTQ` - GTQ * `GWE` - GWE * `GWP` - GWP * `GYD` - GYD * `HKD` - HKD * `HNL` - HNL * `HRD` - HRD * `HRK` - HRK * `HTG` - HTG * `HUF` - HUF * `IDR` - IDR * `IEP` - IEP * `ILP` - ILP * `ILR` - ILR * `ILS` - ILS * `INR` - INR * `IQD` - IQD * `IRR` - IRR * `ISJ` - ISJ * `ISK` - ISK * `ITL` - ITL * `JMD` - JMD * `JOD` - JOD * `JPY` - JPY * `KES` - KES * `KGS` - KGS * `KHR` - KHR * `KMF` - KMF * `KPW` - KPW * `KRH` - KRH * `KRO` - KRO * `KRW` - KRW * `KWD` - KWD * `KYD` - KYD * `KZT` - KZT * `LAK` - LAK * `LBP` - LBP * `LKR` - LKR * `LRD` - LRD * `LSL` - LSL * `LTL` - LTL * `LTT` - LTT * `LUC` - LUC * `LUF` - LUF * `LUL` - LUL * `LVL` - LVL * `LVR` - LVR * `LYD` - LYD * `MAD` - MAD * `MAF` - MAF * `MCF` - MCF * `MDC` - MDC * `MDL` - MDL * `MGA` - MGA * `MGF` - MGF * `MKD` - MKD * `MKN` - MKN * `MLF` - MLF * `MMK` - MMK * `MNT` - MNT * `MOP` - MOP * `MRO` - MRO * `MRU` - MRU * `MTL` - MTL * `MTP` - MTP * `MUR` - MUR * `MVP` - MVP * `MVR` - MVR * `MWK` - MWK * `MXN` - MXN * `MXP` - MXP * `MXV` - MXV * `MYR` - MYR * `MZE` - MZE * `MZM` - MZM * `MZN` - MZN * `NAD` - NAD * `NGN` - NGN * `NIC` - NIC * `NIO` - NIO * `NLG` - NLG * `NOK` - NOK * `NPR` - NPR * `NZD` - NZD * `OMR` - OMR * `PAB` - PAB * `PEI` - PEI * `PEN` - PEN * `PES` - PES * `PGK` - PGK * `PHP` - PHP * `PKR` - PKR * `PLN` - PLN * `PLZ` - PLZ * `PTE` - PTE * `PYG` - PYG * `QAR` - QAR * `RHD` - RHD * `ROL` - ROL * `RON` - RON * `RSD` - RSD * `RUB` - RUB * `RUR` - RUR * `RWF` - RWF * `SAR` - SAR * `SBD` - SBD * `SCR` - SCR * `SDD` - SDD * `SDG` - SDG * `SDP` - SDP * `SEK` - SEK * `SGD` - SGD * `SHP` - SHP * `SIT` - SIT * `SKK` - SKK * `SLE` - SLE * `SLL` - SLL * `SOS` - SOS * `SRD` - SRD * `SRG` - SRG * `SSP` - SSP * `STD` - STD * `STN` - STN * `SUR` - SUR * `SVC` - SVC * `SYP` - SYP * `SZL` - SZL * `THB` - THB * `TJR` - TJR * `TJS` - TJS * `TMM` - TMM * `TMT` - TMT * `TND` - TND * `TOP` - TOP * `TPE` - TPE * `TRL` - TRL * `TRY` - TRY * `TTD` - TTD * `TWD` - TWD * `TZS` - TZS * `UAH` - UAH * `UAK` - UAK * `UGS` - UGS * `UGX` - UGX * `USD` - USD * `USN` - USN * `USS` - USS * `UYI` - UYI * `UYP` - UYP * `UYU` - UYU * `UYW` - UYW * `UZS` - UZS * `VEB` - VEB * `VED` - VED * `VEF` - VEF * `VES` - VES * `VND` - VND * `VNN` - VNN * `VUV` - VUV * `WST` - WST * `XAF` - XAF * `XAG` - XAG * `XAU` - XAU * `XBA` - XBA * `XBB` - XBB * `XBC` - XBC * `XBD` - XBD * `XCD` - XCD * `XDR` - XDR * `XEU` - XEU * `XFO` - XFO * `XFU` - XFU * `XOF` - XOF * `XPD` - XPD * `XPF` - XPF * `XPT` - XPT * `XRE` - XRE * `XSU` - XSU * `XTS` - XTS * `XUA` - XUA * `XXX` - XXX * `YDD` - YDD * `YER` - YER * `YUD` - YUD * `YUM` - YUM * `YUN` - YUN * `YUR` - YUR * `ZAL` - ZAL * `ZAR` - ZAR * `ZMK` - ZMK * `ZMW` - ZMW * `ZRN` - ZRN * `ZRZ` - ZRZ * `ZWD` - ZWD * `ZWL` - ZWL * `ZWR` - ZWR (optional)
    var_date = '2013-10-20' # date |  (optional)
    date__gt = '2013-10-20' # date |  (optional)
    date__gte = '2013-10-20' # date |  (optional)
    date__lt = '2013-10-20' # date |  (optional)
    date__lte = '2013-10-20' # date |  (optional)
    date__month = 3.4 # float |  (optional)
    date__year = 3.4 # float |  (optional)
    labels_tags__contains = 'labels_tags__contains_example' # str |  (optional)
    location_id = 56 # int |  (optional)
    location_id__isnull = True # bool |  (optional)
    location_osm_id = 56 # int |  (optional)
    location_osm_type = 'location_osm_type_example' # str | * `NODE` - NODE * `WAY` - WAY * `RELATION` - RELATION (optional)
    order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
    origins_tags__contains = 'origins_tags__contains_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    price = 3.4 # float |  (optional)
    price__gt = 3.4 # float |  (optional)
    price__gte = 3.4 # float |  (optional)
    price__lt = 3.4 # float |  (optional)
    price__lte = 3.4 # float |  (optional)
    price_is_discounted = True # bool |  (optional)
    product_code = 'product_code_example' # str |  (optional)
    product_id = 56 # int |  (optional)
    product_id__isnull = True # bool |  (optional)
    proof_id = 56 # int |  (optional)
    proof_id__isnull = True # bool |  (optional)
    size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.prices_list(category_tag=category_tag, created__gte=created__gte, created__lte=created__lte, currency=currency, var_date=var_date, date__gt=date__gt, date__gte=date__gte, date__lt=date__lt, date__lte=date__lte, date__month=date__month, date__year=date__year, labels_tags__contains=labels_tags__contains, location_id=location_id, location_id__isnull=location_id__isnull, location_osm_id=location_osm_id, location_osm_type=location_osm_type, order_by=order_by, origins_tags__contains=origins_tags__contains, owner=owner, page=page, price=price, price__gt=price__gt, price__gte=price__gte, price__lt=price__lt, price__lte=price__lte, price_is_discounted=price_is_discounted, product_code=product_code, product_id=product_id, product_id__isnull=product_id__isnull, proof_id=proof_id, proof_id__isnull=proof_id__isnull, size=size)
        print("The response of PricesApi->prices_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tag** | **str**|  | [optional] 
 **created__gte** | **datetime**|  | [optional] 
 **created__lte** | **datetime**|  | [optional] 
 **currency** | **str**| * &#x60;ADP&#x60; - ADP * &#x60;AED&#x60; - AED * &#x60;AFA&#x60; - AFA * &#x60;AFN&#x60; - AFN * &#x60;ALK&#x60; - ALK * &#x60;ALL&#x60; - ALL * &#x60;AMD&#x60; - AMD * &#x60;ANG&#x60; - ANG * &#x60;AOA&#x60; - AOA * &#x60;AOK&#x60; - AOK * &#x60;AON&#x60; - AON * &#x60;AOR&#x60; - AOR * &#x60;ARA&#x60; - ARA * &#x60;ARL&#x60; - ARL * &#x60;ARM&#x60; - ARM * &#x60;ARP&#x60; - ARP * &#x60;ARS&#x60; - ARS * &#x60;ATS&#x60; - ATS * &#x60;AUD&#x60; - AUD * &#x60;AWG&#x60; - AWG * &#x60;AZM&#x60; - AZM * &#x60;AZN&#x60; - AZN * &#x60;BAD&#x60; - BAD * &#x60;BAM&#x60; - BAM * &#x60;BAN&#x60; - BAN * &#x60;BBD&#x60; - BBD * &#x60;BDT&#x60; - BDT * &#x60;BEC&#x60; - BEC * &#x60;BEF&#x60; - BEF * &#x60;BEL&#x60; - BEL * &#x60;BGL&#x60; - BGL * &#x60;BGM&#x60; - BGM * &#x60;BGN&#x60; - BGN * &#x60;BGO&#x60; - BGO * &#x60;BHD&#x60; - BHD * &#x60;BIF&#x60; - BIF * &#x60;BMD&#x60; - BMD * &#x60;BND&#x60; - BND * &#x60;BOB&#x60; - BOB * &#x60;BOL&#x60; - BOL * &#x60;BOP&#x60; - BOP * &#x60;BOV&#x60; - BOV * &#x60;BRB&#x60; - BRB * &#x60;BRC&#x60; - BRC * &#x60;BRE&#x60; - BRE * &#x60;BRL&#x60; - BRL * &#x60;BRN&#x60; - BRN * &#x60;BRR&#x60; - BRR * &#x60;BRZ&#x60; - BRZ * &#x60;BSD&#x60; - BSD * &#x60;BTN&#x60; - BTN * &#x60;BUK&#x60; - BUK * &#x60;BWP&#x60; - BWP * &#x60;BYB&#x60; - BYB * &#x60;BYN&#x60; - BYN * &#x60;BYR&#x60; - BYR * &#x60;BZD&#x60; - BZD * &#x60;CAD&#x60; - CAD * &#x60;CDF&#x60; - CDF * &#x60;CHE&#x60; - CHE * &#x60;CHF&#x60; - CHF * &#x60;CHW&#x60; - CHW * &#x60;CLE&#x60; - CLE * &#x60;CLF&#x60; - CLF * &#x60;CLP&#x60; - CLP * &#x60;CNH&#x60; - CNH * &#x60;CNX&#x60; - CNX * &#x60;CNY&#x60; - CNY * &#x60;COP&#x60; - COP * &#x60;COU&#x60; - COU * &#x60;CRC&#x60; - CRC * &#x60;CSD&#x60; - CSD * &#x60;CSK&#x60; - CSK * &#x60;CUC&#x60; - CUC * &#x60;CUP&#x60; - CUP * &#x60;CVE&#x60; - CVE * &#x60;CYP&#x60; - CYP * &#x60;CZK&#x60; - CZK * &#x60;DDM&#x60; - DDM * &#x60;DEM&#x60; - DEM * &#x60;DJF&#x60; - DJF * &#x60;DKK&#x60; - DKK * &#x60;DOP&#x60; - DOP * &#x60;DZD&#x60; - DZD * &#x60;ECS&#x60; - ECS * &#x60;ECV&#x60; - ECV * &#x60;EEK&#x60; - EEK * &#x60;EGP&#x60; - EGP * &#x60;ERN&#x60; - ERN * &#x60;ESA&#x60; - ESA * &#x60;ESB&#x60; - ESB * &#x60;ESP&#x60; - ESP * &#x60;ETB&#x60; - ETB * &#x60;EUR&#x60; - EUR * &#x60;FIM&#x60; - FIM * &#x60;FJD&#x60; - FJD * &#x60;FKP&#x60; - FKP * &#x60;FRF&#x60; - FRF * &#x60;GBP&#x60; - GBP * &#x60;GEK&#x60; - GEK * &#x60;GEL&#x60; - GEL * &#x60;GHC&#x60; - GHC * &#x60;GHS&#x60; - GHS * &#x60;GIP&#x60; - GIP * &#x60;GMD&#x60; - GMD * &#x60;GNF&#x60; - GNF * &#x60;GNS&#x60; - GNS * &#x60;GQE&#x60; - GQE * &#x60;GRD&#x60; - GRD * &#x60;GTQ&#x60; - GTQ * &#x60;GWE&#x60; - GWE * &#x60;GWP&#x60; - GWP * &#x60;GYD&#x60; - GYD * &#x60;HKD&#x60; - HKD * &#x60;HNL&#x60; - HNL * &#x60;HRD&#x60; - HRD * &#x60;HRK&#x60; - HRK * &#x60;HTG&#x60; - HTG * &#x60;HUF&#x60; - HUF * &#x60;IDR&#x60; - IDR * &#x60;IEP&#x60; - IEP * &#x60;ILP&#x60; - ILP * &#x60;ILR&#x60; - ILR * &#x60;ILS&#x60; - ILS * &#x60;INR&#x60; - INR * &#x60;IQD&#x60; - IQD * &#x60;IRR&#x60; - IRR * &#x60;ISJ&#x60; - ISJ * &#x60;ISK&#x60; - ISK * &#x60;ITL&#x60; - ITL * &#x60;JMD&#x60; - JMD * &#x60;JOD&#x60; - JOD * &#x60;JPY&#x60; - JPY * &#x60;KES&#x60; - KES * &#x60;KGS&#x60; - KGS * &#x60;KHR&#x60; - KHR * &#x60;KMF&#x60; - KMF * &#x60;KPW&#x60; - KPW * &#x60;KRH&#x60; - KRH * &#x60;KRO&#x60; - KRO * &#x60;KRW&#x60; - KRW * &#x60;KWD&#x60; - KWD * &#x60;KYD&#x60; - KYD * &#x60;KZT&#x60; - KZT * &#x60;LAK&#x60; - LAK * &#x60;LBP&#x60; - LBP * &#x60;LKR&#x60; - LKR * &#x60;LRD&#x60; - LRD * &#x60;LSL&#x60; - LSL * &#x60;LTL&#x60; - LTL * &#x60;LTT&#x60; - LTT * &#x60;LUC&#x60; - LUC * &#x60;LUF&#x60; - LUF * &#x60;LUL&#x60; - LUL * &#x60;LVL&#x60; - LVL * &#x60;LVR&#x60; - LVR * &#x60;LYD&#x60; - LYD * &#x60;MAD&#x60; - MAD * &#x60;MAF&#x60; - MAF * &#x60;MCF&#x60; - MCF * &#x60;MDC&#x60; - MDC * &#x60;MDL&#x60; - MDL * &#x60;MGA&#x60; - MGA * &#x60;MGF&#x60; - MGF * &#x60;MKD&#x60; - MKD * &#x60;MKN&#x60; - MKN * &#x60;MLF&#x60; - MLF * &#x60;MMK&#x60; - MMK * &#x60;MNT&#x60; - MNT * &#x60;MOP&#x60; - MOP * &#x60;MRO&#x60; - MRO * &#x60;MRU&#x60; - MRU * &#x60;MTL&#x60; - MTL * &#x60;MTP&#x60; - MTP * &#x60;MUR&#x60; - MUR * &#x60;MVP&#x60; - MVP * &#x60;MVR&#x60; - MVR * &#x60;MWK&#x60; - MWK * &#x60;MXN&#x60; - MXN * &#x60;MXP&#x60; - MXP * &#x60;MXV&#x60; - MXV * &#x60;MYR&#x60; - MYR * &#x60;MZE&#x60; - MZE * &#x60;MZM&#x60; - MZM * &#x60;MZN&#x60; - MZN * &#x60;NAD&#x60; - NAD * &#x60;NGN&#x60; - NGN * &#x60;NIC&#x60; - NIC * &#x60;NIO&#x60; - NIO * &#x60;NLG&#x60; - NLG * &#x60;NOK&#x60; - NOK * &#x60;NPR&#x60; - NPR * &#x60;NZD&#x60; - NZD * &#x60;OMR&#x60; - OMR * &#x60;PAB&#x60; - PAB * &#x60;PEI&#x60; - PEI * &#x60;PEN&#x60; - PEN * &#x60;PES&#x60; - PES * &#x60;PGK&#x60; - PGK * &#x60;PHP&#x60; - PHP * &#x60;PKR&#x60; - PKR * &#x60;PLN&#x60; - PLN * &#x60;PLZ&#x60; - PLZ * &#x60;PTE&#x60; - PTE * &#x60;PYG&#x60; - PYG * &#x60;QAR&#x60; - QAR * &#x60;RHD&#x60; - RHD * &#x60;ROL&#x60; - ROL * &#x60;RON&#x60; - RON * &#x60;RSD&#x60; - RSD * &#x60;RUB&#x60; - RUB * &#x60;RUR&#x60; - RUR * &#x60;RWF&#x60; - RWF * &#x60;SAR&#x60; - SAR * &#x60;SBD&#x60; - SBD * &#x60;SCR&#x60; - SCR * &#x60;SDD&#x60; - SDD * &#x60;SDG&#x60; - SDG * &#x60;SDP&#x60; - SDP * &#x60;SEK&#x60; - SEK * &#x60;SGD&#x60; - SGD * &#x60;SHP&#x60; - SHP * &#x60;SIT&#x60; - SIT * &#x60;SKK&#x60; - SKK * &#x60;SLE&#x60; - SLE * &#x60;SLL&#x60; - SLL * &#x60;SOS&#x60; - SOS * &#x60;SRD&#x60; - SRD * &#x60;SRG&#x60; - SRG * &#x60;SSP&#x60; - SSP * &#x60;STD&#x60; - STD * &#x60;STN&#x60; - STN * &#x60;SUR&#x60; - SUR * &#x60;SVC&#x60; - SVC * &#x60;SYP&#x60; - SYP * &#x60;SZL&#x60; - SZL * &#x60;THB&#x60; - THB * &#x60;TJR&#x60; - TJR * &#x60;TJS&#x60; - TJS * &#x60;TMM&#x60; - TMM * &#x60;TMT&#x60; - TMT * &#x60;TND&#x60; - TND * &#x60;TOP&#x60; - TOP * &#x60;TPE&#x60; - TPE * &#x60;TRL&#x60; - TRL * &#x60;TRY&#x60; - TRY * &#x60;TTD&#x60; - TTD * &#x60;TWD&#x60; - TWD * &#x60;TZS&#x60; - TZS * &#x60;UAH&#x60; - UAH * &#x60;UAK&#x60; - UAK * &#x60;UGS&#x60; - UGS * &#x60;UGX&#x60; - UGX * &#x60;USD&#x60; - USD * &#x60;USN&#x60; - USN * &#x60;USS&#x60; - USS * &#x60;UYI&#x60; - UYI * &#x60;UYP&#x60; - UYP * &#x60;UYU&#x60; - UYU * &#x60;UYW&#x60; - UYW * &#x60;UZS&#x60; - UZS * &#x60;VEB&#x60; - VEB * &#x60;VED&#x60; - VED * &#x60;VEF&#x60; - VEF * &#x60;VES&#x60; - VES * &#x60;VND&#x60; - VND * &#x60;VNN&#x60; - VNN * &#x60;VUV&#x60; - VUV * &#x60;WST&#x60; - WST * &#x60;XAF&#x60; - XAF * &#x60;XAG&#x60; - XAG * &#x60;XAU&#x60; - XAU * &#x60;XBA&#x60; - XBA * &#x60;XBB&#x60; - XBB * &#x60;XBC&#x60; - XBC * &#x60;XBD&#x60; - XBD * &#x60;XCD&#x60; - XCD * &#x60;XDR&#x60; - XDR * &#x60;XEU&#x60; - XEU * &#x60;XFO&#x60; - XFO * &#x60;XFU&#x60; - XFU * &#x60;XOF&#x60; - XOF * &#x60;XPD&#x60; - XPD * &#x60;XPF&#x60; - XPF * &#x60;XPT&#x60; - XPT * &#x60;XRE&#x60; - XRE * &#x60;XSU&#x60; - XSU * &#x60;XTS&#x60; - XTS * &#x60;XUA&#x60; - XUA * &#x60;XXX&#x60; - XXX * &#x60;YDD&#x60; - YDD * &#x60;YER&#x60; - YER * &#x60;YUD&#x60; - YUD * &#x60;YUM&#x60; - YUM * &#x60;YUN&#x60; - YUN * &#x60;YUR&#x60; - YUR * &#x60;ZAL&#x60; - ZAL * &#x60;ZAR&#x60; - ZAR * &#x60;ZMK&#x60; - ZMK * &#x60;ZMW&#x60; - ZMW * &#x60;ZRN&#x60; - ZRN * &#x60;ZRZ&#x60; - ZRZ * &#x60;ZWD&#x60; - ZWD * &#x60;ZWL&#x60; - ZWL * &#x60;ZWR&#x60; - ZWR | [optional] 
 **var_date** | **date**|  | [optional] 
 **date__gt** | **date**|  | [optional] 
 **date__gte** | **date**|  | [optional] 
 **date__lt** | **date**|  | [optional] 
 **date__lte** | **date**|  | [optional] 
 **date__month** | **float**|  | [optional] 
 **date__year** | **float**|  | [optional] 
 **labels_tags__contains** | **str**|  | [optional] 
 **location_id** | **int**|  | [optional] 
 **location_id__isnull** | **bool**|  | [optional] 
 **location_osm_id** | **int**|  | [optional] 
 **location_osm_type** | **str**| * &#x60;NODE&#x60; - NODE * &#x60;WAY&#x60; - WAY * &#x60;RELATION&#x60; - RELATION | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **origins_tags__contains** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **price** | **float**|  | [optional] 
 **price__gt** | **float**|  | [optional] 
 **price__gte** | **float**|  | [optional] 
 **price__lt** | **float**|  | [optional] 
 **price__lte** | **float**|  | [optional] 
 **price_is_discounted** | **bool**|  | [optional] 
 **product_code** | **str**|  | [optional] 
 **product_id** | **int**|  | [optional] 
 **product_id__isnull** | **bool**|  | [optional] 
 **proof_id** | **int**|  | [optional] 
 **proof_id__isnull** | **bool**|  | [optional] 
 **size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPriceFullList**](PaginatedPriceFullList.md)

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

# **prices_partial_update**
> PriceUpdate prices_partial_update(id, patched_price_update=patched_price_update)



### Example


```python
import openapi_client
from openapi_client.models.patched_price_update import PatchedPriceUpdate
from openapi_client.models.price_update import PriceUpdate
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
    api_instance = openapi_client.PricesApi(api_client)
    id = 56 # int | A unique integer value identifying this Price.
    patched_price_update = openapi_client.PatchedPriceUpdate() # PatchedPriceUpdate |  (optional)

    try:
        api_response = api_instance.prices_partial_update(id, patched_price_update=patched_price_update)
        print("The response of PricesApi->prices_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Price. | 
 **patched_price_update** | [**PatchedPriceUpdate**](PatchedPriceUpdate.md)|  | [optional] 

### Return type

[**PriceUpdate**](PriceUpdate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_retrieve**
> PriceFull prices_retrieve(id)



### Example


```python
import openapi_client
from openapi_client.models.price_full import PriceFull
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
    api_instance = openapi_client.PricesApi(api_client)
    id = 56 # int | A unique integer value identifying this Price.

    try:
        api_response = api_instance.prices_retrieve(id)
        print("The response of PricesApi->prices_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Price. | 

### Return type

[**PriceFull**](PriceFull.md)

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

# **prices_stats_retrieve**
> PriceStats prices_stats_retrieve(category_tag=category_tag, created__gte=created__gte, created__lte=created__lte, currency=currency, var_date=var_date, date__gt=date__gt, date__gte=date__gte, date__lt=date__lt, date__lte=date__lte, date__month=date__month, date__year=date__year, labels_tags__contains=labels_tags__contains, location_id=location_id, location_id__isnull=location_id__isnull, location_osm_id=location_osm_id, location_osm_type=location_osm_type, order_by=order_by, origins_tags__contains=origins_tags__contains, owner=owner, price=price, price__gt=price__gt, price__gte=price__gte, price__lt=price__lt, price__lte=price__lte, price_is_discounted=price_is_discounted, product_code=product_code, product_id=product_id, product_id__isnull=product_id__isnull, proof_id=proof_id, proof_id__isnull=proof_id__isnull)



### Example


```python
import openapi_client
from openapi_client.models.price_stats import PriceStats
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
    api_instance = openapi_client.PricesApi(api_client)
    category_tag = 'category_tag_example' # str |  (optional)
    created__gte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created__lte = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    currency = 'currency_example' # str | * `ADP` - ADP * `AED` - AED * `AFA` - AFA * `AFN` - AFN * `ALK` - ALK * `ALL` - ALL * `AMD` - AMD * `ANG` - ANG * `AOA` - AOA * `AOK` - AOK * `AON` - AON * `AOR` - AOR * `ARA` - ARA * `ARL` - ARL * `ARM` - ARM * `ARP` - ARP * `ARS` - ARS * `ATS` - ATS * `AUD` - AUD * `AWG` - AWG * `AZM` - AZM * `AZN` - AZN * `BAD` - BAD * `BAM` - BAM * `BAN` - BAN * `BBD` - BBD * `BDT` - BDT * `BEC` - BEC * `BEF` - BEF * `BEL` - BEL * `BGL` - BGL * `BGM` - BGM * `BGN` - BGN * `BGO` - BGO * `BHD` - BHD * `BIF` - BIF * `BMD` - BMD * `BND` - BND * `BOB` - BOB * `BOL` - BOL * `BOP` - BOP * `BOV` - BOV * `BRB` - BRB * `BRC` - BRC * `BRE` - BRE * `BRL` - BRL * `BRN` - BRN * `BRR` - BRR * `BRZ` - BRZ * `BSD` - BSD * `BTN` - BTN * `BUK` - BUK * `BWP` - BWP * `BYB` - BYB * `BYN` - BYN * `BYR` - BYR * `BZD` - BZD * `CAD` - CAD * `CDF` - CDF * `CHE` - CHE * `CHF` - CHF * `CHW` - CHW * `CLE` - CLE * `CLF` - CLF * `CLP` - CLP * `CNH` - CNH * `CNX` - CNX * `CNY` - CNY * `COP` - COP * `COU` - COU * `CRC` - CRC * `CSD` - CSD * `CSK` - CSK * `CUC` - CUC * `CUP` - CUP * `CVE` - CVE * `CYP` - CYP * `CZK` - CZK * `DDM` - DDM * `DEM` - DEM * `DJF` - DJF * `DKK` - DKK * `DOP` - DOP * `DZD` - DZD * `ECS` - ECS * `ECV` - ECV * `EEK` - EEK * `EGP` - EGP * `ERN` - ERN * `ESA` - ESA * `ESB` - ESB * `ESP` - ESP * `ETB` - ETB * `EUR` - EUR * `FIM` - FIM * `FJD` - FJD * `FKP` - FKP * `FRF` - FRF * `GBP` - GBP * `GEK` - GEK * `GEL` - GEL * `GHC` - GHC * `GHS` - GHS * `GIP` - GIP * `GMD` - GMD * `GNF` - GNF * `GNS` - GNS * `GQE` - GQE * `GRD` - GRD * `GTQ` - GTQ * `GWE` - GWE * `GWP` - GWP * `GYD` - GYD * `HKD` - HKD * `HNL` - HNL * `HRD` - HRD * `HRK` - HRK * `HTG` - HTG * `HUF` - HUF * `IDR` - IDR * `IEP` - IEP * `ILP` - ILP * `ILR` - ILR * `ILS` - ILS * `INR` - INR * `IQD` - IQD * `IRR` - IRR * `ISJ` - ISJ * `ISK` - ISK * `ITL` - ITL * `JMD` - JMD * `JOD` - JOD * `JPY` - JPY * `KES` - KES * `KGS` - KGS * `KHR` - KHR * `KMF` - KMF * `KPW` - KPW * `KRH` - KRH * `KRO` - KRO * `KRW` - KRW * `KWD` - KWD * `KYD` - KYD * `KZT` - KZT * `LAK` - LAK * `LBP` - LBP * `LKR` - LKR * `LRD` - LRD * `LSL` - LSL * `LTL` - LTL * `LTT` - LTT * `LUC` - LUC * `LUF` - LUF * `LUL` - LUL * `LVL` - LVL * `LVR` - LVR * `LYD` - LYD * `MAD` - MAD * `MAF` - MAF * `MCF` - MCF * `MDC` - MDC * `MDL` - MDL * `MGA` - MGA * `MGF` - MGF * `MKD` - MKD * `MKN` - MKN * `MLF` - MLF * `MMK` - MMK * `MNT` - MNT * `MOP` - MOP * `MRO` - MRO * `MRU` - MRU * `MTL` - MTL * `MTP` - MTP * `MUR` - MUR * `MVP` - MVP * `MVR` - MVR * `MWK` - MWK * `MXN` - MXN * `MXP` - MXP * `MXV` - MXV * `MYR` - MYR * `MZE` - MZE * `MZM` - MZM * `MZN` - MZN * `NAD` - NAD * `NGN` - NGN * `NIC` - NIC * `NIO` - NIO * `NLG` - NLG * `NOK` - NOK * `NPR` - NPR * `NZD` - NZD * `OMR` - OMR * `PAB` - PAB * `PEI` - PEI * `PEN` - PEN * `PES` - PES * `PGK` - PGK * `PHP` - PHP * `PKR` - PKR * `PLN` - PLN * `PLZ` - PLZ * `PTE` - PTE * `PYG` - PYG * `QAR` - QAR * `RHD` - RHD * `ROL` - ROL * `RON` - RON * `RSD` - RSD * `RUB` - RUB * `RUR` - RUR * `RWF` - RWF * `SAR` - SAR * `SBD` - SBD * `SCR` - SCR * `SDD` - SDD * `SDG` - SDG * `SDP` - SDP * `SEK` - SEK * `SGD` - SGD * `SHP` - SHP * `SIT` - SIT * `SKK` - SKK * `SLE` - SLE * `SLL` - SLL * `SOS` - SOS * `SRD` - SRD * `SRG` - SRG * `SSP` - SSP * `STD` - STD * `STN` - STN * `SUR` - SUR * `SVC` - SVC * `SYP` - SYP * `SZL` - SZL * `THB` - THB * `TJR` - TJR * `TJS` - TJS * `TMM` - TMM * `TMT` - TMT * `TND` - TND * `TOP` - TOP * `TPE` - TPE * `TRL` - TRL * `TRY` - TRY * `TTD` - TTD * `TWD` - TWD * `TZS` - TZS * `UAH` - UAH * `UAK` - UAK * `UGS` - UGS * `UGX` - UGX * `USD` - USD * `USN` - USN * `USS` - USS * `UYI` - UYI * `UYP` - UYP * `UYU` - UYU * `UYW` - UYW * `UZS` - UZS * `VEB` - VEB * `VED` - VED * `VEF` - VEF * `VES` - VES * `VND` - VND * `VNN` - VNN * `VUV` - VUV * `WST` - WST * `XAF` - XAF * `XAG` - XAG * `XAU` - XAU * `XBA` - XBA * `XBB` - XBB * `XBC` - XBC * `XBD` - XBD * `XCD` - XCD * `XDR` - XDR * `XEU` - XEU * `XFO` - XFO * `XFU` - XFU * `XOF` - XOF * `XPD` - XPD * `XPF` - XPF * `XPT` - XPT * `XRE` - XRE * `XSU` - XSU * `XTS` - XTS * `XUA` - XUA * `XXX` - XXX * `YDD` - YDD * `YER` - YER * `YUD` - YUD * `YUM` - YUM * `YUN` - YUN * `YUR` - YUR * `ZAL` - ZAL * `ZAR` - ZAR * `ZMK` - ZMK * `ZMW` - ZMW * `ZRN` - ZRN * `ZRZ` - ZRZ * `ZWD` - ZWD * `ZWL` - ZWL * `ZWR` - ZWR (optional)
    var_date = '2013-10-20' # date |  (optional)
    date__gt = '2013-10-20' # date |  (optional)
    date__gte = '2013-10-20' # date |  (optional)
    date__lt = '2013-10-20' # date |  (optional)
    date__lte = '2013-10-20' # date |  (optional)
    date__month = 3.4 # float |  (optional)
    date__year = 3.4 # float |  (optional)
    labels_tags__contains = 'labels_tags__contains_example' # str |  (optional)
    location_id = 56 # int |  (optional)
    location_id__isnull = True # bool |  (optional)
    location_osm_id = 56 # int |  (optional)
    location_osm_type = 'location_osm_type_example' # str | * `NODE` - NODE * `WAY` - WAY * `RELATION` - RELATION (optional)
    order_by = 'order_by_example' # str | Which field to use when ordering the results. (optional)
    origins_tags__contains = 'origins_tags__contains_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    price = 3.4 # float |  (optional)
    price__gt = 3.4 # float |  (optional)
    price__gte = 3.4 # float |  (optional)
    price__lt = 3.4 # float |  (optional)
    price__lte = 3.4 # float |  (optional)
    price_is_discounted = True # bool |  (optional)
    product_code = 'product_code_example' # str |  (optional)
    product_id = 56 # int |  (optional)
    product_id__isnull = True # bool |  (optional)
    proof_id = 56 # int |  (optional)
    proof_id__isnull = True # bool |  (optional)

    try:
        api_response = api_instance.prices_stats_retrieve(category_tag=category_tag, created__gte=created__gte, created__lte=created__lte, currency=currency, var_date=var_date, date__gt=date__gt, date__gte=date__gte, date__lt=date__lt, date__lte=date__lte, date__month=date__month, date__year=date__year, labels_tags__contains=labels_tags__contains, location_id=location_id, location_id__isnull=location_id__isnull, location_osm_id=location_osm_id, location_osm_type=location_osm_type, order_by=order_by, origins_tags__contains=origins_tags__contains, owner=owner, price=price, price__gt=price__gt, price__gte=price__gte, price__lt=price__lt, price__lte=price__lte, price_is_discounted=price_is_discounted, product_code=product_code, product_id=product_id, product_id__isnull=product_id__isnull, proof_id=proof_id, proof_id__isnull=proof_id__isnull)
        print("The response of PricesApi->prices_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->prices_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_tag** | **str**|  | [optional] 
 **created__gte** | **datetime**|  | [optional] 
 **created__lte** | **datetime**|  | [optional] 
 **currency** | **str**| * &#x60;ADP&#x60; - ADP * &#x60;AED&#x60; - AED * &#x60;AFA&#x60; - AFA * &#x60;AFN&#x60; - AFN * &#x60;ALK&#x60; - ALK * &#x60;ALL&#x60; - ALL * &#x60;AMD&#x60; - AMD * &#x60;ANG&#x60; - ANG * &#x60;AOA&#x60; - AOA * &#x60;AOK&#x60; - AOK * &#x60;AON&#x60; - AON * &#x60;AOR&#x60; - AOR * &#x60;ARA&#x60; - ARA * &#x60;ARL&#x60; - ARL * &#x60;ARM&#x60; - ARM * &#x60;ARP&#x60; - ARP * &#x60;ARS&#x60; - ARS * &#x60;ATS&#x60; - ATS * &#x60;AUD&#x60; - AUD * &#x60;AWG&#x60; - AWG * &#x60;AZM&#x60; - AZM * &#x60;AZN&#x60; - AZN * &#x60;BAD&#x60; - BAD * &#x60;BAM&#x60; - BAM * &#x60;BAN&#x60; - BAN * &#x60;BBD&#x60; - BBD * &#x60;BDT&#x60; - BDT * &#x60;BEC&#x60; - BEC * &#x60;BEF&#x60; - BEF * &#x60;BEL&#x60; - BEL * &#x60;BGL&#x60; - BGL * &#x60;BGM&#x60; - BGM * &#x60;BGN&#x60; - BGN * &#x60;BGO&#x60; - BGO * &#x60;BHD&#x60; - BHD * &#x60;BIF&#x60; - BIF * &#x60;BMD&#x60; - BMD * &#x60;BND&#x60; - BND * &#x60;BOB&#x60; - BOB * &#x60;BOL&#x60; - BOL * &#x60;BOP&#x60; - BOP * &#x60;BOV&#x60; - BOV * &#x60;BRB&#x60; - BRB * &#x60;BRC&#x60; - BRC * &#x60;BRE&#x60; - BRE * &#x60;BRL&#x60; - BRL * &#x60;BRN&#x60; - BRN * &#x60;BRR&#x60; - BRR * &#x60;BRZ&#x60; - BRZ * &#x60;BSD&#x60; - BSD * &#x60;BTN&#x60; - BTN * &#x60;BUK&#x60; - BUK * &#x60;BWP&#x60; - BWP * &#x60;BYB&#x60; - BYB * &#x60;BYN&#x60; - BYN * &#x60;BYR&#x60; - BYR * &#x60;BZD&#x60; - BZD * &#x60;CAD&#x60; - CAD * &#x60;CDF&#x60; - CDF * &#x60;CHE&#x60; - CHE * &#x60;CHF&#x60; - CHF * &#x60;CHW&#x60; - CHW * &#x60;CLE&#x60; - CLE * &#x60;CLF&#x60; - CLF * &#x60;CLP&#x60; - CLP * &#x60;CNH&#x60; - CNH * &#x60;CNX&#x60; - CNX * &#x60;CNY&#x60; - CNY * &#x60;COP&#x60; - COP * &#x60;COU&#x60; - COU * &#x60;CRC&#x60; - CRC * &#x60;CSD&#x60; - CSD * &#x60;CSK&#x60; - CSK * &#x60;CUC&#x60; - CUC * &#x60;CUP&#x60; - CUP * &#x60;CVE&#x60; - CVE * &#x60;CYP&#x60; - CYP * &#x60;CZK&#x60; - CZK * &#x60;DDM&#x60; - DDM * &#x60;DEM&#x60; - DEM * &#x60;DJF&#x60; - DJF * &#x60;DKK&#x60; - DKK * &#x60;DOP&#x60; - DOP * &#x60;DZD&#x60; - DZD * &#x60;ECS&#x60; - ECS * &#x60;ECV&#x60; - ECV * &#x60;EEK&#x60; - EEK * &#x60;EGP&#x60; - EGP * &#x60;ERN&#x60; - ERN * &#x60;ESA&#x60; - ESA * &#x60;ESB&#x60; - ESB * &#x60;ESP&#x60; - ESP * &#x60;ETB&#x60; - ETB * &#x60;EUR&#x60; - EUR * &#x60;FIM&#x60; - FIM * &#x60;FJD&#x60; - FJD * &#x60;FKP&#x60; - FKP * &#x60;FRF&#x60; - FRF * &#x60;GBP&#x60; - GBP * &#x60;GEK&#x60; - GEK * &#x60;GEL&#x60; - GEL * &#x60;GHC&#x60; - GHC * &#x60;GHS&#x60; - GHS * &#x60;GIP&#x60; - GIP * &#x60;GMD&#x60; - GMD * &#x60;GNF&#x60; - GNF * &#x60;GNS&#x60; - GNS * &#x60;GQE&#x60; - GQE * &#x60;GRD&#x60; - GRD * &#x60;GTQ&#x60; - GTQ * &#x60;GWE&#x60; - GWE * &#x60;GWP&#x60; - GWP * &#x60;GYD&#x60; - GYD * &#x60;HKD&#x60; - HKD * &#x60;HNL&#x60; - HNL * &#x60;HRD&#x60; - HRD * &#x60;HRK&#x60; - HRK * &#x60;HTG&#x60; - HTG * &#x60;HUF&#x60; - HUF * &#x60;IDR&#x60; - IDR * &#x60;IEP&#x60; - IEP * &#x60;ILP&#x60; - ILP * &#x60;ILR&#x60; - ILR * &#x60;ILS&#x60; - ILS * &#x60;INR&#x60; - INR * &#x60;IQD&#x60; - IQD * &#x60;IRR&#x60; - IRR * &#x60;ISJ&#x60; - ISJ * &#x60;ISK&#x60; - ISK * &#x60;ITL&#x60; - ITL * &#x60;JMD&#x60; - JMD * &#x60;JOD&#x60; - JOD * &#x60;JPY&#x60; - JPY * &#x60;KES&#x60; - KES * &#x60;KGS&#x60; - KGS * &#x60;KHR&#x60; - KHR * &#x60;KMF&#x60; - KMF * &#x60;KPW&#x60; - KPW * &#x60;KRH&#x60; - KRH * &#x60;KRO&#x60; - KRO * &#x60;KRW&#x60; - KRW * &#x60;KWD&#x60; - KWD * &#x60;KYD&#x60; - KYD * &#x60;KZT&#x60; - KZT * &#x60;LAK&#x60; - LAK * &#x60;LBP&#x60; - LBP * &#x60;LKR&#x60; - LKR * &#x60;LRD&#x60; - LRD * &#x60;LSL&#x60; - LSL * &#x60;LTL&#x60; - LTL * &#x60;LTT&#x60; - LTT * &#x60;LUC&#x60; - LUC * &#x60;LUF&#x60; - LUF * &#x60;LUL&#x60; - LUL * &#x60;LVL&#x60; - LVL * &#x60;LVR&#x60; - LVR * &#x60;LYD&#x60; - LYD * &#x60;MAD&#x60; - MAD * &#x60;MAF&#x60; - MAF * &#x60;MCF&#x60; - MCF * &#x60;MDC&#x60; - MDC * &#x60;MDL&#x60; - MDL * &#x60;MGA&#x60; - MGA * &#x60;MGF&#x60; - MGF * &#x60;MKD&#x60; - MKD * &#x60;MKN&#x60; - MKN * &#x60;MLF&#x60; - MLF * &#x60;MMK&#x60; - MMK * &#x60;MNT&#x60; - MNT * &#x60;MOP&#x60; - MOP * &#x60;MRO&#x60; - MRO * &#x60;MRU&#x60; - MRU * &#x60;MTL&#x60; - MTL * &#x60;MTP&#x60; - MTP * &#x60;MUR&#x60; - MUR * &#x60;MVP&#x60; - MVP * &#x60;MVR&#x60; - MVR * &#x60;MWK&#x60; - MWK * &#x60;MXN&#x60; - MXN * &#x60;MXP&#x60; - MXP * &#x60;MXV&#x60; - MXV * &#x60;MYR&#x60; - MYR * &#x60;MZE&#x60; - MZE * &#x60;MZM&#x60; - MZM * &#x60;MZN&#x60; - MZN * &#x60;NAD&#x60; - NAD * &#x60;NGN&#x60; - NGN * &#x60;NIC&#x60; - NIC * &#x60;NIO&#x60; - NIO * &#x60;NLG&#x60; - NLG * &#x60;NOK&#x60; - NOK * &#x60;NPR&#x60; - NPR * &#x60;NZD&#x60; - NZD * &#x60;OMR&#x60; - OMR * &#x60;PAB&#x60; - PAB * &#x60;PEI&#x60; - PEI * &#x60;PEN&#x60; - PEN * &#x60;PES&#x60; - PES * &#x60;PGK&#x60; - PGK * &#x60;PHP&#x60; - PHP * &#x60;PKR&#x60; - PKR * &#x60;PLN&#x60; - PLN * &#x60;PLZ&#x60; - PLZ * &#x60;PTE&#x60; - PTE * &#x60;PYG&#x60; - PYG * &#x60;QAR&#x60; - QAR * &#x60;RHD&#x60; - RHD * &#x60;ROL&#x60; - ROL * &#x60;RON&#x60; - RON * &#x60;RSD&#x60; - RSD * &#x60;RUB&#x60; - RUB * &#x60;RUR&#x60; - RUR * &#x60;RWF&#x60; - RWF * &#x60;SAR&#x60; - SAR * &#x60;SBD&#x60; - SBD * &#x60;SCR&#x60; - SCR * &#x60;SDD&#x60; - SDD * &#x60;SDG&#x60; - SDG * &#x60;SDP&#x60; - SDP * &#x60;SEK&#x60; - SEK * &#x60;SGD&#x60; - SGD * &#x60;SHP&#x60; - SHP * &#x60;SIT&#x60; - SIT * &#x60;SKK&#x60; - SKK * &#x60;SLE&#x60; - SLE * &#x60;SLL&#x60; - SLL * &#x60;SOS&#x60; - SOS * &#x60;SRD&#x60; - SRD * &#x60;SRG&#x60; - SRG * &#x60;SSP&#x60; - SSP * &#x60;STD&#x60; - STD * &#x60;STN&#x60; - STN * &#x60;SUR&#x60; - SUR * &#x60;SVC&#x60; - SVC * &#x60;SYP&#x60; - SYP * &#x60;SZL&#x60; - SZL * &#x60;THB&#x60; - THB * &#x60;TJR&#x60; - TJR * &#x60;TJS&#x60; - TJS * &#x60;TMM&#x60; - TMM * &#x60;TMT&#x60; - TMT * &#x60;TND&#x60; - TND * &#x60;TOP&#x60; - TOP * &#x60;TPE&#x60; - TPE * &#x60;TRL&#x60; - TRL * &#x60;TRY&#x60; - TRY * &#x60;TTD&#x60; - TTD * &#x60;TWD&#x60; - TWD * &#x60;TZS&#x60; - TZS * &#x60;UAH&#x60; - UAH * &#x60;UAK&#x60; - UAK * &#x60;UGS&#x60; - UGS * &#x60;UGX&#x60; - UGX * &#x60;USD&#x60; - USD * &#x60;USN&#x60; - USN * &#x60;USS&#x60; - USS * &#x60;UYI&#x60; - UYI * &#x60;UYP&#x60; - UYP * &#x60;UYU&#x60; - UYU * &#x60;UYW&#x60; - UYW * &#x60;UZS&#x60; - UZS * &#x60;VEB&#x60; - VEB * &#x60;VED&#x60; - VED * &#x60;VEF&#x60; - VEF * &#x60;VES&#x60; - VES * &#x60;VND&#x60; - VND * &#x60;VNN&#x60; - VNN * &#x60;VUV&#x60; - VUV * &#x60;WST&#x60; - WST * &#x60;XAF&#x60; - XAF * &#x60;XAG&#x60; - XAG * &#x60;XAU&#x60; - XAU * &#x60;XBA&#x60; - XBA * &#x60;XBB&#x60; - XBB * &#x60;XBC&#x60; - XBC * &#x60;XBD&#x60; - XBD * &#x60;XCD&#x60; - XCD * &#x60;XDR&#x60; - XDR * &#x60;XEU&#x60; - XEU * &#x60;XFO&#x60; - XFO * &#x60;XFU&#x60; - XFU * &#x60;XOF&#x60; - XOF * &#x60;XPD&#x60; - XPD * &#x60;XPF&#x60; - XPF * &#x60;XPT&#x60; - XPT * &#x60;XRE&#x60; - XRE * &#x60;XSU&#x60; - XSU * &#x60;XTS&#x60; - XTS * &#x60;XUA&#x60; - XUA * &#x60;XXX&#x60; - XXX * &#x60;YDD&#x60; - YDD * &#x60;YER&#x60; - YER * &#x60;YUD&#x60; - YUD * &#x60;YUM&#x60; - YUM * &#x60;YUN&#x60; - YUN * &#x60;YUR&#x60; - YUR * &#x60;ZAL&#x60; - ZAL * &#x60;ZAR&#x60; - ZAR * &#x60;ZMK&#x60; - ZMK * &#x60;ZMW&#x60; - ZMW * &#x60;ZRN&#x60; - ZRN * &#x60;ZRZ&#x60; - ZRZ * &#x60;ZWD&#x60; - ZWD * &#x60;ZWL&#x60; - ZWL * &#x60;ZWR&#x60; - ZWR | [optional] 
 **var_date** | **date**|  | [optional] 
 **date__gt** | **date**|  | [optional] 
 **date__gte** | **date**|  | [optional] 
 **date__lt** | **date**|  | [optional] 
 **date__lte** | **date**|  | [optional] 
 **date__month** | **float**|  | [optional] 
 **date__year** | **float**|  | [optional] 
 **labels_tags__contains** | **str**|  | [optional] 
 **location_id** | **int**|  | [optional] 
 **location_id__isnull** | **bool**|  | [optional] 
 **location_osm_id** | **int**|  | [optional] 
 **location_osm_type** | **str**| * &#x60;NODE&#x60; - NODE * &#x60;WAY&#x60; - WAY * &#x60;RELATION&#x60; - RELATION | [optional] 
 **order_by** | **str**| Which field to use when ordering the results. | [optional] 
 **origins_tags__contains** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **price** | **float**|  | [optional] 
 **price__gt** | **float**|  | [optional] 
 **price__gte** | **float**|  | [optional] 
 **price__lt** | **float**|  | [optional] 
 **price__lte** | **float**|  | [optional] 
 **price_is_discounted** | **bool**|  | [optional] 
 **product_code** | **str**|  | [optional] 
 **product_id** | **int**|  | [optional] 
 **product_id__isnull** | **bool**|  | [optional] 
 **proof_id** | **int**|  | [optional] 
 **proof_id__isnull** | **bool**|  | [optional] 

### Return type

[**PriceStats**](PriceStats.md)

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

