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
    from ._models_py3 import ACIServiceCreateRequest
    from ._models_py3 import ACIServiceCreateRequestDataCollection
    from ._models_py3 import ACIServiceCreateRequestEncryptionProperties
    from ._models_py3 import ACIServiceCreateRequestVnetConfiguration
    from ._models_py3 import ACIServiceResponse
    from ._models_py3 import ACIServiceResponseDataCollection
    from ._models_py3 import ACIServiceResponseEncryptionProperties
    from ._models_py3 import ACIServiceResponseEnvironmentImageRequest
    from ._models_py3 import ACIServiceResponseVnetConfiguration
    from ._models_py3 import AKS
    from ._models_py3 import AksComputeSecrets
    from ._models_py3 import AksNetworkingConfiguration
    from ._models_py3 import AKSProperties
    from ._models_py3 import AKSReplicaStatus
    from ._models_py3 import AKSReplicaStatusError
    from ._models_py3 import AKSServiceCreateRequest
    from ._models_py3 import AKSServiceCreateRequestAutoScaler
    from ._models_py3 import AKSServiceCreateRequestDataCollection
    from ._models_py3 import AKSServiceCreateRequestLivenessProbeRequirements
    from ._models_py3 import AKSServiceResponse
    from ._models_py3 import AKSServiceResponseAutoScaler
    from ._models_py3 import AKSServiceResponseDataCollection
    from ._models_py3 import AKSServiceResponseDeploymentStatus
    from ._models_py3 import AKSServiceResponseEnvironmentImageRequest
    from ._models_py3 import AKSServiceResponseLivenessProbeRequirements
    from ._models_py3 import AKSVariantResponse
    from ._models_py3 import AmlCompute
    from ._models_py3 import AmlComputeNodeInformation
    from ._models_py3 import AmlComputeProperties
    from ._models_py3 import AmlUserFeature
    from ._models_py3 import AssignedUser
    from ._models_py3 import AuthKeys
    from ._models_py3 import AutoScaler
    from ._models_py3 import ClusterUpdateParameters
    from ._models_py3 import Compute
    from ._models_py3 import ComputeInstance
    from ._models_py3 import ComputeInstanceApplication
    from ._models_py3 import ComputeInstanceConnectivityEndpoints
    from ._models_py3 import ComputeInstanceCreatedBy
    from ._models_py3 import ComputeInstanceLastOperation
    from ._models_py3 import ComputeInstanceProperties
    from ._models_py3 import ComputeInstanceSshSettings
    from ._models_py3 import ComputeNodesInformation
    from ._models_py3 import ComputeResource
    from ._models_py3 import ComputeSecrets
    from ._models_py3 import ContainerRegistry
    from ._models_py3 import ContainerRegistryResponse
    from ._models_py3 import ContainerResourceRequirements
    from ._models_py3 import CosmosDbSettings
    from ._models_py3 import CreateEndpointVariantRequest
    from ._models_py3 import CreateServiceRequest
    from ._models_py3 import CreateServiceRequestEnvironmentImageRequest
    from ._models_py3 import CreateServiceRequestKeys
    from ._models_py3 import Databricks
    from ._models_py3 import DatabricksComputeSecrets
    from ._models_py3 import DatabricksProperties
    from ._models_py3 import DataFactory
    from ._models_py3 import DataLakeAnalytics
    from ._models_py3 import DataLakeAnalyticsProperties
    from ._models_py3 import DatasetReference
    from ._models_py3 import EncryptionProperties
    from ._models_py3 import EncryptionProperty
    from ._models_py3 import EnvironmentImageRequest
    from ._models_py3 import EnvironmentImageRequestEnvironment
    from ._models_py3 import EnvironmentImageRequestEnvironmentReference
    from ._models_py3 import EnvironmentImageResponse
    from ._models_py3 import EnvironmentImageResponseEnvironment
    from ._models_py3 import EnvironmentImageResponseEnvironmentReference
    from ._models_py3 import EnvironmentReference
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EstimatedVMPrice
    from ._models_py3 import EstimatedVMPrices
    from ._models_py3 import HDInsight
    from ._models_py3 import HDInsightProperties
    from ._models_py3 import Identity
    from ._models_py3 import IdentityForCmk
    from ._models_py3 import ImageAsset
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import ListNotebookKeysResult
    from ._models_py3 import ListStorageAccountKeysResult
    from ._models_py3 import ListWorkspaceKeysResult
    from ._models_py3 import LivenessProbeRequirements
    from ._models_py3 import MachineLearningServiceError, MachineLearningServiceErrorException
    from ._models_py3 import Model
    from ._models_py3 import ModelDataCollection
    from ._models_py3 import ModelDockerSection
    from ._models_py3 import ModelDockerSectionBaseImageRegistry
    from ._models_py3 import ModelDockerSectionResponse
    from ._models_py3 import ModelDockerSectionResponseBaseImageRegistry
    from ._models_py3 import ModelEnvironmentDefinition
    from ._models_py3 import ModelEnvironmentDefinitionDocker
    from ._models_py3 import ModelEnvironmentDefinitionPython
    from ._models_py3 import ModelEnvironmentDefinitionR
    from ._models_py3 import ModelEnvironmentDefinitionResponse
    from ._models_py3 import ModelEnvironmentDefinitionResponseDocker
    from ._models_py3 import ModelEnvironmentDefinitionResponsePython
    from ._models_py3 import ModelEnvironmentDefinitionResponseR
    from ._models_py3 import ModelEnvironmentDefinitionResponseSpark
    from ._models_py3 import ModelEnvironmentDefinitionSpark
    from ._models_py3 import ModelPythonSection
    from ._models_py3 import ModelSparkSection
    from ._models_py3 import NodeStateCounts
    from ._models_py3 import NotebookAccessTokenResult
    from ._models_py3 import NotebookPreparationError
    from ._models_py3 import NotebookResourceInfo
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Password
    from ._models_py3 import PersonalComputeInstanceSettings
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import QuotaBaseProperties
    from ._models_py3 import QuotaUpdateParameters
    from ._models_py3 import RCranPackage
    from ._models_py3 import RegistryListCredentialsResult
    from ._models_py3 import Resource
    from ._models_py3 import ResourceId
    from ._models_py3 import ResourceName
    from ._models_py3 import ResourceQuota
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkuZoneDetails
    from ._models_py3 import Restriction
    from ._models_py3 import RGitHubPackage
    from ._models_py3 import RGitHubPackageResponse
    from ._models_py3 import RSection
    from ._models_py3 import RSectionResponse
    from ._models_py3 import ScaleSettings
    from ._models_py3 import ScriptReference
    from ._models_py3 import ScriptsToExecute
    from ._models_py3 import ServiceManagedResourcesSettings
    from ._models_py3 import ServicePrincipalCredentials
    from ._models_py3 import ServiceResource
    from ._models_py3 import ServiceResponseBase
    from ._models_py3 import ServiceResponseBaseError
    from ._models_py3 import SetupScripts
    from ._models_py3 import SharedPrivateLinkResource
    from ._models_py3 import Sku
    from ._models_py3 import SKUCapability
    from ._models_py3 import SparkMavenPackage
    from ._models_py3 import SslConfiguration
    from ._models_py3 import SystemData
    from ._models_py3 import SystemService
    from ._models_py3 import UpdateWorkspaceQuotas
    from ._models_py3 import UpdateWorkspaceQuotasResult
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UserAccountCredentials
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineImage
    from ._models_py3 import VirtualMachineProperties
    from ._models_py3 import VirtualMachineSecrets
    from ._models_py3 import VirtualMachineSize
    from ._models_py3 import VirtualMachineSizeListResult
    from ._models_py3 import VirtualMachineSshCredentials
    from ._models_py3 import VnetConfiguration
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceConnection
    from ._models_py3 import WorkspaceConnectionDto
    from ._models_py3 import WorkspaceSku
    from ._models_py3 import WorkspaceUpdateParameters
