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

from msrest.pipeline import ClientRawResponse
from .. import models


class AnomalyDetectorClientOperationsMixin(object):

    def entire_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect anomalies for the entire series in batch.

        This operation generates a model using an entire series, each point is
        detected with the same model. With this method, points before and after
        a certain point are used to determine whether it is an anomaly. The
        entire detection can give user an overall status of the time series.

        :param body: Time series points and period if needed. Advanced model
         parameters can also be set in the request.
        :type body: ~azure.cognitiveservices.anomalydetector.models.Request
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EntireDetectResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.anomalydetector.models.EntireDetectResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.entire_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'Request')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('EntireDetectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    entire_detect.metadata = {'url': '/timeseries/entire/detect'}

    def last_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect anomaly status of the latest point in time series.

        This operation generates a model using points before the latest one.
        With this method, only historical points are used to determine whether
        the target point is an anomaly. The latest point detecting operation
        matches the scenario of real-time monitoring of business metrics.

        :param body: Time series points and period if needed. Advanced model
         parameters can also be set in the request.
        :type body: ~azure.cognitiveservices.anomalydetector.models.Request
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LastDetectResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.anomalydetector.models.LastDetectResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.last_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'Request')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LastDetectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    last_detect.metadata = {'url': '/timeseries/last/detect'}

    def change_point_detect(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Detect change point for the entire series.

        Evaluate change point score of every series point.

        :param body: Time series points and granularity is needed. Advanced
         model parameters can also be set in the request if needed.
        :type body:
         ~azure.cognitiveservices.anomalydetector.models.ChangePointDetectRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ChangePointDetectResponse or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.anomalydetector.models.ChangePointDetectResponse
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`APIErrorException<azure.cognitiveservices.anomalydetector.models.APIErrorException>`
        """
        # Construct URL
        url = self.change_point_detect.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(body, 'ChangePointDetectRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.APIErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ChangePointDetectResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    change_point_detect.metadata = {'url': '/timeseries/changepoint/detect'}
