# ProofUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TypeEnum**](TypeEnum.md) |  | 
**currency** | [**PatchedPriceUpdateCurrency**](PatchedPriceUpdateCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.proof_update import ProofUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProofUpdate from a JSON string
proof_update_instance = ProofUpdate.from_json(json)
# print the JSON string representation of the object
print(ProofUpdate.to_json())

# convert the object into a dict
proof_update_dict = proof_update_instance.to_dict()
# create an instance of ProofUpdate from a dict
proof_update_from_dict = ProofUpdate.from_dict(proof_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


