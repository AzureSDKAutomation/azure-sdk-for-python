# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
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

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
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

    def __init__(
        self,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs['location']


class Account(TrackedResource):
    """An ADP account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.adp.v2020_07_01_preview.models.SystemData
    :ivar account_id: The account's data-plane ID.
    :vartype account_id: str
    :ivar provisioning_state: Gets the status of the account at the time the operation was called.
     Possible values include: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning",
     "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.adp.v2020_07_01_preview.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'account_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Account, self).__init__(**kwargs)
        self.system_data = None
        self.account_id = None
        self.provisioning_state = None


class AccountList(msrest.serialization.Model):
    """The list operation response, that contains the data pools and their properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of accounts and their properties.
    :vartype value: list[~azure.mgmt.adp.v2020_07_01_preview.models.Account]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Account]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountList, self).__init__(**kwargs)
        self.value = None
        self.next_link = kwargs.get('next_link', None)


class Tags(msrest.serialization.Model):
    """Resource tags.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Tags, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class AccountPatch(Tags):
    """An ADP account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar account_id: The account's data-plane ID.
    :vartype account_id: str
    :ivar provisioning_state: Gets the status of the account at the time the operation was called.
     Possible values include: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning",
     "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.adp.v2020_07_01_preview.models.ProvisioningState
    """

    _validation = {
        'account_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'account_id': {'key': 'properties.accountId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccountPatch, self).__init__(**kwargs)
        self.account_id = None
        self.provisioning_state = None


class DataPool(Resource):
    """An ADP Data Pool.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar data_pool_id: The Data Pool's data-plane ID.
    :vartype data_pool_id: str
    :ivar provisioning_state: Gets the status of the data pool at the time the operation was
     called. Possible values include: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning",
     "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.adp.v2020_07_01_preview.models.ProvisioningState
    :param locations: Gets or sets the collection of locations where Data Pool resources should be
     created.
    :type locations: list[~azure.mgmt.adp.v2020_07_01_preview.models.DataPoolLocation]
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.adp.v2020_07_01_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'data_pool_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'locations': {'min_items': 1},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'data_pool_id': {'key': 'properties.dataPoolId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'locations': {'key': 'properties.locations', 'type': '[DataPoolLocation]'},
        'system_data': {'key': 'properties.systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataPool, self).__init__(**kwargs)
        self.data_pool_id = None
        self.provisioning_state = None
        self.locations = kwargs.get('locations', None)
        self.system_data = None


class DataPoolBaseProperties(msrest.serialization.Model):
    """Data Pool properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar data_pool_id: The Data Pool's data-plane ID.
    :vartype data_pool_id: str
    :ivar provisioning_state: Gets the status of the data pool at the time the operation was
     called. Possible values include: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning",
     "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.adp.v2020_07_01_preview.models.ProvisioningState
    :param locations: Gets or sets the collection of locations where Data Pool resources should be
     created.
    :type locations: list[~azure.mgmt.adp.v2020_07_01_preview.models.DataPoolLocation]
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.adp.v2020_07_01_preview.models.SystemData
    """

    _validation = {
        'data_pool_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'locations': {'min_items': 1},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'data_pool_id': {'key': 'dataPoolId', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[DataPoolLocation]'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataPoolBaseProperties, self).__init__(**kwargs)
        self.data_pool_id = None
        self.provisioning_state = None
        self.locations = kwargs.get('locations', None)
        self.system_data = None


class DataPoolList(msrest.serialization.Model):
    """The list operation response, that contains the data pools and their properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of data pools and their properties.
    :vartype value: list[~azure.mgmt.adp.v2020_07_01_preview.models.DataPool]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DataPool]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataPoolList, self).__init__(**kwargs)
        self.value = None
        self.next_link = kwargs.get('next_link', None)


class DataPoolLocation(msrest.serialization.Model):
    """Location of a Data Pool.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The location name.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataPoolLocation, self).__init__(**kwargs)
        self.name = kwargs['name']


