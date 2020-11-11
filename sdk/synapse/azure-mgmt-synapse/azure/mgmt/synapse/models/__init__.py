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
    from ._models_py3 import AutoPauseProperties
    from ._models_py3 import AutoScaleProperties
    from ._models_py3 import AvailableRpOperation
    from ._models_py3 import AvailableRpOperationDisplayInfo
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import BabylonConfiguration
    from ._models_py3 import BigDataPoolPatchInfo
    from ._models_py3 import BigDataPoolResourceInfo
    from ._models_py3 import CheckNameAvailabilityRequest
    from ._models_py3 import CheckNameAvailabilityResponse
    from ._models_py3 import CmdkeySetup
    from ._models_py3 import ComponentSetup
    from ._models_py3 import CreateSqlPoolRestorePointDefinition
    from ._models_py3 import CustomerManagedKeyDetails
    from ._models_py3 import CustomSetupBase
    from ._models_py3 import DataLakeStorageAccountDetails
    from ._models_py3 import DataMaskingPolicy
    from ._models_py3 import DataMaskingRule
    from ._models_py3 import DataWarehouseUserActivities
    from ._models_py3 import EncryptionDetails
    from ._models_py3 import EncryptionProtector
    from ._models_py3 import EntityReference
    from ._models_py3 import EnvironmentVariableSetup
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorContract, ErrorContractException
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExtendedServerBlobAuditingPolicy
    from ._models_py3 import ExtendedSqlPoolBlobAuditingPolicy
    from ._models_py3 import GeoBackupPolicy
    from ._models_py3 import GetSsisObjectMetadataRequest
    from ._models_py3 import IntegrationRuntime
    from ._models_py3 import IntegrationRuntimeAuthKeys
    from ._models_py3 import IntegrationRuntimeComputeProperties
    from ._models_py3 import IntegrationRuntimeConnectionInfo
    from ._models_py3 import IntegrationRuntimeCustomSetupScriptProperties
    from ._models_py3 import IntegrationRuntimeDataFlowProperties
    from ._models_py3 import IntegrationRuntimeDataProxyProperties
    from ._models_py3 import IntegrationRuntimeMonitoringData
    from ._models_py3 import IntegrationRuntimeNodeIpAddress
    from ._models_py3 import IntegrationRuntimeNodeMonitoringData
    from ._models_py3 import IntegrationRuntimeRegenerateKeyParameters
    from ._models_py3 import IntegrationRuntimeResource
    from ._models_py3 import IntegrationRuntimeSsisCatalogInfo
    from ._models_py3 import IntegrationRuntimeSsisProperties
    from ._models_py3 import IntegrationRuntimeStatus
    from ._models_py3 import IntegrationRuntimeStatusResponse
    from ._models_py3 import IntegrationRuntimeVNetProperties
    from ._models_py3 import IpFirewallRuleInfo
    from ._models_py3 import IpFirewallRuleProperties
    from ._models_py3 import Key
    from ._models_py3 import LibraryRequirements
    from ._models_py3 import LinkedIntegrationRuntime
    from ._models_py3 import LinkedIntegrationRuntimeKeyAuthorization
    from ._models_py3 import LinkedIntegrationRuntimeRbacAuthorization
    from ._models_py3 import LinkedIntegrationRuntimeType
    from ._models_py3 import ManagedIdentity
    from ._models_py3 import ManagedIdentitySqlControlSettingsModel
    from ._models_py3 import ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity
    from ._models_py3 import ManagedIntegrationRuntime
    from ._models_py3 import ManagedIntegrationRuntimeError
    from ._models_py3 import ManagedIntegrationRuntimeNode
    from ._models_py3 import ManagedIntegrationRuntimeOperationResult
    from ._models_py3 import ManagedIntegrationRuntimeStatus
    from ._models_py3 import ManagedVirtualNetworkSettings
    from ._models_py3 import MetadataSyncConfig
    from ._models_py3 import OperationMetaLogSpecification
    from ._models_py3 import OperationMetaMetricDimensionSpecification
    from ._models_py3 import OperationMetaMetricSpecification
    from ._models_py3 import OperationMetaServiceSpecification
    from ._models_py3 import OperationResource
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionForPrivateLinkHub
    from ._models_py3 import PrivateEndpointConnectionForPrivateLinkHubBasic
    from ._models_py3 import PrivateLinkHub
    from ._models_py3 import PrivateLinkHubPatchInfo
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyResource
    from ._models_py3 import QueryInterval
    from ._models_py3 import QueryMetric
    from ._models_py3 import QueryStatistic
    from ._models_py3 import RecoverableSqlPool
    from ._models_py3 import ReplaceAllFirewallRulesOperationResponse
    from ._models_py3 import ReplaceAllIpFirewallRulesRequest
    from ._models_py3 import ReplicationLink
    from ._models_py3 import Resource
    from ._models_py3 import ResourceMoveDefinition
    from ._models_py3 import RestorableDroppedSqlPool
    from ._models_py3 import RestorePoint
    from ._models_py3 import SecretBase
    from ._models_py3 import SecureString
    from ._models_py3 import SelfHostedIntegrationRuntime
    from ._models_py3 import SelfHostedIntegrationRuntimeNode
    from ._models_py3 import SelfHostedIntegrationRuntimeStatus
    from ._models_py3 import SensitivityLabel
    from ._models_py3 import ServerBlobAuditingPolicy
    from ._models_py3 import ServerSecurityAlertPolicy
    from ._models_py3 import ServerUsage
    from ._models_py3 import ServerVulnerabilityAssessment
    from ._models_py3 import Sku
    from ._models_py3 import SqlPool
    from ._models_py3 import SqlPoolBlobAuditingPolicy
    from ._models_py3 import SqlPoolColumn
    from ._models_py3 import SqlPoolConnectionPolicy
    from ._models_py3 import SqlPoolOperation
    from ._models_py3 import SqlPoolPatchInfo
    from ._models_py3 import SqlPoolSchema
    from ._models_py3 import SqlPoolSecurityAlertPolicy
    from ._models_py3 import SqlPoolTable
    from ._models_py3 import SqlPoolUsage
    from ._models_py3 import SqlPoolVulnerabilityAssessment
    from ._models_py3 import SqlPoolVulnerabilityAssessmentRuleBaseline
    from ._models_py3 import SqlPoolVulnerabilityAssessmentRuleBaselineItem
    from ._models_py3 import SqlPoolVulnerabilityAssessmentScansExport
    from ._models_py3 import SsisEnvironment
    from ._models_py3 import SsisEnvironmentReference
    from ._models_py3 import SsisFolder
    from ._models_py3 import SsisObjectMetadata
    from ._models_py3 import SsisObjectMetadataListResponse
    from ._models_py3 import SsisObjectMetadataStatusResponse
    from ._models_py3 import SsisPackage
    from ._models_py3 import SsisParameter
    from ._models_py3 import SsisProject
    from ._models_py3 import SsisVariable
    from ._models_py3 import SubResource
    from ._models_py3 import TopQueries
    from ._models_py3 import TopQueriesListResult
    from ._models_py3 import TrackedResource
    from ._models_py3 import TransparentDataEncryption
    from ._models_py3 import UpdateIntegrationRuntimeNodeRequest
    from ._models_py3 import UpdateIntegrationRuntimeRequest
    from ._models_py3 import VirtualNetworkProfile
    from ._models_py3 import VulnerabilityAssessmentRecurringScansProperties
    from ._models_py3 import VulnerabilityAssessmentScanError
    from ._models_py3 import VulnerabilityAssessmentScanRecord
    from ._models_py3 import WorkloadClassifier
    from ._models_py3 import WorkloadGroup
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceAadAdminInfo
    from ._models_py3 import WorkspaceKeyDetails
    from ._models_py3 import WorkspacePatchInfo
    from ._models_py3 import WorkspaceRepositoryConfiguration
