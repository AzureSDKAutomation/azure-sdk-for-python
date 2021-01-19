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


class ScopeRoleAssignmentApprovalOperations(object):
    """ScopeRoleAssignmentApprovalOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to be used with the HTTP request. Constant value: "2021-01-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2021-01-01-preview"

        self.config = config

    def list(
            self, scope, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get role assignment approvals.

        :param scope: The scope of the resource.
        :type scope: str
        :param filter: The filter to apply on the operation. Valid values for
         $filter are: 'asApprover()', 'asCreatedBy()' and 'asTarget()'. If
         $filter is not provided, no filtering is performed. If
         $filter=asApprover() is provided, the returned list only includes all
         role assignment approvals that the calling user is assigned as an
         approver for. If $filter=asCreatedBy() is provided, the returned list
         only includes all role assignment approvals that the calling user
         created requests for. If $filter=asTarget() is provided, the returned
         list only includes all role assignment approvals that the calling user
         has requests targeted for.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of RoleAssignmentApproval
        :rtype:
         ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApprovalPaged[~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApproval]
        :raises:
         :class:`ErrorDefinitionException<azure.mgmt.authorization.v2021_01_01_preview.models.ErrorDefinitionException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str', skip_quote=True)

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
                raise models.ErrorDefinitionException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.RoleAssignmentApprovalPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleAssignmentApprovals'}

    def get_by_id(
            self, approval_id, scope, custom_headers=None, raw=False, **operation_config):
        """Get role assignment approval.

        :param approval_id: The id of the role assignment approval.
        :type approval_id: str
        :param scope: The scope of the resource.
        :type scope: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RoleAssignmentApproval or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.authorization.v2021_01_01_preview.models.RoleAssignmentApproval
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorDefinitionException<azure.mgmt.authorization.v2021_01_01_preview.models.ErrorDefinitionException>`
        """
        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'approvalId': self._serialize.url("approval_id", approval_id, 'str'),
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
            raise models.ErrorDefinitionException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RoleAssignmentApproval', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_by_id.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleAssignmentApprovals/{approvalId}'}
