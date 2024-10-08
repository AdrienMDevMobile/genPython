# TotalStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_count** | **int** |  | [optional] 
**price_barcode_count** | **int** |  | [optional] 
**price_category_count** | **int** |  | [optional] 
**product_count** | **int** |  | [optional] 
**product_with_price_count** | **int** |  | [optional] 
**location_count** | **int** |  | [optional] 
**location_with_price_count** | **int** |  | [optional] 
**proof_count** | **int** |  | [optional] 
**proof_with_price_count** | **int** |  | [optional] 
**user_count** | **int** |  | [optional] 
**user_with_price_count** | **int** |  | [optional] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.total_stats import TotalStats

# TODO update the JSON string below
json = "{}"
# create an instance of TotalStats from a JSON string
total_stats_instance = TotalStats.from_json(json)
# print the JSON string representation of the object
print(TotalStats.to_json())

# convert the object into a dict
total_stats_dict = total_stats_instance.to_dict()
# create an instance of TotalStats from a dict
total_stats_from_dict = TotalStats.from_dict(total_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


