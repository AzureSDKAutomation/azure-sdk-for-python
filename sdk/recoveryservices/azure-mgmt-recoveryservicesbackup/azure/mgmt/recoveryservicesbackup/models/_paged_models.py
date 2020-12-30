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

from msrest.paging import Paged


class ProtectionIntentResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProtectionIntentResource <azure.mgmt.recoveryservicesbackup.models.ProtectionIntentResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProtectionIntentResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProtectionIntentResourcePaged, self).__init__(*args, **kwargs)
class BackupManagementUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`BackupManagementUsage <azure.mgmt.recoveryservicesbackup.models.BackupManagementUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BackupManagementUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(BackupManagementUsagePaged, self).__init__(*args, **kwargs)
class ClientDiscoveryValueForSingleApiPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ClientDiscoveryValueForSingleApi <azure.mgmt.recoveryservicesbackup.models.ClientDiscoveryValueForSingleApi>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ClientDiscoveryValueForSingleApi]'}
    }

    def __init__(self, *args, **kwargs):

        super(ClientDiscoveryValueForSingleApiPaged, self).__init__(*args, **kwargs)
class RecoveryPointResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RecoveryPointResource <azure.mgmt.recoveryservicesbackup.models.RecoveryPointResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RecoveryPointResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecoveryPointResourcePaged, self).__init__(*args, **kwargs)
class ProtectionPolicyResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProtectionPolicyResource <azure.mgmt.recoveryservicesbackup.models.ProtectionPolicyResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProtectionPolicyResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProtectionPolicyResourcePaged, self).__init__(*args, **kwargs)
class JobResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobResource <azure.mgmt.recoveryservicesbackup.models.JobResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobResourcePaged, self).__init__(*args, **kwargs)
class ProtectedItemResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProtectedItemResource <azure.mgmt.recoveryservicesbackup.models.ProtectedItemResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProtectedItemResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProtectedItemResourcePaged, self).__init__(*args, **kwargs)
class BackupEngineBaseResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`BackupEngineBaseResource <azure.mgmt.recoveryservicesbackup.models.BackupEngineBaseResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BackupEngineBaseResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(BackupEngineBaseResourcePaged, self).__init__(*args, **kwargs)
class ProtectableContainerResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProtectableContainerResource <azure.mgmt.recoveryservicesbackup.models.ProtectableContainerResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProtectableContainerResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProtectableContainerResourcePaged, self).__init__(*args, **kwargs)
class WorkloadItemResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`WorkloadItemResource <azure.mgmt.recoveryservicesbackup.models.WorkloadItemResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WorkloadItemResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkloadItemResourcePaged, self).__init__(*args, **kwargs)
class WorkloadProtectableItemResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`WorkloadProtectableItemResource <azure.mgmt.recoveryservicesbackup.models.WorkloadProtectableItemResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WorkloadProtectableItemResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkloadProtectableItemResourcePaged, self).__init__(*args, **kwargs)
class ProtectionContainerResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProtectionContainerResource <azure.mgmt.recoveryservicesbackup.models.ProtectionContainerResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProtectionContainerResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProtectionContainerResourcePaged, self).__init__(*args, **kwargs)
