# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AzureDigitalTwinsManagementClientConfiguration
from .operations import DigitalTwinsOperations
from .operations import DigitalTwinsEndpointOperations
from .operations import Operations
from .. import models


class AzureDigitalTwinsManagementClient(object):
    """Azure Digital Twins Client for managing DigitalTwinsInstance.

    :ivar digital_twins: DigitalTwinsOperations operations
    :vartype digital_twins: azure.mgmt.digitaltwins.aio.operations.DigitalTwinsOperations
    :ivar digital_twins_endpoint: DigitalTwinsEndpointOperations operations
    :vartype digital_twins_endpoint: azure.mgmt.digitaltwins.aio.operations.DigitalTwinsEndpointOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.digitaltwins.aio.operations.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureDigitalTwinsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.digital_twins = DigitalTwinsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.digital_twins_endpoint = DigitalTwinsEndpointOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureDigitalTwinsManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
