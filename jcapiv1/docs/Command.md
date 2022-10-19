# Command

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The command to execute on the server. | 
**command_runners** | **list[str]** | An array of IDs of the Command Runner Users that can execute this command. | [optional] 
**command_type** | **str** | The Command OS | [default to 'linux']
**files** | **list[str]** | An array of file IDs to include with the command. | [optional] 
**launch_type** | **str** | How the command will execute. | [optional] 
**listens_to** | **str** |  | [optional] 
**name** | **str** |  | 
**organization** | **str** | The ID of the organization. | [optional] 
**schedule** | **str** | A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately.  | [optional] 
**schedule_repeat_type** | **str** | When the command will repeat. | [optional] 
**schedule_year** | **int** | The year that a scheduled command will launch in. | [optional] 
**shell** | **str** | The shell used to run the command. | [optional] 
**sudo** | **bool** |  | [optional] 
**systems** | **list[str]** | An array of system IDs to run the command on. Not available if you are using Groups. | [optional] 
**template** | **str** | The template this command was created from | [optional] 
**time_to_live_seconds** | **int** | Time in seconds a command can wait in the queue to be run before timing out | [optional] 
**timeout** | **str** | The time in seconds to allow the command to run for. | [optional] 
**trigger** | **str** | The name of the command trigger. | [optional] 
**user** | **str** | The ID of the system user to run the command as. This field is required when creating a command with a commandType of \&quot;mac\&quot; or \&quot;linux\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

