# Systemuser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**allow_public_key** | **bool** |  | [optional] 
**public_key** | **str** |  | [optional] 
**ssh_keys** | [**list[Sshkeylist]**](Sshkeylist.md) |  | [optional] 
**sudo** | **bool** |  | [optional] 
**enable_managed_uid** | **bool** |  | [optional] 
**unix_uid** | **int** |  | [optional] 
**unix_guid** | **int** |  | [optional] 
**activated** | **bool** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**password_expired** | **bool** |  | [optional] 
**account_locked** | **bool** |  | [optional] 
**passwordless_sudo** | **bool** |  | [optional] 
**externally_managed** | **bool** |  | [optional] 
**external_dn** | **str** |  | [optional] 
**external_source_type** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**ldap_binding_user** | **bool** |  | [optional] 
**enable_user_portal_multifactor** | **bool** |  | [optional] 
**associated_tag_count** | **int** |  | [optional] 
**totp_enabled** | **bool** |  | [optional] 
**password_expiration_date** | **str** |  | [optional] 
**attributes** | **list[object]** |  | [optional] 
**created** | **str** |  | [optional] 
**samba_service_user** | **bool** |  | [optional] 
**password_never_expires** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**middlename** | **str** |  | [optional] 
**displayname** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**cost_center** | **str** |  | [optional] 
**employee_type** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**employee_identifier** | **str** | Must be unique per user.  | [optional] 
**job_title** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**mfa** | [**Mfa**](Mfa.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


