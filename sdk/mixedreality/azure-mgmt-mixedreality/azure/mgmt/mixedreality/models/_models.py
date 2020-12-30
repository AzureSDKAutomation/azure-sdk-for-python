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


class AccountKeyRegenerateRequest(Model):
    """Request for account key regeneration.

    :param serial: serial of key to be regenerated. Default value: 1 .
    :type serial: int
    """

    _attribute_map = {
        'serial': {'key': 'serial', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AccountKeyRegenerateRequest, self).__init__(**kwargs)
        self.serial = kwargs.get('serial', 1)


class AccountKeys(Model):
    """Developer Keys of account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar primary_key: value of primary key.
    :vartype primary_key: str
    :ivar secondary_key: value of secondary key.
    :vartype secondary_key: str
    """

    _validation = {
        'primary_key': {'readonly': True},
        'secondary_key': {'readonly': True},
    }

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AccountKeys, self).__init__(**kwargs)
        self.primary_key = None
        self.secondary_key = None


class Resource(Model):
    """Resource.

    Common fields that are returned in the response for all Azure Resource
    Manager resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AzureEntityResource(Resource):
    """Entity Resource.

    The resource model definition for an Azure Resource Manager resource with
    an etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CheckNameAvailabilityRequest(Model):
    """Check Name Availability Request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Resource Name To Verify
    :type name: str
    :param type: Required. Fully qualified resource type which includes
     provider namespace
    :type type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityRequest, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)


class CheckNameAvailabilityResponse(Model):
    """Check Name Availability Response.

    All required parameters must be populated in order to send to Azure.

    :param name_available: Required. if name Available
    :type name_available: bool
    :param reason: Resource Name To Verify. Possible values include:
     'Invalid', 'AlreadyExists'
    :type reason: str or ~azure.mgmt.mixedreality.models.NameUnavailableReason
    :param message: detail message
    :type message: str
    """

    _validation = {
        'name_available': {'required': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityResponse, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class CloudError(Model):
    """An Error response.

    :param error:
    :type error: ~azure.mgmt.mixedreality.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, **kwargs):
        super(CloudError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """An error response from Azure.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for displaying in a user interface.
    :type message: str
    :param target: The target of the particular error. For example, the name
     of the property in error.
    :type target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.mixedreality.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(self, **kwargs):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)


class Identity(Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: 'SystemAssigned'
    :type type: str or ~azure.mgmt.mixedreality.models.ResourceIdentityType
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


class Operation(Model):
    """REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.mixedreality.models.OperationDisplay
    :param is_data_action: Whether or not this is a data plane operation
    :type is_data_action: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.is_data_action = kwargs.get('is_data_action', None)


class OperationDisplay(Model):
    """The object that represents the operation.

    All required parameters must be populated in order to send to Azure.

    :param provider: Required. Service provider: Microsoft.ResourceProvider
    :type provider: str
    :param resource: Required. Resource on which the operation is performed:
     Profile, endpoint, etc.
    :type resource: str
    :param operation: Required. Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Required. Description of operation
    :type description: str
    """

    _validation = {
        'provider': {'required': True},
        'resource': {'required': True},
        'operation': {'required': True},
        'description': {'required': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class Plan(Model):
    """Plan for the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. A user defined name of the 3rd Party Artifact that
     is being procured.
    :type name: str
    :param publisher: Required. The publisher of the 3rd Party Artifact that
     is being bought. E.g. NewRelic
    :type publisher: str
    :param product: Required. The 3rd Party artifact that is being procured.
     E.g. NewRelic. Product maps to the OfferID specified for the artifact at
     the time of Data Market onboarding.
    :type product: str
    :param promotion_code: A publisher provided promotion code as provisioned
     in Data Market for the said product/artifact.
    :type promotion_code: str
    :param version: The version of the desired product/artifact.
    :type version: str
    """

    _validation = {
        'name': {'required': True},
        'publisher': {'required': True},
        'product': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Plan, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.publisher = kwargs.get('publisher', None)
        self.product = kwargs.get('product', None)
        self.promotion_code = kwargs.get('promotion_code', None)
        self.version = kwargs.get('version', None)


class ProxyResource(Resource):
    """Proxy Resource.

    The resource model definition for a Azure Resource Manager proxy resource.
    It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProxyResource, self).__init__(**kwargs)


class TrackedResource(Resource):
    """Tracked Resource.

    The resource model definition for an Azure Resource Manager tracked top
    level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)


class RemoteRenderingAccount(TrackedResource):
    """RemoteRenderingAccount Response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param identity:
    :type identity:
     ~azure.mgmt.mixedreality.models.RemoteRenderingAccountIdentity
    :ivar account_id: unique id of certain account.
    :vartype account_id: str
    :ivar account_domain: Correspond domain name of certain Spatial Anchors
     Account
    :vartype account_domain: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'account_id': {'readonly': True},
        'account_domain': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'RemoteRenderingAccountIdentity'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
        'account_domain': {'key': 'properties.accountDomain', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RemoteRenderingAccount, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.account_id = None
        self.account_domain = None


class RemoteRenderingAccountIdentity(Identity):
    """RemoteRenderingAccountIdentity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: 'SystemAssigned'
    :type type: str or ~azure.mgmt.mixedreality.models.ResourceIdentityType
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
        super(RemoteRenderingAccountIdentity, self).__init__(**kwargs)


class ResourceModelWithAllowedPropertySet(Model):
    """The resource model definition containing the full set of allowed properties
    for a resource. Except properties bag, there cannot be a top level property
    outside of this set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param location: The geo-location where the resource lives
    :type location: str
    :param managed_by: The fully qualified resource ID of the resource that
     manages this resource. Indicates if this resource is managed by another
     Azure resource. If this is present, complete mode deployment will not
     delete the resource if it is removed from the template since it is managed
     by another resource.
    :type managed_by: str
    :param kind: Metadata used by portal/tooling/etc to render different UX
     experiences for resources of the same type; e.g. ApiApps are a kind of
     Microsoft.Web/sites type.  If supported, the resource provider must
     validate and persist this value.
    :type kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the
     response body, it must also be provided as a header per the normal etag
     convention.  Entity tags are used for comparing two or more entities from
     the same requested resource. HTTP/1.1 uses entity tags in the etag
     (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26),
     and If-Range (section 14.27) header fields.
    :vartype etag: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param identity:
    :type identity:
     ~azure.mgmt.mixedreality.models.ResourceModelWithAllowedPropertySetIdentity
    :param sku:
    :type sku:
     ~azure.mgmt.mixedreality.models.ResourceModelWithAllowedPropertySetSku
    :param plan:
    :type plan:
     ~azure.mgmt.mixedreality.models.ResourceModelWithAllowedPropertySetPlan
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'pattern': r'^[-\w\._,\(\)]+$'},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ResourceModelWithAllowedPropertySetIdentity'},
        'sku': {'key': 'sku', 'type': 'ResourceModelWithAllowedPropertySetSku'},
        'plan': {'key': 'plan', 'type': 'ResourceModelWithAllowedPropertySetPlan'},
    }

    def __init__(self, **kwargs):
        super(ResourceModelWithAllowedPropertySet, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.managed_by = kwargs.get('managed_by', None)
        self.kind = kwargs.get('kind', None)
        self.etag = None
        self.tags = kwargs.get('tags', None)
        self.identity = kwargs.get('identity', None)
        self.sku = kwargs.get('sku', None)
        self.plan = kwargs.get('plan', None)


class ResourceModelWithAllowedPropertySetIdentity(Identity):
    """ResourceModelWithAllowedPropertySetIdentity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: 'SystemAssigned'
    :type type: str or ~azure.mgmt.mixedreality.models.ResourceIdentityType
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
        super(ResourceModelWithAllowedPropertySetIdentity, self).__init__(**kwargs)


class ResourceModelWithAllowedPropertySetPlan(Plan):
    """ResourceModelWithAllowedPropertySetPlan.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. A user defined name of the 3rd Party Artifact that
     is being procured.
    :type name: str
    :param publisher: Required. The publisher of the 3rd Party Artifact that
     is being bought. E.g. NewRelic
    :type publisher: str
    :param product: Required. The 3rd Party artifact that is being procured.
     E.g. NewRelic. Product maps to the OfferID specified for the artifact at
     the time of Data Market onboarding.
    :type product: str
    :param promotion_code: A publisher provided promotion code as provisioned
     in Data Market for the said product/artifact.
    :type promotion_code: str
    :param version: The version of the desired product/artifact.
    :type version: str
    """

    _validation = {
        'name': {'required': True},
        'publisher': {'required': True},
        'product': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceModelWithAllowedPropertySetPlan, self).__init__(**kwargs)


class Sku(Model):
    """The resource model definition representing SKU.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Ex - P3. It is typically a
     letter+number code
    :type name: str
    :param tier: This field is required to be implemented by the Resource
     Provider if the service has more than one tier, but is not required on a
     PUT. Possible values include: 'Free', 'Basic', 'Standard', 'Premium'
    :type tier: str or ~azure.mgmt.mixedreality.models.SkuTier
    :param size: The SKU size. When the name field is the combination of tier
     and some other value, this would be the standalone code.
    :type size: str
    :param family: If the service has different generations of hardware, for
     the same SKU, then that can be captured here.
    :type family: str
    :param capacity: If the SKU supports scale out/in then the capacity
     integer should be included. If scale out/in is not possible for the
     resource this may be omitted.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'SkuTier'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
        self.size = kwargs.get('size', None)
        self.family = kwargs.get('family', None)
        self.capacity = kwargs.get('capacity', None)


class ResourceModelWithAllowedPropertySetSku(Sku):
    """ResourceModelWithAllowedPropertySetSku.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Ex - P3. It is typically a
     letter+number code
    :type name: str
    :param tier: This field is required to be implemented by the Resource
     Provider if the service has more than one tier, but is not required on a
     PUT. Possible values include: 'Free', 'Basic', 'Standard', 'Premium'
    :type tier: str or ~azure.mgmt.mixedreality.models.SkuTier
    :param size: The SKU size. When the name field is the combination of tier
     and some other value, this would be the standalone code.
    :type size: str
    :param family: If the service has different generations of hardware, for
     the same SKU, then that can be captured here.
    :type family: str
    :param capacity: If the SKU supports scale out/in then the capacity
     integer should be included. If scale out/in is not possible for the
     resource this may be omitted.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'SkuTier'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ResourceModelWithAllowedPropertySetSku, self).__init__(**kwargs)


class SpatialAnchorsAccount(TrackedResource):
    """SpatialAnchorsAccount Response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :ivar account_id: unique id of certain account.
    :vartype account_id: str
    :ivar account_domain: Correspond domain name of certain Spatial Anchors
     Account
    :vartype account_domain: str
    :param identity: The identity associated with this account
    :type identity: ~azure.mgmt.mixedreality.models.Identity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'account_id': {'readonly': True},
        'account_domain': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
        'account_domain': {'key': 'properties.accountDomain', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, **kwargs):
        super(SpatialAnchorsAccount, self).__init__(**kwargs)
        self.account_id = None
        self.account_domain = None
        self.identity = kwargs.get('identity', None)