except (SyntaxError, ImportError):
    from ._models import ACIServiceCreateRequest
    from ._models import ACIServiceCreateRequestDataCollection
    from ._models import ACIServiceCreateRequestEncryptionProperties
    from ._models import ACIServiceCreateRequestVnetConfiguration
    from ._models import ACIServiceResponse
    from ._models import ACIServiceResponseDataCollection
    from ._models import ACIServiceResponseEncryptionProperties
    from ._models import ACIServiceResponseEnvironmentImageRequest
    from ._models import ACIServiceResponseVnetConfiguration
    from ._models import AKS
    from ._models import AksComputeSecrets
    from ._models import AksNetworkingConfiguration
    from ._models import AKSProperties
    from ._models import AKSReplicaStatus
    from ._models import AKSReplicaStatusError
    from ._models import AKSServiceCreateRequest
    from ._models import AKSServiceCreateRequestAutoScaler
    from ._models import AKSServiceCreateRequestDataCollection
    from ._models import AKSServiceCreateRequestLivenessProbeRequirements
    from ._models import AKSServiceResponse
    from ._models import AKSServiceResponseAutoScaler
    from ._models import AKSServiceResponseDataCollection
    from ._models import AKSServiceResponseDeploymentStatus
    from ._models import AKSServiceResponseEnvironmentImageRequest
    from ._models import AKSServiceResponseLivenessProbeRequirements
    from ._models import AKSVariantResponse
    from ._models import AmlCompute
    from ._models import AmlComputeNodeInformation
    from ._models import AmlComputeProperties
    from ._models import AmlUserFeature
    from ._models import AssignedUser
    from ._models import AuthKeys
    from ._models import AutoScaler
    from ._models import ClusterUpdateParameters
    from ._models import Compute
    from ._models import ComputeInstance
    from ._models import ComputeInstanceApplication
    from ._models import ComputeInstanceConnectivityEndpoints
    from ._models import ComputeInstanceCreatedBy
    from ._models import ComputeInstanceLastOperation
    from ._models import ComputeInstanceProperties
    from ._models import ComputeInstanceSshSettings
    from ._models import ComputeNodesInformation
    from ._models import ComputeResource
    from ._models import ComputeSecrets
    from ._models import ContainerRegistry
    from ._models import ContainerRegistryResponse
    from ._models import ContainerResourceRequirements
    from ._models import CosmosDbSettings
    from ._models import CreateEndpointVariantRequest
    from ._models import CreateServiceRequest
    from ._models import CreateServiceRequestEnvironmentImageRequest
    from ._models import CreateServiceRequestKeys
    from ._models import Databricks
    from ._models import DatabricksComputeSecrets
    from ._models import DatabricksProperties
    from ._models import DataFactory
    from ._models import DataLakeAnalytics
    from ._models import DataLakeAnalyticsProperties
    from ._models import DatasetReference
    from ._models import EncryptionProperties
    from ._models import EncryptionProperty
    from ._models import EnvironmentImageRequest
    from ._models import EnvironmentImageRequestEnvironment
    from ._models import EnvironmentImageRequestEnvironmentReference
    from ._models import EnvironmentImageResponse
    from ._models import EnvironmentImageResponseEnvironment
    from ._models import EnvironmentImageResponseEnvironmentReference
    from ._models import EnvironmentReference
    from ._models import ErrorDetail
    from ._models import ErrorResponse
    from ._models import EstimatedVMPrice
    from ._models import EstimatedVMPrices
    from ._models import HDInsight
    from ._models import HDInsightProperties
    from ._models import Identity
    from ._models import IdentityForCmk
    from ._models import ImageAsset
    from ._models import KeyVaultProperties
    from ._models import ListNotebookKeysResult
    from ._models import ListStorageAccountKeysResult
    from ._models import ListWorkspaceKeysResult
    from ._models import LivenessProbeRequirements
    from ._models import MachineLearningServiceError, MachineLearningServiceErrorException
    from ._models import Model
    from ._models import ModelDataCollection
    from ._models import ModelDockerSection
    from ._models import ModelDockerSectionBaseImageRegistry
    from ._models import ModelDockerSectionResponse
    from ._models import ModelDockerSectionResponseBaseImageRegistry
    from ._models import ModelEnvironmentDefinition
    from ._models import ModelEnvironmentDefinitionDocker
    from ._models import ModelEnvironmentDefinitionPython
    from ._models import ModelEnvironmentDefinitionR
    from ._models import ModelEnvironmentDefinitionResponse
    from ._models import ModelEnvironmentDefinitionResponseDocker
    from ._models import ModelEnvironmentDefinitionResponsePython
    from ._models import ModelEnvironmentDefinitionResponseR
    from ._models import ModelEnvironmentDefinitionResponseSpark
    from ._models import ModelEnvironmentDefinitionSpark
    from ._models import ModelPythonSection
    from ._models import ModelSparkSection
    from ._models import NodeStateCounts
    from ._models import NotebookAccessTokenResult
    from ._models import NotebookPreparationError
    from ._models import NotebookResourceInfo
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Password
    from ._models import PersonalComputeInstanceSettings
    from ._models import PrivateEndpoint
    from ._models import PrivateEndpointConnection
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkResourceListResult
    from ._models import PrivateLinkServiceConnectionState
    from ._models import QuotaBaseProperties
    from ._models import QuotaUpdateParameters
    from ._models import RCranPackage
    from ._models import RegistryListCredentialsResult
    from ._models import Resource
    from ._models import ResourceId
    from ._models import ResourceName
    from ._models import ResourceQuota
    from ._models import ResourceSkuLocationInfo
    from ._models import ResourceSkuZoneDetails
    from ._models import Restriction
    from ._models import RGitHubPackage
    from ._models import RGitHubPackageResponse
    from ._models import RSection
    from ._models import RSectionResponse
    from ._models import ScaleSettings
    from ._models import ScriptReference
    from ._models import ScriptsToExecute
    from ._models import ServiceManagedResourcesSettings
    from ._models import ServicePrincipalCredentials
    from ._models import ServiceResource
    from ._models import ServiceResponseBase
    from ._models import ServiceResponseBaseError
    from ._models import SetupScripts
    from ._models import SharedPrivateLinkResource
    from ._models import Sku
    from ._models import SKUCapability
    from ._models import SparkMavenPackage
    from ._models import SslConfiguration
    from ._models import SystemData
    from ._models import SystemService
    from ._models import UpdateWorkspaceQuotas
    from ._models import UpdateWorkspaceQuotasResult
    from ._models import Usage
    from ._models import UsageName
    from ._models import UserAccountCredentials
    from ._models import UserAssignedIdentity
    from ._models import VirtualMachine
    from ._models import VirtualMachineImage
    from ._models import VirtualMachineProperties
    from ._models import VirtualMachineSecrets
    from ._models import VirtualMachineSize
    from ._models import VirtualMachineSizeListResult
    from ._models import VirtualMachineSshCredentials
    from ._models import VnetConfiguration
    from ._models import Workspace
    from ._models import WorkspaceConnection
    from ._models import WorkspaceConnectionDto
    from ._models import WorkspaceSku
    from ._models import WorkspaceUpdateParameters
