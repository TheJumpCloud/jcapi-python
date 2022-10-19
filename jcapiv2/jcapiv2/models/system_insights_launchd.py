# coding: utf-8

"""
    JumpCloud API

    # Overview  JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # Directory Objects  This API offers the ability to interact with some of our core features; otherwise known as Directory Objects. The Directory Objects are:  * Commands * Policies * Policy Groups * Applications * Systems * Users * User Groups * System Groups * Radius Servers * Directories: Office 365, LDAP,G-Suite, Active Directory * Duo accounts and applications.  The Directory Object is an important concept to understand in order to successfully use JumpCloud API.  ## JumpCloud Graph  We've also introduced the concept of the JumpCloud Graph along with  Directory Objects. The Graph is a powerful aspect of our platform which will enable you to associate objects with each other, or establish membership for certain objects to become members of other objects.  Specific `GET` endpoints will allow you to traverse the JumpCloud Graph to return all indirect and directly bound objects in your organization.  | ![alt text](https://s3.amazonaws.com/jumpcloud-kb/Knowledge+Base+Photos/API+Docs/jumpcloud_graph.png \"JumpCloud Graph Model Example\") | |:--:| | **This diagram highlights our association and membership model as it relates to Directory Objects.** |  # API Key  ## Access Your API Key  To locate your API Key:  1. Log into the [JumpCloud Admin Console](https://console.jumpcloud.com/). 2. Go to the username drop down located in the top-right of the Console. 3. Retrieve your API key from API Settings.  ## API Key Considerations  This API key is associated to the currently logged in administrator. Other admins will have different API keys.  **WARNING** Please keep this API key secret, as it grants full access to any data accessible via your JumpCloud console account.  You can also reset your API key in the same location in the JumpCloud Admin Console.  ## Recycling or Resetting Your API Key  In order to revoke access with the current API key, simply reset your API key. This will render all calls using the previous API key inaccessible.  Your API key will be passed in as a header with the header name \"x-api-key\".  ```bash curl -H \"x-api-key: [YOUR_API_KEY_HERE]\" \"https://console.jumpcloud.com/api/v2/systemgroups\" ```  # System Context  * [Introduction](#introduction) * [Supported endpoints](#supported-endpoints) * [Response codes](#response-codes) * [Authentication](#authentication) * [Additional examples](#additional-examples) * [Third party](#third-party)  ## Introduction  JumpCloud System Context Authorization is an alternative way to authenticate with a subset of JumpCloud's REST APIs. Using this method, a system can manage its information and resource associations, allowing modern auto provisioning environments to scale as needed.  **Notes:**   * The following documentation applies to Linux Operating Systems only.  * Systems that have been automatically enrolled using Apple's Device Enrollment Program (DEP) or systems enrolled using the User Portal install are not eligible to use the System Context API to prevent unauthorized access to system groups and resources. If a script that utilizes the System Context API is invoked on a system enrolled in this way, it will display an error.  ## Supported Endpoints  JumpCloud System Context Authorization can be used in conjunction with Systems endpoints found in the V1 API and certain System Group endpoints found in the v2 API.  * A system may fetch, alter, and delete metadata about itself, including manipulating a system's Group and Systemuser associations,   * `/api/systems/{system_id}` | [`GET`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_get) [`PUT`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_put) * A system may delete itself from your JumpCloud organization   * `/api/systems/{system_id}` | [`DELETE`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_delete) * A system may fetch its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/memberof` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembership)   * `/api/v2/systems/{system_id}/associations` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsList)   * `/api/v2/systems/{system_id}/users` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemTraverseUser) * A system may alter its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/associations` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsPost) * A system may alter its System Group associations   * `/api/v2/systemgroups/{group_id}/members` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembersPost)     * _NOTE_ If a system attempts to alter the system group membership of a different system the request will be rejected  ## Response Codes  If endpoints other than those described above are called using the System Context API, the server will return a `401` response.  ## Authentication  To allow for secure access to our APIs, you must authenticate each API request. JumpCloud System Context Authorization uses [HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures-00) to authenticate API requests. The HTTP Signatures sent with each request are similar to the signatures used by the Amazon Web Services REST API. To help with the request-signing process, we have provided an [example bash script](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh). This example API request simply requests the entire system record. You must be root, or have permissions to access the contents of the `/opt/jc` directory to generate a signature.  Here is a breakdown of the example script with explanations.  First, the script extracts the systemKey from the JSON formatted `/opt/jc/jcagent.conf` file.  ```bash #!/bin/bash conf=\"`cat /opt/jc/jcagent.conf`\" regex=\"systemKey\\\":\\\"(\\w+)\\\"\"  if [[ $conf =~ $regex ]] ; then   systemKey=\"${BASH_REMATCH[1]}\" fi ```  Then, the script retrieves the current date in the correct format.  ```bash now=`date -u \"+%a, %d %h %Y %H:%M:%S GMT\"`; ```  Next, we build a signing string to demonstrate the expected signature format. The signed string must consist of the [request-line](https://tools.ietf.org/html/rfc2616#page-35) and the date header, separated by a newline character.  ```bash signstr=\"GET /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" ```  The next step is to calculate and apply the signature. This is a two-step process:  1. Create a signature from the signing string using the JumpCloud Agent private key: ``printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key`` 2. Then Base64-encode the signature string and trim off the newline characters: ``| openssl enc -e -a | tr -d '\\n'``  The combined steps above result in:  ```bash signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ; ```  Finally, we make sure the API call sending the signature has the same Authorization and Date header values, HTTP method, and URL that were used in the signing string.  ```bash curl -iq \\   -H \"Accept: application/json\" \\   -H \"Content-Type: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Input Data  All PUT and POST methods should use the HTTP Content-Type header with a value of 'application/json'. PUT methods are used for updating a record. POST methods are used to create a record.  The following example demonstrates how to update the `displayName` of the system.  ```bash signstr=\"PUT /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ;  curl -iq \\   -d \"{\\\"displayName\\\" : \\\"updated-system-name-1\\\"}\" \\   -X \"PUT\" \\   -H \"Content-Type: application/json\" \\   -H \"Accept: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Output Data  All results will be formatted as JSON.  Here is an abbreviated example of response output:  ```json {   \"_id\": \"525ee96f52e144993e000015\",   \"agentServer\": \"lappy386\",   \"agentVersion\": \"0.9.42\",   \"arch\": \"x86_64\",   \"connectionKey\": \"127.0.0.1_51812\",   \"displayName\": \"ubuntu-1204\",   \"firstContact\": \"2013-10-16T19:30:55.611Z\",   \"hostname\": \"ubuntu-1204\"   ... ```  ## Additional Examples  ### Signing Authentication Example  This example demonstrates how to make an authenticated request to fetch the JumpCloud record for this system.  [SigningExample.sh](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh)  ### Shutdown Hook  This example demonstrates how to make an authenticated request on system shutdown. Using an init.d script registered at run level 0, you can call the System Context API as the system is shutting down.  [Instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) is an example of an init.d script that only runs at system shutdown.  After customizing the [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) script, you should install it on the system(s) running the JumpCloud agent.  1. Copy the modified [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) to `/etc/init.d/instance-shutdown`. 2. On Ubuntu systems, run `update-rc.d instance-shutdown defaults`. On RedHat/CentOS systems, run `chkconfig --add instance-shutdown`.  ## Third Party  ### Chef Cookbooks  [https://github.com/nshenry03/jumpcloud](https://github.com/nshenry03/jumpcloud)  [https://github.com/cjs226/jumpcloud](https://github.com/cjs226/jumpcloud)  # Multi-Tenant Portal Headers  Multi-Tenant Organization API Headers are available for JumpCloud Admins to use when making API requests from Organizations that have multiple managed organizations.  The `x-org-id` is a required header for all multi-tenant admins when making API requests to JumpCloud. This header will define to which organization you would like to make the request.  **NOTE** Single Tenant Admins do not need to provide this header when making an API request.  ## Header Value  `x-org-id`  ## API Response Codes  * `400` Malformed ID. * `400` x-org-id and Organization path ID do not match. * `401` ID not included for multi-tenant admin * `403` ID included on unsupported route. * `404` Organization ID Not Found.  ```bash curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -H 'x-org-id: {ORG_ID}'  ```  ## To Obtain an Individual Organization ID via the UI  As a prerequisite, your Primary Organization will need to be setup for Multi-Tenancy. This provides access to the Multi-Tenant Organization Admin Portal.  1. Log into JumpCloud [Admin Console](https://console.jumpcloud.com). If you are a multi-tenant Admin, you will automatically be routed to the Multi-Tenant Admin Portal. 2. From the Multi-Tenant Portal's primary navigation bar, select the Organization you'd like to access. 3. You will automatically be routed to that Organization's Admin Console. 4. Go to Settings in the sub-tenant's primary navigation. 5. You can obtain your Organization ID below your Organization's Contact Information on the Settings page.  ## To Obtain All Organization IDs via the API  * You can make an API request to this endpoint using the API key of your Primary Organization.  `https://console.jumpcloud.com/api/organizations/` This will return all your managed organizations.  ```bash curl -X GET \\   https://console.jumpcloud.com/api/organizations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # SDKs  You can find language specific SDKs that can help you kickstart your Integration with JumpCloud in the following GitHub repositories:  * [Python](https://github.com/TheJumpCloud/jcapi-python) * [Go](https://github.com/TheJumpCloud/jcapi-go) * [Ruby](https://github.com/TheJumpCloud/jcapi-ruby) * [Java](https://github.com/TheJumpCloud/jcapi-java)   # noqa: E501

    OpenAPI spec version: 2.0
    Contact: support@jumpcloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInsightsLaunchd(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'collection_time': 'str',
        'disabled': 'str',
        'groupname': 'str',
        'inetd_compatibility': 'str',
        'keep_alive': 'str',
        'label': 'str',
        'name': 'str',
        'on_demand': 'str',
        'path': 'str',
        'process_type': 'str',
        'program': 'str',
        'program_arguments': 'str',
        'queue_directories': 'str',
        'root_directory': 'str',
        'run_at_load': 'str',
        'start_interval': 'str',
        'start_on_mount': 'str',
        'stderr_path': 'str',
        'stdout_path': 'str',
        'system_id': 'str',
        'username': 'str',
        'watch_paths': 'str',
        'working_directory': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'disabled': 'disabled',
        'groupname': 'groupname',
        'inetd_compatibility': 'inetd_compatibility',
        'keep_alive': 'keep_alive',
        'label': 'label',
        'name': 'name',
        'on_demand': 'on_demand',
        'path': 'path',
        'process_type': 'process_type',
        'program': 'program',
        'program_arguments': 'program_arguments',
        'queue_directories': 'queue_directories',
        'root_directory': 'root_directory',
        'run_at_load': 'run_at_load',
        'start_interval': 'start_interval',
        'start_on_mount': 'start_on_mount',
        'stderr_path': 'stderr_path',
        'stdout_path': 'stdout_path',
        'system_id': 'system_id',
        'username': 'username',
        'watch_paths': 'watch_paths',
        'working_directory': 'working_directory'
    }

    def __init__(self, collection_time=None, disabled=None, groupname=None, inetd_compatibility=None, keep_alive=None, label=None, name=None, on_demand=None, path=None, process_type=None, program=None, program_arguments=None, queue_directories=None, root_directory=None, run_at_load=None, start_interval=None, start_on_mount=None, stderr_path=None, stdout_path=None, system_id=None, username=None, watch_paths=None, working_directory=None):  # noqa: E501
        """SystemInsightsLaunchd - a model defined in Swagger"""  # noqa: E501
        self._collection_time = None
        self._disabled = None
        self._groupname = None
        self._inetd_compatibility = None
        self._keep_alive = None
        self._label = None
        self._name = None
        self._on_demand = None
        self._path = None
        self._process_type = None
        self._program = None
        self._program_arguments = None
        self._queue_directories = None
        self._root_directory = None
        self._run_at_load = None
        self._start_interval = None
        self._start_on_mount = None
        self._stderr_path = None
        self._stdout_path = None
        self._system_id = None
        self._username = None
        self._watch_paths = None
        self._working_directory = None
        self.discriminator = None
        if collection_time is not None:
            self.collection_time = collection_time
        if disabled is not None:
            self.disabled = disabled
        if groupname is not None:
            self.groupname = groupname
        if inetd_compatibility is not None:
            self.inetd_compatibility = inetd_compatibility
        if keep_alive is not None:
            self.keep_alive = keep_alive
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if on_demand is not None:
            self.on_demand = on_demand
        if path is not None:
            self.path = path
        if process_type is not None:
            self.process_type = process_type
        if program is not None:
            self.program = program
        if program_arguments is not None:
            self.program_arguments = program_arguments
        if queue_directories is not None:
            self.queue_directories = queue_directories
        if root_directory is not None:
            self.root_directory = root_directory
        if run_at_load is not None:
            self.run_at_load = run_at_load
        if start_interval is not None:
            self.start_interval = start_interval
        if start_on_mount is not None:
            self.start_on_mount = start_on_mount
        if stderr_path is not None:
            self.stderr_path = stderr_path
        if stdout_path is not None:
            self.stdout_path = stdout_path
        if system_id is not None:
            self.system_id = system_id
        if username is not None:
            self.username = username
        if watch_paths is not None:
            self.watch_paths = watch_paths
        if working_directory is not None:
            self.working_directory = working_directory

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsLaunchd.  # noqa: E501


        :return: The collection_time of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsLaunchd.


        :param collection_time: The collection_time of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def disabled(self):
        """Gets the disabled of this SystemInsightsLaunchd.  # noqa: E501


        :return: The disabled of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SystemInsightsLaunchd.


        :param disabled: The disabled of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._disabled = disabled

    @property
    def groupname(self):
        """Gets the groupname of this SystemInsightsLaunchd.  # noqa: E501


        :return: The groupname of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this SystemInsightsLaunchd.


        :param groupname: The groupname of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._groupname = groupname

    @property
    def inetd_compatibility(self):
        """Gets the inetd_compatibility of this SystemInsightsLaunchd.  # noqa: E501


        :return: The inetd_compatibility of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._inetd_compatibility

    @inetd_compatibility.setter
    def inetd_compatibility(self, inetd_compatibility):
        """Sets the inetd_compatibility of this SystemInsightsLaunchd.


        :param inetd_compatibility: The inetd_compatibility of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._inetd_compatibility = inetd_compatibility

    @property
    def keep_alive(self):
        """Gets the keep_alive of this SystemInsightsLaunchd.  # noqa: E501


        :return: The keep_alive of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        """Sets the keep_alive of this SystemInsightsLaunchd.


        :param keep_alive: The keep_alive of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._keep_alive = keep_alive

    @property
    def label(self):
        """Gets the label of this SystemInsightsLaunchd.  # noqa: E501


        :return: The label of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SystemInsightsLaunchd.


        :param label: The label of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this SystemInsightsLaunchd.  # noqa: E501


        :return: The name of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsLaunchd.


        :param name: The name of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def on_demand(self):
        """Gets the on_demand of this SystemInsightsLaunchd.  # noqa: E501


        :return: The on_demand of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._on_demand

    @on_demand.setter
    def on_demand(self, on_demand):
        """Sets the on_demand of this SystemInsightsLaunchd.


        :param on_demand: The on_demand of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._on_demand = on_demand

    @property
    def path(self):
        """Gets the path of this SystemInsightsLaunchd.  # noqa: E501


        :return: The path of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsLaunchd.


        :param path: The path of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def process_type(self):
        """Gets the process_type of this SystemInsightsLaunchd.  # noqa: E501


        :return: The process_type of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        """Sets the process_type of this SystemInsightsLaunchd.


        :param process_type: The process_type of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._process_type = process_type

    @property
    def program(self):
        """Gets the program of this SystemInsightsLaunchd.  # noqa: E501


        :return: The program of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this SystemInsightsLaunchd.


        :param program: The program of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._program = program

    @property
    def program_arguments(self):
        """Gets the program_arguments of this SystemInsightsLaunchd.  # noqa: E501


        :return: The program_arguments of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._program_arguments

    @program_arguments.setter
    def program_arguments(self, program_arguments):
        """Sets the program_arguments of this SystemInsightsLaunchd.


        :param program_arguments: The program_arguments of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._program_arguments = program_arguments

    @property
    def queue_directories(self):
        """Gets the queue_directories of this SystemInsightsLaunchd.  # noqa: E501


        :return: The queue_directories of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._queue_directories

    @queue_directories.setter
    def queue_directories(self, queue_directories):
        """Sets the queue_directories of this SystemInsightsLaunchd.


        :param queue_directories: The queue_directories of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._queue_directories = queue_directories

    @property
    def root_directory(self):
        """Gets the root_directory of this SystemInsightsLaunchd.  # noqa: E501


        :return: The root_directory of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._root_directory

    @root_directory.setter
    def root_directory(self, root_directory):
        """Sets the root_directory of this SystemInsightsLaunchd.


        :param root_directory: The root_directory of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._root_directory = root_directory

    @property
    def run_at_load(self):
        """Gets the run_at_load of this SystemInsightsLaunchd.  # noqa: E501


        :return: The run_at_load of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._run_at_load

    @run_at_load.setter
    def run_at_load(self, run_at_load):
        """Sets the run_at_load of this SystemInsightsLaunchd.


        :param run_at_load: The run_at_load of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._run_at_load = run_at_load

    @property
    def start_interval(self):
        """Gets the start_interval of this SystemInsightsLaunchd.  # noqa: E501


        :return: The start_interval of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._start_interval

    @start_interval.setter
    def start_interval(self, start_interval):
        """Sets the start_interval of this SystemInsightsLaunchd.


        :param start_interval: The start_interval of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._start_interval = start_interval

    @property
    def start_on_mount(self):
        """Gets the start_on_mount of this SystemInsightsLaunchd.  # noqa: E501


        :return: The start_on_mount of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._start_on_mount

    @start_on_mount.setter
    def start_on_mount(self, start_on_mount):
        """Sets the start_on_mount of this SystemInsightsLaunchd.


        :param start_on_mount: The start_on_mount of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._start_on_mount = start_on_mount

    @property
    def stderr_path(self):
        """Gets the stderr_path of this SystemInsightsLaunchd.  # noqa: E501


        :return: The stderr_path of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._stderr_path

    @stderr_path.setter
    def stderr_path(self, stderr_path):
        """Sets the stderr_path of this SystemInsightsLaunchd.


        :param stderr_path: The stderr_path of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._stderr_path = stderr_path

    @property
    def stdout_path(self):
        """Gets the stdout_path of this SystemInsightsLaunchd.  # noqa: E501


        :return: The stdout_path of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._stdout_path

    @stdout_path.setter
    def stdout_path(self, stdout_path):
        """Sets the stdout_path of this SystemInsightsLaunchd.


        :param stdout_path: The stdout_path of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._stdout_path = stdout_path

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsLaunchd.  # noqa: E501


        :return: The system_id of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsLaunchd.


        :param system_id: The system_id of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def username(self):
        """Gets the username of this SystemInsightsLaunchd.  # noqa: E501


        :return: The username of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SystemInsightsLaunchd.


        :param username: The username of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def watch_paths(self):
        """Gets the watch_paths of this SystemInsightsLaunchd.  # noqa: E501


        :return: The watch_paths of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._watch_paths

    @watch_paths.setter
    def watch_paths(self, watch_paths):
        """Sets the watch_paths of this SystemInsightsLaunchd.


        :param watch_paths: The watch_paths of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._watch_paths = watch_paths

    @property
    def working_directory(self):
        """Gets the working_directory of this SystemInsightsLaunchd.  # noqa: E501


        :return: The working_directory of this SystemInsightsLaunchd.  # noqa: E501
        :rtype: str
        """
        return self._working_directory

    @working_directory.setter
    def working_directory(self, working_directory):
        """Sets the working_directory of this SystemInsightsLaunchd.


        :param working_directory: The working_directory of this SystemInsightsLaunchd.  # noqa: E501
        :type: str
        """

        self._working_directory = working_directory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SystemInsightsLaunchd, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SystemInsightsLaunchd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
