# Commandresults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The command that was executed on the system. | [optional] 
**system** | **str** | The ID of the system on which the command was executed. | [optional] 
**organization** | **str** | The ID of the organization. | [optional] 
**user** | **str** | The user which ran the command. | [optional] 
**files** | **list[str]** | An array of file IDs that were included with the command. | [optional] 
**request_time** | **date** | The time that the command was sent. | [optional] 
**response_time** | **date** | The time that the command was completed. | [optional] 
**response_id** | **str** | The ID of the parent command. | [optional] 
**response_data_output** | **int** | the stdout from the command that ran. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


