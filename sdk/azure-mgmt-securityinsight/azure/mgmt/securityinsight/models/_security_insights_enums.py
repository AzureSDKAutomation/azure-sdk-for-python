# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AlertRuleKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the alert rule
    """

    SCHEDULED = "Scheduled"
    MICROSOFT_SECURITY_INCIDENT_CREATION = "MicrosoftSecurityIncidentCreation"
    FUSION = "Fusion"

class AlertSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The severity of the alert
    """

    HIGH = "High"  #: High severity.
    MEDIUM = "Medium"  #: Medium severity.
    LOW = "Low"  #: Low severity.
    INFORMATIONAL = "Informational"  #: Informational severity.

class AttackTactic(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The severity for alerts created by this alert rule.
    """

    INITIAL_ACCESS = "InitialAccess"
    EXECUTION = "Execution"
    PERSISTENCE = "Persistence"
    PRIVILEGE_ESCALATION = "PrivilegeEscalation"
    DEFENSE_EVASION = "DefenseEvasion"
    CREDENTIAL_ACCESS = "CredentialAccess"
    DISCOVERY = "Discovery"
    LATERAL_MOVEMENT = "LateralMovement"
    COLLECTION = "Collection"
    EXFILTRATION = "Exfiltration"
    COMMAND_AND_CONTROL = "CommandAndControl"
    IMPACT = "Impact"

class CaseSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The severity of the incident
    """

    CRITICAL = "Critical"  #: Critical severity.
    HIGH = "High"  #: High severity.
    MEDIUM = "Medium"  #: Medium severity.
    LOW = "Low"  #: Low severity.
    INFORMATIONAL = "Informational"  #: Informational severity.

class DataConnectorKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the data connector
    """

    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    AZURE_SECURITY_CENTER = "AzureSecurityCenter"
    MICROSOFT_CLOUD_APP_SECURITY = "MicrosoftCloudAppSecurity"
    THREAT_INTELLIGENCE = "ThreatIntelligence"
    OFFICE365 = "Office365"
    AMAZON_WEB_SERVICES_CLOUD_TRAIL = "AmazonWebServicesCloudTrail"
    AZURE_ADVANCED_THREAT_PROTECTION = "AzureAdvancedThreatProtection"
    MICROSOFT_DEFENDER_ADVANCED_THREAT_PROTECTION = "MicrosoftDefenderAdvancedThreatProtection"

class DataTypeState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describe whether this data type connection is enabled or not.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class IncidentClassification(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason the incident was closed
    """

    UNDETERMINED = "Undetermined"  #: Incident classification was undetermined.
    TRUE_POSITIVE = "TruePositive"  #: Incident was true positive.
    BENIGN_POSITIVE = "BenignPositive"  #: Incident was benign positive.
    FALSE_POSITIVE = "FalsePositive"  #: Incident was false positive.

class IncidentClassificationReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The classification reason the incident was closed with
    """

    SUSPICIOUS_ACTIVITY = "SuspiciousActivity"  #: Classification reason was suspicious activity.
    SUSPICIOUS_BUT_EXPECTED = "SuspiciousButExpected"  #: Classification reason was suspicious but expected.
    INCORRECT_ALERT_LOGIC = "IncorrectAlertLogic"  #: Classification reason was incorrect alert logic.
    INACCURATE_DATA = "InaccurateData"  #: Classification reason was inaccurate data.

class IncidentLabelType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the label
    """

    USER = "User"  #: Label manually created by a user.
    SYSTEM = "System"  #: Label automatically created by the system.

class IncidentSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The severity of the incident
    """

    HIGH = "High"  #: High severity.
    MEDIUM = "Medium"  #: Medium severity.
    LOW = "Low"  #: Low severity.
    INFORMATIONAL = "Informational"  #: Informational severity.

class IncidentStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the incident
    """

    NEW = "New"  #: An active incident which isn't being handled currently.
    ACTIVE = "Active"  #: An active incident which is being handled.
    CLOSED = "Closed"  #: A non-active incident.

class LicenseStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Determines whether the tenant has ATP (Advanced Threat Protection) license.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class MicrosoftSecurityProductName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The alerts' productName on which the cases will be generated
    """

    MICROSOFT_CLOUD_APP_SECURITY = "Microsoft Cloud App Security"
    AZURE_SECURITY_CENTER = "Azure Security Center"
    AZURE_ADVANCED_THREAT_PROTECTION = "Azure Advanced Threat Protection"
    AZURE_ACTIVE_DIRECTORY_IDENTITY_PROTECTION = "Azure Active Directory Identity Protection"
    AZURE_SECURITY_CENTER_FOR_IO_T = "Azure Security Center for IoT"

class SettingKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the setting
    """

    UEBA_SETTINGS = "UebaSettings"
    TOGGLE_SETTINGS = "ToggleSettings"

class StatusInMcas(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Determines whether User and Entity Behavior Analytics is enabled from MCAS (Microsoft Cloud App
    Security).
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class TemplateStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The alert rule template status.
    """

    INSTALLED = "Installed"  #: Alert rule template installed. and can not use more then once.
    AVAILABLE = "Available"  #: Alert rule template is available.
    NOT_AVAILABLE = "NotAvailable"  #: Alert rule template is not available.

class TriggerOperator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operation against the threshold that triggers alert rule.
    """

    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    EQUAL = "Equal"
    NOT_EQUAL = "NotEqual"
