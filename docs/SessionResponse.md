# SessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | 

## Example

```python
from openapi_client.models.session_response import SessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SessionResponse from a JSON string
session_response_instance = SessionResponse.from_json(json)
# print the JSON string representation of the object
print(SessionResponse.to_json())

# convert the object into a dict
session_response_dict = session_response_instance.to_dict()
# create an instance of SessionResponse from a dict
session_response_from_dict = SessionResponse.from_dict(session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


