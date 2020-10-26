# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MonitorClientConfiguration
from .operations import PrivateLinkScopesOperations
from .operations import PrivateLinkScopeOperationStatusOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkScopedResourcesOperations
from . import models


class MonitorClient(object):
    """Monitor Management Client.

    :ivar private_link_scopes: PrivateLinkScopesOperations operations
    :vartype private_link_scopes: $(python-base-namespace).v2019_10_17.operations.PrivateLinkScopesOperations
    :ivar private_link_scope_operation_status: PrivateLinkScopeOperationStatusOperations operations
    :vartype private_link_scope_operation_status: $(python-base-namespace).v2019_10_17.operations.PrivateLinkScopeOperationStatusOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: $(python-base-namespace).v2019_10_17.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: $(python-base-namespace).v2019_10_17.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_scoped_resources: PrivateLinkScopedResourcesOperations operations
    :vartype private_link_scoped_resources: $(python-base-namespace).v2019_10_17.operations.PrivateLinkScopedResourcesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MonitorClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.private_link_scopes = PrivateLinkScopesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_scope_operation_status = PrivateLinkScopeOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_scoped_resources = PrivateLinkScopedResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MonitorClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
