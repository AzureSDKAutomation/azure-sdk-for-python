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


class HttpAuthentication(Model):
    """HttpAuthentication.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ClientCertAuthentication, BasicAuthentication,
    OAuthAuthentication

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'ClientCertificate': 'ClientCertAuthentication', 'Basic': 'BasicAuthentication', 'ActiveDirectoryOAuth': 'OAuthAuthentication'}
    }

    def __init__(self, **kwargs):
        super(HttpAuthentication, self).__init__(**kwargs)
        self.type = None


class BasicAuthentication(HttpAuthentication):
    """BasicAuthentication.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param username: Gets or sets the username.
    :type username: str
    :param password: Gets or sets the password, return value will always be
     empty.
    :type password: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BasicAuthentication, self).__init__(**kwargs)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.type = 'Basic'


class ClientCertAuthentication(HttpAuthentication):
    """ClientCertAuthentication.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param password: Gets or sets the certificate password, return value will
     always be empty.
    :type password: str
    :param pfx: Gets or sets the pfx certificate. Accepts certification in
     base64 encoding, return value will always be empty.
    :type pfx: str
    :param certificate_thumbprint: Gets or sets the certificate thumbprint.
    :type certificate_thumbprint: str
    :param certificate_expiration_date: Gets or sets the certificate
     expiration date.
    :type certificate_expiration_date: datetime
    :param certificate_subject_name: Gets or sets the certificate subject
     name.
    :type certificate_subject_name: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'pfx': {'key': 'pfx', 'type': 'str'},
        'certificate_thumbprint': {'key': 'certificateThumbprint', 'type': 'str'},
        'certificate_expiration_date': {'key': 'certificateExpirationDate', 'type': 'iso-8601'},
        'certificate_subject_name': {'key': 'certificateSubjectName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ClientCertAuthentication, self).__init__(**kwargs)
        self.password = kwargs.get('password', None)
        self.pfx = kwargs.get('pfx', None)
        self.certificate_thumbprint = kwargs.get('certificate_thumbprint', None)
        self.certificate_expiration_date = kwargs.get('certificate_expiration_date', None)
        self.certificate_subject_name = kwargs.get('certificate_subject_name', None)
        self.type = 'ClientCertificate'


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class HttpRequest(Model):
    """HttpRequest.

    :param authentication: Gets or sets the authentication method of the
     request.
    :type authentication: ~azure.mgmt.scheduler.models.HttpAuthentication
    :param uri: Gets or sets the URI of the request.
    :type uri: str
    :param method: Gets or sets the method of the request.
    :type method: str
    :param body: Gets or sets the request body.
    :type body: str
    :param headers: Gets or sets the headers.
    :type headers: dict[str, str]
    """

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'HttpAuthentication'},
        'uri': {'key': 'uri', 'type': 'str'},
        'method': {'key': 'method', 'type': 'str'},
        'body': {'key': 'body', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(HttpRequest, self).__init__(**kwargs)
        self.authentication = kwargs.get('authentication', None)
        self.uri = kwargs.get('uri', None)
        self.method = kwargs.get('method', None)
        self.body = kwargs.get('body', None)
        self.headers = kwargs.get('headers', None)


class JobAction(Model):
    """JobAction.

    :param type: Gets or sets the job action type. Possible values include:
     'Http', 'Https', 'StorageQueue', 'ServiceBusQueue', 'ServiceBusTopic'
    :type type: str or ~azure.mgmt.scheduler.models.JobActionType
    :param request: Gets or sets the http requests.
    :type request: ~azure.mgmt.scheduler.models.HttpRequest
    :param queue_message: Gets or sets the storage queue message.
    :type queue_message: ~azure.mgmt.scheduler.models.StorageQueueMessage
    :param service_bus_queue_message: Gets or sets the service bus queue
     message.
    :type service_bus_queue_message:
     ~azure.mgmt.scheduler.models.ServiceBusQueueMessage
    :param service_bus_topic_message: Gets or sets the service bus topic
     message.
    :type service_bus_topic_message:
     ~azure.mgmt.scheduler.models.ServiceBusTopicMessage
    :param retry_policy: Gets or sets the retry policy.
    :type retry_policy: ~azure.mgmt.scheduler.models.RetryPolicy
    :param error_action: Gets or sets the error action.
    :type error_action: ~azure.mgmt.scheduler.models.JobErrorAction
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'JobActionType'},
        'request': {'key': 'request', 'type': 'HttpRequest'},
        'queue_message': {'key': 'queueMessage', 'type': 'StorageQueueMessage'},
        'service_bus_queue_message': {'key': 'serviceBusQueueMessage', 'type': 'ServiceBusQueueMessage'},
        'service_bus_topic_message': {'key': 'serviceBusTopicMessage', 'type': 'ServiceBusTopicMessage'},
        'retry_policy': {'key': 'retryPolicy', 'type': 'RetryPolicy'},
        'error_action': {'key': 'errorAction', 'type': 'JobErrorAction'},
    }

    def __init__(self, **kwargs):
        super(JobAction, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.request = kwargs.get('request', None)
        self.queue_message = kwargs.get('queue_message', None)
        self.service_bus_queue_message = kwargs.get('service_bus_queue_message', None)
        self.service_bus_topic_message = kwargs.get('service_bus_topic_message', None)
        self.retry_policy = kwargs.get('retry_policy', None)
        self.error_action = kwargs.get('error_action', None)


class JobCollectionDefinition(Model):
    """JobCollectionDefinition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the job collection resource identifier.
    :vartype id: str
    :ivar type: Gets the job collection resource type.
    :vartype type: str
    :param name: Gets or sets the job collection resource name.
    :type name: str
    :param location: Gets or sets the storage account location.
    :type location: str
    :param tags: Gets or sets the tags.
    :type tags: dict[str, str]
    :param properties: Gets or sets the job collection properties.
    :type properties: ~azure.mgmt.scheduler.models.JobCollectionProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': 'JobCollectionProperties'},
    }

    def __init__(self, **kwargs):
        super(JobCollectionDefinition, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = kwargs.get('name', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)


class JobCollectionProperties(Model):
    """JobCollectionProperties.

    :param sku: Gets or sets the SKU.
    :type sku: ~azure.mgmt.scheduler.models.Sku
    :param state: Gets or sets the state. Possible values include: 'Enabled',
     'Disabled', 'Suspended', 'Deleted'
    :type state: str or ~azure.mgmt.scheduler.models.JobCollectionState
    :param quota: Gets or sets the job collection quota.
    :type quota: ~azure.mgmt.scheduler.models.JobCollectionQuota
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'state': {'key': 'state', 'type': 'JobCollectionState'},
        'quota': {'key': 'quota', 'type': 'JobCollectionQuota'},
    }

    def __init__(self, **kwargs):
        super(JobCollectionProperties, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.state = kwargs.get('state', None)
        self.quota = kwargs.get('quota', None)


class JobCollectionQuota(Model):
    """JobCollectionQuota.

    :param max_job_count: Gets or set the maximum job count.
    :type max_job_count: int
    :param max_job_occurrence: Gets or sets the maximum job occurrence.
    :type max_job_occurrence: int
    :param max_recurrence: Gets or set the maximum recurrence.
    :type max_recurrence: ~azure.mgmt.scheduler.models.JobMaxRecurrence
    """

    _attribute_map = {
        'max_job_count': {'key': 'maxJobCount', 'type': 'int'},
        'max_job_occurrence': {'key': 'maxJobOccurrence', 'type': 'int'},
        'max_recurrence': {'key': 'maxRecurrence', 'type': 'JobMaxRecurrence'},
    }

    def __init__(self, **kwargs):
        super(JobCollectionQuota, self).__init__(**kwargs)
        self.max_job_count = kwargs.get('max_job_count', None)
        self.max_job_occurrence = kwargs.get('max_job_occurrence', None)
        self.max_recurrence = kwargs.get('max_recurrence', None)


class JobDefinition(Model):
    """JobDefinition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the job resource identifier.
    :vartype id: str
    :ivar type: Gets the job resource type.
    :vartype type: str
    :ivar name: Gets the job resource name.
    :vartype name: str
    :param properties: Gets or sets the job properties.
    :type properties: ~azure.mgmt.scheduler.models.JobProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'JobProperties'},
    }

    def __init__(self, **kwargs):
        super(JobDefinition, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = kwargs.get('properties', None)


class JobErrorAction(Model):
    """JobErrorAction.

    :param type: Gets or sets the job error action type. Possible values
     include: 'Http', 'Https', 'StorageQueue', 'ServiceBusQueue',
     'ServiceBusTopic'
    :type type: str or ~azure.mgmt.scheduler.models.JobActionType
    :param request: Gets or sets the http requests.
    :type request: ~azure.mgmt.scheduler.models.HttpRequest
    :param queue_message: Gets or sets the storage queue message.
    :type queue_message: ~azure.mgmt.scheduler.models.StorageQueueMessage
    :param service_bus_queue_message: Gets or sets the service bus queue
     message.
    :type service_bus_queue_message:
     ~azure.mgmt.scheduler.models.ServiceBusQueueMessage
    :param service_bus_topic_message: Gets or sets the service bus topic
     message.
    :type service_bus_topic_message:
     ~azure.mgmt.scheduler.models.ServiceBusTopicMessage
    :param retry_policy: Gets or sets the retry policy.
    :type retry_policy: ~azure.mgmt.scheduler.models.RetryPolicy
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'JobActionType'},
        'request': {'key': 'request', 'type': 'HttpRequest'},
        'queue_message': {'key': 'queueMessage', 'type': 'StorageQueueMessage'},
        'service_bus_queue_message': {'key': 'serviceBusQueueMessage', 'type': 'ServiceBusQueueMessage'},
        'service_bus_topic_message': {'key': 'serviceBusTopicMessage', 'type': 'ServiceBusTopicMessage'},
        'retry_policy': {'key': 'retryPolicy', 'type': 'RetryPolicy'},
    }

    def __init__(self, **kwargs):
        super(JobErrorAction, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.request = kwargs.get('request', None)
        self.queue_message = kwargs.get('queue_message', None)
        self.service_bus_queue_message = kwargs.get('service_bus_queue_message', None)
        self.service_bus_topic_message = kwargs.get('service_bus_topic_message', None)
        self.retry_policy = kwargs.get('retry_policy', None)


class JobHistoryDefinition(Model):
    """JobHistoryDefinition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the job history identifier.
    :vartype id: str
    :ivar type: Gets the job history resource type.
    :vartype type: str
    :ivar name: Gets the job history name.
    :vartype name: str
    :ivar properties: Gets or sets the job history properties.
    :vartype properties:
     ~azure.mgmt.scheduler.models.JobHistoryDefinitionProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'JobHistoryDefinitionProperties'},
    }

    def __init__(self, **kwargs):
        super(JobHistoryDefinition, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.properties = None


class JobHistoryDefinitionProperties(Model):
    """JobHistoryDefinitionProperties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar start_time: Gets the start time for this job.
    :vartype start_time: datetime
    :ivar end_time: Gets the end time for this job.
    :vartype end_time: datetime
    :ivar expected_execution_time: Gets the expected execution time for this
     job.
    :vartype expected_execution_time: datetime
    :ivar action_name: Gets the job history action name. Possible values
     include: 'MainAction', 'ErrorAction'
    :vartype action_name: str or
     ~azure.mgmt.scheduler.models.JobHistoryActionName
    :ivar status: Gets the job history status. Possible values include:
     'Completed', 'Failed', 'Postponed'
    :vartype status: str or ~azure.mgmt.scheduler.models.JobExecutionStatus
    :ivar message: Gets the message for the job history.
    :vartype message: str
    :ivar retry_count: Gets the retry count for job.
    :vartype retry_count: int
    :ivar repeat_count: Gets the repeat count for the job.
    :vartype repeat_count: int
    """

    _validation = {
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'expected_execution_time': {'readonly': True},
        'action_name': {'readonly': True},
        'status': {'readonly': True},
        'message': {'readonly': True},
        'retry_count': {'readonly': True},
        'repeat_count': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'expected_execution_time': {'key': 'expectedExecutionTime', 'type': 'iso-8601'},
        'action_name': {'key': 'actionName', 'type': 'JobHistoryActionName'},
        'status': {'key': 'status', 'type': 'JobExecutionStatus'},
        'message': {'key': 'message', 'type': 'str'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'repeat_count': {'key': 'repeatCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(JobHistoryDefinitionProperties, self).__init__(**kwargs)
        self.start_time = None
        self.end_time = None
        self.expected_execution_time = None
        self.action_name = None
        self.status = None
        self.message = None
        self.retry_count = None
        self.repeat_count = None


class JobHistoryFilter(Model):
    """JobHistoryFilter.

    :param status: Gets or sets the job execution status. Possible values
     include: 'Completed', 'Failed', 'Postponed'
    :type status: str or ~azure.mgmt.scheduler.models.JobExecutionStatus
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'JobExecutionStatus'},
    }

    def __init__(self, **kwargs):
        super(JobHistoryFilter, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)


