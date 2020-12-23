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


class MetricAggregationType(str, Enum):

    not_specified = "NotSpecified"
    none = "None"
    average = "Average"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"
    count = "Count"


class CacheIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    none = "None"


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"


class HealthStateType(str, Enum):

    unknown = "Unknown"
    healthy = "Healthy"
    degraded = "Degraded"
    down = "Down"
    transitioning = "Transitioning"
    stopping = "Stopping"
    stopped = "Stopped"
    upgrading = "Upgrading"
    flushing = "Flushing"


class ProvisioningStateType(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"
    creating = "Creating"
    deleting = "Deleting"
    updating = "Updating"


class FirmwareStatusType(str, Enum):

    available = "available"
    unavailable = "unavailable"


class NfsAccessRuleScope(str, Enum):

    default = "default"
    network = "network"
    host = "host"


class NfsAccessRuleAccess(str, Enum):

    no = "no"
    ro = "ro"
    rw = "rw"


class DomainJoinedType(str, Enum):

    yes = "Yes"
    no = "No"
    error = "Error"


class UsernameSource(str, Enum):

    ad = "AD"
    ldap = "LDAP"
    file = "File"
    none = "None"


class UsernameDownloadedType(str, Enum):

    yes = "Yes"
    no = "No"
    error = "Error"


class ReasonCode(str, Enum):

    quota_id = "QuotaId"
    not_available_for_subscription = "NotAvailableForSubscription"
