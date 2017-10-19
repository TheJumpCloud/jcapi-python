## JCAPI-Python

### Description ###

This repository contains the Python client code for the JumpCloud API v1 and v2.
It also provides the tools to generate the client code from the API yaml files, using swagger-codegen.
For detailed instructions on how to generate the code, see the [Contributing](CONTRIBUTING.md) section.

#### Installing the Python Client

You can run the following pip commands in order to install the packages directly from Github:
```
pip install git+https://github.com/TheJumpCloud/jcapi-python.git#subdirectory=jcapiv1
pip install git+https://github.com/TheJumpCloud/jcapi-python.git#subdirectory=jcapiv2
```

Alternatively you can also pull this repository and install manually:
Change to the appropriate directory (jcapiv1 or jcapiv2) and then run the following command:

To install the package for the local user:
```
$ python setup.py install --user
```
To install the package for all users:
```
$ sudo python setup.py install
```

#### Authentication and Authorization

All endpoints support authentication via API key: see the [Authentication and Authorization](https://docs.jumpcloud.com/2.0/authentication-and-authorization/authentication-and-authorization-overview) section in our API docs.

Some Systems endpoints (in both API v1 and v2) also support the System Context authorization which allows an individual system to manage its information and resource associations.
More more information on System Context Authorization, please refer to the [System Context](https://docs.jumpcloud.com/2.0/authentication-and-authorization/system-context) section in our API docs.

#### Usage Examples

For more detailed instructions, refer to each API's respective README file ([README for API v1](jcapiv1/README.md) and [README for API v2](jcapiv2/README.md)) and the generated docs under each folder.

API v1 example:
```python
import jcapiv1
from jcapiv1.rest import ApiException

...
content_type = 'application/json'
accept = 'application/json'

# set up the configuration object with your API key for authorization:
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
```python
import jcapiv2
from jcapiv2.rest import ApiException

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

System Context Authorization example:
```python
import jcapiv2
from jcapiv2.rest import ApiException

content_type = 'application/json'
accept = 'application/json'
system_id = '<YOUR_SYSTEM_ID>'

# set headers for the System Context Authorization:
# for detailed instructions on how to generate these headers,
# refer to: https://docs.jumpcloud.com/2.0/authentication-and-authorization/system-context
sys_context_auth = 'Signature keyId="system/<YOUR_SYSTEM_ID>",headers="request-line date",algorithm="rsa-sha256",signature="<YOUR_SYSTEM_SIGNATURE>"'
sys_context_date = 'Thu, 19 Oct 2017 17:27:57 GMT' # the current date on the system

# instantiate the API object for the group of endpoints you need to use
# for instance for User Groups API:
systemsAPI = jcapiv2.SystemsApi()

try:
    # list the system groups this system is a member of:
    # Note that we pass the System Context Authorization headers as the 'date' and 'authorization' parameters
    groups = systemsAPI.graph_system_member_of(system_id, content_type, accept, date=sys_context_date, authorization=sys_context_auth)
    print groups
except ApiException as e:
    print("Exception when calling systemsAPI->graph_system_member_of: %s\n" % e)
```
