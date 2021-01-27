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
    from ._models_py3 import AutoScaleVCore
    from ._models_py3 import AutoScaleVCoreSku
    from ._models_py3 import AutoScaleVCoreUpdateParameters
    from ._models_py3 import CapacitySku
    from ._models_py3 import CheckCapacityNameAvailabilityParameters
    from ._models_py3 import CheckCapacityNameAvailabilityResult
    from ._models_py3 import DedicatedCapacity
    from ._models_py3 import DedicatedCapacityAdministrators
    from ._models_py3 import DedicatedCapacityUpdateParameters
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ErrorResponseError
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Resource
    from ._models_py3 import SkuDetailsForExistingResource
    from ._models_py3 import SkuEnumerationForExistingResourceResult
    from ._models_py3 import SkuEnumerationForNewResourceResult
    from ._models_py3 import SystemData
except (SyntaxError, ImportError):
    from ._models import AutoScaleVCore
    from ._models import AutoScaleVCoreSku
    from ._models import AutoScaleVCoreUpdateParameters
    from ._models import CapacitySku
    from ._models import CheckCapacityNameAvailabilityParameters
    from ._models import CheckCapacityNameAvailabilityResult
    from ._models import DedicatedCapacity
    from ._models import DedicatedCapacityAdministrators
    from ._models import DedicatedCapacityUpdateParameters
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ErrorResponseError
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Resource
    from ._models import SkuDetailsForExistingResource
    from ._models import SkuEnumerationForExistingResourceResult
    from ._models import SkuEnumerationForNewResourceResult
    from ._models import SystemData
from ._paged_models import AutoScaleVCorePaged
from ._paged_models import DedicatedCapacityPaged
from ._paged_models import OperationPaged
from ._power_bi_dedicated_management_client_enums import (
    IdentityType,
    CapacitySkuTier,
    State,
    CapacityProvisioningState,
    VCoreSkuTier,
    VCoreProvisioningState,
)

__all__ = [
    'AutoScaleVCore',
    'AutoScaleVCoreSku',
    'AutoScaleVCoreUpdateParameters',
    'CapacitySku',
    'CheckCapacityNameAvailabilityParameters',
    'CheckCapacityNameAvailabilityResult',
    'DedicatedCapacity',
    'DedicatedCapacityAdministrators',
    'DedicatedCapacityUpdateParameters',
    'ErrorResponse', 'ErrorResponseException',
    'ErrorResponseError',
    'Operation',
    'OperationDisplay',
    'Resource',
    'SkuDetailsForExistingResource',
    'SkuEnumerationForExistingResourceResult',
    'SkuEnumerationForNewResourceResult',
    'SystemData',
    'DedicatedCapacityPaged',
    'OperationPaged',
    'AutoScaleVCorePaged',
    'IdentityType',
    'CapacitySkuTier',
    'State',
    'CapacityProvisioningState',
    'VCoreSkuTier',
    'VCoreProvisioningState',
]
