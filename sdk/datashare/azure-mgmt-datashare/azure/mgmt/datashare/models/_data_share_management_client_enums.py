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


class Type(str, Enum):

    system_assigned = "SystemAssigned"


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    creating = "Creating"
    deleting = "Deleting"
    moving = "Moving"
    failed = "Failed"


class DataSetMappingStatus(str, Enum):

    ok = "Ok"
    broken = "Broken"


class OutputType(str, Enum):

    csv = "Csv"
    parquet = "Parquet"


class InvitationStatus(str, Enum):

    pending = "Pending"
    accepted = "Accepted"
    rejected = "Rejected"
    withdrawn = "Withdrawn"


class DataSetType(str, Enum):

    blob = "Blob"
    container = "Container"
    blob_folder = "BlobFolder"
    adls_gen2_file_system = "AdlsGen2FileSystem"
    adls_gen2_folder = "AdlsGen2Folder"
    adls_gen2_file = "AdlsGen2File"
    adls_gen1_folder = "AdlsGen1Folder"
    adls_gen1_file = "AdlsGen1File"
    kusto_cluster = "KustoCluster"
    kusto_database = "KustoDatabase"
    sql_db_table = "SqlDBTable"
    sql_dw_table = "SqlDWTable"


class Status(str, Enum):

    accepted = "Accepted"
    in_progress = "InProgress"
    transient_failure = "TransientFailure"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"


class ShareSubscriptionStatus(str, Enum):

    active = "Active"
    revoked = "Revoked"
    source_deleted = "SourceDeleted"
    revoking = "Revoking"


class RecurrenceInterval(str, Enum):

    hour = "Hour"
    day = "Day"


class SynchronizationMode(str, Enum):

    incremental = "Incremental"
    full_sync = "FullSync"


class TriggerStatus(str, Enum):

    active = "Active"
    inactive = "Inactive"
    source_synchronization_setting_deleted = "SourceSynchronizationSettingDeleted"


class ShareKind(str, Enum):

    copy_based = "CopyBased"
    in_place = "InPlace"
