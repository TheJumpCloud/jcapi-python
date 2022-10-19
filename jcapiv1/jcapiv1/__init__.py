# coding: utf-8

# flake8: noqa

"""
    JumpCloud API

    # Overview  JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, and system users.  # API Key  ## Access Your API Key  To locate your API Key:  1. Log into the [JumpCloud Admin Console](https://console.jumpcloud.com/). 2. Go to the username drop down located in the top-right of the Console. 3. Retrieve your API key from API Settings.  ## API Key Considerations  This API key is associated to the currently logged in administrator. Other admins will have different API keys.  **WARNING** Please keep this API key secret, as it grants full access to any data accessible via your JumpCloud console account.  You can also reset your API key in the same location in the JumpCloud Admin Console.  ## Recycling or Resetting Your API Key  In order to revoke access with the current API key, simply reset your API key. This will render all calls using the previous API key inaccessible.  Your API key will be passed in as a header with the header name \"x-api-key\".  ```bash curl -H \"x-api-key: [YOUR_API_KEY_HERE]\" \"https://console.jumpcloud.com/api/systemusers\" ```  # System Context  * [Introduction](#introduction) * [Supported endpoints](#supported-endpoints) * [Response codes](#response-codes) * [Authentication](#authentication) * [Additional examples](#additional-examples) * [Third party](#third-party)  ## Introduction  JumpCloud System Context Authorization is an alternative way to authenticate with a subset of JumpCloud's REST APIs. Using this method, a system can manage its information and resource associations, allowing modern auto provisioning environments to scale as needed.  **Notes:**   * The following documentation applies to Linux Operating Systems only.  * Systems that have been automatically enrolled using Apple's Device Enrollment Program (DEP) or systems enrolled using the User Portal install are not eligible to use the System Context API to prevent unauthorized access to system groups and resources. If a script that utilizes the System Context API is invoked on a system enrolled in this way, it will display an error.  ## Supported Endpoints  JumpCloud System Context Authorization can be used in conjunction with Systems endpoints found in the V1 API and certain System Group endpoints found in the v2 API.  * A system may fetch, alter, and delete metadata about itself, including manipulating a system's Group and Systemuser associations,   * `/api/systems/{system_id}` | [`GET`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_get) [`PUT`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_put) * A system may delete itself from your JumpCloud organization   * `/api/systems/{system_id}` | [`DELETE`](https://docs.jumpcloud.com/api/1.0/index.html#operation/systems_delete) * A system may fetch its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/memberof` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembership)   * `/api/v2/systems/{system_id}/associations` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsList)   * `/api/v2/systems/{system_id}/users` | [`GET`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemTraverseUser) * A system may alter its direct resource associations under v2 (Groups)   * `/api/v2/systems/{system_id}/associations` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemAssociationsPost) * A system may alter its System Group associations   * `/api/v2/systemgroups/{group_id}/members` | [`POST`](https://docs.jumpcloud.com/api/2.0/index.html#operation/graph_systemGroupMembersPost)     * _NOTE_ If a system attempts to alter the system group membership of a different system the request will be rejected  ## Response Codes  If endpoints other than those described above are called using the System Context API, the server will return a `401` response.  ## Authentication  To allow for secure access to our APIs, you must authenticate each API request. JumpCloud System Context Authorization uses [HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures-00) to authenticate API requests. The HTTP Signatures sent with each request are similar to the signatures used by the Amazon Web Services REST API. To help with the request-signing process, we have provided an [example bash script](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh). This example API request simply requests the entire system record. You must be root, or have permissions to access the contents of the `/opt/jc` directory to generate a signature.  Here is a breakdown of the example script with explanations.  First, the script extracts the systemKey from the JSON formatted `/opt/jc/jcagent.conf` file.  ```bash #!/bin/bash conf=\"`cat /opt/jc/jcagent.conf`\" regex=\"systemKey\\\":\\\"(\\w+)\\\"\"  if [[ $conf =~ $regex ]] ; then   systemKey=\"${BASH_REMATCH[1]}\" fi ```  Then, the script retrieves the current date in the correct format.  ```bash now=`date -u \"+%a, %d %h %Y %H:%M:%S GMT\"`; ```  Next, we build a signing string to demonstrate the expected signature format. The signed string must consist of the [request-line](https://tools.ietf.org/html/rfc2616#page-35) and the date header, separated by a newline character.  ```bash signstr=\"GET /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" ```  The next step is to calculate and apply the signature. This is a two-step process:  1. Create a signature from the signing string using the JumpCloud Agent private key: ``printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key`` 2. Then Base64-encode the signature string and trim off the newline characters: ``| openssl enc -e -a | tr -d '\\n'``  The combined steps above result in:  ```bash signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ; ```  Finally, we make sure the API call sending the signature has the same Authorization and Date header values, HTTP method, and URL that were used in the signing string.  ```bash curl -iq \\   -H \"Accept: application/json\" \\   -H \"Content-Type: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Input Data  All PUT and POST methods should use the HTTP Content-Type header with a value of 'application/json'. PUT methods are used for updating a record. POST methods are used to create a record.  The following example demonstrates how to update the `displayName` of the system.  ```bash signstr=\"PUT /api/systems/${systemKey} HTTP/1.1\\ndate: ${now}\" signature=`printf \"$signstr\" | openssl dgst -sha256 -sign /opt/jc/client.key | openssl enc -e -a | tr -d '\\n'` ;  curl -iq \\   -d \"{\\\"displayName\\\" : \\\"updated-system-name-1\\\"}\" \\   -X \"PUT\" \\   -H \"Content-Type: application/json\" \\   -H \"Accept: application/json\" \\   -H \"Date: ${now}\" \\   -H \"Authorization: Signature keyId=\\\"system/${systemKey}\\\",headers=\\\"request-line date\\\",algorithm=\\\"rsa-sha256\\\",signature=\\\"${signature}\\\"\" \\   --url https://console.jumpcloud.com/api/systems/${systemKey} ```  ### Output Data  All results will be formatted as JSON.  Here is an abbreviated example of response output:  ```json {   \"_id\": \"525ee96f52e144993e000015\",   \"agentServer\": \"lappy386\",   \"agentVersion\": \"0.9.42\",   \"arch\": \"x86_64\",   \"connectionKey\": \"127.0.0.1_51812\",   \"displayName\": \"ubuntu-1204\",   \"firstContact\": \"2013-10-16T19:30:55.611Z\",   \"hostname\": \"ubuntu-1204\"   ... ```  ## Additional Examples  ### Signing Authentication Example  This example demonstrates how to make an authenticated request to fetch the JumpCloud record for this system.  [SigningExample.sh](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/shell/SigningExample.sh)  ### Shutdown Hook  This example demonstrates how to make an authenticated request on system shutdown. Using an init.d script registered at run level 0, you can call the System Context API as the system is shutting down.  [Instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) is an example of an init.d script that only runs at system shutdown.  After customizing the [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) script, you should install it on the system(s) running the JumpCloud agent.  1. Copy the modified [instance-shutdown-initd](https://github.com/TheJumpCloud/SystemContextAPI/blob/master/examples/instance-shutdown-initd) to `/etc/init.d/instance-shutdown`. 2. On Ubuntu systems, run `update-rc.d instance-shutdown defaults`. On RedHat/CentOS systems, run `chkconfig --add instance-shutdown`.  ## Third Party  ### Chef Cookbooks  [https://github.com/nshenry03/jumpcloud](https://github.com/nshenry03/jumpcloud)  [https://github.com/cjs226/jumpcloud](https://github.com/cjs226/jumpcloud)  # Multi-Tenant Portal Headers  Multi-Tenant Organization API Headers are available for JumpCloud Admins to use when making API requests from Organizations that have multiple managed organizations.  The `x-org-id` is a required header for all multi-tenant admins when making API requests to JumpCloud. This header will define to which organization you would like to make the request.  **NOTE** Single Tenant Admins do not need to provide this header when making an API request.  ## Header Value  `x-org-id`  ## API Response Codes  * `400` Malformed ID. * `400` x-org-id and Organization path ID do not match. * `401` ID not included for multi-tenant admin * `403` ID included on unsupported route. * `404` Organization ID Not Found.  ```bash curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -H 'x-org-id: {ORG_ID}'  ```  ## To Obtain an Individual Organization ID via the UI  As a prerequisite, your Primary Organization will need to be setup for Multi-Tenancy. This provides access to the Multi-Tenant Organization Admin Portal.  1. Log into JumpCloud [Admin Console](https://console.jumpcloud.com). If you are a multi-tenant Admin, you will automatically be routed to the Multi-Tenant Admin Portal. 2. From the Multi-Tenant Portal's primary navigation bar, select the Organization you'd like to access. 3. You will automatically be routed to that Organization's Admin Console. 4. Go to Settings in the sub-tenant's primary navigation. 5. You can obtain your Organization ID below your Organization's Contact Information on the Settings page.  ## To Obtain All Organization IDs via the API  * You can make an API request to this endpoint using the API key of your Primary Organization.  `https://console.jumpcloud.com/api/organizations/` This will return all your managed organizations.  ```bash curl -X GET \\   https://console.jumpcloud.com/api/organizations/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' ```  # SDKs  You can find language specific SDKs that can help you kickstart your Integration with JumpCloud in the following GitHub repositories:  * [Python](https://github.com/TheJumpCloud/jcapi-python) * [Go](https://github.com/TheJumpCloud/jcapi-go) * [Ruby](https://github.com/TheJumpCloud/jcapi-ruby) * [Java](https://github.com/TheJumpCloud/jcapi-java)   # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@jumpcloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from jcapiv1.api.application_templates_api import ApplicationTemplatesApi
from jcapiv1.api.applications_api import ApplicationsApi
from jcapiv1.api.command_results_api import CommandResultsApi
from jcapiv1.api.command_triggers_api import CommandTriggersApi
from jcapiv1.api.commands_api import CommandsApi
from jcapiv1.api.managed_service_provider_api import ManagedServiceProviderApi
from jcapiv1.api.organizations_api import OrganizationsApi
from jcapiv1.api.radius_servers_api import RadiusServersApi
from jcapiv1.api.search_api import SearchApi
from jcapiv1.api.systems_api import SystemsApi
from jcapiv1.api.systemusers_api import SystemusersApi
from jcapiv1.api.users_api import UsersApi
# import ApiClient
from jcapiv1.api_client import ApiClient
from jcapiv1.configuration import Configuration
# import models into sdk package
from jcapiv1.models.application import Application
from jcapiv1.models.application_config import ApplicationConfig
from jcapiv1.models.application_config_acs_url import ApplicationConfigAcsUrl
from jcapiv1.models.application_config_acs_url_tooltip import ApplicationConfigAcsUrlTooltip
from jcapiv1.models.application_config_acs_url_tooltip_variables import ApplicationConfigAcsUrlTooltipVariables
from jcapiv1.models.application_config_constant_attributes import ApplicationConfigConstantAttributes
from jcapiv1.models.application_config_constant_attributes_value import ApplicationConfigConstantAttributesValue
from jcapiv1.models.application_config_database_attributes import ApplicationConfigDatabaseAttributes
from jcapiv1.models.application_logo import ApplicationLogo
from jcapiv1.models.applicationslist import Applicationslist
from jcapiv1.models.applicationtemplate import Applicationtemplate
from jcapiv1.models.applicationtemplate_jit import ApplicationtemplateJit
from jcapiv1.models.applicationtemplate_logo import ApplicationtemplateLogo
from jcapiv1.models.applicationtemplate_oidc import ApplicationtemplateOidc
from jcapiv1.models.applicationtemplate_provision import ApplicationtemplateProvision
from jcapiv1.models.applicationtemplateslist import Applicationtemplateslist
from jcapiv1.models.command import Command
from jcapiv1.models.commandfilereturn import Commandfilereturn
from jcapiv1.models.commandfilereturn_results import CommandfilereturnResults
from jcapiv1.models.commandresult import Commandresult
from jcapiv1.models.commandresult_response import CommandresultResponse
from jcapiv1.models.commandresult_response_data import CommandresultResponseData
from jcapiv1.models.commandresultslist import Commandresultslist
from jcapiv1.models.commandresultslist_results import CommandresultslistResults
from jcapiv1.models.commandslist import Commandslist
from jcapiv1.models.commandslist_results import CommandslistResults
from jcapiv1.models.error import Error
from jcapiv1.models.error_details import ErrorDetails
from jcapiv1.models.fde import Fde
from jcapiv1.models.id_resetmfa_body import IdResetmfaBody
from jcapiv1.models.mfa import Mfa
from jcapiv1.models.mfa_enrollment import MfaEnrollment
from jcapiv1.models.mfa_enrollment_status import MfaEnrollmentStatus
from jcapiv1.models.organization import Organization
from jcapiv1.models.organizationentitlement import Organizationentitlement
from jcapiv1.models.organizationentitlement_entitlement_products import OrganizationentitlementEntitlementProducts
from jcapiv1.models.organizations_id_body import OrganizationsIdBody
from jcapiv1.models.organizationsettings import Organizationsettings
from jcapiv1.models.organizationsettings_display_preferences import OrganizationsettingsDisplayPreferences
from jcapiv1.models.organizationsettings_display_preferences_org_insights import OrganizationsettingsDisplayPreferencesOrgInsights
from jcapiv1.models.organizationsettings_display_preferences_org_insights_applications_usage import OrganizationsettingsDisplayPreferencesOrgInsightsApplicationsUsage
from jcapiv1.models.organizationsettings_display_preferences_org_insights_console_stats import OrganizationsettingsDisplayPreferencesOrgInsightsConsoleStats
from jcapiv1.models.organizationsettings_display_preferences_org_insights_device_notifications import OrganizationsettingsDisplayPreferencesOrgInsightsDeviceNotifications
from jcapiv1.models.organizationsettings_display_preferences_org_insights_user_notifications import OrganizationsettingsDisplayPreferencesOrgInsightsUserNotifications
from jcapiv1.models.organizationsettings_features import OrganizationsettingsFeatures
from jcapiv1.models.organizationsettings_features_directory_insights import OrganizationsettingsFeaturesDirectoryInsights
from jcapiv1.models.organizationsettings_features_directory_insights_premium import OrganizationsettingsFeaturesDirectoryInsightsPremium
from jcapiv1.models.organizationsettings_features_system_insights import OrganizationsettingsFeaturesSystemInsights
from jcapiv1.models.organizationsettings_new_system_user_state_defaults import OrganizationsettingsNewSystemUserStateDefaults
from jcapiv1.models.organizationsettings_password_policy import OrganizationsettingsPasswordPolicy
from jcapiv1.models.organizationsettings_user_portal import OrganizationsettingsUserPortal
from jcapiv1.models.organizationsettingsput import Organizationsettingsput
from jcapiv1.models.organizationsettingsput_new_system_user_state_defaults import OrganizationsettingsputNewSystemUserStateDefaults
from jcapiv1.models.organizationsettingsput_password_policy import OrganizationsettingsputPasswordPolicy
from jcapiv1.models.organizationslist import Organizationslist
from jcapiv1.models.organizationslist_results import OrganizationslistResults
from jcapiv1.models.radiusserver import Radiusserver
from jcapiv1.models.radiusserverpost import Radiusserverpost
from jcapiv1.models.radiusserverput import Radiusserverput
from jcapiv1.models.radiusservers_id_body import RadiusserversIdBody
from jcapiv1.models.radiusserverslist import Radiusserverslist
from jcapiv1.models.search import Search
from jcapiv1.models.sshkeylist import Sshkeylist
from jcapiv1.models.sshkeypost import Sshkeypost
from jcapiv1.models.sso import Sso
from jcapiv1.models.state_activate_body import StateActivateBody
from jcapiv1.models.system import System
from jcapiv1.models.system_built_in_commands import SystemBuiltInCommands
from jcapiv1.models.system_domain_info import SystemDomainInfo
from jcapiv1.models.system_mdm import SystemMdm
from jcapiv1.models.system_mdm_internal import SystemMdmInternal
from jcapiv1.models.system_network_interfaces import SystemNetworkInterfaces
from jcapiv1.models.system_os_version_detail import SystemOsVersionDetail
from jcapiv1.models.system_provision_metadata import SystemProvisionMetadata
from jcapiv1.models.system_provision_metadata_provisioner import SystemProvisionMetadataProvisioner
from jcapiv1.models.system_service_account_state import SystemServiceAccountState
from jcapiv1.models.system_sshd_params import SystemSshdParams
from jcapiv1.models.system_system_insights import SystemSystemInsights
from jcapiv1.models.system_user_metrics import SystemUserMetrics
from jcapiv1.models.systemput import Systemput
from jcapiv1.models.systemput_agent_bound_messages import SystemputAgentBoundMessages
from jcapiv1.models.systemslist import Systemslist
from jcapiv1.models.systemuserput import Systemuserput
from jcapiv1.models.systemuserput_addresses import SystemuserputAddresses
from jcapiv1.models.systemuserput_attributes import SystemuserputAttributes
from jcapiv1.models.systemuserput_phone_numbers import SystemuserputPhoneNumbers
from jcapiv1.models.systemuserput_relationships import SystemuserputRelationships
from jcapiv1.models.systemuserputpost import Systemuserputpost
from jcapiv1.models.systemuserputpost_addresses import SystemuserputpostAddresses
from jcapiv1.models.systemuserputpost_phone_numbers import SystemuserputpostPhoneNumbers
from jcapiv1.models.systemuserputpost_recovery_email import SystemuserputpostRecoveryEmail
from jcapiv1.models.systemuserreturn import Systemuserreturn
from jcapiv1.models.systemuserreturn_addresses import SystemuserreturnAddresses
from jcapiv1.models.systemuserreturn_phone_numbers import SystemuserreturnPhoneNumbers
from jcapiv1.models.systemuserreturn_recovery_email import SystemuserreturnRecoveryEmail
from jcapiv1.models.systemuserslist import Systemuserslist
from jcapiv1.models.triggerreturn import Triggerreturn
from jcapiv1.models.trustedapp_config_get import TrustedappConfigGet
from jcapiv1.models.trustedapp_config_get_trusted_apps import TrustedappConfigGetTrustedApps
from jcapiv1.models.trustedapp_config_put import TrustedappConfigPut
from jcapiv1.models.userput import Userput
from jcapiv1.models.userreturn import Userreturn
from jcapiv1.models.userreturn_growth_data import UserreturnGrowthData
