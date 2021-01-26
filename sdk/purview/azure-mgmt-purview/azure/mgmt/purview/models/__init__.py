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
    from ._models_py3 import AccessKeys
    from ._models_py3 import Account
    from ._models_py3 import AccountEndpoints
    from ._models_py3 import AccountPropertiesEndpoints
    from ._models_py3 import AccountPropertiesManagedResources
    from ._models_py3 import AccountSku
    from ._models_py3 import AccountUpdateParameters
    from ._models_py3 import CheckNameAvailabilityRequest
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import CloudConnectors
    from ._models_py3 import DefaultAccountPayload
    from ._models_py3 import DeletedAccount
    from ._models_py3 import DeletedAccountList
    from ._models_py3 import DeletedAccountPropertiesModel
    from ._models_py3 import DimensionProperties
    from ._models_py3 import ErrorModel
    from ._models_py3 import ErrorResponseModel, ErrorResponseModelException
    from ._models_py3 import ErrorResponseModelError
    from ._models_py3 import Identity
    from ._models_py3 import ManagedResources
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationMetaLogSpecification
    from ._models_py3 import OperationMetaMetricSpecification
    from ._models_py3 import OperationMetaServiceSpecification
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyResource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AccessKeys
    from ._models import Account
    from ._models import AccountEndpoints
    from ._models import AccountPropertiesEndpoints
    from ._models import AccountPropertiesManagedResources
    from ._models import AccountSku
    from ._models import AccountUpdateParameters
    from ._models import CheckNameAvailabilityRequest
    from ._models import CheckNameAvailabilityResult
    from ._models import CloudConnectors
    from ._models import DefaultAccountPayload
    from ._models import DeletedAccount
    from ._models import DeletedAccountList
    from ._models import DeletedAccountPropertiesModel
    from ._models import DimensionProperties
    from ._models import ErrorModel
    from ._models import ErrorResponseModel, ErrorResponseModelException
    from ._models import ErrorResponseModelError
    from ._models import Identity
    from ._models import ManagedResources
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OperationMetaLogSpecification
    from ._models import OperationMetaMetricSpecification
    from ._models import OperationMetaServiceSpecification
    from ._models import PrivateEndpoint
    from ._models import PrivateEndpointConnection
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkServiceConnectionState
    from ._models import ProxyResource
    from ._models import TrackedResource
from ._paged_models import AccountPaged
from ._paged_models import OperationPaged
from ._paged_models import PrivateEndpointConnectionPaged
from ._paged_models import PrivateLinkResourcePaged
from ._purview_management_client_enums import (
    Status,
    ProvisioningState,
    PublicNetworkAccess,
    Name,
    Type,
    ScopeType,
    Reason,
)

__all__ = [
    'AccessKeys',
    'Account',
    'AccountEndpoints',
    'AccountPropertiesEndpoints',
    'AccountPropertiesManagedResources',
    'AccountSku',
    'AccountUpdateParameters',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResult',
    'CloudConnectors',
    'DefaultAccountPayload',
    'DeletedAccount',
    'DeletedAccountList',
    'DeletedAccountPropertiesModel',
    'DimensionProperties',
    'ErrorModel',
    'ErrorResponseModel', 'ErrorResponseModelException',
    'ErrorResponseModelError',
    'Identity',
    'ManagedResources',
    'Operation',
    'OperationDisplay',
    'OperationMetaLogSpecification',
    'OperationMetaMetricSpecification',
    'OperationMetaServiceSpecification',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateLinkResource',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'TrackedResource',
    'AccountPaged',
    'OperationPaged',
    'PrivateEndpointConnectionPaged',
    'PrivateLinkResourcePaged',
    'Status',
    'ProvisioningState',
    'PublicNetworkAccess',
    'Name',
    'Type',
    'ScopeType',
    'Reason',
]
