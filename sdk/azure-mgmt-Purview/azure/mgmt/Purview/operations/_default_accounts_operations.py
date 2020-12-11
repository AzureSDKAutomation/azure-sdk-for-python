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


class DefaultAccountsOperations(object):
    """DefaultAccountsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The api version to use. Constant value: "2020-12-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-12-01-preview"

        self.config = config

    def get(
            self, scope_tenant_id, scope_type, scope=None, custom_headers=None, raw=False, **operation_config):
        """Gets the default account information set for the scope.

        Get the default account for the scope.

        :param scope_tenant_id: The tenant ID.
        :type scope_tenant_id: str
        :param scope_type: The scope for the default account. Possible values
         include: 'Tenant', 'Subscription'
        :type scope_type: str or ~azure.mgmt.purview.models.ScopeType
        :param scope: The Id of the scope object, for example if the scope is
         "Subscription" then it is the ID of that subscription.
        :type scope: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DefaultAccountPayload or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.purview.models.DefaultAccountPayload or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseModelException<azure.mgmt.purview.models.ErrorResponseModelException>`
        """
        # Construct URL
        url = self.get.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['scopeTenantId'] = self._serialize.query("scope_tenant_id", scope_tenant_id, 'str')
        query_parameters['scopeType'] = self._serialize.query("scope_type", scope_type, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
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
            raise models.ErrorResponseModelException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DefaultAccountPayload', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Purview/getDefaultAccount'}

    def set(
            self, default_account_payload, custom_headers=None, raw=False, **operation_config):
        """Sets the default account for the scope.

        Sets the default account for the scope.

        :param default_account_payload: The payload containing the default
         account information and the scope.
        :type default_account_payload:
         ~azure.mgmt.purview.models.DefaultAccountPayload
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DefaultAccountPayload or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.purview.models.DefaultAccountPayload or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseModelException<azure.mgmt.purview.models.ErrorResponseModelException>`
        """
        # Construct URL
        url = self.set.metadata['url']

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
        body_content = self._serialize.body(default_account_payload, 'DefaultAccountPayload')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseModelException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DefaultAccountPayload', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set.metadata = {'url': '/providers/Microsoft.Purview/setDefaultAccount'}

    def remove(
            self, scope_tenant_id, scope_type, scope=None, custom_headers=None, raw=False, **operation_config):
        """Removes the default account from the scope.

        Removes the default account from the scope.

        :param scope_tenant_id: The tenant ID.
        :type scope_tenant_id: str
        :param scope_type: The scope for the default account. Possible values
         include: 'Tenant', 'Subscription'
        :type scope_type: str or ~azure.mgmt.purview.models.ScopeType
        :param scope: The Id of the scope object, for example if the scope is
         "Subscription" then it is the ID of that subscription.
        :type scope: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseModelException<azure.mgmt.purview.models.ErrorResponseModelException>`
        """
        # Construct URL
        url = self.remove.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['scopeTenantId'] = self._serialize.query("scope_tenant_id", scope_tenant_id, 'str')
        query_parameters['scopeType'] = self._serialize.query("scope_type", scope_type, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
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
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorResponseModelException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    remove.metadata = {'url': '/providers/Microsoft.Purview/removeDefaultAccount'}
