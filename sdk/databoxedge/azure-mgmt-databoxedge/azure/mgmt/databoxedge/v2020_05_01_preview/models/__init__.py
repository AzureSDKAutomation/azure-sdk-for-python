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
    from ._models_py3 import Address
    from ._models_py3 import Alert
    from ._models_py3 import AlertErrorDetails
    from ._models_py3 import ARMBaseModel
    from ._models_py3 import AsymmetricEncryptedSecret
    from ._models_py3 import Authentication
    from ._models_py3 import AzureContainerInfo
    from ._models_py3 import BandwidthSchedule
    from ._models_py3 import ClientAccessRight
    from ._models_py3 import ContactDetails
    from ._models_py3 import Container
    from ._models_py3 import DataBoxEdgeDevice
    from ._models_py3 import DataBoxEdgeDeviceExtendedInfo
    from ._models_py3 import DataBoxEdgeDevicePatch
    from ._models_py3 import DataBoxEdgeSku
    from ._models_py3 import FileEventTrigger
    from ._models_py3 import FileSourceInfo
    from ._models_py3 import ImageRepositoryCredential
    from ._models_py3 import IoTDeviceInfo
    from ._models_py3 import IoTEdgeAgentInfo
    from ._models_py3 import IoTRole
    from ._models_py3 import Ipv4Config
    from ._models_py3 import Ipv6Config
    from ._models_py3 import Job
    from ._models_py3 import JobErrorDetails
    from ._models_py3 import JobErrorItem
    from ._models_py3 import MetricDimensionV1
    from ._models_py3 import MetricSpecificationV1
    from ._models_py3 import MountPointMap
    from ._models_py3 import NetworkAdapter
    from ._models_py3 import NetworkAdapterPosition
    from ._models_py3 import NetworkSettings
    from ._models_py3 import Node
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Order
    from ._models_py3 import OrderStatus
    from ._models_py3 import PeriodicTimerEventTrigger
    from ._models_py3 import PeriodicTimerSourceInfo
    from ._models_py3 import RefreshDetails
    from ._models_py3 import ResourceTypeSku
    from ._models_py3 import Role
    from ._models_py3 import RoleSinkInfo
    from ._models_py3 import SecuritySettings
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Share
    from ._models_py3 import ShareAccessRight
    from ._models_py3 import Sku
    from ._models_py3 import SKUCapability
    from ._models_py3 import SkuCost
    from ._models_py3 import SkuInformation
    from ._models_py3 import SkuLocationInfo
    from ._models_py3 import SkuRestriction
    from ._models_py3 import SkuRestrictionInfo
    from ._models_py3 import StorageAccount
    from ._models_py3 import StorageAccountCredential
    from ._models_py3 import SymmetricKey
    from ._models_py3 import TrackingInfo
    from ._models_py3 import Trigger
    from ._models_py3 import UpdateDownloadProgress
    from ._models_py3 import UpdateInstallProgress
    from ._models_py3 import UpdateSummary
    from ._models_py3 import UploadCertificateRequest
    from ._models_py3 import UploadCertificateResponse
    from ._models_py3 import User
    from ._models_py3 import UserAccessRight
except (SyntaxError, ImportError):
    from ._models import Address
    from ._models import Alert
    from ._models import AlertErrorDetails
    from ._models import ARMBaseModel
    from ._models import AsymmetricEncryptedSecret
    from ._models import Authentication
    from ._models import AzureContainerInfo
    from ._models import BandwidthSchedule
    from ._models import ClientAccessRight
    from ._models import ContactDetails
    from ._models import Container
    from ._models import DataBoxEdgeDevice
    from ._models import DataBoxEdgeDeviceExtendedInfo
    from ._models import DataBoxEdgeDevicePatch
    from ._models import DataBoxEdgeSku
    from ._models import FileEventTrigger
    from ._models import FileSourceInfo
    from ._models import ImageRepositoryCredential
    from ._models import IoTDeviceInfo
    from ._models import IoTEdgeAgentInfo
    from ._models import IoTRole
    from ._models import Ipv4Config
    from ._models import Ipv6Config
    from ._models import Job
    from ._models import JobErrorDetails
    from ._models import JobErrorItem
    from ._models import MetricDimensionV1
    from ._models import MetricSpecificationV1
    from ._models import MountPointMap
    from ._models import NetworkAdapter
    from ._models import NetworkAdapterPosition
    from ._models import NetworkSettings
    from ._models import Node
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Order
    from ._models import OrderStatus
    from ._models import PeriodicTimerEventTrigger
    from ._models import PeriodicTimerSourceInfo
    from ._models import RefreshDetails
    from ._models import ResourceTypeSku
    from ._models import Role
    from ._models import RoleSinkInfo
    from ._models import SecuritySettings
    from ._models import ServiceSpecification
    from ._models import Share
    from ._models import ShareAccessRight
    from ._models import Sku
    from ._models import SKUCapability
    from ._models import SkuCost
    from ._models import SkuInformation
    from ._models import SkuLocationInfo
    from ._models import SkuRestriction
    from ._models import SkuRestrictionInfo
    from ._models import StorageAccount
    from ._models import StorageAccountCredential
    from ._models import SymmetricKey
    from ._models import TrackingInfo
    from ._models import Trigger
    from ._models import UpdateDownloadProgress
    from ._models import UpdateInstallProgress
    from ._models import UpdateSummary
    from ._models import UploadCertificateRequest
    from ._models import UploadCertificateResponse
    from ._models import User
    from ._models import UserAccessRight
