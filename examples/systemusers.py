#!/usr/bin/env python

from __future__ import print_function
import os
import time
import jcapi
from jcapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
# FIXME(ppg): allow changing the host used
#jcapi.Configuration.host = "https://console.jumpcloud.com"
api_instance = jcapi.DefaultApi()

try:
    # Get JumpCloud systemusers.
    api_response = api_instance.systemusers_get(x_api_key=os.environ['API_KEY'])
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->systemusers_get: %s\n" % e)

