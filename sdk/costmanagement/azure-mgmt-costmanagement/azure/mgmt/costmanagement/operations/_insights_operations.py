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


class InsightsOperations(object):
    """InsightsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request (e.g. '2020-08-01-preview'). Constant value: "2020-08-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-08-01-preview"

        self.config = config

    def list_by_scope(
            self, scope, custom_headers=None, raw=False, **operation_config):
        """Lists all insights at the given scope.

        :param scope: The scope associated with insights operations. This
         includes '/subscriptions/{subscriptionId}/' for subscription scope. At
         present, only subscription scope is supported.
        :type scope: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Insights
        :rtype:
         ~azure.mgmt.costmanagement.models.InsightsPaged[~azure.mgmt.costmanagement.models.Insights]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.costmanagement.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_scope.metadata['url']
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
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
        deserialized = models.InsightsPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_scope.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/insights'}

    def get_by_scope(
            self, scope, insight_name, custom_headers=None, raw=False, **operation_config):
        """Gets the insight for the defined scope by insight name.

        :param scope: The scope associated with insights operations. This
         includes '/subscriptions/{subscriptionId}/' for subscription scope. At
         present, only subscription scope is supported.
        :type scope: str
        :param insight_name: Insights name
        :type insight_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Insights or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.costmanagement.models.Insights or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.costmanagement.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_scope.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'insightName': self._serialize.url("insight_name", insight_name, 'str')
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
            deserialized = self._deserialize('Insights', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_scope.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/insights/{insightName}'}
