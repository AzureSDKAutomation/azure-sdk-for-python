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
    from ._models_py3 import Addon
    from ._models_py3 import AddonSrmProperties
    from ._models_py3 import AddonUpdate
    from ._models_py3 import AdminCredentials
    from ._models_py3 import Circuit
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterUpdate
    from ._models_py3 import CommonClusterProperties
    from ._models_py3 import Endpoints
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExpressRouteAuthorization
    from ._models_py3 import GlobalReachConnection
    from ._models_py3 import HcxEnterpriseSite
    from ._models_py3 import IdentitySource
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagementCluster
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationProperties
    from ._models_py3 import PrivateCloud
    from ._models_py3 import PrivateCloudUpdate
    from ._models_py3 import ProxyResource
    from ._models_py3 import Quota
    from ._models_py3 import Resource
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
    from ._models_py3 import Trial
    from ._models_py3 import WorkloadNetworkDhcp
    from ._models_py3 import WorkloadNetworkDhcpEntity
    from ._models_py3 import WorkloadNetworkDhcpRelay
    from ._models_py3 import WorkloadNetworkDhcpServer
    from ._models_py3 import WorkloadNetworkDnsService
    from ._models_py3 import WorkloadNetworkDnsZone
    from ._models_py3 import WorkloadNetworkGateway
    from ._models_py3 import WorkloadNetworkPortMirroring
    from ._models_py3 import WorkloadNetworkSegment
    from ._models_py3 import WorkloadNetworkSegmentPortVif
    from ._models_py3 import WorkloadNetworkSegmentSubnet
    from ._models_py3 import WorkloadNetworkVirtualMachine
    from ._models_py3 import WorkloadNetworkVMGroup
except (SyntaxError, ImportError):
    from ._models import Addon
    from ._models import AddonSrmProperties
    from ._models import AddonUpdate
    from ._models import AdminCredentials
    from ._models import Circuit
    from ._models import Cluster
    from ._models import ClusterUpdate
    from ._models import CommonClusterProperties
    from ._models import Endpoints
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorResponse
    from ._models import ExpressRouteAuthorization
    from ._models import GlobalReachConnection
    from ._models import HcxEnterpriseSite
    from ._models import IdentitySource
    from ._models import LogSpecification
    from ._models import ManagementCluster
    from ._models import MetricDimension
    from ._models import MetricSpecification
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OperationProperties
    from ._models import PrivateCloud
    from ._models import PrivateCloudUpdate
    from ._models import ProxyResource
    from ._models import Quota
    from ._models import Resource
    from ._models import ServiceSpecification
    from ._models import Sku
    from ._models import TrackedResource
    from ._models import Trial
    from ._models import WorkloadNetworkDhcp
    from ._models import WorkloadNetworkDhcpEntity
    from ._models import WorkloadNetworkDhcpRelay
    from ._models import WorkloadNetworkDhcpServer
    from ._models import WorkloadNetworkDnsService
    from ._models import WorkloadNetworkDnsZone
    from ._models import WorkloadNetworkGateway
    from ._models import WorkloadNetworkPortMirroring
    from ._models import WorkloadNetworkSegment
    from ._models import WorkloadNetworkSegmentPortVif
    from ._models import WorkloadNetworkSegmentSubnet
    from ._models import WorkloadNetworkVirtualMachine
    from ._models import WorkloadNetworkVMGroup
