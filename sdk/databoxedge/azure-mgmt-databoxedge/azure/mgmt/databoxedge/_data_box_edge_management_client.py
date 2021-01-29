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

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import DataBoxEdgeManagementClientConfiguration



class DataBoxEdgeManagementClient(MultiApiClientMixin, SDKClient):
    """DataBoxEdgeManagementClient

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: DataBoxEdgeManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2019-08-01'
    _PROFILE_TAG = "azure.mgmt.databoxedge.DataBoxEdgeManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = DataBoxEdgeManagementClientConfiguration(credentials, subscription_id, base_url)
        super(DataBoxEdgeManagementClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-03-01: :mod:`v2019_03_01.models<azure.mgmt.databoxedge.v2019_03_01.models>`
           * 2019-07-01: :mod:`v2019_07_01.models<azure.mgmt.databoxedge.v2019_07_01.models>`
           * 2019-08-01: :mod:`v2019_08_01.models<azure.mgmt.databoxedge.v2019_08_01.models>`
           * 2020-05-01-preview: :mod:`v2020_05_01_preview.models<azure.mgmt.databoxedge.v2020_05_01_preview.models>`
           * 2020-09-01: :mod:`v2020_09_01_preview.models<azure.mgmt.databoxedge.v2020_09_01_preview.models>`
        """
        if api_version == '2019-03-01':
            from .v2019_03_01 import models
            return models
        elif api_version == '2019-07-01':
            from .v2019_07_01 import models
            return models
        elif api_version == '2019-08-01':
            from .v2019_08_01 import models
            return models
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview import models
            return models
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def addons(self):
        """Instance depends on the API version:

           * 2020-09-01: :class:`AddonsOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.AddonsOperations>`
        """
        api_version = self._get_api_version('addons')
        if api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import AddonsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def alerts(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`AlertsOperations<azure.mgmt.databoxedge.v2019_03_01.operations.AlertsOperations>`
           * 2019-07-01: :class:`AlertsOperations<azure.mgmt.databoxedge.v2019_07_01.operations.AlertsOperations>`
           * 2019-08-01: :class:`AlertsOperations<azure.mgmt.databoxedge.v2019_08_01.operations.AlertsOperations>`
           * 2020-05-01-preview: :class:`AlertsOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.AlertsOperations>`
           * 2020-09-01: :class:`AlertsOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.AlertsOperations>`
        """
        api_version = self._get_api_version('alerts')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import AlertsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import AlertsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import AlertsOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import AlertsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import AlertsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def available_skus(self):
        """Instance depends on the API version:

           * 2020-05-01-preview: :class:`AvailableSkusOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.AvailableSkusOperations>`
           * 2020-09-01: :class:`AvailableSkusOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.AvailableSkusOperations>`
        """
        api_version = self._get_api_version('available_skus')
        if api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import AvailableSkusOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import AvailableSkusOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def bandwidth_schedules(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`BandwidthSchedulesOperations<azure.mgmt.databoxedge.v2019_03_01.operations.BandwidthSchedulesOperations>`
           * 2019-07-01: :class:`BandwidthSchedulesOperations<azure.mgmt.databoxedge.v2019_07_01.operations.BandwidthSchedulesOperations>`
           * 2019-08-01: :class:`BandwidthSchedulesOperations<azure.mgmt.databoxedge.v2019_08_01.operations.BandwidthSchedulesOperations>`
           * 2020-05-01-preview: :class:`BandwidthSchedulesOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.BandwidthSchedulesOperations>`
           * 2020-09-01: :class:`BandwidthSchedulesOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.BandwidthSchedulesOperations>`
        """
        api_version = self._get_api_version('bandwidth_schedules')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import BandwidthSchedulesOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import BandwidthSchedulesOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import BandwidthSchedulesOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import BandwidthSchedulesOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import BandwidthSchedulesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def containers(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`ContainersOperations<azure.mgmt.databoxedge.v2019_08_01.operations.ContainersOperations>`
           * 2020-05-01-preview: :class:`ContainersOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.ContainersOperations>`
           * 2020-09-01: :class:`ContainersOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.ContainersOperations>`
        """
        api_version = self._get_api_version('containers')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import ContainersOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import ContainersOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import ContainersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def devices(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`DevicesOperations<azure.mgmt.databoxedge.v2019_03_01.operations.DevicesOperations>`
           * 2019-07-01: :class:`DevicesOperations<azure.mgmt.databoxedge.v2019_07_01.operations.DevicesOperations>`
           * 2019-08-01: :class:`DevicesOperations<azure.mgmt.databoxedge.v2019_08_01.operations.DevicesOperations>`
           * 2020-05-01-preview: :class:`DevicesOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.DevicesOperations>`
           * 2020-09-01: :class:`DevicesOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.DevicesOperations>`
        """
        api_version = self._get_api_version('devices')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import DevicesOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import DevicesOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import DevicesOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import DevicesOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import DevicesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def jobs(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`JobsOperations<azure.mgmt.databoxedge.v2019_03_01.operations.JobsOperations>`
           * 2019-07-01: :class:`JobsOperations<azure.mgmt.databoxedge.v2019_07_01.operations.JobsOperations>`
           * 2019-08-01: :class:`JobsOperations<azure.mgmt.databoxedge.v2019_08_01.operations.JobsOperations>`
           * 2020-05-01-preview: :class:`JobsOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.JobsOperations>`
           * 2020-09-01: :class:`JobsOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.JobsOperations>`
        """
        api_version = self._get_api_version('jobs')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import JobsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import JobsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import JobsOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import JobsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import JobsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def monitoring_config(self):
        """Instance depends on the API version:

           * 2020-09-01: :class:`MonitoringConfigOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.MonitoringConfigOperations>`
        """
        api_version = self._get_api_version('monitoring_config')
        if api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import MonitoringConfigOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def nodes(self):
        """Instance depends on the API version:

           * 2019-07-01: :class:`NodesOperations<azure.mgmt.databoxedge.v2019_07_01.operations.NodesOperations>`
           * 2019-08-01: :class:`NodesOperations<azure.mgmt.databoxedge.v2019_08_01.operations.NodesOperations>`
           * 2020-05-01-preview: :class:`NodesOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.NodesOperations>`
           * 2020-09-01: :class:`NodesOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.NodesOperations>`
        """
        api_version = self._get_api_version('nodes')
        if api_version == '2019-07-01':
            from .v2019_07_01.operations import NodesOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import NodesOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import NodesOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import NodesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`Operations<azure.mgmt.databoxedge.v2019_03_01.operations.Operations>`
           * 2019-07-01: :class:`Operations<azure.mgmt.databoxedge.v2019_07_01.operations.Operations>`
           * 2019-08-01: :class:`Operations<azure.mgmt.databoxedge.v2019_08_01.operations.Operations>`
           * 2020-05-01-preview: :class:`Operations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.Operations>`
           * 2020-09-01: :class:`Operations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import Operations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import Operations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import Operations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations_status(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`OperationsStatusOperations<azure.mgmt.databoxedge.v2019_03_01.operations.OperationsStatusOperations>`
           * 2019-07-01: :class:`OperationsStatusOperations<azure.mgmt.databoxedge.v2019_07_01.operations.OperationsStatusOperations>`
           * 2019-08-01: :class:`OperationsStatusOperations<azure.mgmt.databoxedge.v2019_08_01.operations.OperationsStatusOperations>`
           * 2020-05-01-preview: :class:`OperationsStatusOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.OperationsStatusOperations>`
           * 2020-09-01: :class:`OperationsStatusOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.OperationsStatusOperations>`
        """
        api_version = self._get_api_version('operations_status')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import OperationsStatusOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import OperationsStatusOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import OperationsStatusOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import OperationsStatusOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import OperationsStatusOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def orders(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`OrdersOperations<azure.mgmt.databoxedge.v2019_03_01.operations.OrdersOperations>`
           * 2019-07-01: :class:`OrdersOperations<azure.mgmt.databoxedge.v2019_07_01.operations.OrdersOperations>`
           * 2019-08-01: :class:`OrdersOperations<azure.mgmt.databoxedge.v2019_08_01.operations.OrdersOperations>`
           * 2020-05-01-preview: :class:`OrdersOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.OrdersOperations>`
           * 2020-09-01: :class:`OrdersOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.OrdersOperations>`
        """
        api_version = self._get_api_version('orders')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import OrdersOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import OrdersOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import OrdersOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import OrdersOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import OrdersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def roles(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`RolesOperations<azure.mgmt.databoxedge.v2019_03_01.operations.RolesOperations>`
           * 2019-07-01: :class:`RolesOperations<azure.mgmt.databoxedge.v2019_07_01.operations.RolesOperations>`
           * 2019-08-01: :class:`RolesOperations<azure.mgmt.databoxedge.v2019_08_01.operations.RolesOperations>`
           * 2020-05-01-preview: :class:`RolesOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.RolesOperations>`
           * 2020-09-01: :class:`RolesOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.RolesOperations>`
        """
        api_version = self._get_api_version('roles')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import RolesOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import RolesOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import RolesOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import RolesOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import RolesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def shares(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`SharesOperations<azure.mgmt.databoxedge.v2019_03_01.operations.SharesOperations>`
           * 2019-07-01: :class:`SharesOperations<azure.mgmt.databoxedge.v2019_07_01.operations.SharesOperations>`
           * 2019-08-01: :class:`SharesOperations<azure.mgmt.databoxedge.v2019_08_01.operations.SharesOperations>`
           * 2020-05-01-preview: :class:`SharesOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.SharesOperations>`
           * 2020-09-01: :class:`SharesOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.SharesOperations>`
        """
        api_version = self._get_api_version('shares')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import SharesOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import SharesOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import SharesOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import SharesOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import SharesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def skus(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`SkusOperations<azure.mgmt.databoxedge.v2019_08_01.operations.SkusOperations>`
           * 2020-05-01-preview: :class:`SkusOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.SkusOperations>`
        """
        api_version = self._get_api_version('skus')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import SkusOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import SkusOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def storage_account_credentials(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`StorageAccountCredentialsOperations<azure.mgmt.databoxedge.v2019_03_01.operations.StorageAccountCredentialsOperations>`
           * 2019-07-01: :class:`StorageAccountCredentialsOperations<azure.mgmt.databoxedge.v2019_07_01.operations.StorageAccountCredentialsOperations>`
           * 2019-08-01: :class:`StorageAccountCredentialsOperations<azure.mgmt.databoxedge.v2019_08_01.operations.StorageAccountCredentialsOperations>`
           * 2020-05-01-preview: :class:`StorageAccountCredentialsOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.StorageAccountCredentialsOperations>`
           * 2020-09-01: :class:`StorageAccountCredentialsOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.StorageAccountCredentialsOperations>`
        """
        api_version = self._get_api_version('storage_account_credentials')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import StorageAccountCredentialsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import StorageAccountCredentialsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import StorageAccountCredentialsOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import StorageAccountCredentialsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import StorageAccountCredentialsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def storage_accounts(self):
        """Instance depends on the API version:

           * 2019-08-01: :class:`StorageAccountsOperations<azure.mgmt.databoxedge.v2019_08_01.operations.StorageAccountsOperations>`
           * 2020-05-01-preview: :class:`StorageAccountsOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.StorageAccountsOperations>`
           * 2020-09-01: :class:`StorageAccountsOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.StorageAccountsOperations>`
        """
        api_version = self._get_api_version('storage_accounts')
        if api_version == '2019-08-01':
            from .v2019_08_01.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import StorageAccountsOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import StorageAccountsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def triggers(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`TriggersOperations<azure.mgmt.databoxedge.v2019_03_01.operations.TriggersOperations>`
           * 2019-07-01: :class:`TriggersOperations<azure.mgmt.databoxedge.v2019_07_01.operations.TriggersOperations>`
           * 2019-08-01: :class:`TriggersOperations<azure.mgmt.databoxedge.v2019_08_01.operations.TriggersOperations>`
           * 2020-05-01-preview: :class:`TriggersOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.TriggersOperations>`
           * 2020-09-01: :class:`TriggersOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.TriggersOperations>`
        """
        api_version = self._get_api_version('triggers')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import TriggersOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import TriggersOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import TriggersOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import TriggersOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import TriggersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def users(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`UsersOperations<azure.mgmt.databoxedge.v2019_03_01.operations.UsersOperations>`
           * 2019-07-01: :class:`UsersOperations<azure.mgmt.databoxedge.v2019_07_01.operations.UsersOperations>`
           * 2019-08-01: :class:`UsersOperations<azure.mgmt.databoxedge.v2019_08_01.operations.UsersOperations>`
           * 2020-05-01-preview: :class:`UsersOperations<azure.mgmt.databoxedge.v2020_05_01_preview.operations.UsersOperations>`
           * 2020-09-01: :class:`UsersOperations<azure.mgmt.databoxedge.v2020_09_01_preview.operations.UsersOperations>`
        """
        api_version = self._get_api_version('users')
        if api_version == '2019-03-01':
            from .v2019_03_01.operations import UsersOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import UsersOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import UsersOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import UsersOperations as OperationClass
        elif api_version == '2020-09-01':
            from .v2020_09_01_preview.operations import UsersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