class JobMaxRecurrence(Model):
    """JobMaxRecurrence.

    :param frequency: Gets or sets the frequency of recurrence (second,
     minute, hour, day, week, month). Possible values include: 'Minute',
     'Hour', 'Day', 'Week', 'Month'
    :type frequency: str or ~azure.mgmt.scheduler.models.RecurrenceFrequency
    :param interval: Gets or sets the interval between retries.
    :type interval: int
    """

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'RecurrenceFrequency'},
        'interval': {'key': 'interval', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(JobMaxRecurrence, self).__init__(**kwargs)
        self.frequency = kwargs.get('frequency', None)
        self.interval = kwargs.get('interval', None)


class JobProperties(Model):
    """JobProperties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param start_time: Gets or sets the job start time.
    :type start_time: datetime
    :param action: Gets or sets the job action.
    :type action: ~azure.mgmt.scheduler.models.JobAction
    :param recurrence: Gets or sets the job recurrence.
    :type recurrence: ~azure.mgmt.scheduler.models.JobRecurrence
    :param state: Gets or set the job state. Possible values include:
     'Enabled', 'Disabled', 'Faulted', 'Completed'
    :type state: str or ~azure.mgmt.scheduler.models.JobState
    :ivar status: Gets the job status.
    :vartype status: ~azure.mgmt.scheduler.models.JobStatus
    """

    _validation = {
        'status': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'action': {'key': 'action', 'type': 'JobAction'},
        'recurrence': {'key': 'recurrence', 'type': 'JobRecurrence'},
        'state': {'key': 'state', 'type': 'JobState'},
        'status': {'key': 'status', 'type': 'JobStatus'},
    }

    def __init__(self, **kwargs):
        super(JobProperties, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.action = kwargs.get('action', None)
        self.recurrence = kwargs.get('recurrence', None)
        self.state = kwargs.get('state', None)
        self.status = None


class JobRecurrence(Model):
    """JobRecurrence.

    :param frequency: Gets or sets the frequency of recurrence (second,
     minute, hour, day, week, month). Possible values include: 'Minute',
     'Hour', 'Day', 'Week', 'Month'
    :type frequency: str or ~azure.mgmt.scheduler.models.RecurrenceFrequency
    :param interval: Gets or sets the interval between retries.
    :type interval: int
    :param count: Gets or sets the maximum number of times that the job should
     run.
    :type count: int
    :param end_time: Gets or sets the time at which the job will complete.
    :type end_time: datetime
    :param schedule:
    :type schedule: ~azure.mgmt.scheduler.models.JobRecurrenceSchedule
    """

    _attribute_map = {
        'frequency': {'key': 'frequency', 'type': 'RecurrenceFrequency'},
        'interval': {'key': 'interval', 'type': 'int'},
        'count': {'key': 'count', 'type': 'int'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'schedule': {'key': 'schedule', 'type': 'JobRecurrenceSchedule'},
    }

    def __init__(self, **kwargs):
        super(JobRecurrence, self).__init__(**kwargs)
        self.frequency = kwargs.get('frequency', None)
        self.interval = kwargs.get('interval', None)
        self.count = kwargs.get('count', None)
        self.end_time = kwargs.get('end_time', None)
        self.schedule = kwargs.get('schedule', None)


class JobRecurrenceSchedule(Model):
    """JobRecurrenceSchedule.

    :param week_days: Gets or sets the days of the week that the job should
     execute on.
    :type week_days: list[str or ~azure.mgmt.scheduler.models.DayOfWeek]
    :param hours: Gets or sets the hours of the day that the job should
     execute at.
    :type hours: list[int]
    :param minutes: Gets or sets the minutes of the hour that the job should
     execute at.
    :type minutes: list[int]
    :param month_days: Gets or sets the days of the month that the job should
     execute on. Must be between 1 and 31.
    :type month_days: list[int]
    :param monthly_occurrences: Gets or sets the occurrences of days within a
     month.
    :type monthly_occurrences:
     list[~azure.mgmt.scheduler.models.JobRecurrenceScheduleMonthlyOccurrence]
    """

    _attribute_map = {
        'week_days': {'key': 'weekDays', 'type': '[DayOfWeek]'},
        'hours': {'key': 'hours', 'type': '[int]'},
        'minutes': {'key': 'minutes', 'type': '[int]'},
        'month_days': {'key': 'monthDays', 'type': '[int]'},
        'monthly_occurrences': {'key': 'monthlyOccurrences', 'type': '[JobRecurrenceScheduleMonthlyOccurrence]'},
    }

    def __init__(self, **kwargs):
        super(JobRecurrenceSchedule, self).__init__(**kwargs)
        self.week_days = kwargs.get('week_days', None)
        self.hours = kwargs.get('hours', None)
        self.minutes = kwargs.get('minutes', None)
        self.month_days = kwargs.get('month_days', None)
        self.monthly_occurrences = kwargs.get('monthly_occurrences', None)


class JobRecurrenceScheduleMonthlyOccurrence(Model):
    """JobRecurrenceScheduleMonthlyOccurrence.

    :param day: Gets or sets the day. Must be one of monday, tuesday,
     wednesday, thursday, friday, saturday, sunday. Possible values include:
     'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
     'Sunday'
    :type day: str or ~azure.mgmt.scheduler.models.JobScheduleDay
    :param occurrence: Gets or sets the occurrence. Must be between -5 and 5.
    :type occurrence: int
    """

    _attribute_map = {
        'day': {'key': 'day', 'type': 'JobScheduleDay'},
        'occurrence': {'key': 'Occurrence', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(JobRecurrenceScheduleMonthlyOccurrence, self).__init__(**kwargs)
        self.day = kwargs.get('day', None)
        self.occurrence = kwargs.get('occurrence', None)


class JobStateFilter(Model):
    """JobStateFilter.

    :param state: Gets or sets the job state. Possible values include:
     'Enabled', 'Disabled', 'Faulted', 'Completed'
    :type state: str or ~azure.mgmt.scheduler.models.JobState
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'JobState'},
    }

    def __init__(self, **kwargs):
        super(JobStateFilter, self).__init__(**kwargs)
        self.state = kwargs.get('state', None)


class JobStatus(Model):
    """JobStatus.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar execution_count: Gets the number of times this job has executed.
    :vartype execution_count: int
    :ivar failure_count: Gets the number of times this job has failed.
    :vartype failure_count: int
    :ivar faulted_count: Gets the number of faulted occurrences (occurrences
     that were retried and failed as many times as the retry policy states).
    :vartype faulted_count: int
    :ivar last_execution_time: Gets the time the last occurrence executed in
     ISO-8601 format.  Could be empty if job has not run yet.
    :vartype last_execution_time: datetime
    :ivar next_execution_time: Gets the time of the next occurrence in
     ISO-8601 format. Could be empty if the job is completed.
    :vartype next_execution_time: datetime
    """

    _validation = {
        'execution_count': {'readonly': True},
        'failure_count': {'readonly': True},
        'faulted_count': {'readonly': True},
        'last_execution_time': {'readonly': True},
        'next_execution_time': {'readonly': True},
    }

    _attribute_map = {
        'execution_count': {'key': 'executionCount', 'type': 'int'},
        'failure_count': {'key': 'failureCount', 'type': 'int'},
        'faulted_count': {'key': 'faultedCount', 'type': 'int'},
        'last_execution_time': {'key': 'lastExecutionTime', 'type': 'iso-8601'},
        'next_execution_time': {'key': 'nextExecutionTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(JobStatus, self).__init__(**kwargs)
        self.execution_count = None
        self.failure_count = None
        self.faulted_count = None
        self.last_execution_time = None
        self.next_execution_time = None


class OAuthAuthentication(HttpAuthentication):
    """OAuthAuthentication.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param secret: Gets or sets the secret, return value will always be empty.
    :type secret: str
    :param tenant: Gets or sets the tenant.
    :type tenant: str
    :param audience: Gets or sets the audience.
    :type audience: str
    :param client_id: Gets or sets the client identifier.
    :type client_id: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
        'tenant': {'key': 'tenant', 'type': 'str'},
        'audience': {'key': 'audience', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OAuthAuthentication, self).__init__(**kwargs)
        self.secret = kwargs.get('secret', None)
        self.tenant = kwargs.get('tenant', None)
        self.audience = kwargs.get('audience', None)
        self.client_id = kwargs.get('client_id', None)
        self.type = 'ActiveDirectoryOAuth'


class RetryPolicy(Model):
    """RetryPolicy.

    :param retry_type: Gets or sets the retry strategy to be used. Possible
     values include: 'None', 'Fixed'
    :type retry_type: str or ~azure.mgmt.scheduler.models.RetryType
    :param retry_interval: Gets or sets the retry interval between retries,
     specify duration in ISO 8601 format.
    :type retry_interval: timedelta
    :param retry_count: Gets or sets the number of times a retry should be
     attempted.
    :type retry_count: int
    """

    _attribute_map = {
        'retry_type': {'key': 'retryType', 'type': 'RetryType'},
        'retry_interval': {'key': 'retryInterval', 'type': 'duration'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RetryPolicy, self).__init__(**kwargs)
        self.retry_type = kwargs.get('retry_type', None)
        self.retry_interval = kwargs.get('retry_interval', None)
        self.retry_count = kwargs.get('retry_count', None)


class ServiceBusAuthentication(Model):
    """ServiceBusAuthentication.

    :param sas_key: Gets or sets the SAS key.
    :type sas_key: str
    :param sas_key_name: Gets or sets the SAS key name.
    :type sas_key_name: str
    :param type: Gets or sets the authentication type. Possible values
     include: 'NotSpecified', 'SharedAccessKey'
    :type type: str or
     ~azure.mgmt.scheduler.models.ServiceBusAuthenticationType
    """

    _attribute_map = {
        'sas_key': {'key': 'sasKey', 'type': 'str'},
        'sas_key_name': {'key': 'sasKeyName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ServiceBusAuthenticationType'},
    }

    def __init__(self, **kwargs):
        super(ServiceBusAuthentication, self).__init__(**kwargs)
        self.sas_key = kwargs.get('sas_key', None)
        self.sas_key_name = kwargs.get('sas_key_name', None)
        self.type = kwargs.get('type', None)


class ServiceBusBrokeredMessageProperties(Model):
    """ServiceBusBrokeredMessageProperties.

    :param content_type: Gets or sets the content type.
    :type content_type: str
    :param correlation_id: Gets or sets the correlation ID.
    :type correlation_id: str
    :param force_persistence: Gets or sets the force persistence.
    :type force_persistence: bool
    :param label: Gets or sets the label.
    :type label: str
    :param message_id: Gets or sets the message ID.
    :type message_id: str
    :param partition_key: Gets or sets the partition key.
    :type partition_key: str
    :param reply_to: Gets or sets the reply to.
    :type reply_to: str
    :param reply_to_session_id: Gets or sets the reply to session ID.
    :type reply_to_session_id: str
    :param scheduled_enqueue_time_utc: Gets or sets the scheduled enqueue time
     UTC.
    :type scheduled_enqueue_time_utc: datetime
    :param session_id: Gets or sets the session ID.
    :type session_id: str
    :param time_to_live: Gets or sets the time to live.
    :type time_to_live: timedelta
    :param to: Gets or sets the to.
    :type to: str
    :param via_partition_key: Gets or sets the via partition key.
    :type via_partition_key: str
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'force_persistence': {'key': 'forcePersistence', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'partition_key': {'key': 'partitionKey', 'type': 'str'},
        'reply_to': {'key': 'replyTo', 'type': 'str'},
        'reply_to_session_id': {'key': 'replyToSessionId', 'type': 'str'},
        'scheduled_enqueue_time_utc': {'key': 'scheduledEnqueueTimeUtc', 'type': 'iso-8601'},
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'time_to_live': {'key': 'timeToLive', 'type': 'duration'},
        'to': {'key': 'to', 'type': 'str'},
        'via_partition_key': {'key': 'viaPartitionKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceBusBrokeredMessageProperties, self).__init__(**kwargs)
        self.content_type = kwargs.get('content_type', None)
        self.correlation_id = kwargs.get('correlation_id', None)
        self.force_persistence = kwargs.get('force_persistence', None)
        self.label = kwargs.get('label', None)
        self.message_id = kwargs.get('message_id', None)
        self.partition_key = kwargs.get('partition_key', None)
        self.reply_to = kwargs.get('reply_to', None)
        self.reply_to_session_id = kwargs.get('reply_to_session_id', None)
        self.scheduled_enqueue_time_utc = kwargs.get('scheduled_enqueue_time_utc', None)
        self.session_id = kwargs.get('session_id', None)
        self.time_to_live = kwargs.get('time_to_live', None)
        self.to = kwargs.get('to', None)
        self.via_partition_key = kwargs.get('via_partition_key', None)


class ServiceBusMessage(Model):
    """ServiceBusMessage.

    :param authentication: Gets or sets the Service Bus authentication.
    :type authentication:
     ~azure.mgmt.scheduler.models.ServiceBusAuthentication
    :param brokered_message_properties: Gets or sets the brokered message
     properties.
    :type brokered_message_properties:
     ~azure.mgmt.scheduler.models.ServiceBusBrokeredMessageProperties
    :param custom_message_properties: Gets or sets the custom message
     properties.
    :type custom_message_properties: dict[str, str]
    :param message: Gets or sets the message.
    :type message: str
    :param namespace: Gets or sets the namespace.
    :type namespace: str
    :param transport_type: Gets or sets the transport type. Possible values
     include: 'NotSpecified', 'NetMessaging', 'AMQP'
    :type transport_type: str or
     ~azure.mgmt.scheduler.models.ServiceBusTransportType
    """

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'ServiceBusAuthentication'},
        'brokered_message_properties': {'key': 'brokeredMessageProperties', 'type': 'ServiceBusBrokeredMessageProperties'},
        'custom_message_properties': {'key': 'customMessageProperties', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'transport_type': {'key': 'transportType', 'type': 'ServiceBusTransportType'},
    }

    def __init__(self, **kwargs):
        super(ServiceBusMessage, self).__init__(**kwargs)
        self.authentication = kwargs.get('authentication', None)
        self.brokered_message_properties = kwargs.get('brokered_message_properties', None)
        self.custom_message_properties = kwargs.get('custom_message_properties', None)
        self.message = kwargs.get('message', None)
        self.namespace = kwargs.get('namespace', None)
        self.transport_type = kwargs.get('transport_type', None)


class ServiceBusQueueMessage(ServiceBusMessage):
    """ServiceBusQueueMessage.

    :param authentication: Gets or sets the Service Bus authentication.
    :type authentication:
     ~azure.mgmt.scheduler.models.ServiceBusAuthentication
    :param brokered_message_properties: Gets or sets the brokered message
     properties.
    :type brokered_message_properties:
     ~azure.mgmt.scheduler.models.ServiceBusBrokeredMessageProperties
    :param custom_message_properties: Gets or sets the custom message
     properties.
    :type custom_message_properties: dict[str, str]
    :param message: Gets or sets the message.
    :type message: str
    :param namespace: Gets or sets the namespace.
    :type namespace: str
    :param transport_type: Gets or sets the transport type. Possible values
     include: 'NotSpecified', 'NetMessaging', 'AMQP'
    :type transport_type: str or
     ~azure.mgmt.scheduler.models.ServiceBusTransportType
    :param queue_name: Gets or sets the queue name.
    :type queue_name: str
    """

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'ServiceBusAuthentication'},
        'brokered_message_properties': {'key': 'brokeredMessageProperties', 'type': 'ServiceBusBrokeredMessageProperties'},
        'custom_message_properties': {'key': 'customMessageProperties', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'transport_type': {'key': 'transportType', 'type': 'ServiceBusTransportType'},
        'queue_name': {'key': 'queueName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceBusQueueMessage, self).__init__(**kwargs)
        self.queue_name = kwargs.get('queue_name', None)


class ServiceBusTopicMessage(ServiceBusMessage):
    """ServiceBusTopicMessage.

    :param authentication: Gets or sets the Service Bus authentication.
    :type authentication:
     ~azure.mgmt.scheduler.models.ServiceBusAuthentication
    :param brokered_message_properties: Gets or sets the brokered message
     properties.
    :type brokered_message_properties:
     ~azure.mgmt.scheduler.models.ServiceBusBrokeredMessageProperties
    :param custom_message_properties: Gets or sets the custom message
     properties.
    :type custom_message_properties: dict[str, str]
    :param message: Gets or sets the message.
    :type message: str
    :param namespace: Gets or sets the namespace.
    :type namespace: str
    :param transport_type: Gets or sets the transport type. Possible values
     include: 'NotSpecified', 'NetMessaging', 'AMQP'
    :type transport_type: str or
     ~azure.mgmt.scheduler.models.ServiceBusTransportType
    :param topic_path: Gets or sets the topic path.
    :type topic_path: str
    """

    _attribute_map = {
        'authentication': {'key': 'authentication', 'type': 'ServiceBusAuthentication'},
        'brokered_message_properties': {'key': 'brokeredMessageProperties', 'type': 'ServiceBusBrokeredMessageProperties'},
        'custom_message_properties': {'key': 'customMessageProperties', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'transport_type': {'key': 'transportType', 'type': 'ServiceBusTransportType'},
        'topic_path': {'key': 'topicPath', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceBusTopicMessage, self).__init__(**kwargs)
        self.topic_path = kwargs.get('topic_path', None)


class Sku(Model):
    """Sku.

    :param name: Gets or set the SKU. Possible values include: 'Standard',
     'Free', 'P10Premium', 'P20Premium'
    :type name: str or ~azure.mgmt.scheduler.models.SkuDefinition
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'SkuDefinition'},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)


class StorageQueueMessage(Model):
    """StorageQueueMessage.

    :param storage_account: Gets or sets the storage account name.
    :type storage_account: str
    :param queue_name: Gets or sets the queue name.
    :type queue_name: str
    :param sas_token: Gets or sets the SAS key.
    :type sas_token: str
    :param message: Gets or sets the message.
    :type message: str
    """

    _attribute_map = {
        'storage_account': {'key': 'storageAccount', 'type': 'str'},
        'queue_name': {'key': 'queueName', 'type': 'str'},
        'sas_token': {'key': 'sasToken', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StorageQueueMessage, self).__init__(**kwargs)
        self.storage_account = kwargs.get('storage_account', None)
        self.queue_name = kwargs.get('queue_name', None)
        self.sas_token = kwargs.get('sas_token', None)
        self.message = kwargs.get('message', None)
