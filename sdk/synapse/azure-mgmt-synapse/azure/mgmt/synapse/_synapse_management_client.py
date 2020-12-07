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

from ._configuration import SynapseManagementClientConfiguration
from .operations import BigDataPoolsOperations
from .operations import Operations
from .operations import IpFirewallRulesOperations
from .operations import SqlPoolsOperations
from .operations import SqlPoolMetadataSyncConfigsOperations
from .operations import SqlPoolOperationResultsOperations
from .operations import SqlPoolGeoBackupPoliciesOperations
from .operations import SqlPoolDataWarehouseUserActivitiesOperations
from .operations import SqlPoolRestorePointsOperations
from .operations import SqlPoolReplicationLinksOperations
from .operations import SqlPoolTransparentDataEncryptionsOperations
from .operations import SqlPoolBlobAuditingPoliciesOperations
from .operations import SqlPoolOperations
from .operations import SqlPoolUsagesOperations
from .operations import SqlPoolSensitivityLabelsOperations
from .operations import SqlPoolSchemasOperations
from .operations import SqlPoolTablesOperations
from .operations import SqlPoolTableColumnsOperations
from .operations import SqlPoolConnectionPoliciesOperations
from .operations import SqlPoolVulnerabilityAssessmentsOperations
from .operations import SqlPoolVulnerabilityAssessmentScansOperations
from .operations import SqlPoolSecurityAlertPoliciesOperations
from .operations import SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
from .operations import ExtendedSqlPoolBlobAuditingPoliciesOperations
from .operations import DataMaskingPoliciesOperations
from .operations import DataMaskingRulesOperations
from .operations import SqlPoolColumnsOperations
from .operations import SqlPoolWorkloadGroupOperations
from .operations import SqlPoolWorkloadClassifierOperations
from .operations import WorkspacesOperations
from .operations import WorkspaceAadAdminsOperations
from .operations import WorkspaceSqlAadAdminsOperations
from .operations import WorkspaceManagedIdentitySqlControlSettingsOperations
from .operations import RestorableDroppedSqlPoolsOperations
from .operations import IntegrationRuntimesOperations
from .operations import IntegrationRuntimeNodeIpAddressOperations
from .operations import IntegrationRuntimeObjectMetadataOperations
from .operations import IntegrationRuntimeNodesOperations
from .operations import IntegrationRuntimeCredentialsOperations
from .operations import IntegrationRuntimeConnectionInfosOperations
from .operations import IntegrationRuntimeAuthKeysOperations
from .operations import IntegrationRuntimeMonitoringDataOperations
from .operations import IntegrationRuntimeStatusOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkHubsOperations
from .operations import PrivateEndpointConnectionsPrivateLinkHubOperations
from .operations import WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
from .operations import WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
from .operations import WorkspaceManagedSqlServerSecurityAlertPolicyOperations
from .operations import WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
from .operations import WorkspaceManagedSqlServerUsagesOperations
from .operations import WorkspaceManagedSqlServerRecoverableSqlPoolsOperations
from .operations import KeysOperations
from . import models