from ._paged_models import AddonPaged
from ._paged_models import ClusterPaged
from ._paged_models import ExpressRouteAuthorizationPaged
from ._paged_models import GlobalReachConnectionPaged
from ._paged_models import HcxEnterpriseSitePaged
from ._paged_models import OperationPaged
from ._paged_models import PrivateCloudPaged
from ._paged_models import WorkloadNetworkDhcpPaged
from ._paged_models import WorkloadNetworkDnsServicePaged
from ._paged_models import WorkloadNetworkDnsZonePaged
from ._paged_models import WorkloadNetworkGatewayPaged
from ._paged_models import WorkloadNetworkPortMirroringPaged
from ._paged_models import WorkloadNetworkSegmentPaged
from ._paged_models import WorkloadNetworkVirtualMachinePaged
from ._paged_models import WorkloadNetworkVMGroupPaged
from ._avs_client_enums import (
    TrialStatus,
    QuotaEnabled,
    ExpressRouteAuthorizationProvisioningState,
    SslEnum,
    PrivateCloudProvisioningState,
    InternetEnum,
    ClusterProvisioningState,
    AddonType,
    AddonProvisioningState,
    HcxEnterpriseSiteStatus,
    GlobalReachConnectionProvisioningState,
    GlobalReachConnectionStatus,
    SegmentStatusEnum,
    WorkloadNetworkSegmentProvisioningState,
    WorkloadNetworkDhcpProvisioningState,
    PortMirroringDirectionEnum,
    PortMirroringStatusEnum,
    WorkloadNetworkPortMirroringProvisioningState,
    VMGroupStatusEnum,
    WorkloadNetworkVMGroupProvisioningState,
    VMTypeEnum,
    DnsServiceLogLevelEnum,
    DnsServiceStatusEnum,
    WorkloadNetworkDnsServiceProvisioningState,
    WorkloadNetworkDnsZoneProvisioningState,
)

__all__ = [
    'Addon',
    'AddonSrmProperties',
    'AddonUpdate',
    'AdminCredentials',
    'Circuit',
    'Cluster',
    'ClusterUpdate',
    'CommonClusterProperties',
    'Endpoints',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'ExpressRouteAuthorization',
    'GlobalReachConnection',
    'HcxEnterpriseSite',
    'IdentitySource',
    'LogSpecification',
    'ManagementCluster',
    'MetricDimension',
    'MetricSpecification',
    'Operation',
    'OperationDisplay',
    'OperationProperties',
    'PrivateCloud',
    'PrivateCloudUpdate',
    'ProxyResource',
    'Quota',
    'Resource',
    'ServiceSpecification',
    'Sku',
    'TrackedResource',
    'Trial',
    'WorkloadNetworkDhcp',
    'WorkloadNetworkDhcpEntity',
    'WorkloadNetworkDhcpRelay',
    'WorkloadNetworkDhcpServer',
    'WorkloadNetworkDnsService',
    'WorkloadNetworkDnsZone',
    'WorkloadNetworkGateway',
    'WorkloadNetworkPortMirroring',
    'WorkloadNetworkSegment',
    'WorkloadNetworkSegmentPortVif',
    'WorkloadNetworkSegmentSubnet',
    'WorkloadNetworkVirtualMachine',
    'WorkloadNetworkVMGroup',
    'OperationPaged',
    'PrivateCloudPaged',
    'ClusterPaged',
    'HcxEnterpriseSitePaged',
    'ExpressRouteAuthorizationPaged',
    'GlobalReachConnectionPaged',
    'WorkloadNetworkSegmentPaged',
    'WorkloadNetworkDhcpPaged',
    'WorkloadNetworkGatewayPaged',
    'WorkloadNetworkPortMirroringPaged',
    'WorkloadNetworkVMGroupPaged',
    'WorkloadNetworkVirtualMachinePaged',
    'WorkloadNetworkDnsServicePaged',
    'WorkloadNetworkDnsZonePaged',
    'AddonPaged',
    'TrialStatus',
    'QuotaEnabled',
    'ExpressRouteAuthorizationProvisioningState',
    'SslEnum',
    'PrivateCloudProvisioningState',
    'InternetEnum',
    'ClusterProvisioningState',
    'AddonType',
    'AddonProvisioningState',
    'HcxEnterpriseSiteStatus',
    'GlobalReachConnectionProvisioningState',
    'GlobalReachConnectionStatus',
    'SegmentStatusEnum',
    'WorkloadNetworkSegmentProvisioningState',
    'WorkloadNetworkDhcpProvisioningState',
    'PortMirroringDirectionEnum',
    'PortMirroringStatusEnum',
    'WorkloadNetworkPortMirroringProvisioningState',
    'VMGroupStatusEnum',
    'WorkloadNetworkVMGroupProvisioningState',
    'VMTypeEnum',
    'DnsServiceLogLevelEnum',
    'DnsServiceStatusEnum',
    'WorkloadNetworkDnsServiceProvisioningState',
    'WorkloadNetworkDnsZoneProvisioningState',
]
