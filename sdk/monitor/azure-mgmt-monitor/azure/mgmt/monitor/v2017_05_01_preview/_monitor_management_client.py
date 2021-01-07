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

from ._configuration import MonitorManagementClientConfiguration
from .operations import DiagnosticSettingsCategoryOperations
from .operations import DiagnosticSettingsOperations
from .operations import MetricDefinitionsOperations
from .operations import MetricsOperations
from .operations import SubscriptionDiagnosticSettingsOperations
from . import models


class MonitorManagementClient(SDKClient):
    """Monitor Management Client

    :ivar config: Configuration for client.
    :vartype config: MonitorManagementClientConfiguration

    :ivar diagnostic_settings_category: DiagnosticSettingsCategory operations
    :vartype diagnostic_settings_category: azure.mgmt.monitor.v2017_05_01_preview.operations.DiagnosticSettingsCategoryOperations
    :ivar diagnostic_settings: DiagnosticSettings operations
    :vartype diagnostic_settings: azure.mgmt.monitor.v2017_05_01_preview.operations.DiagnosticSettingsOperations
    :ivar metric_definitions: MetricDefinitions operations
    :vartype metric_definitions: azure.mgmt.monitor.v2017_05_01_preview.operations.MetricDefinitionsOperations
    :ivar metrics: Metrics operations
    :vartype metrics: azure.mgmt.monitor.v2017_05_01_preview.operations.MetricsOperations
    :ivar subscription_diagnostic_settings: SubscriptionDiagnosticSettings operations
    :vartype subscription_diagnostic_settings: azure.mgmt.monitor.v2017_05_01_preview.operations.SubscriptionDiagnosticSettingsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MonitorManagementClientConfiguration(credentials, subscription_id, base_url)
        super(MonitorManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-05-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.diagnostic_settings_category = DiagnosticSettingsCategoryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.diagnostic_settings = DiagnosticSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metric_definitions = MetricDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metrics = MetricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscription_diagnostic_settings = SubscriptionDiagnosticSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
