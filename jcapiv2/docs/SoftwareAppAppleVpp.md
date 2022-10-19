# SoftwareAppAppleVpp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_configuration** | **str** | Text sent to configure the application, the text should be a valid plist.  Returned only by &#x27;GET /softwareapps/{id}&#x27;. | [optional] 
**assigned_licenses** | **int** |  | [optional] 
**available_licenses** | **int** |  | [optional] 
**details** | **object** | App details returned by iTunes API. See example. The properties in this field are out of our control and we cannot guarantee consistency, so it should be checked by the client and manage the details accordingly. | [optional] 
**is_config_enabled** | **bool** | Denotes if configuration has been enabled for the application.  Returned only by &#x27;&#x27;GET /softwareapps/{id}&#x27;&#x27;. | [optional] 
**supported_device_families** | **list[str]** | The supported device families for this VPP Application. | [optional] 
**total_licenses** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

