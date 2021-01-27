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

from ._configuration import KeyVaultManagementClientConfiguration
from .operations import VaultsOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import Operations
from .operations import ManagedHsmsOperations
from . import models


class KeyVaultManagementClient(SDKClient):
    """The Azure management API provides a RESTful set of web services that interact with Azure Key Vault.

    :ivar config: Configuration for client.
    :vartype config: KeyVaultManagementClientConfiguration

    :ivar vaults: Vaults operations
    :vartype vaults: azure.mgmt.keyvault.v2020_04_01_preview.operations.VaultsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.keyvault.v2020_04_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.keyvault.v2020_04_01_preview.operations.PrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.keyvault.v2020_04_01_preview.operations.Operations
    :ivar managed_hsms: ManagedHsms operations
    :vartype managed_hsms: azure.mgmt.keyvault.v2020_04_01_preview.operations.ManagedHsmsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = KeyVaultManagementClientConfiguration(credentials, subscription_id, base_url)
        super(KeyVaultManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.vaults = VaultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.managed_hsms = ManagedHsmsOperations(
            self._client, self.config, self._serialize, self._deserialize)
