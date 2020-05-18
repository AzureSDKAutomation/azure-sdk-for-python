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
    from ._models_py3 import AccountKeyRegenerateRequest
    from ._models_py3 import AccountKeys
    from ._models_py3 import AzureEntityResource
    from ._models_py3 import CheckNameAvailabilityRequest
    from ._models_py3 import CheckNameAvailabilityResponse
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import ProxyResource
    from ._models_py3 import RemoteRenderingAccount
    from ._models_py3 import Resource
    from ._models_py3 import SpatialAnchorsAccount
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AccountKeyRegenerateRequest
    from ._models import AccountKeys
    from ._models import AzureEntityResource
    from ._models import CheckNameAvailabilityRequest
    from ._models import CheckNameAvailabilityResponse
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import ProxyResource
    from ._models import RemoteRenderingAccount
    from ._models import Resource
    from ._models import SpatialAnchorsAccount
    from ._models import TrackedResource
from ._paged_models import OperationPaged
from ._paged_models import RemoteRenderingAccountPaged
from ._paged_models import SpatialAnchorsAccountPaged
from ._mixed_reality_client_enums import (
    NameAvailability,
    NameUnavailableReason,
)

__all__ = [
    'AccountKeyRegenerateRequest',
    'AccountKeys',
    'AzureEntityResource',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'Operation',
    'OperationDisplay',
    'ProxyResource',
    'RemoteRenderingAccount',
    'Resource',
    'SpatialAnchorsAccount',
    'TrackedResource',
    'OperationPaged',
    'SpatialAnchorsAccountPaged',
    'RemoteRenderingAccountPaged',
    'NameAvailability',
    'NameUnavailableReason',
]
