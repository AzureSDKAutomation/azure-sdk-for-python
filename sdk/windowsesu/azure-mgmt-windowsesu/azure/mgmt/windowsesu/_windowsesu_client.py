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

from ._configuration import windowsesuClientConfiguration
from .operations import Operations
from .operations import MultipleActivationKeysOperations
from . import models


class windowsesuClient(SDKClient):
    """Manage Multi-Access Keys (MAK) that enable Windows Extended Security Updates (ESU).

    :ivar config: Configuration for client.
    :vartype config: windowsesuClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.windowsesu.operations.Operations
    :ivar multiple_activation_keys: MultipleActivationKeys operations
    :vartype multiple_activation_keys: azure.mgmt.windowsesu.operations.MultipleActivationKeysOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = windowsesuClientConfiguration(credentials, subscription_id, base_url)
        super(windowsesuClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-09-16-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.multiple_activation_keys = MultipleActivationKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
