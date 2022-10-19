# BulkScheduledStatechangeCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_email_override** | **str** | Send the activation or welcome email to the specified email address upon activation. Can only be used with a single user_id and scheduled activation. This field will be ignored if &#x60;send_activation_emails&#x60; is explicitly set to false. | [optional] 
**send_activation_emails** | **bool** | Set to true to send activation or welcome email(s) to each user_id upon activation. Set to false to suppress emails. Can only be used with scheduled activation(s). | [optional] 
**start_date** | **datetime** | Date and time that scheduled action should occur | 
**state** | **str** | The state to move the user(s) to | 
**user_ids** | **list[str]** | Array of system user ids to schedule for a state change | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