from ._paged_models import AlertPaged
from ._paged_models import BandwidthSchedulePaged
from ._paged_models import ContainerPaged
from ._paged_models import DataBoxEdgeDevicePaged
from ._paged_models import DataBoxEdgeSkuPaged
from ._paged_models import NodePaged
from ._paged_models import OperationPaged
from ._paged_models import OrderPaged
from ._paged_models import ResourceTypeSkuPaged
from ._paged_models import RolePaged
from ._paged_models import SharePaged
from ._paged_models import StorageAccountCredentialPaged
from ._paged_models import StorageAccountPaged
from ._paged_models import TriggerPaged
from ._paged_models import UserPaged
from ._data_box_edge_management_client_enums import (
    AlertSeverity,
    EncryptionAlgorithm,
    AzureContainerDataFormat,
    DayOfWeek,
    ClientPermissionType,
    ContainerStatus,
    SkuName,
    SkuTier,
    DataBoxEdgeDeviceStatus,
    DeviceType,
    RoleTypes,
    SkuRestrictionReasonCode,
    SkuSignupOption,
    SkuVersion,
    SkuAvailability,
    PlatformType,
    MountType,
    HostPlatformType,
    RoleStatus,
    JobStatus,
    JobType,
    UpdateOperationStage,
    DownloadPhase,
    MetricUnit,
    MetricAggregationType,
    MetricCategory,
    TimeGrain,
    NetworkGroup,
    NetworkAdapterStatus,
    NetworkAdapterRDMAStatus,
    NetworkAdapterDHCPStatus,
    NodeStatus,
    OrderState,
    AuthenticationType,
    ShareStatus,
    MonitoringStatus,
    ShareAccessProtocol,
    ShareAccessType,
    DataPolicy,
    StorageAccountStatus,
    SSLStatus,
    AccountType,
    InstallRebootBehavior,
    UpdateOperation,
    UserType,
)

__all__ = [
    'Address',
    'Alert',
    'AlertErrorDetails',
    'ARMBaseModel',
    'AsymmetricEncryptedSecret',
    'Authentication',
    'AzureContainerInfo',
    'BandwidthSchedule',
    'ClientAccessRight',
    'ContactDetails',
    'Container',
    'DataBoxEdgeDevice',
    'DataBoxEdgeDeviceExtendedInfo',
    'DataBoxEdgeDevicePatch',
    'DataBoxEdgeSku',
    'FileEventTrigger',
    'FileSourceInfo',
    'ImageRepositoryCredential',
    'IoTDeviceInfo',
    'IoTEdgeAgentInfo',
    'IoTRole',
    'Ipv4Config',
    'Ipv6Config',
    'Job',
    'JobErrorDetails',
    'JobErrorItem',
    'MetricDimensionV1',
    'MetricSpecificationV1',
    'MountPointMap',
    'NetworkAdapter',
    'NetworkAdapterPosition',
    'NetworkSettings',
    'Node',
    'Operation',
    'OperationDisplay',
    'Order',
    'OrderStatus',
    'PeriodicTimerEventTrigger',
    'PeriodicTimerSourceInfo',
    'RefreshDetails',
    'ResourceTypeSku',
    'Role',
    'RoleSinkInfo',
    'SecuritySettings',
    'ServiceSpecification',
    'Share',
    'ShareAccessRight',
    'Sku',
    'SKUCapability',
    'SkuCost',
    'SkuInformation',
    'SkuLocationInfo',
    'SkuRestriction',
    'SkuRestrictionInfo',
    'StorageAccount',
    'StorageAccountCredential',
    'SymmetricKey',
    'TrackingInfo',
    'Trigger',
    'UpdateDownloadProgress',
    'UpdateInstallProgress',
    'UpdateSummary',
    'UploadCertificateRequest',
    'UploadCertificateResponse',
    'User',
    'UserAccessRight',
    'OperationPaged',
    'DataBoxEdgeSkuPaged',
    'DataBoxEdgeDevicePaged',
    'AlertPaged',
    'BandwidthSchedulePaged',
    'NodePaged',
    'OrderPaged',
    'RolePaged',
    'SharePaged',
    'StorageAccountCredentialPaged',
    'StorageAccountPaged',
    'ContainerPaged',
    'TriggerPaged',
    'UserPaged',
    'ResourceTypeSkuPaged',
    'AlertSeverity',
    'EncryptionAlgorithm',
    'AzureContainerDataFormat',
    'DayOfWeek',
    'ClientPermissionType',
    'ContainerStatus',
    'SkuName',
    'SkuTier',
    'DataBoxEdgeDeviceStatus',
    'DeviceType',
    'RoleTypes',
    'SkuRestrictionReasonCode',
    'SkuSignupOption',
    'SkuVersion',
    'SkuAvailability',
    'PlatformType',
    'MountType',
    'HostPlatformType',
    'RoleStatus',
    'JobStatus',
    'JobType',
    'UpdateOperationStage',
    'DownloadPhase',
    'MetricUnit',
    'MetricAggregationType',
    'MetricCategory',
    'TimeGrain',
    'NetworkGroup',
    'NetworkAdapterStatus',
    'NetworkAdapterRDMAStatus',
    'NetworkAdapterDHCPStatus',
    'NodeStatus',
    'OrderState',
    'AuthenticationType',
    'ShareStatus',
    'MonitoringStatus',
    'ShareAccessProtocol',
    'ShareAccessType',
    'DataPolicy',
    'StorageAccountStatus',
    'SSLStatus',
    'AccountType',
    'InstallRebootBehavior',
    'UpdateOperation',
    'UserType',
]
