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


class CalculateExchangeOperations(object):
    """CalculateExchangeOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Supported version for this document is 2020-10-01-preview. Constant value: "2020-10-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-10-01-preview"

        self.config = config


    def _post_initial(
            self, properties=None, custom_headers=None, raw=False, **operation_config):
        body = models.CalculateExchangeRequest(properties=properties)

        # Construct URL
        url = self.post.metadata['url']

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
        body_content = self._serialize.body(body, 'CalculateExchangeRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('CalculateExchangeOperationResultResponse', response)
            header_dict = {
                'Location': 'str',
                'Retry-After': 'int',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized

    def post(
            self, properties=None, custom_headers=None, raw=False, polling=True, **operation_config):
        """Calculates the refund amounts and price of the new purchases.

        Calculates price for exchanging `Reservations` if there are no policy
        errors.
        .

        :param properties:
        :type properties:
         ~azure.mgmt.reservations.models.CalculateExchangeRequestProperties
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns
         CalculateExchangeOperationResultResponse or
         ClientRawResponse<CalculateExchangeOperationResultResponse> if
         raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.reservations.models.CalculateExchangeOperationResultResponse]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.reservations.models.CalculateExchangeOperationResultResponse]]
        :raises:
         :class:`ErrorException<azure.mgmt.reservations.models.ErrorException>`
        """
        raw_result = self._post_initial(
            properties=properties,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            header_dict = {
                'Location': 'str',
                'Retry-After': 'int',
            }
            deserialized = self._deserialize('CalculateExchangeOperationResultResponse', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                client_raw_response.add_headers(header_dict)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    post.metadata = {'url': '/providers/Microsoft.Capacity/calculateExchange'}
