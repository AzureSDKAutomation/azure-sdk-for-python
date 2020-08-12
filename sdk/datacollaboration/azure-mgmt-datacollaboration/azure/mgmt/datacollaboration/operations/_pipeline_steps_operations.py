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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class PipelineStepsOperations(object):
    """PipelineStepsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The api version to use. Constant value: "2020-05-04-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-05-04-preview"

        self.config = config

    def list_by_pipeline(
            self, resource_group_name, workspace_name, pipeline_name, skip_token=None, custom_headers=None, raw=False, **operation_config):
        """List PipelineSteps of a Pipeline.

        List PipelineSteps of a Pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param pipeline_name: The name of the pipeline.
        :type pipeline_name: str
        :param skip_token: continuation token
        :type skip_token: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PipelineStep
        :rtype:
         ~azure.mgmt.datacollaboration.models.PipelineStepPaged[~azure.mgmt.datacollaboration.models.PipelineStep]
        :raises:
         :class:`DataCollaborationErrorException<azure.mgmt.datacollaboration.models.DataCollaborationErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_pipeline.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
                    'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.DataCollaborationErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PipelineStepPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_pipeline.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataCollaboration/workspaces/{workspaceName}/pipelines/{pipelineName}/pipelineSteps'}

    def get(
            self, resource_group_name, workspace_name, pipeline_name, pipeline_step_name, custom_headers=None, raw=False, **operation_config):
        """Get a PipelineStep in a Pipeline.

        Get a PipelineStep in a Pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param pipeline_name: The name of the pipeline.
        :type pipeline_name: str
        :param pipeline_step_name: The name of the pipeline step.
        :type pipeline_step_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PipelineStep or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.datacollaboration.models.PipelineStep or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`DataCollaborationErrorException<azure.mgmt.datacollaboration.models.DataCollaborationErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
            'pipelineStepName': self._serialize.url("pipeline_step_name", pipeline_step_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.DataCollaborationErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PipelineStep', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataCollaboration/workspaces/{workspaceName}/pipelines/{pipelineName}/pipelineSteps/{pipelineStepName}'}

    def create_or_update(
            self, resource_group_name, workspace_name, pipeline_name, pipeline_step_name, pipeline_step, custom_headers=None, raw=False, **operation_config):
        """Adds a new PipelineStep to an existing Pipeline.

        Create or update a PipelineStep.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param pipeline_name: The name of the pipeline.
        :type pipeline_name: str
        :param pipeline_step_name: The name of the pipeline step.
        :type pipeline_step_name: str
        :param pipeline_step: The new pipeline information.
        :type pipeline_step: ~azure.mgmt.datacollaboration.models.PipelineStep
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PipelineStep or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.datacollaboration.models.PipelineStep or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`DataCollaborationErrorException<azure.mgmt.datacollaboration.models.DataCollaborationErrorException>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
            'pipelineStepName': self._serialize.url("pipeline_step_name", pipeline_step_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(pipeline_step, 'PipelineStep')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.DataCollaborationErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PipelineStep', response)
        if response.status_code == 201:
            deserialized = self._deserialize('PipelineStep', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataCollaboration/workspaces/{workspaceName}/pipelines/{pipelineName}/pipelineSteps/{pipelineStepName}'}


    def _delete_initial(
            self, resource_group_name, workspace_name, pipeline_name, pipeline_step_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
            'pipelineStepName': self._serialize.url("pipeline_step_name", pipeline_step_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            raise models.DataCollaborationErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, resource_group_name, workspace_name, pipeline_name, pipeline_step_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Delete a PipelineStep in a Pipeline.

        Delete a PipelineStep in a Pipeline.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param pipeline_name: The name of the pipeline.
        :type pipeline_name: str
        :param pipeline_step_name: The name of the pipeline step.
        :type pipeline_step_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns OperationResponse or
         ClientRawResponse<OperationResponse> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.datacollaboration.models.OperationResponse]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.datacollaboration.models.OperationResponse]]
        :raises:
         :class:`DataCollaborationErrorException<azure.mgmt.datacollaboration.models.DataCollaborationErrorException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            pipeline_name=pipeline_name,
            pipeline_step_name=pipeline_step_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('OperationResponse', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataCollaboration/workspaces/{workspaceName}/pipelines/{pipelineName}/pipelineSteps/{pipelineStepName}'}
