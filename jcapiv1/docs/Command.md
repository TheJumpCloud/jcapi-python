# Command

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**command** | **str** | The command to execute on the server. | 
**user** | **str** | The ID of the JC managed user to run the command as. | 
**systems** | **list[str]** | An array of system IDs to run the command on. | [optional] 
**schedule** | **str** | A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately.  | [optional] 
**files** | **list[str]** | An array of file IDs to include with the command. | [optional] 
**tags** | **list[str]** | An array of tag IDs to run the command on. | [optional] 
**timeout** | **str** | The time in seconds to allow the command to run for. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


