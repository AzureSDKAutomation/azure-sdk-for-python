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
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import CheckDomainAvailabilityParameter
    from ._models_py3 import CheckDomainAvailabilityResult
    from ._models_py3 import CheckSkuAvailabilityParameter
    from ._models_py3 import CheckSkuAvailabilityResult
    from ._models_py3 import CheckSkuAvailabilityResultList
    from ._models_py3 import CognitiveServicesAccount
    from ._models_py3 import CognitiveServicesAccountApiProperties
    from ._models_py3 import CognitiveServicesAccountEnumerateSkusResult
    from ._models_py3 import CognitiveServicesAccountKeys
    from ._models_py3 import CognitiveServicesAccountProperties
    from ._models_py3 import CognitiveServicesResourceAndSku
    from ._models_py3 import Encryption
    from ._models_py3 import Error, ErrorException
    from ._models_py3 import ErrorBody
    from ._models_py3 import Identity
    from ._models_py3 import IpRule
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import MetricName
    from ._models_py3 import NetworkRuleSet
    from ._models_py3 import OperationDisplayInfo
    from ._models_py3 import OperationEntity
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionProperties
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyResource
    from ._models_py3 import RegenerateKeyParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuRestrictionInfo
    from ._models_py3 import ResourceSkuRestrictions
    from ._models_py3 import Sku
    from ._models_py3 import TrackedResource
    from ._models_py3 import Usage
    from ._models_py3 import UsagesResult
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import UserOwnedStorage
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import AzureEntityResource
    from ._models import CheckDomainAvailabilityParameter
    from ._models import CheckDomainAvailabilityResult
    from ._models import CheckSkuAvailabilityParameter
    from ._models import CheckSkuAvailabilityResult
    from ._models import CheckSkuAvailabilityResultList
    from ._models import CognitiveServicesAccount
    from ._models import CognitiveServicesAccountApiProperties
    from ._models import CognitiveServicesAccountEnumerateSkusResult
    from ._models import CognitiveServicesAccountKeys
    from ._models import CognitiveServicesAccountProperties
    from ._models import CognitiveServicesResourceAndSku
    from ._models import Encryption
    from ._models import Error, ErrorException
    from ._models import ErrorBody
    from ._models import Identity
    from ._models import IpRule
    from ._models import KeyVaultProperties
    from ._models import MetricName
    from ._models import NetworkRuleSet
    from ._models import OperationDisplayInfo
    from ._models import OperationEntity
    from ._models import PrivateEndpoint
    from ._models import PrivateEndpointConnection
    from ._models import PrivateEndpointConnectionProperties
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkResourceListResult
    from ._models import PrivateLinkResourceProperties
    from ._models import PrivateLinkServiceConnectionState
    from ._models import ProxyResource
    from ._models import RegenerateKeyParameters
    from ._models import Resource
    from ._models import ResourceSku
    from ._models import ResourceSkuRestrictionInfo
    from ._models import ResourceSkuRestrictions
    from ._models import Sku
    from ._models import TrackedResource
    from ._models import Usage
    from ._models import UsagesResult
    from ._models import UserAssignedIdentity
    from ._models import UserOwnedStorage
    from ._models import VirtualNetworkRule
from ._paged_models import CognitiveServicesAccountPaged
from ._paged_models import OperationEntityPaged
from ._paged_models import ResourceSkuPaged
from ._cognitive_services_management_client_enums import (
    SkuTier,
    ProvisioningState,
    NetworkRuleAction,
    KeySource,
    PrivateEndpointServiceConnectionStatus,
    PublicNetworkAccess,
    IdentityType,
    KeyName,
    UnitType,
    QuotaUsageStatus,
    ResourceSkuRestrictionsType,
    ResourceSkuRestrictionsReasonCode,
)

__all__ = [
    'AzureEntityResource',
    'CheckDomainAvailabilityParameter',
    'CheckDomainAvailabilityResult',
    'CheckSkuAvailabilityParameter',
    'CheckSkuAvailabilityResult',
    'CheckSkuAvailabilityResultList',
    'CognitiveServicesAccount',
    'CognitiveServicesAccountApiProperties',
    'CognitiveServicesAccountEnumerateSkusResult',
    'CognitiveServicesAccountKeys',
    'CognitiveServicesAccountProperties',
    'CognitiveServicesResourceAndSku',
    'Encryption',
    'Error', 'ErrorException',
    'ErrorBody',
    'Identity',
    'IpRule',
    'KeyVaultProperties',
    'MetricName',
    'NetworkRuleSet',
    'OperationDisplayInfo',
    'OperationEntity',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionProperties',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'RegenerateKeyParameters',
    'Resource',
    'ResourceSku',
    'ResourceSkuRestrictionInfo',
    'ResourceSkuRestrictions',
    'Sku',
    'TrackedResource',
    'Usage',
    'UsagesResult',
    'UserAssignedIdentity',
    'UserOwnedStorage',
    'VirtualNetworkRule',
    'CognitiveServicesAccountPaged',
    'ResourceSkuPaged',
    'OperationEntityPaged',
    'SkuTier',
    'ProvisioningState',
    'NetworkRuleAction',
    'KeySource',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
    'IdentityType',
    'KeyName',
    'UnitType',
    'QuotaUsageStatus',
    'ResourceSkuRestrictionsType',
    'ResourceSkuRestrictionsReasonCode',
]
