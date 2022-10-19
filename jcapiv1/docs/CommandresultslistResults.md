# CommandresultslistResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the command result. | [optional] 
**command** | **str** | The command that was executed on the system. | [optional] 
**exit_code** | **int** | The stderr output from the command that ran. | [optional] 
**name** | **str** | The name of the command. | [optional] 
**request_time** | **datetime** | The time (UTC) that the command was sent. | [optional] 
**response_time** | **datetime** | The time (UTC) that the command was completed. | [optional] 
**sudo** | **bool** | If the user had sudo rights. | [optional] 
**system** | **str** | The display name of the system the command was executed on. | [optional] 
**system_id** | **str** | The id of the system the command was executed on. | [optional] 
**user** | **str** | The user the command ran as. | [optional] 
**workflow_id** | **str** | The id for the command that ran on the system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

