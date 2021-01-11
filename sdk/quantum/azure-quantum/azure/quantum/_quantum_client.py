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

from ._configuration import QuantumClientConfiguration
from .operations import JobsOperations
from .operations import ProvidersOperations
from .operations import StorageOperations
from .operations import QuotasOperations
from . import models


class QuantumClient(SDKClient):
    """Azure Quantum REST API client

    :ivar config: Configuration for client.
    :vartype config: QuantumClientConfiguration

    :ivar jobs: Jobs operations
    :vartype jobs: azure.quantum.operations.JobsOperations
    :ivar providers: Providers operations
    :vartype providers: azure.quantum.operations.ProvidersOperations
    :ivar storage: Storage operations
    :vartype storage: azure.quantum.operations.StorageOperations
    :ivar quotas: Quotas operations
    :vartype quotas: azure.quantum.operations.QuotasOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID. This is a
     GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param workspace_name: Name of the workspace.
    :type workspace_name: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, resource_group_name, workspace_name, base_url=None):

        self.config = QuantumClientConfiguration(credentials, subscription_id, resource_group_name, workspace_name, base_url)
        super(QuantumClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-11-04-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.providers = ProvidersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage = StorageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.quotas = QuotasOperations(
            self._client, self.config, self._serialize, self._deserialize)