class SynapseManagementClient(SDKClient):
    """Azure Synapse Analytics Management Client

    :ivar config: Configuration for client.
    :vartype config: SynapseManagementClientConfiguration

    :ivar big_data_pools: BigDataPools operations
    :vartype big_data_pools: azure.mgmt.synapse.operations.BigDataPoolsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.synapse.operations.Operations
    :ivar ip_firewall_rules: IpFirewallRules operations
    :vartype ip_firewall_rules: azure.mgmt.synapse.operations.IpFirewallRulesOperations
    :ivar sql_pools: SqlPools operations
    :vartype sql_pools: azure.mgmt.synapse.operations.SqlPoolsOperations
    :ivar sql_pool_metadata_sync_configs: SqlPoolMetadataSyncConfigs operations
    :vartype sql_pool_metadata_sync_configs: azure.mgmt.synapse.operations.SqlPoolMetadataSyncConfigsOperations
    :ivar sql_pool_operation_results: SqlPoolOperationResults operations
    :vartype sql_pool_operation_results: azure.mgmt.synapse.operations.SqlPoolOperationResultsOperations
    :ivar sql_pool_geo_backup_policies: SqlPoolGeoBackupPolicies operations
    :vartype sql_pool_geo_backup_policies: azure.mgmt.synapse.operations.SqlPoolGeoBackupPoliciesOperations
    :ivar sql_pool_data_warehouse_user_activities: SqlPoolDataWarehouseUserActivities operations
    :vartype sql_pool_data_warehouse_user_activities: azure.mgmt.synapse.operations.SqlPoolDataWarehouseUserActivitiesOperations
    :ivar sql_pool_restore_points: SqlPoolRestorePoints operations
    :vartype sql_pool_restore_points: azure.mgmt.synapse.operations.SqlPoolRestorePointsOperations
    :ivar sql_pool_replication_links: SqlPoolReplicationLinks operations
    :vartype sql_pool_replication_links: azure.mgmt.synapse.operations.SqlPoolReplicationLinksOperations
    :ivar sql_pool_transparent_data_encryptions: SqlPoolTransparentDataEncryptions operations
    :vartype sql_pool_transparent_data_encryptions: azure.mgmt.synapse.operations.SqlPoolTransparentDataEncryptionsOperations
    :ivar sql_pool_blob_auditing_policies: SqlPoolBlobAuditingPolicies operations
    :vartype sql_pool_blob_auditing_policies: azure.mgmt.synapse.operations.SqlPoolBlobAuditingPoliciesOperations
    :ivar sql_pool_operations: SqlPoolOperations operations
    :vartype sql_pool_operations: azure.mgmt.synapse.operations.SqlPoolOperations
    :ivar sql_pool_usages: SqlPoolUsages operations
    :vartype sql_pool_usages: azure.mgmt.synapse.operations.SqlPoolUsagesOperations
    :ivar sql_pool_sensitivity_labels: SqlPoolSensitivityLabels operations
    :vartype sql_pool_sensitivity_labels: azure.mgmt.synapse.operations.SqlPoolSensitivityLabelsOperations
    :ivar sql_pool_schemas: SqlPoolSchemas operations
    :vartype sql_pool_schemas: azure.mgmt.synapse.operations.SqlPoolSchemasOperations
    :ivar sql_pool_tables: SqlPoolTables operations
    :vartype sql_pool_tables: azure.mgmt.synapse.operations.SqlPoolTablesOperations
    :ivar sql_pool_table_columns: SqlPoolTableColumns operations
    :vartype sql_pool_table_columns: azure.mgmt.synapse.operations.SqlPoolTableColumnsOperations
    :ivar sql_pool_connection_policies: SqlPoolConnectionPolicies operations
    :vartype sql_pool_connection_policies: azure.mgmt.synapse.operations.SqlPoolConnectionPoliciesOperations
    :ivar sql_pool_vulnerability_assessments: SqlPoolVulnerabilityAssessments operations
    :vartype sql_pool_vulnerability_assessments: azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentsOperations
    :ivar sql_pool_vulnerability_assessment_scans: SqlPoolVulnerabilityAssessmentScans operations
    :vartype sql_pool_vulnerability_assessment_scans: azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentScansOperations
    :ivar sql_pool_security_alert_policies: SqlPoolSecurityAlertPolicies operations
    :vartype sql_pool_security_alert_policies: azure.mgmt.synapse.operations.SqlPoolSecurityAlertPoliciesOperations
    :ivar sql_pool_vulnerability_assessment_rule_baselines: SqlPoolVulnerabilityAssessmentRuleBaselines operations
    :vartype sql_pool_vulnerability_assessment_rule_baselines: azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
    :ivar extended_sql_pool_blob_auditing_policies: ExtendedSqlPoolBlobAuditingPolicies operations
    :vartype extended_sql_pool_blob_auditing_policies: azure.mgmt.synapse.operations.ExtendedSqlPoolBlobAuditingPoliciesOperations
    :ivar data_masking_policies: DataMaskingPolicies operations
    :vartype data_masking_policies: azure.mgmt.synapse.operations.DataMaskingPoliciesOperations
    :ivar data_masking_rules: DataMaskingRules operations
    :vartype data_masking_rules: azure.mgmt.synapse.operations.DataMaskingRulesOperations
    :ivar sql_pool_columns: SqlPoolColumns operations
    :vartype sql_pool_columns: azure.mgmt.synapse.operations.SqlPoolColumnsOperations
    :ivar sql_pool_workload_group: SqlPoolWorkloadGroup operations
    :vartype sql_pool_workload_group: azure.mgmt.synapse.operations.SqlPoolWorkloadGroupOperations
    :ivar sql_pool_workload_classifier: SqlPoolWorkloadClassifier operations
    :vartype sql_pool_workload_classifier: azure.mgmt.synapse.operations.SqlPoolWorkloadClassifierOperations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: azure.mgmt.synapse.operations.WorkspacesOperations
    :ivar workspace_aad_admins: WorkspaceAadAdmins operations
    :vartype workspace_aad_admins: azure.mgmt.synapse.operations.WorkspaceAadAdminsOperations
    :ivar workspace_sql_aad_admins: WorkspaceSqlAadAdmins operations
    :vartype workspace_sql_aad_admins: azure.mgmt.synapse.operations.WorkspaceSqlAadAdminsOperations
    :ivar workspace_managed_identity_sql_control_settings: WorkspaceManagedIdentitySqlControlSettings operations
    :vartype workspace_managed_identity_sql_control_settings: azure.mgmt.synapse.operations.WorkspaceManagedIdentitySqlControlSettingsOperations
    :ivar restorable_dropped_sql_pools: RestorableDroppedSqlPools operations
    :vartype restorable_dropped_sql_pools: azure.mgmt.synapse.operations.RestorableDroppedSqlPoolsOperations
    :ivar integration_runtimes: IntegrationRuntimes operations
    :vartype integration_runtimes: azure.mgmt.synapse.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_node_ip_address: IntegrationRuntimeNodeIpAddress operations
    :vartype integration_runtime_node_ip_address: azure.mgmt.synapse.operations.IntegrationRuntimeNodeIpAddressOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadata operations
    :vartype integration_runtime_object_metadata: azure.mgmt.synapse.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodes operations
    :vartype integration_runtime_nodes: azure.mgmt.synapse.operations.IntegrationRuntimeNodesOperations
    :ivar integration_runtime_credentials: IntegrationRuntimeCredentials operations
    :vartype integration_runtime_credentials: azure.mgmt.synapse.operations.IntegrationRuntimeCredentialsOperations
    :ivar integration_runtime_connection_infos: IntegrationRuntimeConnectionInfos operations
    :vartype integration_runtime_connection_infos: azure.mgmt.synapse.operations.IntegrationRuntimeConnectionInfosOperations
    :ivar integration_runtime_auth_keys: IntegrationRuntimeAuthKeys operations
    :vartype integration_runtime_auth_keys: azure.mgmt.synapse.operations.IntegrationRuntimeAuthKeysOperations
    :ivar integration_runtime_monitoring_data: IntegrationRuntimeMonitoringData operations
    :vartype integration_runtime_monitoring_data: azure.mgmt.synapse.operations.IntegrationRuntimeMonitoringDataOperations
    :ivar integration_runtime_status: IntegrationRuntimeStatus operations
    :vartype integration_runtime_status: azure.mgmt.synapse.operations.IntegrationRuntimeStatusOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.synapse.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.synapse.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_hubs: PrivateLinkHubs operations
    :vartype private_link_hubs: azure.mgmt.synapse.operations.PrivateLinkHubsOperations
    :ivar private_endpoint_connections_private_link_hub: PrivateEndpointConnectionsPrivateLinkHub operations
    :vartype private_endpoint_connections_private_link_hub: azure.mgmt.synapse.operations.PrivateEndpointConnectionsPrivateLinkHubOperations
    :ivar workspace_managed_sql_server_blob_auditing_policies: WorkspaceManagedSqlServerBlobAuditingPolicies operations
    :vartype workspace_managed_sql_server_blob_auditing_policies: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_extended_blob_auditing_policies: WorkspaceManagedSqlServerExtendedBlobAuditingPolicies operations
    :vartype workspace_managed_sql_server_extended_blob_auditing_policies: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_security_alert_policy: WorkspaceManagedSqlServerSecurityAlertPolicy operations
    :vartype workspace_managed_sql_server_security_alert_policy: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerSecurityAlertPolicyOperations
    :ivar workspace_managed_sql_server_vulnerability_assessments: WorkspaceManagedSqlServerVulnerabilityAssessments operations
    :vartype workspace_managed_sql_server_vulnerability_assessments: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
    :ivar workspace_managed_sql_server_usages: WorkspaceManagedSqlServerUsages operations
    :vartype workspace_managed_sql_server_usages: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerUsagesOperations
    :ivar workspace_managed_sql_server_recoverable_sql_pools: WorkspaceManagedSqlServerRecoverableSqlPools operations
    :vartype workspace_managed_sql_server_recoverable_sql_pools: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerRecoverableSqlPoolsOperations
    :ivar keys: Keys operations
    :vartype keys: azure.mgmt.synapse.operations.KeysOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SynapseManagementClientConfiguration(credentials, subscription_id, base_url)
        super(SynapseManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.big_data_pools = BigDataPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.ip_firewall_rules = IpFirewallRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pools = SqlPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_metadata_sync_configs = SqlPoolMetadataSyncConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_operation_results = SqlPoolOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_geo_backup_policies = SqlPoolGeoBackupPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_data_warehouse_user_activities = SqlPoolDataWarehouseUserActivitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_restore_points = SqlPoolRestorePointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_replication_links = SqlPoolReplicationLinksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_transparent_data_encryptions = SqlPoolTransparentDataEncryptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_blob_auditing_policies = SqlPoolBlobAuditingPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_operations = SqlPoolOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_usages = SqlPoolUsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_sensitivity_labels = SqlPoolSensitivityLabelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_schemas = SqlPoolSchemasOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_tables = SqlPoolTablesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_table_columns = SqlPoolTableColumnsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_connection_policies = SqlPoolConnectionPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessments = SqlPoolVulnerabilityAssessmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessment_scans = SqlPoolVulnerabilityAssessmentScansOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_security_alert_policies = SqlPoolSecurityAlertPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessment_rule_baselines = SqlPoolVulnerabilityAssessmentRuleBaselinesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.extended_sql_pool_blob_auditing_policies = ExtendedSqlPoolBlobAuditingPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_masking_policies = DataMaskingPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.data_masking_rules = DataMaskingRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_columns = SqlPoolColumnsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_workload_group = SqlPoolWorkloadGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.sql_pool_workload_classifier = SqlPoolWorkloadClassifierOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_aad_admins = WorkspaceAadAdminsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_sql_aad_admins = WorkspaceSqlAadAdminsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_identity_sql_control_settings = WorkspaceManagedIdentitySqlControlSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restorable_dropped_sql_pools = RestorableDroppedSqlPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_node_ip_address = IntegrationRuntimeNodeIpAddressOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_credentials = IntegrationRuntimeCredentialsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_connection_infos = IntegrationRuntimeConnectionInfosOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_auth_keys = IntegrationRuntimeAuthKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_monitoring_data = IntegrationRuntimeMonitoringDataOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.integration_runtime_status = IntegrationRuntimeStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_hubs = PrivateLinkHubsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections_private_link_hub = PrivateEndpointConnectionsPrivateLinkHubOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_blob_auditing_policies = WorkspaceManagedSqlServerBlobAuditingPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_extended_blob_auditing_policies = WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_security_alert_policy = WorkspaceManagedSqlServerSecurityAlertPolicyOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_vulnerability_assessments = WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_usages = WorkspaceManagedSqlServerUsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_recoverable_sql_pools = WorkspaceManagedSqlServerRecoverableSqlPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.keys = KeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
