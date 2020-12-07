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


class AcsClusterProperties(Model):
    """Information about the container service backing the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar cluster_fqdn: The FQDN of the cluster.
    :vartype cluster_fqdn: str
    :param orchestrator_type: Required. Type of orchestrator. It cannot be
     changed once the cluster is created. Possible values include:
     'Kubernetes', 'None'
    :type orchestrator_type: str or
     ~azure.mgmt.machinelearningcompute.models.OrchestratorType
    :param orchestrator_properties: Orchestrator specific properties
    :type orchestrator_properties:
     ~azure.mgmt.machinelearningcompute.models.KubernetesClusterProperties
    :param system_services: The system services deployed to the cluster
    :type system_services:
     list[~azure.mgmt.machinelearningcompute.models.SystemService]
    :param master_count: The number of master nodes in the container service.
     Default value: 1 .
    :type master_count: int
    :param agent_count: The number of agent nodes in the Container Service.
     This can be changed to scale the cluster. Default value: 2 .
    :type agent_count: int
    :param agent_vm_size: The Azure VM size of the agent VM nodes. This cannot
     be changed once the cluster is created. This list is non exhaustive; refer
     to https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
     for the possible VM sizes. Possible values include: 'Standard_A0',
     'Standard_A1', 'Standard_A2', 'Standard_A3', 'Standard_A4', 'Standard_A5',
     'Standard_A6', 'Standard_A7', 'Standard_A8', 'Standard_A9',
     'Standard_A10', 'Standard_A11', 'Standard_D1', 'Standard_D2',
     'Standard_D3', 'Standard_D4', 'Standard_D11', 'Standard_D12',
     'Standard_D13', 'Standard_D14', 'Standard_D1_v2', 'Standard_D2_v2',
     'Standard_D3_v2', 'Standard_D4_v2', 'Standard_D5_v2', 'Standard_D11_v2',
     'Standard_D12_v2', 'Standard_D13_v2', 'Standard_D14_v2', 'Standard_G1',
     'Standard_G2', 'Standard_G3', 'Standard_G4', 'Standard_G5',
     'Standard_DS1', 'Standard_DS2', 'Standard_DS3', 'Standard_DS4',
     'Standard_DS11', 'Standard_DS12', 'Standard_DS13', 'Standard_DS14',
     'Standard_GS1', 'Standard_GS2', 'Standard_GS3', 'Standard_GS4',
     'Standard_GS5'. Default value: "Standard_D3_v2" .
    :type agent_vm_size: str or
     ~azure.mgmt.machinelearningcompute.models.AgentVMSizeTypes
    """

    _validation = {
        'cluster_fqdn': {'readonly': True},
        'orchestrator_type': {'required': True},
        'master_count': {'maximum': 5, 'minimum': 1},
        'agent_count': {'maximum': 100, 'minimum': 1},
    }

    _attribute_map = {
        'cluster_fqdn': {'key': 'clusterFqdn', 'type': 'str'},
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'str'},
        'orchestrator_properties': {'key': 'orchestratorProperties', 'type': 'KubernetesClusterProperties'},
        'system_services': {'key': 'systemServices', 'type': '[SystemService]'},
        'master_count': {'key': 'masterCount', 'type': 'int'},
        'agent_count': {'key': 'agentCount', 'type': 'int'},
        'agent_vm_size': {'key': 'agentVmSize', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AcsClusterProperties, self).__init__(**kwargs)
        self.cluster_fqdn = None
        self.orchestrator_type = kwargs.get('orchestrator_type', None)
        self.orchestrator_properties = kwargs.get('orchestrator_properties', None)
        self.system_services = kwargs.get('system_services', None)
        self.master_count = kwargs.get('master_count', 1)
        self.agent_count = kwargs.get('agent_count', 2)
        self.agent_vm_size = kwargs.get('agent_vm_size', "Standard_D3_v2")


