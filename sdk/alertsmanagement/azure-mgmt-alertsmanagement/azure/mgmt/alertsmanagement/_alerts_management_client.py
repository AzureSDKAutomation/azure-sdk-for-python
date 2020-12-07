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

from ._configuration import AlertsManagementClientConfiguration
from .operations import ActionRulesOperations
from .operations import Operations
from .operations import AlertsOperations
from .operations import SmartGroupsOperations
from .operations import SmartDetectorAlertRulesOperations
from . import models


class AlertsManagementClient(SDKClient):
    """AlertsManagement Client

    :ivar config: Configuration for client.
    :vartype config: AlertsManagementClientConfiguration

    :ivar action_rules: ActionRules operations
    :vartype action_rules: azure.mgmt.alertsmanagement.operations.ActionRulesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.alertsmanagement.operations.Operations
    :ivar alerts: Alerts operations
    :vartype alerts: azure.mgmt.alertsmanagement.operations.AlertsOperations
    :ivar smart_groups: SmartGroups operations
    :vartype smart_groups: azure.mgmt.alertsmanagement.operations.SmartGroupsOperations
    :ivar smart_detector_alert_rules: SmartDetectorAlertRules operations
    :vartype smart_detector_alert_rules: azure.mgmt.alertsmanagement.operations.SmartDetectorAlertRulesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AlertsManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AlertsManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.action_rules = ActionRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.smart_groups = SmartGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.smart_detector_alert_rules = SmartDetectorAlertRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
