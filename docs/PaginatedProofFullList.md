# PaginatedProofFullList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProofFull]**](ProofFull.md) |  | 

## Example

```python
from openapi_client.models.paginated_proof_full_list import PaginatedProofFullList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProofFullList from a JSON string
paginated_proof_full_list_instance = PaginatedProofFullList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProofFullList.to_json())

# convert the object into a dict
paginated_proof_full_list_dict = paginated_proof_full_list_instance.to_dict()
# create an instance of PaginatedProofFullList from a dict
paginated_proof_full_list_from_dict = PaginatedProofFullList.from_dict(paginated_proof_full_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


