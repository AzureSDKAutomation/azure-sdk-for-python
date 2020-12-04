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
    :ivar api_version: The API version to use for this operation. Constant value: "2020-09-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-09-01"

        self.config = config

    def get(
            self, resource_group_name, storage_sync_service_name, private_endpoint_connection_name, custom_headers=None, raw=False, **operation_config):
        """Gets the specified private endpoint connection associated with the
        storage sync service.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param storage_sync_service_name: The name of the storage sync service
         name within the specified resource group.
        :type storage_sync_service_name: str
        :param private_endpoint_connection_name: The name of the private
         endpoint connection associated with the Azure resource
        :type private_endpoint_connection_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PrivateEndpointConnection or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.storagesync.models.PrivateEndpointConnection or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`StorageSyncErrorException<azure.mgmt.storagesync.models.StorageSyncErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'storageSyncServiceName': self._serialize.url("storage_sync_service_name", storage_sync_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

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
            raise models.StorageSyncErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/privateEndpointConnections/{privateEndpointConnectionName}'}


    def _create_initial(
            self, resource_group_name, storage_sync_service_name, private_endpoint_connection_name, properties, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'storageSyncServiceName': self._serialize.url("storage_sync_service_name", storage_sync_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

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
        body_content = self._serialize.body(properties, 'PrivateEndpointConnection')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.StorageSyncErrorException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('PrivateEndpointConnection', response)
            header_dict = {
                'Azure-AsyncOperation': 'str',
                'Location': 'str',
                'Retry-After': 'str',
                'x-ms-request-id': 'str',
                'x-ms-correlation-request-id': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized

    def create(
            self, resource_group_name, storage_sync_service_name, private_endpoint_connection_name, properties, custom_headers=None, raw=False, polling=True, **operation_config):
        """Update the state of specified private endpoint connection associated
        with the storage sync service.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param storage_sync_service_name: The name of the storage sync service
         name within the specified resource group.
        :type storage_sync_service_name: str
        :param private_endpoint_connection_name: The name of the private
         endpoint connection associated with the Azure resource
        :type private_endpoint_connection_name: str
        :param properties: The private endpoint connection properties.
        :type properties:
         ~azure.mgmt.storagesync.models.PrivateEndpointConnection
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns
         PrivateEndpointConnection or
         ClientRawResponse<PrivateEndpointConnection> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.storagesync.models.PrivateEndpointConnection]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.storagesync.models.PrivateEndpointConnection]]
        :raises:
         :class:`StorageSyncErrorException<azure.mgmt.storagesync.models.StorageSyncErrorException>`
        """
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            storage_sync_service_name=storage_sync_service_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            properties=properties,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            header_dict = {
                'Azure-AsyncOperation': 'str',
                'Location': 'str',
                'Retry-After': 'str',
                'x-ms-request-id': 'str',
                'x-ms-correlation-request-id': 'str',
            }
            deserialized = self._deserialize('PrivateEndpointConnection', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                client_raw_response.add_headers(header_dict)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/privateEndpointConnections/{privateEndpointConnectionName}'}


    def _delete_initial(
            self, resource_group_name, storage_sync_service_name, private_endpoint_connection_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'storageSyncServiceName': self._serialize.url("storage_sync_service_name", storage_sync_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
            'privateEndpointConnectionName': self._serialize.url("private_endpoint_connection_name", private_endpoint_connection_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

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
            raise models.StorageSyncErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            header_dict = {
                'Azure-AsyncOperation': 'str',
                'Location': 'str',
                'Retry-After': 'str',
                'x-ms-request-id': 'str',
                'x-ms-correlation-request-id': 'str',
            }
            client_raw_response.add_headers(header_dict)
            return client_raw_response

    def delete(
            self, resource_group_name, storage_sync_service_name, private_endpoint_connection_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes the specified private endpoint connection associated with the
        storage sync service.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param storage_sync_service_name: The name of the storage sync service
         name within the specified resource group.
        :type storage_sync_service_name: str
        :param private_endpoint_connection_name: The name of the private
         endpoint connection associated with the Azure resource
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
         :class:`StorageSyncErrorException<azure.mgmt.storagesync.models.StorageSyncErrorException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            storage_sync_service_name=storage_sync_service_name,
            private_endpoint_connection_name=private_endpoint_connection_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                client_raw_response.add_headers({
                    'Azure-AsyncOperation': 'str',
                    'Location': 'str',
                    'Retry-After': 'str',
                    'x-ms-request-id': 'str',
                    'x-ms-correlation-request-id': 'str',
                })
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/privateEndpointConnections/{privateEndpointConnectionName}'}

    def list_by_storage_sync_service(
            self, resource_group_name, storage_sync_service_name, custom_headers=None, raw=False, **operation_config):
        """Get a PrivateEndpointConnection List.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param storage_sync_service_name: Name of Storage Sync Service
         resource.
        :type storage_sync_service_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PrivateEndpointConnection
        :rtype:
         ~azure.mgmt.storagesync.models.PrivateEndpointConnectionPaged[~azure.mgmt.storagesync.models.PrivateEndpointConnection]
        :raises:
         :class:`StorageSyncErrorException<azure.mgmt.storagesync.models.StorageSyncErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_storage_sync_service.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'storageSyncServiceName': self._serialize.url("storage_sync_service_name", storage_sync_service_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

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
                raise models.StorageSyncErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PrivateEndpointConnectionPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_storage_sync_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/privateEndpointConnections'}
