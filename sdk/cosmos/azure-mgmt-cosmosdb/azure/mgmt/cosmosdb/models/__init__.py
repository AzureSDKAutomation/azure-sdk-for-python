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

try:
    from ._models_py3 import AnalyticalStorageConfig
    from ._models_py3 import ApiProperties
    from ._models_py3 import ARMProxyResource
    from ._models_py3 import ARMResourceProperties
    from ._models_py3 import AutoscaleSettings
    from ._models_py3 import AutoscaleSettingsResource
    from ._models_py3 import AutoUpgradePolicyResource
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import BackupPolicy
    from ._models_py3 import Capability
    from ._models_py3 import CassandraKeyspaceCreateUpdateParameters
    from ._models_py3 import CassandraKeyspaceGetPropertiesOptions
    from ._models_py3 import CassandraKeyspaceGetPropertiesResource
    from ._models_py3 import CassandraKeyspaceGetResults
    from ._models_py3 import CassandraKeyspaceResource
    from ._models_py3 import CassandraPartitionKey
    from ._models_py3 import CassandraSchema
    from ._models_py3 import CassandraTableCreateUpdateParameters
    from ._models_py3 import CassandraTableGetPropertiesOptions
    from ._models_py3 import CassandraTableGetPropertiesResource
    from ._models_py3 import CassandraTableGetResults
    from ._models_py3 import CassandraTableResource
    from ._models_py3 import ClusterKey
    from ._models_py3 import Column
    from ._models_py3 import CompositePath
    from ._models_py3 import ConflictResolutionPolicy
    from ._models_py3 import ConsistencyPolicy
    from ._models_py3 import ContainerPartitionKey
    from ._models_py3 import ContinuousModeBackupPolicy
    from ._models_py3 import CorsPolicy
    from ._models_py3 import CreateUpdateOptions
    from ._models_py3 import DatabaseAccountConnectionString
    from ._models_py3 import DatabaseAccountCreateUpdateParameters
    from ._models_py3 import DatabaseAccountGetResults
    from ._models_py3 import DatabaseAccountListConnectionStringsResult
    from ._models_py3 import DatabaseAccountListKeysResult
    from ._models_py3 import DatabaseAccountListReadOnlyKeysResult
    from ._models_py3 import DatabaseAccountRegenerateKeyParameters
    from ._models_py3 import DatabaseAccountUpdateParameters
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ErrorResponseUpdatedFormat, ErrorResponseUpdatedFormatException
    from ._models_py3 import ExcludedPath
    from ._models_py3 import ExtendedResourceProperties
    from ._models_py3 import FailoverPolicies
    from ._models_py3 import FailoverPolicy
    from ._models_py3 import GremlinDatabaseCreateUpdateParameters
    from ._models_py3 import GremlinDatabaseGetPropertiesOptions
    from ._models_py3 import GremlinDatabaseGetPropertiesResource
    from ._models_py3 import GremlinDatabaseGetResults
    from ._models_py3 import GremlinDatabaseResource
    from ._models_py3 import GremlinGraphCreateUpdateParameters
    from ._models_py3 import GremlinGraphGetPropertiesOptions
    from ._models_py3 import GremlinGraphGetPropertiesResource
    from ._models_py3 import GremlinGraphGetResults
    from ._models_py3 import GremlinGraphResource
    from ._models_py3 import IncludedPath
    from ._models_py3 import Indexes
    from ._models_py3 import IndexingPolicy
    from ._models_py3 import IpAddressOrRange
    from ._models_py3 import Location
    from ._models_py3 import Metric
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricDefinition
    from ._models_py3 import MetricName
    from ._models_py3 import MetricValue
    from ._models_py3 import MongoDBCollectionCreateUpdateParameters
    from ._models_py3 import MongoDBCollectionGetPropertiesOptions
    from ._models_py3 import MongoDBCollectionGetPropertiesResource
    from ._models_py3 import MongoDBCollectionGetResults
    from ._models_py3 import MongoDBCollectionResource
    from ._models_py3 import MongoDBDatabaseCreateUpdateParameters
    from ._models_py3 import MongoDBDatabaseGetPropertiesOptions
    from ._models_py3 import MongoDBDatabaseGetPropertiesResource
    from ._models_py3 import MongoDBDatabaseGetResults
    from ._models_py3 import MongoDBDatabaseResource
    from ._models_py3 import MongoIndex
    from ._models_py3 import MongoIndexKeys
    from ._models_py3 import MongoIndexOptions
    from ._models_py3 import NotebookWorkspace
    from ._models_py3 import NotebookWorkspaceConnectionInfoResult
    from ._models_py3 import NotebookWorkspaceCreateUpdateParameters
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OptionsResource
    from ._models_py3 import PartitionMetric
    from ._models_py3 import PartitionUsage
    from ._models_py3 import PercentileMetric
    from ._models_py3 import PercentileMetricValue
    from ._models_py3 import PeriodicModeBackupPolicy
    from ._models_py3 import PeriodicModeProperties
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ProxyResource
    from ._models_py3 import RegionForOnlineOffline
    from ._models_py3 import Resource
    from ._models_py3 import SpatialSpec
    from ._models_py3 import SqlContainerCreateUpdateParameters
    from ._models_py3 import SqlContainerGetPropertiesOptions
    from ._models_py3 import SqlContainerGetPropertiesResource
    from ._models_py3 import SqlContainerGetResults
    from ._models_py3 import SqlContainerResource
    from ._models_py3 import SqlDatabaseCreateUpdateParameters
    from ._models_py3 import SqlDatabaseGetPropertiesOptions
    from ._models_py3 import SqlDatabaseGetPropertiesResource
    from ._models_py3 import SqlDatabaseGetResults
    from ._models_py3 import SqlDatabaseResource
    from ._models_py3 import SqlStoredProcedureCreateUpdateParameters
    from ._models_py3 import SqlStoredProcedureGetPropertiesResource
    from ._models_py3 import SqlStoredProcedureGetResults
    from ._models_py3 import SqlStoredProcedureResource
    from ._models_py3 import SqlTriggerCreateUpdateParameters
    from ._models_py3 import SqlTriggerGetPropertiesResource
    from ._models_py3 import SqlTriggerGetResults
    from ._models_py3 import SqlTriggerResource
    from ._models_py3 import SqlUserDefinedFunctionCreateUpdateParameters
    from ._models_py3 import SqlUserDefinedFunctionGetPropertiesResource
    from ._models_py3 import SqlUserDefinedFunctionGetResults
    from ._models_py3 import SqlUserDefinedFunctionResource
    from ._models_py3 import TableCreateUpdateParameters
    from ._models_py3 import TableGetPropertiesOptions
    from ._models_py3 import TableGetPropertiesResource
    from ._models_py3 import TableGetResults
    from ._models_py3 import TableResource
    from ._models_py3 import ThroughputPolicyResource
    from ._models_py3 import ThroughputSettingsGetPropertiesResource
    from ._models_py3 import ThroughputSettingsGetResults
    from ._models_py3 import ThroughputSettingsResource
    from ._models_py3 import ThroughputSettingsUpdateParameters
    from ._models_py3 import TrackedResource
    from ._models_py3 import UniqueKey
    from ._models_py3 import UniqueKeyPolicy
    from ._models_py3 import Usage
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import AnalyticalStorageConfig
    from ._models import ApiProperties
    from ._models import ARMProxyResource
    from ._models import ARMResourceProperties
    from ._models import AutoscaleSettings
    from ._models import AutoscaleSettingsResource
    from ._models import AutoUpgradePolicyResource
    from ._models import AzureEntityResource
    from ._models import BackupPolicy
    from ._models import Capability
    from ._models import CassandraKeyspaceCreateUpdateParameters
    from ._models import CassandraKeyspaceGetPropertiesOptions
    from ._models import CassandraKeyspaceGetPropertiesResource
    from ._models import CassandraKeyspaceGetResults
    from ._models import CassandraKeyspaceResource
    from ._models import CassandraPartitionKey
    from ._models import CassandraSchema
    from ._models import CassandraTableCreateUpdateParameters
    from ._models import CassandraTableGetPropertiesOptions
    from ._models import CassandraTableGetPropertiesResource
    from ._models import CassandraTableGetResults
    from ._models import CassandraTableResource
    from ._models import ClusterKey
    from ._models import Column
    from ._models import CompositePath
    from ._models import ConflictResolutionPolicy
    from ._models import ConsistencyPolicy
    from ._models import ContainerPartitionKey
    from ._models import ContinuousModeBackupPolicy
    from ._models import CorsPolicy
    from ._models import CreateUpdateOptions
    from ._models import DatabaseAccountConnectionString
    from ._models import DatabaseAccountCreateUpdateParameters
    from ._models import DatabaseAccountGetResults
    from ._models import DatabaseAccountListConnectionStringsResult
    from ._models import DatabaseAccountListKeysResult
    from ._models import DatabaseAccountListReadOnlyKeysResult
    from ._models import DatabaseAccountRegenerateKeyParameters
    from ._models import DatabaseAccountUpdateParameters
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ErrorResponseUpdatedFormat, ErrorResponseUpdatedFormatException
    from ._models import ExcludedPath
    from ._models import ExtendedResourceProperties
    from ._models import FailoverPolicies
    from ._models import FailoverPolicy
    from ._models import GremlinDatabaseCreateUpdateParameters
    from ._models import GremlinDatabaseGetPropertiesOptions
    from ._models import GremlinDatabaseGetPropertiesResource
    from ._models import GremlinDatabaseGetResults
    from ._models import GremlinDatabaseResource
    from ._models import GremlinGraphCreateUpdateParameters
    from ._models import GremlinGraphGetPropertiesOptions
    from ._models import GremlinGraphGetPropertiesResource
    from ._models import GremlinGraphGetResults
    from ._models import GremlinGraphResource
    from ._models import IncludedPath
    from ._models import Indexes
    from ._models import IndexingPolicy
    from ._models import IpAddressOrRange
    from ._models import Location
    from ._models import Metric
    from ._models import MetricAvailability
    from ._models import MetricDefinition
    from ._models import MetricName
    from ._models import MetricValue
    from ._models import MongoDBCollectionCreateUpdateParameters
    from ._models import MongoDBCollectionGetPropertiesOptions
    from ._models import MongoDBCollectionGetPropertiesResource
    from ._models import MongoDBCollectionGetResults
    from ._models import MongoDBCollectionResource
    from ._models import MongoDBDatabaseCreateUpdateParameters
    from ._models import MongoDBDatabaseGetPropertiesOptions
    from ._models import MongoDBDatabaseGetPropertiesResource
    from ._models import MongoDBDatabaseGetResults
    from ._models import MongoDBDatabaseResource
    from ._models import MongoIndex
    from ._models import MongoIndexKeys
    from ._models import MongoIndexOptions
    from ._models import NotebookWorkspace
    from ._models import NotebookWorkspaceConnectionInfoResult
    from ._models import NotebookWorkspaceCreateUpdateParameters
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OptionsResource
    from ._models import PartitionMetric
    from ._models import PartitionUsage
    from ._models import PercentileMetric
    from ._models import PercentileMetricValue
    from ._models import PeriodicModeBackupPolicy
    from ._models import PeriodicModeProperties
    from ._models import PrivateEndpointConnection
    from ._models import PrivateEndpointProperty
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkServiceConnectionStateProperty
    from ._models import ProxyResource
    from ._models import RegionForOnlineOffline
    from ._models import Resource
    from ._models import SpatialSpec
    from ._models import SqlContainerCreateUpdateParameters
    from ._models import SqlContainerGetPropertiesOptions
    from ._models import SqlContainerGetPropertiesResource
    from ._models import SqlContainerGetResults
    from ._models import SqlContainerResource
    from ._models import SqlDatabaseCreateUpdateParameters
    from ._models import SqlDatabaseGetPropertiesOptions
    from ._models import SqlDatabaseGetPropertiesResource
    from ._models import SqlDatabaseGetResults
    from ._models import SqlDatabaseResource
    from ._models import SqlStoredProcedureCreateUpdateParameters
    from ._models import SqlStoredProcedureGetPropertiesResource
    from ._models import SqlStoredProcedureGetResults
    from ._models import SqlStoredProcedureResource
    from ._models import SqlTriggerCreateUpdateParameters
    from ._models import SqlTriggerGetPropertiesResource
    from ._models import SqlTriggerGetResults
    from ._models import SqlTriggerResource
    from ._models import SqlUserDefinedFunctionCreateUpdateParameters
    from ._models import SqlUserDefinedFunctionGetPropertiesResource
    from ._models import SqlUserDefinedFunctionGetResults
    from ._models import SqlUserDefinedFunctionResource
    from ._models import TableCreateUpdateParameters
    from ._models import TableGetPropertiesOptions
    from ._models import TableGetPropertiesResource
    from ._models import TableGetResults
    from ._models import TableResource
    from ._models import ThroughputPolicyResource
    from ._models import ThroughputSettingsGetPropertiesResource
    from ._models import ThroughputSettingsGetResults
    from ._models import ThroughputSettingsResource
    from ._models import ThroughputSettingsUpdateParameters
    from ._models import TrackedResource
    from ._models import UniqueKey
    from ._models import UniqueKeyPolicy
    from ._models import Usage
    from ._models import VirtualNetworkRule
