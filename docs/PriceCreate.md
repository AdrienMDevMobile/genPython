# PriceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**price_is_discounted** | **bool** |  | [optional] 
**price_without_discount** | **float** |  | [optional] 
**price_per** | [**PatchedPriceUpdatePricePer**](PatchedPriceUpdatePricePer.md) |  | [optional] 
**currency** | [**PatchedPriceUpdateCurrency**](PatchedPriceUpdateCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**product_code** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**category_tag** | **str** |  | [optional] 
**labels_tags** | **object** |  | [optional] 
**origins_tags** | **object** |  | [optional] 
**location_osm_id** | **int** |  | [optional] 
**location_osm_type** | [**PriceCreateLocationOsmType**](PriceCreateLocationOsmType.md) |  | [optional] 
**proof_id** | **int** |  | 

## Example

```python
from openapi_client.models.price_create import PriceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PriceCreate from a JSON string
price_create_instance = PriceCreate.from_json(json)
# print the JSON string representation of the object
print(PriceCreate.to_json())

# convert the object into a dict
price_create_dict = price_create_instance.to_dict()
# create an instance of PriceCreate from a dict
price_create_from_dict = PriceCreate.from_dict(price_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


