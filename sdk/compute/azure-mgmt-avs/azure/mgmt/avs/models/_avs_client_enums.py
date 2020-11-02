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


class TrialStatus(str, Enum):

    trial_available = "TrialAvailable"
    trial_used = "TrialUsed"
    trial_disabled = "TrialDisabled"


class QuotaEnabled(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ExpressRouteAuthorizationProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    updating = "Updating"


class SslEnum(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class PrivateCloudProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"
    pending = "Pending"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"


class ClusterProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"
    deleting = "Deleting"
    updating = "Updating"


class InternetEnum(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class HcxEnterpriseSiteStatus(str, Enum):

    available = "Available"
    consumed = "Consumed"
    deactivated = "Deactivated"
    deleted = "Deleted"
