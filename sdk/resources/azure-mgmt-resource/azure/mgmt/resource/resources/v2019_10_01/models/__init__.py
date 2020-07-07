# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Alias
    from ._models_py3 import AliasPath
    from ._models_py3 import AliasPattern
    from ._models_py3 import BasicDependency
    from ._models_py3 import DebugSetting
    from ._models_py3 import Dependency
    from ._models_py3 import Deployment
    from ._models_py3 import DeploymentExportResult
    from ._models_py3 import DeploymentExtended
    from ._models_py3 import DeploymentExtendedFilter
    from ._models_py3 import DeploymentListResult
    from ._models_py3 import DeploymentOperation
    from ._models_py3 import DeploymentOperationProperties
    from ._models_py3 import DeploymentOperationsListResult
    from ._models_py3 import DeploymentProperties
    from ._models_py3 import DeploymentPropertiesExtended
    from ._models_py3 import DeploymentValidateResult
    from ._models_py3 import DeploymentWhatIf
    from ._models_py3 import DeploymentWhatIfProperties
    from ._models_py3 import DeploymentWhatIfSettings
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExportTemplateRequest
    from ._models_py3 import GenericResource
    from ._models_py3 import GenericResourceExpanded
    from ._models_py3 import GenericResourceFilter
    from ._models_py3 import HttpMessage
    from ._models_py3 import Identity
    from ._models_py3 import IdentityUserAssignedIdentitiesValue
    from ._models_py3 import OnErrorDeployment
    from ._models_py3 import OnErrorDeploymentExtended
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import ParametersLink
    from ._models_py3 import Plan
    from ._models_py3 import Provider
    from ._models_py3 import ProviderListResult
    from ._models_py3 import ProviderResourceType
    from ._models_py3 import Resource
    from ._models_py3 import ResourceGroup
    from ._models_py3 import ResourceGroupExportResult
    from ._models_py3 import ResourceGroupFilter
    from ._models_py3 import ResourceGroupListResult
    from ._models_py3 import ResourceGroupPatchable
    from ._models_py3 import ResourceGroupProperties
    from ._models_py3 import ResourceListResult
    from ._models_py3 import ResourceProviderOperationDisplayProperties
    from ._models_py3 import ResourceReference
    from ._models_py3 import ResourcesMoveInfo
    from ._models_py3 import ScopedDeployment
    from ._models_py3 import ScopedDeploymentWhatIf
    from ._models_py3 import Sku
    from ._models_py3 import SubResource
    from ._models_py3 import TagCount
    from ._models_py3 import TagDetails
    from ._models_py3 import TagValue
    from ._models_py3 import Tags
    from ._models_py3 import TagsListResult
    from ._models_py3 import TagsPatchResource
    from ._models_py3 import TagsResource
    from ._models_py3 import TargetResource
    from ._models_py3 import TemplateHashResult
    from ._models_py3 import TemplateLink
    from ._models_py3 import WhatIfChange
    from ._models_py3 import WhatIfOperationResult
    from ._models_py3 import WhatIfPropertyChange
