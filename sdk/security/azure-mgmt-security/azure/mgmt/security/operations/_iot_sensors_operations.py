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
from msrestazure.azure_exceptions import CloudError

from .. import models


class IotSensorsOperations(object):
    """IotSensorsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: API version for the operation. Constant value: "2020-08-06-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-08-06-preview"

        self.config = config

    def list(
            self, scope, custom_headers=None, raw=False, **operation_config):
        """List IoT sensors.

        :param scope: Scope of the query (IoT Hub,
         /providers/Microsoft.Devices/iotHubs/myHub)
        :type scope: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: IotSensorsList or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.security.models.IotSensorsList or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
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
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('IotSensorsList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/{scope}/providers/Microsoft.Security/iotSensors'}

    def get(
            self, scope, iot_sensor_name, custom_headers=None, raw=False, **operation_config):
        """Get IoT sensor.

        :param scope: Scope of the query (IoT Hub,
         /providers/Microsoft.Devices/iotHubs/myHub)
        :type scope: str
        :param iot_sensor_name: Name of the IoT sensor
        :type iot_sensor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: IotSensorsModel or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.security.models.IotSensorsModel or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'iotSensorName': self._serialize.url("iot_sensor_name", iot_sensor_name, 'str')
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
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('IotSensorsModel', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.Security/iotSensors/{iotSensorName}'}

    def create_or_update(
            self, scope, iot_sensor_name, ti_automatic_updates=None, zone=None, custom_headers=None, raw=False, **operation_config):
        """Create or update IoT sensor.

        :param scope: Scope of the query (IoT Hub,
         /providers/Microsoft.Devices/iotHubs/myHub)
        :type scope: str
        :param iot_sensor_name: Name of the IoT sensor
        :type iot_sensor_name: str
        :param ti_automatic_updates: TI Automatic mode status of the IoT
         sensor
        :type ti_automatic_updates: bool
        :param zone: Zone of the IoT sensor
        :type zone: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: IotSensorsModel or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.security.models.IotSensorsModel or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        iot_sensors_model = models.IotSensorsModel(ti_automatic_updates=ti_automatic_updates, zone=zone)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'iotSensorName': self._serialize.url("iot_sensor_name", iot_sensor_name, 'str')
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
        body_content = self._serialize.body(iot_sensors_model, 'IotSensorsModel')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('IotSensorsModel', response)
        if response.status_code == 201:
            deserialized = self._deserialize('IotSensorsModel', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/{scope}/providers/Microsoft.Security/iotSensors/{iotSensorName}'}

    def delete(
            self, scope, iot_sensor_name, custom_headers=None, raw=False, **operation_config):
        """Delete IoT sensor.

        :param scope: Scope of the query (IoT Hub,
         /providers/Microsoft.Devices/iotHubs/myHub)
        :type scope: str
        :param iot_sensor_name: Name of the IoT sensor
        :type iot_sensor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'iotSensorName': self._serialize.url("iot_sensor_name", iot_sensor_name, 'str')
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
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/{scope}/providers/Microsoft.Security/iotSensors/{iotSensorName}'}

    def download_activation(
            self, scope, iot_sensor_name, custom_headers=None, raw=False, callback=None, **operation_config):
        """Download sensor activation file.

        :param scope: Scope of the query (IoT Hub,
         /providers/Microsoft.Devices/iotHubs/myHub)
        :type scope: str
        :param iot_sensor_name: Name of the IoT sensor
        :type iot_sensor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.download_activation.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'iotSensorName': self._serialize.url("iot_sensor_name", iot_sensor_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/zip'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=True, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    download_activation.metadata = {'url': '/{scope}/providers/Microsoft.Security/iotSensors/{iotSensorName}/downloadActivation'}

    def download_reset_password(
            self, scope, iot_sensor_name, appliance_id=None, custom_headers=None, raw=False, callback=None, **operation_config):
        """Download file for reset password of the sensor.

        :param scope: Scope of the query (IoT Hub,
         /providers/Microsoft.Devices/iotHubs/myHub)
        :type scope: str
        :param iot_sensor_name: Name of the IoT sensor
        :type iot_sensor_name: str
        :param appliance_id: The appliance id of the sensor.
        :type appliance_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        body = models.ResetPasswordInput(appliance_id=appliance_id)

        # Construct URL
        url = self.download_reset_password.metadata['url']
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'iotSensorName': self._serialize.url("iot_sensor_name", iot_sensor_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/zip'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'ResetPasswordInput')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=True, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    download_reset_password.metadata = {'url': '/{scope}/providers/Microsoft.Security/iotSensors/{iotSensorName}/downloadResetPassword'}
