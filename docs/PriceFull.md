# PriceFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**product_id** | **int** |  | 
**location_id** | **int** |  | 
**proof_id** | **int** |  | 
**product** | [**ProductFull**](ProductFull.md) |  | 
**location** | [**Location**](Location.md) |  | 
**proof** | [**Proof**](Proof.md) |  | 
**product_code** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**category_tag** | **str** |  | [optional] 
**labels_tags** | **object** |  | [optional] 
**origins_tags** | **object** |  | [optional] 
**price** | **float** |  | [optional] 
**price_is_discounted** | **bool** |  | [optional] 
**price_without_discount** | **float** |  | [optional] 
**price_per** | [**PatchedPriceUpdatePricePer**](PatchedPriceUpdatePricePer.md) |  | [optional] 
**currency** | [**PatchedPriceUpdateCurrency**](PatchedPriceUpdateCurrency.md) |  | [optional] 
**location_osm_id** | **int** |  | [optional] 
**location_osm_type** | [**PriceCreateLocationOsmType**](PriceCreateLocationOsmType.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**owner** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.price_full import PriceFull

# TODO update the JSON string below
json = "{}"
# create an instance of PriceFull from a JSON string
price_full_instance = PriceFull.from_json(json)
# print the JSON string representation of the object
print(PriceFull.to_json())

# convert the object into a dict
price_full_dict = price_full_instance.to_dict()
# create an instance of PriceFull from a dict
price_full_from_dict = PriceFull.from_dict(price_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


