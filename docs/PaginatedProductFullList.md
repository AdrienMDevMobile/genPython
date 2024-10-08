# PaginatedProductFullList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductFull]**](ProductFull.md) |  | 

## Example

```python
from openapi_client.models.paginated_product_full_list import PaginatedProductFullList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductFullList from a JSON string
paginated_product_full_list_instance = PaginatedProductFullList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProductFullList.to_json())

# convert the object into a dict
paginated_product_full_list_dict = paginated_product_full_list_instance.to_dict()
# create an instance of PaginatedProductFullList from a dict
paginated_product_full_list_from_dict = PaginatedProductFullList.from_dict(paginated_product_full_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


