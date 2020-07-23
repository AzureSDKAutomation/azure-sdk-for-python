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

from msrest.paging import Paged


class RecoverableDatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RecoverableDatabase <azure.mgmt.sql.models.RecoverableDatabase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RecoverableDatabase]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecoverableDatabasePaged, self).__init__(*args, **kwargs)
class RestorableDroppedDatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RestorableDroppedDatabase <azure.mgmt.sql.models.RestorableDroppedDatabase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RestorableDroppedDatabase]'}
    }

    def __init__(self, *args, **kwargs):

        super(RestorableDroppedDatabasePaged, self).__init__(*args, **kwargs)
class DataMaskingRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DataMaskingRule <azure.mgmt.sql.models.DataMaskingRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DataMaskingRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(DataMaskingRulePaged, self).__init__(*args, **kwargs)
class FirewallRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`FirewallRule <azure.mgmt.sql.models.FirewallRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FirewallRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(FirewallRulePaged, self).__init__(*args, **kwargs)
class GeoBackupPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GeoBackupPolicy <azure.mgmt.sql.models.GeoBackupPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GeoBackupPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(GeoBackupPolicyPaged, self).__init__(*args, **kwargs)
class MetricPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Metric <azure.mgmt.sql.models.Metric>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Metric]'}
    }

    def __init__(self, *args, **kwargs):

        super(MetricPaged, self).__init__(*args, **kwargs)
class MetricDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`MetricDefinition <azure.mgmt.sql.models.MetricDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[MetricDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(MetricDefinitionPaged, self).__init__(*args, **kwargs)
class DatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Database <azure.mgmt.sql.models.Database>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Database]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabasePaged, self).__init__(*args, **kwargs)
class ElasticPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ElasticPool <azure.mgmt.sql.models.ElasticPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ElasticPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(ElasticPoolPaged, self).__init__(*args, **kwargs)
class RecommendedElasticPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RecommendedElasticPool <azure.mgmt.sql.models.RecommendedElasticPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RecommendedElasticPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecommendedElasticPoolPaged, self).__init__(*args, **kwargs)
class RecommendedElasticPoolMetricPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RecommendedElasticPoolMetric <azure.mgmt.sql.models.RecommendedElasticPoolMetric>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RecommendedElasticPoolMetric]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecommendedElasticPoolMetricPaged, self).__init__(*args, **kwargs)
class ReplicationLinkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ReplicationLink <azure.mgmt.sql.models.ReplicationLink>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ReplicationLink]'}
    }

    def __init__(self, *args, **kwargs):

        super(ReplicationLinkPaged, self).__init__(*args, **kwargs)
class ServerCommunicationLinkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerCommunicationLink <azure.mgmt.sql.models.ServerCommunicationLink>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerCommunicationLink]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerCommunicationLinkPaged, self).__init__(*args, **kwargs)
class ServiceObjectivePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServiceObjective <azure.mgmt.sql.models.ServiceObjective>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServiceObjective]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServiceObjectivePaged, self).__init__(*args, **kwargs)
class ElasticPoolActivityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ElasticPoolActivity <azure.mgmt.sql.models.ElasticPoolActivity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ElasticPoolActivity]'}
    }

    def __init__(self, *args, **kwargs):

        super(ElasticPoolActivityPaged, self).__init__(*args, **kwargs)
class ElasticPoolDatabaseActivityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ElasticPoolDatabaseActivity <azure.mgmt.sql.models.ElasticPoolDatabaseActivity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ElasticPoolDatabaseActivity]'}
    }

    def __init__(self, *args, **kwargs):

        super(ElasticPoolDatabaseActivityPaged, self).__init__(*args, **kwargs)
class ServiceTierAdvisorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServiceTierAdvisor <azure.mgmt.sql.models.ServiceTierAdvisor>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServiceTierAdvisor]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServiceTierAdvisorPaged, self).__init__(*args, **kwargs)
class TransparentDataEncryptionActivityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TransparentDataEncryptionActivity <azure.mgmt.sql.models.TransparentDataEncryptionActivity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TransparentDataEncryptionActivity]'}
    }

    def __init__(self, *args, **kwargs):

        super(TransparentDataEncryptionActivityPaged, self).__init__(*args, **kwargs)
class ServerUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerUsage <azure.mgmt.sql.models.ServerUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerUsagePaged, self).__init__(*args, **kwargs)
class DatabaseUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DatabaseUsage <azure.mgmt.sql.models.DatabaseUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DatabaseUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabaseUsagePaged, self).__init__(*args, **kwargs)
class EncryptionProtectorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`EncryptionProtector <azure.mgmt.sql.models.EncryptionProtector>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EncryptionProtector]'}
    }

    def __init__(self, *args, **kwargs):

        super(EncryptionProtectorPaged, self).__init__(*args, **kwargs)
class FailoverGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FailoverGroup <azure.mgmt.sql.models.FailoverGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FailoverGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(FailoverGroupPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.sql.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class ServerKeyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerKey <azure.mgmt.sql.models.ServerKey>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerKey]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerKeyPaged, self).__init__(*args, **kwargs)
class SyncAgentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncAgent <azure.mgmt.sql.models.SyncAgent>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncAgent]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncAgentPaged, self).__init__(*args, **kwargs)
class SyncAgentLinkedDatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncAgentLinkedDatabase <azure.mgmt.sql.models.SyncAgentLinkedDatabase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncAgentLinkedDatabase]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncAgentLinkedDatabasePaged, self).__init__(*args, **kwargs)
class SubscriptionUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SubscriptionUsage <azure.mgmt.sql.models.SubscriptionUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SubscriptionUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(SubscriptionUsagePaged, self).__init__(*args, **kwargs)
class VirtualClusterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualCluster <azure.mgmt.sql.models.VirtualCluster>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualCluster]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualClusterPaged, self).__init__(*args, **kwargs)
class VirtualNetworkRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkRule <azure.mgmt.sql.models.VirtualNetworkRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkRulePaged, self).__init__(*args, **kwargs)
class ExtendedDatabaseBlobAuditingPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExtendedDatabaseBlobAuditingPolicy <azure.mgmt.sql.models.ExtendedDatabaseBlobAuditingPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExtendedDatabaseBlobAuditingPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExtendedDatabaseBlobAuditingPolicyPaged, self).__init__(*args, **kwargs)
class ExtendedServerBlobAuditingPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExtendedServerBlobAuditingPolicy <azure.mgmt.sql.models.ExtendedServerBlobAuditingPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExtendedServerBlobAuditingPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExtendedServerBlobAuditingPolicyPaged, self).__init__(*args, **kwargs)
class ServerBlobAuditingPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerBlobAuditingPolicy <azure.mgmt.sql.models.ServerBlobAuditingPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerBlobAuditingPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerBlobAuditingPolicyPaged, self).__init__(*args, **kwargs)
class DatabaseBlobAuditingPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DatabaseBlobAuditingPolicy <azure.mgmt.sql.models.DatabaseBlobAuditingPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DatabaseBlobAuditingPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabaseBlobAuditingPolicyPaged, self).__init__(*args, **kwargs)
class DatabaseVulnerabilityAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DatabaseVulnerabilityAssessment <azure.mgmt.sql.models.DatabaseVulnerabilityAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DatabaseVulnerabilityAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabaseVulnerabilityAssessmentPaged, self).__init__(*args, **kwargs)
class JobAgentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobAgent <azure.mgmt.sql.models.JobAgent>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobAgent]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobAgentPaged, self).__init__(*args, **kwargs)
class JobCredentialPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobCredential <azure.mgmt.sql.models.JobCredential>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobCredential]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobCredentialPaged, self).__init__(*args, **kwargs)
class JobExecutionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobExecution <azure.mgmt.sql.models.JobExecution>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobExecution]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobExecutionPaged, self).__init__(*args, **kwargs)
class JobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Job <azure.mgmt.sql.models.Job>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Job]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobPaged, self).__init__(*args, **kwargs)
class JobStepPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobStep <azure.mgmt.sql.models.JobStep>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobStep]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobStepPaged, self).__init__(*args, **kwargs)
class JobTargetGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobTargetGroup <azure.mgmt.sql.models.JobTargetGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobTargetGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobTargetGroupPaged, self).__init__(*args, **kwargs)
class JobVersionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobVersion <azure.mgmt.sql.models.JobVersion>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobVersion]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobVersionPaged, self).__init__(*args, **kwargs)
class LongTermRetentionBackupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LongTermRetentionBackup <azure.mgmt.sql.models.LongTermRetentionBackup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LongTermRetentionBackup]'}
    }

    def __init__(self, *args, **kwargs):

        super(LongTermRetentionBackupPaged, self).__init__(*args, **kwargs)
class ManagedBackupShortTermRetentionPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedBackupShortTermRetentionPolicy <azure.mgmt.sql.models.ManagedBackupShortTermRetentionPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedBackupShortTermRetentionPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedBackupShortTermRetentionPolicyPaged, self).__init__(*args, **kwargs)
class ServerDnsAliasPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerDnsAlias <azure.mgmt.sql.models.ServerDnsAlias>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerDnsAlias]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerDnsAliasPaged, self).__init__(*args, **kwargs)
class ServerSecurityAlertPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerSecurityAlertPolicy <azure.mgmt.sql.models.ServerSecurityAlertPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerSecurityAlertPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerSecurityAlertPolicyPaged, self).__init__(*args, **kwargs)
class RestorableDroppedManagedDatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RestorableDroppedManagedDatabase <azure.mgmt.sql.models.RestorableDroppedManagedDatabase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RestorableDroppedManagedDatabase]'}
    }

    def __init__(self, *args, **kwargs):

        super(RestorableDroppedManagedDatabasePaged, self).__init__(*args, **kwargs)
class RestorePointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RestorePoint <azure.mgmt.sql.models.RestorePoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RestorePoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(RestorePointPaged, self).__init__(*args, **kwargs)
class ManagedDatabaseSecurityAlertPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedDatabaseSecurityAlertPolicy <azure.mgmt.sql.models.ManagedDatabaseSecurityAlertPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedDatabaseSecurityAlertPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedDatabaseSecurityAlertPolicyPaged, self).__init__(*args, **kwargs)
class ManagedServerSecurityAlertPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedServerSecurityAlertPolicy <azure.mgmt.sql.models.ManagedServerSecurityAlertPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedServerSecurityAlertPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedServerSecurityAlertPolicyPaged, self).__init__(*args, **kwargs)
class SensitivityLabelPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SensitivityLabel <azure.mgmt.sql.models.SensitivityLabel>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SensitivityLabel]'}
    }

    def __init__(self, *args, **kwargs):

        super(SensitivityLabelPaged, self).__init__(*args, **kwargs)
class ManagedInstanceAdministratorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceAdministrator <azure.mgmt.sql.models.ManagedInstanceAdministrator>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceAdministrator]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceAdministratorPaged, self).__init__(*args, **kwargs)
class DatabaseOperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DatabaseOperation <azure.mgmt.sql.models.DatabaseOperation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DatabaseOperation]'}
    }

    def __init__(self, *args, **kwargs):

        super(DatabaseOperationPaged, self).__init__(*args, **kwargs)
class ElasticPoolOperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ElasticPoolOperation <azure.mgmt.sql.models.ElasticPoolOperation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ElasticPoolOperation]'}
    }

    def __init__(self, *args, **kwargs):

        super(ElasticPoolOperationPaged, self).__init__(*args, **kwargs)
class VulnerabilityAssessmentScanRecordPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VulnerabilityAssessmentScanRecord <azure.mgmt.sql.models.VulnerabilityAssessmentScanRecord>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VulnerabilityAssessmentScanRecord]'}
    }

    def __init__(self, *args, **kwargs):

        super(VulnerabilityAssessmentScanRecordPaged, self).__init__(*args, **kwargs)
class InstanceFailoverGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`InstanceFailoverGroup <azure.mgmt.sql.models.InstanceFailoverGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[InstanceFailoverGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(InstanceFailoverGroupPaged, self).__init__(*args, **kwargs)
class BackupShortTermRetentionPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BackupShortTermRetentionPolicy <azure.mgmt.sql.models.BackupShortTermRetentionPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BackupShortTermRetentionPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(BackupShortTermRetentionPolicyPaged, self).__init__(*args, **kwargs)
class ManagedInstanceKeyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceKey <azure.mgmt.sql.models.ManagedInstanceKey>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceKey]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceKeyPaged, self).__init__(*args, **kwargs)
class ManagedInstanceEncryptionProtectorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceEncryptionProtector <azure.mgmt.sql.models.ManagedInstanceEncryptionProtector>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceEncryptionProtector]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceEncryptionProtectorPaged, self).__init__(*args, **kwargs)
class RecoverableManagedDatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RecoverableManagedDatabase <azure.mgmt.sql.models.RecoverableManagedDatabase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RecoverableManagedDatabase]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecoverableManagedDatabasePaged, self).__init__(*args, **kwargs)
class ManagedInstanceVulnerabilityAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceVulnerabilityAssessment <azure.mgmt.sql.models.ManagedInstanceVulnerabilityAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceVulnerabilityAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceVulnerabilityAssessmentPaged, self).__init__(*args, **kwargs)
class ServerVulnerabilityAssessmentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerVulnerabilityAssessment <azure.mgmt.sql.models.ServerVulnerabilityAssessment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerVulnerabilityAssessment]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerVulnerabilityAssessmentPaged, self).__init__(*args, **kwargs)
class InstancePoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`InstancePool <azure.mgmt.sql.models.InstancePool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[InstancePool]'}
    }

    def __init__(self, *args, **kwargs):

        super(InstancePoolPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.sql.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class ManagedInstancePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstance <azure.mgmt.sql.models.ManagedInstance>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstance]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstancePaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.sql.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.sql.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class ServerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Server <azure.mgmt.sql.models.Server>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Server]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerPaged, self).__init__(*args, **kwargs)
class ManagedInstanceLongTermRetentionBackupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceLongTermRetentionBackup <azure.mgmt.sql.models.ManagedInstanceLongTermRetentionBackup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceLongTermRetentionBackup]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceLongTermRetentionBackupPaged, self).__init__(*args, **kwargs)
class ManagedInstanceLongTermRetentionPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceLongTermRetentionPolicy <azure.mgmt.sql.models.ManagedInstanceLongTermRetentionPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceLongTermRetentionPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceLongTermRetentionPolicyPaged, self).__init__(*args, **kwargs)
class WorkloadGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WorkloadGroup <azure.mgmt.sql.models.WorkloadGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WorkloadGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkloadGroupPaged, self).__init__(*args, **kwargs)
class WorkloadClassifierPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WorkloadClassifier <azure.mgmt.sql.models.WorkloadClassifier>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WorkloadClassifier]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkloadClassifierPaged, self).__init__(*args, **kwargs)
class ManagedInstanceOperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedInstanceOperation <azure.mgmt.sql.models.ManagedInstanceOperation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedInstanceOperation]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedInstanceOperationPaged, self).__init__(*args, **kwargs)
class ServerAzureADAdministratorPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerAzureADAdministrator <azure.mgmt.sql.models.ServerAzureADAdministrator>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerAzureADAdministrator]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerAzureADAdministratorPaged, self).__init__(*args, **kwargs)
class SyncDatabaseIdPropertiesPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncDatabaseIdProperties <azure.mgmt.sql.models.SyncDatabaseIdProperties>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncDatabaseIdProperties]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncDatabaseIdPropertiesPaged, self).__init__(*args, **kwargs)
class SyncFullSchemaPropertiesPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncFullSchemaProperties <azure.mgmt.sql.models.SyncFullSchemaProperties>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncFullSchemaProperties]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncFullSchemaPropertiesPaged, self).__init__(*args, **kwargs)
class SyncGroupLogPropertiesPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncGroupLogProperties <azure.mgmt.sql.models.SyncGroupLogProperties>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncGroupLogProperties]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncGroupLogPropertiesPaged, self).__init__(*args, **kwargs)
class SyncGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncGroup <azure.mgmt.sql.models.SyncGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncGroupPaged, self).__init__(*args, **kwargs)
class SyncMemberPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SyncMember <azure.mgmt.sql.models.SyncMember>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SyncMember]'}
    }

    def __init__(self, *args, **kwargs):

        super(SyncMemberPaged, self).__init__(*args, **kwargs)
class ManagedDatabasePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ManagedDatabase <azure.mgmt.sql.models.ManagedDatabase>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ManagedDatabase]'}
    }

    def __init__(self, *args, **kwargs):

        super(ManagedDatabasePaged, self).__init__(*args, **kwargs)
class ServerAzureADOnlyAuthenticationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServerAzureADOnlyAuthentication <azure.mgmt.sql.models.ServerAzureADOnlyAuthentication>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServerAzureADOnlyAuthentication]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServerAzureADOnlyAuthenticationPaged, self).__init__(*args, **kwargs)
