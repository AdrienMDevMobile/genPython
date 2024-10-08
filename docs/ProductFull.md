# ProductFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**code** | **str** |  | 
**source** | [**ProductFullSource**](ProductFullSource.md) |  | [optional] 
**product_name** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**product_quantity** | **int** |  | [optional] 
**product_quantity_unit** | **str** |  | [optional] 
**categories_tags** | **List[str]** |  | [optional] 
**brands** | **str** |  | [optional] 
**brands_tags** | **List[str]** |  | [optional] 
**labels_tags** | **List[str]** |  | [optional] 
**nutriscore_grade** | **str** |  | [optional] 
**ecoscore_grade** | **str** |  | [optional] 
**nova_group** | **int** |  | [optional] 
**unique_scans_n** | **int** |  | [optional] 
**price_count** | **int** |  | [optional] 
**location_count** | **int** |  | [optional] 
**user_count** | **int** |  | [optional] 
**proof_count** | **int** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.product_full import ProductFull

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFull from a JSON string
product_full_instance = ProductFull.from_json(json)
# print the JSON string representation of the object
print(ProductFull.to_json())

# convert the object into a dict
product_full_dict = product_full_instance.to_dict()
# create an instance of ProductFull from a dict
product_full_from_dict = ProductFull.from_dict(product_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


