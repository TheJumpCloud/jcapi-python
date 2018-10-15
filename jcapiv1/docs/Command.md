# Command

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**command** | **str** | The command to execute on the server. | 
**command_type** | **str** | The Command OS | [optional] 
**command_runners** | **list[str]** | An array of IDs of the Command Runner Users that can execute this command. | [optional] 
**user** | **str** | The ID of the system user to run the command as. | 
**sudo** | **bool** |  | [optional] 
**systems** | **list[str]** | An array of system IDs to run the command on. Not available if you are using Groups. | [optional] 
**launch_type** | **str** | How the command will execute. | [optional] 
**listens_to** | **str** |  | [optional] 
**schedule_repeat_type** | **str** | When the command will repeat. | [optional] 
**schedule** | **str** | A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately.  | [optional] 
**files** | **list[str]** | An array of file IDs to include with the command. | [optional] 
**timeout** | **str** | The time in seconds to allow the command to run for. | [optional] 
**organization** | **str** | The ID of the organization. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