from ._paged_models import AmlComputeNodeInformationPaged
from ._paged_models import AmlUserFeaturePaged
from ._paged_models import ComputeResourcePaged
from ._paged_models import OperationPaged
from ._paged_models import ResourceQuotaPaged
from ._paged_models import ServiceResourcePaged
from ._paged_models import UsagePaged
from ._paged_models import WorkspaceConnectionPaged
from ._paged_models import WorkspacePaged
from ._paged_models import WorkspaceSkuPaged
from ._azure_machine_learning_workspaces_enums import (
    ProvisioningState,
    EncryptionStatus,
    PrivateEndpointServiceConnectionStatus,
    PrivateEndpointConnectionProvisioningState,
    ResourceIdentityType,
    UsageUnit,
    VMPriceOSType,
    VMTier,
    QuotaUnit,
    Status,
    IdentityType,
    ClusterPurpose,
    OsType,
    VmPriority,
    RemoteLoginPortPublicAccess,
    AllocationState,
    ApplicationSharingPolicy,
    SshPublicAccess,
    ComputeInstanceState,
    ComputeInstanceAuthorizationType,
    OperationName,
    OperationStatus,
    NodeState,
    ComputeType,
    ReasonCode,
    WebServiceState,
    DeploymentType,
    VariantType,
    ValueFormat,
    UnderlyingResourceAction,
    OrderString,
)