except (SyntaxError, ImportError):
    from ._models import AutoPauseProperties
    from ._models import AutoScaleProperties
    from ._models import AvailableRpOperation
    from ._models import AvailableRpOperationDisplayInfo
    from ._models import AzureEntityResource
    from ._models import BabylonConfiguration
    from ._models import BigDataPoolPatchInfo
    from ._models import BigDataPoolResourceInfo
    from ._models import CheckNameAvailabilityRequest
    from ._models import CheckNameAvailabilityResponse
    from ._models import CmdkeySetup
    from ._models import ComponentSetup
    from ._models import CreateSqlPoolRestorePointDefinition
    from ._models import CustomerManagedKeyDetails
    from ._models import CustomSetupBase
    from ._models import DataLakeStorageAccountDetails
    from ._models import DataMaskingPolicy
    from ._models import DataMaskingRule
    from ._models import DataWarehouseUserActivities
    from ._models import EncryptionDetails
    from ._models import EncryptionProtector
    from ._models import EntityReference
    from ._models import EnvironmentVariableSetup
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorContract, ErrorContractException
    from ._models import ErrorDetail
    from ._models import ErrorResponse
    from ._models import ExtendedServerBlobAuditingPolicy
    from ._models import ExtendedSqlPoolBlobAuditingPolicy
    from ._models import GeoBackupPolicy
    from ._models import GetSsisObjectMetadataRequest
    from ._models import IntegrationRuntime
    from ._models import IntegrationRuntimeAuthKeys
    from ._models import IntegrationRuntimeComputeProperties
    from ._models import IntegrationRuntimeConnectionInfo
    from ._models import IntegrationRuntimeCustomSetupScriptProperties
    from ._models import IntegrationRuntimeDataFlowProperties
    from ._models import IntegrationRuntimeDataProxyProperties
    from ._models import IntegrationRuntimeMonitoringData
    from ._models import IntegrationRuntimeNodeIpAddress
    from ._models import IntegrationRuntimeNodeMonitoringData
    from ._models import IntegrationRuntimeRegenerateKeyParameters
    from ._models import IntegrationRuntimeResource
    from ._models import IntegrationRuntimeSsisCatalogInfo
    from ._models import IntegrationRuntimeSsisProperties
    from ._models import IntegrationRuntimeStatus
    from ._models import IntegrationRuntimeStatusResponse
    from ._models import IntegrationRuntimeVNetProperties
    from ._models import IpFirewallRuleInfo
    from ._models import IpFirewallRuleProperties
    from ._models import Key
    from ._models import LibraryRequirements
    from ._models import LinkedIntegrationRuntime
    from ._models import LinkedIntegrationRuntimeKeyAuthorization
    from ._models import LinkedIntegrationRuntimeRbacAuthorization
    from ._models import LinkedIntegrationRuntimeType
    from ._models import ManagedIdentity
    from ._models import ManagedIdentitySqlControlSettingsModel
    from ._models import ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity
    from ._models import ManagedIntegrationRuntime
    from ._models import ManagedIntegrationRuntimeError
    from ._models import ManagedIntegrationRuntimeNode
    from ._models import ManagedIntegrationRuntimeOperationResult
    from ._models import ManagedIntegrationRuntimeStatus
    from ._models import ManagedVirtualNetworkSettings
    from ._models import MetadataSyncConfig
    from ._models import OperationMetaLogSpecification
    from ._models import OperationMetaMetricDimensionSpecification
    from ._models import OperationMetaMetricSpecification
    from ._models import OperationMetaServiceSpecification
    from ._models import OperationResource
    from ._models import PrivateEndpoint
    from ._models import PrivateEndpointConnection
    from ._models import PrivateEndpointConnectionForPrivateLinkHub
    from ._models import PrivateEndpointConnectionForPrivateLinkHubBasic
    from ._models import PrivateLinkHub
    from ._models import PrivateLinkHubPatchInfo
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkResourceProperties
    from ._models import PrivateLinkServiceConnectionState
    from ._models import ProxyResource
    from ._models import QueryInterval
    from ._models import QueryMetric
    from ._models import QueryStatistic
    from ._models import RecoverableSqlPool
    from ._models import ReplaceAllFirewallRulesOperationResponse
    from ._models import ReplaceAllIpFirewallRulesRequest
    from ._models import ReplicationLink
    from ._models import Resource
    from ._models import ResourceMoveDefinition
    from ._models import RestorableDroppedSqlPool
    from ._models import RestorePoint
    from ._models import SecretBase
    from ._models import SecureString
    from ._models import SelfHostedIntegrationRuntime
    from ._models import SelfHostedIntegrationRuntimeNode
    from ._models import SelfHostedIntegrationRuntimeStatus
    from ._models import SensitivityLabel
    from ._models import ServerBlobAuditingPolicy
    from ._models import ServerSecurityAlertPolicy
    from ._models import ServerUsage
    from ._models import ServerVulnerabilityAssessment
    from ._models import Sku
    from ._models import SqlPool
    from ._models import SqlPoolBlobAuditingPolicy
    from ._models import SqlPoolColumn
    from ._models import SqlPoolConnectionPolicy
    from ._models import SqlPoolOperation
    from ._models import SqlPoolPatchInfo
    from ._models import SqlPoolSchema
    from ._models import SqlPoolSecurityAlertPolicy
    from ._models import SqlPoolTable
    from ._models import SqlPoolUsage
    from ._models import SqlPoolVulnerabilityAssessment
    from ._models import SqlPoolVulnerabilityAssessmentRuleBaseline
    from ._models import SqlPoolVulnerabilityAssessmentRuleBaselineItem
    from ._models import SqlPoolVulnerabilityAssessmentScansExport
    from ._models import SsisEnvironment
    from ._models import SsisEnvironmentReference
    from ._models import SsisFolder
    from ._models import SsisObjectMetadata
    from ._models import SsisObjectMetadataListResponse
    from ._models import SsisObjectMetadataStatusResponse
    from ._models import SsisPackage
    from ._models import SsisParameter
    from ._models import SsisProject
    from ._models import SsisVariable
    from ._models import SubResource
    from ._models import TopQueries
    from ._models import TopQueriesListResult
    from ._models import TrackedResource
    from ._models import TransparentDataEncryption
    from ._models import UpdateIntegrationRuntimeNodeRequest
    from ._models import UpdateIntegrationRuntimeRequest
    from ._models import VirtualNetworkProfile
    from ._models import VulnerabilityAssessmentRecurringScansProperties
    from ._models import VulnerabilityAssessmentScanError
    from ._models import VulnerabilityAssessmentScanRecord
    from ._models import WorkloadClassifier
    from ._models import WorkloadGroup
    from ._models import Workspace
    from ._models import WorkspaceAadAdminInfo
    from ._models import WorkspaceKeyDetails
    from ._models import WorkspacePatchInfo
    from ._models import WorkspaceRepositoryConfiguration
