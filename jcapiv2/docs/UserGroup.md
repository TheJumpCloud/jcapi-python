# UserGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**GroupAttributesUserGroup**](GroupAttributesUserGroup.md) |  | [optional] 
**description** | **str** | Description of a User Group | [optional] 
**email** | **str** | Email address of a User Group | [optional] 
**id** | **str** | ObjectId uniquely identifying a User Group. | [optional] 
**member_query** | [**FilterQuery**](FilterQuery.md) |  | [optional] 
**member_query_exemptions** | [**list[GraphObject]**](GraphObject.md) | Array of GraphObjects exempted from the query | [optional] 
**member_suggestions_notify** | **bool** | True if notification emails are to be sent for membership suggestions. | [optional] 
**membership_automated** | **bool** | True if membership of this group is automatically updated based on the Member Query and Member Query Exemptions, if configured | [optional] 
**name** | **str** | Display name of a User Group. | [optional] 
**suggestion_counts** | [**SuggestionCounts**](SuggestionCounts.md) |  | [optional] 
**type** | **str** | The type of the group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

