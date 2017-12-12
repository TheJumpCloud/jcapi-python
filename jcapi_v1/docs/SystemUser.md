# SystemUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ObjectId for the systemuser. | [optional] 
**email** | **str** | The email address of the new System User. | 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**username** | **str** |  | 
**password** | **str** |  | [optional] 
**allow_public_key** | **bool** | Allow the system user to authenticate with a public key. | [optional] 
**passwordless_sudo** | **bool** | Allow the system user to execute as root without a password. | [optional] 
**sudo** | **bool** | Give the system user sudo access. | [optional] 
**public_key** | **str** | The SSH public key for the system user. | [optional] 
**unix_uid** | **int** | The Unix user ID for the system user. | [optional] 
**unix_guid** | **int** | The Unix group ID for the system user. | [optional] 
**tags** | **list[str]** | An array of tag IDs or names to which the system user belongs.  | [optional] 
**attributes** | [**list[SystemUserAttributes]**](SystemUserAttributes.md) | An array of attributes associated with the system user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


