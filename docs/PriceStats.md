# PriceStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price__count** | **int** |  | 
**price__min** | **float** |  | 
**price__max** | **float** |  | 
**price__avg** | **float** |  | 

## Example

```python
from openapi_client.models.price_stats import PriceStats

# TODO update the JSON string below
json = "{}"
# create an instance of PriceStats from a JSON string
price_stats_instance = PriceStats.from_json(json)
# print the JSON string representation of the object
print(PriceStats.to_json())

# convert the object into a dict
price_stats_dict = price_stats_instance.to_dict()
# create an instance of PriceStats from a dict
price_stats_from_dict = PriceStats.from_dict(price_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


