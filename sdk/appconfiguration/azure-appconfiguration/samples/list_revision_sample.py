# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: list_revision_sample.py
DESCRIPTION:
    This sample demos list revision operations for app configuration
USAGE: python list_revision_sample.py
"""

import os
import sys
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

def main():
    try:
        CONNECTION_STRING = os.environ['AZURE_APPCONFIG_CONNECTION_STRING']

    except KeyError:
        print("AZURE_APPCONFIG_CONNECTION_STRING must be set.")
        sys.exit(1)

    # Create app config client
    client = AzureAppConfigurationClient.from_connection_string(CONNECTION_STRING)

    config_setting = ConfigurationSetting(
        key="MyKey",
        value="my value",
        content_type="my content type",
        tags={"my tag": "my tag value"}
    )
    returned_config_setting = client.set_configuration_setting(config_setting)

    returned_config_setting.value = "new value"
    returned_config_setting.content_type = "new content type"
    client.set_configuration_setting(config_setting)

    items = client.list_revisions(keys=["MyKey"])
    for item in items:
        print(item)

    client.delete_configuration_setting(
        key="MyKey",
    )

if __name__ == "__main__":
    main()