__all__ = [
    'ACIServiceCreateRequest',
    'ACIServiceCreateRequestDataCollection',
    'ACIServiceCreateRequestEncryptionProperties',
    'ACIServiceCreateRequestVnetConfiguration',
    'ACIServiceResponse',
    'ACIServiceResponseDataCollection',
    'ACIServiceResponseEncryptionProperties',
    'ACIServiceResponseEnvironmentImageRequest',
    'ACIServiceResponseVnetConfiguration',
    'AKS',
    'AksComputeSecrets',
    'AksNetworkingConfiguration',
    'AKSProperties',
    'AKSReplicaStatus',
    'AKSReplicaStatusError',
    'AKSServiceCreateRequest',
    'AKSServiceCreateRequestAutoScaler',
    'AKSServiceCreateRequestDataCollection',
    'AKSServiceCreateRequestLivenessProbeRequirements',
    'AKSServiceResponse',
    'AKSServiceResponseAutoScaler',
    'AKSServiceResponseDataCollection',
    'AKSServiceResponseDeploymentStatus',
    'AKSServiceResponseEnvironmentImageRequest',
    'AKSServiceResponseLivenessProbeRequirements',
    'AKSVariantResponse',
    'AmlCompute',
    'AmlComputeNodeInformation',
    'AmlComputeProperties',
    'AmlUserFeature',
    'AssignedUser',
    'AuthKeys',
    'AutoScaler',
    'ClusterUpdateParameters',
    'Compute',
    'ComputeInstance',
    'ComputeInstanceApplication',
    'ComputeInstanceConnectivityEndpoints',
    'ComputeInstanceCreatedBy',
    'ComputeInstanceLastOperation',
    'ComputeInstanceProperties',
    'ComputeInstanceSshSettings',
    'ComputeNodesInformation',
    'ComputeResource',
    'ComputeSecrets',
    'ContainerRegistry',
    'ContainerRegistryResponse',
    'ContainerResourceRequirements',
    'CosmosDbSettings',
    'CreateEndpointVariantRequest',
    'CreateServiceRequest',
    'CreateServiceRequestEnvironmentImageRequest',
    'CreateServiceRequestKeys',
    'Databricks',
    'DatabricksComputeSecrets',
    'DatabricksProperties',
    'DataFactory',
    'DataLakeAnalytics',
    'DataLakeAnalyticsProperties',
    'DatasetReference',
    'EncryptionProperties',
    'EncryptionProperty',
    'EnvironmentImageRequest',
    'EnvironmentImageRequestEnvironment',
    'EnvironmentImageRequestEnvironmentReference',
    'EnvironmentImageResponse',
    'EnvironmentImageResponseEnvironment',
    'EnvironmentImageResponseEnvironmentReference',
    'EnvironmentReference',
    'ErrorDetail',
    'ErrorResponse',
    'EstimatedVMPrice',
    'EstimatedVMPrices',
    'HDInsight',
    'HDInsightProperties',
    'Identity',
    'IdentityForCmk',
    'ImageAsset',
    'KeyVaultProperties',
    'ListNotebookKeysResult',
    'ListStorageAccountKeysResult',
    'ListWorkspaceKeysResult',
    'LivenessProbeRequirements',
    'MachineLearningServiceError', 'MachineLearningServiceErrorException',
    'Model',
    'ModelDataCollection',
    'ModelDockerSection',
    'ModelDockerSectionBaseImageRegistry',
    'ModelDockerSectionResponse',
    'ModelDockerSectionResponseBaseImageRegistry',
    'ModelEnvironmentDefinition',
    'ModelEnvironmentDefinitionDocker',
    'ModelEnvironmentDefinitionPython',
    'ModelEnvironmentDefinitionR',
    'ModelEnvironmentDefinitionResponse',
    'ModelEnvironmentDefinitionResponseDocker',
    'ModelEnvironmentDefinitionResponsePython',
    'ModelEnvironmentDefinitionResponseR',
    'ModelEnvironmentDefinitionResponseSpark',
    'ModelEnvironmentDefinitionSpark',
    'ModelPythonSection',
    'ModelSparkSection',
    'NodeStateCounts',
    'NotebookAccessTokenResult',
    'NotebookPreparationError',
    'NotebookResourceInfo',
    'Operation',
    'OperationDisplay',
    'Password',
    'PersonalComputeInstanceSettings',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'QuotaBaseProperties',
    'QuotaUpdateParameters',
    'RCranPackage',
    'RegistryListCredentialsResult',
    'Resource',
    'ResourceId',
    'ResourceName',
    'ResourceQuota',
    'ResourceSkuLocationInfo',
    'ResourceSkuZoneDetails',
    'Restriction',
    'RGitHubPackage',
    'RGitHubPackageResponse',
    'RSection',
    'RSectionResponse',
    'ScaleSettings',
    'ScriptReference',
    'ScriptsToExecute',
    'ServiceManagedResourcesSettings',
    'ServicePrincipalCredentials',
    'ServiceResource',
    'ServiceResponseBase',
    'ServiceResponseBaseError',
    'SetupScripts',
    'SharedPrivateLinkResource',
    'Sku',
    'SKUCapability',
    'SparkMavenPackage',
    'SslConfiguration',
    'SystemData',
    'SystemService',
    'UpdateWorkspaceQuotas',
    'UpdateWorkspaceQuotasResult',
    'Usage',
    'UsageName',
    'UserAccountCredentials',
    'UserAssignedIdentity',
    'VirtualMachine',
    'VirtualMachineImage',
    'VirtualMachineProperties',
    'VirtualMachineSecrets',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineSshCredentials',
    'VnetConfiguration',
    'Workspace',
    'WorkspaceConnection',
    'WorkspaceConnectionDto',
    'WorkspaceSku',
    'WorkspaceUpdateParameters',
    'OperationPaged',
    'WorkspacePaged',
    'AmlUserFeaturePaged',
    'UsagePaged',
    'ResourceQuotaPaged',
    'ComputeResourcePaged',
    'AmlComputeNodeInformationPaged',
    'WorkspaceSkuPaged',
    'ServiceResourcePaged',
    'WorkspaceConnectionPaged',
    'ProvisioningState',
    'EncryptionStatus',
    'PrivateEndpointServiceConnectionStatus',
    'PrivateEndpointConnectionProvisioningState',
    'ResourceIdentityType',
    'UsageUnit',
    'VMPriceOSType',
    'VMTier',
    'QuotaUnit',
    'Status',
    'IdentityType',
    'ClusterPurpose',
    'OsType',
    'VmPriority',
    'RemoteLoginPortPublicAccess',
    'AllocationState',
    'ApplicationSharingPolicy',
    'SshPublicAccess',
    'ComputeInstanceState',
    'ComputeInstanceAuthorizationType',
    'OperationName',
    'OperationStatus',
    'NodeState',
    'ComputeType',
    'ReasonCode',
    'WebServiceState',
    'DeploymentType',
    'VariantType',
    'ValueFormat',
    'UnderlyingResourceAction',
    'OrderString',
]
