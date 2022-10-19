# Commandresult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the command. | [optional] 
**command** | **str** | The command that was executed on the system. | [optional] 
**files** | **list[str]** | An array of file ids that were included in the command | [optional] 
**name** | **str** | The name of the command. | [optional] 
**organization** | **str** | The ID of the organization. | [optional] 
**request_time** | **datetime** | The time that the command was sent. | [optional] 
**response** | [**CommandresultResponse**](CommandresultResponse.md) |  | [optional] 
**response_time** | **datetime** | The time that the command was completed. | [optional] 
**sudo** | **bool** | If the user had sudo rights | [optional] 
**system** | **str** | The name of the system the command was executed on. | [optional] 
**system_id** | **str** | The id of the system the command was executed on. | [optional] 
**user** | **str** | The user the command ran as. | [optional] 
**workflow_id** | **str** |  | [optional] 
**workflow_instance_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

