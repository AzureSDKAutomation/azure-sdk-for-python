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
    from ._models_py3 import AccountKeySection
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
    from ._models_py3 import AssetPath
    from ._models_py3 import AssignedUser
    from ._models_py3 import AuthKeys
    from ._models_py3 import AutoScaler
    from ._models_py3 import AzureDataLakeSection
    from ._models_py3 import AzureDataLakeSectionCredentials
    from ._models_py3 import AzureMySqlSection
    from ._models_py3 import AzureMySqlSectionCredentials
    from ._models_py3 import AzurePostgreSqlSection
    from ._models_py3 import AzurePostgreSqlSectionCredentials
    from ._models_py3 import AzureSqlDatabaseSection
    from ._models_py3 import AzureSqlDatabaseSectionCredentials
    from ._models_py3 import AzureStorageSection
    from ._models_py3 import AzureStorageSectionCredentials
    from ._models_py3 import Body
    from ._models_py3 import CertificateSection
    from ._models_py3 import ClusterUpdateParameters
    from ._models_py3 import CodeConfiguration
    from ._models_py3 import CodeContainer
    from ._models_py3 import CodeContainerResource
    from ._models_py3 import CodeContainerResourceSystemData
    from ._models_py3 import CodeVersion
    from ._models_py3 import CodeVersionAssetPath
    from ._models_py3 import CodeVersionResource
    from ._models_py3 import CodeVersionResourceSystemData
    from ._models_py3 import CommandJob
    from ._models_py3 import CommandJobCodeConfiguration
    from ._models_py3 import Compute
    from ._models_py3 import ComputeBinding
    from ._models_py3 import ComputeInstance
    from ._models_py3 import ComputeInstanceApplication
    from ._models_py3 import ComputeInstanceConnectivityEndpoints
    from ._models_py3 import ComputeInstanceCreatedBy
    from ._models_py3 import ComputeInstanceLastOperation
    from ._models_py3 import ComputeInstanceProperties
    from ._models_py3 import ComputeInstanceSshSettings
    from ._models_py3 import ComputeJobBase
    from ._models_py3 import ComputeJobBaseComputeBinding
    from ._models_py3 import ComputeJobBaseOutput
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
    from ._models_py3 import DataBinding
    from ._models_py3 import Databricks
    from ._models_py3 import DatabricksComputeSecrets
    from ._models_py3 import DatabricksProperties
    from ._models_py3 import DataContainer
    from ._models_py3 import DataContainerResource
    from ._models_py3 import DataContainerResourceSystemData
    from ._models_py3 import DataFactory
    from ._models_py3 import DataLakeAnalytics
    from ._models_py3 import DataLakeAnalyticsProperties
    from ._models_py3 import DatasetReference
    from ._models_py3 import DatastoreContents
    from ._models_py3 import DatastoreContentsAzureDataLake
    from ._models_py3 import DatastoreContentsAzureMySql
    from ._models_py3 import DatastoreContentsAzurePostgreSql
    from ._models_py3 import DatastoreContentsAzureSqlDatabase
    from ._models_py3 import DatastoreContentsAzureStorage
    from ._models_py3 import DatastoreContentsGlusterFs
    from ._models_py3 import DatastoreCredentials
    from ._models_py3 import DatastoreCredentialsAccountKey
    from ._models_py3 import DatastoreCredentialsCertificate
    from ._models_py3 import DatastoreCredentialsSas
    from ._models_py3 import DatastoreCredentialsServicePrincipal
    from ._models_py3 import DatastoreCredentialsSqlAdmin
    from ._models_py3 import DatastoreProperties
    from ._models_py3 import DatastorePropertiesContents
    from ._models_py3 import DatastorePropertiesLinkedInfo
    from ._models_py3 import DatastorePropertiesResource
    from ._models_py3 import DatastorePropertiesResourceSystemData
    from ._models_py3 import DataVersion
    from ._models_py3 import DataVersionAssetPath
    from ._models_py3 import DataVersionResource
    from ._models_py3 import DataVersionResourceSystemData
    from ._models_py3 import DistributionConfiguration
    from ._models_py3 import DockerSpecification
    from ._models_py3 import EarlyTerminationPolicyConfiguration
    from ._models_py3 import EncryptionProperties
    from ._models_py3 import EncryptionProperty
    from ._models_py3 import EnvironmentContainer
    from ._models_py3 import EnvironmentContainerResource
    from ._models_py3 import EnvironmentContainerResourceSystemData
    from ._models_py3 import EnvironmentImageRequest
    from ._models_py3 import EnvironmentImageRequestEnvironment
    from ._models_py3 import EnvironmentImageRequestEnvironmentReference
    from ._models_py3 import EnvironmentImageResponse
    from ._models_py3 import EnvironmentImageResponseEnvironment
    from ._models_py3 import EnvironmentImageResponseEnvironmentReference
    from ._models_py3 import EnvironmentReference
    from ._models_py3 import EnvironmentSpecificationVersion
    from ._models_py3 import EnvironmentSpecificationVersionAssetPath
    from ._models_py3 import EnvironmentSpecificationVersionResource
    from ._models_py3 import EnvironmentSpecificationVersionResourceSystemData
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EstimatedVMPrice
    from ._models_py3 import EstimatedVMPrices
    from ._models_py3 import EvaluationConfiguration
    from ._models_py3 import GlusterFsSection
    from ._models_py3 import HDInsight
    from ._models_py3 import HDInsightProperties
    from ._models_py3 import Identity
    from ._models_py3 import IdentityForCmk
    from ._models_py3 import ImageAsset
    from ._models_py3 import InnerErrorResponse
    from ._models_py3 import InnerErrorResponseInnerError
    from ._models_py3 import JobBase
    from ._models_py3 import JobBaseInteractionEndpoints
    from ._models_py3 import JobBaseResource
    from ._models_py3 import JobBaseResourceSystemData
    from ._models_py3 import JobOutput
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import LabelClass
    from ._models_py3 import LinkedInfo
    from ._models_py3 import ListNotebookKeysResult
    from ._models_py3 import ListStorageAccountKeysResult
    from ._models_py3 import ListWorkspaceKeysResult
    from ._models_py3 import LivenessProbeRequirements
    from ._models_py3 import MachineLearningServiceError, MachineLearningServiceErrorException
    from ._models_py3 import Model
    from ._models_py3 import ModelContainer
    from ._models_py3 import ModelContainerResource
    from ._models_py3 import ModelContainerResourceSystemData
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
    from ._models_py3 import ModelVersion
    from ._models_py3 import ModelVersionAssetPath
    from ._models_py3 import ModelVersionResource
    from ._models_py3 import ModelVersionResourceSystemData
    from ._models_py3 import NodeStateCounts
    from ._models_py3 import NotebookAccessTokenResult
    from ._models_py3 import NotebookPreparationError
    from ._models_py3 import NotebookResourceInfo
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ParameterSamplingConfiguration
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
    from ._models_py3 import RootError
    from ._models_py3 import RootErrorInnerError
    from ._models_py3 import RSection
    from ._models_py3 import RSectionResponse
    from ._models_py3 import SasSection
    from ._models_py3 import ScaleSettings
    from ._models_py3 import ScriptReference
    from ._models_py3 import ScriptsToExecute
    from ._models_py3 import ServiceManagedResourcesSettings
    from ._models_py3 import ServicePrincipalCredentials
    from ._models_py3 import ServicePrincipalSection
    from ._models_py3 import ServiceResource
    from ._models_py3 import ServiceResponseBase
    from ._models_py3 import ServiceResponseBaseError
    from ._models_py3 import SetupScripts
    from ._models_py3 import SharedPrivateLinkResource
    from ._models_py3 import Sku
    from ._models_py3 import SKUCapability
    from ._models_py3 import SparkMavenPackage
    from ._models_py3 import SqlAdminSection
    from ._models_py3 import SslConfiguration
    from ._models_py3 import SweepJob
    from ._models_py3 import SweepJobEvaluationConfiguration
    from ._models_py3 import SweepJobParameterSamplingConfiguration
    from ._models_py3 import SweepJobTerminationConfiguration
    from ._models_py3 import SweepJobTrialComponent
    from ._models_py3 import SystemData
    from ._models_py3 import SystemDataModel
    from ._models_py3 import SystemService
    from ._models_py3 import TerminationConfiguration
    from ._models_py3 import TrialComponent
    from ._models_py3 import TrialComponentCodeConfiguration
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
    from ._models import AccountKeySection
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
    from ._models import AssetPath
    from ._models import AssignedUser
    from ._models import AuthKeys
    from ._models import AutoScaler
    from ._models import AzureDataLakeSection
    from ._models import AzureDataLakeSectionCredentials
    from ._models import AzureMySqlSection
    from ._models import AzureMySqlSectionCredentials
    from ._models import AzurePostgreSqlSection
    from ._models import AzurePostgreSqlSectionCredentials
    from ._models import AzureSqlDatabaseSection
    from ._models import AzureSqlDatabaseSectionCredentials
    from ._models import AzureStorageSection
    from ._models import AzureStorageSectionCredentials
    from ._models import Body
    from ._models import CertificateSection
    from ._models import ClusterUpdateParameters
    from ._models import CodeConfiguration
    from ._models import CodeContainer
    from ._models import CodeContainerResource
    from ._models import CodeContainerResourceSystemData
    from ._models import CodeVersion
    from ._models import CodeVersionAssetPath
    from ._models import CodeVersionResource
    from ._models import CodeVersionResourceSystemData
    from ._models import CommandJob
    from ._models import CommandJobCodeConfiguration
    from ._models import Compute
    from ._models import ComputeBinding
    from ._models import ComputeInstance
    from ._models import ComputeInstanceApplication
    from ._models import ComputeInstanceConnectivityEndpoints
    from ._models import ComputeInstanceCreatedBy
    from ._models import ComputeInstanceLastOperation
    from ._models import ComputeInstanceProperties
    from ._models import ComputeInstanceSshSettings
    from ._models import ComputeJobBase
    from ._models import ComputeJobBaseComputeBinding
    from ._models import ComputeJobBaseOutput
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
    from ._models import DataBinding
    from ._models import Databricks
    from ._models import DatabricksComputeSecrets
    from ._models import DatabricksProperties
    from ._models import DataContainer
    from ._models import DataContainerResource
    from ._models import DataContainerResourceSystemData
    from ._models import DataFactory
    from ._models import DataLakeAnalytics
    from ._models import DataLakeAnalyticsProperties
    from ._models import DatasetReference
    from ._models import DatastoreContents
    from ._models import DatastoreContentsAzureDataLake
    from ._models import DatastoreContentsAzureMySql
    from ._models import DatastoreContentsAzurePostgreSql
    from ._models import DatastoreContentsAzureSqlDatabase
    from ._models import DatastoreContentsAzureStorage
    from ._models import DatastoreContentsGlusterFs
    from ._models import DatastoreCredentials
    from ._models import DatastoreCredentialsAccountKey
    from ._models import DatastoreCredentialsCertificate
    from ._models import DatastoreCredentialsSas
    from ._models import DatastoreCredentialsServicePrincipal
    from ._models import DatastoreCredentialsSqlAdmin
    from ._models import DatastoreProperties
    from ._models import DatastorePropertiesContents
    from ._models import DatastorePropertiesLinkedInfo
    from ._models import DatastorePropertiesResource
    from ._models import DatastorePropertiesResourceSystemData
    from ._models import DataVersion
    from ._models import DataVersionAssetPath
    from ._models import DataVersionResource
    from ._models import DataVersionResourceSystemData
    from ._models import DistributionConfiguration
    from ._models import DockerSpecification
    from ._models import EarlyTerminationPolicyConfiguration
    from ._models import EncryptionProperties
    from ._models import EncryptionProperty
    from ._models import EnvironmentContainer
    from ._models import EnvironmentContainerResource
    from ._models import EnvironmentContainerResourceSystemData
    from ._models import EnvironmentImageRequest
    from ._models import EnvironmentImageRequestEnvironment
    from ._models import EnvironmentImageRequestEnvironmentReference
    from ._models import EnvironmentImageResponse
    from ._models import EnvironmentImageResponseEnvironment
    from ._models import EnvironmentImageResponseEnvironmentReference
    from ._models import EnvironmentReference
    from ._models import EnvironmentSpecificationVersion
    from ._models import EnvironmentSpecificationVersionAssetPath
    from ._models import EnvironmentSpecificationVersionResource
    from ._models import EnvironmentSpecificationVersionResourceSystemData
    from ._models import ErrorDetail
    from ._models import ErrorResponse
    from ._models import EstimatedVMPrice
    from ._models import EstimatedVMPrices
    from ._models import EvaluationConfiguration
    from ._models import GlusterFsSection
    from ._models import HDInsight
    from ._models import HDInsightProperties
    from ._models import Identity
    from ._models import IdentityForCmk
    from ._models import ImageAsset
    from ._models import InnerErrorResponse
    from ._models import InnerErrorResponseInnerError
    from ._models import JobBase
    from ._models import JobBaseInteractionEndpoints
    from ._models import JobBaseResource
    from ._models import JobBaseResourceSystemData
    from ._models import JobOutput
    from ._models import KeyVaultProperties
    from ._models import LabelClass
    from ._models import LinkedInfo
    from ._models import ListNotebookKeysResult
    from ._models import ListStorageAccountKeysResult
    from ._models import ListWorkspaceKeysResult
    from ._models import LivenessProbeRequirements
    from ._models import MachineLearningServiceError, MachineLearningServiceErrorException
    from ._models import Model
    from ._models import ModelContainer
    from ._models import ModelContainerResource
    from ._models import ModelContainerResourceSystemData
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
    from ._models import ModelVersion
    from ._models import ModelVersionAssetPath
    from ._models import ModelVersionResource
    from ._models import ModelVersionResourceSystemData
    from ._models import NodeStateCounts
    from ._models import NotebookAccessTokenResult
    from ._models import NotebookPreparationError
    from ._models import NotebookResourceInfo
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import ParameterSamplingConfiguration
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
    from ._models import RootError
    from ._models import RootErrorInnerError
    from ._models import RSection
    from ._models import RSectionResponse
    from ._models import SasSection
    from ._models import ScaleSettings
    from ._models import ScriptReference
    from ._models import ScriptsToExecute
    from ._models import ServiceManagedResourcesSettings
    from ._models import ServicePrincipalCredentials
    from ._models import ServicePrincipalSection
    from ._models import ServiceResource
    from ._models import ServiceResponseBase
    from ._models import ServiceResponseBaseError
    from ._models import SetupScripts
    from ._models import SharedPrivateLinkResource
    from ._models import Sku
    from ._models import SKUCapability
    from ._models import SparkMavenPackage
    from ._models import SqlAdminSection
    from ._models import SslConfiguration
    from ._models import SweepJob
    from ._models import SweepJobEvaluationConfiguration
    from ._models import SweepJobParameterSamplingConfiguration
    from ._models import SweepJobTerminationConfiguration
    from ._models import SweepJobTrialComponent
    from ._models import SystemData
    from ._models import SystemDataModel
    from ._models import SystemService
    from ._models import TerminationConfiguration
    from ._models import TrialComponent
    from ._models import TrialComponentCodeConfiguration
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
from ._paged_models import CodeContainerResourcePaged
from ._paged_models import CodeVersionResourcePaged
from ._paged_models import ComputeResourcePaged
from ._paged_models import DataContainerResourcePaged
from ._paged_models import DatastorePropertiesResourcePaged
from ._paged_models import DataVersionResourcePaged
from ._paged_models import EnvironmentContainerResourcePaged
from ._paged_models import EnvironmentSpecificationVersionResourcePaged
from ._paged_models import JobBaseResourcePaged
from ._paged_models import ModelContainerResourcePaged
from ._paged_models import ModelVersionResourcePaged
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
    CredentialsType,
    ContentsType,
    OriginType,
    DatasetType,
    EnvironmentSpecificationType,
    DataBindingMode,
    JobProvisioningState,
    JobStatus,
    ParameterSamplingType,
    PrimaryMetricGoal,
    CreatedByType,
    UnderlyingResourceAction,
    OrderString,
)

