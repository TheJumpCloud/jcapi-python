# PolicyTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation** | **str** | Requirements before the policy can be activated. | [optional] 
**alert** | **str** | Text to describe any risk associated with this policy. | [optional] 
**behavior** | **str** | Specifics about the behavior of the policy. | [optional] 
**delivery_types** | **list[str]** | The supported delivery mechanisms for this policy template. | [optional] 
**description** | **str** | The default description for the Policy. | [optional] 
**display_name** | **str** | The default display name for the Policy. | [optional] 
**id** | **str** | ObjectId uniquely identifying a Policy Template. | [optional] 
**name** | **str** | The unique name for the Policy Template. | [optional] 
**os_meta_family** | **str** |  | [optional] 
**os_restrictions** | [**list[OSRestriction]**](OSRestriction.md) |  | [optional] 
**reference** | **str** | URL to visit for further information. | [optional] 
**state** | **str** | String describing the release status of the policy template. | [optional] [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

