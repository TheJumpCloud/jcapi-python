# SoftwareAppSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_update_delay** | **bool** |  | [optional] [default to False]
**apple_vpp** | [**SoftwareAppAppleVpp**](SoftwareAppAppleVpp.md) |  | [optional] 
**asset_kind** | **str** | The manifest asset kind (ex: software). | [optional] 
**asset_sha256_size** | **int** | The incremental size to use for summing the package as it is downloaded. | [optional] 
**asset_sha256_strings** | **list[str]** | The array of checksums, one each for the hash size up to the total size of the package. | [optional] 
**auto_update** | **bool** |  | [optional] [default to False]
**description** | **str** | The software app description. | [optional] 
**desired_state** | **str** | State of Install or Uninstall | [optional] 
**location** | **str** | Repository where the app is located within the package manager | [optional] 
**location_object_id** | **str** | ID of the repository where the app is located within the package manager | [optional] 
**package_id** | **str** |  | [optional] 
**package_kind** | **str** | The package manifest kind (ex: software-package). | [optional] 
**package_manager** | **str** | App store serving the app: APPLE_VPP, CHOCOLATEY, etc. | [optional] 
**package_subtitle** | **str** | The package manifest subtitle. | [optional] 
**package_version** | **str** | The package manifest version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