except (SyntaxError, ImportError):
    from ._models import Alias  # type: ignore
    from ._models import AliasPath  # type: ignore
    from ._models import AliasPattern  # type: ignore
    from ._models import BasicDependency  # type: ignore
    from ._models import DebugSetting  # type: ignore
    from ._models import Dependency  # type: ignore
    from ._models import Deployment  # type: ignore
    from ._models import DeploymentExportResult  # type: ignore
    from ._models import DeploymentExtended  # type: ignore
    from ._models import DeploymentExtendedFilter  # type: ignore
    from ._models import DeploymentListResult  # type: ignore
    from ._models import DeploymentOperation  # type: ignore
    from ._models import DeploymentOperationProperties  # type: ignore
    from ._models import DeploymentOperationsListResult  # type: ignore
    from ._models import DeploymentProperties  # type: ignore
    from ._models import DeploymentPropertiesExtended  # type: ignore
    from ._models import DeploymentValidateResult  # type: ignore
    from ._models import DeploymentWhatIf  # type: ignore
    from ._models import DeploymentWhatIfProperties  # type: ignore
    from ._models import DeploymentWhatIfSettings  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExportTemplateRequest  # type: ignore
    from ._models import GenericResource  # type: ignore
    from ._models import GenericResourceExpanded  # type: ignore
    from ._models import GenericResourceFilter  # type: ignore
    from ._models import HttpMessage  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import IdentityUserAssignedIdentitiesValue  # type: ignore
    from ._models import OnErrorDeployment  # type: ignore
    from ._models import OnErrorDeploymentExtended  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import ParametersLink  # type: ignore
    from ._models import Plan  # type: ignore
    from ._models import Provider  # type: ignore
    from ._models import ProviderListResult  # type: ignore
    from ._models import ProviderResourceType  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceGroup  # type: ignore
    from ._models import ResourceGroupExportResult  # type: ignore
    from ._models import ResourceGroupFilter  # type: ignore
    from ._models import ResourceGroupListResult  # type: ignore
    from ._models import ResourceGroupPatchable  # type: ignore
    from ._models import ResourceGroupProperties  # type: ignore
    from ._models import ResourceListResult  # type: ignore
    from ._models import ResourceProviderOperationDisplayProperties  # type: ignore
    from ._models import ResourceReference  # type: ignore
    from ._models import ResourcesMoveInfo  # type: ignore
    from ._models import ScopedDeployment  # type: ignore
    from ._models import ScopedDeploymentWhatIf  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import TagCount  # type: ignore
    from ._models import TagDetails  # type: ignore
    from ._models import TagValue  # type: ignore
    from ._models import Tags  # type: ignore
    from ._models import TagsListResult  # type: ignore
    from ._models import TagsPatchResource  # type: ignore
    from ._models import TagsResource  # type: ignore
    from ._models import TargetResource  # type: ignore
    from ._models import TemplateHashResult  # type: ignore
    from ._models import TemplateLink  # type: ignore
    from ._models import WhatIfChange  # type: ignore
    from ._models import WhatIfOperationResult  # type: ignore
    from ._models import WhatIfPropertyChange  # type: ignore

from ._resource_management_client_enums import (
    AliasPatternType,
    AliasType,
    ChangeType,
    DeploymentMode,
    OnErrorDeploymentType,
    PropertyChangeType,
    ProvisioningOperation,
    ResourceIdentityType,
    TagsPatchResourceOperation,
    WhatIfResultFormat,
)

__all__ = [
    'Alias',
    'AliasPath',
    'AliasPattern',
    'BasicDependency',
    'DebugSetting',
    'Dependency',
    'Deployment',
    'DeploymentExportResult',
    'DeploymentExtended',
    'DeploymentExtendedFilter',
    'DeploymentListResult',
    'DeploymentOperation',
    'DeploymentOperationProperties',
    'DeploymentOperationsListResult',
    'DeploymentProperties',
    'DeploymentPropertiesExtended',
    'DeploymentValidateResult',
    'DeploymentWhatIf',
    'DeploymentWhatIfProperties',
    'DeploymentWhatIfSettings',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'ExportTemplateRequest',
    'GenericResource',
    'GenericResourceExpanded',
    'GenericResourceFilter',
    'HttpMessage',
    'Identity',
    'IdentityUserAssignedIdentitiesValue',
    'OnErrorDeployment',
    'OnErrorDeploymentExtended',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'ParametersLink',
    'Plan',
    'Provider',
    'ProviderListResult',
    'ProviderResourceType',
    'Resource',
    'ResourceGroup',
    'ResourceGroupExportResult',
    'ResourceGroupFilter',
    'ResourceGroupListResult',
    'ResourceGroupPatchable',
    'ResourceGroupProperties',
    'ResourceListResult',
    'ResourceProviderOperationDisplayProperties',
    'ResourceReference',
    'ResourcesMoveInfo',
    'ScopedDeployment',
    'ScopedDeploymentWhatIf',
    'Sku',
    'SubResource',
    'TagCount',
    'TagDetails',
    'TagValue',
    'Tags',
    'TagsListResult',
    'TagsPatchResource',
    'TagsResource',
    'TargetResource',
    'TemplateHashResult',
    'TemplateLink',
    'WhatIfChange',
    'WhatIfOperationResult',
    'WhatIfPropertyChange',
    'AliasPatternType',
    'AliasType',
    'ChangeType',
    'DeploymentMode',
    'OnErrorDeploymentType',
    'PropertyChangeType',
    'ProvisioningOperation',
    'ResourceIdentityType',
    'TagsPatchResourceOperation',
    'WhatIfResultFormat',
]
