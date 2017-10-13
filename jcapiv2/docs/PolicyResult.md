# PolicyResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | ObjectId uniquely identifying the parent Policy. | [optional] 
**system_id** | **str** | ObjectId uniquely identifying the parent System. | [optional] 
**id** | **str** | ObjectId uniquely identifying a Policy Result. | [optional] 
**started_at** | **datetime** | The start of the policy application. | [optional] 
**ended_at** | **datetime** | The end of the policy application. | [optional] 
**success** | **bool** | True if the policy was successfully applied; false otherwise. | [optional] 
**exit_status** | **int** | The 32-bit unsigned exit status from the applying the policy. | [optional] 
**std_err** | **str** | The STDERR output from applying the policy. | [optional] 
**std_out** | **str** | The STDOUT output from applying the policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


