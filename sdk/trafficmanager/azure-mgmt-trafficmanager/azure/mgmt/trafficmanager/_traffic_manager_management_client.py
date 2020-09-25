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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import TrafficManagerManagementClientConfiguration
from .operations import EndpointsOperations
from .operations import ProfilesOperations
from .operations import GeographicHierarchiesOperations
from .operations import HeatMapOperations
from .operations import TrafficManagerUserMetricsKeysOperations
from . import models


class TrafficManagerManagementClient(SDKClient):
    """TrafficManagerManagementClient

    :ivar config: Configuration for client.
    :vartype config: TrafficManagerManagementClientConfiguration

    :ivar endpoints: Endpoints operations
    :vartype endpoints: azure.mgmt.trafficmanager.operations.EndpointsOperations
    :ivar profiles: Profiles operations
    :vartype profiles: azure.mgmt.trafficmanager.operations.ProfilesOperations
    :ivar geographic_hierarchies: GeographicHierarchies operations
    :vartype geographic_hierarchies: azure.mgmt.trafficmanager.operations.GeographicHierarchiesOperations
    :ivar heat_map: HeatMap operations
    :vartype heat_map: azure.mgmt.trafficmanager.operations.HeatMapOperations
    :ivar traffic_manager_user_metrics_keys: TrafficManagerUserMetricsKeys operations
    :vartype traffic_manager_user_metrics_keys: azure.mgmt.trafficmanager.operations.TrafficManagerUserMetricsKeysOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = TrafficManagerManagementClientConfiguration(credentials, subscription_id, base_url)
        super(TrafficManagerManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.endpoints = EndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.profiles = ProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.geographic_hierarchies = GeographicHierarchiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.heat_map = HeatMapOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.traffic_manager_user_metrics_keys = TrafficManagerUserMetricsKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)