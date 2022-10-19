# AppleMDM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ades** | [**ADES**](ADES.md) |  | [optional] 
**allow_mobile_user_enrollment** | **bool** | A toggle to allow mobile device enrollment for an organization. | [optional] 
**apns_cert_expiry** | **str** | The expiration date and time for the APNS Certificate. | [optional] 
**apns_push_topic** | **str** | The push topic assigned to this enrollment by Apple after uploading the Signed CSR plist. | [optional] 
**default_ios_user_enrollment_device_group_id** | **str** | ObjectId uniquely identifying the MDM default iOS user enrollment device group. | [optional] 
**default_system_group_id** | **str** | ObjectId uniquely identifying the MDM default System Group. | [optional] 
**dep** | [**DEP**](DEP.md) |  | [optional] 
**dep_access_token_expiry** | **str** | The expiration date and time for the DEP Access Token. This aligns with the DEP Server Token State. | [optional] 
**dep_server_token_state** | **str** | The state of the dep server token, presence and expiry. | [optional] 
**id** | **str** | ObjectId uniquely identifying an MDM Enrollment, | 
**name** | **str** | A friendly name to identify this enrollment.  Not required to be unique. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

