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


class AdminKeyResult(Model):
    """Response containing the primary and secondary admin API keys for a given
    Azure Cognitive Search service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar primary_key: The primary admin API key of the Search service.
    :vartype primary_key: str
    :ivar secondary_key: The secondary admin API key of the Search service.
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

    def __init__(self, **kwargs) -> None:
        super(AdminKeyResult, self).__init__(**kwargs)
        self.primary_key = None
        self.secondary_key = None


class CheckNameAvailabilityInput(Model):
    """Input of check name availability API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The Search service name to validate. Search service
     names must only contain lowercase letters, digits or dashes, cannot use
     dash as the first two or last one characters, cannot contain consecutive
     dashes, and must be between 2 and 60 characters in length.
    :type name: str
    :ivar type: Required. The type of the resource whose name is to be
     validated. This value must always be 'searchServices'. Default value:
     "searchServices" .
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "searchServices"

    def __init__(self, *, name: str, **kwargs) -> None:
        super(CheckNameAvailabilityInput, self).__init__(**kwargs)
        self.name = name


class CheckNameAvailabilityOutput(Model):
    """Output of check name availability API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar is_name_available: A value indicating whether the name is available.
    :vartype is_name_available: bool
    :ivar reason: The reason why the name is not available. 'Invalid'
     indicates the name provided does not match the naming requirements
     (incorrect length, unsupported characters, etc.). 'AlreadyExists'
     indicates that the name is already in use and is therefore unavailable.
     Possible values include: 'Invalid', 'AlreadyExists'
    :vartype reason: str or ~azure.mgmt.search.models.UnavailableNameReason
    :ivar message: A message that explains why the name is invalid and
     provides resource naming requirements. Available only if 'Invalid' is
     returned in the 'reason' property.
    :vartype message: str
    """

    _validation = {
        'is_name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'is_name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(CheckNameAvailabilityOutput, self).__init__(**kwargs)
        self.is_name_available = None
        self.reason = None
        self.message = None


class CloudError(Model):
    """Contains information about an API error.

    :param error: Describes a particular API error with an error code and a
     message.
    :type error: ~azure.mgmt.search.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """Describes a particular API error with an error code and a message.

    :param code: An error code that describes the error condition more
     precisely than an HTTP status code. Can be used to programmatically handle
     specific error cases.
    :type code: str
    :param message: A message that describes the error in detail and provides
     debugging information.
    :type message: str
    :param target: The target of the particular error (for example, the name
     of the property in error).
    :type target: str
    :param details: Contains nested errors that are related to this error.
    :type details: list[~azure.mgmt.search.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(self, *, code: str=None, message: str=None, target: str=None, details=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class Identity(Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: Required. The identity type. Possible values include: 'None',
     'SystemAssigned'
    :type type: str or ~azure.mgmt.search.models.IdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'IdentityType'},
    }

    def __init__(self, *, type, **kwargs) -> None:
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class IpRule(Model):
    """The IP restriction rule of the Azure Cognitive Search service.

    :param value: Value corresponding to a single IPv4 address (eg.,
     123.1.2.3) or an IP range in CIDR format (eg., 123.1.2.3/24) to be
     allowed.
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str=None, **kwargs) -> None:
        super(IpRule, self).__init__(**kwargs)
        self.value = value


class NetworkRuleSet(Model):
    """Network specific rules that determine how the Azure Cognitive Search
    service may be reached.

    :param ip_rules: A list of IP restriction rules that defines the inbound
     network(s) with allowing access to the search service endpoint. At the
     meantime, all other public IP networks are blocked by the firewall. These
     restriction rules are applied only when the 'publicNetworkAccess' of the
     search service is 'enabled'; otherwise, traffic over public interface is
     not allowed even with any public IP rules, and private endpoint
     connections would be the exclusive access method.
    :type ip_rules: list[~azure.mgmt.search.models.IpRule]
    """

    _attribute_map = {
        'ip_rules': {'key': 'ipRules', 'type': '[IpRule]'},
    }

    def __init__(self, *, ip_rules=None, **kwargs) -> None:
        super(NetworkRuleSet, self).__init__(**kwargs)
        self.ip_rules = ip_rules


class Operation(Model):
    """Describes a REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation. This name is of the form
     {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: The object that describes the operation.
    :vartype display: ~azure.mgmt.search.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = None


class OperationDisplay(Model):
    """The object that describes the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: The friendly name of the resource provider.
    :vartype provider: str
    :ivar operation: The operation type: read, write, delete, listKeys/action,
     etc.
    :vartype operation: str
    :ivar resource: The resource type on which the operation is performed.
    :vartype resource: str
    :ivar description: The friendly name of the operation.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'operation': {'readonly': True},
        'resource': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.operation = None
        self.resource = None
        self.description = None


class PrivateEndpointConnection(Model):
    """Describes an existing Private Endpoint connection to the Azure Cognitive
    Search service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the private endpoint connection. This can be used with
     the Azure Resource Manager to link resources together.
    :vartype id: str
    :ivar name: The name of the private endpoint connection.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param properties: Describes the properties of an existing Private
     Endpoint connection to the Azure Cognitive Search service.
    :type properties:
     ~azure.mgmt.search.models.PrivateEndpointConnectionProperties
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
        'properties': {'key': 'properties', 'type': 'PrivateEndpointConnectionProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(PrivateEndpointConnection, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties


class PrivateEndpointConnectionProperties(Model):
    """Describes the properties of an existing Private Endpoint connection to the
    Azure Cognitive Search service.

    :param private_endpoint: The private endpoint resource from
     Microsoft.Network provider.
    :type private_endpoint:
     ~azure.mgmt.search.models.PrivateEndpointConnectionPropertiesPrivateEndpoint
    :param private_link_service_connection_state: Describes the current state
     of an existing Private Link Service connection to the Azure Private
     Endpoint.
    :type private_link_service_connection_state:
     ~azure.mgmt.search.models.PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionState
    """

    _attribute_map = {
        'private_endpoint': {'key': 'privateEndpoint', 'type': 'PrivateEndpointConnectionPropertiesPrivateEndpoint'},
        'private_link_service_connection_state': {'key': 'privateLinkServiceConnectionState', 'type': 'PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionState'},
    }

    def __init__(self, *, private_endpoint=None, private_link_service_connection_state=None, **kwargs) -> None:
        super(PrivateEndpointConnectionProperties, self).__init__(**kwargs)
        self.private_endpoint = private_endpoint
        self.private_link_service_connection_state = private_link_service_connection_state


class PrivateEndpointConnectionPropertiesPrivateEndpoint(Model):
    """The private endpoint resource from Microsoft.Network provider.

    :param id: The resource id of the private endpoint resource from
     Microsoft.Network provider.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(PrivateEndpointConnectionPropertiesPrivateEndpoint, self).__init__(**kwargs)
        self.id = id


class PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionState(Model):
    """Describes the current state of an existing Private Link Service connection
    to the Azure Private Endpoint.

    :param status: Status of the the private link service connection. Can be
     Pending, Approved, Rejected, or Disconnected. Possible values include:
     'Pending', 'Approved', 'Rejected', 'Disconnected'
    :type status: str or
     ~azure.mgmt.search.models.PrivateLinkServiceConnectionStatus
    :param description: The description for the private link service
     connection state.
    :type description: str
    :param actions_required: A description of any extra actions that may be
     required. Default value: "None" .
    :type actions_required: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'PrivateLinkServiceConnectionStatus'},
        'description': {'key': 'description', 'type': 'str'},
        'actions_required': {'key': 'actionsRequired', 'type': 'str'},
    }

    def __init__(self, *, status=None, description: str=None, actions_required: str="None", **kwargs) -> None:
        super(PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionState, self).__init__(**kwargs)
        self.status = status
        self.description = description
        self.actions_required = actions_required


class PrivateLinkResource(Model):
    """Describes a supported private link resource for the Azure Cognitive Search
    service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the private link resource.
    :vartype id: str
    :ivar name: The name of the private link resource.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar properties: Describes the properties of a supported private link
     resource for the Azure Cognitive Search service.
    :vartype properties:
     ~azure.mgmt.search.models.PrivateLinkResourceProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'PrivateLinkResourceProperties'},
    }

    def __init__(self, **kwargs) -> None:
        super(PrivateLinkResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = None


class PrivateLinkResourceProperties(Model):
    """Describes the properties of a supported private link resource for the Azure
    Cognitive Search service. For a given API version, this represents the
    'supported' groupIds when creating a shared private link resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar group_id: The group ID of the private link resource.
    :vartype group_id: str
    :ivar required_members: The list of required members of the private link
     resource.
    :vartype required_members: list[str]
    :ivar required_zone_names: The list of required DNS zone names of the
     private link resource.
    :vartype required_zone_names: list[str]
    :ivar shareable_private_link_resource_types: The list of resources that
     are onboarded to private link service, that are supported by Azure
     Cognitive Search.
    :vartype shareable_private_link_resource_types:
     list[~azure.mgmt.search.models.ShareablePrivateLinkResourceType]
    """

    _validation = {
        'group_id': {'readonly': True},
        'required_members': {'readonly': True},
        'required_zone_names': {'readonly': True},
        'shareable_private_link_resource_types': {'readonly': True},
    }

    _attribute_map = {
        'group_id': {'key': 'groupId', 'type': 'str'},
        'required_members': {'key': 'requiredMembers', 'type': '[str]'},
        'required_zone_names': {'key': 'requiredZoneNames', 'type': '[str]'},
        'shareable_private_link_resource_types': {'key': 'shareablePrivateLinkResourceTypes', 'type': '[ShareablePrivateLinkResourceType]'},
    }

    def __init__(self, **kwargs) -> None:
        super(PrivateLinkResourceProperties, self).__init__(**kwargs)
        self.group_id = None
        self.required_members = None
        self.required_zone_names = None
        self.shareable_private_link_resource_types = None


class QueryKey(Model):
    """Describes an API key for a given Azure Cognitive Search service that has
    permissions for query operations only.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the query API key; may be empty.
    :vartype name: str
    :ivar key: The value of the query API key.
    :vartype key: str
    """

    _validation = {
        'name': {'readonly': True},
        'key': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(QueryKey, self).__init__(**kwargs)
        self.name = None
        self.key = None


class Resource(Model):
    """Base type for all Azure resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource. This can be used with the Azure Resource
     Manager to link resources together.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: The geographic location of the resource. This must be one
     of the supported and registered Azure Geo Regions (for example, West US,
     East US, Southeast Asia, and so forth). This property is required when
     creating a new resource.
    :type location: str
    :param tags: Tags to help categorize the resource in the Azure portal.
    :type tags: dict[str, str]
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.search.models.Identity
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
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, *, location: str=None, tags=None, identity=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
        self.identity = identity


class SearchManagementRequestOptions(Model):
    """Additional parameters for a set of operations.

    :param client_request_id: A client-generated GUID value that identifies
     this request. If specified, this will be included in response information
     as a way to track the request.
    :type client_request_id: str
    """

    _attribute_map = {
        'client_request_id': {'key': '', 'type': 'str'},
    }

    def __init__(self, *, client_request_id: str=None, **kwargs) -> None:
        super(SearchManagementRequestOptions, self).__init__(**kwargs)
        self.client_request_id = client_request_id


class SearchService(Resource):
    """Describes an Azure Cognitive Search service and its current state.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource. This can be used with the Azure Resource
     Manager to link resources together.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :param location: The geographic location of the resource. This must be one
     of the supported and registered Azure Geo Regions (for example, West US,
     East US, Southeast Asia, and so forth). This property is required when
     creating a new resource.
    :type location: str
    :param tags: Tags to help categorize the resource in the Azure portal.
    :type tags: dict[str, str]
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.search.models.Identity
    :param replica_count: The number of replicas in the Search service. If
     specified, it must be a value between 1 and 12 inclusive for standard SKUs
     or between 1 and 3 inclusive for basic SKU. Default value: 1 .
    :type replica_count: int
    :param partition_count: The number of partitions in the Search service; if
     specified, it can be 1, 2, 3, 4, 6, or 12. Values greater than 1 are only
     valid for standard SKUs. For 'standard3' services with hostingMode set to
     'highDensity', the allowed values are between 1 and 3. Default value: 1 .
    :type partition_count: int
    :param hosting_mode: Applicable only for the standard3 SKU. You can set
     this property to enable up to 3 high density partitions that allow up to
     1000 indexes, which is much higher than the maximum indexes allowed for
     any other SKU. For the standard3 SKU, the value is either 'default' or
     'highDensity'. For all other SKUs, this value must be 'default'. Possible
     values include: 'default', 'highDensity'. Default value: "default" .
    :type hosting_mode: str or ~azure.mgmt.search.models.HostingMode
    :param public_network_access: This value can be set to 'enabled' to avoid
     breaking changes on existing customer resources and templates. If set to
     'disabled', traffic over public interface is not allowed, and private
     endpoint connections would be the exclusive access method. Possible values
     include: 'enabled', 'disabled'. Default value: "enabled" .
    :type public_network_access: str or
     ~azure.mgmt.search.models.PublicNetworkAccess
    :ivar status: The status of the Search service. Possible values include:
     'running': The Search service is running and no provisioning operations
     are underway. 'provisioning': The Search service is being provisioned or
     scaled up or down. 'deleting': The Search service is being deleted.
     'degraded': The Search service is degraded. This can occur when the
     underlying search units are not healthy. The Search service is most likely
     operational, but performance might be slow and some requests might be
     dropped. 'disabled': The Search service is disabled. In this state, the
     service will reject all API requests. 'error': The Search service is in an
     error state. If your service is in the degraded, disabled, or error
     states, it means the Azure Cognitive Search team is actively investigating
     the underlying issue. Dedicated services in these states are still
     chargeable based on the number of search units provisioned. Possible
     values include: 'running', 'provisioning', 'deleting', 'degraded',
     'disabled', 'error'
    :vartype status: str or ~azure.mgmt.search.models.SearchServiceStatus
    :ivar status_details: The details of the Search service status.
    :vartype status_details: str
    :ivar provisioning_state: The state of the last provisioning operation
     performed on the Search service. Provisioning is an intermediate state
     that occurs while service capacity is being established. After capacity is
     set up, provisioningState changes to either 'succeeded' or 'failed'.
     Client applications can poll provisioning status (the recommended polling
     interval is from 30 seconds to one minute) by using the Get Search Service
     operation to see when an operation is completed. If you are using the free
     service, this value tends to come back as 'succeeded' directly in the call
     to Create Search service. This is because the free service uses capacity
     that is already set up. Possible values include: 'succeeded',
     'provisioning', 'failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.search.models.ProvisioningState
    :param network_rule_set: Network specific rules that determine how the
     Azure Cognitive Search service may be reached.
    :type network_rule_set: ~azure.mgmt.search.models.NetworkRuleSet
    :ivar private_endpoint_connections: The list of private endpoint
     connections to the Azure Cognitive Search service.
    :vartype private_endpoint_connections:
     list[~azure.mgmt.search.models.PrivateEndpointConnection]
    :ivar shared_private_link_resources: The list of shared private link
     resources managed by the Azure Cognitive Search service.
    :vartype shared_private_link_resources:
     list[~azure.mgmt.search.models.SharedPrivateLinkResource]
    :param sku: The SKU of the Search Service, which determines price tier and
     capacity limits. This property is required when creating a new Search
     Service.
    :type sku: ~azure.mgmt.search.models.Sku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'replica_count': {'maximum': 12, 'minimum': 1},
        'partition_count': {'maximum': 12, 'minimum': 1},
        'status': {'readonly': True},
        'status_details': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'private_endpoint_connections': {'readonly': True},
        'shared_private_link_resources': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'replica_count': {'key': 'properties.replicaCount', 'type': 'int'},
        'partition_count': {'key': 'properties.partitionCount', 'type': 'int'},
        'hosting_mode': {'key': 'properties.hostingMode', 'type': 'HostingMode'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'PublicNetworkAccess'},
        'status': {'key': 'properties.status', 'type': 'SearchServiceStatus'},
        'status_details': {'key': 'properties.statusDetails', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'network_rule_set': {'key': 'properties.networkRuleSet', 'type': 'NetworkRuleSet'},
        'private_endpoint_connections': {'key': 'properties.privateEndpointConnections', 'type': '[PrivateEndpointConnection]'},
        'shared_private_link_resources': {'key': 'properties.sharedPrivateLinkResources', 'type': '[SharedPrivateLinkResource]'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, *, location: str=None, tags=None, identity=None, replica_count: int=1, partition_count: int=1, hosting_mode="default", public_network_access="enabled", network_rule_set=None, sku=None, **kwargs) -> None:
        super(SearchService, self).__init__(location=location, tags=tags, identity=identity, **kwargs)
        self.replica_count = replica_count
        self.partition_count = partition_count
        self.hosting_mode = hosting_mode
        self.public_network_access = public_network_access
        self.status = None
        self.status_details = None
        self.provisioning_state = None
        self.network_rule_set = network_rule_set
        self.private_endpoint_connections = None
        self.shared_private_link_resources = None
        self.sku = sku


class ShareablePrivateLinkResourceProperties(Model):
    """Describes the properties of a resource type that has been onboarded to
    private link service, supported by Azure Cognitive Search.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The resource provider type for the resource that has been
     onboarded to private link service, supported by Azure Cognitive Search.
    :vartype type: str
    :ivar group_id: The resource provider group id for the resource that has
     been onboarded to private link service, supported by Azure Cognitive
     Search.
    :vartype group_id: str
    :ivar description: The description of the resource type that has been
     onboarded to private link service, supported by Azure Cognitive Search.
    :vartype description: str
    """

    _validation = {
        'type': {'readonly': True},
        'group_id': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ShareablePrivateLinkResourceProperties, self).__init__(**kwargs)
        self.type = None
        self.group_id = None
        self.description = None


class ShareablePrivateLinkResourceType(Model):
    """Describes an resource type that has been onboarded to private link service,
    supported by Azure Cognitive Search.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource type that has been onboarded to
     private link service, supported by Azure Cognitive Search.
    :vartype name: str
    :ivar properties: Describes the properties of a resource type that has
     been onboarded to private link service, supported by Azure Cognitive
     Search.
    :vartype properties:
     ~azure.mgmt.search.models.ShareablePrivateLinkResourceProperties
    """

    _validation = {
        'name': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ShareablePrivateLinkResourceProperties'},
    }

    def __init__(self, **kwargs) -> None:
        super(ShareablePrivateLinkResourceType, self).__init__(**kwargs)
        self.name = None
        self.properties = None


class SharedPrivateLinkResource(Model):
    """Describes a Shared Private Link Resource managed by the Azure Cognitive
    Search service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the shared private link resource.
    :vartype name: str
    :ivar id: The ID of the shared private link resource.
    :vartype id: str
    :ivar type: The resource type.
    :vartype type: str
    :param properties: Describes the properties of a Shared Private Link
     Resource managed by the Azure Cognitive Search service.
    :type properties:
     ~azure.mgmt.search.models.SharedPrivateLinkResourceProperties
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'SharedPrivateLinkResourceProperties'},
    }

    def __init__(self, *, properties=None, **kwargs) -> None:
        super(SharedPrivateLinkResource, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None
        self.properties = properties


class SharedPrivateLinkResourceProperties(Model):
    """Describes the properties of an existing Shared Private Link Resource
    managed by the Azure Cognitive Search service.

    :param private_link_resource_id: The resource id of the resource the
     shared private link resource is for.
    :type private_link_resource_id: str
    :param group_id: The group id from the provider of resource the shared
     private link resource is for.
    :type group_id: str
    :param request_message: The request message for requesting approval of the
     shared private link resource.
    :type request_message: str
    :param status: Status of the shared private link resource. Can be Pending,
     Approved, Rejected, Disconnected, or Timeout. Possible values include:
     'Pending', 'Approved', 'Rejected', 'Disconnected', 'Timeout'
    :type status: str or
     ~azure.mgmt.search.models.SharedPrivateLinkResourceStatus
    """

    _attribute_map = {
        'private_link_resource_id': {'key': 'privateLinkResourceId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'request_message': {'key': 'requestMessage', 'type': 'str'},
        'status': {'key': 'status', 'type': 'SharedPrivateLinkResourceStatus'},
    }

    def __init__(self, *, private_link_resource_id: str=None, group_id: str=None, request_message: str=None, status=None, **kwargs) -> None:
        super(SharedPrivateLinkResourceProperties, self).__init__(**kwargs)
        self.private_link_resource_id = private_link_resource_id
        self.group_id = group_id
        self.request_message = request_message
        self.status = status


class Sku(Model):
    """Defines the SKU of an Azure Cognitive Search Service, which determines
    price tier and capacity limits.

    :param name: The SKU of the Search service. Valid values include: 'free':
     Shared service. 'basic': Dedicated service with up to 3 replicas.
     'standard': Dedicated service with up to 12 partitions and 12 replicas.
     'standard2': Similar to standard, but with more capacity per search unit.
     'standard3': The largest Standard offering with up to 12 partitions and 12
     replicas (or up to 3 partitions with more indexes if you also set the
     hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports
     1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports
     2TB per partition, up to 12 partitions.'. Possible values include: 'free',
     'basic', 'standard', 'standard2', 'standard3', 'storage_optimized_l1',
     'storage_optimized_l2'
    :type name: str or ~azure.mgmt.search.models.SkuName
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'SkuName'},
    }

    def __init__(self, *, name=None, **kwargs) -> None:
        super(Sku, self).__init__(**kwargs)
        self.name = name
