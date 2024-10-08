# PaginatedLocationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Location]**](Location.md) |  | 

## Example

```python
from openapi_client.models.paginated_location_list import PaginatedLocationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLocationList from a JSON string
paginated_location_list_instance = PaginatedLocationList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLocationList.to_json())

# convert the object into a dict
paginated_location_list_dict = paginated_location_list_instance.to_dict()
# create an instance of PaginatedLocationList from a dict
paginated_location_list_from_dict = PaginatedLocationList.from_dict(paginated_location_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


