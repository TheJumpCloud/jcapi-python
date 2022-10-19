# ApplicationtemplateOidc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_types** | **list[str]** | The grant types allowed. Currently only authorization_code is allowed. | [optional] 
**redirect_uris** | **list[str]** | List of allowed redirectUris | [optional] 
**sso_url** | **str** | The relying party url to trigger an oidc login. | [optional] 
**token_endpoint_auth_method** | **str** | Method that the client uses to authenticate when requesting a token. If &#x27;none&#x27;, then the client must use PKCE. If &#x27;client_secret_post&#x27;, then the secret is passed in the post body when requesting the token. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

