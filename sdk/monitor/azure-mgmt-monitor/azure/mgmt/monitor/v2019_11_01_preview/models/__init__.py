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

try:
    from ._models_py3 import AzureMonitorMetricsDestination
    from ._models_py3 import DataCollectionRule
    from ._models_py3 import DataCollectionRuleAssociation
    from ._models_py3 import DataCollectionRuleAssociationProxyOnlyResource
    from ._models_py3 import DataCollectionRuleDataSources
    from ._models_py3 import DataCollectionRuleDestinations
    from ._models_py3 import DataCollectionRuleResource
    from ._models_py3 import DataFlow
    from ._models_py3 import DataSourcesSpec
    from ._models_py3 import DestinationsSpec
    from ._models_py3 import DestinationsSpecAzureMonitorMetrics
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ErrorResponseError
    from ._models_py3 import ExtensionDataSource
    from ._models_py3 import LogAnalyticsDestination
    from ._models_py3 import PerfCounterDataSource
    from ._models_py3 import ResourceForUpdate
    from ._models_py3 import SyslogDataSource
    from ._models_py3 import WindowsEventLogDataSource
except (SyntaxError, ImportError):
    from ._models import AzureMonitorMetricsDestination
    from ._models import DataCollectionRule
    from ._models import DataCollectionRuleAssociation
    from ._models import DataCollectionRuleAssociationProxyOnlyResource
    from ._models import DataCollectionRuleDataSources
    from ._models import DataCollectionRuleDestinations
    from ._models import DataCollectionRuleResource
    from ._models import DataFlow
    from ._models import DataSourcesSpec
    from ._models import DestinationsSpec
    from ._models import DestinationsSpecAzureMonitorMetrics
    from ._models import ErrorAdditionalInfo
    from ._models import ErrorDetails
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ErrorResponseError
    from ._models import ExtensionDataSource
    from ._models import LogAnalyticsDestination
    from ._models import PerfCounterDataSource
    from ._models import ResourceForUpdate
    from ._models import SyslogDataSource
    from ._models import WindowsEventLogDataSource
from ._paged_models import DataCollectionRuleAssociationProxyOnlyResourcePaged
from ._paged_models import DataCollectionRuleResourcePaged
from ._monitor_management_client_enums import (
    KnownDataCollectionRuleAssociationProvisioningState,
    KnownPerfCounterDataSourceStreams,
    KnownPerfCounterDataSourceScheduledTransferPeriod,
    KnownWindowsEventLogDataSourceStreams,
    KnownWindowsEventLogDataSourceScheduledTransferPeriod,
    KnownSyslogDataSourceStreams,
    KnownSyslogDataSourceFacilityNames,
    KnownSyslogDataSourceLogLevels,
    KnownExtensionDataSourceStreams,
    KnownDataFlowStreams,
    KnownDataCollectionRuleProvisioningState,
)

__all__ = [
    'AzureMonitorMetricsDestination',
    'DataCollectionRule',
    'DataCollectionRuleAssociation',
    'DataCollectionRuleAssociationProxyOnlyResource',
    'DataCollectionRuleDataSources',
    'DataCollectionRuleDestinations',
    'DataCollectionRuleResource',
    'DataFlow',
    'DataSourcesSpec',
    'DestinationsSpec',
    'DestinationsSpecAzureMonitorMetrics',
    'ErrorAdditionalInfo',
    'ErrorDetails',
    'ErrorResponse', 'ErrorResponseException',
    'ErrorResponseError',
    'ExtensionDataSource',
    'LogAnalyticsDestination',
    'PerfCounterDataSource',
    'ResourceForUpdate',
    'SyslogDataSource',
    'WindowsEventLogDataSource',
    'DataCollectionRuleAssociationProxyOnlyResourcePaged',
    'DataCollectionRuleResourcePaged',
    'KnownDataCollectionRuleAssociationProvisioningState',
    'KnownPerfCounterDataSourceStreams',
    'KnownPerfCounterDataSourceScheduledTransferPeriod',
    'KnownWindowsEventLogDataSourceStreams',
    'KnownWindowsEventLogDataSourceScheduledTransferPeriod',
    'KnownSyslogDataSourceStreams',
    'KnownSyslogDataSourceFacilityNames',
    'KnownSyslogDataSourceLogLevels',
    'KnownExtensionDataSourceStreams',
    'KnownDataFlowStreams',
    'KnownDataCollectionRuleProvisioningState',
]
