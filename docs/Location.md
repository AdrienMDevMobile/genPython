# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**osm_id** | **int** |  | 
**osm_type** | [**LocationOsmTypeEnum**](LocationOsmTypeEnum.md) |  | 
**osm_name** | **str** |  | [optional] 
**osm_display_name** | **str** |  | [optional] 
**osm_tag_key** | **str** |  | [optional] 
**osm_tag_value** | **str** |  | [optional] 
**osm_address_postcode** | **str** |  | [optional] 
**osm_address_city** | **str** |  | [optional] 
**osm_address_country** | **str** |  | [optional] 
**osm_address_country_code** | **str** |  | [optional] 
**osm_lat** | **float** |  | [optional] 
**osm_lon** | **float** |  | [optional] 
**price_count** | **int** |  | [optional] 
**user_count** | **int** |  | [optional] 
**product_count** | **int** |  | [optional] 
**proof_count** | **int** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


