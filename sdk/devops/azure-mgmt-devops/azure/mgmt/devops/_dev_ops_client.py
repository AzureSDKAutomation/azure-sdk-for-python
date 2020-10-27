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

from ._configuration import DevOpsClientConfiguration
from .operations import Operations
from .operations import PipelineTemplateDefinitionsOperations
from .operations import PipelinesOperations
from . import models


class DevOpsClient(SDKClient):
    """Azure DevOps Resource Provider

    :ivar config: Configuration for client.
    :vartype config: DevOpsClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.devops.operations.Operations
    :ivar pipeline_template_definitions: PipelineTemplateDefinitions operations
    :vartype pipeline_template_definitions: azure.mgmt.devops.operations.PipelineTemplateDefinitionsOperations
    :ivar pipelines: Pipelines operations
    :vartype pipelines: azure.mgmt.devops.operations.PipelinesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Unique identifier of the Azure subscription. This
     is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DevOpsClientConfiguration(credentials, subscription_id, base_url)
        super(DevOpsClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-07-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pipeline_template_definitions = PipelineTemplateDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.pipelines = PipelinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
