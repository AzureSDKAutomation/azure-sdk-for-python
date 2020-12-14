# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ProvisioningState(str, Enum):

    accepted = "Accepted"
    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    deleted = "Deleted"
    not_specified = "NotSpecified"


class MonitoringStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class MarketplaceSubscriptionStatus(str, Enum):

    active = "Active"
    suspended = "Suspended"


class LiftrResourceCategories(str, Enum):

    unknown = "Unknown"
    monitor_logs = "MonitorLogs"


class ManagedIdentityTypes(str, Enum):

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"


class TagAction(str, Enum):

    include = "Include"
    exclude = "Exclude"


class SingleSignOnStates(str, Enum):

    initial = "Initial"
    enable = "Enable"
    disable = "Disable"
    existing = "Existing"