from ._paged_models import CassandraKeyspaceGetResultsPaged
from ._paged_models import CassandraTableGetResultsPaged
from ._paged_models import DatabaseAccountGetResultsPaged
from ._paged_models import GremlinDatabaseGetResultsPaged
from ._paged_models import GremlinGraphGetResultsPaged
from ._paged_models import MetricDefinitionPaged
from ._paged_models import MetricPaged
from ._paged_models import MongoDBCollectionGetResultsPaged
from ._paged_models import MongoDBDatabaseGetResultsPaged
from ._paged_models import NotebookWorkspacePaged
from ._paged_models import OperationPaged
from ._paged_models import PartitionMetricPaged
from ._paged_models import PartitionUsagePaged
from ._paged_models import PercentileMetricPaged
from ._paged_models import PrivateEndpointConnectionPaged
from ._paged_models import PrivateLinkResourcePaged
from ._paged_models import SqlContainerGetResultsPaged
from ._paged_models import SqlDatabaseGetResultsPaged
from ._paged_models import SqlStoredProcedureGetResultsPaged
from ._paged_models import SqlTriggerGetResultsPaged
from ._paged_models import SqlUserDefinedFunctionGetResultsPaged
from ._paged_models import TableGetResultsPaged
from ._paged_models import UsagePaged
from ._cosmos_db_management_client_enums import (
    DatabaseAccountKind,
    DatabaseAccountOfferType,
    DefaultConsistencyLevel,
    ConnectorOffer,
    PublicNetworkAccess,
    ServerVersion,
    AnalyticalStorageSchemaType,
    IndexingMode,
    DataType,
    IndexKind,
    CompositePathSortOrder,
    SpatialType,
    PartitionKind,
    ConflictResolutionMode,
    TriggerType,
    TriggerOperation,
    KeyKind,
    UnitType,
    PrimaryAggregationType,
    BackupPolicyType,
)

