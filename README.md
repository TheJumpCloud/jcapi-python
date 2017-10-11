## JCAPI-Python

### Description ###

This repository contains the Python client code for the JumpCloud API v1 and v2.
It also provides the tools to generate the client code from the API yaml files, using swagger-codegen.
It relies on the following docker file in order to run swagger-codegen inside a docker container:
https://hub.docker.com/r/jimschubert/swagger-codegen-cli/

We're currently using the version 2.2.2 of swagger-codegen.

Note that there is now an official swagger Docker file for the swagger-codegen-cli but it seems to only be supporting the latest version of swagger-codegen (2.3.0, which generates a completely different API interface from 2.2.2).
This docker file can be found here: https://hub.docker.com/r/swaggerapi/swagger-codegen-cli/
We might want to consider using this Docker file once it supports different versions of swagger-codegen.

### Generating the API Client

Copy the API yaml files to the local `/input` directory.

The API v1 yaml file can be found here: `https://github.com/TheJumpCloud/SI/blob/master/routes/webui/api/index.yaml`

The API v2 yaml file can be found here: `https://github.com/TheJumpCloud/SI/blob/master/routes/webui/api/v2/index.yaml`

To generate the API v1 client, run the command below (assuming your API v1 yaml file is `input/index1.yaml`):  

```
$ docker-compose run --rm swagger-codegen generate -i /swagger-api/yaml/index1.yaml -l python -c /config/config_v1.json -o /swagger-api/out/jcapiv1
```
This will generate the API v1 client files under `output/jcapiv1`

To generate the API v2 client, run the command below (assuming your API v2 yaml file is `input/index2.yaml`):  

```
$ docker-compose run --rm swagger-codegen generate -i /swagger-api/yaml/index2.yaml -l python -c /config/config_v2.json -o /swagger-api/out/jcapiv2
```
This will generate the API v1 client files under `output/jcapiv1`

Once you are satisfied with the generated API client, you can replace the existing files under the `jcapiv1` and `jcapiv2` folders with your generated files.


#### Installing the Python Client

Change to the appropriate directory (jcapiv1 or jcapiv2) and then run the following command to install the Python Client API locally:

```
$ python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

#### Usage Examples

API v1 example:
```
import jcapiv1

...
content_type = 'application/json'
accept = 'application/json'

// set up the configuration object with your API key:
jcapiv1.configuration.api_key['x-api-key'] = '<YOUR_API_KEY>'

// instantiate the API object for the group of endpoints you need to use
// for instance for Systemusers API:
systemusersAPI = jcapiv1.SystemusersApi()

try:
    // make an API call to retrieve all systemusers:
    users = systemusersAPI.systemusers_list(content_type, accept)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_list: %s\n" % e)

try:
    // make an API call to modify a specific user's last name:
    put_request = jcapiv1.Systemuserputpost()
    put_request.lastname = 'Updated Last Name'
    systemusersAPI.systemusers_put('<YOUR_SYSTEMUSER_ID>', content_type, accept, body=put_request)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_put: %s\n" % e)
```

API v2 example:
```
import jcapiv2

...
content_type = 'application/json'
accept = 'application/json'
group_id = '<YOUR_GROUP_ID>'

// set up the configuration object with your API key:
jcapiv2.configuration.api_key['x-api-key'] = '<YOUR_API_KEY>'

// instantiate the API object for the group of endpoints you need to use
// for instance for User Groups API:
userGroupsAPI = jcapiv2.UserGroupsApi()

try:
    // make an API call to retrieve a specific user group:
    userGroup = userGroupsAPI.groups_user_get(group_id, content_type, accept)
except ApiException as e:
    print("Exception when calling UserGroupsApi->groups_user_get: %s\n" % e)

```
