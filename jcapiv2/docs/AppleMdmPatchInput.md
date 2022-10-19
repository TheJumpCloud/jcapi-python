# AppleMdmPatchInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ades** | [**ADES**](ADES.md) |  | [optional] 
**allow_mobile_user_enrollment** | **bool** | A toggle to allow mobile device enrollment for an organization. | [optional] 
**apple_signed_cert** | **str** | A signed certificate obtained from Apple after providing Apple with the plist file provided on POST. | [optional] 
**default_ios_user_enrollment_device_group_id** | **str** | ObjectId uniquely identifying the MDM default iOS user enrollment device group. | [optional] 
**default_system_group_id** | **str** | ObjectId uniquely identifying the MDM default System Group. | [optional] 
**dep** | [**DEP**](DEP.md) |  | [optional] 
**encrypted_dep_server_token** | **str** | The S/MIME encoded DEP Server Token returned by Apple Business Manager when creating an MDM instance. | [optional] 
**name** | **str** | A new name for the Apple MDM configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