__all__ = [
    'AnalyticalStorageConfig',
    'ApiProperties',
    'ARMProxyResource',
    'ARMResourceProperties',
    'AutoscaleSettings',
    'AutoscaleSettingsResource',
    'AutoUpgradePolicyResource',
    'AzureEntityResource',
    'BackupPolicy',
    'Capability',
    'CassandraKeyspaceCreateUpdateParameters',
    'CassandraKeyspaceGetPropertiesOptions',
    'CassandraKeyspaceGetPropertiesResource',
    'CassandraKeyspaceGetResults',
    'CassandraKeyspaceResource',
    'CassandraPartitionKey',
    'CassandraSchema',
    'CassandraTableCreateUpdateParameters',
    'CassandraTableGetPropertiesOptions',
    'CassandraTableGetPropertiesResource',
    'CassandraTableGetResults',
    'CassandraTableResource',
    'ClusterKey',
    'Column',
    'CompositePath',
    'ConflictResolutionPolicy',
    'ConsistencyPolicy',
    'ContainerPartitionKey',
    'ContinuousModeBackupPolicy',
    'CorsPolicy',
    'CreateUpdateOptions',
    'DatabaseAccountConnectionString',
    'DatabaseAccountCreateUpdateParameters',
    'DatabaseAccountGetResults',
    'DatabaseAccountListConnectionStringsResult',
    'DatabaseAccountListKeysResult',
    'DatabaseAccountListReadOnlyKeysResult',
    'DatabaseAccountRegenerateKeyParameters',
    'DatabaseAccountUpdateParameters',
    'ErrorResponse', 'ErrorResponseException',
    'ErrorResponseUpdatedFormat', 'ErrorResponseUpdatedFormatException',
    'ExcludedPath',
    'ExtendedResourceProperties',
    'FailoverPolicies',
    'FailoverPolicy',
    'GremlinDatabaseCreateUpdateParameters',
    'GremlinDatabaseGetPropertiesOptions',
    'GremlinDatabaseGetPropertiesResource',
    'GremlinDatabaseGetResults',
    'GremlinDatabaseResource',
    'GremlinGraphCreateUpdateParameters',
    'GremlinGraphGetPropertiesOptions',
    'GremlinGraphGetPropertiesResource',
    'GremlinGraphGetResults',
    'GremlinGraphResource',
    'IncludedPath',
    'Indexes',
    'IndexingPolicy',
    'IpAddressOrRange',
    'Location',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'MetricName',
    'MetricValue',
    'MongoDBCollectionCreateUpdateParameters',
    'MongoDBCollectionGetPropertiesOptions',
    'MongoDBCollectionGetPropertiesResource',
    'MongoDBCollectionGetResults',
    'MongoDBCollectionResource',
    'MongoDBDatabaseCreateUpdateParameters',
    'MongoDBDatabaseGetPropertiesOptions',
    'MongoDBDatabaseGetPropertiesResource',
    'MongoDBDatabaseGetResults',
    'MongoDBDatabaseResource',
    'MongoIndex',
    'MongoIndexKeys',
    'MongoIndexOptions',
    'NotebookWorkspace',
    'NotebookWorkspaceConnectionInfoResult',
    'NotebookWorkspaceCreateUpdateParameters',
    'Operation',
    'OperationDisplay',
    'OptionsResource',
    'PartitionMetric',
    'PartitionUsage',
    'PercentileMetric',
    'PercentileMetricValue',
    'PeriodicModeBackupPolicy',
    'PeriodicModeProperties',
    'PrivateEndpointConnection',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'RegionForOnlineOffline',
    'Resource',
    'SpatialSpec',
    'SqlContainerCreateUpdateParameters',
    'SqlContainerGetPropertiesOptions',
    'SqlContainerGetPropertiesResource',
    'SqlContainerGetResults',
    'SqlContainerResource',
    'SqlDatabaseCreateUpdateParameters',
    'SqlDatabaseGetPropertiesOptions',
    'SqlDatabaseGetPropertiesResource',
    'SqlDatabaseGetResults',
    'SqlDatabaseResource',
    'SqlStoredProcedureCreateUpdateParameters',
    'SqlStoredProcedureGetPropertiesResource',
    'SqlStoredProcedureGetResults',
    'SqlStoredProcedureResource',
    'SqlTriggerCreateUpdateParameters',
    'SqlTriggerGetPropertiesResource',
    'SqlTriggerGetResults',
    'SqlTriggerResource',
    'SqlUserDefinedFunctionCreateUpdateParameters',
    'SqlUserDefinedFunctionGetPropertiesResource',
    'SqlUserDefinedFunctionGetResults',
    'SqlUserDefinedFunctionResource',
    'TableCreateUpdateParameters',
    'TableGetPropertiesOptions',
    'TableGetPropertiesResource',
    'TableGetResults',
    'TableResource',
    'ThroughputPolicyResource',
    'ThroughputSettingsGetPropertiesResource',
    'ThroughputSettingsGetResults',
    'ThroughputSettingsResource',
    'ThroughputSettingsUpdateParameters',
    'TrackedResource',
    'UniqueKey',
    'UniqueKeyPolicy',
    'Usage',
    'VirtualNetworkRule',
    'DatabaseAccountGetResultsPaged',
    'MetricPaged',
    'UsagePaged',
    'MetricDefinitionPaged',
    'OperationPaged',
    'PercentileMetricPaged',
    'PartitionMetricPaged',
    'PartitionUsagePaged',
    'SqlDatabaseGetResultsPaged',
    'SqlContainerGetResultsPaged',
    'SqlStoredProcedureGetResultsPaged',
    'SqlUserDefinedFunctionGetResultsPaged',
    'SqlTriggerGetResultsPaged',
    'MongoDBDatabaseGetResultsPaged',
    'MongoDBCollectionGetResultsPaged',
    'TableGetResultsPaged',
    'CassandraKeyspaceGetResultsPaged',
    'CassandraTableGetResultsPaged',
    'GremlinDatabaseGetResultsPaged',
    'GremlinGraphGetResultsPaged',
    'NotebookWorkspacePaged',
    'PrivateLinkResourcePaged',
    'PrivateEndpointConnectionPaged',
    'DatabaseAccountKind',
    'DatabaseAccountOfferType',
    'DefaultConsistencyLevel',
    'ConnectorOffer',
    'PublicNetworkAccess',
    'ServerVersion',
    'AnalyticalStorageSchemaType',
    'IndexingMode',
    'DataType',
    'IndexKind',
    'CompositePathSortOrder',
    'SpatialType',
    'PartitionKind',
    'ConflictResolutionMode',
    'TriggerType',
    'TriggerOperation',
    'KeyKind',
    'UnitType',
    'PrimaryAggregationType',
    'BackupPolicyType',
]
