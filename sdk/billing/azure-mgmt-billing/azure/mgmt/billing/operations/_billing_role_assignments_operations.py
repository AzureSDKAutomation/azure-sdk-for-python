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


class BillingRoleAssignmentsOperations(object):
    """BillingRoleAssignmentsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The version of the API to be used with the client request. The current version is 2020-05-01. Constant value: "2020-05-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-05-01"

        self.config = config

    def get_by_billing_account(
            self, billing_account_name, billing_role_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Gets a role assignment for the caller on a billing account. The
        operation is supported for billing accounts with agreement type
        Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_role_assignment_name: The ID that uniquely identifies a
         role assignment.
        :type billing_role_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BillingRoleAssignment or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.BillingRoleAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_billing_account.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingRoleAssignmentName': self._serialize.url("billing_role_assignment_name", billing_role_assignment_name, 'str')
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
            deserialized = self._deserialize('BillingRoleAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName}'}

    def delete_by_billing_account(
            self, billing_account_name, billing_role_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a role assignment for the caller on a billing account. The
        operation is supported for billing accounts with agreement type
        Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_role_assignment_name: The ID that uniquely identifies a
         role assignment.
        :type billing_role_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BillingRoleAssignment or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.BillingRoleAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_by_billing_account.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingRoleAssignmentName': self._serialize.url("billing_role_assignment_name", billing_role_assignment_name, 'str')
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

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BillingRoleAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName}'}

    def get_by_invoice_section(
            self, billing_account_name, billing_profile_name, invoice_section_name, billing_role_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Gets a role assignment for the caller on an invoice section. The
        operation is supported for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an
         invoice section.
        :type invoice_section_name: str
        :param billing_role_assignment_name: The ID that uniquely identifies a
         role assignment.
        :type billing_role_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BillingRoleAssignment or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.BillingRoleAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_invoice_section.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str'),
            'billingRoleAssignmentName': self._serialize.url("billing_role_assignment_name", billing_role_assignment_name, 'str')
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
            deserialized = self._deserialize('BillingRoleAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_invoice_section.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments/{billingRoleAssignmentName}'}

    def delete_by_invoice_section(
            self, billing_account_name, billing_profile_name, invoice_section_name, billing_role_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a role assignment for the caller on an invoice section. The
        operation is supported for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an
         invoice section.
        :type invoice_section_name: str
        :param billing_role_assignment_name: The ID that uniquely identifies a
         role assignment.
        :type billing_role_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BillingRoleAssignment or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.BillingRoleAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_by_invoice_section.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str'),
            'billingRoleAssignmentName': self._serialize.url("billing_role_assignment_name", billing_role_assignment_name, 'str')
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

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BillingRoleAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_by_invoice_section.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments/{billingRoleAssignmentName}'}

    def get_by_billing_profile(
            self, billing_account_name, billing_profile_name, billing_role_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Gets a role assignment for the caller on a billing profile. The
        operation is supported for billing accounts with agreement type
        Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param billing_role_assignment_name: The ID that uniquely identifies a
         role assignment.
        :type billing_role_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BillingRoleAssignment or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.BillingRoleAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_by_billing_profile.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'billingRoleAssignmentName': self._serialize.url("billing_role_assignment_name", billing_role_assignment_name, 'str')
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
            deserialized = self._deserialize('BillingRoleAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_billing_profile.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments/{billingRoleAssignmentName}'}

    def delete_by_billing_profile(
            self, billing_account_name, billing_profile_name, billing_role_assignment_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a role assignment for the caller on a billing profile. The
        operation is supported for billing accounts with agreement type
        Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param billing_role_assignment_name: The ID that uniquely identifies a
         role assignment.
        :type billing_role_assignment_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BillingRoleAssignment or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.BillingRoleAssignment or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete_by_billing_profile.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
            'billingRoleAssignmentName': self._serialize.url("billing_role_assignment_name", billing_role_assignment_name, 'str')
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

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BillingRoleAssignment', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete_by_billing_profile.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments/{billingRoleAssignmentName}'}

    def list_by_billing_account(
            self, billing_account_name, custom_headers=None, raw=False, **operation_config):
        """Lists the role assignments for the caller on a billing account. The
        operation is supported for billing accounts with agreement type
        Microsoft Partner Agreement or Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of BillingRoleAssignment
        :rtype:
         ~azure.mgmt.billing.models.BillingRoleAssignmentPaged[~azure.mgmt.billing.models.BillingRoleAssignment]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_billing_account.metadata['url']
                path_format_arguments = {
                    'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str')
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
        deserialized = models.BillingRoleAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments'}

    def list_by_invoice_section(
            self, billing_account_name, billing_profile_name, invoice_section_name, custom_headers=None, raw=False, **operation_config):
        """Lists the role assignments for the caller on an invoice section. The
        operation is supported for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param invoice_section_name: The ID that uniquely identifies an
         invoice section.
        :type invoice_section_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of BillingRoleAssignment
        :rtype:
         ~azure.mgmt.billing.models.BillingRoleAssignmentPaged[~azure.mgmt.billing.models.BillingRoleAssignment]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_invoice_section.metadata['url']
                path_format_arguments = {
                    'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
                    'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str'),
                    'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str')
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
        deserialized = models.BillingRoleAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_invoice_section.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments'}

    def list_by_billing_profile(
            self, billing_account_name, billing_profile_name, custom_headers=None, raw=False, **operation_config):
        """Lists the role assignments for the caller on a billing profile. The
        operation is supported for billing accounts with agreement type
        Microsoft Customer Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of BillingRoleAssignment
        :rtype:
         ~azure.mgmt.billing.models.BillingRoleAssignmentPaged[~azure.mgmt.billing.models.BillingRoleAssignment]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_billing_profile.metadata['url']
                path_format_arguments = {
                    'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
                    'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str')
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
        deserialized = models.BillingRoleAssignmentPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_billing_profile.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments'}
