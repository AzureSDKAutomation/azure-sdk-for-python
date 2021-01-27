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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Action(Model):
    """Action descriptor.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AlertingAction, LogToMetricAction

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction': 'AlertingAction', 'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction': 'LogToMetricAction'}
    }

    def __init__(self, **kwargs):
        super(Action, self).__init__(**kwargs)
        self.odatatype = None


class AlertingAction(Action):
    """Specify action need to be taken when rule type is Alert.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param severity: Required. Severity of the alert. Possible values include:
     '0', '1', '2', '3', '4'
    :type severity: str or
     ~azure.mgmt.monitor.v2018_04_16.models.AlertSeverity
    :param azns_action: Azure action group reference.
    :type azns_action: ~azure.mgmt.monitor.v2018_04_16.models.AzNsActionGroup
    :param throttling_in_min: time (in minutes) for which Alerts should be
     throttled or suppressed.
    :type throttling_in_min: int
    :param trigger: Required. The trigger condition that results in the alert
     rule being.
    :type trigger: ~azure.mgmt.monitor.v2018_04_16.models.TriggerCondition
    """

    _validation = {
        'odatatype': {'required': True},
        'severity': {'required': True},
        'trigger': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'str'},
        'azns_action': {'key': 'aznsAction', 'type': 'AzNsActionGroup'},
        'throttling_in_min': {'key': 'throttlingInMin', 'type': 'int'},
        'trigger': {'key': 'trigger', 'type': 'TriggerCondition'},
    }

    def __init__(self, **kwargs):
        super(AlertingAction, self).__init__(**kwargs)
        self.severity = kwargs.get('severity', None)
        self.azns_action = kwargs.get('azns_action', None)
        self.throttling_in_min = kwargs.get('throttling_in_min', None)
        self.trigger = kwargs.get('trigger', None)
        self.odatatype = 'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction'


class AzNsActionGroup(Model):
    """Azure action group.

    :param action_group: Azure Action Group reference.
    :type action_group: list[str]
    :param email_subject: Custom subject override for all email ids in Azure
     action group
    :type email_subject: str
    :param custom_webhook_payload: Custom payload to be sent for all webhook
     URI in Azure action group
    :type custom_webhook_payload: str
    """

    _attribute_map = {
        'action_group': {'key': 'actionGroup', 'type': '[str]'},
        'email_subject': {'key': 'emailSubject', 'type': 'str'},
        'custom_webhook_payload': {'key': 'customWebhookPayload', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzNsActionGroup, self).__init__(**kwargs)
        self.action_group = kwargs.get('action_group', None)
        self.email_subject = kwargs.get('email_subject', None)
        self.custom_webhook_payload = kwargs.get('custom_webhook_payload', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Criteria(Model):
    """Specifies the criteria for converting log to metric.

    All required parameters must be populated in order to send to Azure.

    :param metric_name: Required. Name of the metric
    :type metric_name: str
    :param dimensions: List of Dimensions for creating metric
    :type dimensions: list[~azure.mgmt.monitor.v2018_04_16.models.Dimension]
    """

    _validation = {
        'metric_name': {'required': True},
    }

    _attribute_map = {
        'metric_name': {'key': 'metricName', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[Dimension]'},
    }

    def __init__(self, **kwargs):
        super(Criteria, self).__init__(**kwargs)
        self.metric_name = kwargs.get('metric_name', None)
        self.dimensions = kwargs.get('dimensions', None)


class Dimension(Model):
    """Specifies the criteria for converting log to metric.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the dimension
    :type name: str
    :ivar operator: Required. Operator for dimension values. Default value:
     "Include" .
    :vartype operator: str
    :param values: Required. List of dimension values
    :type values: list[str]
    """

    _validation = {
        'name': {'required': True},
        'operator': {'required': True, 'constant': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    operator = "Include"

    def __init__(self, **kwargs):
        super(Dimension, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.values = kwargs.get('values', None)


class ErrorContract(Model):
    """Describes the format of Error response.

    :param error: The error details.
    :type error: ~azure.mgmt.monitor.v2018_04_16.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, **kwargs):
        super(ErrorContract, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorContractException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorContract'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorContractException, self).__init__(deserialize, response, 'ErrorContract', *args)


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class LogMetricTrigger(Model):
    """A log metrics trigger descriptor.

    :param threshold_operator: Evaluation operation for Metric -'GreaterThan'
     or 'LessThan' or 'Equal'. Possible values include: 'GreaterThanOrEqual',
     'LessThanOrEqual', 'GreaterThan', 'LessThan', 'Equal'. Default value:
     "GreaterThanOrEqual" .
    :type threshold_operator: str or
     ~azure.mgmt.monitor.v2018_04_16.models.ConditionalOperator
    :param threshold: The threshold of the metric trigger.
    :type threshold: float
    :param metric_trigger_type: Metric Trigger Type - 'Consecutive' or
     'Total'. Possible values include: 'Consecutive', 'Total'. Default value:
     "Consecutive" .
    :type metric_trigger_type: str or
     ~azure.mgmt.monitor.v2018_04_16.models.MetricTriggerType
    :param metric_column: Evaluation of metric on a particular column
    :type metric_column: str
    """

    _attribute_map = {
        'threshold_operator': {'key': 'thresholdOperator', 'type': 'str'},
        'threshold': {'key': 'threshold', 'type': 'float'},
        'metric_trigger_type': {'key': 'metricTriggerType', 'type': 'str'},
        'metric_column': {'key': 'metricColumn', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LogMetricTrigger, self).__init__(**kwargs)
        self.threshold_operator = kwargs.get('threshold_operator', "GreaterThanOrEqual")
        self.threshold = kwargs.get('threshold', None)
        self.metric_trigger_type = kwargs.get('metric_trigger_type', "Consecutive")
        self.metric_column = kwargs.get('metric_column', None)


class Resource(Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar kind: Metadata used by portal/tooling/etc to render different UX
     experiences for resources of the same type; e.g. ApiApps are a kind of
     Microsoft.Web/sites type.  If supported, the resource provider must
     validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the
     response body, it must also be provided as a header per the normal etag
     convention.  Entity tags are used for comparing two or more entities from
     the same requested resource. HTTP/1.1 uses entity tags in the etag
     (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26),
     and If-Range (section 14.27) header fields.
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

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.kind = None
        self.etag = None


class LogSearchRuleResource(Resource):
    """The Log Search Rule resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar kind: Metadata used by portal/tooling/etc to render different UX
     experiences for resources of the same type; e.g. ApiApps are a kind of
     Microsoft.Web/sites type.  If supported, the resource provider must
     validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the
     response body, it must also be provided as a header per the normal etag
     convention.  Entity tags are used for comparing two or more entities from
     the same requested resource. HTTP/1.1 uses entity tags in the etag
     (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26),
     and If-Range (section 14.27) header fields.
    :vartype etag: str
    :param description: The description of the Log Search rule.
    :type description: str
    :param display_name: The display name of the alert rule
    :type display_name: str
    :param enabled: The flag which indicates whether the Log Search rule is
     enabled. Value should be true or false. Possible values include: 'true',
     'false'
    :type enabled: str or ~azure.mgmt.monitor.v2018_04_16.models.Enabled
    :ivar last_updated_time: Last time the rule was updated in IS08601 format.
    :vartype last_updated_time: datetime
    :ivar provisioning_state: Provisioning state of the scheduled query rule.
     Possible values include: 'Succeeded', 'Deploying', 'Canceled', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.monitor.v2018_04_16.models.ProvisioningState
    :param source: Required. Data Source against which rule will Query Data
    :type source: ~azure.mgmt.monitor.v2018_04_16.models.Source
    :param schedule: Schedule (Frequency, Time Window) for rule. Required for
     action type - AlertingAction
    :type schedule: ~azure.mgmt.monitor.v2018_04_16.models.Schedule
    :param action: Required. Action needs to be taken on rule execution.
    :type action: ~azure.mgmt.monitor.v2018_04_16.models.Action
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

    def __init__(self, **kwargs):
        super(LogSearchRuleResource, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.display_name = kwargs.get('display_name', None)
        self.enabled = kwargs.get('enabled', None)
        self.last_updated_time = None
        self.provisioning_state = None
        self.source = kwargs.get('source', None)
        self.schedule = kwargs.get('schedule', None)
        self.action = kwargs.get('action', None)


class LogSearchRuleResourcePatch(Model):
    """The log search rule resource for patch operations.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param enabled: The flag which indicates whether the Log Search rule is
     enabled. Value should be true or false. Possible values include: 'true',
     'false'
    :type enabled: str or ~azure.mgmt.monitor.v2018_04_16.models.Enabled
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LogSearchRuleResourcePatch, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.enabled = kwargs.get('enabled', None)


class LogToMetricAction(Action):
    """Specify action need to be taken when rule type is converting log to metric.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param criteria: Required. Criteria of Metric
    :type criteria: list[~azure.mgmt.monitor.v2018_04_16.models.Criteria]
    """

    _validation = {
        'odatatype': {'required': True},
        'criteria': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'criteria': {'key': 'criteria', 'type': '[Criteria]'},
    }

    def __init__(self, **kwargs):
        super(LogToMetricAction, self).__init__(**kwargs)
        self.criteria = kwargs.get('criteria', None)
        self.odatatype = 'Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction'


class Schedule(Model):
    """Defines how often to run the search and the time interval.

    All required parameters must be populated in order to send to Azure.

    :param frequency_in_minutes: Required. frequency (in minutes) at which
     rule condition should be evaluated.
    :type frequency_in_minutes: int
    :param time_window_in_minutes: Required. Time window for which data needs
     to be fetched for query (should be greater than or equal to
     frequencyInMinutes).
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

    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        self.frequency_in_minutes = kwargs.get('frequency_in_minutes', None)
        self.time_window_in_minutes = kwargs.get('time_window_in_minutes', None)


class Source(Model):
    """Specifies the log search query.

    All required parameters must be populated in order to send to Azure.

    :param query: Log search query. Required for action type - AlertingAction
    :type query: str
    :param authorized_resources: List of  Resource referred into query
    :type authorized_resources: list[str]
    :param data_source_id: Required. The resource uri over which log search
     query is to be run.
    :type data_source_id: str
    :param query_type: Set value to 'ResultCount'. Possible values include:
     'ResultCount'
    :type query_type: str or ~azure.mgmt.monitor.v2018_04_16.models.QueryType
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

    def __init__(self, **kwargs):
        super(Source, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.authorized_resources = kwargs.get('authorized_resources', None)
        self.data_source_id = kwargs.get('data_source_id', None)
        self.query_type = kwargs.get('query_type', None)


class TriggerCondition(Model):
    """The condition that results in the Log Search rule.

    All required parameters must be populated in order to send to Azure.

    :param threshold_operator: Required. Evaluation operation for rule -
     'GreaterThan' or 'LessThan. Possible values include: 'GreaterThanOrEqual',
     'LessThanOrEqual', 'GreaterThan', 'LessThan', 'Equal'. Default value:
     "GreaterThanOrEqual" .
    :type threshold_operator: str or
     ~azure.mgmt.monitor.v2018_04_16.models.ConditionalOperator
    :param threshold: Required. Result or count threshold based on which rule
     should be triggered.
    :type threshold: float
    :param metric_trigger: Trigger condition for metric query rule
    :type metric_trigger:
     ~azure.mgmt.monitor.v2018_04_16.models.LogMetricTrigger
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

    def __init__(self, **kwargs):
        super(TriggerCondition, self).__init__(**kwargs)
        self.threshold_operator = kwargs.get('threshold_operator', "GreaterThanOrEqual")
        self.threshold = kwargs.get('threshold', None)
        self.metric_trigger = kwargs.get('metric_trigger', None)
