# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: hello_world_advanced_sample.py
DESCRIPTION:
    This sample demos more advanced scenarios including add/set with label/list operations for app configuration
USAGE: python hello_world_advanced_sample.py
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

    print("Add new configration setting")
    config_setting = ConfigurationSetting(
        key="MyKey",
        label="MyLabel",
        value="my value",
        content_type="my content type",
        tags={"my tag": "my tag value"}
    )
    added_config_setting = client.add_configuration_setting(config_setting)
    print("New configration setting:")
    print(added_config_setting)
    print("")

    print("Set configuration setting")
    added_config_setting.value = "new value"
    added_config_setting.content_type = "new content type"
    updated_config_setting = client.set_configuration_setting(config_setting)
    print(updated_config_setting)
    print("")

    print("List configuration settings")
    config_settings = client.list_configuration_settings()
    for item in config_settings:
        print(item)

    print("Delete configuration setting")
    client.delete_configuration_setting(
        key="MyKey",
        label="MyLabel",
    )

if __name__ == "__main__":
    main()