from ._paged_models import BigDataPoolResourceInfoPaged
from ._paged_models import DataMaskingRulePaged
from ._paged_models import EncryptionProtectorPaged
from ._paged_models import ExtendedServerBlobAuditingPolicyPaged
from ._paged_models import ExtendedSqlPoolBlobAuditingPolicyPaged
from ._paged_models import GeoBackupPolicyPaged
from ._paged_models import IntegrationRuntimeResourcePaged
from ._paged_models import IpFirewallRuleInfoPaged
from ._paged_models import KeyPaged
from ._paged_models import PrivateEndpointConnectionForPrivateLinkHubPaged
from ._paged_models import PrivateEndpointConnectionPaged
from ._paged_models import PrivateLinkHubPaged
from ._paged_models import PrivateLinkResourcePaged
from ._paged_models import RecoverableSqlPoolPaged
from ._paged_models import ReplicationLinkPaged
from ._paged_models import RestorableDroppedSqlPoolPaged
from ._paged_models import RestorePointPaged
from ._paged_models import SensitivityLabelPaged
from ._paged_models import ServerBlobAuditingPolicyPaged
from ._paged_models import ServerSecurityAlertPolicyPaged
from ._paged_models import ServerUsagePaged
from ._paged_models import ServerVulnerabilityAssessmentPaged
from ._paged_models import SqlPoolBlobAuditingPolicyPaged
from ._paged_models import SqlPoolColumnPaged
from ._paged_models import SqlPoolOperationPaged
from ._paged_models import SqlPoolPaged
from ._paged_models import SqlPoolSchemaPaged
from ._paged_models import SqlPoolSecurityAlertPolicyPaged
from ._paged_models import SqlPoolTablePaged
from ._paged_models import SqlPoolUsagePaged
from ._paged_models import SqlPoolVulnerabilityAssessmentPaged
from ._paged_models import TransparentDataEncryptionPaged
from ._paged_models import VulnerabilityAssessmentScanRecordPaged
from ._paged_models import WorkloadClassifierPaged
from ._paged_models import WorkloadGroupPaged
from ._paged_models import WorkspacePaged
from ._synapse_management_client_enums import (
    NodeSize,
    NodeSizeFamily,
    ProvisioningState,
    OperationStatus,
    GeoBackupPolicyState,
    QueryAggregationFunction,
    QueryExecutionType,
    QueryObservedMetricType,
    QueryMetricUnit,
    RestorePointType,
    ReplicationRole,
    ReplicationState,
    TransparentDataEncryptionStatus,
    BlobAuditingPolicyState,
    ManagementOperationState,
    ColumnDataType,
    VulnerabilityAssessmentScanTriggerType,
    VulnerabilityAssessmentScanState,
    SecurityAlertPolicyState,
    DataMaskingState,
    DataMaskingRuleState,
    DataMaskingFunction,
    ResourceIdentityType,
    IntegrationRuntimeType,
    IntegrationRuntimeState,
    DataFlowComputeType,
    IntegrationRuntimeSsisCatalogPricingTier,
    IntegrationRuntimeLicenseType,
    IntegrationRuntimeEntityReferenceType,
    IntegrationRuntimeEdition,
    ManagedIntegrationRuntimeNodeStatus,
    IntegrationRuntimeInternalChannelEncryptionMode,
    SelfHostedIntegrationRuntimeNodeStatus,
    IntegrationRuntimeUpdateResult,
    IntegrationRuntimeAutoUpdate,
    IntegrationRuntimeAuthKeyName,
    SsisObjectMetadataType,
    ServerKeyType,
    SensitivityLabelSource,
    VulnerabilityAssessmentPolicyBaselineName,
)

