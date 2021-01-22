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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Alias(Model):
    """The alias type. .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The alias name.
    :type name: str
    :param paths: The paths for an alias.
    :type paths:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.AliasPath]
    :param type: The type of the alias. Possible values include:
     'NotSpecified', 'PlainText', 'Mask'
    :type type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasType
    :param default_path: The default path for an alias.
    :type default_path: str
    :param default_pattern: The default pattern for an alias.
    :type default_pattern:
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPattern
    :ivar default_metadata: The default alias path metadata. Applies to the
     default path and to any alias path that doesn't have metadata
    :vartype default_metadata:
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPathMetadata
    """

    _validation = {
        'default_metadata': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'paths': {'key': 'paths', 'type': '[AliasPath]'},
        'type': {'key': 'type', 'type': 'AliasType'},
        'default_path': {'key': 'defaultPath', 'type': 'str'},
        'default_pattern': {'key': 'defaultPattern', 'type': 'AliasPattern'},
        'default_metadata': {'key': 'defaultMetadata', 'type': 'AliasPathMetadata'},
    }

    def __init__(self, **kwargs):
        super(Alias, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.paths = kwargs.get('paths', None)
        self.type = kwargs.get('type', None)
        self.default_path = kwargs.get('default_path', None)
        self.default_pattern = kwargs.get('default_pattern', None)
        self.default_metadata = None


class AliasPath(Model):
    """The type of the paths for alias.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param path: The path of an alias.
    :type path: str
    :param api_versions: The API versions.
    :type api_versions: list[str]
    :param pattern: The pattern for an alias path.
    :type pattern: ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPattern
    :ivar metadata: The metadata of the alias path. If missing, fall back to
     the default metadata of the alias.
    :vartype metadata:
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPathMetadata
    """

    _validation = {
        'metadata': {'readonly': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'api_versions': {'key': 'apiVersions', 'type': '[str]'},
        'pattern': {'key': 'pattern', 'type': 'AliasPattern'},
        'metadata': {'key': 'metadata', 'type': 'AliasPathMetadata'},
    }

    def __init__(self, **kwargs):
        super(AliasPath, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.api_versions = kwargs.get('api_versions', None)
        self.pattern = kwargs.get('pattern', None)
        self.metadata = None


class AliasPathMetadata(Model):
    """AliasPathMetadata.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of the token that the alias path is referring to.
     Possible values include: 'NotSpecified', 'Any', 'String', 'Object',
     'Array', 'Integer', 'Number', 'Boolean'
    :vartype type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPathTokenType
    :ivar attributes: The attributes of the token that the alias path is
     referring to. Possible values include: 'None', 'Modifiable'
    :vartype attributes: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPathAttributes
    """

    _validation = {
        'type': {'readonly': True},
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AliasPathMetadata, self).__init__(**kwargs)
        self.type = None
        self.attributes = None


class AliasPattern(Model):
    """The type of the pattern for an alias path.

    :param phrase: The alias pattern phrase.
    :type phrase: str
    :param variable: The alias pattern variable.
    :type variable: str
    :param type: The type of alias pattern. Possible values include:
     'NotSpecified', 'Extract'
    :type type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.AliasPatternType
    """

    _attribute_map = {
        'phrase': {'key': 'phrase', 'type': 'str'},
        'variable': {'key': 'variable', 'type': 'str'},
        'type': {'key': 'type', 'type': 'AliasPatternType'},
    }

    def __init__(self, **kwargs):
        super(AliasPattern, self).__init__(**kwargs)
        self.phrase = kwargs.get('phrase', None)
        self.variable = kwargs.get('variable', None)
        self.type = kwargs.get('type', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class DataEffect(Model):
    """The data effect definition.

    :param name: The data effect name.
    :type name: str
    :param details_schema: The data effect details schema.
    :type details_schema: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'details_schema': {'key': 'detailsSchema', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(DataEffect, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.details_schema = kwargs.get('details_schema', None)


class DataManifestCustomResourceFunctionDefinition(Model):
    """The custom resource function definition.

    :param name: The function name as it will appear in the policy rule. eg -
     'vault'.
    :type name: str
    :param fully_qualified_resource_type: The fully qualified control plane
     resource type that this function represents. eg -
     'Microsoft.KeyVault/vaults'.
    :type fully_qualified_resource_type: str
    :param default_properties: The top-level properties that can be selected
     on the function's output. eg - [ "name", "location" ] if vault().name and
     vault().location are supported
    :type default_properties: list[str]
    :param allow_custom_properties: A value indicating whether the custom
     properties within the property bag are allowed. Needs api-version to be
     specified in the policy rule eg - vault('2019-06-01').
    :type allow_custom_properties: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'fully_qualified_resource_type': {'key': 'fullyQualifiedResourceType', 'type': 'str'},
        'default_properties': {'key': 'defaultProperties', 'type': '[str]'},
        'allow_custom_properties': {'key': 'allowCustomProperties', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DataManifestCustomResourceFunctionDefinition, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.fully_qualified_resource_type = kwargs.get('fully_qualified_resource_type', None)
        self.default_properties = kwargs.get('default_properties', None)
        self.allow_custom_properties = kwargs.get('allow_custom_properties', None)


class DataPolicyManifest(Model):
    """The data policy manifest.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param namespaces: The list of namespaces for the data policy manifest.
    :type namespaces: list[str]
    :param policy_mode: The policy mode of the data policy manifest.
    :type policy_mode: str
    :param is_built_in_only: A value indicating whether policy mode is allowed
     only in built-in definitions.
    :type is_built_in_only: bool
    :param resource_type_aliases: An array of resource type aliases.
    :type resource_type_aliases:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.ResourceTypeAliases]
    :param effects: The effect definition.
    :type effects:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.DataEffect]
    :param field_values: The non-alias field accessor values that can be used
     in the policy rule.
    :type field_values: list[str]
    :param standard: The standard resource functions (subscription and/or
     resourceGroup).
    :type standard: list[str]
    :param custom: An array of data manifest custom resource definition.
    :type custom:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.DataManifestCustomResourceFunctionDefinition]
    :ivar id: The ID of the data policy manifest.
    :vartype id: str
    :ivar name: The name of the data policy manifest (it's the same as the
     Policy Mode).
    :vartype name: str
    :ivar type: The type of the resource
     (Microsoft.Authorization/dataPolicyManifests).
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'namespaces': {'key': 'properties.namespaces', 'type': '[str]'},
        'policy_mode': {'key': 'properties.policyMode', 'type': 'str'},
        'is_built_in_only': {'key': 'properties.isBuiltInOnly', 'type': 'bool'},
        'resource_type_aliases': {'key': 'properties.resourceTypeAliases', 'type': '[ResourceTypeAliases]'},
        'effects': {'key': 'properties.effects', 'type': '[DataEffect]'},
        'field_values': {'key': 'properties.fieldValues', 'type': '[str]'},
        'standard': {'key': 'properties.resourceFunctions.standard', 'type': '[str]'},
        'custom': {'key': 'properties.resourceFunctions.custom', 'type': '[DataManifestCustomResourceFunctionDefinition]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataPolicyManifest, self).__init__(**kwargs)
        self.namespaces = kwargs.get('namespaces', None)
        self.policy_mode = kwargs.get('policy_mode', None)
        self.is_built_in_only = kwargs.get('is_built_in_only', None)
        self.resource_type_aliases = kwargs.get('resource_type_aliases', None)
        self.effects = kwargs.get('effects', None)
        self.field_values = kwargs.get('field_values', None)
        self.standard = kwargs.get('standard', None)
        self.custom = kwargs.get('custom', None)
        self.id = None
        self.name = None
        self.type = None


class ErrorAdditionalInfo(Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(Model):
    """Error response.

    Common error response for all Azure Resource Manager APIs to return error
    details for failed operations. (This also follows the OData error response
    format.).

    :param error: The error object.
    :type error: ~azure.mgmt.resource.policy.v2020_09_01.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Identity(Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource identity.
    :vartype tenant_id: str
    :param type: The identity type. This is the only required field when
     adding a system assigned identity to a resource. Possible values include:
     'SystemAssigned', 'None'
    :type type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
    }

    def __init__(self, **kwargs):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class NonComplianceMessage(Model):
    """A message that describes why a resource is non-compliant with the policy.
    This is shown in 'deny' error messages and on resource's non-compliant
    compliance results.

    All required parameters must be populated in order to send to Azure.

    :param message: Required. A message that describes why a resource is
     non-compliant with the policy. This is shown in 'deny' error messages and
     on resource's non-compliant compliance results.
    :type message: str
    :param policy_definition_reference_id: The policy definition reference ID
     within a policy set definition the message is intended for. This is only
     applicable if the policy assignment assigns a policy set definition. If
     this is not provided the message applies to all policies assigned by this
     policy assignment.
    :type policy_definition_reference_id: str
    """

    _validation = {
        'message': {'required': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'policy_definition_reference_id': {'key': 'policyDefinitionReferenceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NonComplianceMessage, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)
        self.policy_definition_reference_id = kwargs.get('policy_definition_reference_id', None)


class ParameterDefinitionsValue(Model):
    """The definition of a parameter that can be provided to the policy.

    :param type: The data type of the parameter. Possible values include:
     'String', 'Array', 'Object', 'Boolean', 'Integer', 'Float', 'DateTime'
    :type type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.ParameterType
    :param allowed_values: The allowed values for the parameter.
    :type allowed_values: list[object]
    :param default_value: The default value for the parameter if no value is
     provided.
    :type default_value: object
    :param metadata: General metadata for the parameter.
    :type metadata:
     ~azure.mgmt.resource.policy.v2020_09_01.models.ParameterDefinitionsValueMetadata
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'allowed_values': {'key': 'allowedValues', 'type': '[object]'},
        'default_value': {'key': 'defaultValue', 'type': 'object'},
        'metadata': {'key': 'metadata', 'type': 'ParameterDefinitionsValueMetadata'},
    }

    def __init__(self, **kwargs):
        super(ParameterDefinitionsValue, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.allowed_values = kwargs.get('allowed_values', None)
        self.default_value = kwargs.get('default_value', None)
        self.metadata = kwargs.get('metadata', None)


class ParameterDefinitionsValueMetadata(Model):
    """General metadata for the parameter.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param display_name: The display name for the parameter.
    :type display_name: str
    :param description: The description of the parameter.
    :type description: str
    :param strong_type: Used when assigning the policy definition through the
     portal. Provides a context aware list of values for the user to choose
     from.
    :type strong_type: str
    :param assign_permissions: Set to true to have Azure portal create role
     assignments on the resource ID or resource scope value of this parameter
     during policy assignment. This property is useful in case you wish to
     assign permissions outside the assignment scope.
    :type assign_permissions: bool
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'strong_type': {'key': 'strongType', 'type': 'str'},
        'assign_permissions': {'key': 'assignPermissions', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ParameterDefinitionsValueMetadata, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.strong_type = kwargs.get('strong_type', None)
        self.assign_permissions = kwargs.get('assign_permissions', None)


class ParameterValuesValue(Model):
    """The value of a parameter.

    :param value: The value of the parameter.
    :type value: object
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ParameterValuesValue, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class PolicyAssignment(Model):
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition or policy set
     definition being assigned.
    :type policy_definition_id: str
    :ivar scope: The scope for the policy assignment.
    :vartype scope: str
    :param not_scopes: The policy's excluded scopes.
    :type not_scopes: list[str]
    :param parameters: The parameter values for the assigned policy rule. The
     keys are the parameter names.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2020_09_01.models.ParameterValuesValue]
    :param description: This message will be part of response in case of
     policy violation.
    :type description: str
    :param metadata: The policy assignment metadata. Metadata is an open ended
     object and is typically a collection of key value pairs.
    :type metadata: object
    :param enforcement_mode: The policy assignment enforcement mode. Possible
     values are Default and DoNotEnforce. Possible values include: 'Default',
     'DoNotEnforce'. Default value: "Default" .
    :type enforcement_mode: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.EnforcementMode
    :param non_compliance_messages: The messages that describe why a resource
     is non-compliant with the policy.
    :type non_compliance_messages:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.NonComplianceMessage]
    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :ivar type: The type of the policy assignment.
    :vartype type: str
    :ivar name: The name of the policy assignment.
    :vartype name: str
    :param location: The location of the policy assignment. Only required when
     utilizing managed identity.
    :type location: str
    :param identity: The managed identity associated with the policy
     assignment.
    :type identity: ~azure.mgmt.resource.policy.v2020_09_01.models.Identity
    """

    _validation = {
        'scope': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'not_scopes': {'key': 'properties.notScopes', 'type': '[str]'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterValuesValue}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'enforcement_mode': {'key': 'properties.enforcementMode', 'type': 'str'},
        'non_compliance_messages': {'key': 'properties.nonComplianceMessages', 'type': '[NonComplianceMessage]'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, **kwargs):
        super(PolicyAssignment, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.scope = None
        self.not_scopes = kwargs.get('not_scopes', None)
        self.parameters = kwargs.get('parameters', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.enforcement_mode = kwargs.get('enforcement_mode', "Default")
        self.non_compliance_messages = kwargs.get('non_compliance_messages', None)
        self.id = None
        self.type = None
        self.name = None
        self.location = kwargs.get('location', None)
        self.identity = kwargs.get('identity', None)


class PolicyDefinition(Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param policy_type: The type of policy definition. Possible values are
     NotSpecified, BuiltIn, Custom, and Static. Possible values include:
     'NotSpecified', 'BuiltIn', 'Custom', 'Static'
    :type policy_type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyType
    :param mode: The policy definition mode. Some examples are All, Indexed,
     Microsoft.KeyVault.Data. Default value: "Indexed" .
    :type mode: str
    :param display_name: The display name of the policy definition.
    :type display_name: str
    :param description: The policy definition description.
    :type description: str
    :param policy_rule: The policy rule.
    :type policy_rule: object
    :param metadata: The policy definition metadata.  Metadata is an open
     ended object and is typically a collection of key value pairs.
    :type metadata: object
    :param parameters: The parameter definitions for parameters used in the
     policy rule. The keys are the parameter names.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2020_09_01.models.ParameterDefinitionsValue]
    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    :ivar type: The type of the resource
     (Microsoft.Authorization/policyDefinitions).
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterDefinitionsValue}'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicyDefinition, self).__init__(**kwargs)
        self.policy_type = kwargs.get('policy_type', None)
        self.mode = kwargs.get('mode', "Indexed")
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.policy_rule = kwargs.get('policy_rule', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)
        self.id = None
        self.name = None
        self.type = None


class PolicyDefinitionGroup(Model):
    """The policy definition group.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the group.
    :type name: str
    :param display_name: The group's display name.
    :type display_name: str
    :param category: The group's category.
    :type category: str
    :param description: The group's description.
    :type description: str
    :param additional_metadata_id: A resource ID of a resource that contains
     additional metadata about the group.
    :type additional_metadata_id: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'additional_metadata_id': {'key': 'additionalMetadataId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicyDefinitionGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.category = kwargs.get('category', None)
        self.description = kwargs.get('description', None)
        self.additional_metadata_id = kwargs.get('additional_metadata_id', None)


class PolicyDefinitionReference(Model):
    """The policy definition reference.

    All required parameters must be populated in order to send to Azure.

    :param policy_definition_id: Required. The ID of the policy definition or
     policy set definition.
    :type policy_definition_id: str
    :param parameters: The parameter values for the referenced policy rule.
     The keys are the parameter names.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2020_09_01.models.ParameterValuesValue]
    :param policy_definition_reference_id: A unique id (within the policy set
     definition) for this policy definition reference.
    :type policy_definition_reference_id: str
    :param group_names: The name of the groups that this policy definition
     reference belongs to.
    :type group_names: list[str]
    """

    _validation = {
        'policy_definition_id': {'required': True},
    }

    _attribute_map = {
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterValuesValue}'},
        'policy_definition_reference_id': {'key': 'policyDefinitionReferenceId', 'type': 'str'},
        'group_names': {'key': 'groupNames', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(PolicyDefinitionReference, self).__init__(**kwargs)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.parameters = kwargs.get('parameters', None)
        self.policy_definition_reference_id = kwargs.get('policy_definition_reference_id', None)
        self.group_names = kwargs.get('group_names', None)


class PolicySetDefinition(Model):
    """The policy set definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param policy_type: The type of policy definition. Possible values are
     NotSpecified, BuiltIn, Custom, and Static. Possible values include:
     'NotSpecified', 'BuiltIn', 'Custom', 'Static'
    :type policy_type: str or
     ~azure.mgmt.resource.policy.v2020_09_01.models.PolicyType
    :param display_name: The display name of the policy set definition.
    :type display_name: str
    :param description: The policy set definition description.
    :type description: str
    :param metadata: The policy set definition metadata.  Metadata is an open
     ended object and is typically a collection of key value pairs.
    :type metadata: object
    :param parameters: The policy set definition parameters that can be used
     in policy definition references.
    :type parameters: dict[str,
     ~azure.mgmt.resource.policy.v2020_09_01.models.ParameterDefinitionsValue]
    :param policy_definitions: Required. An array of policy definition
     references.
    :type policy_definitions:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinitionReference]
    :param policy_definition_groups: The metadata describing groups of policy
     definition references within the policy set definition.
    :type policy_definition_groups:
     list[~azure.mgmt.resource.policy.v2020_09_01.models.PolicyDefinitionGroup]
    :ivar id: The ID of the policy set definition.
    :vartype id: str
    :ivar name: The name of the policy set definition.
    :vartype name: str
    :ivar type: The type of the resource
     (Microsoft.Authorization/policySetDefinitions).
    :vartype type: str
    """

    _validation = {
        'policy_definitions': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterDefinitionsValue}'},
        'policy_definitions': {'key': 'properties.policyDefinitions', 'type': '[PolicyDefinitionReference]'},
        'policy_definition_groups': {'key': 'properties.policyDefinitionGroups', 'type': '[PolicyDefinitionGroup]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicySetDefinition, self).__init__(**kwargs)
        self.policy_type = kwargs.get('policy_type', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)
        self.policy_definitions = kwargs.get('policy_definitions', None)
        self.policy_definition_groups = kwargs.get('policy_definition_groups', None)
        self.id = None
        self.name = None
        self.type = None


class ResourceTypeAliases(Model):
    """The resource type aliases definition.

    :param resource_type: The resource type name.
    :type resource_type: str
    :param aliases: The aliases for property names.
    :type aliases: list[~azure.mgmt.resource.policy.v2020_09_01.models.Alias]
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'aliases': {'key': 'aliases', 'type': '[Alias]'},
    }

    def __init__(self, **kwargs):
        super(ResourceTypeAliases, self).__init__(**kwargs)
        self.resource_type = kwargs.get('resource_type', None)
        self.aliases = kwargs.get('aliases', None)
