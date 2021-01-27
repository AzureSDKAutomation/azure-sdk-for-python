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


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"


class AttestationServiceStatus(str, Enum):

    ready = "Ready"
    not_ready = "NotReady"
    error = "Error"


class PrivateEndpointConnectionProvisioningState(str, Enum):

    succeeded = "Succeeded"
    creating = "Creating"
    deleting = "Deleting"
    failed = "Failed"