__all__ = [
    'AutoPauseProperties',
    'AutoScaleProperties',
    'AvailableRpOperation',
    'AvailableRpOperationDisplayInfo',
    'AzureEntityResource',
    'BabylonConfiguration',
    'BigDataPoolPatchInfo',
    'BigDataPoolResourceInfo',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'CmdkeySetup',
    'ComponentSetup',
    'CreateSqlPoolRestorePointDefinition',
    'CustomerManagedKeyDetails',
    'CustomSetupBase',
    'DataLakeStorageAccountDetails',
    'DataMaskingPolicy',
    'DataMaskingRule',
    'DataWarehouseUserActivities',
    'EncryptionDetails',
    'EncryptionProtector',
    'EntityReference',
    'EnvironmentVariableSetup',
    'ErrorAdditionalInfo',
    'ErrorContract', 'ErrorContractException',
    'ErrorDetail',
    'ErrorResponse',
    'ExtendedServerBlobAuditingPolicy',
    'ExtendedSqlPoolBlobAuditingPolicy',
    'GeoBackupPolicy',
    'GetSsisObjectMetadataRequest',
    'IntegrationRuntime',
    'IntegrationRuntimeAuthKeys',
    'IntegrationRuntimeComputeProperties',
    'IntegrationRuntimeConnectionInfo',
    'IntegrationRuntimeCustomSetupScriptProperties',
    'IntegrationRuntimeDataFlowProperties',
    'IntegrationRuntimeDataProxyProperties',
    'IntegrationRuntimeMonitoringData',
    'IntegrationRuntimeNodeIpAddress',
    'IntegrationRuntimeNodeMonitoringData',
    'IntegrationRuntimeRegenerateKeyParameters',
    'IntegrationRuntimeResource',
    'IntegrationRuntimeSsisCatalogInfo',
    'IntegrationRuntimeSsisProperties',
    'IntegrationRuntimeStatus',
    'IntegrationRuntimeStatusResponse',
    'IntegrationRuntimeVNetProperties',
    'IpFirewallRuleInfo',
    'IpFirewallRuleProperties',
    'Key',
    'LibraryRequirements',
    'LinkedIntegrationRuntime',
    'LinkedIntegrationRuntimeKeyAuthorization',
    'LinkedIntegrationRuntimeRbacAuthorization',
    'LinkedIntegrationRuntimeType',
    'ManagedIdentity',
    'ManagedIdentitySqlControlSettingsModel',
    'ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity',
    'ManagedIntegrationRuntime',
    'ManagedIntegrationRuntimeError',
    'ManagedIntegrationRuntimeNode',
    'ManagedIntegrationRuntimeOperationResult',
    'ManagedIntegrationRuntimeStatus',
    'ManagedVirtualNetworkSettings',
    'MetadataSyncConfig',
    'OperationMetaLogSpecification',
    'OperationMetaMetricDimensionSpecification',
    'OperationMetaMetricSpecification',
    'OperationMetaServiceSpecification',
    'OperationResource',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionForPrivateLinkHub',
    'PrivateEndpointConnectionForPrivateLinkHubBasic',
    'PrivateLinkHub',
    'PrivateLinkHubPatchInfo',
    'PrivateLinkResource',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'QueryInterval',
    'QueryMetric',
    'QueryStatistic',
    'RecoverableSqlPool',
    'ReplaceAllFirewallRulesOperationResponse',
    'ReplaceAllIpFirewallRulesRequest',
    'ReplicationLink',
    'Resource',
    'ResourceMoveDefinition',
    'RestorableDroppedSqlPool',
    'RestorePoint',
    'SecretBase',
    'SecureString',
    'SelfHostedIntegrationRuntime',
    'SelfHostedIntegrationRuntimeNode',
    'SelfHostedIntegrationRuntimeStatus',
    'SensitivityLabel',
    'ServerBlobAuditingPolicy',
    'ServerSecurityAlertPolicy',
    'ServerUsage',
    'ServerVulnerabilityAssessment',
    'Sku',
    'SqlPool',
    'SqlPoolBlobAuditingPolicy',
    'SqlPoolColumn',
    'SqlPoolConnectionPolicy',
    'SqlPoolOperation',
    'SqlPoolPatchInfo',
    'SqlPoolSchema',
    'SqlPoolSecurityAlertPolicy',
    'SqlPoolTable',
    'SqlPoolUsage',
    'SqlPoolVulnerabilityAssessment',
    'SqlPoolVulnerabilityAssessmentRuleBaseline',
    'SqlPoolVulnerabilityAssessmentRuleBaselineItem',
    'SqlPoolVulnerabilityAssessmentScansExport',
    'SsisEnvironment',
    'SsisEnvironmentReference',
    'SsisFolder',
    'SsisObjectMetadata',
    'SsisObjectMetadataListResponse',
    'SsisObjectMetadataStatusResponse',
    'SsisPackage',
    'SsisParameter',
    'SsisProject',
    'SsisVariable',
    'SubResource',
    'TopQueries',
    'TopQueriesListResult',
    'TrackedResource',
    'TransparentDataEncryption',
    'UpdateIntegrationRuntimeNodeRequest',
    'UpdateIntegrationRuntimeRequest',
    'VirtualNetworkProfile',
    'VulnerabilityAssessmentRecurringScansProperties',
    'VulnerabilityAssessmentScanError',
    'VulnerabilityAssessmentScanRecord',
    'WorkloadClassifier',
    'WorkloadGroup',
    'Workspace',
    'WorkspaceAadAdminInfo',
    'WorkspaceKeyDetails',
    'WorkspacePatchInfo',
    'WorkspaceRepositoryConfiguration',
    'BigDataPoolResourceInfoPaged',
    'IpFirewallRuleInfoPaged',
    'SqlPoolPaged',
    'GeoBackupPolicyPaged',
    'RestorePointPaged',
    'ReplicationLinkPaged',
    'TransparentDataEncryptionPaged',
    'SqlPoolBlobAuditingPolicyPaged',
    'SqlPoolOperationPaged',
    'SqlPoolUsagePaged',
    'SensitivityLabelPaged',
    'SqlPoolSchemaPaged',
    'SqlPoolTablePaged',
    'SqlPoolColumnPaged',
    'SqlPoolVulnerabilityAssessmentPaged',
    'VulnerabilityAssessmentScanRecordPaged',
    'SqlPoolSecurityAlertPolicyPaged',
    'ExtendedSqlPoolBlobAuditingPolicyPaged',
    'DataMaskingRulePaged',
    'WorkloadGroupPaged',
    'WorkloadClassifierPaged',
    'WorkspacePaged',
    'RestorableDroppedSqlPoolPaged',
    'IntegrationRuntimeResourcePaged',
    'PrivateLinkResourcePaged',
    'PrivateEndpointConnectionPaged',
    'PrivateLinkHubPaged',
    'PrivateEndpointConnectionForPrivateLinkHubPaged',
    'ServerBlobAuditingPolicyPaged',
    'ExtendedServerBlobAuditingPolicyPaged',
    'ServerSecurityAlertPolicyPaged',
    'ServerVulnerabilityAssessmentPaged',
    'EncryptionProtectorPaged',
    'ServerUsagePaged',
    'RecoverableSqlPoolPaged',
    'KeyPaged',
    'NodeSize',
    'NodeSizeFamily',
    'ProvisioningState',
    'OperationStatus',
    'GeoBackupPolicyState',
    'QueryAggregationFunction',
    'QueryExecutionType',
    'QueryObservedMetricType',
    'QueryMetricUnit',
    'RestorePointType',
    'ReplicationRole',
    'ReplicationState',
    'TransparentDataEncryptionStatus',
    'BlobAuditingPolicyState',
    'ManagementOperationState',
    'ColumnDataType',
    'VulnerabilityAssessmentScanTriggerType',
    'VulnerabilityAssessmentScanState',
    'SecurityAlertPolicyState',
    'DataMaskingState',
    'DataMaskingRuleState',
    'DataMaskingFunction',
    'ResourceIdentityType',
    'IntegrationRuntimeType',
    'IntegrationRuntimeState',
    'DataFlowComputeType',
    'IntegrationRuntimeSsisCatalogPricingTier',
    'IntegrationRuntimeLicenseType',
    'IntegrationRuntimeEntityReferenceType',
    'IntegrationRuntimeEdition',
    'ManagedIntegrationRuntimeNodeStatus',
    'IntegrationRuntimeInternalChannelEncryptionMode',
    'SelfHostedIntegrationRuntimeNodeStatus',
    'IntegrationRuntimeUpdateResult',
    'IntegrationRuntimeAutoUpdate',
    'IntegrationRuntimeAuthKeyName',
    'SsisObjectMetadataType',
    'ServerKeyType',
    'SensitivityLabelSource',
    'VulnerabilityAssessmentPolicyBaselineName',
]
