# Commandresult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The command that was executed on the system. | [optional] 
**name** | **str** | The name of the command. | [optional] 
**system** | **str** | The id of the system the command was executed on. | [optional] 
**organization** | **str** | The id of the organization. | [optional] 
**workflow_id** | **str** |  | [optional] 
**workflow_instance_id** | **str** |  | [optional] 
**user** | **str** | The user the command ran as. | [optional] 
**sudo** | **bool** | If the user had sudo rights | [optional] 
**files** | **list[str]** | An array of file ids that were included in the command | [optional] 
**request_time** | **int** | The time that the command was sent. | [optional] 
**response_time** | **int** | The time that the command was completed. | [optional] 
**response** | [**CommandresultResponse**](CommandresultResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


