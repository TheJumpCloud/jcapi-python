# jcapiv2
# Overview  JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # Directory Objects  This API offers the ability to interact with some of our core features; otherwise known as Directory Objects. The Directory Objects are:  * Commands * Policies * Policy Groups * Applications * Systems * Users * User Groups * System Groups * Radius Servers * Directories: Office 365, LDAP,G-Suite, Active Directory * Duo accounts and applications.  The Directory Object is an important concept to understand in order to successfully use JumpCloud API.  ## JumpCloud Graph  We've also introduced the concept of the JumpCloud Graph along with  Directory Objects. The Graph is a powerful aspect of our platform which will enable you to associate objects with each other, or establish membership for certain objects to become members of other objects.  Specific `GET` endpoints will allow you to traverse the JumpCloud Graph to return all indirect and directly bound objects in your organization.  | ![alt text](https://s3.amazonaws.com/jumpcloud-kb/Knowledge+Base+Photos/API+Docs/jumpcloud_graph.png \"JumpCloud Graph Model Example\") | |:--:| | **This diagram highlights our association and membership model as it relates to Directory Objects.** |  # API Key  ## Access Your API Key  To locate your API Key:  1. Log into the [JumpCloud Admin Console](https://console.jumpcloud.com/). 2. Go to the username drop down located in the top-right of the Console. 3. Retrieve your API key from API Settings.  ## API Key Considerations  This API key is associated to the currently logged in administrator. Other admins will have different API keys.  **WARNING** Please keep this API key secret, as it grants full access to any data accessible via your JumpCloud console account.  You can also reset your API key in the same location in the JumpCloud Admin Console.  ## Recycling or Resetting Your API Key  In order to revoke access with the current API key, simply reset your API key. This will render all calls using the previous API key inaccessible.  Your API key will be passed in as a header with the header name \"x-api-key\".  ```bash curl -H \"x-api-key: [YOUR_API_KEY_HERE]\" \"https://console.jumpcloud.com/api/v2/systemgroups\" ```  # System Context  * [Introduction](#introduction) * [Supported endpoints](#supported-endpoints) * [Response codes](#response-codes) * [Authentication](#authentication) * [Additional examples](#additional-examples) * [Third party](#third-party)  ## Introduction  JumpCloud System Context Authorization is an alternative way to authenticate with a subset of JumpCloud's REST APIs. Using this method, a system can manage its information and resource associations, allowing modern auto provisioning environments to scale as needed.  **Notes:**   * The following documentation applies to Linux Operating Systems only.  * Systems that have been automatically enrolled using Apple's Device Enrollment Program (DEP) or systems enrolled using the User Portal install are not eligible to use the System Context API to prevent unauthorized access to system groups and resources. If a script that utilizes the System Context API is invoked on a system enrolled in this way, it will display an error.  ## Supported Endpoints  JumpCloud System Context Authorization can be used in conjunction with Systems endpoints found in the V1 API and certain System Group endpoints found in the v2 API.  * A system may fetch, alter, and delete metadata about itself, including manipulating a system's Group and Systemuser associations,   * `/api/systems/{system_id}` | [`GET`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_get) [`PUT`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_put) * A system may delete itself from your JumpCloud organization   * `/api/systems/{system_id}` | [`DELETE`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_delete) * A system may fetch its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/memberof` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembership)   * `/api/v2/systems/{system_id}/associations` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsList)   * `/api/v2/systems/{system_id}/users` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemTraverseUser) * A system may alter its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/associations` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsPost) * A system may alter its System Group associations   * `/api/v2/systemgroups/{group_id}/members` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembersPost)     * _NOTE_ If a system attempts to alter the system group membership of a different system the request will be rejected  ## Response Codes  If endpoints other than those described above are called using the System Context API, the server will return a `401` response.  ## Authentication  To allow for secure access to our APIs, you must authenticate each API request. JumpCloud System Context Authorization uses [HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures-00) to authenticate API requests. The HTTP Signatures sent with each request are similar to the signatures used by the Amazon Web Services REST API. To help with the request-signing process, we have provided an [example bash script](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh). This example API request simply requests the entire system record. You must be root, or have permissions to access the contents of the `/opt/jc` directory to generate a signature.  Here is a breakdown of the example script with explanations.  First, the script extracts the systemKey from the JSON formatted `/opt/jc/jcagent.conf` file.  ```bash #!/bin/bash conf=\"`cat /opt/jc/jcagent.conf`\" regex=\"systemKey\\\":\\\"(\\w+)\\\"\"  if [[ $conf =~ $regex ]] ; then   systemKey=\"${BASH_REMATCH[1]}\" fi ```  Then, the script retrieves the current date in the correct format.  ```bash now=`date -u \"+%a, %d %h %Y %H:%M:%S GMT\"`; ```  Next, we build a signing string to demonstrate the expected signature format. The signed string must consist of the [request-line](https://tools.ietf.org/html/rfc2616#page-35) and the date header, separated by a newline character.  ```bash signstr=\"GET /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" ```  The next step is to calculate and apply the signature. This is a two-step process:  1. Create a signature from the signing string using the JumpCloud Agent private key: ``printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key`` 2. Then Base64-encode the signature string and trim off the newline characters: ``| openssl enc -e -a | tr -d '\\n'``  The combined steps above result in:  ```bash signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ; ```  Finally, we make sure the API call sending the signature has the same Authorization and Date header values, HTTP method, and URL that were used in the signing string.  ```bash curl -iq \\   -H \"Accept: application/json\" \\   -H \"Content-Type: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Input Data  All PUT and POST methods should use the HTTP Content-Type header with a value of 'application/json'. PUT methods are used for updating a record. POST methods are used to create a record.  The following example demonstrates how to update the `displayName` of the system.  ```bash signstr=\"PUT /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ;  curl -iq \\   -d \"{\\\"displayName\\\" : \\\"updated-system-name-1\\\"}\" \\   -X \"PUT\" \\   -H \"Content-Type: application/json\" \\   -H \"Accept: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Output Data  All results will be formatted as JSON.  Here is an abbreviated example of response output:  ```json {   \"_id\": \"525ee96f52e144993e000015\",   \"agentServer\": \"lappy386\",   \"agentVersion\": \"0.9.42\",   \"arch\": \"x86_64\",   \"connectionKey\": \"127.0.0.1_51812\",   \"displayName\": \"ubuntu-1204\",   \"firstContact\": \"2013-10-16T19:30:55.611Z\",   \"hostname\": \"ubuntu-1204\"   ... ```  ## Additional Examples  ### Signing Authentication Example  This example demonstrates how to make an authenticated request to fetch the JumpCloud record for this system.  [SigningExample.sh](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh)  ### Shutdown Hook  This example demonstrates how to make an authenticated request on system shutdown. Using an init.d script registered at run level 0, you can call the System Context API as the system is shutting down.  [Instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) is an example of an init.d script that only runs at system shutdown.  After customizing the [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) script, you should install it on the system(s) running the JumpCloud agent.  1. Copy the modified [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) to `/etc/init.d/instance-shutdown`. 2. On Ubuntu systems, run `update-rc.d instance-shutdown defaults`. On RedHat/CentOS systems, run `chkconfig --add instance-shutdown`.  ## Third Party  ### Chef Cookbooks  [https://github.com/nshenry03/jumpcloud](https://github.com/nshenry03/jumpcloud)  [https://github.com/cjs226/jumpcloud](https://github.com/cjs226/jumpcloud)  # Multi-Tenant Portal Headers  Multi-Tenant Organization API Headers are available for JumpCloud Admins to use when making API requests from Organizations that have multiple managed organizations.  The `x-org-id` is a required header for all multi-tenant admins when making API requests to JumpCloud. This header will define to which organization you would like to make the request.  **NOTE** Single Tenant Admins do not need to provide this header when making an API request.  ## Header Value  `x-org-id`  ## API Response Codes  * `400` Malformed ID. * `400` x-org-id and Organization path ID do not match. * `401` ID not included for multi-tenant admin * `403` ID included on unsupported route. * `404` Organization ID Not Found.  ```bash curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -H 'x-org-id: {ORG_ID}'  ```  ## To Obtain an Individual Organization ID via the UI  As a prerequisite, your Primary Organization will need to be setup for Multi-Tenancy. This provides access to the Multi-Tenant Organization Admin Portal.  1. Log into JumpCloud [Admin Console](https://console.jumpcloud.com). If you are a multi-tenant Admin, you will automatically be routed to the Multi-Tenant Admin Portal. 2. From the Multi-Tenant Portal's primary navigation bar, select the Organization you'd like to access. 3. You will automatically be routed to that Organization's Admin Console. 4. Go to Settings in the sub-tenant's primary navigation. 5. You can obtain your Organization ID below your Organization's Contact Information on the Settings page.  ## To Obtain All Organization IDs via the API  * You can make an API request to this endpoint using the API key of your Primary Organization.  `https://console.jumpcloud.com/api/organizations/` This will return all your managed organizations.  ```bash curl -X GET \\   https://console.jumpcloud.com/api/organizations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # SDKs  You can find language specific SDKs that can help you kickstart your Integration with JumpCloud in the following GitHub repositories:  * [Python](https://github.com/TheJumpCloud/jcapi-python) * [Go](https://github.com/TheJumpCloud/jcapi-go) * [Ruby](https://github.com/TheJumpCloud/jcapi-ruby) * [Java](https://github.com/TheJumpCloud/jcapi-java) 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 5.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://support.jumpcloud.com/support/s/](https://support.jumpcloud.com/support/s/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import jcapiv2 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import jcapiv2
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import jcapiv2
from jcapiv2.rest import ApiException
from pprint import pprint

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | 
agent_id = 'agent_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete Active Directory Agent
    api_instance.activedirectories_agents_delete(activedirectory_id, agent_id, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_agents_delete: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | 
agent_id = 'agent_id_example' # str | 
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get Active Directory Agent
    api_response = api_instance.activedirectories_agents_get(activedirectory_id, agent_id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_agents_get: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | 
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Active Directory Agents
    api_response = api_instance.activedirectories_agents_list(activedirectory_id, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_agents_list: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | 
body = jcapiv2.ActiveDirectoryAgentInput() # ActiveDirectoryAgentInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create a new Active Directory Agent
    api_response = api_instance.activedirectories_agents_post(activedirectory_id, body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_agents_post: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | ObjectID of this Active Directory instance.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Delete an Active Directory
    api_response = api_instance.activedirectories_delete(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_delete: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
id = 'id_example' # str | ObjectID of this Active Directory instance.
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Get an Active Directory
    api_response = api_instance.activedirectories_get(id, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_get: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
fields = ['fields_example'] # list[str] | The comma separated fields included in the returned records. If omitted, the default list of fields will be returned.  (optional)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
sort = ['sort_example'] # list[str] | The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending.  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List Active Directories
    api_response = api_instance.activedirectories_list(fields=fields, filter=filter, limit=limit, skip=skip, sort=sort, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_list: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
body = jcapiv2.ActiveDirectoryInput() # ActiveDirectoryInput |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Create a new Active Directory
    api_response = api_instance.activedirectories_post(body=body, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->activedirectories_post: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | 
targets = ['targets_example'] # list[str] | Targets which a \"active_directory\" can be associated to.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # List the associations of an Active Directory instance
    api_response = api_instance.graph_active_directory_associations_list(activedirectory_id, targets, limit=limit, skip=skip, x_org_id=x_org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->graph_active_directory_associations_list: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | 
body = jcapiv2.GraphOperationActiveDirectory() # GraphOperationActiveDirectory |  (optional)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)

try:
    # Manage the associations of an Active Directory instance
    api_instance.graph_active_directory_associations_post(activedirectory_id, body=body, x_org_id=x_org_id)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->graph_active_directory_associations_post: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | ObjectID of the Active Directory instance.
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)

try:
    # List the Users bound to an Active Directory instance
    api_response = api_instance.graph_active_directory_traverse_user(activedirectory_id, filter=filter, limit=limit, x_org_id=x_org_id, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->graph_active_directory_traverse_user: %s\n" % e)

# Configure API key authorization: x-api-key
configuration = jcapiv2.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = jcapiv2.ActiveDirectoryApi(jcapiv2.ApiClient(configuration))
activedirectory_id = 'activedirectory_id_example' # str | ObjectID of the Active Directory instance.
limit = 10 # int | The number of records to return at once. Limited to 100. (optional) (default to 10)
x_org_id = 'x_org_id_example' # str | Organization identifier that can be obtained from console settings. (optional)
skip = 0 # int | The offset into the records to return. (optional) (default to 0)
filter = ['filter_example'] # list[str] | A filter to apply to the query.  **Filter structure**: `<field>:<operator>:<value>`.  **field** = Populate with a valid field from an endpoint response.  **operator** =  Supported operators are: eq, ne, gt, ge, lt, le, between, search, in. _Note: v1 operators differ from v2 operators._  **value** = Populate with the value you want to search for. Is case sensitive. Supports wild cards.  **EX:** `GET /api/v2/groups?filter=name:eq:Test+Group` (optional)

try:
    # List the User Groups bound to an Active Directory instance
    api_response = api_instance.graph_active_directory_traverse_user_group(activedirectory_id, limit=limit, x_org_id=x_org_id, skip=skip, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActiveDirectoryApi->graph_active_directory_traverse_user_group: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://console.jumpcloud.com/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActiveDirectoryApi* | [**activedirectories_agents_delete**](docs/ActiveDirectoryApi.md#activedirectories_agents_delete) | **DELETE** /activedirectories/{activedirectory_id}/agents/{agent_id} | Delete Active Directory Agent
*ActiveDirectoryApi* | [**activedirectories_agents_get**](docs/ActiveDirectoryApi.md#activedirectories_agents_get) | **GET** /activedirectories/{activedirectory_id}/agents/{agent_id} | Get Active Directory Agent
*ActiveDirectoryApi* | [**activedirectories_agents_list**](docs/ActiveDirectoryApi.md#activedirectories_agents_list) | **GET** /activedirectories/{activedirectory_id}/agents | List Active Directory Agents
*ActiveDirectoryApi* | [**activedirectories_agents_post**](docs/ActiveDirectoryApi.md#activedirectories_agents_post) | **POST** /activedirectories/{activedirectory_id}/agents | Create a new Active Directory Agent
*ActiveDirectoryApi* | [**activedirectories_delete**](docs/ActiveDirectoryApi.md#activedirectories_delete) | **DELETE** /activedirectories/{id} | Delete an Active Directory
*ActiveDirectoryApi* | [**activedirectories_get**](docs/ActiveDirectoryApi.md#activedirectories_get) | **GET** /activedirectories/{id} | Get an Active Directory
*ActiveDirectoryApi* | [**activedirectories_list**](docs/ActiveDirectoryApi.md#activedirectories_list) | **GET** /activedirectories | List Active Directories
*ActiveDirectoryApi* | [**activedirectories_post**](docs/ActiveDirectoryApi.md#activedirectories_post) | **POST** /activedirectories | Create a new Active Directory
*ActiveDirectoryApi* | [**graph_active_directory_associations_list**](docs/ActiveDirectoryApi.md#graph_active_directory_associations_list) | **GET** /activedirectories/{activedirectory_id}/associations | List the associations of an Active Directory instance
*ActiveDirectoryApi* | [**graph_active_directory_associations_post**](docs/ActiveDirectoryApi.md#graph_active_directory_associations_post) | **POST** /activedirectories/{activedirectory_id}/associations | Manage the associations of an Active Directory instance
*ActiveDirectoryApi* | [**graph_active_directory_traverse_user**](docs/ActiveDirectoryApi.md#graph_active_directory_traverse_user) | **GET** /activedirectories/{activedirectory_id}/users | List the Users bound to an Active Directory instance
*ActiveDirectoryApi* | [**graph_active_directory_traverse_user_group**](docs/ActiveDirectoryApi.md#graph_active_directory_traverse_user_group) | **GET** /activedirectories/{activedirectory_id}/usergroups | List the User Groups bound to an Active Directory instance
*AdministratorsApi* | [**administrator_organizations_create_by_administrator**](docs/AdministratorsApi.md#administrator_organizations_create_by_administrator) | **POST** /administrators/{id}/organizationlinks | Allow Adminstrator access to an Organization.
*AdministratorsApi* | [**administrator_organizations_list_by_administrator**](docs/AdministratorsApi.md#administrator_organizations_list_by_administrator) | **GET** /administrators/{id}/organizationlinks | List the association links between an Administrator and Organizations.
*AdministratorsApi* | [**administrator_organizations_list_by_organization**](docs/AdministratorsApi.md#administrator_organizations_list_by_organization) | **GET** /organizations/{id}/administratorlinks | List the association links between an Organization and Administrators.
*AdministratorsApi* | [**administrator_organizations_remove_by_administrator**](docs/AdministratorsApi.md#administrator_organizations_remove_by_administrator) | **DELETE** /administrators/{administrator_id}/organizationlinks/{id} | Remove association between an Administrator and an Organization.
*AppleMDMApi* | [**applemdms_csrget**](docs/AppleMDMApi.md#applemdms_csrget) | **GET** /applemdms/{apple_mdm_id}/csr | Get Apple MDM CSR Plist
*AppleMDMApi* | [**applemdms_delete**](docs/AppleMDMApi.md#applemdms_delete) | **DELETE** /applemdms/{id} | Delete an Apple MDM
*AppleMDMApi* | [**applemdms_deletedevice**](docs/AppleMDMApi.md#applemdms_deletedevice) | **DELETE** /applemdms/{apple_mdm_id}/devices/{device_id} | Remove an Apple MDM Device&#x27;s Enrollment
*AppleMDMApi* | [**applemdms_depkeyget**](docs/AppleMDMApi.md#applemdms_depkeyget) | **GET** /applemdms/{apple_mdm_id}/depkey | Get Apple MDM DEP Public Key
*AppleMDMApi* | [**applemdms_devices_clear_activation_lock**](docs/AppleMDMApi.md#applemdms_devices_clear_activation_lock) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/clearActivationLock | Clears the Activation Lock for a Device
*AppleMDMApi* | [**applemdms_devices_refresh_activation_lock_information**](docs/AppleMDMApi.md#applemdms_devices_refresh_activation_lock_information) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/refreshActivationLockInformation | Refresh activation lock information for a device
*AppleMDMApi* | [**applemdms_deviceserase**](docs/AppleMDMApi.md#applemdms_deviceserase) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/erase | Erase Device
*AppleMDMApi* | [**applemdms_deviceslist**](docs/AppleMDMApi.md#applemdms_deviceslist) | **GET** /applemdms/{apple_mdm_id}/devices | List AppleMDM Devices
*AppleMDMApi* | [**applemdms_deviceslock**](docs/AppleMDMApi.md#applemdms_deviceslock) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/lock | Lock Device
*AppleMDMApi* | [**applemdms_devicesrestart**](docs/AppleMDMApi.md#applemdms_devicesrestart) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/restart | Restart Device
*AppleMDMApi* | [**applemdms_devicesshutdown**](docs/AppleMDMApi.md#applemdms_devicesshutdown) | **POST** /applemdms/{apple_mdm_id}/devices/{device_id}/shutdown | Shut Down Device
*AppleMDMApi* | [**applemdms_enrollmentprofilesget**](docs/AppleMDMApi.md#applemdms_enrollmentprofilesget) | **GET** /applemdms/{apple_mdm_id}/enrollmentprofiles/{id} | Get an Apple MDM Enrollment Profile
*AppleMDMApi* | [**applemdms_enrollmentprofileslist**](docs/AppleMDMApi.md#applemdms_enrollmentprofileslist) | **GET** /applemdms/{apple_mdm_id}/enrollmentprofiles | List Apple MDM Enrollment Profiles
*AppleMDMApi* | [**applemdms_getdevice**](docs/AppleMDMApi.md#applemdms_getdevice) | **GET** /applemdms/{apple_mdm_id}/devices/{device_id} | Details of an AppleMDM Device
*AppleMDMApi* | [**applemdms_list**](docs/AppleMDMApi.md#applemdms_list) | **GET** /applemdms | List Apple MDMs
*AppleMDMApi* | [**applemdms_put**](docs/AppleMDMApi.md#applemdms_put) | **PUT** /applemdms/{id} | Update an Apple MDM
*AppleMDMApi* | [**applemdms_refreshdepdevices**](docs/AppleMDMApi.md#applemdms_refreshdepdevices) | **POST** /applemdms/{apple_mdm_id}/refreshdepdevices | Refresh DEP Devices
*ApplicationsApi* | [**applications_delete_logo**](docs/ApplicationsApi.md#applications_delete_logo) | **DELETE** /applications/{application_id}/logo | Delete application image
*ApplicationsApi* | [**applications_get**](docs/ApplicationsApi.md#applications_get) | **GET** /applications/{application_id} | Get an Application
*ApplicationsApi* | [**applications_post_logo**](docs/ApplicationsApi.md#applications_post_logo) | **POST** /applications/{application_id}/logo | 
*ApplicationsApi* | [**graph_application_associations_list**](docs/ApplicationsApi.md#graph_application_associations_list) | **GET** /applications/{application_id}/associations | List the associations of an Application
*ApplicationsApi* | [**graph_application_associations_post**](docs/ApplicationsApi.md#graph_application_associations_post) | **POST** /applications/{application_id}/associations | Manage the associations of an Application
*ApplicationsApi* | [**graph_application_traverse_user**](docs/ApplicationsApi.md#graph_application_traverse_user) | **GET** /applications/{application_id}/users | List the Users bound to an Application
*ApplicationsApi* | [**graph_application_traverse_user_group**](docs/ApplicationsApi.md#graph_application_traverse_user_group) | **GET** /applications/{application_id}/usergroups | List the User Groups bound to an Application
*ApplicationsApi* | [**import_users**](docs/ApplicationsApi.md#import_users) | **GET** /applications/{application_id}/import/users | Get a list of users to import from an Application IdM service provider
*AuthenticationPoliciesApi* | [**authnpolicies_delete**](docs/AuthenticationPoliciesApi.md#authnpolicies_delete) | **DELETE** /authn/policies/{id} | Delete Authentication Policy
*AuthenticationPoliciesApi* | [**authnpolicies_get**](docs/AuthenticationPoliciesApi.md#authnpolicies_get) | **GET** /authn/policies/{id} | Get an authentication policy
*AuthenticationPoliciesApi* | [**authnpolicies_list**](docs/AuthenticationPoliciesApi.md#authnpolicies_list) | **GET** /authn/policies | List Authentication Policies
*AuthenticationPoliciesApi* | [**authnpolicies_patch**](docs/AuthenticationPoliciesApi.md#authnpolicies_patch) | **PATCH** /authn/policies/{id} | Patch Authentication Policy
*AuthenticationPoliciesApi* | [**authnpolicies_post**](docs/AuthenticationPoliciesApi.md#authnpolicies_post) | **POST** /authn/policies | Create an Authentication Policy
*BulkJobRequestsApi* | [**bulk_user_states_create**](docs/BulkJobRequestsApi.md#bulk_user_states_create) | **POST** /bulk/userstates | Create Scheduled Userstate Job
*BulkJobRequestsApi* | [**bulk_user_states_delete**](docs/BulkJobRequestsApi.md#bulk_user_states_delete) | **DELETE** /bulk/userstates/{id} | Delete Scheduled Userstate Job
*BulkJobRequestsApi* | [**bulk_user_states_get_next_scheduled**](docs/BulkJobRequestsApi.md#bulk_user_states_get_next_scheduled) | **GET** /bulk/userstates/eventlist/next | Gets the next scheduled state change for each user in a list of system users
*BulkJobRequestsApi* | [**bulk_user_states_list**](docs/BulkJobRequestsApi.md#bulk_user_states_list) | **GET** /bulk/userstates | List Scheduled Userstate Change Jobs
*BulkJobRequestsApi* | [**bulk_users_create**](docs/BulkJobRequestsApi.md#bulk_users_create) | **POST** /bulk/users | Bulk Users Create
*BulkJobRequestsApi* | [**bulk_users_create_results**](docs/BulkJobRequestsApi.md#bulk_users_create_results) | **GET** /bulk/users/{job_id}/results | List Bulk Users Results
*BulkJobRequestsApi* | [**bulk_users_update**](docs/BulkJobRequestsApi.md#bulk_users_update) | **PATCH** /bulk/users | Bulk Users Update
*CommandResultsApi* | [**commands_list_results_by_workflow**](docs/CommandResultsApi.md#commands_list_results_by_workflow) | **GET** /commandresult/workflows | List all Command Results by Workflow
*CommandsApi* | [**commands_cancel_queued_commands_by_workflow_instance_id**](docs/CommandsApi.md#commands_cancel_queued_commands_by_workflow_instance_id) | **DELETE** /commandqueue/{workflow_instance_id} | Cancel all queued commands for an organization by workflow instance Id
*CommandsApi* | [**commands_get_queued_commands_by_workflow**](docs/CommandsApi.md#commands_get_queued_commands_by_workflow) | **GET** /queuedcommand/workflows | Fetch the queued Commands for an Organization
*CommandsApi* | [**graph_command_associations_list**](docs/CommandsApi.md#graph_command_associations_list) | **GET** /commands/{command_id}/associations | List the associations of a Command
*CommandsApi* | [**graph_command_associations_post**](docs/CommandsApi.md#graph_command_associations_post) | **POST** /commands/{command_id}/associations | Manage the associations of a Command
*CommandsApi* | [**graph_command_traverse_system**](docs/CommandsApi.md#graph_command_traverse_system) | **GET** /commands/{command_id}/systems | List the Systems bound to a Command
*CommandsApi* | [**graph_command_traverse_system_group**](docs/CommandsApi.md#graph_command_traverse_system_group) | **GET** /commands/{command_id}/systemgroups | List the System Groups bound to a Command
*CustomEmailsApi* | [**custom_emails_create**](docs/CustomEmailsApi.md#custom_emails_create) | **POST** /customemails | Create custom email configuration
*CustomEmailsApi* | [**custom_emails_destroy**](docs/CustomEmailsApi.md#custom_emails_destroy) | **DELETE** /customemails/{custom_email_type} | Delete custom email configuration
*CustomEmailsApi* | [**custom_emails_get_templates**](docs/CustomEmailsApi.md#custom_emails_get_templates) | **GET** /customemail/templates | List custom email templates
*CustomEmailsApi* | [**custom_emails_read**](docs/CustomEmailsApi.md#custom_emails_read) | **GET** /customemails/{custom_email_type} | Get custom email configuration
*CustomEmailsApi* | [**custom_emails_update**](docs/CustomEmailsApi.md#custom_emails_update) | **PUT** /customemails/{custom_email_type} | Update custom email configuration
*DirectoriesApi* | [**directories_list**](docs/DirectoriesApi.md#directories_list) | **GET** /directories | List All Directories
*DuoApi* | [**duo_account_delete**](docs/DuoApi.md#duo_account_delete) | **DELETE** /duo/accounts/{id} | Delete a Duo Account
*DuoApi* | [**duo_account_get**](docs/DuoApi.md#duo_account_get) | **GET** /duo/accounts/{id} | Get a Duo Acount
*DuoApi* | [**duo_account_list**](docs/DuoApi.md#duo_account_list) | **GET** /duo/accounts | List Duo Accounts
*DuoApi* | [**duo_account_post**](docs/DuoApi.md#duo_account_post) | **POST** /duo/accounts | Create Duo Account
*DuoApi* | [**duo_application_delete**](docs/DuoApi.md#duo_application_delete) | **DELETE** /duo/accounts/{account_id}/applications/{application_id} | Delete a Duo Application
*DuoApi* | [**duo_application_get**](docs/DuoApi.md#duo_application_get) | **GET** /duo/accounts/{account_id}/applications/{application_id} | Get a Duo application
*DuoApi* | [**duo_application_list**](docs/DuoApi.md#duo_application_list) | **GET** /duo/accounts/{account_id}/applications | List Duo Applications
*DuoApi* | [**duo_application_post**](docs/DuoApi.md#duo_application_post) | **POST** /duo/accounts/{account_id}/applications | Create Duo Application
*DuoApi* | [**duo_application_update**](docs/DuoApi.md#duo_application_update) | **PUT** /duo/accounts/{account_id}/applications/{application_id} | Update Duo Application
*GSuiteApi* | [**graph_g_suite_associations_list**](docs/GSuiteApi.md#graph_g_suite_associations_list) | **GET** /gsuites/{gsuite_id}/associations | List the associations of a G Suite instance
*GSuiteApi* | [**graph_g_suite_associations_post**](docs/GSuiteApi.md#graph_g_suite_associations_post) | **POST** /gsuites/{gsuite_id}/associations | Manage the associations of a G Suite instance
*GSuiteApi* | [**graph_g_suite_traverse_user**](docs/GSuiteApi.md#graph_g_suite_traverse_user) | **GET** /gsuites/{gsuite_id}/users | List the Users bound to a G Suite instance
*GSuiteApi* | [**graph_g_suite_traverse_user_group**](docs/GSuiteApi.md#graph_g_suite_traverse_user_group) | **GET** /gsuites/{gsuite_id}/usergroups | List the User Groups bound to a G Suite instance
*GSuiteApi* | [**gsuites_get**](docs/GSuiteApi.md#gsuites_get) | **GET** /gsuites/{id} | Get G Suite
*GSuiteApi* | [**gsuites_list_import_jumpcloud_users**](docs/GSuiteApi.md#gsuites_list_import_jumpcloud_users) | **GET** /gsuites/{gsuite_id}/import/jumpcloudusers | Get a list of users in Jumpcloud format to import from a Google Workspace account.
*GSuiteApi* | [**gsuites_list_import_users**](docs/GSuiteApi.md#gsuites_list_import_users) | **GET** /gsuites/{gsuite_id}/import/users | Get a list of users to import from a G Suite instance
*GSuiteApi* | [**gsuites_patch**](docs/GSuiteApi.md#gsuites_patch) | **PATCH** /gsuites/{id} | Update existing G Suite
*GSuiteApi* | [**translation_rules_g_suite_delete**](docs/GSuiteApi.md#translation_rules_g_suite_delete) | **DELETE** /gsuites/{gsuite_id}/translationrules/{id} | Deletes a G Suite translation rule
*GSuiteApi* | [**translation_rules_g_suite_get**](docs/GSuiteApi.md#translation_rules_g_suite_get) | **GET** /gsuites/{gsuite_id}/translationrules/{id} | Gets a specific G Suite translation rule
*GSuiteApi* | [**translation_rules_g_suite_list**](docs/GSuiteApi.md#translation_rules_g_suite_list) | **GET** /gsuites/{gsuite_id}/translationrules | List all the G Suite Translation Rules
*GSuiteApi* | [**translation_rules_g_suite_post**](docs/GSuiteApi.md#translation_rules_g_suite_post) | **POST** /gsuites/{gsuite_id}/translationrules | Create a new G Suite Translation Rule
*GSuiteImportApi* | [**gsuites_list_import_jumpcloud_users**](docs/GSuiteImportApi.md#gsuites_list_import_jumpcloud_users) | **GET** /gsuites/{gsuite_id}/import/jumpcloudusers | Get a list of users in Jumpcloud format to import from a Google Workspace account.
*GSuiteImportApi* | [**gsuites_list_import_users**](docs/GSuiteImportApi.md#gsuites_list_import_users) | **GET** /gsuites/{gsuite_id}/import/users | Get a list of users to import from a G Suite instance
*GraphApi* | [**graph_active_directory_associations_list**](docs/GraphApi.md#graph_active_directory_associations_list) | **GET** /activedirectories/{activedirectory_id}/associations | List the associations of an Active Directory instance
*GraphApi* | [**graph_active_directory_associations_post**](docs/GraphApi.md#graph_active_directory_associations_post) | **POST** /activedirectories/{activedirectory_id}/associations | Manage the associations of an Active Directory instance
*GraphApi* | [**graph_active_directory_traverse_user**](docs/GraphApi.md#graph_active_directory_traverse_user) | **GET** /activedirectories/{activedirectory_id}/users | List the Users bound to an Active Directory instance
*GraphApi* | [**graph_active_directory_traverse_user_group**](docs/GraphApi.md#graph_active_directory_traverse_user_group) | **GET** /activedirectories/{activedirectory_id}/usergroups | List the User Groups bound to an Active Directory instance
*GraphApi* | [**graph_application_associations_list**](docs/GraphApi.md#graph_application_associations_list) | **GET** /applications/{application_id}/associations | List the associations of an Application
*GraphApi* | [**graph_application_associations_post**](docs/GraphApi.md#graph_application_associations_post) | **POST** /applications/{application_id}/associations | Manage the associations of an Application
*GraphApi* | [**graph_application_traverse_user**](docs/GraphApi.md#graph_application_traverse_user) | **GET** /applications/{application_id}/users | List the Users bound to an Application
*GraphApi* | [**graph_application_traverse_user_group**](docs/GraphApi.md#graph_application_traverse_user_group) | **GET** /applications/{application_id}/usergroups | List the User Groups bound to an Application
*GraphApi* | [**graph_command_associations_list**](docs/GraphApi.md#graph_command_associations_list) | **GET** /commands/{command_id}/associations | List the associations of a Command
*GraphApi* | [**graph_command_associations_post**](docs/GraphApi.md#graph_command_associations_post) | **POST** /commands/{command_id}/associations | Manage the associations of a Command
*GraphApi* | [**graph_command_traverse_system**](docs/GraphApi.md#graph_command_traverse_system) | **GET** /commands/{command_id}/systems | List the Systems bound to a Command
*GraphApi* | [**graph_command_traverse_system_group**](docs/GraphApi.md#graph_command_traverse_system_group) | **GET** /commands/{command_id}/systemgroups | List the System Groups bound to a Command
*GraphApi* | [**graph_g_suite_associations_list**](docs/GraphApi.md#graph_g_suite_associations_list) | **GET** /gsuites/{gsuite_id}/associations | List the associations of a G Suite instance
*GraphApi* | [**graph_g_suite_associations_post**](docs/GraphApi.md#graph_g_suite_associations_post) | **POST** /gsuites/{gsuite_id}/associations | Manage the associations of a G Suite instance
*GraphApi* | [**graph_g_suite_traverse_user**](docs/GraphApi.md#graph_g_suite_traverse_user) | **GET** /gsuites/{gsuite_id}/users | List the Users bound to a G Suite instance
*GraphApi* | [**graph_g_suite_traverse_user_group**](docs/GraphApi.md#graph_g_suite_traverse_user_group) | **GET** /gsuites/{gsuite_id}/usergroups | List the User Groups bound to a G Suite instance
*GraphApi* | [**graph_ldap_server_associations_list**](docs/GraphApi.md#graph_ldap_server_associations_list) | **GET** /ldapservers/{ldapserver_id}/associations | List the associations of a LDAP Server
*GraphApi* | [**graph_ldap_server_associations_post**](docs/GraphApi.md#graph_ldap_server_associations_post) | **POST** /ldapservers/{ldapserver_id}/associations | Manage the associations of a LDAP Server
*GraphApi* | [**graph_ldap_server_traverse_user**](docs/GraphApi.md#graph_ldap_server_traverse_user) | **GET** /ldapservers/{ldapserver_id}/users | List the Users bound to a LDAP Server
*GraphApi* | [**graph_ldap_server_traverse_user_group**](docs/GraphApi.md#graph_ldap_server_traverse_user_group) | **GET** /ldapservers/{ldapserver_id}/usergroups | List the User Groups bound to a LDAP Server
*GraphApi* | [**graph_office365_associations_list**](docs/GraphApi.md#graph_office365_associations_list) | **GET** /office365s/{office365_id}/associations | List the associations of an Office 365 instance
*GraphApi* | [**graph_office365_associations_post**](docs/GraphApi.md#graph_office365_associations_post) | **POST** /office365s/{office365_id}/associations | Manage the associations of an Office 365 instance
*GraphApi* | [**graph_office365_traverse_user**](docs/GraphApi.md#graph_office365_traverse_user) | **GET** /office365s/{office365_id}/users | List the Users bound to an Office 365 instance
*GraphApi* | [**graph_office365_traverse_user_group**](docs/GraphApi.md#graph_office365_traverse_user_group) | **GET** /office365s/{office365_id}/usergroups | List the User Groups bound to an Office 365 instance
*GraphApi* | [**graph_policy_associations_list**](docs/GraphApi.md#graph_policy_associations_list) | **GET** /policies/{policy_id}/associations | List the associations of a Policy
*GraphApi* | [**graph_policy_associations_post**](docs/GraphApi.md#graph_policy_associations_post) | **POST** /policies/{policy_id}/associations | Manage the associations of a Policy
*GraphApi* | [**graph_policy_group_associations_list**](docs/GraphApi.md#graph_policy_group_associations_list) | **GET** /policygroups/{group_id}/associations | List the associations of a Policy Group.
*GraphApi* | [**graph_policy_group_associations_post**](docs/GraphApi.md#graph_policy_group_associations_post) | **POST** /policygroups/{group_id}/associations | Manage the associations of a Policy Group
*GraphApi* | [**graph_policy_group_members_list**](docs/GraphApi.md#graph_policy_group_members_list) | **GET** /policygroups/{group_id}/members | List the members of a Policy Group
*GraphApi* | [**graph_policy_group_members_post**](docs/GraphApi.md#graph_policy_group_members_post) | **POST** /policygroups/{group_id}/members | Manage the members of a Policy Group
*GraphApi* | [**graph_policy_group_membership**](docs/GraphApi.md#graph_policy_group_membership) | **GET** /policygroups/{group_id}/membership | List the Policy Group&#x27;s membership
*GraphApi* | [**graph_policy_group_traverse_system**](docs/GraphApi.md#graph_policy_group_traverse_system) | **GET** /policygroups/{group_id}/systems | List the Systems bound to a Policy Group
*GraphApi* | [**graph_policy_group_traverse_system_group**](docs/GraphApi.md#graph_policy_group_traverse_system_group) | **GET** /policygroups/{group_id}/systemgroups | List the System Groups bound to Policy Groups
*GraphApi* | [**graph_policy_member_of**](docs/GraphApi.md#graph_policy_member_of) | **GET** /policies/{policy_id}/memberof | List the parent Groups of a Policy
*GraphApi* | [**graph_policy_traverse_system**](docs/GraphApi.md#graph_policy_traverse_system) | **GET** /policies/{policy_id}/systems | List the Systems bound to a Policy
*GraphApi* | [**graph_policy_traverse_system_group**](docs/GraphApi.md#graph_policy_traverse_system_group) | **GET** /policies/{policy_id}/systemgroups | List the System Groups bound to a Policy
*GraphApi* | [**graph_radius_server_associations_list**](docs/GraphApi.md#graph_radius_server_associations_list) | **GET** /radiusservers/{radiusserver_id}/associations | List the associations of a RADIUS  Server
*GraphApi* | [**graph_radius_server_associations_post**](docs/GraphApi.md#graph_radius_server_associations_post) | **POST** /radiusservers/{radiusserver_id}/associations | Manage the associations of a RADIUS Server
*GraphApi* | [**graph_radius_server_traverse_user**](docs/GraphApi.md#graph_radius_server_traverse_user) | **GET** /radiusservers/{radiusserver_id}/users | List the Users bound to a RADIUS  Server
*GraphApi* | [**graph_radius_server_traverse_user_group**](docs/GraphApi.md#graph_radius_server_traverse_user_group) | **GET** /radiusservers/{radiusserver_id}/usergroups | List the User Groups bound to a RADIUS  Server
*GraphApi* | [**graph_softwareapps_associations_list**](docs/GraphApi.md#graph_softwareapps_associations_list) | **GET** /softwareapps/{software_app_id}/associations | List the associations of a Software Application
*GraphApi* | [**graph_softwareapps_associations_post**](docs/GraphApi.md#graph_softwareapps_associations_post) | **POST** /softwareapps/{software_app_id}/associations | Manage the associations of a software application.
*GraphApi* | [**graph_softwareapps_traverse_system**](docs/GraphApi.md#graph_softwareapps_traverse_system) | **GET** /softwareapps/{software_app_id}/systems | List the Systems bound to a Software App.
*GraphApi* | [**graph_softwareapps_traverse_system_group**](docs/GraphApi.md#graph_softwareapps_traverse_system_group) | **GET** /softwareapps/{software_app_id}/systemgroups | List the System Groups bound to a Software App.
*GraphApi* | [**graph_system_associations_list**](docs/GraphApi.md#graph_system_associations_list) | **GET** /systems/{system_id}/associations | List the associations of a System
*GraphApi* | [**graph_system_associations_post**](docs/GraphApi.md#graph_system_associations_post) | **POST** /systems/{system_id}/associations | Manage associations of a System
*GraphApi* | [**graph_system_group_associations_list**](docs/GraphApi.md#graph_system_group_associations_list) | **GET** /systemgroups/{group_id}/associations | List the associations of a System Group
*GraphApi* | [**graph_system_group_associations_post**](docs/GraphApi.md#graph_system_group_associations_post) | **POST** /systemgroups/{group_id}/associations | Manage the associations of a System Group
*GraphApi* | [**graph_system_group_members_list**](docs/GraphApi.md#graph_system_group_members_list) | **GET** /systemgroups/{group_id}/members | List the members of a System Group
*GraphApi* | [**graph_system_group_members_post**](docs/GraphApi.md#graph_system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage the members of a System Group
*GraphApi* | [**graph_system_group_membership**](docs/GraphApi.md#graph_system_group_membership) | **GET** /systemgroups/{group_id}/membership | List the System Group&#x27;s membership
*GraphApi* | [**graph_system_group_traverse_command**](docs/GraphApi.md#graph_system_group_traverse_command) | **GET** /systemgroups/{group_id}/commands | List the Commands bound to a System Group
*GraphApi* | [**graph_system_group_traverse_policy**](docs/GraphApi.md#graph_system_group_traverse_policy) | **GET** /systemgroups/{group_id}/policies | List the Policies bound to a System Group
*GraphApi* | [**graph_system_group_traverse_policy_group**](docs/GraphApi.md#graph_system_group_traverse_policy_group) | **GET** /systemgroups/{group_id}/policygroups | List the Policy Groups bound to a System Group
*GraphApi* | [**graph_system_group_traverse_user**](docs/GraphApi.md#graph_system_group_traverse_user) | **GET** /systemgroups/{group_id}/users | List the Users bound to a System Group
*GraphApi* | [**graph_system_group_traverse_user_group**](docs/GraphApi.md#graph_system_group_traverse_user_group) | **GET** /systemgroups/{group_id}/usergroups | List the User Groups bound to a System Group
*GraphApi* | [**graph_system_member_of**](docs/GraphApi.md#graph_system_member_of) | **GET** /systems/{system_id}/memberof | List the parent Groups of a System
*GraphApi* | [**graph_system_traverse_command**](docs/GraphApi.md#graph_system_traverse_command) | **GET** /systems/{system_id}/commands | List the Commands bound to a System
*GraphApi* | [**graph_system_traverse_policy**](docs/GraphApi.md#graph_system_traverse_policy) | **GET** /systems/{system_id}/policies | List the Policies bound to a System
*GraphApi* | [**graph_system_traverse_policy_group**](docs/GraphApi.md#graph_system_traverse_policy_group) | **GET** /systems/{system_id}/policygroups | List the Policy Groups bound to a System
*GraphApi* | [**graph_system_traverse_user**](docs/GraphApi.md#graph_system_traverse_user) | **GET** /systems/{system_id}/users | List the Users bound to a System
*GraphApi* | [**graph_system_traverse_user_group**](docs/GraphApi.md#graph_system_traverse_user_group) | **GET** /systems/{system_id}/usergroups | List the User Groups bound to a System
*GraphApi* | [**graph_user_associations_list**](docs/GraphApi.md#graph_user_associations_list) | **GET** /users/{user_id}/associations | List the associations of a User
*GraphApi* | [**graph_user_associations_post**](docs/GraphApi.md#graph_user_associations_post) | **POST** /users/{user_id}/associations | Manage the associations of a User
*GraphApi* | [**graph_user_group_associations_list**](docs/GraphApi.md#graph_user_group_associations_list) | **GET** /usergroups/{group_id}/associations | List the associations of a User Group.
*GraphApi* | [**graph_user_group_associations_post**](docs/GraphApi.md#graph_user_group_associations_post) | **POST** /usergroups/{group_id}/associations | Manage the associations of a User Group
*GraphApi* | [**graph_user_group_members_list**](docs/GraphApi.md#graph_user_group_members_list) | **GET** /usergroups/{group_id}/members | List the members of a User Group
*GraphApi* | [**graph_user_group_members_post**](docs/GraphApi.md#graph_user_group_members_post) | **POST** /usergroups/{group_id}/members | Manage the members of a User Group
*GraphApi* | [**graph_user_group_membership**](docs/GraphApi.md#graph_user_group_membership) | **GET** /usergroups/{group_id}/membership | List the User Group&#x27;s membership
*GraphApi* | [**graph_user_group_traverse_active_directory**](docs/GraphApi.md#graph_user_group_traverse_active_directory) | **GET** /usergroups/{group_id}/activedirectories | List the Active Directories bound to a User Group
*GraphApi* | [**graph_user_group_traverse_application**](docs/GraphApi.md#graph_user_group_traverse_application) | **GET** /usergroups/{group_id}/applications | List the Applications bound to a User Group
*GraphApi* | [**graph_user_group_traverse_directory**](docs/GraphApi.md#graph_user_group_traverse_directory) | **GET** /usergroups/{group_id}/directories | List the Directories bound to a User Group
*GraphApi* | [**graph_user_group_traverse_g_suite**](docs/GraphApi.md#graph_user_group_traverse_g_suite) | **GET** /usergroups/{group_id}/gsuites | List the G Suite instances bound to a User Group
*GraphApi* | [**graph_user_group_traverse_ldap_server**](docs/GraphApi.md#graph_user_group_traverse_ldap_server) | **GET** /usergroups/{group_id}/ldapservers | List the LDAP Servers bound to a User Group
*GraphApi* | [**graph_user_group_traverse_office365**](docs/GraphApi.md#graph_user_group_traverse_office365) | **GET** /usergroups/{group_id}/office365s | List the Office 365 instances bound to a User Group
*GraphApi* | [**graph_user_group_traverse_radius_server**](docs/GraphApi.md#graph_user_group_traverse_radius_server) | **GET** /usergroups/{group_id}/radiusservers | List the RADIUS Servers bound to a User Group
*GraphApi* | [**graph_user_group_traverse_system**](docs/GraphApi.md#graph_user_group_traverse_system) | **GET** /usergroups/{group_id}/systems | List the Systems bound to a User Group
*GraphApi* | [**graph_user_group_traverse_system_group**](docs/GraphApi.md#graph_user_group_traverse_system_group) | **GET** /usergroups/{group_id}/systemgroups | List the System Groups bound to User Groups
*GraphApi* | [**graph_user_member_of**](docs/GraphApi.md#graph_user_member_of) | **GET** /users/{user_id}/memberof | List the parent Groups of a User
*GraphApi* | [**graph_user_traverse_active_directory**](docs/GraphApi.md#graph_user_traverse_active_directory) | **GET** /users/{user_id}/activedirectories | List the Active Directory instances bound to a User
*GraphApi* | [**graph_user_traverse_application**](docs/GraphApi.md#graph_user_traverse_application) | **GET** /users/{user_id}/applications | List the Applications bound to a User
*GraphApi* | [**graph_user_traverse_directory**](docs/GraphApi.md#graph_user_traverse_directory) | **GET** /users/{user_id}/directories | List the Directories bound to a User
*GraphApi* | [**graph_user_traverse_g_suite**](docs/GraphApi.md#graph_user_traverse_g_suite) | **GET** /users/{user_id}/gsuites | List the G Suite instances bound to a User
*GraphApi* | [**graph_user_traverse_ldap_server**](docs/GraphApi.md#graph_user_traverse_ldap_server) | **GET** /users/{user_id}/ldapservers | List the LDAP servers bound to a User
*GraphApi* | [**graph_user_traverse_office365**](docs/GraphApi.md#graph_user_traverse_office365) | **GET** /users/{user_id}/office365s | List the Office 365 instances bound to a User
*GraphApi* | [**graph_user_traverse_radius_server**](docs/GraphApi.md#graph_user_traverse_radius_server) | **GET** /users/{user_id}/radiusservers | List the RADIUS Servers bound to a User
*GraphApi* | [**graph_user_traverse_system**](docs/GraphApi.md#graph_user_traverse_system) | **GET** /users/{user_id}/systems | List the Systems bound to a User
*GraphApi* | [**graph_user_traverse_system_group**](docs/GraphApi.md#graph_user_traverse_system_group) | **GET** /users/{user_id}/systemgroups | List the System Groups bound to a User
*GraphApi* | [**policystatuses_systems_list**](docs/GraphApi.md#policystatuses_systems_list) | **GET** /systems/{system_id}/policystatuses | List the policy statuses for a system
*GroupsApi* | [**groups_list**](docs/GroupsApi.md#groups_list) | **GET** /groups | List All Groups
*IPListsApi* | [**iplists_delete**](docs/IPListsApi.md#iplists_delete) | **DELETE** /iplists/{id} | Delete an IP list
*IPListsApi* | [**iplists_get**](docs/IPListsApi.md#iplists_get) | **GET** /iplists/{id} | Get an IP list
*IPListsApi* | [**iplists_list**](docs/IPListsApi.md#iplists_list) | **GET** /iplists | List IP Lists
*IPListsApi* | [**iplists_patch**](docs/IPListsApi.md#iplists_patch) | **PATCH** /iplists/{id} | Update an IP list
*IPListsApi* | [**iplists_post**](docs/IPListsApi.md#iplists_post) | **POST** /iplists | Create IP List
*IPListsApi* | [**iplists_put**](docs/IPListsApi.md#iplists_put) | **PUT** /iplists/{id} | Replace an IP list
*ImageApi* | [**applications_delete_logo**](docs/ImageApi.md#applications_delete_logo) | **DELETE** /applications/{application_id}/logo | Delete application image
*LDAPServersApi* | [**graph_ldap_server_associations_list**](docs/LDAPServersApi.md#graph_ldap_server_associations_list) | **GET** /ldapservers/{ldapserver_id}/associations | List the associations of a LDAP Server
*LDAPServersApi* | [**graph_ldap_server_associations_post**](docs/LDAPServersApi.md#graph_ldap_server_associations_post) | **POST** /ldapservers/{ldapserver_id}/associations | Manage the associations of a LDAP Server
*LDAPServersApi* | [**graph_ldap_server_traverse_user**](docs/LDAPServersApi.md#graph_ldap_server_traverse_user) | **GET** /ldapservers/{ldapserver_id}/users | List the Users bound to a LDAP Server
*LDAPServersApi* | [**graph_ldap_server_traverse_user_group**](docs/LDAPServersApi.md#graph_ldap_server_traverse_user_group) | **GET** /ldapservers/{ldapserver_id}/usergroups | List the User Groups bound to a LDAP Server
*LDAPServersApi* | [**ldapservers_get**](docs/LDAPServersApi.md#ldapservers_get) | **GET** /ldapservers/{id} | Get LDAP Server
*LDAPServersApi* | [**ldapservers_list**](docs/LDAPServersApi.md#ldapservers_list) | **GET** /ldapservers | List LDAP Servers
*LDAPServersApi* | [**ldapservers_patch**](docs/LDAPServersApi.md#ldapservers_patch) | **PATCH** /ldapservers/{id} | Update existing LDAP server
*LogosApi* | [**logos_get**](docs/LogosApi.md#logos_get) | **GET** /logos/{id} | Get the logo associated with the specified id
*ManagedServiceProviderApi* | [**administrator_organizations_create_by_administrator**](docs/ManagedServiceProviderApi.md#administrator_organizations_create_by_administrator) | **POST** /administrators/{id}/organizationlinks | Allow Adminstrator access to an Organization.
*ManagedServiceProviderApi* | [**administrator_organizations_list_by_administrator**](docs/ManagedServiceProviderApi.md#administrator_organizations_list_by_administrator) | **GET** /administrators/{id}/organizationlinks | List the association links between an Administrator and Organizations.
*ManagedServiceProviderApi* | [**administrator_organizations_list_by_organization**](docs/ManagedServiceProviderApi.md#administrator_organizations_list_by_organization) | **GET** /organizations/{id}/administratorlinks | List the association links between an Organization and Administrators.
*ManagedServiceProviderApi* | [**administrator_organizations_remove_by_administrator**](docs/ManagedServiceProviderApi.md#administrator_organizations_remove_by_administrator) | **DELETE** /administrators/{administrator_id}/organizationlinks/{id} | Remove association between an Administrator and an Organization.
*ManagedServiceProviderApi* | [**provider_organizations_update_org**](docs/ManagedServiceProviderApi.md#provider_organizations_update_org) | **PUT** /providers/{provider_id}/organizations/{id} | Update Provider Organization
*ManagedServiceProviderApi* | [**providers_get_provider**](docs/ManagedServiceProviderApi.md#providers_get_provider) | **GET** /providers/{provider_id} | Retrieve Provider
*ManagedServiceProviderApi* | [**providers_list_administrators**](docs/ManagedServiceProviderApi.md#providers_list_administrators) | **GET** /providers/{provider_id}/administrators | List Provider Administrators
*ManagedServiceProviderApi* | [**providers_list_organizations**](docs/ManagedServiceProviderApi.md#providers_list_organizations) | **GET** /providers/{provider_id}/organizations | List Provider Organizations
*ManagedServiceProviderApi* | [**providers_post_admins**](docs/ManagedServiceProviderApi.md#providers_post_admins) | **POST** /providers/{provider_id}/administrators | Create a new Provider Administrator
*ManagedServiceProviderApi* | [**providers_retrieve_invoice**](docs/ManagedServiceProviderApi.md#providers_retrieve_invoice) | **GET** /providers/{provider_id}/invoices/{ID} | Download a provider&#x27;s invoice.
*ManagedServiceProviderApi* | [**providers_retrieve_invoices**](docs/ManagedServiceProviderApi.md#providers_retrieve_invoices) | **GET** /providers/{provider_id}/invoices | List a provider&#x27;s invoices.
*Office365Api* | [**graph_office365_associations_list**](docs/Office365Api.md#graph_office365_associations_list) | **GET** /office365s/{office365_id}/associations | List the associations of an Office 365 instance
*Office365Api* | [**graph_office365_associations_post**](docs/Office365Api.md#graph_office365_associations_post) | **POST** /office365s/{office365_id}/associations | Manage the associations of an Office 365 instance
*Office365Api* | [**graph_office365_traverse_user**](docs/Office365Api.md#graph_office365_traverse_user) | **GET** /office365s/{office365_id}/users | List the Users bound to an Office 365 instance
*Office365Api* | [**graph_office365_traverse_user_group**](docs/Office365Api.md#graph_office365_traverse_user_group) | **GET** /office365s/{office365_id}/usergroups | List the User Groups bound to an Office 365 instance
*Office365Api* | [**office365s_get**](docs/Office365Api.md#office365s_get) | **GET** /office365s/{office365_id} | Get Office 365 instance
*Office365Api* | [**office365s_list_import_users**](docs/Office365Api.md#office365s_list_import_users) | **GET** /office365s/{office365_id}/import/users | Get a list of users to import from an Office 365 instance
*Office365Api* | [**office365s_patch**](docs/Office365Api.md#office365s_patch) | **PATCH** /office365s/{office365_id} | Update existing Office 365 instance.
*Office365Api* | [**translation_rules_office365_delete**](docs/Office365Api.md#translation_rules_office365_delete) | **DELETE** /office365s/{office365_id}/translationrules/{id} | Deletes a Office 365 translation rule
*Office365Api* | [**translation_rules_office365_get**](docs/Office365Api.md#translation_rules_office365_get) | **GET** /office365s/{office365_id}/translationrules/{id} | Gets a specific Office 365 translation rule
*Office365Api* | [**translation_rules_office365_list**](docs/Office365Api.md#translation_rules_office365_list) | **GET** /office365s/{office365_id}/translationrules | List all the Office 365 Translation Rules
*Office365Api* | [**translation_rules_office365_post**](docs/Office365Api.md#translation_rules_office365_post) | **POST** /office365s/{office365_id}/translationrules | Create a new Office 365 Translation Rule
*Office365ImportApi* | [**office365s_list_import_users**](docs/Office365ImportApi.md#office365s_list_import_users) | **GET** /office365s/{office365_id}/import/users | Get a list of users to import from an Office 365 instance
*OrganizationsApi* | [**administrator_organizations_create_by_administrator**](docs/OrganizationsApi.md#administrator_organizations_create_by_administrator) | **POST** /administrators/{id}/organizationlinks | Allow Adminstrator access to an Organization.
*OrganizationsApi* | [**administrator_organizations_list_by_administrator**](docs/OrganizationsApi.md#administrator_organizations_list_by_administrator) | **GET** /administrators/{id}/organizationlinks | List the association links between an Administrator and Organizations.
*OrganizationsApi* | [**administrator_organizations_list_by_organization**](docs/OrganizationsApi.md#administrator_organizations_list_by_organization) | **GET** /organizations/{id}/administratorlinks | List the association links between an Organization and Administrators.
*OrganizationsApi* | [**administrator_organizations_remove_by_administrator**](docs/OrganizationsApi.md#administrator_organizations_remove_by_administrator) | **DELETE** /administrators/{administrator_id}/organizationlinks/{id} | Remove association between an Administrator and an Organization.
*OrganizationsApi* | [**organizations_list_cases**](docs/OrganizationsApi.md#organizations_list_cases) | **GET** /organizations/cases | Get all cases (Support/Feature requests) for organization
*PoliciesApi* | [**graph_policy_associations_list**](docs/PoliciesApi.md#graph_policy_associations_list) | **GET** /policies/{policy_id}/associations | List the associations of a Policy
*PoliciesApi* | [**graph_policy_associations_post**](docs/PoliciesApi.md#graph_policy_associations_post) | **POST** /policies/{policy_id}/associations | Manage the associations of a Policy
*PoliciesApi* | [**graph_policy_member_of**](docs/PoliciesApi.md#graph_policy_member_of) | **GET** /policies/{policy_id}/memberof | List the parent Groups of a Policy
*PoliciesApi* | [**graph_policy_traverse_system**](docs/PoliciesApi.md#graph_policy_traverse_system) | **GET** /policies/{policy_id}/systems | List the Systems bound to a Policy
*PoliciesApi* | [**graph_policy_traverse_system_group**](docs/PoliciesApi.md#graph_policy_traverse_system_group) | **GET** /policies/{policy_id}/systemgroups | List the System Groups bound to a Policy
*PoliciesApi* | [**policies_delete**](docs/PoliciesApi.md#policies_delete) | **DELETE** /policies/{id} | Deletes a Policy
*PoliciesApi* | [**policies_get**](docs/PoliciesApi.md#policies_get) | **GET** /policies/{id} | Gets a specific Policy.
*PoliciesApi* | [**policies_list**](docs/PoliciesApi.md#policies_list) | **GET** /policies | Lists all the Policies
*PoliciesApi* | [**policies_post**](docs/PoliciesApi.md#policies_post) | **POST** /policies | Create a new Policy
*PoliciesApi* | [**policies_put**](docs/PoliciesApi.md#policies_put) | **PUT** /policies/{id} | Update an existing Policy
*PoliciesApi* | [**policyresults_get**](docs/PoliciesApi.md#policyresults_get) | **GET** /policyresults/{id} | Get a specific Policy Result.
*PoliciesApi* | [**policyresults_list**](docs/PoliciesApi.md#policyresults_list) | **GET** /policies/{policy_id}/policyresults | Lists all the policy results of a policy.
*PoliciesApi* | [**policyresults_org_list**](docs/PoliciesApi.md#policyresults_org_list) | **GET** /policyresults | Lists all of the policy results for an organization.
*PoliciesApi* | [**policystatuses_policies_list**](docs/PoliciesApi.md#policystatuses_policies_list) | **GET** /policies/{policy_id}/policystatuses | Lists the latest policy results of a policy.
*PoliciesApi* | [**policystatuses_systems_list**](docs/PoliciesApi.md#policystatuses_systems_list) | **GET** /systems/{system_id}/policystatuses | List the policy statuses for a system
*PoliciesApi* | [**policytemplates_get**](docs/PoliciesApi.md#policytemplates_get) | **GET** /policytemplates/{id} | Get a specific Policy Template
*PoliciesApi* | [**policytemplates_list**](docs/PoliciesApi.md#policytemplates_list) | **GET** /policytemplates | Lists all of the Policy Templates
*PolicyGroupAssociationsApi* | [**graph_policy_group_associations_list**](docs/PolicyGroupAssociationsApi.md#graph_policy_group_associations_list) | **GET** /policygroups/{group_id}/associations | List the associations of a Policy Group.
*PolicyGroupAssociationsApi* | [**graph_policy_group_associations_post**](docs/PolicyGroupAssociationsApi.md#graph_policy_group_associations_post) | **POST** /policygroups/{group_id}/associations | Manage the associations of a Policy Group
*PolicyGroupAssociationsApi* | [**graph_policy_group_traverse_system**](docs/PolicyGroupAssociationsApi.md#graph_policy_group_traverse_system) | **GET** /policygroups/{group_id}/systems | List the Systems bound to a Policy Group
*PolicyGroupAssociationsApi* | [**graph_policy_group_traverse_system_group**](docs/PolicyGroupAssociationsApi.md#graph_policy_group_traverse_system_group) | **GET** /policygroups/{group_id}/systemgroups | List the System Groups bound to Policy Groups
*PolicyGroupMembersMembershipApi* | [**graph_policy_group_members_list**](docs/PolicyGroupMembersMembershipApi.md#graph_policy_group_members_list) | **GET** /policygroups/{group_id}/members | List the members of a Policy Group
*PolicyGroupMembersMembershipApi* | [**graph_policy_group_members_post**](docs/PolicyGroupMembersMembershipApi.md#graph_policy_group_members_post) | **POST** /policygroups/{group_id}/members | Manage the members of a Policy Group
*PolicyGroupMembersMembershipApi* | [**graph_policy_group_membership**](docs/PolicyGroupMembersMembershipApi.md#graph_policy_group_membership) | **GET** /policygroups/{group_id}/membership | List the Policy Group&#x27;s membership
*PolicyGroupsApi* | [**graph_policy_group_associations_list**](docs/PolicyGroupsApi.md#graph_policy_group_associations_list) | **GET** /policygroups/{group_id}/associations | List the associations of a Policy Group.
*PolicyGroupsApi* | [**graph_policy_group_associations_post**](docs/PolicyGroupsApi.md#graph_policy_group_associations_post) | **POST** /policygroups/{group_id}/associations | Manage the associations of a Policy Group
*PolicyGroupsApi* | [**graph_policy_group_members_list**](docs/PolicyGroupsApi.md#graph_policy_group_members_list) | **GET** /policygroups/{group_id}/members | List the members of a Policy Group
*PolicyGroupsApi* | [**graph_policy_group_members_post**](docs/PolicyGroupsApi.md#graph_policy_group_members_post) | **POST** /policygroups/{group_id}/members | Manage the members of a Policy Group
*PolicyGroupsApi* | [**graph_policy_group_membership**](docs/PolicyGroupsApi.md#graph_policy_group_membership) | **GET** /policygroups/{group_id}/membership | List the Policy Group&#x27;s membership
*PolicyGroupsApi* | [**graph_policy_group_traverse_system**](docs/PolicyGroupsApi.md#graph_policy_group_traverse_system) | **GET** /policygroups/{group_id}/systems | List the Systems bound to a Policy Group
*PolicyGroupsApi* | [**graph_policy_group_traverse_system_group**](docs/PolicyGroupsApi.md#graph_policy_group_traverse_system_group) | **GET** /policygroups/{group_id}/systemgroups | List the System Groups bound to Policy Groups
*PolicyGroupsApi* | [**groups_policy_delete**](docs/PolicyGroupsApi.md#groups_policy_delete) | **DELETE** /policygroups/{id} | Delete a Policy Group
*PolicyGroupsApi* | [**groups_policy_get**](docs/PolicyGroupsApi.md#groups_policy_get) | **GET** /policygroups/{id} | View an individual Policy Group details
*PolicyGroupsApi* | [**groups_policy_list**](docs/PolicyGroupsApi.md#groups_policy_list) | **GET** /policygroups | List all Policy Groups
*PolicyGroupsApi* | [**groups_policy_post**](docs/PolicyGroupsApi.md#groups_policy_post) | **POST** /policygroups | Create a new Policy Group
*PolicyGroupsApi* | [**groups_policy_put**](docs/PolicyGroupsApi.md#groups_policy_put) | **PUT** /policygroups/{id} | Update a Policy Group
*PolicytemplatesApi* | [**policytemplates_get**](docs/PolicytemplatesApi.md#policytemplates_get) | **GET** /policytemplates/{id} | Get a specific Policy Template
*PolicytemplatesApi* | [**policytemplates_list**](docs/PolicytemplatesApi.md#policytemplates_list) | **GET** /policytemplates | Lists all of the Policy Templates
*ProvidersApi* | [**autotask_create_configuration**](docs/ProvidersApi.md#autotask_create_configuration) | **POST** /providers/{provider_id}/integrations/autotask | Creates a new Autotask integration for the provider
*ProvidersApi* | [**autotask_delete_configuration**](docs/ProvidersApi.md#autotask_delete_configuration) | **DELETE** /integrations/autotask/{UUID} | Delete Autotask Integration
*ProvidersApi* | [**autotask_get_configuration**](docs/ProvidersApi.md#autotask_get_configuration) | **GET** /integrations/autotask/{UUID} | Retrieve Autotask Integration Configuration
*ProvidersApi* | [**autotask_patch_mappings**](docs/ProvidersApi.md#autotask_patch_mappings) | **PATCH** /integrations/autotask/{UUID}/mappings | Create, edit, and/or delete Autotask Mappings
*ProvidersApi* | [**autotask_patch_settings**](docs/ProvidersApi.md#autotask_patch_settings) | **PATCH** /integrations/autotask/{UUID}/settings | Create, edit, and/or delete Autotask Integration settings
*ProvidersApi* | [**autotask_retrieve_all_alert_configuration_options**](docs/ProvidersApi.md#autotask_retrieve_all_alert_configuration_options) | **GET** /providers/{provider_id}/integrations/autotask/alerts/configuration/options | Get all Autotask ticketing alert configuration options for a provider
*ProvidersApi* | [**autotask_retrieve_all_alert_configurations**](docs/ProvidersApi.md#autotask_retrieve_all_alert_configurations) | **GET** /providers/{provider_id}/integrations/autotask/alerts/configuration | Get all Autotask ticketing alert configurations for a provider
*ProvidersApi* | [**autotask_retrieve_companies**](docs/ProvidersApi.md#autotask_retrieve_companies) | **GET** /integrations/autotask/{UUID}/companies | Retrieve Autotask Companies
*ProvidersApi* | [**autotask_retrieve_company_types**](docs/ProvidersApi.md#autotask_retrieve_company_types) | **GET** /integrations/autotask/{UUID}/companytypes | Retrieve Autotask Company Types
*ProvidersApi* | [**autotask_retrieve_contracts**](docs/ProvidersApi.md#autotask_retrieve_contracts) | **GET** /integrations/autotask/{UUID}/contracts | Retrieve Autotask Contracts
*ProvidersApi* | [**autotask_retrieve_contracts_fields**](docs/ProvidersApi.md#autotask_retrieve_contracts_fields) | **GET** /integrations/autotask/{UUID}/contracts/fields | Retrieve Autotask Contract Fields
*ProvidersApi* | [**autotask_retrieve_mappings**](docs/ProvidersApi.md#autotask_retrieve_mappings) | **GET** /integrations/autotask/{UUID}/mappings | Retrieve Autotask mappings
*ProvidersApi* | [**autotask_retrieve_services**](docs/ProvidersApi.md#autotask_retrieve_services) | **GET** /integrations/autotask/{UUID}/contracts/services | Retrieve Autotask Contract Services
*ProvidersApi* | [**autotask_retrieve_settings**](docs/ProvidersApi.md#autotask_retrieve_settings) | **GET** /integrations/autotask/{UUID}/settings | Retrieve Autotask Integration settings
*ProvidersApi* | [**autotask_update_alert_configuration**](docs/ProvidersApi.md#autotask_update_alert_configuration) | **PUT** /providers/{provider_id}/integrations/autotask/alerts/{alert_UUID}/configuration | Update an Autotask ticketing alert&#x27;s configuration
*ProvidersApi* | [**autotask_update_configuration**](docs/ProvidersApi.md#autotask_update_configuration) | **PATCH** /integrations/autotask/{UUID} | Update Autotask Integration configuration
*ProvidersApi* | [**connectwise_create_configuration**](docs/ProvidersApi.md#connectwise_create_configuration) | **POST** /providers/{provider_id}/integrations/connectwise | Creates a new ConnectWise integration for the provider
*ProvidersApi* | [**connectwise_delete_configuration**](docs/ProvidersApi.md#connectwise_delete_configuration) | **DELETE** /integrations/connectwise/{UUID} | Delete ConnectWise Integration
*ProvidersApi* | [**connectwise_get_configuration**](docs/ProvidersApi.md#connectwise_get_configuration) | **GET** /integrations/connectwise/{UUID} | Retrieve ConnectWise Integration Configuration
*ProvidersApi* | [**connectwise_patch_mappings**](docs/ProvidersApi.md#connectwise_patch_mappings) | **PATCH** /integrations/connectwise/{UUID}/mappings | Create, edit, and/or delete ConnectWise Mappings
*ProvidersApi* | [**connectwise_patch_settings**](docs/ProvidersApi.md#connectwise_patch_settings) | **PATCH** /integrations/connectwise/{UUID}/settings | Create, edit, and/or delete ConnectWise Integration settings
*ProvidersApi* | [**connectwise_retrieve_additions**](docs/ProvidersApi.md#connectwise_retrieve_additions) | **GET** /integrations/connectwise/{UUID}/agreements/{agreement_ID}/additions | Retrieve ConnectWise Additions
*ProvidersApi* | [**connectwise_retrieve_agreements**](docs/ProvidersApi.md#connectwise_retrieve_agreements) | **GET** /integrations/connectwise/{UUID}/agreements | Retrieve ConnectWise Agreements
*ProvidersApi* | [**connectwise_retrieve_all_alert_configuration_options**](docs/ProvidersApi.md#connectwise_retrieve_all_alert_configuration_options) | **GET** /providers/{provider_id}/integrations/connectwise/alerts/configuration/options | Get all ConnectWise ticketing alert configuration options for a provider
*ProvidersApi* | [**connectwise_retrieve_all_alert_configurations**](docs/ProvidersApi.md#connectwise_retrieve_all_alert_configurations) | **GET** /providers/{provider_id}/integrations/connectwise/alerts/configuration | Get all ConnectWise ticketing alert configurations for a provider
*ProvidersApi* | [**connectwise_retrieve_companies**](docs/ProvidersApi.md#connectwise_retrieve_companies) | **GET** /integrations/connectwise/{UUID}/companies | Retrieve ConnectWise Companies
*ProvidersApi* | [**connectwise_retrieve_company_types**](docs/ProvidersApi.md#connectwise_retrieve_company_types) | **GET** /integrations/connectwise/{UUID}/companytypes | Retrieve ConnectWise Company Types
*ProvidersApi* | [**connectwise_retrieve_mappings**](docs/ProvidersApi.md#connectwise_retrieve_mappings) | **GET** /integrations/connectwise/{UUID}/mappings | Retrieve ConnectWise mappings
*ProvidersApi* | [**connectwise_retrieve_settings**](docs/ProvidersApi.md#connectwise_retrieve_settings) | **GET** /integrations/connectwise/{UUID}/settings | Retrieve ConnectWise Integration settings
*ProvidersApi* | [**connectwise_update_alert_configuration**](docs/ProvidersApi.md#connectwise_update_alert_configuration) | **PUT** /providers/{provider_id}/integrations/connectwise/alerts/{alert_UUID}/configuration | Update a ConnectWise ticketing alert&#x27;s configuration
*ProvidersApi* | [**connectwise_update_configuration**](docs/ProvidersApi.md#connectwise_update_configuration) | **PATCH** /integrations/connectwise/{UUID} | Update ConnectWise Integration configuration
*ProvidersApi* | [**mtp_integration_retrieve_alerts**](docs/ProvidersApi.md#mtp_integration_retrieve_alerts) | **GET** /providers/{provider_id}/integrations/ticketing/alerts | Get all ticketing alerts available for a provider&#x27;s ticketing integration.
*ProvidersApi* | [**mtp_integration_retrieve_sync_errors**](docs/ProvidersApi.md#mtp_integration_retrieve_sync_errors) | **GET** /integrations/{integration_type}/{UUID}/errors | Retrieve Recent Integration Sync Errors
*ProvidersApi* | [**provider_organizations_update_org**](docs/ProvidersApi.md#provider_organizations_update_org) | **PUT** /providers/{provider_id}/organizations/{id} | Update Provider Organization
*ProvidersApi* | [**providers_get_provider**](docs/ProvidersApi.md#providers_get_provider) | **GET** /providers/{provider_id} | Retrieve Provider
*ProvidersApi* | [**providers_list_administrators**](docs/ProvidersApi.md#providers_list_administrators) | **GET** /providers/{provider_id}/administrators | List Provider Administrators
*ProvidersApi* | [**providers_list_organizations**](docs/ProvidersApi.md#providers_list_organizations) | **GET** /providers/{provider_id}/organizations | List Provider Organizations
*ProvidersApi* | [**providers_post_admins**](docs/ProvidersApi.md#providers_post_admins) | **POST** /providers/{provider_id}/administrators | Create a new Provider Administrator
*ProvidersApi* | [**providers_remove_administrator**](docs/ProvidersApi.md#providers_remove_administrator) | **DELETE** /providers/{provider_id}/administrators/{id} | Delete Provider Administrator
*ProvidersApi* | [**providers_retrieve_integrations**](docs/ProvidersApi.md#providers_retrieve_integrations) | **GET** /providers/{provider_id}/integrations | Retrieve Integrations for Provider
*ProvidersApi* | [**providers_retrieve_invoice**](docs/ProvidersApi.md#providers_retrieve_invoice) | **GET** /providers/{provider_id}/invoices/{ID} | Download a provider&#x27;s invoice.
*ProvidersApi* | [**providers_retrieve_invoices**](docs/ProvidersApi.md#providers_retrieve_invoices) | **GET** /providers/{provider_id}/invoices | List a provider&#x27;s invoices.
*RADIUSServersApi* | [**graph_radius_server_associations_list**](docs/RADIUSServersApi.md#graph_radius_server_associations_list) | **GET** /radiusservers/{radiusserver_id}/associations | List the associations of a RADIUS  Server
*RADIUSServersApi* | [**graph_radius_server_associations_post**](docs/RADIUSServersApi.md#graph_radius_server_associations_post) | **POST** /radiusservers/{radiusserver_id}/associations | Manage the associations of a RADIUS Server
*RADIUSServersApi* | [**graph_radius_server_traverse_user**](docs/RADIUSServersApi.md#graph_radius_server_traverse_user) | **GET** /radiusservers/{radiusserver_id}/users | List the Users bound to a RADIUS  Server
*RADIUSServersApi* | [**graph_radius_server_traverse_user_group**](docs/RADIUSServersApi.md#graph_radius_server_traverse_user_group) | **GET** /radiusservers/{radiusserver_id}/usergroups | List the User Groups bound to a RADIUS  Server
*SCIMImportApi* | [**import_users**](docs/SCIMImportApi.md#import_users) | **GET** /applications/{application_id}/import/users | Get a list of users to import from an Application IdM service provider
*SambaDomainsApi* | [**ldapservers_samba_domains_delete**](docs/SambaDomainsApi.md#ldapservers_samba_domains_delete) | **DELETE** /ldapservers/{ldapserver_id}/sambadomains/{id} | Delete Samba Domain
*SambaDomainsApi* | [**ldapservers_samba_domains_get**](docs/SambaDomainsApi.md#ldapservers_samba_domains_get) | **GET** /ldapservers/{ldapserver_id}/sambadomains/{id} | Get Samba Domain
*SambaDomainsApi* | [**ldapservers_samba_domains_list**](docs/SambaDomainsApi.md#ldapservers_samba_domains_list) | **GET** /ldapservers/{ldapserver_id}/sambadomains | List Samba Domains
*SambaDomainsApi* | [**ldapservers_samba_domains_post**](docs/SambaDomainsApi.md#ldapservers_samba_domains_post) | **POST** /ldapservers/{ldapserver_id}/sambadomains | Create Samba Domain
*SambaDomainsApi* | [**ldapservers_samba_domains_put**](docs/SambaDomainsApi.md#ldapservers_samba_domains_put) | **PUT** /ldapservers/{ldapserver_id}/sambadomains/{id} | Update Samba Domain
*SoftwareAppsApi* | [**graph_softwareapps_associations_list**](docs/SoftwareAppsApi.md#graph_softwareapps_associations_list) | **GET** /softwareapps/{software_app_id}/associations | List the associations of a Software Application
*SoftwareAppsApi* | [**graph_softwareapps_associations_post**](docs/SoftwareAppsApi.md#graph_softwareapps_associations_post) | **POST** /softwareapps/{software_app_id}/associations | Manage the associations of a software application.
*SoftwareAppsApi* | [**graph_softwareapps_traverse_system**](docs/SoftwareAppsApi.md#graph_softwareapps_traverse_system) | **GET** /softwareapps/{software_app_id}/systems | List the Systems bound to a Software App.
*SoftwareAppsApi* | [**graph_softwareapps_traverse_system_group**](docs/SoftwareAppsApi.md#graph_softwareapps_traverse_system_group) | **GET** /softwareapps/{software_app_id}/systemgroups | List the System Groups bound to a Software App.
*SoftwareAppsApi* | [**software_app_statuses_list**](docs/SoftwareAppsApi.md#software_app_statuses_list) | **GET** /softwareapps/{software_app_id}/statuses | Get the status of the provided Software Application
*SoftwareAppsApi* | [**software_apps_delete**](docs/SoftwareAppsApi.md#software_apps_delete) | **DELETE** /softwareapps/{id} | Delete a configured Software Application
*SoftwareAppsApi* | [**software_apps_get**](docs/SoftwareAppsApi.md#software_apps_get) | **GET** /softwareapps/{id} | Retrieve a configured Software Application.
*SoftwareAppsApi* | [**software_apps_list**](docs/SoftwareAppsApi.md#software_apps_list) | **GET** /softwareapps | Get all configured Software Applications.
*SoftwareAppsApi* | [**software_apps_post**](docs/SoftwareAppsApi.md#software_apps_post) | **POST** /softwareapps | Create a Software Application that will be managed by JumpCloud.
*SoftwareAppsApi* | [**software_apps_reclaim_licenses**](docs/SoftwareAppsApi.md#software_apps_reclaim_licenses) | **POST** /softwareapps/{software_app_id}/reclaim-licenses | Reclaim Licenses for a Software Application.
*SoftwareAppsApi* | [**software_apps_retry_installation**](docs/SoftwareAppsApi.md#software_apps_retry_installation) | **POST** /softwareapps/{software_app_id}/retry-installation | Retry Installation for a Software Application
*SoftwareAppsApi* | [**software_apps_update**](docs/SoftwareAppsApi.md#software_apps_update) | **PUT** /softwareapps/{id} | Update a Software Application Configuration.
*SubscriptionsApi* | [**subscriptions_get**](docs/SubscriptionsApi.md#subscriptions_get) | **GET** /subscriptions | Lists all the Pricing &amp; Packaging Subscriptions
*SystemGroupAssociationsApi* | [**graph_system_group_associations_list**](docs/SystemGroupAssociationsApi.md#graph_system_group_associations_list) | **GET** /systemgroups/{group_id}/associations | List the associations of a System Group
*SystemGroupAssociationsApi* | [**graph_system_group_associations_post**](docs/SystemGroupAssociationsApi.md#graph_system_group_associations_post) | **POST** /systemgroups/{group_id}/associations | Manage the associations of a System Group
*SystemGroupAssociationsApi* | [**graph_system_group_traverse_command**](docs/SystemGroupAssociationsApi.md#graph_system_group_traverse_command) | **GET** /systemgroups/{group_id}/commands | List the Commands bound to a System Group
*SystemGroupAssociationsApi* | [**graph_system_group_traverse_policy**](docs/SystemGroupAssociationsApi.md#graph_system_group_traverse_policy) | **GET** /systemgroups/{group_id}/policies | List the Policies bound to a System Group
*SystemGroupAssociationsApi* | [**graph_system_group_traverse_policy_group**](docs/SystemGroupAssociationsApi.md#graph_system_group_traverse_policy_group) | **GET** /systemgroups/{group_id}/policygroups | List the Policy Groups bound to a System Group
*SystemGroupAssociationsApi* | [**graph_system_group_traverse_user**](docs/SystemGroupAssociationsApi.md#graph_system_group_traverse_user) | **GET** /systemgroups/{group_id}/users | List the Users bound to a System Group
*SystemGroupAssociationsApi* | [**graph_system_group_traverse_user_group**](docs/SystemGroupAssociationsApi.md#graph_system_group_traverse_user_group) | **GET** /systemgroups/{group_id}/usergroups | List the User Groups bound to a System Group
*SystemGroupMembersMembershipApi* | [**graph_system_group_members_list**](docs/SystemGroupMembersMembershipApi.md#graph_system_group_members_list) | **GET** /systemgroups/{group_id}/members | List the members of a System Group
*SystemGroupMembersMembershipApi* | [**graph_system_group_members_post**](docs/SystemGroupMembersMembershipApi.md#graph_system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage the members of a System Group
*SystemGroupMembersMembershipApi* | [**graph_system_group_membership**](docs/SystemGroupMembersMembershipApi.md#graph_system_group_membership) | **GET** /systemgroups/{group_id}/membership | List the System Group&#x27;s membership
*SystemGroupsApi* | [**graph_system_group_associations_list**](docs/SystemGroupsApi.md#graph_system_group_associations_list) | **GET** /systemgroups/{group_id}/associations | List the associations of a System Group
*SystemGroupsApi* | [**graph_system_group_associations_post**](docs/SystemGroupsApi.md#graph_system_group_associations_post) | **POST** /systemgroups/{group_id}/associations | Manage the associations of a System Group
*SystemGroupsApi* | [**graph_system_group_members_list**](docs/SystemGroupsApi.md#graph_system_group_members_list) | **GET** /systemgroups/{group_id}/members | List the members of a System Group
*SystemGroupsApi* | [**graph_system_group_members_post**](docs/SystemGroupsApi.md#graph_system_group_members_post) | **POST** /systemgroups/{group_id}/members | Manage the members of a System Group
*SystemGroupsApi* | [**graph_system_group_membership**](docs/SystemGroupsApi.md#graph_system_group_membership) | **GET** /systemgroups/{group_id}/membership | List the System Group&#x27;s membership
*SystemGroupsApi* | [**graph_system_group_traverse_policy**](docs/SystemGroupsApi.md#graph_system_group_traverse_policy) | **GET** /systemgroups/{group_id}/policies | List the Policies bound to a System Group
*SystemGroupsApi* | [**graph_system_group_traverse_policy_group**](docs/SystemGroupsApi.md#graph_system_group_traverse_policy_group) | **GET** /systemgroups/{group_id}/policygroups | List the Policy Groups bound to a System Group
*SystemGroupsApi* | [**graph_system_group_traverse_user**](docs/SystemGroupsApi.md#graph_system_group_traverse_user) | **GET** /systemgroups/{group_id}/users | List the Users bound to a System Group
*SystemGroupsApi* | [**graph_system_group_traverse_user_group**](docs/SystemGroupsApi.md#graph_system_group_traverse_user_group) | **GET** /systemgroups/{group_id}/usergroups | List the User Groups bound to a System Group
*SystemGroupsApi* | [**groups_system_delete**](docs/SystemGroupsApi.md#groups_system_delete) | **DELETE** /systemgroups/{id} | Delete a System Group
*SystemGroupsApi* | [**groups_system_get**](docs/SystemGroupsApi.md#groups_system_get) | **GET** /systemgroups/{id} | View an individual System Group details
*SystemGroupsApi* | [**groups_system_list**](docs/SystemGroupsApi.md#groups_system_list) | **GET** /systemgroups | List all System Groups
*SystemGroupsApi* | [**groups_system_post**](docs/SystemGroupsApi.md#groups_system_post) | **POST** /systemgroups | Create a new System Group
*SystemGroupsApi* | [**groups_system_put**](docs/SystemGroupsApi.md#groups_system_put) | **PUT** /systemgroups/{id} | Update a System Group
*SystemInsightsApi* | [**systeminsights_list_alf**](docs/SystemInsightsApi.md#systeminsights_list_alf) | **GET** /systeminsights/alf | List System Insights ALF
*SystemInsightsApi* | [**systeminsights_list_alf_exceptions**](docs/SystemInsightsApi.md#systeminsights_list_alf_exceptions) | **GET** /systeminsights/alf_exceptions | List System Insights ALF Exceptions
*SystemInsightsApi* | [**systeminsights_list_alf_explicit_auths**](docs/SystemInsightsApi.md#systeminsights_list_alf_explicit_auths) | **GET** /systeminsights/alf_explicit_auths | List System Insights ALF Explicit Authentications
*SystemInsightsApi* | [**systeminsights_list_appcompat_shims**](docs/SystemInsightsApi.md#systeminsights_list_appcompat_shims) | **GET** /systeminsights/appcompat_shims | List System Insights Application Compatibility Shims
*SystemInsightsApi* | [**systeminsights_list_apps**](docs/SystemInsightsApi.md#systeminsights_list_apps) | **GET** /systeminsights/apps | List System Insights Apps
*SystemInsightsApi* | [**systeminsights_list_authorized_keys**](docs/SystemInsightsApi.md#systeminsights_list_authorized_keys) | **GET** /systeminsights/authorized_keys | List System Insights Authorized Keys
*SystemInsightsApi* | [**systeminsights_list_azure_instance_metadata**](docs/SystemInsightsApi.md#systeminsights_list_azure_instance_metadata) | **GET** /systeminsights/azure_instance_metadata | List System Insights Azure Instance Metadata
*SystemInsightsApi* | [**systeminsights_list_azure_instance_tags**](docs/SystemInsightsApi.md#systeminsights_list_azure_instance_tags) | **GET** /systeminsights/azure_instance_tags | List System Insights Azure Instance Tags
*SystemInsightsApi* | [**systeminsights_list_battery**](docs/SystemInsightsApi.md#systeminsights_list_battery) | **GET** /systeminsights/battery | List System Insights Battery
*SystemInsightsApi* | [**systeminsights_list_bitlocker_info**](docs/SystemInsightsApi.md#systeminsights_list_bitlocker_info) | **GET** /systeminsights/bitlocker_info | List System Insights Bitlocker Info
*SystemInsightsApi* | [**systeminsights_list_browser_plugins**](docs/SystemInsightsApi.md#systeminsights_list_browser_plugins) | **GET** /systeminsights/browser_plugins | List System Insights Browser Plugins
*SystemInsightsApi* | [**systeminsights_list_certificates**](docs/SystemInsightsApi.md#systeminsights_list_certificates) | **GET** /systeminsights/certificates | List System Insights Certificates
*SystemInsightsApi* | [**systeminsights_list_chassis_info**](docs/SystemInsightsApi.md#systeminsights_list_chassis_info) | **GET** /systeminsights/chassis_info | List System Insights Chassis Info
*SystemInsightsApi* | [**systeminsights_list_chrome_extensions**](docs/SystemInsightsApi.md#systeminsights_list_chrome_extensions) | **GET** /systeminsights/chrome_extensions | List System Insights Chrome Extensions
*SystemInsightsApi* | [**systeminsights_list_connectivity**](docs/SystemInsightsApi.md#systeminsights_list_connectivity) | **GET** /systeminsights/connectivity | List System Insights Connectivity
*SystemInsightsApi* | [**systeminsights_list_crashes**](docs/SystemInsightsApi.md#systeminsights_list_crashes) | **GET** /systeminsights/crashes | List System Insights Crashes
*SystemInsightsApi* | [**systeminsights_list_cups_destinations**](docs/SystemInsightsApi.md#systeminsights_list_cups_destinations) | **GET** /systeminsights/cups_destinations | List System Insights CUPS Destinations
*SystemInsightsApi* | [**systeminsights_list_disk_encryption**](docs/SystemInsightsApi.md#systeminsights_list_disk_encryption) | **GET** /systeminsights/disk_encryption | List System Insights Disk Encryption
*SystemInsightsApi* | [**systeminsights_list_disk_info**](docs/SystemInsightsApi.md#systeminsights_list_disk_info) | **GET** /systeminsights/disk_info | List System Insights Disk Info
*SystemInsightsApi* | [**systeminsights_list_dns_resolvers**](docs/SystemInsightsApi.md#systeminsights_list_dns_resolvers) | **GET** /systeminsights/dns_resolvers | List System Insights DNS Resolvers
*SystemInsightsApi* | [**systeminsights_list_etc_hosts**](docs/SystemInsightsApi.md#systeminsights_list_etc_hosts) | **GET** /systeminsights/etc_hosts | List System Insights Etc Hosts
*SystemInsightsApi* | [**systeminsights_list_firefox_addons**](docs/SystemInsightsApi.md#systeminsights_list_firefox_addons) | **GET** /systeminsights/firefox_addons | List System Insights Firefox Addons
*SystemInsightsApi* | [**systeminsights_list_groups**](docs/SystemInsightsApi.md#systeminsights_list_groups) | **GET** /systeminsights/groups | List System Insights Groups
*SystemInsightsApi* | [**systeminsights_list_ie_extensions**](docs/SystemInsightsApi.md#systeminsights_list_ie_extensions) | **GET** /systeminsights/ie_extensions | List System Insights IE Extensions
*SystemInsightsApi* | [**systeminsights_list_interface_addresses**](docs/SystemInsightsApi.md#systeminsights_list_interface_addresses) | **GET** /systeminsights/interface_addresses | List System Insights Interface Addresses
*SystemInsightsApi* | [**systeminsights_list_interface_details**](docs/SystemInsightsApi.md#systeminsights_list_interface_details) | **GET** /systeminsights/interface_details | List System Insights Interface Details
*SystemInsightsApi* | [**systeminsights_list_kernel_info**](docs/SystemInsightsApi.md#systeminsights_list_kernel_info) | **GET** /systeminsights/kernel_info | List System Insights Kernel Info
*SystemInsightsApi* | [**systeminsights_list_launchd**](docs/SystemInsightsApi.md#systeminsights_list_launchd) | **GET** /systeminsights/launchd | List System Insights Launchd
*SystemInsightsApi* | [**systeminsights_list_linux_packages**](docs/SystemInsightsApi.md#systeminsights_list_linux_packages) | **GET** /systeminsights/linux_packages | List System Insights Linux Packages
*SystemInsightsApi* | [**systeminsights_list_logged_in_users**](docs/SystemInsightsApi.md#systeminsights_list_logged_in_users) | **GET** /systeminsights/logged_in_users | List System Insights Logged-In Users
*SystemInsightsApi* | [**systeminsights_list_logical_drives**](docs/SystemInsightsApi.md#systeminsights_list_logical_drives) | **GET** /systeminsights/logical_drives | List System Insights Logical Drives
*SystemInsightsApi* | [**systeminsights_list_managed_policies**](docs/SystemInsightsApi.md#systeminsights_list_managed_policies) | **GET** /systeminsights/managed_policies | List System Insights Managed Policies
*SystemInsightsApi* | [**systeminsights_list_mounts**](docs/SystemInsightsApi.md#systeminsights_list_mounts) | **GET** /systeminsights/mounts | List System Insights Mounts
*SystemInsightsApi* | [**systeminsights_list_os_version**](docs/SystemInsightsApi.md#systeminsights_list_os_version) | **GET** /systeminsights/os_version | List System Insights OS Version
*SystemInsightsApi* | [**systeminsights_list_patches**](docs/SystemInsightsApi.md#systeminsights_list_patches) | **GET** /systeminsights/patches | List System Insights Patches
*SystemInsightsApi* | [**systeminsights_list_programs**](docs/SystemInsightsApi.md#systeminsights_list_programs) | **GET** /systeminsights/programs | List System Insights Programs
*SystemInsightsApi* | [**systeminsights_list_python_packages**](docs/SystemInsightsApi.md#systeminsights_list_python_packages) | **GET** /systeminsights/python_packages | List System Insights Python Packages
*SystemInsightsApi* | [**systeminsights_list_safari_extensions**](docs/SystemInsightsApi.md#systeminsights_list_safari_extensions) | **GET** /systeminsights/safari_extensions | List System Insights Safari Extensions
*SystemInsightsApi* | [**systeminsights_list_scheduled_tasks**](docs/SystemInsightsApi.md#systeminsights_list_scheduled_tasks) | **GET** /systeminsights/scheduled_tasks | List System Insights Scheduled Tasks
*SystemInsightsApi* | [**systeminsights_list_secureboot**](docs/SystemInsightsApi.md#systeminsights_list_secureboot) | **GET** /systeminsights/secureboot | List System Insights Secure Boot
*SystemInsightsApi* | [**systeminsights_list_services**](docs/SystemInsightsApi.md#systeminsights_list_services) | **GET** /systeminsights/services | List System Insights Services
*SystemInsightsApi* | [**systeminsights_list_shadow**](docs/SystemInsightsApi.md#systeminsights_list_shadow) | **GET** /systeminsights/shadow | LIst System Insights Shadow
*SystemInsightsApi* | [**systeminsights_list_shared_folders**](docs/SystemInsightsApi.md#systeminsights_list_shared_folders) | **GET** /systeminsights/shared_folders | List System Insights Shared Folders
*SystemInsightsApi* | [**systeminsights_list_shared_resources**](docs/SystemInsightsApi.md#systeminsights_list_shared_resources) | **GET** /systeminsights/shared_resources | List System Insights Shared Resources
*SystemInsightsApi* | [**systeminsights_list_sharing_preferences**](docs/SystemInsightsApi.md#systeminsights_list_sharing_preferences) | **GET** /systeminsights/sharing_preferences | List System Insights Sharing Preferences
*SystemInsightsApi* | [**systeminsights_list_sip_config**](docs/SystemInsightsApi.md#systeminsights_list_sip_config) | **GET** /systeminsights/sip_config | List System Insights SIP Config
*SystemInsightsApi* | [**systeminsights_list_startup_items**](docs/SystemInsightsApi.md#systeminsights_list_startup_items) | **GET** /systeminsights/startup_items | List System Insights Startup Items
*SystemInsightsApi* | [**systeminsights_list_system_controls**](docs/SystemInsightsApi.md#systeminsights_list_system_controls) | **GET** /systeminsights/system_controls | List System Insights System Control
*SystemInsightsApi* | [**systeminsights_list_system_info**](docs/SystemInsightsApi.md#systeminsights_list_system_info) | **GET** /systeminsights/system_info | List System Insights System Info
*SystemInsightsApi* | [**systeminsights_list_tpm_info**](docs/SystemInsightsApi.md#systeminsights_list_tpm_info) | **GET** /systeminsights/tpm_info | List System Insights TPM Info
*SystemInsightsApi* | [**systeminsights_list_uptime**](docs/SystemInsightsApi.md#systeminsights_list_uptime) | **GET** /systeminsights/uptime | List System Insights Uptime
*SystemInsightsApi* | [**systeminsights_list_usb_devices**](docs/SystemInsightsApi.md#systeminsights_list_usb_devices) | **GET** /systeminsights/usb_devices | List System Insights USB Devices
*SystemInsightsApi* | [**systeminsights_list_user_groups**](docs/SystemInsightsApi.md#systeminsights_list_user_groups) | **GET** /systeminsights/user_groups | List System Insights User Groups
*SystemInsightsApi* | [**systeminsights_list_user_ssh_keys**](docs/SystemInsightsApi.md#systeminsights_list_user_ssh_keys) | **GET** /systeminsights/user_ssh_keys | List System Insights User SSH Keys
*SystemInsightsApi* | [**systeminsights_list_userassist**](docs/SystemInsightsApi.md#systeminsights_list_userassist) | **GET** /systeminsights/userassist | List System Insights User Assist
*SystemInsightsApi* | [**systeminsights_list_users**](docs/SystemInsightsApi.md#systeminsights_list_users) | **GET** /systeminsights/users | List System Insights Users
*SystemInsightsApi* | [**systeminsights_list_wifi_networks**](docs/SystemInsightsApi.md#systeminsights_list_wifi_networks) | **GET** /systeminsights/wifi_networks | List System Insights WiFi Networks
*SystemInsightsApi* | [**systeminsights_list_wifi_status**](docs/SystemInsightsApi.md#systeminsights_list_wifi_status) | **GET** /systeminsights/wifi_status | List System Insights WiFi Status
*SystemInsightsApi* | [**systeminsights_list_windows_security_center**](docs/SystemInsightsApi.md#systeminsights_list_windows_security_center) | **GET** /systeminsights/windows_security_center | List System Insights Windows Security Center
*SystemInsightsApi* | [**systeminsights_list_windows_security_products**](docs/SystemInsightsApi.md#systeminsights_list_windows_security_products) | **GET** /systeminsights/windows_security_products | List System Insights Windows Security Products
*SystemsApi* | [**graph_system_associations_list**](docs/SystemsApi.md#graph_system_associations_list) | **GET** /systems/{system_id}/associations | List the associations of a System
*SystemsApi* | [**graph_system_associations_post**](docs/SystemsApi.md#graph_system_associations_post) | **POST** /systems/{system_id}/associations | Manage associations of a System
*SystemsApi* | [**graph_system_member_of**](docs/SystemsApi.md#graph_system_member_of) | **GET** /systems/{system_id}/memberof | List the parent Groups of a System
*SystemsApi* | [**graph_system_traverse_command**](docs/SystemsApi.md#graph_system_traverse_command) | **GET** /systems/{system_id}/commands | List the Commands bound to a System
*SystemsApi* | [**graph_system_traverse_policy**](docs/SystemsApi.md#graph_system_traverse_policy) | **GET** /systems/{system_id}/policies | List the Policies bound to a System
*SystemsApi* | [**graph_system_traverse_policy_group**](docs/SystemsApi.md#graph_system_traverse_policy_group) | **GET** /systems/{system_id}/policygroups | List the Policy Groups bound to a System
*SystemsApi* | [**graph_system_traverse_user**](docs/SystemsApi.md#graph_system_traverse_user) | **GET** /systems/{system_id}/users | List the Users bound to a System
*SystemsApi* | [**graph_system_traverse_user_group**](docs/SystemsApi.md#graph_system_traverse_user_group) | **GET** /systems/{system_id}/usergroups | List the User Groups bound to a System
*SystemsApi* | [**systems_get_fde_key**](docs/SystemsApi.md#systems_get_fde_key) | **GET** /systems/{system_id}/fdekey | Get System FDE Key
*SystemsApi* | [**systems_list_software_apps_with_statuses**](docs/SystemsApi.md#systems_list_software_apps_with_statuses) | **GET** /systems/{system_id}/softwareappstatuses | List the associated Software Application Statuses of a System
*UserGroupAssociationsApi* | [**graph_user_group_associations_list**](docs/UserGroupAssociationsApi.md#graph_user_group_associations_list) | **GET** /usergroups/{group_id}/associations | List the associations of a User Group.
*UserGroupAssociationsApi* | [**graph_user_group_associations_post**](docs/UserGroupAssociationsApi.md#graph_user_group_associations_post) | **POST** /usergroups/{group_id}/associations | Manage the associations of a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_active_directory**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_active_directory) | **GET** /usergroups/{group_id}/activedirectories | List the Active Directories bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_application**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_application) | **GET** /usergroups/{group_id}/applications | List the Applications bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_directory**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_directory) | **GET** /usergroups/{group_id}/directories | List the Directories bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_g_suite**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_g_suite) | **GET** /usergroups/{group_id}/gsuites | List the G Suite instances bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_ldap_server**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_ldap_server) | **GET** /usergroups/{group_id}/ldapservers | List the LDAP Servers bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_office365**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_office365) | **GET** /usergroups/{group_id}/office365s | List the Office 365 instances bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_radius_server**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_radius_server) | **GET** /usergroups/{group_id}/radiusservers | List the RADIUS Servers bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_system**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_system) | **GET** /usergroups/{group_id}/systems | List the Systems bound to a User Group
*UserGroupAssociationsApi* | [**graph_user_group_traverse_system_group**](docs/UserGroupAssociationsApi.md#graph_user_group_traverse_system_group) | **GET** /usergroups/{group_id}/systemgroups | List the System Groups bound to User Groups
*UserGroupMembersMembershipApi* | [**graph_user_group_members_list**](docs/UserGroupMembersMembershipApi.md#graph_user_group_members_list) | **GET** /usergroups/{group_id}/members | List the members of a User Group
*UserGroupMembersMembershipApi* | [**graph_user_group_members_post**](docs/UserGroupMembersMembershipApi.md#graph_user_group_members_post) | **POST** /usergroups/{group_id}/members | Manage the members of a User Group
*UserGroupMembersMembershipApi* | [**graph_user_group_membership**](docs/UserGroupMembersMembershipApi.md#graph_user_group_membership) | **GET** /usergroups/{group_id}/membership | List the User Group&#x27;s membership
*UserGroupsApi* | [**graph_user_group_associations_list**](docs/UserGroupsApi.md#graph_user_group_associations_list) | **GET** /usergroups/{group_id}/associations | List the associations of a User Group.
*UserGroupsApi* | [**graph_user_group_associations_post**](docs/UserGroupsApi.md#graph_user_group_associations_post) | **POST** /usergroups/{group_id}/associations | Manage the associations of a User Group
*UserGroupsApi* | [**graph_user_group_members_list**](docs/UserGroupsApi.md#graph_user_group_members_list) | **GET** /usergroups/{group_id}/members | List the members of a User Group
*UserGroupsApi* | [**graph_user_group_members_post**](docs/UserGroupsApi.md#graph_user_group_members_post) | **POST** /usergroups/{group_id}/members | Manage the members of a User Group
*UserGroupsApi* | [**graph_user_group_membership**](docs/UserGroupsApi.md#graph_user_group_membership) | **GET** /usergroups/{group_id}/membership | List the User Group&#x27;s membership
*UserGroupsApi* | [**graph_user_group_traverse_active_directory**](docs/UserGroupsApi.md#graph_user_group_traverse_active_directory) | **GET** /usergroups/{group_id}/activedirectories | List the Active Directories bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_application**](docs/UserGroupsApi.md#graph_user_group_traverse_application) | **GET** /usergroups/{group_id}/applications | List the Applications bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_directory**](docs/UserGroupsApi.md#graph_user_group_traverse_directory) | **GET** /usergroups/{group_id}/directories | List the Directories bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_g_suite**](docs/UserGroupsApi.md#graph_user_group_traverse_g_suite) | **GET** /usergroups/{group_id}/gsuites | List the G Suite instances bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_ldap_server**](docs/UserGroupsApi.md#graph_user_group_traverse_ldap_server) | **GET** /usergroups/{group_id}/ldapservers | List the LDAP Servers bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_office365**](docs/UserGroupsApi.md#graph_user_group_traverse_office365) | **GET** /usergroups/{group_id}/office365s | List the Office 365 instances bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_radius_server**](docs/UserGroupsApi.md#graph_user_group_traverse_radius_server) | **GET** /usergroups/{group_id}/radiusservers | List the RADIUS Servers bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_system**](docs/UserGroupsApi.md#graph_user_group_traverse_system) | **GET** /usergroups/{group_id}/systems | List the Systems bound to a User Group
*UserGroupsApi* | [**graph_user_group_traverse_system_group**](docs/UserGroupsApi.md#graph_user_group_traverse_system_group) | **GET** /usergroups/{group_id}/systemgroups | List the System Groups bound to User Groups
*UserGroupsApi* | [**groups_suggestions_get**](docs/UserGroupsApi.md#groups_suggestions_get) | **GET** /usergroups/{group_id}/suggestions | List Suggestions for a User Group
*UserGroupsApi* | [**groups_suggestions_post**](docs/UserGroupsApi.md#groups_suggestions_post) | **POST** /usergroups/{group_id}/suggestions | List Suggestions for a User Group
*UserGroupsApi* | [**groups_user_delete**](docs/UserGroupsApi.md#groups_user_delete) | **DELETE** /usergroups/{id} | Delete a User Group
*UserGroupsApi* | [**groups_user_get**](docs/UserGroupsApi.md#groups_user_get) | **GET** /usergroups/{id} | View an individual User Group details
*UserGroupsApi* | [**groups_user_list**](docs/UserGroupsApi.md#groups_user_list) | **GET** /usergroups | List all User Groups
*UserGroupsApi* | [**groups_user_post**](docs/UserGroupsApi.md#groups_user_post) | **POST** /usergroups | Create a new User Group
*UserGroupsApi* | [**groups_user_put**](docs/UserGroupsApi.md#groups_user_put) | **PUT** /usergroups/{id} | Update a User Group
*UsersApi* | [**graph_user_associations_list**](docs/UsersApi.md#graph_user_associations_list) | **GET** /users/{user_id}/associations | List the associations of a User
*UsersApi* | [**graph_user_associations_post**](docs/UsersApi.md#graph_user_associations_post) | **POST** /users/{user_id}/associations | Manage the associations of a User
*UsersApi* | [**graph_user_member_of**](docs/UsersApi.md#graph_user_member_of) | **GET** /users/{user_id}/memberof | List the parent Groups of a User
*UsersApi* | [**graph_user_traverse_active_directory**](docs/UsersApi.md#graph_user_traverse_active_directory) | **GET** /users/{user_id}/activedirectories | List the Active Directory instances bound to a User
*UsersApi* | [**graph_user_traverse_application**](docs/UsersApi.md#graph_user_traverse_application) | **GET** /users/{user_id}/applications | List the Applications bound to a User
*UsersApi* | [**graph_user_traverse_directory**](docs/UsersApi.md#graph_user_traverse_directory) | **GET** /users/{user_id}/directories | List the Directories bound to a User
*UsersApi* | [**graph_user_traverse_g_suite**](docs/UsersApi.md#graph_user_traverse_g_suite) | **GET** /users/{user_id}/gsuites | List the G Suite instances bound to a User
*UsersApi* | [**graph_user_traverse_ldap_server**](docs/UsersApi.md#graph_user_traverse_ldap_server) | **GET** /users/{user_id}/ldapservers | List the LDAP servers bound to a User
*UsersApi* | [**graph_user_traverse_office365**](docs/UsersApi.md#graph_user_traverse_office365) | **GET** /users/{user_id}/office365s | List the Office 365 instances bound to a User
*UsersApi* | [**graph_user_traverse_radius_server**](docs/UsersApi.md#graph_user_traverse_radius_server) | **GET** /users/{user_id}/radiusservers | List the RADIUS Servers bound to a User
*UsersApi* | [**graph_user_traverse_system**](docs/UsersApi.md#graph_user_traverse_system) | **GET** /users/{user_id}/systems | List the Systems bound to a User
*UsersApi* | [**graph_user_traverse_system_group**](docs/UsersApi.md#graph_user_traverse_system_group) | **GET** /users/{user_id}/systemgroups | List the System Groups bound to a User
*UsersApi* | [**push_endpoints_delete**](docs/UsersApi.md#push_endpoints_delete) | **DELETE** /users/{user_id}/pushendpoints/{push_endpoint_id} | Delete a Push Endpoint associated with a User
*UsersApi* | [**push_endpoints_get**](docs/UsersApi.md#push_endpoints_get) | **GET** /users/{user_id}/pushendpoints/{push_endpoint_id} | Get a push endpoint associated with a User
*UsersApi* | [**push_endpoints_list**](docs/UsersApi.md#push_endpoints_list) | **GET** /users/{user_id}/pushendpoints | List Push Endpoints associated with a User
*UsersApi* | [**push_endpoints_patch**](docs/UsersApi.md#push_endpoints_patch) | **PATCH** /users/{user_id}/pushendpoints/{push_endpoint_id} | Update a push endpoint associated with a User
*WorkdayImportApi* | [**workdays_authorize**](docs/WorkdayImportApi.md#workdays_authorize) | **POST** /workdays/{workday_id}/auth | Authorize Workday
*WorkdayImportApi* | [**workdays_deauthorize**](docs/WorkdayImportApi.md#workdays_deauthorize) | **DELETE** /workdays/{workday_id}/auth | Deauthorize Workday
*WorkdayImportApi* | [**workdays_get**](docs/WorkdayImportApi.md#workdays_get) | **GET** /workdays/{id} | Get Workday
*WorkdayImportApi* | [**workdays_import**](docs/WorkdayImportApi.md#workdays_import) | **POST** /workdays/{workday_id}/import | Workday Import
*WorkdayImportApi* | [**workdays_importresults**](docs/WorkdayImportApi.md#workdays_importresults) | **GET** /workdays/{id}/import/{job_id}/results | List Import Results
*WorkdayImportApi* | [**workdays_list**](docs/WorkdayImportApi.md#workdays_list) | **GET** /workdays | List Workdays
*WorkdayImportApi* | [**workdays_post**](docs/WorkdayImportApi.md#workdays_post) | **POST** /workdays | Create new Workday
*WorkdayImportApi* | [**workdays_put**](docs/WorkdayImportApi.md#workdays_put) | **PUT** /workdays/{id} | Update Workday
*WorkdayImportApi* | [**workdays_workers**](docs/WorkdayImportApi.md#workdays_workers) | **GET** /workdays/{workday_id}/workers | List Workday Workers
*FdeApi* | [**systems_get_fde_key**](docs/FdeApi.md#systems_get_fde_key) | **GET** /systems/{system_id}/fdekey | Get System FDE Key

## Documentation For Models

 - [ADE](docs/ADE.md)
 - [ADES](docs/ADES.md)
 - [ActiveDirectoryAgentGetOutput](docs/ActiveDirectoryAgentGetOutput.md)
 - [ActiveDirectoryAgentInput](docs/ActiveDirectoryAgentInput.md)
 - [ActiveDirectoryAgentListOutput](docs/ActiveDirectoryAgentListOutput.md)
 - [ActiveDirectoryInput](docs/ActiveDirectoryInput.md)
 - [ActiveDirectoryOutput](docs/ActiveDirectoryOutput.md)
 - [Address](docs/Address.md)
 - [Administrator](docs/Administrator.md)
 - [AdministratorOrganizationLink](docs/AdministratorOrganizationLink.md)
 - [AdministratorOrganizationLinkReq](docs/AdministratorOrganizationLinkReq.md)
 - [AllOfAutotaskTicketingAlertConfigurationListRecordsItems](docs/AllOfAutotaskTicketingAlertConfigurationListRecordsItems.md)
 - [AllOfConnectWiseTicketingAlertConfigurationListRecordsItems](docs/AllOfConnectWiseTicketingAlertConfigurationListRecordsItems.md)
 - [AnyValue](docs/AnyValue.md)
 - [AppleMDM](docs/AppleMDM.md)
 - [AppleMdmDevice](docs/AppleMdmDevice.md)
 - [AppleMdmDeviceInfo](docs/AppleMdmDeviceInfo.md)
 - [AppleMdmDeviceSecurityInfo](docs/AppleMdmDeviceSecurityInfo.md)
 - [AppleMdmPatchInput](docs/AppleMdmPatchInput.md)
 - [AppleMdmPublicKeyCert](docs/AppleMdmPublicKeyCert.md)
 - [AppleMdmSignedCsrPlist](docs/AppleMdmSignedCsrPlist.md)
 - [ApplicationIdLogoBody](docs/ApplicationIdLogoBody.md)
 - [AuthInfo](docs/AuthInfo.md)
 - [AuthInput](docs/AuthInput.md)
 - [AuthInputObject](docs/AuthInputObject.md)
 - [AuthinputBasic](docs/AuthinputBasic.md)
 - [AuthinputOauth](docs/AuthinputOauth.md)
 - [AuthnPolicy](docs/AuthnPolicy.md)
 - [AuthnPolicyEffect](docs/AuthnPolicyEffect.md)
 - [AuthnPolicyInput](docs/AuthnPolicyInput.md)
 - [AuthnPolicyObligations](docs/AuthnPolicyObligations.md)
 - [AuthnPolicyObligationsMfa](docs/AuthnPolicyObligationsMfa.md)
 - [AuthnPolicyObligationsUserVerification](docs/AuthnPolicyObligationsUserVerification.md)
 - [AuthnPolicyResourceTarget](docs/AuthnPolicyResourceTarget.md)
 - [AuthnPolicyTargets](docs/AuthnPolicyTargets.md)
 - [AuthnPolicyType](docs/AuthnPolicyType.md)
 - [AuthnPolicyUserAttributeFilter](docs/AuthnPolicyUserAttributeFilter.md)
 - [AuthnPolicyUserAttributeTarget](docs/AuthnPolicyUserAttributeTarget.md)
 - [AuthnPolicyUserGroupTarget](docs/AuthnPolicyUserGroupTarget.md)
 - [AuthnPolicyUserTarget](docs/AuthnPolicyUserTarget.md)
 - [AutotaskCompany](docs/AutotaskCompany.md)
 - [AutotaskCompanyResp](docs/AutotaskCompanyResp.md)
 - [AutotaskCompanyTypeResp](docs/AutotaskCompanyTypeResp.md)
 - [AutotaskContract](docs/AutotaskContract.md)
 - [AutotaskContractField](docs/AutotaskContractField.md)
 - [AutotaskContractFieldValues](docs/AutotaskContractFieldValues.md)
 - [AutotaskIntegration](docs/AutotaskIntegration.md)
 - [AutotaskIntegrationPatchReq](docs/AutotaskIntegrationPatchReq.md)
 - [AutotaskIntegrationReq](docs/AutotaskIntegrationReq.md)
 - [AutotaskMappingRequest](docs/AutotaskMappingRequest.md)
 - [AutotaskMappingRequestCompany](docs/AutotaskMappingRequestCompany.md)
 - [AutotaskMappingRequestContract](docs/AutotaskMappingRequestContract.md)
 - [AutotaskMappingRequestData](docs/AutotaskMappingRequestData.md)
 - [AutotaskMappingRequestOrganization](docs/AutotaskMappingRequestOrganization.md)
 - [AutotaskMappingRequestService](docs/AutotaskMappingRequestService.md)
 - [AutotaskMappingResponse](docs/AutotaskMappingResponse.md)
 - [AutotaskMappingResponseCompany](docs/AutotaskMappingResponseCompany.md)
 - [AutotaskMappingResponseContract](docs/AutotaskMappingResponseContract.md)
 - [AutotaskMappingResponseOrganization](docs/AutotaskMappingResponseOrganization.md)
 - [AutotaskMappingResponseService](docs/AutotaskMappingResponseService.md)
 - [AutotaskService](docs/AutotaskService.md)
 - [AutotaskSettings](docs/AutotaskSettings.md)
 - [AutotaskSettingsPatchReq](docs/AutotaskSettingsPatchReq.md)
 - [AutotaskTicketingAlertConfiguration](docs/AutotaskTicketingAlertConfiguration.md)
 - [AutotaskTicketingAlertConfigurationList](docs/AutotaskTicketingAlertConfigurationList.md)
 - [AutotaskTicketingAlertConfigurationOption](docs/AutotaskTicketingAlertConfigurationOption.md)
 - [AutotaskTicketingAlertConfigurationOptionValues](docs/AutotaskTicketingAlertConfigurationOptionValues.md)
 - [AutotaskTicketingAlertConfigurationOptions](docs/AutotaskTicketingAlertConfigurationOptions.md)
 - [AutotaskTicketingAlertConfigurationPriority](docs/AutotaskTicketingAlertConfigurationPriority.md)
 - [AutotaskTicketingAlertConfigurationRequest](docs/AutotaskTicketingAlertConfigurationRequest.md)
 - [AutotaskTicketingAlertConfigurationResource](docs/AutotaskTicketingAlertConfigurationResource.md)
 - [BillingIntegrationCompanyType](docs/BillingIntegrationCompanyType.md)
 - [BulkScheduledStatechangeCreate](docs/BulkScheduledStatechangeCreate.md)
 - [BulkUserCreate](docs/BulkUserCreate.md)
 - [BulkUserUpdate](docs/BulkUserUpdate.md)
 - [CommandResultList](docs/CommandResultList.md)
 - [CommandResultListResults](docs/CommandResultListResults.md)
 - [ConnectWiseMappingRequest](docs/ConnectWiseMappingRequest.md)
 - [ConnectWiseMappingRequestCompany](docs/ConnectWiseMappingRequestCompany.md)
 - [ConnectWiseMappingRequestData](docs/ConnectWiseMappingRequestData.md)
 - [ConnectWiseMappingRequestOrganization](docs/ConnectWiseMappingRequestOrganization.md)
 - [ConnectWiseMappingResponse](docs/ConnectWiseMappingResponse.md)
 - [ConnectWiseMappingResponseAddition](docs/ConnectWiseMappingResponseAddition.md)
 - [ConnectWiseSettings](docs/ConnectWiseSettings.md)
 - [ConnectWiseSettingsPatchReq](docs/ConnectWiseSettingsPatchReq.md)
 - [ConnectWiseTicketingAlertConfiguration](docs/ConnectWiseTicketingAlertConfiguration.md)
 - [ConnectWiseTicketingAlertConfigurationList](docs/ConnectWiseTicketingAlertConfigurationList.md)
 - [ConnectWiseTicketingAlertConfigurationOption](docs/ConnectWiseTicketingAlertConfigurationOption.md)
 - [ConnectWiseTicketingAlertConfigurationOptions](docs/ConnectWiseTicketingAlertConfigurationOptions.md)
 - [ConnectWiseTicketingAlertConfigurationRequest](docs/ConnectWiseTicketingAlertConfigurationRequest.md)
 - [ConnectwiseAddition](docs/ConnectwiseAddition.md)
 - [ConnectwiseAgreement](docs/ConnectwiseAgreement.md)
 - [ConnectwiseCompany](docs/ConnectwiseCompany.md)
 - [ConnectwiseCompanyResp](docs/ConnectwiseCompanyResp.md)
 - [ConnectwiseCompanyTypeResp](docs/ConnectwiseCompanyTypeResp.md)
 - [ConnectwiseIntegration](docs/ConnectwiseIntegration.md)
 - [ConnectwiseIntegrationPatchReq](docs/ConnectwiseIntegrationPatchReq.md)
 - [ConnectwiseIntegrationReq](docs/ConnectwiseIntegrationReq.md)
 - [CustomEmail](docs/CustomEmail.md)
 - [CustomEmailTemplate](docs/CustomEmailTemplate.md)
 - [CustomEmailTemplateField](docs/CustomEmailTemplateField.md)
 - [CustomEmailType](docs/CustomEmailType.md)
 - [DEP](docs/DEP.md)
 - [DEPSetupAssistantOption](docs/DEPSetupAssistantOption.md)
 - [DEPWelcomeScreen](docs/DEPWelcomeScreen.md)
 - [DeviceIdEraseBody](docs/DeviceIdEraseBody.md)
 - [DeviceIdLockBody](docs/DeviceIdLockBody.md)
 - [DeviceIdRestartBody](docs/DeviceIdRestartBody.md)
 - [Directory](docs/Directory.md)
 - [DuoAccount](docs/DuoAccount.md)
 - [DuoApplication](docs/DuoApplication.md)
 - [DuoApplicationReq](docs/DuoApplicationReq.md)
 - [DuoApplicationUpdateReq](docs/DuoApplicationUpdateReq.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [Feature](docs/Feature.md)
 - [Filter](docs/Filter.md)
 - [FilterQuery](docs/FilterQuery.md)
 - [GSuiteBuiltinTranslation](docs/GSuiteBuiltinTranslation.md)
 - [GSuiteDirectionTranslation](docs/GSuiteDirectionTranslation.md)
 - [GSuiteTranslationRule](docs/GSuiteTranslationRule.md)
 - [GSuiteTranslationRuleRequest](docs/GSuiteTranslationRuleRequest.md)
 - [GraphAttributeLdapGroups](docs/GraphAttributeLdapGroups.md)
 - [GraphAttributePosixGroups](docs/GraphAttributePosixGroups.md)
 - [GraphAttributePosixGroupsPosixGroups](docs/GraphAttributePosixGroupsPosixGroups.md)
 - [GraphAttributeRadius](docs/GraphAttributeRadius.md)
 - [GraphAttributeRadiusRadius](docs/GraphAttributeRadiusRadius.md)
 - [GraphAttributeRadiusRadiusReply](docs/GraphAttributeRadiusRadiusReply.md)
 - [GraphAttributeSambaEnabled](docs/GraphAttributeSambaEnabled.md)
 - [GraphAttributeSudo](docs/GraphAttributeSudo.md)
 - [GraphAttributeSudoSudo](docs/GraphAttributeSudoSudo.md)
 - [GraphAttributes](docs/GraphAttributes.md)
 - [GraphConnection](docs/GraphConnection.md)
 - [GraphObject](docs/GraphObject.md)
 - [GraphObjectWithPaths](docs/GraphObjectWithPaths.md)
 - [GraphOperation](docs/GraphOperation.md)
 - [GraphOperationActiveDirectory](docs/GraphOperationActiveDirectory.md)
 - [GraphOperationApplication](docs/GraphOperationApplication.md)
 - [GraphOperationCommand](docs/GraphOperationCommand.md)
 - [GraphOperationGSuite](docs/GraphOperationGSuite.md)
 - [GraphOperationLdapServer](docs/GraphOperationLdapServer.md)
 - [GraphOperationOffice365](docs/GraphOperationOffice365.md)
 - [GraphOperationPolicy](docs/GraphOperationPolicy.md)
 - [GraphOperationPolicyGroup](docs/GraphOperationPolicyGroup.md)
 - [GraphOperationPolicyGroupMember](docs/GraphOperationPolicyGroupMember.md)
 - [GraphOperationRadiusServer](docs/GraphOperationRadiusServer.md)
 - [GraphOperationSoftwareApp](docs/GraphOperationSoftwareApp.md)
 - [GraphOperationSystem](docs/GraphOperationSystem.md)
 - [GraphOperationSystemGroup](docs/GraphOperationSystemGroup.md)
 - [GraphOperationSystemGroupMember](docs/GraphOperationSystemGroupMember.md)
 - [GraphOperationUser](docs/GraphOperationUser.md)
 - [GraphOperationUserGroup](docs/GraphOperationUserGroup.md)
 - [GraphOperationUserGroupMember](docs/GraphOperationUserGroupMember.md)
 - [GraphType](docs/GraphType.md)
 - [Group](docs/Group.md)
 - [GroupAttributesUserGroup](docs/GroupAttributesUserGroup.md)
 - [GroupIdSuggestionsBody](docs/GroupIdSuggestionsBody.md)
 - [GroupType](docs/GroupType.md)
 - [GsuiteOutput](docs/GsuiteOutput.md)
 - [GsuitePatchInput](docs/GsuitePatchInput.md)
 - [IPList](docs/IPList.md)
 - [IPListRequest](docs/IPListRequest.md)
 - [ImportUser](docs/ImportUser.md)
 - [ImportUserAddress](docs/ImportUserAddress.md)
 - [ImportUserPhoneNumber](docs/ImportUserPhoneNumber.md)
 - [ImportUsersResponse](docs/ImportUsersResponse.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20011Users](docs/InlineResponse20011Users.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2002Users](docs/InlineResponse2002Users.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [Integration](docs/Integration.md)
 - [IntegrationSyncError](docs/IntegrationSyncError.md)
 - [IntegrationSyncErrorResp](docs/IntegrationSyncErrorResp.md)
 - [IntegrationType](docs/IntegrationType.md)
 - [IntegrationsResponse](docs/IntegrationsResponse.md)
 - [JobId](docs/JobId.md)
 - [JobWorkresult](docs/JobWorkresult.md)
 - [LdapGroup](docs/LdapGroup.md)
 - [LdapServerAction](docs/LdapServerAction.md)
 - [LdapServerInput](docs/LdapServerInput.md)
 - [LdapServerOutput](docs/LdapServerOutput.md)
 - [LdapserversIdBody](docs/LdapserversIdBody.md)
 - [MemberSuggestion](docs/MemberSuggestion.md)
 - [MemberSuggestionsPostResult](docs/MemberSuggestionsPostResult.md)
 - [Mobileconfig](docs/Mobileconfig.md)
 - [OSRestriction](docs/OSRestriction.md)
 - [OSRestrictionAppleRestrictions](docs/OSRestrictionAppleRestrictions.md)
 - [Office365BuiltinTranslation](docs/Office365BuiltinTranslation.md)
 - [Office365DirectionTranslation](docs/Office365DirectionTranslation.md)
 - [Office365Output](docs/Office365Output.md)
 - [Office365PatchInput](docs/Office365PatchInput.md)
 - [Office365TranslationRule](docs/Office365TranslationRule.md)
 - [Office365TranslationRuleRequest](docs/Office365TranslationRuleRequest.md)
 - [Organization](docs/Organization.md)
 - [OrganizationCase](docs/OrganizationCase.md)
 - [OrganizationCasesResponse](docs/OrganizationCasesResponse.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [Policy](docs/Policy.md)
 - [PolicyGroup](docs/PolicyGroup.md)
 - [PolicyGroupData](docs/PolicyGroupData.md)
 - [PolicyRequest](docs/PolicyRequest.md)
 - [PolicyRequestTemplate](docs/PolicyRequestTemplate.md)
 - [PolicyResult](docs/PolicyResult.md)
 - [PolicyTemplate](docs/PolicyTemplate.md)
 - [PolicyTemplateConfigField](docs/PolicyTemplateConfigField.md)
 - [PolicyTemplateConfigFieldTooltip](docs/PolicyTemplateConfigFieldTooltip.md)
 - [PolicyTemplateConfigFieldTooltipVariables](docs/PolicyTemplateConfigFieldTooltipVariables.md)
 - [PolicyTemplateWithDetails](docs/PolicyTemplateWithDetails.md)
 - [PolicyValue](docs/PolicyValue.md)
 - [PolicyWithDetails](docs/PolicyWithDetails.md)
 - [Provider](docs/Provider.md)
 - [ProviderAdminReq](docs/ProviderAdminReq.md)
 - [ProviderInvoice](docs/ProviderInvoice.md)
 - [ProviderInvoiceResponse](docs/ProviderInvoiceResponse.md)
 - [PushEndpointResponse](docs/PushEndpointResponse.md)
 - [PushEndpointResponseDevice](docs/PushEndpointResponseDevice.md)
 - [PushendpointsPushEndpointIdBody](docs/PushendpointsPushEndpointIdBody.md)
 - [PwmAllUsers](docs/PwmAllUsers.md)
 - [PwmAllUsersGroups](docs/PwmAllUsersGroups.md)
 - [PwmAllUsersResults](docs/PwmAllUsersResults.md)
 - [PwmOverviewAppVersions](docs/PwmOverviewAppVersions.md)
 - [PwmOverviewAppVersionsResults](docs/PwmOverviewAppVersionsResults.md)
 - [PwmOverviewMain](docs/PwmOverviewMain.md)
 - [PwmOverviewMainDevices](docs/PwmOverviewMainDevices.md)
 - [Query](docs/Query.md)
 - [QueuedCommandList](docs/QueuedCommandList.md)
 - [QueuedCommandListResults](docs/QueuedCommandListResults.md)
 - [SambaDomainInput](docs/SambaDomainInput.md)
 - [SambaDomainOutput](docs/SambaDomainOutput.md)
 - [ScheduledUserstateResult](docs/ScheduledUserstateResult.md)
 - [SetupAssistantOption](docs/SetupAssistantOption.md)
 - [SharedFolderAccessLevels](docs/SharedFolderAccessLevels.md)
 - [SharedFolderAccessLevelsResults](docs/SharedFolderAccessLevelsResults.md)
 - [SharedFolderDetails](docs/SharedFolderDetails.md)
 - [SharedFolderUsers](docs/SharedFolderUsers.md)
 - [SharedFolderUsersResults](docs/SharedFolderUsersResults.md)
 - [SharedFoldersList](docs/SharedFoldersList.md)
 - [SharedFoldersListResults](docs/SharedFoldersListResults.md)
 - [SoftwareApp](docs/SoftwareApp.md)
 - [SoftwareAppAppleVpp](docs/SoftwareAppAppleVpp.md)
 - [SoftwareAppReclaimLicenses](docs/SoftwareAppReclaimLicenses.md)
 - [SoftwareAppSettings](docs/SoftwareAppSettings.md)
 - [SoftwareAppStatus](docs/SoftwareAppStatus.md)
 - [SoftwareAppWithStatus](docs/SoftwareAppWithStatus.md)
 - [SoftwareAppsRetryInstallationRequest](docs/SoftwareAppsRetryInstallationRequest.md)
 - [Subscription](docs/Subscription.md)
 - [SuggestionCounts](docs/SuggestionCounts.md)
 - [SystemGroup](docs/SystemGroup.md)
 - [SystemGroupData](docs/SystemGroupData.md)
 - [SystemInsightsAlf](docs/SystemInsightsAlf.md)
 - [SystemInsightsAlfExceptions](docs/SystemInsightsAlfExceptions.md)
 - [SystemInsightsAlfExplicitAuths](docs/SystemInsightsAlfExplicitAuths.md)
 - [SystemInsightsAppcompatShims](docs/SystemInsightsAppcompatShims.md)
 - [SystemInsightsApps](docs/SystemInsightsApps.md)
 - [SystemInsightsAuthorizedKeys](docs/SystemInsightsAuthorizedKeys.md)
 - [SystemInsightsAzureInstanceMetadata](docs/SystemInsightsAzureInstanceMetadata.md)
 - [SystemInsightsAzureInstanceTags](docs/SystemInsightsAzureInstanceTags.md)
 - [SystemInsightsBattery](docs/SystemInsightsBattery.md)
 - [SystemInsightsBitlockerInfo](docs/SystemInsightsBitlockerInfo.md)
 - [SystemInsightsBrowserPlugins](docs/SystemInsightsBrowserPlugins.md)
 - [SystemInsightsCertificates](docs/SystemInsightsCertificates.md)
 - [SystemInsightsChassisInfo](docs/SystemInsightsChassisInfo.md)
 - [SystemInsightsChromeExtensions](docs/SystemInsightsChromeExtensions.md)
 - [SystemInsightsConnectivity](docs/SystemInsightsConnectivity.md)
 - [SystemInsightsCrashes](docs/SystemInsightsCrashes.md)
 - [SystemInsightsCupsDestinations](docs/SystemInsightsCupsDestinations.md)
 - [SystemInsightsDiskEncryption](docs/SystemInsightsDiskEncryption.md)
 - [SystemInsightsDiskInfo](docs/SystemInsightsDiskInfo.md)
 - [SystemInsightsDnsResolvers](docs/SystemInsightsDnsResolvers.md)
 - [SystemInsightsEtcHosts](docs/SystemInsightsEtcHosts.md)
 - [SystemInsightsFirefoxAddons](docs/SystemInsightsFirefoxAddons.md)
 - [SystemInsightsGroups](docs/SystemInsightsGroups.md)
 - [SystemInsightsIeExtensions](docs/SystemInsightsIeExtensions.md)
 - [SystemInsightsInterfaceAddresses](docs/SystemInsightsInterfaceAddresses.md)
 - [SystemInsightsInterfaceDetails](docs/SystemInsightsInterfaceDetails.md)
 - [SystemInsightsKernelInfo](docs/SystemInsightsKernelInfo.md)
 - [SystemInsightsLaunchd](docs/SystemInsightsLaunchd.md)
 - [SystemInsightsLinuxPackages](docs/SystemInsightsLinuxPackages.md)
 - [SystemInsightsLoggedInUsers](docs/SystemInsightsLoggedInUsers.md)
 - [SystemInsightsLogicalDrives](docs/SystemInsightsLogicalDrives.md)
 - [SystemInsightsManagedPolicies](docs/SystemInsightsManagedPolicies.md)
 - [SystemInsightsMounts](docs/SystemInsightsMounts.md)
 - [SystemInsightsOsVersion](docs/SystemInsightsOsVersion.md)
 - [SystemInsightsPatches](docs/SystemInsightsPatches.md)
 - [SystemInsightsPrograms](docs/SystemInsightsPrograms.md)
 - [SystemInsightsPythonPackages](docs/SystemInsightsPythonPackages.md)
 - [SystemInsightsSafariExtensions](docs/SystemInsightsSafariExtensions.md)
 - [SystemInsightsScheduledTasks](docs/SystemInsightsScheduledTasks.md)
 - [SystemInsightsSecureboot](docs/SystemInsightsSecureboot.md)
 - [SystemInsightsServices](docs/SystemInsightsServices.md)
 - [SystemInsightsShadow](docs/SystemInsightsShadow.md)
 - [SystemInsightsSharedFolders](docs/SystemInsightsSharedFolders.md)
 - [SystemInsightsSharedResources](docs/SystemInsightsSharedResources.md)
 - [SystemInsightsSharingPreferences](docs/SystemInsightsSharingPreferences.md)
 - [SystemInsightsSipConfig](docs/SystemInsightsSipConfig.md)
 - [SystemInsightsStartupItems](docs/SystemInsightsStartupItems.md)
 - [SystemInsightsSystemControls](docs/SystemInsightsSystemControls.md)
 - [SystemInsightsSystemInfo](docs/SystemInsightsSystemInfo.md)
 - [SystemInsightsTpmInfo](docs/SystemInsightsTpmInfo.md)
 - [SystemInsightsUptime](docs/SystemInsightsUptime.md)
 - [SystemInsightsUsbDevices](docs/SystemInsightsUsbDevices.md)
 - [SystemInsightsUserGroups](docs/SystemInsightsUserGroups.md)
 - [SystemInsightsUserSshKeys](docs/SystemInsightsUserSshKeys.md)
 - [SystemInsightsUserassist](docs/SystemInsightsUserassist.md)
 - [SystemInsightsUsers](docs/SystemInsightsUsers.md)
 - [SystemInsightsWifiNetworks](docs/SystemInsightsWifiNetworks.md)
 - [SystemInsightsWifiStatus](docs/SystemInsightsWifiStatus.md)
 - [SystemInsightsWindowsSecurityCenter](docs/SystemInsightsWindowsSecurityCenter.md)
 - [SystemInsightsWindowsSecurityProducts](docs/SystemInsightsWindowsSecurityProducts.md)
 - [Systemfdekey](docs/Systemfdekey.md)
 - [TicketingIntegrationAlert](docs/TicketingIntegrationAlert.md)
 - [TicketingIntegrationAlertsResp](docs/TicketingIntegrationAlertsResp.md)
 - [User](docs/User.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserGroupPost](docs/UserGroupPost.md)
 - [UserGroupPut](docs/UserGroupPut.md)
 - [WorkdayFields](docs/WorkdayFields.md)
 - [WorkdayInput](docs/WorkdayInput.md)
 - [WorkdayOutput](docs/WorkdayOutput.md)
 - [WorkdayWorker](docs/WorkdayWorker.md)
 - [WorkdayoutputAuth](docs/WorkdayoutputAuth.md)

## Documentation For Authorization


## x-api-key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author

support@jumpcloud.com
