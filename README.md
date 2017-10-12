## JCAPI-Python

### Description ###

This repository contains the Python client code for the JumpCloud API v1 and v2.
It also provides the tools to generate the client code from the API yaml files, using swagger-codegen.
For detailed instructions on how to generate the code, see the [Contributing](CONTRIBUTING.md) section.

#### Installing the Python Client

Change to the appropriate directory (jcapiv1 or jcapiv2) and then run the following command to install the Python Client API package:

To install the package for the local user:
```
$ python setup.py install --user
```
To install the package for all users:
```
sudo python setup.py install
```

#### Usage Examples

For more detailed instructions, refer to each API's respective README file ([README for API v1](jcapiv1/README.md) and [README for API v2](jcapiv2/README.md)) and the generated docs under each folder.

API v1 example:
```
import jcapiv1

...
content_type = 'application/json'
accept = 'application/json'

# set up the configuration object with your API key:
jcapiv1.configuration.api_key['x-api-key'] = '<YOUR_API_KEY>'

# instantiate the API object for the group of endpoints you need to use
# for instance for Systemusers API:
systemusersAPI = jcapiv1.SystemusersApi()

try:
    # make an API call to retrieve all systemusers:
    users = systemusersAPI.systemusers_list(content_type, accept)
except ApiException as e:
    print("Exception when calling SystemusersApi->systemusers_list: %s\n" % e)

try:
    # make an API call to modify a specific user's last name:
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

# set up the configuration object with your API key:
jcapiv2.configuration.api_key['x-api-key'] = '<YOUR_API_KEY>'

# instantiate the API object for the group of endpoints you need to use
# for instance for User Groups API:
userGroupsAPI = jcapiv2.UserGroupsApi()

try:
    # make an API call to retrieve a specific user group:
    userGroup = userGroupsAPI.groups_user_get(group_id, content_type, accept)
except ApiException as e:
    print("Exception when calling UserGroupsApi->groups_user_get: %s\n" % e)

```
