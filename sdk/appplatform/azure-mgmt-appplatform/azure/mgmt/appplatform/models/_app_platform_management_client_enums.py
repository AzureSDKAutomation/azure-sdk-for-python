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

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    deleted = "Deleted"
    succeeded = "Succeeded"
    failed = "Failed"
    moving = "Moving"
    moved = "Moved"
    move_failed = "MoveFailed"


class ConfigServerState(str, Enum):

    not_available = "NotAvailable"
    deleted = "Deleted"
    failed = "Failed"
    succeeded = "Succeeded"
    updating = "Updating"


class TraceProxyState(str, Enum):

    not_available = "NotAvailable"
    failed = "Failed"
    succeeded = "Succeeded"
    updating = "Updating"


class TestKeyType(str, Enum):

    primary = "Primary"
    secondary = "Secondary"


class AppResourceProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"


class UserSourceType(str, Enum):

    jar = "Jar"
    net_core_zip = "NetCoreZip"
    source = "Source"


class DeploymentResourceProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    succeeded = "Succeeded"
    failed = "Failed"
    deleting = "Deleting"


class RuntimeVersion(str, Enum):

    java_8 = "Java_8"
    java_11 = "Java_11"
    net_core_31 = "NetCore_31"


class DeploymentResourceStatus(str, Enum):

    unknown = "Unknown"
    stopped = "Stopped"
    running = "Running"
    failed = "Failed"
    allocating = "Allocating"
    upgrading = "Upgrading"
    compiling = "Compiling"
    processing = "Processing"


class RuntimePlatform(str, Enum):

    java = "Java"
    net_core = ".NET Core"


class SkuScaleType(str, Enum):

    none = "None"
    manual = "Manual"
    automatic = "Automatic"
