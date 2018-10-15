## JCAPI-Python

### Description

This repository contains the Python client code for the JumpCloud API v1 and
v2. It also provides the tools to generate the client code from the API YAML
files, using Swagger Codegen. For detailed instructions on how to generate the
code, see the [Contributing](CONTRIBUTING.md) section.

### Installing the Python Client

You can run the following `pip` commands in order to install the packages
directly from GitHub:

```
pip install git+https://github.com/TheJumpCloud/jcapi-python.git#subdirectory=jcapiv1
pip install git+https://github.com/TheJumpCloud/jcapi-python.git#subdirectory=jcapiv2
```

Alternatively you can also pull this repository and install manually. Change to
the appropriate directory (jcapiv1 or jcapiv2) and then run one of the
following commands.

To install the package for the local user:

```
$ python setup.py install --user
```

To install the package for all users:

```
$ sudo python setup.py install
```

### Authentication and Authorization

All endpoints support authentication via API key: see the
[Authentication & Authorization](https://docs.jumpcloud.com/2.0/authentication-and-authorization/authentication-and-authorization-overview)
section in our API documentation.

Some systems endpoints (in both API v1 and v2) also support
[System Context Authorization](https://docs.jumpcloud.com/2.0/authentication-and-authorization/system-context)
which allows an individual system to manage its information and resource
associations.

### Usage Examples

For more detailed instructions, refer to each API version's respective README
file ([README for API v1](jcapiv1/README.md) and
[README for API v2](jcapiv2/README.md)) and the generated documentation under
each folder.

#### API v1 Example

```python
"""JumpCloud API v1 example."""

import jcapiv1
from jcapiv1.rest import ApiException

API_KEY = "YOUR_API_KEY"
SYSTEM_USER_ID = "YOUR_SYSTEM_USER_ID"
SYSTEM_USER_EMAIL = "YOUR_SYSTEM_USER_EMAIL"
SYSTEM_USER_USERNAME = "YOUR_SYSTEM_USER_USERNAME"

CONTENT_TYPE = "application/json"
ACCEPT = "application/json"

# Set up the configuration object with your API key for authorization
CONFIGURATION = jcapiv1.Configuration()
CONFIGURATION.api_key['x-api-key'] = API_KEY

# Instantiate the API object for the group of endpoints you need to use,
# for instance the system users API
API_INSTANCE = jcapiv1.SystemusersApi(jcapiv1.ApiClient(CONFIGURATION))

def list_users():
    """Make an API call to retrieve all system users."""
    try:
        users = API_INSTANCE.systemusers_list(CONTENT_TYPE, ACCEPT)
        print(users)
    except ApiException as err:
        print("Exception when calling SystemusersApi->systemusers_list: %s\n" % err)

def update_user():
    """Make an API call to update a system user."""
    put_request = jcapiv1.Systemuserputpost(email=SYSTEM_USER_EMAIL, username=SYSTEM_USER_USERNAME)
    put_request.lastname = "Updated Last Name"

    try:
        user = API_INSTANCE.systemusers_put(SYSTEM_USER_ID, CONTENT_TYPE, ACCEPT, body=put_request)
        print(user)
    except ApiException as err:
        print("Exception when calling SystemusersApi->systemusers_put: %s\n" % err)

if __name__ == "__main__":
    list_users()
    update_user()

```

#### API v2 Example

```python
"""JumpCloud API v2 example."""

import jcapiv2
from jcapiv2.rest import ApiException

API_KEY = "YOUR_API_KEY"

CONTENT_TYPE = "application/json"
ACCEPT = "application/json"

# Set up the configuration object with your API key for authorization
CONFIGURATION = jcapiv2.Configuration()
CONFIGURATION.api_key['x-api-key'] = API_KEY

# Instantiate the API object for the group of endpoints you need to use,
# for instance the user groups API
API_INSTANCE = jcapiv2.UserGroupsApi(jcapiv2.ApiClient(CONFIGURATION))

def get_user_groups():
    """Make an API call to retrieve all user groups."""
    try:
        user_groups = API_INSTANCE.groups_user_list(CONTENT_TYPE, ACCEPT)
        print(user_groups)
    except ApiException as err:
        print("Exception when calling UserGroupsApi->groups_user_list: %s\n" % err)

if __name__ == "__main__":
    get_user_groups()

```

#### System Context Authorization Example

```python
"""JumpCloud system context authorization example."""

import jcapiv2
from jcapiv2.rest import ApiException

# Set headers for System Context Authorization. For detailed instructions on
# how to generate these headers, refer to:
# https://docs.jumpcloud.com/2.0/authentication-and-authorization/system-context
SYSTEM_ID = "YOUR_SYSTEM_ID"
# The current date on the system, e.g. "Thu, 09 Aug 1990 14:25:15 GMT"
SYSTEM_DATE = "YOUR_SYSTEM_DATE"
SYSTEM_SIGNATURE = "YOUR_SYSTEM_SIGNATURE"
SYSTEM_CONTEXT_AUTH = (
    'Signature keyId="system/{}",'
    'headers="request-line date",'
    'algorithm="rsa-sha256",'
    'signature="{}"'
).format(SYSTEM_ID, SYSTEM_SIGNATURE)

CONTENT_TYPE = "application/json"
ACCEPT = "application/json"

# Set up the configuration object
CONFIGURATION = jcapiv2.Configuration()

# Instantiate the API object for the group of endpoints you need to use,
# for instance the systems API
API_INSTANCE = jcapiv2.SystemsApi(jcapiv2.ApiClient(CONFIGURATION))

def get_system_groups():
    """Make an API call to retrieve all system groups this system is a member of."""
    try:
        # Note the System Context Authorization headers are passed as arguments
        system_groups = API_INSTANCE.graph_system_member_of(
            SYSTEM_ID, CONTENT_TYPE, ACCEPT,
            date=SYSTEM_DATE, authorization=SYSTEM_CONTEXT_AUTH,
        )
        print(system_groups)
    except ApiException as err:
        print("Exception when calling systemsAPI->graph_system_member_of: %s\n" % err)

if __name__ == "__main__":
    get_system_groups()

```
