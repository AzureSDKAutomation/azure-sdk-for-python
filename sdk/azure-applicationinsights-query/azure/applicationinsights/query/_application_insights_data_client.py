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

from ._configuration import ApplicationInsightsDataClientConfiguration
from .operations import MetricsOperations
from .operations import EventsOperations
from .operations import QueryOperations
from .operations import MetadataOperations
from . import models


class ApplicationInsightsDataClient(SDKClient):
    """Composite Swagger for Application Insights Data Client

    :ivar config: Configuration for client.
    :vartype config: ApplicationInsightsDataClientConfiguration

    :ivar metrics: Metrics operations
    :vartype metrics: azure.applicationinsights.query.operations.MetricsOperations
    :ivar events: Events operations
    :vartype events: azure.applicationinsights.query.operations.EventsOperations
    :ivar query: Query operations
    :vartype query: azure.applicationinsights.query.operations.QueryOperations
    :ivar metadata: Metadata operations
    :vartype metadata: azure.applicationinsights.query.operations.MetadataOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = ApplicationInsightsDataClientConfiguration(credentials, base_url)
        super(ApplicationInsightsDataClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = 'v1'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.metrics = MetricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.events = EventsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.metadata = MetadataOperations(
            self._client, self.config, self._serialize, self._deserialize)
