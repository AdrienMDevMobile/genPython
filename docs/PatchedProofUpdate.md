# PatchedProofUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](TypeEnum.md) |  | [optional] 
**currency** | [**PatchedPriceUpdateCurrency**](PatchedPriceUpdateCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.patched_proof_update import PatchedProofUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProofUpdate from a JSON string
patched_proof_update_instance = PatchedProofUpdate.from_json(json)
# print the JSON string representation of the object
print(PatchedProofUpdate.to_json())

# convert the object into a dict
patched_proof_update_dict = patched_proof_update_instance.to_dict()
# create an instance of PatchedProofUpdate from a dict
patched_proof_update_from_dict = PatchedProofUpdate.from_dict(patched_proof_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


