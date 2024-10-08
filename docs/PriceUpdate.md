# PriceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**price_is_discounted** | **bool** |  | [optional] 
**price_without_discount** | **float** |  | [optional] 
**price_per** | [**PatchedPriceUpdatePricePer**](PatchedPriceUpdatePricePer.md) |  | [optional] 
**currency** | [**PatchedPriceUpdateCurrency**](PatchedPriceUpdateCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.price_update import PriceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PriceUpdate from a JSON string
price_update_instance = PriceUpdate.from_json(json)
# print the JSON string representation of the object
print(PriceUpdate.to_json())

# convert the object into a dict
price_update_dict = price_update_instance.to_dict()
# create an instance of PriceUpdate from a dict
price_update_from_dict = PriceUpdate.from_dict(price_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


