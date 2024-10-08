# Proof


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**location_id** | **int** |  | 
**file_path** | **str** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**image_thumb_path** | **str** |  | [optional] 
**location_osm_id** | **int** |  | [optional] 
**location_osm_type** | [**PriceCreateLocationOsmType**](PriceCreateLocationOsmType.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**currency** | [**PatchedPriceUpdateCurrency**](PatchedPriceUpdateCurrency.md) |  | [optional] 
**price_count** | **int** |  | [optional] 
**owner** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.proof import Proof

# TODO update the JSON string below
json = "{}"
# create an instance of Proof from a JSON string
proof_instance = Proof.from_json(json)
# print the JSON string representation of the object
print(Proof.to_json())

# convert the object into a dict
proof_dict = proof_instance.to_dict()
# create an instance of Proof from a dict
proof_from_dict = Proof.from_dict(proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


