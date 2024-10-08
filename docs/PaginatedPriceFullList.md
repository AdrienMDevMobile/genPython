# PaginatedPriceFullList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PriceFull]**](PriceFull.md) |  | 

## Example

```python
from openapi_client.models.paginated_price_full_list import PaginatedPriceFullList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPriceFullList from a JSON string
paginated_price_full_list_instance = PaginatedPriceFullList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPriceFullList.to_json())

# convert the object into a dict
paginated_price_full_list_dict = paginated_price_full_list_instance.to_dict()
# create an instance of PaginatedPriceFullList from a dict
paginated_price_full_list_from_dict = PaginatedPriceFullList.from_dict(paginated_price_full_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


