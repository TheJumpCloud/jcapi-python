# Systemuserputpost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_locked** | **bool** |  | [optional] 
**activated** | **bool** |  | [optional] 
**addresses** | [**list[SystemuserputpostAddresses]**](SystemuserputpostAddresses.md) |  | [optional] 
**allow_public_key** | **bool** |  | [optional] 
**alternate_email** | **str** |  | [optional] 
**attributes** | [**list[SystemuserputAttributes]**](SystemuserputAttributes.md) |  | [optional] 
**company** | **str** |  | [optional] 
**cost_center** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disable_device_max_login_attempts** | **bool** |  | [optional] 
**displayname** | **str** |  | [optional] 
**email** | **str** |  | 
**employee_identifier** | **str** | Must be unique per user.  | [optional] 
**employee_type** | **str** |  | [optional] 
**enable_managed_uid** | **bool** |  | [optional] 
**enable_user_portal_multifactor** | **bool** |  | [optional] 
**external_dn** | **str** |  | [optional] 
**external_password_expiration_date** | **datetime** |  | [optional] 
**external_source_type** | **str** |  | [optional] 
**externally_managed** | **bool** |  | [optional] 
**firstname** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**ldap_binding_user** | **bool** |  | [optional] 
**location** | **str** |  | [optional] 
**managed_apple_id** | **str** |  | [optional] 
**manager** | **str** | Relation with another systemuser to identify the last as a manager. | [optional] 
**mfa** | [**Mfa**](Mfa.md) |  | [optional] 
**middlename** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**password_never_expires** | **bool** |  | [optional] 
**passwordless_sudo** | **bool** |  | [optional] 
**phone_numbers** | [**list[SystemuserputpostPhoneNumbers]**](SystemuserputpostPhoneNumbers.md) |  | [optional] 
**public_key** | **str** |  | [optional] 
**recovery_email** | [**SystemuserputpostRecoveryEmail**](SystemuserputpostRecoveryEmail.md) |  | [optional] 
**relationships** | [**list[SystemuserputRelationships]**](SystemuserputRelationships.md) |  | [optional] 
**samba_service_user** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**sudo** | **bool** |  | [optional] 
**suspended** | **bool** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**unix_guid** | **int** |  | [optional] 
**unix_uid** | **int** |  | [optional] 
**username** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

