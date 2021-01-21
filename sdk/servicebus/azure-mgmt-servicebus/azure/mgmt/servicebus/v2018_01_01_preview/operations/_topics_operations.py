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


class TopicsOperations(object):
    """TopicsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2018-01-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-01-01-preview"

        self.config = config

    def list_authorization_rules(
            self, resource_group_name, namespace_name, topic_name, custom_headers=None, raw=False, **operation_config):
        """Gets authorization rules for a topic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of SBAuthorizationRule
        :rtype:
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBAuthorizationRulePaged[~azure.mgmt.servicebus.v2018_01_01_preview.models.SBAuthorizationRule]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_authorization_rules.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
                    'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
                    'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
        deserialized = models.SBAuthorizationRulePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_authorization_rules.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules'}

    def create_or_update_authorization_rule(
            self, resource_group_name, namespace_name, topic_name, authorization_rule_name, rights, custom_headers=None, raw=False, **operation_config):
        """Creates an authorization rule for the specified topic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param rights: The rights associated with the rule.
        :type rights: list[str or
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.AccessRights]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SBAuthorizationRule or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBAuthorizationRule
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        parameters = models.SBAuthorizationRule(rights=rights)

        # Construct URL
        url = self.create_or_update_authorization_rule.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', max_length=50, min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
        body_content = self._serialize.body(parameters, 'SBAuthorizationRule')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SBAuthorizationRule', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update_authorization_rule.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}'}

    def get_authorization_rule(
            self, resource_group_name, namespace_name, topic_name, authorization_rule_name, custom_headers=None, raw=False, **operation_config):
        """Returns the specified authorization rule.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SBAuthorizationRule or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBAuthorizationRule
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_authorization_rule.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', max_length=50, min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
            deserialized = self._deserialize('SBAuthorizationRule', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_authorization_rule.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}'}

    def delete_authorization_rule(
            self, resource_group_name, namespace_name, topic_name, authorization_rule_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a topic authorization rule.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_authorization_rule.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', max_length=50, min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete_authorization_rule.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}'}

    def list_keys(
            self, resource_group_name, namespace_name, topic_name, authorization_rule_name, custom_headers=None, raw=False, **operation_config):
        """Gets the primary and secondary connection strings for the topic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AccessKeys or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.servicebus.v2018_01_01_preview.models.AccessKeys
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_keys.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', max_length=50, min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AccessKeys', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}/ListKeys'}

    def regenerate_keys(
            self, resource_group_name, namespace_name, topic_name, authorization_rule_name, key_type, key=None, custom_headers=None, raw=False, **operation_config):
        """Regenerates primary or secondary connection strings for the topic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param authorization_rule_name: The authorization rule name.
        :type authorization_rule_name: str
        :param key_type: The access key to regenerate. Possible values
         include: 'PrimaryKey', 'SecondaryKey'
        :type key_type: str or
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.KeyType
        :param key: Optional, if the key value provided, is reset for KeyType
         value or autogenerate Key value set for keyType
        :type key: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AccessKeys or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.servicebus.v2018_01_01_preview.models.AccessKeys
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        parameters = models.RegenerateAccessKeyParameters(key_type=key_type, key=key)

        # Construct URL
        url = self.regenerate_keys.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'authorizationRuleName': self._serialize.url("authorization_rule_name", authorization_rule_name, 'str', max_length=50, min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
        body_content = self._serialize.body(parameters, 'RegenerateAccessKeyParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AccessKeys', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    regenerate_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}/authorizationRules/{authorizationRuleName}/regenerateKeys'}

    def list_by_namespace(
            self, resource_group_name, namespace_name, skip=None, top=None, custom_headers=None, raw=False, **operation_config):
        """Gets all the topics in a namespace.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param skip: Skip is only used if a previous operation returned a
         partial result. If a previous response contains a nextLink element,
         the value of the nextLink element will include a skip parameter that
         specifies a starting point to use for subsequent calls.
        :type skip: int
        :param top: May be used to limit the number of results to the most
         recent N usageDetails.
        :type top: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of SBTopic
        :rtype:
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBTopicPaged[~azure.mgmt.servicebus.v2018_01_01_preview.models.SBTopic]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_namespace.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
                    'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int', maximum=1000, minimum=0)
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int', maximum=1000, minimum=1)

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
        deserialized = models.SBTopicPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_namespace.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics'}

    def create_or_update(
            self, resource_group_name, namespace_name, topic_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates a topic in the specified namespace.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param parameters: Parameters supplied to create a topic resource.
        :type parameters:
         ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBTopic
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SBTopic or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBTopic or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
        body_content = self._serialize.body(parameters, 'SBTopic')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('SBTopic', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}'}

    def delete(
            self, resource_group_name, namespace_name, topic_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a topic from the specified namespace and resource group.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}'}

    def get(
            self, resource_group_name, namespace_name, topic_name, custom_headers=None, raw=False, **operation_config):
        """Returns a description for the specified topic.

        :param resource_group_name: Name of the Resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param namespace_name: The namespace name
        :type namespace_name: str
        :param topic_name: The topic name.
        :type topic_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SBTopic or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.servicebus.v2018_01_01_preview.models.SBTopic or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.servicebus.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'namespaceName': self._serialize.url("namespace_name", namespace_name, 'str', max_length=50, min_length=6),
            'topicName': self._serialize.url("topic_name", topic_name, 'str', min_length=1),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
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
            deserialized = self._deserialize('SBTopic', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/topics/{topicName}'}
