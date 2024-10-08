# PatchedPriceUpdate


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
from openapi_client.models.patched_price_update import PatchedPriceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPriceUpdate from a JSON string
patched_price_update_instance = PatchedPriceUpdate.from_json(json)
# print the JSON string representation of the object
print(PatchedPriceUpdate.to_json())

# convert the object into a dict
patched_price_update_dict = patched_price_update_instance.to_dict()
# create an instance of PatchedPriceUpdate from a dict
patched_price_update_from_dict = PatchedPriceUpdate.from_dict(patched_price_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


