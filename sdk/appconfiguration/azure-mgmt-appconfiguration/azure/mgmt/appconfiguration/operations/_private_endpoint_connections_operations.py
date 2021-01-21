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


class PrivateEndpointConnectionsOperations(object):
    """PrivateEndpointConnectionsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The client API version. Constant value: "2020-07-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-07-01-preview"

        self.config = config

    def list_by_configuration_store(
            self, resource_group_name, config_store_name, custom_headers=None, raw=False, **operation_config):
        """Lists all private endpoint connections for a configuration store.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PrivateEndpointConnection
        :rtype:
         ~azure.mgmt.appconfiguration.models.PrivateEndpointConnectionPaged[~azure.mgmt.appconfiguration.models.PrivateEndpointConnection]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.appconfiguration.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_configuration_store.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PrivateEndpointConnectionPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_configuration_store.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections'}

    def get(
            self, resource_group_name, config_store_name, private_endpoint_connection_name, custom_headers=None, raw=False, **operation_config):
        """Gets the specified private endpoint connection associated with the
        configuration store.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param private_endpoint_connection_name: Private endpoint connection
         name
        :type private_endpoint_connection_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PrivateEndpointConnection or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.appconfiguration.models.PrivateEndpointConnection
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.appconfiguration.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
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
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}


    def _create_or_update_initial(
            self, resource_group_name, config_store_name, private_endpoint_connection_name, private_link_service_connection_state, private_endpoint=None, custom_headers=None, raw=False, **operation_config):
        private_endpoint_connection = models.PrivateEndpointConnection(private_endpoint=private_endpoint, private_link_service_connection_state=private_link_service_connection_state)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
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
        body_content = self._serialize.body(private_endpoint_connection, 'PrivateEndpointConnection')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', response)
        if response.status_code == 201:
            deserialized = self._deserialize('PrivateEndpointConnection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update(
            self, resource_group_name, config_store_name, private_endpoint_connection_name, private_link_service_connection_state, private_endpoint=None, custom_headers=None, raw=False, polling=True, **operation_config):
        """Update the state of the specified private endpoint connection
        associated with the configuration store.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param private_endpoint_connection_name: Private endpoint connection
         name
        :type private_endpoint_connection_name: str
        :param private_link_service_connection_state: A collection of
         information about the state of the connection between service consumer
         and provider.
        :type private_link_service_connection_state:
         ~azure.mgmt.appconfiguration.models.PrivateLinkServiceConnectionState
        :param private_endpoint: The resource of private endpoint.
        :type private_endpoint:
         ~azure.mgmt.appconfiguration.models.PrivateEndpoint
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns
         PrivateEndpointConnection or
         ClientRawResponse<PrivateEndpointConnection> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.appconfiguration.models.PrivateEndpointConnection]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.appconfiguration.models.PrivateEndpointConnection]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.appconfiguration.models.ErrorResponseException>`
        """
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            config_store_name=config_store_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            private_link_service_connection_state=private_link_service_connection_state,
            private_endpoint=private_endpoint,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('PrivateEndpointConnection', response)

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
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}


    def _delete_initial(
            self, resource_group_name, config_store_name, private_endpoint_connection_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'configStoreName': self._serialize.url("config_store_name", config_store_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9_-]*$'),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
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
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, resource_group_name, config_store_name, private_endpoint_connection_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes a private endpoint connection.

        :param resource_group_name: The name of the resource group to which
         the container registry belongs.
        :type resource_group_name: str
        :param config_store_name: The name of the configuration store.
        :type config_store_name: str
        :param private_endpoint_connection_name: Private endpoint connection
         name
        :type private_endpoint_connection_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.appconfiguration.models.ErrorResponseException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            config_store_name=config_store_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName}'}
