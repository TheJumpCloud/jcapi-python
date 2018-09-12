# Systemuserput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**username** | **str** |  | 
**allow_public_key** | **bool** |  | [optional] 
**public_key** | **str** |  | [optional] 
**ssh_keys** | [**list[Sshkeypost]**](Sshkeypost.md) |  | [optional] 
**sudo** | **bool** |  | [optional] 
**enable_managed_uid** | **bool** |  | [optional] 
**unix_uid** | **int** |  | [optional] 
**unix_guid** | **int** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**account_locked** | **bool** |  | [optional] 
**externally_managed** | **bool** |  | [optional] 
**external_dn** | **str** |  | [optional] 
**external_source_type** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**lastname** | **str** |  | [optional] 
**ldap_binding_user** | **bool** |  | [optional] 
**enable_user_portal_multifactor** | **bool** |  | [optional] 
**attributes** | **list[object]** |  | [optional] 
**samba_service_user** | **bool** |  | [optional] 
**addresses** | [**list[SystemuserputpostAddresses]**](SystemuserputpostAddresses.md) | type, poBox, extendedAddress, streetAddress, locality, region, postalCode, country | [optional] 
**job_title** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**phone_numbers** | [**list[SystemuserputpostPhoneNumbers]**](SystemuserputpostPhoneNumbers.md) |  | [optional] 
**relationships** | **list[object]** |  | [optional] 
**password** | **str** |  | [optional] 
**password_never_expires** | **bool** |  | [optional] 
**middlename** | **str** |  | [optional] 
**displayname** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**cost_center** | **str** |  | [optional] 
**employee_type** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**employee_identifier** | **str** | Must be unique per user.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


