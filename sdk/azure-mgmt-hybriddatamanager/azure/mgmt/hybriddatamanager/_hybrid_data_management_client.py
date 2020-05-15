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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import HybridDataManagementClientConfiguration
from .operations import Operations
from .operations import DataManagersOperations
from .operations import DataServicesOperations
from .operations import JobDefinitionsOperations
from .operations import JobsOperations
from .operations import DataStoresOperations
from .operations import DataStoreTypesOperations
from .operations import PublicKeysOperations
from . import models


class HybridDataManagementClient(SDKClient):
    """HybridDataManagementClient

    :ivar config: Configuration for client.
    :vartype config: HybridDataManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.hybriddatamanager.operations.Operations
    :ivar data_managers: DataManagers operations
    :vartype data_managers: azure.mgmt.hybriddatamanager.operations.DataManagersOperations
    :ivar data_services: DataServices operations
    :vartype data_services: azure.mgmt.hybriddatamanager.operations.DataServicesOperations
    :ivar job_definitions: JobDefinitions operations
    :vartype job_definitions: azure.mgmt.hybriddatamanager.operations.JobDefinitionsOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.hybriddatamanager.operations.JobsOperations
    :ivar data_stores: DataStores operations
    :vartype data_stores: azure.mgmt.hybriddatamanager.operations.DataStoresOperations
    :ivar data_store_types: DataStoreTypes operations
    :vartype data_store_types: azure.mgmt.hybriddatamanager.operations.DataStoreTypesOperations
    :ivar public_keys: PublicKeys operations
    :vartype public_keys: azure.mgmt.hybriddatamanager.operations.PublicKeysOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = HybridDataManagementClientConfiguration(credentials, subscription_id, base_url)
        super(HybridDataManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_managers = DataManagersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_services = DataServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_definitions = JobDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_stores = DataStoresOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_store_types = DataStoreTypesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.public_keys = PublicKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
