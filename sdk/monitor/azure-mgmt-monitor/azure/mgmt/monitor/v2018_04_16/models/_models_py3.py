# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._monitor_client_enums import *


class Action(msrest.serialization.Model):
    """Action descriptor.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AlertingAction, LogToMetricAction.

    All required parameters must be populated in order to send to Azure.

    :param odata_type: Required. Specifies the action. Supported values - AlertingAction,
     LogToMetricAction.Constant filled by server.
    :type odata_type: str
    """

    _validation = {
        'odata_type': {'required': True},
    }

    _attribute_map = {
        'odata_type': {'key': 'odata\\.type', 'type': 'str'},
    }

    _subtype_map = {
        'odata_type': {'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction': 'AlertingAction', 'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction': 'LogToMetricAction'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Action, self).__init__(**kwargs)
        self.odata_type = None  # type: Optional[str]


class AlertingAction(Action):
    """Specify action need to be taken when rule type is Alert.

    All required parameters must be populated in order to send to Azure.

    :param odata_type: Required. Specifies the action. Supported values - AlertingAction,
     LogToMetricAction.Constant filled by server.
    :type odata_type: str
    :param severity: Required. Severity of the alert. Possible values include: "0", "1", "2", "3",
     "4".
    :type severity: str or ~$(python-base-namespace).v2018_04_16.models.AlertSeverity
    :param azns_action: Azure action group reference.
    :type azns_action: ~$(python-base-namespace).v2018_04_16.models.AzNsActionGroup
    :param throttling_in_min: time (in minutes) for which Alerts should be throttled or suppressed.
    :type throttling_in_min: int
    :param trigger: Required. The trigger condition that results in the alert rule being.
    :type trigger: ~$(python-base-namespace).v2018_04_16.models.TriggerCondition
    """

    _validation = {
        'odata_type': {'required': True},
        'severity': {'required': True},
        'trigger': {'required': True},
    }

    _attribute_map = {
        'odata_type': {'key': 'odata\\.type', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'str'},
        'azns_action': {'key': 'aznsAction', 'type': 'AzNsActionGroup'},
        'throttling_in_min': {'key': 'throttlingInMin', 'type': 'int'},
        'trigger': {'key': 'trigger', 'type': 'TriggerCondition'},
    }

    def __init__(
        self,
        *,
        severity: Union[str, "AlertSeverity"],
        trigger: "TriggerCondition",
        azns_action: Optional["AzNsActionGroup"] = None,
        throttling_in_min: Optional[int] = None,
        **kwargs
    ):
        super(AlertingAction, self).__init__(**kwargs)
        self.odata_type = 'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction'  # type: str
        self.severity = severity
        self.azns_action = azns_action
        self.throttling_in_min = throttling_in_min
        self.trigger = trigger


class AzNsActionGroup(msrest.serialization.Model):
    """Azure action group.

    :param action_group: Azure Action Group reference.
    :type action_group: list[str]
    :param email_subject: Custom subject override for all email ids in Azure action group.
    :type email_subject: str
    :param custom_webhook_payload: Custom payload to be sent for all webhook URI in Azure action
     group.
    :type custom_webhook_payload: str
    """

    _attribute_map = {
        'action_group': {'key': 'actionGroup', 'type': '[str]'},
        'email_subject': {'key': 'emailSubject', 'type': 'str'},
        'custom_webhook_payload': {'key': 'customWebhookPayload', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        action_group: Optional[List[str]] = None,
        email_subject: Optional[str] = None,
        custom_webhook_payload: Optional[str] = None,
        **kwargs
    ):
        super(AzNsActionGroup, self).__init__(**kwargs)
        self.action_group = action_group
        self.email_subject = email_subject
        self.custom_webhook_payload = custom_webhook_payload


class Criteria(msrest.serialization.Model):
    """Specifies the criteria for converting log to metric.

    All required parameters must be populated in order to send to Azure.

    :param metric_name: Required. Name of the metric.
    :type metric_name: str
    :param dimensions: List of Dimensions for creating metric.
    :type dimensions: list[~$(python-base-namespace).v2018_04_16.models.Dimension]
    """

    _validation = {
        'metric_name': {'required': True},
    }

    _attribute_map = {
        'metric_name': {'key': 'metricName', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[Dimension]'},
    }

    def __init__(
        self,
        *,
        metric_name: str,
        dimensions: Optional[List["Dimension"]] = None,
        **kwargs
    ):
        super(Criteria, self).__init__(**kwargs)
        self.metric_name = metric_name
        self.dimensions = dimensions


class Dimension(msrest.serialization.Model):
    """Specifies the criteria for converting log to metric.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the dimension.
    :type name: str
    :param operator: Required. Operator for dimension values. Possible values include: "Include".
    :type operator: str or ~$(python-base-namespace).v2018_04_16.models.Operator
    :param values: Required. List of dimension values.
    :type values: list[str]
    """

    _validation = {
        'name': {'required': True},
        'operator': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        name: str,
        operator: Union[str, "Operator"],
        values: List[str],
        **kwargs
    ):
        super(Dimension, self).__init__(**kwargs)
        self.name = name
        self.operator = operator
        self.values = values


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class LogMetricTrigger(msrest.serialization.Model):
    """A log metrics trigger descriptor.

    :param threshold_operator: Evaluation operation for Metric -'GreaterThan' or 'LessThan' or
     'Equal'. Possible values include: "GreaterThanOrEqual", "LessThanOrEqual", "GreaterThan",
     "LessThan", "Equal".
    :type threshold_operator: str or ~$(python-base-
     namespace).v2018_04_16.models.ConditionalOperator
    :param threshold: The threshold of the metric trigger.
    :type threshold: float
    :param metric_trigger_type: Metric Trigger Type - 'Consecutive' or 'Total'. Possible values
     include: "Consecutive", "Total".
    :type metric_trigger_type: str or ~$(python-base-
     namespace).v2018_04_16.models.MetricTriggerType
    :param metric_column: Evaluation of metric on a particular column.
    :type metric_column: str
    """

    _attribute_map = {
        'threshold_operator': {'key': 'thresholdOperator', 'type': 'str'},
        'threshold': {'key': 'threshold', 'type': 'float'},
        'metric_trigger_type': {'key': 'metricTriggerType', 'type': 'str'},
        'metric_column': {'key': 'metricColumn', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        threshold_operator: Optional[Union[str, "ConditionalOperator"]] = None,
        threshold: Optional[float] = None,
        metric_trigger_type: Optional[Union[str, "MetricTriggerType"]] = None,
        metric_column: Optional[str] = None,
        **kwargs
    ):
        super(LogMetricTrigger, self).__init__(**kwargs)
        self.threshold_operator = threshold_operator
        self.threshold = threshold
        self.metric_trigger_type = metric_trigger_type
        self.metric_column = metric_column


class Resource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar kind: Metadata used by portal/tooling/etc to render different UX experiences for
     resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported,
     the resource provider must validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the response body, it must
     also be provided as a header per the normal etag convention.  Entity tags are used for
     comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in
     the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range
     (section 14.27) header fields.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'kind': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
        self.kind = None
        self.etag = None


class LogSearchRuleResource(Resource):
    """The Log Search Rule resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :ivar kind: Metadata used by portal/tooling/etc to render different UX experiences for
     resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported,
     the resource provider must validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the response body, it must
     also be provided as a header per the normal etag convention.  Entity tags are used for
     comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in
     the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range
     (section 14.27) header fields.
    :vartype etag: str
    :param description: The description of the Log Search rule.
    :type description: str
    :param display_name: The display name of the alert rule.
    :type display_name: str
    :param enabled: The flag which indicates whether the Log Search rule is enabled. Value should
     be true or false. Possible values include: "true", "false".
    :type enabled: str or ~$(python-base-namespace).v2018_04_16.models.Enabled
    :ivar last_updated_time: Last time the rule was updated in IS08601 format.
    :vartype last_updated_time: ~datetime.datetime
    :ivar provisioning_state: Provisioning state of the scheduled query rule. Possible values
     include: "Succeeded", "Deploying", "Canceled", "Failed".
    :vartype provisioning_state: str or ~$(python-base-
     namespace).v2018_04_16.models.ProvisioningState
    :param source: Required. Data Source against which rule will Query Data.
    :type source: ~$(python-base-namespace).v2018_04_16.models.Source
    :param schedule: Schedule (Frequency, Time Window) for rule. Required for action type -
     AlertingAction.
    :type schedule: ~$(python-base-namespace).v2018_04_16.models.Schedule
    :param action: Required. Action needs to be taken on rule execution.
    :type action: ~$(python-base-namespace).v2018_04_16.models.Action
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'kind': {'readonly': True},
        'etag': {'readonly': True},
        'last_updated_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'source': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'str'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'source': {'key': 'properties.source', 'type': 'Source'},
        'schedule': {'key': 'properties.schedule', 'type': 'Schedule'},
        'action': {'key': 'properties.action', 'type': 'Action'},
    }

    def __init__(
        self,
        *,
        location: str,
        source: "Source",
        action: "Action",
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        enabled: Optional[Union[str, "Enabled"]] = None,
        schedule: Optional["Schedule"] = None,
        **kwargs
    ):
        super(LogSearchRuleResource, self).__init__(location=location, tags=tags, **kwargs)
        self.description = description
        self.display_name = display_name
        self.enabled = enabled
        self.last_updated_time = None
        self.provisioning_state = None
        self.source = source
        self.schedule = schedule
        self.action = action


class LogSearchRuleResourceCollection(msrest.serialization.Model):
    """Represents a collection of Log Search rule resources.

    :param value: The values for the Log Search Rule resources.
    :type value: list[~$(python-base-namespace).v2018_04_16.models.LogSearchRuleResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[LogSearchRuleResource]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["LogSearchRuleResource"]] = None,
        **kwargs
    ):
        super(LogSearchRuleResourceCollection, self).__init__(**kwargs)
        self.value = value


class LogSearchRuleResourcePatch(msrest.serialization.Model):
    """The log search rule resource for patch operations.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param enabled: The flag which indicates whether the Log Search rule is enabled. Value should
     be true or false. Possible values include: "true", "false".
    :type enabled: str or ~$(python-base-namespace).v2018_04_16.models.Enabled
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        enabled: Optional[Union[str, "Enabled"]] = None,
        **kwargs
    ):
        super(LogSearchRuleResourcePatch, self).__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class LogToMetricAction(Action):
    """Specify action need to be taken when rule type is converting log to metric.

    All required parameters must be populated in order to send to Azure.

    :param odata_type: Required. Specifies the action. Supported values - AlertingAction,
     LogToMetricAction.Constant filled by server.
    :type odata_type: str
    :param criteria: Required. Criteria of Metric.
    :type criteria: list[~$(python-base-namespace).v2018_04_16.models.Criteria]
    """

    _validation = {
        'odata_type': {'required': True},
        'criteria': {'required': True},
    }

    _attribute_map = {
        'odata_type': {'key': 'odata\\.type', 'type': 'str'},
        'criteria': {'key': 'criteria', 'type': '[Criteria]'},
    }

    def __init__(
        self,
        *,
        criteria: List["Criteria"],
        **kwargs
    ):
        super(LogToMetricAction, self).__init__(**kwargs)
        self.odata_type = 'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction'  # type: str
        self.criteria = criteria


class Schedule(msrest.serialization.Model):
    """Defines how often to run the search and the time interval.

    All required parameters must be populated in order to send to Azure.

    :param frequency_in_minutes: Required. frequency (in minutes) at which rule condition should be
     evaluated.
    :type frequency_in_minutes: int
    :param time_window_in_minutes: Required. Time window for which data needs to be fetched for
     query (should be greater than or equal to frequencyInMinutes).
    :type time_window_in_minutes: int
    """

    _validation = {
        'frequency_in_minutes': {'required': True},
        'time_window_in_minutes': {'required': True},
    }

    _attribute_map = {
        'frequency_in_minutes': {'key': 'frequencyInMinutes', 'type': 'int'},
        'time_window_in_minutes': {'key': 'timeWindowInMinutes', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        frequency_in_minutes: int,
        time_window_in_minutes: int,
        **kwargs
    ):
        super(Schedule, self).__init__(**kwargs)
        self.frequency_in_minutes = frequency_in_minutes
        self.time_window_in_minutes = time_window_in_minutes


class Source(msrest.serialization.Model):
    """Specifies the log search query.

    All required parameters must be populated in order to send to Azure.

    :param query: Log search query. Required for action type - AlertingAction.
    :type query: str
    :param authorized_resources: List of  Resource referred into query.
    :type authorized_resources: list[str]
    :param data_source_id: Required. The resource uri over which log search query is to be run.
    :type data_source_id: str
    :param query_type: Set value to 'ResultCount' . Possible values include: "ResultCount".
    :type query_type: str or ~$(python-base-namespace).v2018_04_16.models.QueryType
    """

    _validation = {
        'data_source_id': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'authorized_resources': {'key': 'authorizedResources', 'type': '[str]'},
        'data_source_id': {'key': 'dataSourceId', 'type': 'str'},
        'query_type': {'key': 'queryType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        data_source_id: str,
        query: Optional[str] = None,
        authorized_resources: Optional[List[str]] = None,
        query_type: Optional[Union[str, "QueryType"]] = None,
        **kwargs
    ):
        super(Source, self).__init__(**kwargs)
        self.query = query
        self.authorized_resources = authorized_resources
        self.data_source_id = data_source_id
        self.query_type = query_type


class TriggerCondition(msrest.serialization.Model):
    """The condition that results in the Log Search rule.

    All required parameters must be populated in order to send to Azure.

    :param threshold_operator: Required. Evaluation operation for rule - 'GreaterThan' or
     'LessThan. Possible values include: "GreaterThanOrEqual", "LessThanOrEqual", "GreaterThan",
     "LessThan", "Equal".
    :type threshold_operator: str or ~$(python-base-
     namespace).v2018_04_16.models.ConditionalOperator
    :param threshold: Required. Result or count threshold based on which rule should be triggered.
    :type threshold: float
    :param metric_trigger: Trigger condition for metric query rule.
    :type metric_trigger: ~$(python-base-namespace).v2018_04_16.models.LogMetricTrigger
    """

    _validation = {
        'threshold_operator': {'required': True},
        'threshold': {'required': True},
    }

    _attribute_map = {
        'threshold_operator': {'key': 'thresholdOperator', 'type': 'str'},
        'threshold': {'key': 'threshold', 'type': 'float'},
        'metric_trigger': {'key': 'metricTrigger', 'type': 'LogMetricTrigger'},
    }

    def __init__(
        self,
        *,
        threshold_operator: Union[str, "ConditionalOperator"],
        threshold: float,
        metric_trigger: Optional["LogMetricTrigger"] = None,
        **kwargs
    ):
        super(TriggerCondition, self).__init__(**kwargs)
        self.threshold_operator = threshold_operator
        self.threshold = threshold
        self.metric_trigger = metric_trigger
