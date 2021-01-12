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
    from ._models_py3 import ConfluentAgreementResource
    from ._models_py3 import ErrorResponseBody
    from ._models_py3 import OfferDetail
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationResult
    from ._models_py3 import OrganizationResource
    from ._models_py3 import OrganizationResourceProperties
    from ._models_py3 import OrganizationResourcePropertiesOfferDetail
    from ._models_py3 import OrganizationResourcePropertiesUserDetail
    from ._models_py3 import OrganizationResourceUpdate
    from ._models_py3 import ResourceProviderDefaultErrorResponse, ResourceProviderDefaultErrorResponseException
    from ._models_py3 import UserDetail
except (SyntaxError, ImportError):
    from ._models import ConfluentAgreementResource
    from ._models import ErrorResponseBody
    from ._models import OfferDetail
    from ._models import OperationDisplay
    from ._models import OperationResult
    from ._models import OrganizationResource
    from ._models import OrganizationResourceProperties
    from ._models import OrganizationResourcePropertiesOfferDetail
    from ._models import OrganizationResourcePropertiesUserDetail
    from ._models import OrganizationResourceUpdate
    from ._models import ResourceProviderDefaultErrorResponse, ResourceProviderDefaultErrorResponseException
    from ._models import UserDetail
from ._paged_models import ConfluentAgreementResourcePaged
from ._paged_models import OperationResultPaged
from ._paged_models import OrganizationResourcePaged
from ._confluent_management_client_enums import (
    ProvisionState,
    SaaSOfferStatus,
)

__all__ = [
    'ConfluentAgreementResource',
    'ErrorResponseBody',
    'OfferDetail',
    'OperationDisplay',
    'OperationResult',
    'OrganizationResource',
    'OrganizationResourceProperties',
    'OrganizationResourcePropertiesOfferDetail',
    'OrganizationResourcePropertiesUserDetail',
    'OrganizationResourceUpdate',
    'ResourceProviderDefaultErrorResponse', 'ResourceProviderDefaultErrorResponseException',
    'UserDetail',
    'ConfluentAgreementResourcePaged',
    'OperationResultPaged',
    'OrganizationResourcePaged',
    'ProvisionState',
    'SaaSOfferStatus',
]