class DataPoolPatch(Resource):
    """An ADP Data Pool.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar data_pool_id: The Data Pool's data-plane ID.
    :vartype data_pool_id: str
    :ivar provisioning_state: Gets the status of the data pool at the time the operation was
     called. Possible values include: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning",
     "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.adp.v2020_07_01_preview.models.ProvisioningState
    :param locations: Gets or sets the collection of locations where Data Pool resources should be
     created.
    :type locations: list[~azure.mgmt.adp.v2020_07_01_preview.models.DataPoolLocation]
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.adp.v2020_07_01_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'data_pool_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'locations': {'min_items': 1},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'data_pool_id': {'key': 'properties.dataPoolId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'locations': {'key': 'properties.locations', 'type': '[DataPoolLocation]'},
        'system_data': {'key': 'properties.systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataPoolPatch, self).__init__(**kwargs)
        self.data_pool_id = None
        self.provisioning_state = None
        self.locations = kwargs.get('locations', None)
        self.system_data = None


class DataPoolProperties(DataPoolBaseProperties):
    """Data Pool properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar data_pool_id: The Data Pool's data-plane ID.
    :vartype data_pool_id: str
    :ivar provisioning_state: Gets the status of the data pool at the time the operation was
     called. Possible values include: "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning",
     "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.adp.v2020_07_01_preview.models.ProvisioningState
    :param locations: Gets or sets the collection of locations where Data Pool resources should be
     created.
    :type locations: list[~azure.mgmt.adp.v2020_07_01_preview.models.DataPoolLocation]
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.adp.v2020_07_01_preview.models.SystemData
    """

    _validation = {
        'data_pool_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'locations': {'min_items': 1},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'data_pool_id': {'key': 'dataPoolId', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'locations': {'key': 'locations', 'type': '[DataPoolLocation]'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataPoolProperties, self).__init__(**kwargs)


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~azure.mgmt.adp.v2020_07_01_preview.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: The error details.
    :type error: ~azure.mgmt.adp.v2020_07_01_preview.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Operation(msrest.serialization.Model):
    """Operation detail payload.

    :param name: Name of the operation.
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    :param action_type: Indicates the action type.
    :type action_type: str
    :param display: Display of the operation.
    :type display: ~azure.mgmt.adp.v2020_07_01_preview.models.OperationDisplay
    :param origin: Origin of the operation.
    :type origin: str
    :param service_specification: Details about a service operation.
    :type service_specification:
     ~azure.mgmt.adp.v2020_07_01_preview.models.OperationServiceSpecification
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'action_type': {'key': 'actionType', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'OperationServiceSpecification'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.action_type = kwargs.get('action_type', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)
        self.service_specification = kwargs.get('service_specification', None)


class OperationDisplay(msrest.serialization.Model):
    """Operation display payload.

    :param provider: Resource provider of the operation.
    :type provider: str
    :param resource: Resource of the operation.
    :type resource: str
    :param operation: Localized friendly name for the operation.
    :type operation: str
    :param description: Localized friendly description for the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationListResult(msrest.serialization.Model):
    """Available operations of the service.

    :param value: List of operations supported by the Resource Provider.
    :type value: list[~azure.mgmt.adp.v2020_07_01_preview.models.Operation]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class OperationLogSpecification(msrest.serialization.Model):
    """Details about an operation related to logs.

    :param name: The name of the log category.
    :type name: str
    :param display_name: Localized display name.
    :type display_name: str
    :param blob_duration: Blobs created in the customer storage account, per hour.
    :type blob_duration: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'blob_duration': {'key': 'blobDuration', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationLogSpecification, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.blob_duration = kwargs.get('blob_duration', None)


class OperationMetricAvailability(msrest.serialization.Model):
    """Defines how often data for a metric becomes available.

    :param time_grain: The granularity for the metric.
    :type time_grain: str
    :param blob_duration: Blob created in the customer storage account, per hour.
    :type blob_duration: str
    """

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'str'},
        'blob_duration': {'key': 'blobDuration', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationMetricAvailability, self).__init__(**kwargs)
        self.time_grain = kwargs.get('time_grain', None)
        self.blob_duration = kwargs.get('blob_duration', None)


class OperationMetricSpecification(msrest.serialization.Model):
    """Details about an operation related to metrics.

    :param name: The name of the metric.
    :type name: str
    :param display_name: Localized display name of the metric.
    :type display_name: str
    :param display_description: The description of the metric.
    :type display_description: str
    :param unit: The unit that the metric is measured in.
    :type unit: str
    :param aggregation_type: The type of metric aggregation.
    :type aggregation_type: str
    :param enable_regional_mdm_account: Whether or not the service is using regional MDM accounts.
    :type enable_regional_mdm_account: str
    :param source_mdm_account: The name of the MDM account.
    :type source_mdm_account: str
    :param source_mdm_namespace: The name of the MDM namespace.
    :type source_mdm_namespace: str
    :param availabilities: Defines how often data for metrics becomes available.
    :type availabilities:
     list[~azure.mgmt.adp.v2020_07_01_preview.models.OperationMetricAvailability]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'display_description': {'key': 'displayDescription', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'aggregation_type': {'key': 'aggregationType', 'type': 'str'},
        'enable_regional_mdm_account': {'key': 'enableRegionalMdmAccount', 'type': 'str'},
        'source_mdm_account': {'key': 'sourceMdmAccount', 'type': 'str'},
        'source_mdm_namespace': {'key': 'sourceMdmNamespace', 'type': 'str'},
        'availabilities': {'key': 'availabilities', 'type': '[OperationMetricAvailability]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationMetricSpecification, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.display_description = kwargs.get('display_description', None)
        self.unit = kwargs.get('unit', None)
        self.aggregation_type = kwargs.get('aggregation_type', None)
        self.enable_regional_mdm_account = kwargs.get('enable_regional_mdm_account', None)
        self.source_mdm_account = kwargs.get('source_mdm_account', None)
        self.source_mdm_namespace = kwargs.get('source_mdm_namespace', None)
        self.availabilities = kwargs.get('availabilities', None)


class OperationServiceSpecification(msrest.serialization.Model):
    """Details about a service operation.

    :param log_specifications: Details about operations related to logs.
    :type log_specifications:
     list[~azure.mgmt.adp.v2020_07_01_preview.models.OperationLogSpecification]
    :param metric_specifications: Details about operations related to metrics.
    :type metric_specifications:
     list[~azure.mgmt.adp.v2020_07_01_preview.models.OperationMetricSpecification]
    """

    _attribute_map = {
        'log_specifications': {'key': 'logSpecifications', 'type': '[OperationLogSpecification]'},
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[OperationMetricSpecification]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationServiceSpecification, self).__init__(**kwargs)
        self.log_specifications = kwargs.get('log_specifications', None)
        self.metric_specifications = kwargs.get('metric_specifications', None)


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~azure.mgmt.adp.v2020_07_01_preview.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or ~azure.mgmt.adp.v2020_07_01_preview.models.CreatedByType
    :param last_modified_at: The type of identity that last modified the resource.
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)
