# SessionFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**token** | **str** |  | 
**created** | **str** |  | 
**last_used** | **str** |  | 

## Example

```python
from openapi_client.models.session_full import SessionFull

# TODO update the JSON string below
json = "{}"
# create an instance of SessionFull from a JSON string
session_full_instance = SessionFull.from_json(json)
# print the JSON string representation of the object
print(SessionFull.to_json())

# convert the object into a dict
session_full_dict = session_full_instance.to_dict()
# create an instance of SessionFull from a dict
session_full_from_dict = SessionFull.from_dict(session_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


