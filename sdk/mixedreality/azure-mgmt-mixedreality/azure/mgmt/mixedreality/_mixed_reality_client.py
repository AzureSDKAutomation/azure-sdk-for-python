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

from ._configuration import MixedRealityClientConfiguration
from .operations import MixedRealityClientOperationsMixin
from .operations import Operations
from .operations import SpatialAnchorsAccountsOperations
from .operations import RemoteRenderingAccountsOperations
from . import models


class MixedRealityClient(MixedRealityClientOperationsMixin, SDKClient):
    """Mixed Reality Client

    :ivar config: Configuration for client.
    :vartype config: MixedRealityClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.mixedreality.operations.Operations
    :ivar spatial_anchors_accounts: SpatialAnchorsAccounts operations
    :vartype spatial_anchors_accounts: azure.mgmt.mixedreality.operations.SpatialAnchorsAccountsOperations
    :ivar remote_rendering_accounts: RemoteRenderingAccounts operations
    :vartype remote_rendering_accounts: azure.mgmt.mixedreality.operations.RemoteRenderingAccountsOperations

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

        self.config = MixedRealityClientConfiguration(credentials, subscription_id, base_url)
        super(MixedRealityClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2021-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.spatial_anchors_accounts = SpatialAnchorsAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.remote_rendering_accounts = RemoteRenderingAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