class AppInsightsCredentials(Model):
    """AppInsights credentials.

    :param app_id: The AppInsights application ID.
    :type app_id: str
    :param instrumentation_key: The AppInsights instrumentation key. This is
     not returned in response of GET/PUT on the resource. To see this please
     call listKeys API.
    :type instrumentation_key: str
    """

    _attribute_map = {
        'app_id': {'key': 'appId', 'type': 'str'},
        'instrumentation_key': {'key': 'instrumentationKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AppInsightsCredentials, self).__init__(**kwargs)
        self.app_id = kwargs.get('app_id', None)
        self.instrumentation_key = kwargs.get('instrumentation_key', None)


class AppInsightsProperties(Model):
    """Properties of App Insights.

    :param resource_id: ARM resource ID of the App Insights.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AppInsightsProperties, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)


class AutoScaleConfiguration(Model):
    """AutoScale configuration properties.

    :param status: If auto-scale is enabled for all services. Each service can
     turn it off individually. Possible values include: 'Enabled', 'Disabled'.
     Default value: "Disabled" .
    :type status: str or ~azure.mgmt.machinelearningcompute.models.Status
    :param min_replicas: The minimum number of replicas for each service.
     Default value: 1 .
    :type min_replicas: int
    :param max_replicas: The maximum number of replicas for each service.
     Default value: 100 .
    :type max_replicas: int
    :param target_utilization: The target utilization.
    :type target_utilization: float
    :param refresh_period_in_seconds: Refresh period in seconds.
    :type refresh_period_in_seconds: int
    """

    _validation = {
        'min_replicas': {'minimum': 1},
        'max_replicas': {'minimum': 1},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'min_replicas': {'key': 'minReplicas', 'type': 'int'},
        'max_replicas': {'key': 'maxReplicas', 'type': 'int'},
        'target_utilization': {'key': 'targetUtilization', 'type': 'float'},
        'refresh_period_in_seconds': {'key': 'refreshPeriodInSeconds', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AutoScaleConfiguration, self).__init__(**kwargs)
        self.status = kwargs.get('status', "Disabled")
        self.min_replicas = kwargs.get('min_replicas', 1)
        self.max_replicas = kwargs.get('max_replicas', 100)
        self.target_utilization = kwargs.get('target_utilization', None)
        self.refresh_period_in_seconds = kwargs.get('refresh_period_in_seconds', None)


class AvailableOperations(Model):
    """Available operation list.

    :param value: An array of available operations.
    :type value:
     list[~azure.mgmt.machinelearningcompute.models.ResourceOperation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceOperation]'},
    }

    def __init__(self, **kwargs):
        super(AvailableOperations, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class CheckSystemServicesUpdatesAvailableResponse(Model):
    """Information about updates available for system services in a cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar updates_available: Yes if updates are available for the system
     services, No if not. Possible values include: 'Yes', 'No'
    :vartype updates_available: str or
     ~azure.mgmt.machinelearningcompute.models.UpdatesAvailable
    """

    _validation = {
        'updates_available': {'readonly': True},
    }

    _attribute_map = {
        'updates_available': {'key': 'updatesAvailable', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckSystemServicesUpdatesAvailableResponse, self).__init__(**kwargs)
        self.updates_available = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ContainerRegistryCredentials(Model):
    """Information about the Azure Container Registry which contains the images
    deployed to the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar login_server: The ACR login server name. User name is the first part
     of the FQDN.
    :vartype login_server: str
    :ivar password: The ACR primary password.
    :vartype password: str
    :ivar password2: The ACR secondary password.
    :vartype password2: str
    :ivar username: The ACR login username.
    :vartype username: str
    """

    _validation = {
        'login_server': {'readonly': True},
        'password': {'readonly': True},
        'password2': {'readonly': True},
        'username': {'readonly': True},
    }

    _attribute_map = {
        'login_server': {'key': 'loginServer', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'password2': {'key': 'password2', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerRegistryCredentials, self).__init__(**kwargs)
        self.login_server = None
        self.password = None
        self.password2 = None
        self.username = None


class ContainerRegistryProperties(Model):
    """Properties of Azure Container Registry.

    :param resource_id: ARM resource ID of the Azure Container Registry used
     to store Docker images for web services in the cluster. If not provided
     one will be created. This cannot be changed once the cluster is created.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerRegistryProperties, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)


class ContainerServiceCredentials(Model):
    """Information about the Azure Container Registry which contains the images
    deployed to the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar acs_kube_config: The ACS kube config file.
    :vartype acs_kube_config: str
    :ivar service_principal_configuration: Service principal configuration
     used by Kubernetes.
    :vartype service_principal_configuration:
     ~azure.mgmt.machinelearningcompute.models.ServicePrincipalProperties
    :ivar image_pull_secret_name: The ACR image pull secret name which was
     created in Kubernetes.
    :vartype image_pull_secret_name: str
    """

    _validation = {
        'acs_kube_config': {'readonly': True},
        'service_principal_configuration': {'readonly': True},
        'image_pull_secret_name': {'readonly': True},
    }

    _attribute_map = {
        'acs_kube_config': {'key': 'acsKubeConfig', 'type': 'str'},
        'service_principal_configuration': {'key': 'servicePrincipalConfiguration', 'type': 'ServicePrincipalProperties'},
        'image_pull_secret_name': {'key': 'imagePullSecretName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceCredentials, self).__init__(**kwargs)
        self.acs_kube_config = None
        self.service_principal_configuration = None
        self.image_pull_secret_name = None


class ErrorDetail(Model):
    """Error detail information.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code.
    :type code: str
    :param message: Required. Error message.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ErrorResponse(Model):
    """Error response information.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code.
    :type code: str
    :param message: Required. Error message.
    :type message: str
    :param details: An array of error detail objects.
    :type details: list[~azure.mgmt.machinelearningcompute.models.ErrorDetail]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.details = kwargs.get('details', None)


class ErrorResponseWrapper(Model):
    """Wrapper for error response to follow ARM guidelines.

    :param error: The error response.
    :type error: ~azure.mgmt.machinelearningcompute.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponseWrapper, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseWrapperException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponseWrapper'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseWrapperException, self).__init__(deserialize, response, 'ErrorResponseWrapper', *args)


class GlobalServiceConfiguration(Model):
    """Global configuration for services in the cluster.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param etag: The configuration ETag for updates.
    :type etag: str
    :param ssl: The SSL configuration properties
    :type ssl: ~azure.mgmt.machinelearningcompute.models.SslConfiguration
    :param service_auth: Optional global authorization keys for all user
     services deployed in cluster. These are used if the service does not have
     auth keys.
    :type service_auth:
     ~azure.mgmt.machinelearningcompute.models.ServiceAuthConfiguration
    :param auto_scale: The auto-scale configuration
    :type auto_scale:
     ~azure.mgmt.machinelearningcompute.models.AutoScaleConfiguration
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'ssl': {'key': 'ssl', 'type': 'SslConfiguration'},
        'service_auth': {'key': 'serviceAuth', 'type': 'ServiceAuthConfiguration'},
        'auto_scale': {'key': 'autoScale', 'type': 'AutoScaleConfiguration'},
    }

    def __init__(self, **kwargs):
        super(GlobalServiceConfiguration, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.etag = kwargs.get('etag', None)
        self.ssl = kwargs.get('ssl', None)
        self.service_auth = kwargs.get('service_auth', None)
        self.auto_scale = kwargs.get('auto_scale', None)


class KubernetesClusterProperties(Model):
    """Kubernetes cluster specific properties.

    :param service_principal: The Azure Service Principal used by Kubernetes
    :type service_principal:
     ~azure.mgmt.machinelearningcompute.models.ServicePrincipalProperties
    """

    _attribute_map = {
        'service_principal': {'key': 'servicePrincipal', 'type': 'ServicePrincipalProperties'},
    }

    def __init__(self, **kwargs):
        super(KubernetesClusterProperties, self).__init__(**kwargs)
        self.service_principal = kwargs.get('service_principal', None)


class Resource(Model):
    """Azure resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Specifies the resource ID.
    :vartype id: str
    :ivar name: Specifies the name of the resource.
    :vartype name: str
    :param location: Required. Specifies the location of the resource.
    :type location: str
    :ivar type: Specifies the type of the resource.
    :vartype type: str
    :param tags: Contains resource tags defined as key/value pairs.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.location = kwargs.get('location', None)
        self.type = None
        self.tags = kwargs.get('tags', None)


class OperationalizationCluster(Resource):
    """Instance of an Azure ML Operationalization Cluster resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Specifies the resource ID.
    :vartype id: str
    :ivar name: Specifies the name of the resource.
    :vartype name: str
    :param location: Required. Specifies the location of the resource.
    :type location: str
    :ivar type: Specifies the type of the resource.
    :vartype type: str
    :param tags: Contains resource tags defined as key/value pairs.
    :type tags: dict[str, str]
    :param description: The description of the cluster.
    :type description: str
    :ivar created_on: The date and time when the cluster was created.
    :vartype created_on: datetime
    :ivar modified_on: The date and time when the cluster was last modified.
    :vartype modified_on: datetime
    :ivar provisioning_state: The provision state of the cluster. Valid values
     are Unknown, Updating, Provisioning, Succeeded, and Failed. Possible
     values include: 'Unknown', 'Updating', 'Creating', 'Deleting',
     'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.machinelearningcompute.models.OperationStatus
    :ivar provisioning_errors: List of provisioning errors reported by the
     resource provider.
    :vartype provisioning_errors:
     list[~azure.mgmt.machinelearningcompute.models.ErrorResponseWrapper]
    :param cluster_type: Required. The cluster type. Possible values include:
     'ACS', 'Local'
    :type cluster_type: str or
     ~azure.mgmt.machinelearningcompute.models.ClusterType
    :param storage_account: Storage Account properties.
    :type storage_account:
     ~azure.mgmt.machinelearningcompute.models.StorageAccountProperties
    :param container_registry: Container Registry properties.
    :type container_registry:
     ~azure.mgmt.machinelearningcompute.models.ContainerRegistryProperties
    :param container_service: Parameters for the Azure Container Service
     cluster.
    :type container_service:
     ~azure.mgmt.machinelearningcompute.models.AcsClusterProperties
    :param app_insights: AppInsights configuration.
    :type app_insights:
     ~azure.mgmt.machinelearningcompute.models.AppInsightsProperties
    :param global_service_configuration: Contains global configuration for the
     web services in the cluster.
    :type global_service_configuration:
     ~azure.mgmt.machinelearningcompute.models.GlobalServiceConfiguration
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
        'created_on': {'readonly': True},
        'modified_on': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'provisioning_errors': {'readonly': True},
        'cluster_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'created_on': {'key': 'properties.createdOn', 'type': 'iso-8601'},
        'modified_on': {'key': 'properties.modifiedOn', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_errors': {'key': 'properties.provisioningErrors', 'type': '[ErrorResponseWrapper]'},
        'cluster_type': {'key': 'properties.clusterType', 'type': 'str'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountProperties'},
        'container_registry': {'key': 'properties.containerRegistry', 'type': 'ContainerRegistryProperties'},
        'container_service': {'key': 'properties.containerService', 'type': 'AcsClusterProperties'},
        'app_insights': {'key': 'properties.appInsights', 'type': 'AppInsightsProperties'},
        'global_service_configuration': {'key': 'properties.globalServiceConfiguration', 'type': 'GlobalServiceConfiguration'},
    }

    def __init__(self, **kwargs):
        super(OperationalizationCluster, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.created_on = None
        self.modified_on = None
        self.provisioning_state = None
        self.provisioning_errors = None
        self.cluster_type = kwargs.get('cluster_type', None)
        self.storage_account = kwargs.get('storage_account', None)
        self.container_registry = kwargs.get('container_registry', None)
        self.container_service = kwargs.get('container_service', None)
        self.app_insights = kwargs.get('app_insights', None)
        self.global_service_configuration = kwargs.get('global_service_configuration', None)


class OperationalizationClusterCredentials(Model):
    """Credentials to resources in the cluster.

    :param storage_account: Credentials for the Storage Account.
    :type storage_account:
     ~azure.mgmt.machinelearningcompute.models.StorageAccountCredentials
    :param container_registry: Credentials for Azure Container Registry.
    :type container_registry:
     ~azure.mgmt.machinelearningcompute.models.ContainerRegistryCredentials
    :param container_service: Credentials for Azure Container Service.
    :type container_service:
     ~azure.mgmt.machinelearningcompute.models.ContainerServiceCredentials
    :param app_insights: Credentials for Azure AppInsights.
    :type app_insights:
     ~azure.mgmt.machinelearningcompute.models.AppInsightsCredentials
    :param service_auth_configuration: Global authorization keys for all user
     services deployed in cluster. These are used if the service does not have
     auth keys.
    :type service_auth_configuration:
     ~azure.mgmt.machinelearningcompute.models.ServiceAuthConfiguration
    :param ssl_configuration: The SSL configuration for the services.
    :type ssl_configuration:
     ~azure.mgmt.machinelearningcompute.models.SslConfiguration
    """

    _attribute_map = {
        'storage_account': {'key': 'storageAccount', 'type': 'StorageAccountCredentials'},
        'container_registry': {'key': 'containerRegistry', 'type': 'ContainerRegistryCredentials'},
        'container_service': {'key': 'containerService', 'type': 'ContainerServiceCredentials'},
        'app_insights': {'key': 'appInsights', 'type': 'AppInsightsCredentials'},
        'service_auth_configuration': {'key': 'serviceAuthConfiguration', 'type': 'ServiceAuthConfiguration'},
        'ssl_configuration': {'key': 'sslConfiguration', 'type': 'SslConfiguration'},
    }

    def __init__(self, **kwargs):
        super(OperationalizationClusterCredentials, self).__init__(**kwargs)
        self.storage_account = kwargs.get('storage_account', None)
        self.container_registry = kwargs.get('container_registry', None)
        self.container_service = kwargs.get('container_service', None)
        self.app_insights = kwargs.get('app_insights', None)
        self.service_auth_configuration = kwargs.get('service_auth_configuration', None)
        self.ssl_configuration = kwargs.get('ssl_configuration', None)


class OperationalizationClusterUpdateParameters(Model):
    """Parameters for PATCH operation on an operationalization cluster.

    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used in viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key no greater in length than 128
     characters and a value no greater in length than 256 characters.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(OperationalizationClusterUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class ResourceOperation(Model):
    """Resource operation.

    :param name: Name of this operation.
    :type name: str
    :param display: Display of the operation.
    :type display:
     ~azure.mgmt.machinelearningcompute.models.ResourceOperationDisplay
    :param origin: The operation origin.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceOperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)


class ResourceOperationDisplay(Model):
    """Display of the operation.

    :param provider: The resource provider name.
    :type provider: str
    :param resource: The resource name.
    :type resource: str
    :param operation: The operation.
    :type operation: str
    :param description: The description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ServiceAuthConfiguration(Model):
    """Global service auth configuration properties. These are the data-plane
    authorization keys and are used if a service doesn't define it's own.

    All required parameters must be populated in order to send to Azure.

    :param primary_auth_key_hash: Required. The primary auth key hash. This is
     not returned in response of GET/PUT on the resource.. To see this please
     call listKeys API.
    :type primary_auth_key_hash: str
    :param secondary_auth_key_hash: Required. The secondary auth key hash.
     This is not returned in response of GET/PUT on the resource.. To see this
     please call listKeys API.
    :type secondary_auth_key_hash: str
    """

    _validation = {
        'primary_auth_key_hash': {'required': True},
        'secondary_auth_key_hash': {'required': True},
    }

    _attribute_map = {
        'primary_auth_key_hash': {'key': 'primaryAuthKeyHash', 'type': 'str'},
        'secondary_auth_key_hash': {'key': 'secondaryAuthKeyHash', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceAuthConfiguration, self).__init__(**kwargs)
        self.primary_auth_key_hash = kwargs.get('primary_auth_key_hash', None)
        self.secondary_auth_key_hash = kwargs.get('secondary_auth_key_hash', None)


class ServicePrincipalProperties(Model):
    """The Azure service principal used by Kubernetes for configuring load
    balancers.

    All required parameters must be populated in order to send to Azure.

    :param client_id: Required. The service principal client ID
    :type client_id: str
    :param secret: Required. The service principal secret. This is not
     returned in response of GET/PUT on the resource. To see this please call
     listKeys.
    :type secret: str
    """

    _validation = {
        'client_id': {'required': True},
        'secret': {'required': True},
    }

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServicePrincipalProperties, self).__init__(**kwargs)
        self.client_id = kwargs.get('client_id', None)
        self.secret = kwargs.get('secret', None)


class SslConfiguration(Model):
    """SSL configuration. If configured data-plane calls to user services will be
    exposed over SSL only.

    :param status: SSL status. Allowed values are Enabled and Disabled.
     Possible values include: 'Enabled', 'Disabled'. Default value: "Enabled" .
    :type status: str or ~azure.mgmt.machinelearningcompute.models.Status
    :param cert: The SSL cert data in PEM format.
    :type cert: str
    :param key: The SSL key data in PEM format. This is not returned in
     response of GET/PUT on the resource. To see this please call listKeys API.
    :type key: str
    :param cname: The CName of the certificate.
    :type cname: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'cert': {'key': 'cert', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'cname': {'key': 'cname', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SslConfiguration, self).__init__(**kwargs)
        self.status = kwargs.get('status', "Enabled")
        self.cert = kwargs.get('cert', None)
        self.key = kwargs.get('key', None)
        self.cname = kwargs.get('cname', None)


class StorageAccountCredentials(Model):
    """Access information for the storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar resource_id: The ARM resource ID of the storage account.
    :vartype resource_id: str
    :ivar primary_key: The primary key of the storage account.
    :vartype primary_key: str
    :ivar secondary_key: The secondary key of the storage account.
    :vartype secondary_key: str
    """

    _validation = {
        'resource_id': {'readonly': True},
        'primary_key': {'readonly': True},
        'secondary_key': {'readonly': True},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageAccountCredentials, self).__init__(**kwargs)
        self.resource_id = None
        self.primary_key = None
        self.secondary_key = None


class StorageAccountProperties(Model):
    """Properties of Storage Account.

    :param resource_id: ARM resource ID of the Azure Storage Account to store
     CLI specific files. If not provided one will be created. This cannot be
     changed once the cluster is created.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageAccountProperties, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)


class SystemService(Model):
    """Information about a system service deployed in the cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param system_service_type: Required. The system service type. Possible
     values include: 'None', 'ScoringFrontEnd', 'BatchFrontEnd'
    :type system_service_type: str or
     ~azure.mgmt.machinelearningcompute.models.SystemServiceType
    :ivar public_ip_address: The public IP address of the system service
    :vartype public_ip_address: str
    :ivar version: The state of the system service
    :vartype version: str
    """

    _validation = {
        'system_service_type': {'required': True},
        'public_ip_address': {'readonly': True},
        'version': {'readonly': True},
    }

    _attribute_map = {
        'system_service_type': {'key': 'systemServiceType', 'type': 'str'},
        'public_ip_address': {'key': 'publicIpAddress', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SystemService, self).__init__(**kwargs)
        self.system_service_type = kwargs.get('system_service_type', None)
        self.public_ip_address = None
        self.version = None


class UpdateSystemServicesResponse(Model):
    """Response of the update system services API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar update_status: Update status. Possible values include: 'Unknown',
     'Updating', 'Creating', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype update_status: str or
     ~azure.mgmt.machinelearningcompute.models.OperationStatus
    :ivar update_started_on: The date and time when the last system services
     update was started.
    :vartype update_started_on: datetime
    :ivar update_completed_on: The date and time when the last system services
     update completed.
    :vartype update_completed_on: datetime
    """

    _validation = {
        'update_status': {'readonly': True},
        'update_started_on': {'readonly': True},
        'update_completed_on': {'readonly': True},
    }

    _attribute_map = {
        'update_status': {'key': 'updateStatus', 'type': 'str'},
        'update_started_on': {'key': 'updateStartedOn', 'type': 'iso-8601'},
        'update_completed_on': {'key': 'updateCompletedOn', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(UpdateSystemServicesResponse, self).__init__(**kwargs)
        self.update_status = None
        self.update_started_on = None
        self.update_completed_on = None
