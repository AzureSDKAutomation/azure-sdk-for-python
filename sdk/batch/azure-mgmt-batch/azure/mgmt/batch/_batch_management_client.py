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

from ._configuration import BatchManagementClientConfiguration
from .operations import BatchAccountOperations
from .operations import ApplicationPackageOperations
from .operations import ApplicationOperations
from .operations import LocationOperations
from .operations import Operations
from .operations import CertificateOperations
from .operations import PrivateLinkResourceOperations
from .operations import PrivateEndpointConnectionOperations
from .operations import PoolOperations
from . import models


class BatchManagementClient(SDKClient):
    """BatchManagementClient

    :ivar config: Configuration for client.
    :vartype config: BatchManagementClientConfiguration

    :ivar batch_account: BatchAccount operations
    :vartype batch_account: azure.mgmt.batch.operations.BatchAccountOperations
    :ivar application_package: ApplicationPackage operations
    :vartype application_package: azure.mgmt.batch.operations.ApplicationPackageOperations
    :ivar application: Application operations
    :vartype application: azure.mgmt.batch.operations.ApplicationOperations
    :ivar location: Location operations
    :vartype location: azure.mgmt.batch.operations.LocationOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.batch.operations.Operations
    :ivar certificate: Certificate operations
    :vartype certificate: azure.mgmt.batch.operations.CertificateOperations
    :ivar private_link_resource: PrivateLinkResource operations
    :vartype private_link_resource: azure.mgmt.batch.operations.PrivateLinkResourceOperations
    :ivar private_endpoint_connection: PrivateEndpointConnection operations
    :vartype private_endpoint_connection: azure.mgmt.batch.operations.PrivateEndpointConnectionOperations
    :ivar pool: Pool operations
    :vartype pool: azure.mgmt.batch.operations.PoolOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Azure subscription ID. This is a
     GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = BatchManagementClientConfiguration(credentials, subscription_id, base_url)
        super(BatchManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2021-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.batch_account = BatchAccountOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.application_package = ApplicationPackageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.application = ApplicationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.location = LocationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resource = PrivateLinkResourceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pool = PoolOperations(
            self._client, self.config, self._serialize, self._deserialize)
