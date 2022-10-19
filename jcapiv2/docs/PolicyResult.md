# PolicyResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Details pertaining to the policy result. | [optional] 
**ended_at** | **datetime** | The end of the policy application. | [optional] 
**exit_status** | **int** | The 32-bit unsigned exit status from the applying the policy. | [optional] 
**id** | **str** | ObjectId uniquely identifying a Policy Result. | [optional] 
**policy_id** | **str** | ObjectId uniquely identifying the parent Policy. | [optional] 
**started_at** | **datetime** | The start of the policy application. | [optional] 
**state** | **str** | Enumeration describing the state of the policy. Success, failed, or pending. | [optional] 
**std_err** | **str** | The STDERR output from applying the policy. | [optional] 
**std_out** | **str** | The STDOUT output from applying the policy. | [optional] 
**success** | **bool** | True if the policy was successfully applied; false otherwise. | [optional] 
**system_id** | **str** | ObjectId uniquely identifying the parent System. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