__all__ = [
    'AccountKeySection',
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
    'AssetPath',
    'AssignedUser',
    'AuthKeys',
    'AutoScaler',
    'AzureDataLakeSection',
    'AzureDataLakeSectionCredentials',
    'AzureMySqlSection',
    'AzureMySqlSectionCredentials',
    'AzurePostgreSqlSection',
    'AzurePostgreSqlSectionCredentials',
    'AzureSqlDatabaseSection',
    'AzureSqlDatabaseSectionCredentials',
    'AzureStorageSection',
    'AzureStorageSectionCredentials',
    'Body',
    'CertificateSection',
    'ClusterUpdateParameters',
    'CodeConfiguration',
    'CodeContainer',
    'CodeContainerResource',
    'CodeContainerResourceSystemData',
    'CodeVersion',
    'CodeVersionAssetPath',
    'CodeVersionResource',
    'CodeVersionResourceSystemData',
    'CommandJob',
    'CommandJobCodeConfiguration',
    'Compute',
    'ComputeBinding',
    'ComputeInstance',
    'ComputeInstanceApplication',
    'ComputeInstanceConnectivityEndpoints',
    'ComputeInstanceCreatedBy',
    'ComputeInstanceLastOperation',
    'ComputeInstanceProperties',
    'ComputeInstanceSshSettings',
    'ComputeJobBase',
    'ComputeJobBaseComputeBinding',
    'ComputeJobBaseOutput',
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
    'DataBinding',
    'Databricks',
    'DatabricksComputeSecrets',
    'DatabricksProperties',
    'DataContainer',
    'DataContainerResource',
    'DataContainerResourceSystemData',
    'DataFactory',
    'DataLakeAnalytics',
    'DataLakeAnalyticsProperties',
    'DatasetReference',
    'DatastoreContents',
    'DatastoreContentsAzureDataLake',
    'DatastoreContentsAzureMySql',
    'DatastoreContentsAzurePostgreSql',
    'DatastoreContentsAzureSqlDatabase',
    'DatastoreContentsAzureStorage',
    'DatastoreContentsGlusterFs',
    'DatastoreCredentials',
    'DatastoreCredentialsAccountKey',
    'DatastoreCredentialsCertificate',
    'DatastoreCredentialsSas',
    'DatastoreCredentialsServicePrincipal',
    'DatastoreCredentialsSqlAdmin',
    'DatastoreProperties',
    'DatastorePropertiesContents',
    'DatastorePropertiesLinkedInfo',
    'DatastorePropertiesResource',
    'DatastorePropertiesResourceSystemData',
    'DataVersion',
    'DataVersionAssetPath',
    'DataVersionResource',
    'DataVersionResourceSystemData',
    'DistributionConfiguration',
    'DockerSpecification',
    'EarlyTerminationPolicyConfiguration',
    'EncryptionProperties',
    'EncryptionProperty',
    'EnvironmentContainer',
    'EnvironmentContainerResource',
    'EnvironmentContainerResourceSystemData',
    'EnvironmentImageRequest',
    'EnvironmentImageRequestEnvironment',
    'EnvironmentImageRequestEnvironmentReference',
    'EnvironmentImageResponse',
    'EnvironmentImageResponseEnvironment',
    'EnvironmentImageResponseEnvironmentReference',
    'EnvironmentReference',
    'EnvironmentSpecificationVersion',
    'EnvironmentSpecificationVersionAssetPath',
    'EnvironmentSpecificationVersionResource',
    'EnvironmentSpecificationVersionResourceSystemData',
    'ErrorDetail',
    'ErrorResponse',
    'EstimatedVMPrice',
    'EstimatedVMPrices',
    'EvaluationConfiguration',
    'GlusterFsSection',
    'HDInsight',
    'HDInsightProperties',
    'Identity',
    'IdentityForCmk',
    'ImageAsset',
    'InnerErrorResponse',
    'InnerErrorResponseInnerError',
    'JobBase',
    'JobBaseInteractionEndpoints',
    'JobBaseResource',
    'JobBaseResourceSystemData',
    'JobOutput',
    'KeyVaultProperties',
    'LabelClass',
    'LinkedInfo',
    'ListNotebookKeysResult',
    'ListStorageAccountKeysResult',
    'ListWorkspaceKeysResult',
    'LivenessProbeRequirements',
    'MachineLearningServiceError', 'MachineLearningServiceErrorException',
    'Model',
    'ModelContainer',
    'ModelContainerResource',
    'ModelContainerResourceSystemData',
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
    'ModelVersion',
    'ModelVersionAssetPath',
    'ModelVersionResource',
    'ModelVersionResourceSystemData',
    'NodeStateCounts',
    'NotebookAccessTokenResult',
    'NotebookPreparationError',
    'NotebookResourceInfo',
    'Operation',
    'OperationDisplay',
    'ParameterSamplingConfiguration',
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
    'RootError',
    'RootErrorInnerError',
    'RSection',
    'RSectionResponse',
    'SasSection',
    'ScaleSettings',
    'ScriptReference',
    'ScriptsToExecute',
    'ServiceManagedResourcesSettings',
    'ServicePrincipalCredentials',
    'ServicePrincipalSection',
    'ServiceResource',
    'ServiceResponseBase',
    'ServiceResponseBaseError',
    'SetupScripts',
    'SharedPrivateLinkResource',
    'Sku',
    'SKUCapability',
    'SparkMavenPackage',
    'SqlAdminSection',
    'SslConfiguration',
    'SweepJob',
    'SweepJobEvaluationConfiguration',
    'SweepJobParameterSamplingConfiguration',
    'SweepJobTerminationConfiguration',
    'SweepJobTrialComponent',
    'SystemData',
    'SystemDataModel',
    'SystemService',
    'TerminationConfiguration',
    'TrialComponent',
    'TrialComponentCodeConfiguration',
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
    'CodeContainerResourcePaged',
    'CodeVersionResourcePaged',
    'DataContainerResourcePaged',
    'DatastorePropertiesResourcePaged',
    'DataVersionResourcePaged',
    'EnvironmentContainerResourcePaged',
    'EnvironmentSpecificationVersionResourcePaged',
    'JobBaseResourcePaged',
    'ModelContainerResourcePaged',
    'ModelVersionResourcePaged',
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
    'CredentialsType',
    'ContentsType',
    'OriginType',
    'DatasetType',
    'EnvironmentSpecificationType',
    'DataBindingMode',
    'JobProvisioningState',
    'JobStatus',
    'ParameterSamplingType',
    'PrimaryMetricGoal',
    'CreatedByType',
    'UnderlyingResourceAction',
    'OrderString',
]
