# PaginatedUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[User]**](User.md) |  | 

## Example

```python
from openapi_client.models.paginated_user_list import PaginatedUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserList from a JSON string
paginated_user_list_instance = PaginatedUserList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserList.to_json())

# convert the object into a dict
paginated_user_list_dict = paginated_user_list_instance.to_dict()
# create an instance of PaginatedUserList from a dict
paginated_user_list_from_dict = PaginatedUserList.from_dict(paginated_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


