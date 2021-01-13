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


class InternetEnum(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ClusterProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"
    deleting = "Deleting"
    updating = "Updating"


class AddonType(str, Enum):

    srm = "SRM"
    vr = "VR"


class AddonProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    cancelled = "Cancelled"
    deleting = "Deleting"
    updating = "Updating"


class HcxEnterpriseSiteStatus(str, Enum):

    available = "Available"
    consumed = "Consumed"
    deactivated = "Deactivated"
    deleted = "Deleted"


class GlobalReachConnectionProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    updating = "Updating"


class GlobalReachConnectionStatus(str, Enum):

    connected = "Connected"
    connecting = "Connecting"
    disconnected = "Disconnected"


class SegmentStatusEnum(str, Enum):

    successfailure = "SUCCESS, FAILURE"


class WorkloadNetworkSegmentProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"


class WorkloadNetworkDhcpProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"


class PortMirroringDirectionEnum(str, Enum):

    ingressegressbidirectional = "INGRESS, EGRESS, BIDIRECTIONAL"


class PortMirroringStatusEnum(str, Enum):

    successfailure = "SUCCESS, FAILURE"


class WorkloadNetworkPortMirroringProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"


class VMGroupStatusEnum(str, Enum):

    successfailure = "SUCCESS, FAILURE"


class WorkloadNetworkVMGroupProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"


class VMTypeEnum(str, Enum):

    regularedgeservice = "REGULAR, EDGE, SERVICE"


class DnsServiceLogLevelEnum(str, Enum):

    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    fatal = "FATAL"


class DnsServiceStatusEnum(str, Enum):

    success = "SUCCESS"
    failure = "FAILURE"


class WorkloadNetworkDnsServiceProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"


class WorkloadNetworkDnsZoneProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    building = "Building"
    deleting = "Deleting"
    updating = "Updating"
