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

from .. import models


class DatastoresOperations(object):
    """DatastoresOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of Azure Machine Learning resource provider API. Constant value: "2020-12-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-12-01-preview"

        self.config = config

    def list(
            self, resource_group_name, workspace_name, skiptoken=None, count=30, is_default=None, names=None, search_text=None, order_by=None, order_by_asc=False, custom_headers=None, raw=False, **operation_config):
        """List datastores.

        :param resource_group_name: Name of the resource group in which
         workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param skiptoken: Continuation token for pagination.
        :type skiptoken: str
        :param count: Maximum number of results to return.
        :type count: int
        :param is_default: Filter down to the workspace default datastore.
        :type is_default: bool
        :param names: Names of datastores to return.
        :type names: list[str]
        :param search_text: Text to search for in the datastore names.
        :type search_text: str
        :param order_by: Order by property (createdtime | modifiedtime |
         name).
        :type order_by: str
        :param order_by_asc: Order by property in ascending order.
        :type order_by_asc: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DatastorePropertiesResource
        :rtype:
         ~azure.mgmt.machinelearningservices.models.DatastorePropertiesResourcePaged[~azure.mgmt.machinelearningservices.models.DatastorePropertiesResource]
        :raises:
         :class:`MachineLearningServiceErrorException<azure.mgmt.machinelearningservices.models.MachineLearningServiceErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if skiptoken is not None:
                    query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')
                if count is not None:
                    query_parameters['count'] = self._serialize.query("count", count, 'int')
                if is_default is not None:
                    query_parameters['isDefault'] = self._serialize.query("is_default", is_default, 'bool')
                if names is not None:
                    query_parameters['names'] = self._serialize.query("names", names, '[str]', div=',')
                if search_text is not None:
                    query_parameters['searchText'] = self._serialize.query("search_text", search_text, 'str')
                if order_by is not None:
                    query_parameters['orderBy'] = self._serialize.query("order_by", order_by, 'str')
                if order_by_asc is not None:
                    query_parameters['orderByAsc'] = self._serialize.query("order_by_asc", order_by_asc, 'bool')

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
                raise models.MachineLearningServiceErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.DatastorePropertiesResourcePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datastores'}

    def delete(
            self, name, resource_group_name, workspace_name, custom_headers=None, raw=False, **operation_config):
        """Delete datastore.

        :param name: Datastore name.
        :type name: str
        :param resource_group_name: Name of the resource group in which
         workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MachineLearningServiceErrorException<azure.mgmt.machinelearningservices.models.MachineLearningServiceErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str')
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

        if response.status_code not in [200, 204]:
            raise models.MachineLearningServiceErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datastores/{name}'}

    def get(
            self, name, resource_group_name, workspace_name, custom_headers=None, raw=False, **operation_config):
        """Get datastore.

        :param name: Datastore name.
        :type name: str
        :param resource_group_name: Name of the resource group in which
         workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DatastorePropertiesResource or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.machinelearningservices.models.DatastorePropertiesResource
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MachineLearningServiceErrorException<azure.mgmt.machinelearningservices.models.MachineLearningServiceErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str')
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
            raise models.MachineLearningServiceErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DatastorePropertiesResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datastores/{name}'}

    def create_or_update(
            self, name, resource_group_name, workspace_name, properties, system_data=None, custom_headers=None, raw=False, **operation_config):
        """Create or update datastore.

        :param name: Datastore name.
        :type name: str
        :param resource_group_name: Name of the resource group in which
         workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param properties:
        :type properties:
         ~azure.mgmt.machinelearningservices.models.DatastoreProperties
        :param system_data:
        :type system_data:
         ~azure.mgmt.machinelearningservices.models.SystemData
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DatastorePropertiesResource or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.machinelearningservices.models.DatastorePropertiesResource
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MachineLearningServiceErrorException<azure.mgmt.machinelearningservices.models.MachineLearningServiceErrorException>`
        """
        body = models.DatastorePropertiesResource(properties=properties, system_data=system_data)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str')
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
        body_content = self._serialize.body(body, 'DatastorePropertiesResource')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.MachineLearningServiceErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DatastorePropertiesResource', response)
        if response.status_code == 201:
            deserialized = self._deserialize('DatastorePropertiesResource', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datastores/{name}'}

    def list_secrets(
            self, name, resource_group_name, workspace_name, custom_headers=None, raw=False, **operation_config):
        """Get datastore secrets.

        :param name: Datastore name.
        :type name: str
        :param resource_group_name: Name of the resource group in which
         workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DatastoreCredentials or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.machinelearningservices.models.DatastoreCredentials or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MachineLearningServiceErrorException<azure.mgmt.machinelearningservices.models.MachineLearningServiceErrorException>`
        """
        # Construct URL
        url = self.list_secrets.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str')
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
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.MachineLearningServiceErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DatastoreCredentials', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_secrets.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/datastores/{name}/listSecrets'}
