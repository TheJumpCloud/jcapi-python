# PolicyTemplateWithDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ObjectId uniquely identifying a Policy Template. | [optional] 
**name** | **str** | The unique name for the Policy Template. | [optional] 
**description** | **str** | The default description for the Policy. | [optional] 
**display_name** | **str** | The default display name for the Policy. | [optional] 
**os_meta_family** | **str** |  | [optional] 
**config_fields** | [**list[PolicyTemplateConfigField]**](PolicyTemplateConfigField.md) | An unordered list of all the fields that can be configured for this Policy Template. | [optional] 
**activation** | **str** | Requirements before the policy can be activated. | [optional] 
**behavior** | **str** | Specifics about the behavior of the policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


