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

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import MonitorClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class MonitorClient(MultiApiClientMixin, _SDKClient):
    """Monitor Management Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2019-10-17-preview'
    _PROFILE_TAG = "azure.mgmt.monitor.MonitorClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'action_groups': '2019-06-01',
            'activity_log_alerts': '2017-04-01',
            'activity_logs': '2015-04-01',
            'alert_rule_incidents': '2016-03-01',
            'alert_rules': '2016-03-01',
            'autoscale_settings': '2015-04-01',
            'baseline': '2018-09-01',
            'baselines': '2019-03-01',
            'diagnostic_settings': '2017-05-01-preview',
            'diagnostic_settings_category': '2017-05-01-preview',
            'event_categories': '2015-04-01',
            'guest_diagnostics_settings': '2018-06-01-preview',
            'guest_diagnostics_settings_association': '2018-06-01-preview',
            'log_profiles': '2016-03-01',
            'metric_alerts': '2018-03-01',
            'metric_alerts_status': '2018-03-01',
            'metric_baseline': '2018-09-01',
            'metric_definitions': '2018-01-01',
            'metric_namespaces': '2017-12-01-preview',
            'metrics': '2018-01-01',
            'operations': '2015-04-01',
            'scheduled_query_rules': '2018-04-16',
            'service_diagnostic_settings': '2016-09-01',
            'subscription_diagnostic_settings': '2017-05-01-preview',
            'tenant_activity_logs': '2015-04-01',
            'vm_insights': '2018-11-27-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MonitorClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(MonitorClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-04-01: :mod:`v2015_04_01.models<azure.mgmt.monitor.v2015_04_01.models>`
           * 2015-07-01: :mod:`v2015_07_01.models<azure.mgmt.monitor.v2015_07_01.models>`
           * 2016-03-01: :mod:`v2016_03_01.models<azure.mgmt.monitor.v2016_03_01.models>`
           * 2016-09-01: :mod:`v2016_09_01.models<azure.mgmt.monitor.v2016_09_01.models>`
           * 2017-03-01-preview: :mod:`v2017_03_01_preview.models<azure.mgmt.monitor.v2017_03_01_preview.models>`
           * 2017-04-01: :mod:`v2017_04_01.models<azure.mgmt.monitor.v2017_04_01.models>`
           * 2017-05-01-preview: :mod:`v2017_05_01_preview.models<azure.mgmt.monitor.v2017_05_01_preview.models>`
           * 2017-11-01-preview: :mod:`v2017_11_01_preview.models<azure.mgmt.monitor.v2017_11_01_preview.models>`
           * 2017-12-01-preview: :mod:`v2017_12_01_preview.models<azure.mgmt.monitor.v2017_12_01_preview.models>`
           * 2018-01-01: :mod:`v2018_01_01.models<azure.mgmt.monitor.v2018_01_01.models>`
           * 2018-03-01: :mod:`v2018_03_01.models<azure.mgmt.monitor.v2018_03_01.models>`
           * 2018-04-16: :mod:`v2018_04_16.models<azure.mgmt.monitor.v2018_04_16.models>`
           * 2018-06-01-preview: :mod:`v2018_06_01_preview.models<azure.mgmt.monitor.v2018_06_01_preview.models>`
           * 2018-09-01: :mod:`v2018_09_01.models<azure.mgmt.monitor.v2018_09_01.models>`
           * 2018-11-27-preview: :mod:`v2018_11_27_preview.models<azure.mgmt.monitor.v2018_11_27_preview.models>`
           * 2019-03-01: :mod:`v2019_03_01.models<azure.mgmt.monitor.v2019_03_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.monitor.v2019_06_01.models>`
           * 2019-10-17-preview: :mod:`v2019_10_17.models<azure.mgmt.monitor.v2019_10_17.models>`
           * 2019-11-01-preview: :mod:`v2019_11_01_preview.models<azure.mgmt.monitor.v2019_11_01_preview.models>`
           * 2020-01-01-preview: :mod:`v2020_01_01_preview.models<azure.mgmt.monitor.v2020_01_01_preview.models>`
           * 2020-05-01-preview: :mod:`v2020_05_01_preview.models<azure.mgmt.monitor.v2020_05_01_preview.models>`
        """
        if api_version == '2015-04-01':
            from ..v2015_04_01 import models
            return models
        elif api_version == '2015-07-01':
            from ..v2015_07_01 import models
            return models
        elif api_version == '2016-03-01':
            from ..v2016_03_01 import models
            return models
        elif api_version == '2016-09-01':
            from ..v2016_09_01 import models
            return models
        elif api_version == '2017-03-01-preview':
            from ..v2017_03_01_preview import models
            return models
        elif api_version == '2017-04-01':
            from ..v2017_04_01 import models
            return models
        elif api_version == '2017-05-01-preview':
            from ..v2017_05_01_preview import models
            return models
        elif api_version == '2017-11-01-preview':
            from ..v2017_11_01_preview import models
            return models
        elif api_version == '2017-12-01-preview':
            from ..v2017_12_01_preview import models
            return models
        elif api_version == '2018-01-01':
            from ..v2018_01_01 import models
            return models
        elif api_version == '2018-03-01':
            from ..v2018_03_01 import models
            return models
        elif api_version == '2018-04-16':
            from ..v2018_04_16 import models
            return models
        elif api_version == '2018-06-01-preview':
            from ..v2018_06_01_preview import models
            return models
        elif api_version == '2018-09-01':
            from ..v2018_09_01 import models
            return models
        elif api_version == '2018-11-27-preview':
            from ..v2018_11_27_preview import models
            return models
        elif api_version == '2019-03-01':
            from ..v2019_03_01 import models
            return models
        elif api_version == '2019-06-01':
            from ..v2019_06_01 import models
            return models
        elif api_version == '2019-10-17-preview':
            from ..v2019_10_17 import models
            return models
        elif api_version == '2019-11-01-preview':
            from ..v2019_11_01_preview import models
            return models
        elif api_version == '2020-01-01-preview':
            from ..v2020_01_01_preview import models
            return models
        elif api_version == '2020-05-01-preview':
            from ..v2020_05_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def action_groups(self):
        """Instance depends on the API version:

           * 2017-04-01: :class:`ActionGroupsOperations<azure.mgmt.monitor.v2017_04_01.aio.operations.ActionGroupsOperations>`
           * 2018-03-01: :class:`ActionGroupsOperations<azure.mgmt.monitor.v2018_03_01.aio.operations.ActionGroupsOperations>`
           * 2018-09-01: :class:`ActionGroupsOperations<azure.mgmt.monitor.v2018_09_01.aio.operations.ActionGroupsOperations>`
           * 2019-03-01: :class:`ActionGroupsOperations<azure.mgmt.monitor.v2019_03_01.aio.operations.ActionGroupsOperations>`
           * 2019-06-01: :class:`ActionGroupsOperations<azure.mgmt.monitor.v2019_06_01.aio.operations.ActionGroupsOperations>`
        """
        api_version = self._get_api_version('action_groups')
        if api_version == '2017-04-01':
            from ..v2017_04_01.aio.operations import ActionGroupsOperations as OperationClass
        elif api_version == '2018-03-01':
            from ..v2018_03_01.aio.operations import ActionGroupsOperations as OperationClass
        elif api_version == '2018-09-01':
            from ..v2018_09_01.aio.operations import ActionGroupsOperations as OperationClass
        elif api_version == '2019-03-01':
            from ..v2019_03_01.aio.operations import ActionGroupsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import ActionGroupsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'action_groups'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def activity_log_alerts(self):
        """Instance depends on the API version:

           * 2017-03-01-preview: :class:`ActivityLogAlertsOperations<azure.mgmt.monitor.v2017_03_01_preview.aio.operations.ActivityLogAlertsOperations>`
           * 2017-04-01: :class:`ActivityLogAlertsOperations<azure.mgmt.monitor.v2017_04_01.aio.operations.ActivityLogAlertsOperations>`
        """
        api_version = self._get_api_version('activity_log_alerts')
        if api_version == '2017-03-01-preview':
            from ..v2017_03_01_preview.aio.operations import ActivityLogAlertsOperations as OperationClass
        elif api_version == '2017-04-01':
            from ..v2017_04_01.aio.operations import ActivityLogAlertsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'activity_log_alerts'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def activity_logs(self):
        """Instance depends on the API version:

           * 2015-04-01: :class:`ActivityLogsOperations<azure.mgmt.monitor.v2015_04_01.aio.operations.ActivityLogsOperations>`
        """
        api_version = self._get_api_version('activity_logs')
        if api_version == '2015-04-01':
            from ..v2015_04_01.aio.operations import ActivityLogsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'activity_logs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def alert_rule_incidents(self):
        """Instance depends on the API version:

           * 2016-03-01: :class:`AlertRuleIncidentsOperations<azure.mgmt.monitor.v2016_03_01.aio.operations.AlertRuleIncidentsOperations>`
        """
        api_version = self._get_api_version('alert_rule_incidents')
        if api_version == '2016-03-01':
            from ..v2016_03_01.aio.operations import AlertRuleIncidentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'alert_rule_incidents'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def alert_rules(self):
        """Instance depends on the API version:

           * 2016-03-01: :class:`AlertRulesOperations<azure.mgmt.monitor.v2016_03_01.aio.operations.AlertRulesOperations>`
        """
        api_version = self._get_api_version('alert_rules')
        if api_version == '2016-03-01':
            from ..v2016_03_01.aio.operations import AlertRulesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'alert_rules'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def autoscale_settings(self):
        """Instance depends on the API version:

           * 2015-04-01: :class:`AutoscaleSettingsOperations<azure.mgmt.monitor.v2015_04_01.aio.operations.AutoscaleSettingsOperations>`
        """
        api_version = self._get_api_version('autoscale_settings')
        if api_version == '2015-04-01':
            from ..v2015_04_01.aio.operations import AutoscaleSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'autoscale_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def baseline(self):
        """Instance depends on the API version:

           * 2018-09-01: :class:`BaselineOperations<azure.mgmt.monitor.v2018_09_01.aio.operations.BaselineOperations>`
        """
        api_version = self._get_api_version('baseline')
        if api_version == '2018-09-01':
            from ..v2018_09_01.aio.operations import BaselineOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'baseline'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def baselines(self):
        """Instance depends on the API version:

           * 2019-03-01: :class:`BaselinesOperations<azure.mgmt.monitor.v2019_03_01.aio.operations.BaselinesOperations>`
        """
        api_version = self._get_api_version('baselines')
        if api_version == '2019-03-01':
            from ..v2019_03_01.aio.operations import BaselinesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'baselines'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def data_collection_rule_associations(self):
        """Instance depends on the API version:

           * 2019-11-01-preview: :class:`DataCollectionRuleAssociationsOperations<azure.mgmt.monitor.v2019_11_01_preview.aio.operations.DataCollectionRuleAssociationsOperations>`
        """
        api_version = self._get_api_version('data_collection_rule_associations')
        if api_version == '2019-11-01-preview':
            from ..v2019_11_01_preview.aio.operations import DataCollectionRuleAssociationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'data_collection_rule_associations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def data_collection_rules(self):
        """Instance depends on the API version:

           * 2019-11-01-preview: :class:`DataCollectionRulesOperations<azure.mgmt.monitor.v2019_11_01_preview.aio.operations.DataCollectionRulesOperations>`
        """
        api_version = self._get_api_version('data_collection_rules')
        if api_version == '2019-11-01-preview':
            from ..v2019_11_01_preview.aio.operations import DataCollectionRulesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'data_collection_rules'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def diagnostic_settings(self):
        """Instance depends on the API version:

           * 2017-05-01-preview: :class:`DiagnosticSettingsOperations<azure.mgmt.monitor.v2017_05_01_preview.aio.operations.DiagnosticSettingsOperations>`
        """
        api_version = self._get_api_version('diagnostic_settings')
        if api_version == '2017-05-01-preview':
            from ..v2017_05_01_preview.aio.operations import DiagnosticSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'diagnostic_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def diagnostic_settings_category(self):
        """Instance depends on the API version:

           * 2017-05-01-preview: :class:`DiagnosticSettingsCategoryOperations<azure.mgmt.monitor.v2017_05_01_preview.aio.operations.DiagnosticSettingsCategoryOperations>`
        """
        api_version = self._get_api_version('diagnostic_settings_category')
        if api_version == '2017-05-01-preview':
            from ..v2017_05_01_preview.aio.operations import DiagnosticSettingsCategoryOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'diagnostic_settings_category'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def event_categories(self):
        """Instance depends on the API version:

           * 2015-04-01: :class:`EventCategoriesOperations<azure.mgmt.monitor.v2015_04_01.aio.operations.EventCategoriesOperations>`
        """
        api_version = self._get_api_version('event_categories')
        if api_version == '2015-04-01':
            from ..v2015_04_01.aio.operations import EventCategoriesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'event_categories'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def guest_diagnostics_settings(self):
        """Instance depends on the API version:

           * 2018-06-01-preview: :class:`GuestDiagnosticsSettingsOperations<azure.mgmt.monitor.v2018_06_01_preview.aio.operations.GuestDiagnosticsSettingsOperations>`
        """
        api_version = self._get_api_version('guest_diagnostics_settings')
        if api_version == '2018-06-01-preview':
            from ..v2018_06_01_preview.aio.operations import GuestDiagnosticsSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'guest_diagnostics_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def guest_diagnostics_settings_association(self):
        """Instance depends on the API version:

           * 2018-06-01-preview: :class:`GuestDiagnosticsSettingsAssociationOperations<azure.mgmt.monitor.v2018_06_01_preview.aio.operations.GuestDiagnosticsSettingsAssociationOperations>`
        """
        api_version = self._get_api_version('guest_diagnostics_settings_association')
        if api_version == '2018-06-01-preview':
            from ..v2018_06_01_preview.aio.operations import GuestDiagnosticsSettingsAssociationOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'guest_diagnostics_settings_association'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def log_profiles(self):
        """Instance depends on the API version:

           * 2016-03-01: :class:`LogProfilesOperations<azure.mgmt.monitor.v2016_03_01.aio.operations.LogProfilesOperations>`
        """
        api_version = self._get_api_version('log_profiles')
        if api_version == '2016-03-01':
            from ..v2016_03_01.aio.operations import LogProfilesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'log_profiles'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def management_group_diagnostic_settings(self):
        """Instance depends on the API version:

           * 2020-01-01-preview: :class:`ManagementGroupDiagnosticSettingsOperations<azure.mgmt.monitor.v2020_01_01_preview.aio.operations.ManagementGroupDiagnosticSettingsOperations>`
        """
        api_version = self._get_api_version('management_group_diagnostic_settings')
        if api_version == '2020-01-01-preview':
            from ..v2020_01_01_preview.aio.operations import ManagementGroupDiagnosticSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'management_group_diagnostic_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metric_alerts(self):
        """Instance depends on the API version:

           * 2018-03-01: :class:`MetricAlertsOperations<azure.mgmt.monitor.v2018_03_01.aio.operations.MetricAlertsOperations>`
        """
        api_version = self._get_api_version('metric_alerts')
        if api_version == '2018-03-01':
            from ..v2018_03_01.aio.operations import MetricAlertsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metric_alerts'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metric_alerts_status(self):
        """Instance depends on the API version:

           * 2018-03-01: :class:`MetricAlertsStatusOperations<azure.mgmt.monitor.v2018_03_01.aio.operations.MetricAlertsStatusOperations>`
        """
        api_version = self._get_api_version('metric_alerts_status')
        if api_version == '2018-03-01':
            from ..v2018_03_01.aio.operations import MetricAlertsStatusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metric_alerts_status'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metric_baseline(self):
        """Instance depends on the API version:

           * 2017-11-01-preview: :class:`MetricBaselineOperations<azure.mgmt.monitor.v2017_11_01_preview.aio.operations.MetricBaselineOperations>`
           * 2018-09-01: :class:`MetricBaselineOperations<azure.mgmt.monitor.v2018_09_01.aio.operations.MetricBaselineOperations>`
        """
        api_version = self._get_api_version('metric_baseline')
        if api_version == '2017-11-01-preview':
            from ..v2017_11_01_preview.aio.operations import MetricBaselineOperations as OperationClass
        elif api_version == '2018-09-01':
            from ..v2018_09_01.aio.operations import MetricBaselineOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metric_baseline'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metric_definitions(self):
        """Instance depends on the API version:

           * 2016-03-01: :class:`MetricDefinitionsOperations<azure.mgmt.monitor.v2016_03_01.aio.operations.MetricDefinitionsOperations>`
           * 2017-05-01-preview: :class:`MetricDefinitionsOperations<azure.mgmt.monitor.v2017_05_01_preview.aio.operations.MetricDefinitionsOperations>`
           * 2018-01-01: :class:`MetricDefinitionsOperations<azure.mgmt.monitor.v2018_01_01.aio.operations.MetricDefinitionsOperations>`
        """
        api_version = self._get_api_version('metric_definitions')
        if api_version == '2016-03-01':
            from ..v2016_03_01.aio.operations import MetricDefinitionsOperations as OperationClass
        elif api_version == '2017-05-01-preview':
            from ..v2017_05_01_preview.aio.operations import MetricDefinitionsOperations as OperationClass
        elif api_version == '2018-01-01':
            from ..v2018_01_01.aio.operations import MetricDefinitionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metric_definitions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metric_namespaces(self):
        """Instance depends on the API version:

           * 2017-12-01-preview: :class:`MetricNamespacesOperations<azure.mgmt.monitor.v2017_12_01_preview.aio.operations.MetricNamespacesOperations>`
        """
        api_version = self._get_api_version('metric_namespaces')
        if api_version == '2017-12-01-preview':
            from ..v2017_12_01_preview.aio.operations import MetricNamespacesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metric_namespaces'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def metrics(self):
        """Instance depends on the API version:

           * 2016-09-01: :class:`MetricsOperations<azure.mgmt.monitor.v2016_09_01.aio.operations.MetricsOperations>`
           * 2017-05-01-preview: :class:`MetricsOperations<azure.mgmt.monitor.v2017_05_01_preview.aio.operations.MetricsOperations>`
           * 2018-01-01: :class:`MetricsOperations<azure.mgmt.monitor.v2018_01_01.aio.operations.MetricsOperations>`
        """
        api_version = self._get_api_version('metrics')
        if api_version == '2016-09-01':
            from ..v2016_09_01.aio.operations import MetricsOperations as OperationClass
        elif api_version == '2017-05-01-preview':
            from ..v2017_05_01_preview.aio.operations import MetricsOperations as OperationClass
        elif api_version == '2018-01-01':
            from ..v2018_01_01.aio.operations import MetricsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'metrics'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2015-04-01: :class:`Operations<azure.mgmt.monitor.v2015_04_01.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2015-04-01':
            from ..v2015_04_01.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.monitor.v2019_10_17.aio.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2019-10-17-preview':
            from ..v2019_10_17.aio.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.monitor.v2019_10_17.aio.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2019-10-17-preview':
            from ..v2019_10_17.aio.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_scope_operation_status(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`PrivateLinkScopeOperationStatusOperations<azure.mgmt.monitor.v2019_10_17.aio.operations.PrivateLinkScopeOperationStatusOperations>`
        """
        api_version = self._get_api_version('private_link_scope_operation_status')
        if api_version == '2019-10-17-preview':
            from ..v2019_10_17.aio.operations import PrivateLinkScopeOperationStatusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_scope_operation_status'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_scoped_resources(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`PrivateLinkScopedResourcesOperations<azure.mgmt.monitor.v2019_10_17.aio.operations.PrivateLinkScopedResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_scoped_resources')
        if api_version == '2019-10-17-preview':
            from ..v2019_10_17.aio.operations import PrivateLinkScopedResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_scoped_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_scopes(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`PrivateLinkScopesOperations<azure.mgmt.monitor.v2019_10_17.aio.operations.PrivateLinkScopesOperations>`
        """
        api_version = self._get_api_version('private_link_scopes')
        if api_version == '2019-10-17-preview':
            from ..v2019_10_17.aio.operations import PrivateLinkScopesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_scopes'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def scheduled_query_rules(self):
        """Instance depends on the API version:

           * 2018-04-16: :class:`ScheduledQueryRulesOperations<azure.mgmt.monitor.v2018_04_16.aio.operations.ScheduledQueryRulesOperations>`
           * 2020-05-01-preview: :class:`ScheduledQueryRulesOperations<azure.mgmt.monitor.v2020_05_01_preview.aio.operations.ScheduledQueryRulesOperations>`
        """
        api_version = self._get_api_version('scheduled_query_rules')
        if api_version == '2018-04-16':
            from ..v2018_04_16.aio.operations import ScheduledQueryRulesOperations as OperationClass
        elif api_version == '2020-05-01-preview':
            from ..v2020_05_01_preview.aio.operations import ScheduledQueryRulesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'scheduled_query_rules'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def service_diagnostic_settings(self):
        """Instance depends on the API version:

           * 2015-07-01: :class:`ServiceDiagnosticSettingsOperations<azure.mgmt.monitor.v2015_07_01.aio.operations.ServiceDiagnosticSettingsOperations>`
           * 2016-09-01: :class:`ServiceDiagnosticSettingsOperations<azure.mgmt.monitor.v2016_09_01.aio.operations.ServiceDiagnosticSettingsOperations>`
        """
        api_version = self._get_api_version('service_diagnostic_settings')
        if api_version == '2015-07-01':
            from ..v2015_07_01.aio.operations import ServiceDiagnosticSettingsOperations as OperationClass
        elif api_version == '2016-09-01':
            from ..v2016_09_01.aio.operations import ServiceDiagnosticSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'service_diagnostic_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def subscription_diagnostic_settings(self):
        """Instance depends on the API version:

           * 2017-05-01-preview: :class:`SubscriptionDiagnosticSettingsOperations<azure.mgmt.monitor.v2017_05_01_preview.aio.operations.SubscriptionDiagnosticSettingsOperations>`
        """
        api_version = self._get_api_version('subscription_diagnostic_settings')
        if api_version == '2017-05-01-preview':
            from ..v2017_05_01_preview.aio.operations import SubscriptionDiagnosticSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'subscription_diagnostic_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tenant_activity_logs(self):
        """Instance depends on the API version:

           * 2015-04-01: :class:`TenantActivityLogsOperations<azure.mgmt.monitor.v2015_04_01.aio.operations.TenantActivityLogsOperations>`
        """
        api_version = self._get_api_version('tenant_activity_logs')
        if api_version == '2015-04-01':
            from ..v2015_04_01.aio.operations import TenantActivityLogsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'tenant_activity_logs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def vm_insights(self):
        """Instance depends on the API version:

           * 2018-11-27-preview: :class:`VMInsightsOperations<azure.mgmt.monitor.v2018_11_27_preview.aio.operations.VMInsightsOperations>`
        """
        api_version = self._get_api_version('vm_insights')
        if api_version == '2018-11-27-preview':
            from ..v2018_11_27_preview.aio.operations import VMInsightsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'vm_insights'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
