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
    from ._models_py3 import AFDDomain
    from ._models_py3 import AFDDomainHttpsParameters
    from ._models_py3 import AFDDomainUpdateParameters
    from ._models_py3 import AFDEndpoint
    from ._models_py3 import AFDEndpointUpdateParameters
    from ._models_py3 import AfdErrorResponse, AfdErrorResponseException
    from ._models_py3 import AFDOrigin
    from ._models_py3 import AFDOriginGroup
    from ._models_py3 import AFDOriginGroupUpdateParameters
    from ._models_py3 import AFDOriginUpdateParameters
    from ._models_py3 import AfdPurgeParameters
    from ._models_py3 import AFDStateProperties
    from ._models_py3 import CacheConfiguration
    from ._models_py3 import CacheExpirationActionParameters
    from ._models_py3 import CacheKeyQueryStringActionParameters
    from ._models_py3 import CdnCertificateSourceParameters
    from ._models_py3 import CdnEndpoint
    from ._models_py3 import CdnManagedHttpsParameters
    from ._models_py3 import CdnWebApplicationFirewallPolicy
    from ._models_py3 import CdnWebApplicationFirewallPolicyPatchParameters
    from ._models_py3 import Certificate
    from ._models_py3 import CheckNameAvailabilityInput
    from ._models_py3 import CheckNameAvailabilityOutput
    from ._models_py3 import CidrIpAddress
    from ._models_py3 import CompressionSettings
    from ._models_py3 import ContinentsResponse
    from ._models_py3 import ContinentsResponseContinentsItem
    from ._models_py3 import ContinentsResponseCountryOrRegionsItem
    from ._models_py3 import CookiesMatchConditionParameters
    from ._models_py3 import CustomDomain
    from ._models_py3 import CustomDomainHttpsParameters
    from ._models_py3 import CustomDomainParameters
    from ._models_py3 import CustomerCertificate
    from ._models_py3 import CustomerCertificateParameters
    from ._models_py3 import CustomRule
    from ._models_py3 import CustomRuleList
    from ._models_py3 import DeepCreatedOrigin
    from ._models_py3 import DeepCreatedOriginGroup
    from ._models_py3 import DeliveryRule
    from ._models_py3 import DeliveryRuleAction
    from ._models_py3 import DeliveryRuleCacheExpirationAction
    from ._models_py3 import DeliveryRuleCacheKeyQueryStringAction
    from ._models_py3 import DeliveryRuleCondition
    from ._models_py3 import DeliveryRuleCookiesCondition
    from ._models_py3 import DeliveryRuleHttpVersionCondition
    from ._models_py3 import DeliveryRuleIsDeviceCondition
    from ._models_py3 import DeliveryRulePostArgsCondition
    from ._models_py3 import DeliveryRuleQueryStringCondition
    from ._models_py3 import DeliveryRuleRemoteAddressCondition
    from ._models_py3 import DeliveryRuleRequestBodyCondition
    from ._models_py3 import DeliveryRuleRequestHeaderAction
    from ._models_py3 import DeliveryRuleRequestHeaderCondition
    from ._models_py3 import DeliveryRuleRequestMethodCondition
    from ._models_py3 import DeliveryRuleRequestSchemeCondition
    from ._models_py3 import DeliveryRuleRequestUriCondition
    from ._models_py3 import DeliveryRuleResponseHeaderAction
    from ._models_py3 import DeliveryRuleUrlFileExtensionCondition
    from ._models_py3 import DeliveryRuleUrlFileNameCondition
    from ._models_py3 import DeliveryRuleUrlPathCondition
    from ._models_py3 import DomainValidationProperties
    from ._models_py3 import EdgeNode
    from ._models_py3 import Endpoint
    from ._models_py3 import EndpointPropertiesUpdateParametersDeliveryPolicy
    from ._models_py3 import EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink
    from ._models_py3 import EndpointUpdateParameters
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import GeoFilter
    from ._models_py3 import HeaderActionParameters
    from ._models_py3 import HealthProbeParameters
    from ._models_py3 import HttpErrorRangeParameters
    from ._models_py3 import HttpVersionMatchConditionParameters
    from ._models_py3 import IpAddressGroup
    from ._models_py3 import IsDeviceMatchConditionParameters
    from ._models_py3 import KeyVaultCertificateSourceParameters
    from ._models_py3 import KeyVaultSigningKeyParameters
    from ._models_py3 import LoadBalancingSettingsParameters
    from ._models_py3 import LoadParameters
    from ._models_py3 import ManagedCertificate
    from ._models_py3 import ManagedCertificateParameters
    from ._models_py3 import ManagedRuleDefinition
    from ._models_py3 import ManagedRuleGroupDefinition
    from ._models_py3 import ManagedRuleGroupOverride
    from ._models_py3 import ManagedRuleOverride
    from ._models_py3 import ManagedRuleSet
    from ._models_py3 import ManagedRuleSetDefinition
    from ._models_py3 import ManagedRuleSetList
    from ._models_py3 import MatchCondition
    from ._models_py3 import MetricsResponse
    from ._models_py3 import MetricsResponseSeriesItem
    from ._models_py3 import MetricsResponseSeriesItemDataItem
    from ._models_py3 import MetricsResponseSeriesItemGroupsItem
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Origin
    from ._models_py3 import OriginGroup
    from ._models_py3 import OriginGroupOverrideAction
    from ._models_py3 import OriginGroupOverrideActionParameters
    from ._models_py3 import OriginGroupUpdateParameters
    from ._models_py3 import OriginUpdateParameters
    from ._models_py3 import PolicySettings
    from ._models_py3 import PostArgsMatchConditionParameters
    from ._models_py3 import Profile
    from ._models_py3 import ProfileUpdateParameters
    from ._models_py3 import ProxyResource
    from ._models_py3 import PurgeParameters
    from ._models_py3 import QueryStringMatchConditionParameters
    from ._models_py3 import RankingsResponse
    from ._models_py3 import RankingsResponseTablesItem
    from ._models_py3 import RankingsResponseTablesItemDataItem
    from ._models_py3 import RankingsResponseTablesItemDataItemMetricsItem
    from ._models_py3 import RateLimitRule
    from ._models_py3 import RateLimitRuleList
    from ._models_py3 import RemoteAddressMatchConditionParameters
    from ._models_py3 import RequestBodyMatchConditionParameters
    from ._models_py3 import RequestHeaderMatchConditionParameters
    from ._models_py3 import RequestMethodMatchConditionParameters
    from ._models_py3 import RequestSchemeMatchConditionParameters
    from ._models_py3 import RequestUriMatchConditionParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceReference
    from ._models_py3 import ResourcesResponse
    from ._models_py3 import ResourcesResponseCustomDomainsItem
    from ._models_py3 import ResourcesResponseEndpointsItem
    from ._models_py3 import ResourcesResponseEndpointsItemCustomDomainsItem
    from ._models_py3 import ResourceUsage
    from ._models_py3 import ResponseBasedOriginErrorDetectionParameters
    from ._models_py3 import Route
    from ._models_py3 import RouteUpdateParameters
    from ._models_py3 import Rule
    from ._models_py3 import RuleSet
    from ._models_py3 import RuleUpdateParameters
    from ._models_py3 import Secret
    from ._models_py3 import SecretParameters
    from ._models_py3 import SecretProperties
    from ._models_py3 import SecurityPolicy
    from ._models_py3 import SecurityPolicyParameters
    from ._models_py3 import SecurityPolicyProperties
    from ._models_py3 import SecurityPolicyWebApplicationFirewallAssociation
    from ._models_py3 import SecurityPolicyWebApplicationFirewallParameters
    from ._models_py3 import SharedPrivateLinkResourceProperties
    from ._models_py3 import Sku
    from ._models_py3 import SsoUri
    from ._models_py3 import SupportedOptimizationTypesListResult
    from ._models_py3 import SystemData
    from ._models_py3 import TrackedResource
    from ._models_py3 import UrlFileExtensionMatchConditionParameters
    from ._models_py3 import UrlFileNameMatchConditionParameters
    from ._models_py3 import UrlPathMatchConditionParameters
    from ._models_py3 import UrlRedirectAction
    from ._models_py3 import UrlRedirectActionParameters
    from ._models_py3 import UrlRewriteAction
    from ._models_py3 import UrlRewriteActionParameters
    from ._models_py3 import UrlSigningAction
    from ._models_py3 import UrlSigningActionParameters
    from ._models_py3 import UrlSigningKey
    from ._models_py3 import UrlSigningKeyParameters
    from ._models_py3 import UrlSigningParamIdentifier
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UserManagedHttpsParameters
    from ._models_py3 import ValidateCustomDomainInput
    from ._models_py3 import ValidateCustomDomainOutput
    from ._models_py3 import ValidateProbeInput
    from ._models_py3 import ValidateProbeOutput
    from ._models_py3 import ValidateSecretInput
    from ._models_py3 import ValidateSecretOutput
    from ._models_py3 import ValidationToken
    from ._models_py3 import WafMetricsResponse
    from ._models_py3 import WafMetricsResponseSeriesItem
    from ._models_py3 import WafMetricsResponseSeriesItemDataItem
    from ._models_py3 import WafMetricsResponseSeriesItemGroupsItem
    from ._models_py3 import WafRankingsResponse
    from ._models_py3 import WafRankingsResponseDataItem
    from ._models_py3 import WafRankingsResponseDataItemMetricsItem
except (SyntaxError, ImportError):
    from ._models import AFDDomain
    from ._models import AFDDomainHttpsParameters
    from ._models import AFDDomainUpdateParameters
    from ._models import AFDEndpoint
    from ._models import AFDEndpointUpdateParameters
    from ._models import AfdErrorResponse, AfdErrorResponseException
    from ._models import AFDOrigin
    from ._models import AFDOriginGroup
    from ._models import AFDOriginGroupUpdateParameters
    from ._models import AFDOriginUpdateParameters
    from ._models import AfdPurgeParameters
    from ._models import AFDStateProperties
    from ._models import CacheConfiguration
    from ._models import CacheExpirationActionParameters
    from ._models import CacheKeyQueryStringActionParameters
    from ._models import CdnCertificateSourceParameters
    from ._models import CdnEndpoint
    from ._models import CdnManagedHttpsParameters
    from ._models import CdnWebApplicationFirewallPolicy
    from ._models import CdnWebApplicationFirewallPolicyPatchParameters
    from ._models import Certificate
    from ._models import CheckNameAvailabilityInput
    from ._models import CheckNameAvailabilityOutput
    from ._models import CidrIpAddress
    from ._models import CompressionSettings
    from ._models import ContinentsResponse
    from ._models import ContinentsResponseContinentsItem
    from ._models import ContinentsResponseCountryOrRegionsItem
    from ._models import CookiesMatchConditionParameters
    from ._models import CustomDomain
    from ._models import CustomDomainHttpsParameters
    from ._models import CustomDomainParameters
    from ._models import CustomerCertificate
    from ._models import CustomerCertificateParameters
    from ._models import CustomRule
    from ._models import CustomRuleList
    from ._models import DeepCreatedOrigin
    from ._models import DeepCreatedOriginGroup
    from ._models import DeliveryRule
    from ._models import DeliveryRuleAction
    from ._models import DeliveryRuleCacheExpirationAction
    from ._models import DeliveryRuleCacheKeyQueryStringAction
    from ._models import DeliveryRuleCondition
    from ._models import DeliveryRuleCookiesCondition
    from ._models import DeliveryRuleHttpVersionCondition
    from ._models import DeliveryRuleIsDeviceCondition
    from ._models import DeliveryRulePostArgsCondition
    from ._models import DeliveryRuleQueryStringCondition
    from ._models import DeliveryRuleRemoteAddressCondition
    from ._models import DeliveryRuleRequestBodyCondition
    from ._models import DeliveryRuleRequestHeaderAction
    from ._models import DeliveryRuleRequestHeaderCondition
    from ._models import DeliveryRuleRequestMethodCondition
    from ._models import DeliveryRuleRequestSchemeCondition
    from ._models import DeliveryRuleRequestUriCondition
    from ._models import DeliveryRuleResponseHeaderAction
    from ._models import DeliveryRuleUrlFileExtensionCondition
    from ._models import DeliveryRuleUrlFileNameCondition
    from ._models import DeliveryRuleUrlPathCondition
    from ._models import DomainValidationProperties
    from ._models import EdgeNode
    from ._models import Endpoint
    from ._models import EndpointPropertiesUpdateParametersDeliveryPolicy
    from ._models import EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink
    from ._models import EndpointUpdateParameters
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import GeoFilter
    from ._models import HeaderActionParameters
    from ._models import HealthProbeParameters
    from ._models import HttpErrorRangeParameters
    from ._models import HttpVersionMatchConditionParameters
    from ._models import IpAddressGroup
    from ._models import IsDeviceMatchConditionParameters
    from ._models import KeyVaultCertificateSourceParameters
    from ._models import KeyVaultSigningKeyParameters
    from ._models import LoadBalancingSettingsParameters
    from ._models import LoadParameters
    from ._models import ManagedCertificate
    from ._models import ManagedCertificateParameters
    from ._models import ManagedRuleDefinition
    from ._models import ManagedRuleGroupDefinition
    from ._models import ManagedRuleGroupOverride
    from ._models import ManagedRuleOverride
    from ._models import ManagedRuleSet
    from ._models import ManagedRuleSetDefinition
    from ._models import ManagedRuleSetList
    from ._models import MatchCondition
    from ._models import MetricsResponse
    from ._models import MetricsResponseSeriesItem
    from ._models import MetricsResponseSeriesItemDataItem
    from ._models import MetricsResponseSeriesItemGroupsItem
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Origin
    from ._models import OriginGroup
    from ._models import OriginGroupOverrideAction
    from ._models import OriginGroupOverrideActionParameters
    from ._models import OriginGroupUpdateParameters
    from ._models import OriginUpdateParameters
    from ._models import PolicySettings
    from ._models import PostArgsMatchConditionParameters
    from ._models import Profile
    from ._models import ProfileUpdateParameters
    from ._models import ProxyResource
    from ._models import PurgeParameters
    from ._models import QueryStringMatchConditionParameters
    from ._models import RankingsResponse
    from ._models import RankingsResponseTablesItem
    from ._models import RankingsResponseTablesItemDataItem
    from ._models import RankingsResponseTablesItemDataItemMetricsItem
    from ._models import RateLimitRule
    from ._models import RateLimitRuleList
    from ._models import RemoteAddressMatchConditionParameters
    from ._models import RequestBodyMatchConditionParameters
    from ._models import RequestHeaderMatchConditionParameters
    from ._models import RequestMethodMatchConditionParameters
    from ._models import RequestSchemeMatchConditionParameters
    from ._models import RequestUriMatchConditionParameters
    from ._models import Resource
    from ._models import ResourceReference
    from ._models import ResourcesResponse
    from ._models import ResourcesResponseCustomDomainsItem
    from ._models import ResourcesResponseEndpointsItem
    from ._models import ResourcesResponseEndpointsItemCustomDomainsItem
    from ._models import ResourceUsage
    from ._models import ResponseBasedOriginErrorDetectionParameters
    from ._models import Route
    from ._models import RouteUpdateParameters
    from ._models import Rule
    from ._models import RuleSet
    from ._models import RuleUpdateParameters
    from ._models import Secret
    from ._models import SecretParameters
    from ._models import SecretProperties
    from ._models import SecurityPolicy
    from ._models import SecurityPolicyParameters
    from ._models import SecurityPolicyProperties
    from ._models import SecurityPolicyWebApplicationFirewallAssociation
    from ._models import SecurityPolicyWebApplicationFirewallParameters
    from ._models import SharedPrivateLinkResourceProperties
    from ._models import Sku
    from ._models import SsoUri
    from ._models import SupportedOptimizationTypesListResult
    from ._models import SystemData
    from ._models import TrackedResource
    from ._models import UrlFileExtensionMatchConditionParameters
    from ._models import UrlFileNameMatchConditionParameters
    from ._models import UrlPathMatchConditionParameters
    from ._models import UrlRedirectAction
    from ._models import UrlRedirectActionParameters
    from ._models import UrlRewriteAction
    from ._models import UrlRewriteActionParameters
    from ._models import UrlSigningAction
    from ._models import UrlSigningActionParameters
    from ._models import UrlSigningKey
    from ._models import UrlSigningKeyParameters
    from ._models import UrlSigningParamIdentifier
    from ._models import Usage
    from ._models import UsageName
    from ._models import UserManagedHttpsParameters
    from ._models import ValidateCustomDomainInput
    from ._models import ValidateCustomDomainOutput
    from ._models import ValidateProbeInput
    from ._models import ValidateProbeOutput
    from ._models import ValidateSecretInput
    from ._models import ValidateSecretOutput
    from ._models import ValidationToken
    from ._models import WafMetricsResponse
    from ._models import WafMetricsResponseSeriesItem
    from ._models import WafMetricsResponseSeriesItemDataItem
    from ._models import WafMetricsResponseSeriesItemGroupsItem
    from ._models import WafRankingsResponse
    from ._models import WafRankingsResponseDataItem
    from ._models import WafRankingsResponseDataItemMetricsItem
from ._paged_models import AFDDomainPaged
from ._paged_models import AFDEndpointPaged
from ._paged_models import AFDOriginGroupPaged
from ._paged_models import AFDOriginPaged
from ._paged_models import CdnWebApplicationFirewallPolicyPaged
from ._paged_models import CustomDomainPaged
from ._paged_models import EdgeNodePaged
from ._paged_models import EndpointPaged
from ._paged_models import ManagedRuleSetDefinitionPaged
from ._paged_models import OperationPaged
from ._paged_models import OriginGroupPaged
from ._paged_models import OriginPaged
from ._paged_models import ProfilePaged
from ._paged_models import ResourceUsagePaged
from ._paged_models import RoutePaged
from ._paged_models import RulePaged
from ._paged_models import RuleSetPaged
from ._paged_models import SecretPaged
from ._paged_models import SecurityPolicyPaged
from ._paged_models import UsagePaged
from ._cdn_management_client_enums import (
    SkuName,
    ProfileResourceState,
    OptimizationType,
    HealthProbeRequestType,
    ProbeProtocol,
    ResponseBasedDetectedErrorTypes,
    EndpointResourceState,
    QueryStringCachingBehavior,
    GeoFilterActions,
    RemoteAddressOperator,
    Transform,
    QueryStringOperator,
    PostArgsOperator,
    RequestUriOperator,
    RequestHeaderOperator,
    RequestBodyOperator,
    UrlPathOperator,
    UrlFileExtensionOperator,
    UrlFileNameOperator,
    CookiesOperator,
    RedirectType,
    DestinationProtocol,
    Algorithm,
    ParamIndicator,
    RouteType,
    ForwardingProtocol,
    QueryStringBehavior,
    DynamicCompressionEnabled,
    HeaderAction,
    CacheBehavior,
    OriginResourceState,
    PrivateEndpointStatus,
    OriginGroupResourceState,
    CustomDomainResourceState,
    CustomHttpsProvisioningState,
    CustomHttpsProvisioningSubstate,
    ProtocolType,
    MinimumTlsVersion,
    CertificateType,
    ResourceType,
    IdentityType,
    ValidateSecretType,
    Status,
    AfdCertificateType,
    AfdMinimumTlsVersion,
    AfdProvisioningState,
    DeploymentStatus,
    DomainValidationState,
    EnabledState,
    AFDEndpointProtocols,
    SharedPrivateLinkResourceStatus,
    AfdQueryStringCachingBehavior,
    LinkToDefaultDomain,
    HttpsRedirect,
    MatchProcessingBehavior,
    PolicyEnabledState,
    PolicyMode,
    CustomRuleEnabledState,
    MatchVariable,
    Operator,
    TransformType,
    ActionType,
    ManagedRuleEnabledState,
    ProvisioningState,
    PolicyResourceState,
)

__all__ = [
    'AFDDomain',
    'AFDDomainHttpsParameters',
    'AFDDomainUpdateParameters',
    'AFDEndpoint',
    'AFDEndpointUpdateParameters',
    'AfdErrorResponse', 'AfdErrorResponseException',
    'AFDOrigin',
    'AFDOriginGroup',
    'AFDOriginGroupUpdateParameters',
    'AFDOriginUpdateParameters',
    'AfdPurgeParameters',
    'AFDStateProperties',
    'CacheConfiguration',
    'CacheExpirationActionParameters',
    'CacheKeyQueryStringActionParameters',
    'CdnCertificateSourceParameters',
    'CdnEndpoint',
    'CdnManagedHttpsParameters',
    'CdnWebApplicationFirewallPolicy',
    'CdnWebApplicationFirewallPolicyPatchParameters',
    'Certificate',
    'CheckNameAvailabilityInput',
    'CheckNameAvailabilityOutput',
    'CidrIpAddress',
    'CompressionSettings',
    'ContinentsResponse',
    'ContinentsResponseContinentsItem',
    'ContinentsResponseCountryOrRegionsItem',
    'CookiesMatchConditionParameters',
    'CustomDomain',
    'CustomDomainHttpsParameters',
    'CustomDomainParameters',
    'CustomerCertificate',
    'CustomerCertificateParameters',
    'CustomRule',
    'CustomRuleList',
    'DeepCreatedOrigin',
    'DeepCreatedOriginGroup',
    'DeliveryRule',
    'DeliveryRuleAction',
    'DeliveryRuleCacheExpirationAction',
    'DeliveryRuleCacheKeyQueryStringAction',
    'DeliveryRuleCondition',
    'DeliveryRuleCookiesCondition',
    'DeliveryRuleHttpVersionCondition',
    'DeliveryRuleIsDeviceCondition',
    'DeliveryRulePostArgsCondition',
    'DeliveryRuleQueryStringCondition',
    'DeliveryRuleRemoteAddressCondition',
    'DeliveryRuleRequestBodyCondition',
    'DeliveryRuleRequestHeaderAction',
    'DeliveryRuleRequestHeaderCondition',
    'DeliveryRuleRequestMethodCondition',
    'DeliveryRuleRequestSchemeCondition',
    'DeliveryRuleRequestUriCondition',
    'DeliveryRuleResponseHeaderAction',
    'DeliveryRuleUrlFileExtensionCondition',
    'DeliveryRuleUrlFileNameCondition',
    'DeliveryRuleUrlPathCondition',
    'DomainValidationProperties',
    'EdgeNode',
    'Endpoint',
    'EndpointPropertiesUpdateParametersDeliveryPolicy',
    'EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink',
    'EndpointUpdateParameters',
    'ErrorResponse', 'ErrorResponseException',
    'GeoFilter',
    'HeaderActionParameters',
    'HealthProbeParameters',
    'HttpErrorRangeParameters',
    'HttpVersionMatchConditionParameters',
    'IpAddressGroup',
    'IsDeviceMatchConditionParameters',
    'KeyVaultCertificateSourceParameters',
    'KeyVaultSigningKeyParameters',
    'LoadBalancingSettingsParameters',
    'LoadParameters',
    'ManagedCertificate',
    'ManagedCertificateParameters',
    'ManagedRuleDefinition',
    'ManagedRuleGroupDefinition',
    'ManagedRuleGroupOverride',
    'ManagedRuleOverride',
    'ManagedRuleSet',
    'ManagedRuleSetDefinition',
    'ManagedRuleSetList',
    'MatchCondition',
    'MetricsResponse',
    'MetricsResponseSeriesItem',
    'MetricsResponseSeriesItemDataItem',
    'MetricsResponseSeriesItemGroupsItem',
    'Operation',
    'OperationDisplay',
    'Origin',
    'OriginGroup',
    'OriginGroupOverrideAction',
    'OriginGroupOverrideActionParameters',
    'OriginGroupUpdateParameters',
    'OriginUpdateParameters',
    'PolicySettings',
    'PostArgsMatchConditionParameters',
    'Profile',
    'ProfileUpdateParameters',
    'ProxyResource',
    'PurgeParameters',
    'QueryStringMatchConditionParameters',
    'RankingsResponse',
    'RankingsResponseTablesItem',
    'RankingsResponseTablesItemDataItem',
    'RankingsResponseTablesItemDataItemMetricsItem',
    'RateLimitRule',
    'RateLimitRuleList',
    'RemoteAddressMatchConditionParameters',
    'RequestBodyMatchConditionParameters',
    'RequestHeaderMatchConditionParameters',
    'RequestMethodMatchConditionParameters',
    'RequestSchemeMatchConditionParameters',
    'RequestUriMatchConditionParameters',
    'Resource',
    'ResourceReference',
    'ResourcesResponse',
    'ResourcesResponseCustomDomainsItem',
    'ResourcesResponseEndpointsItem',
    'ResourcesResponseEndpointsItemCustomDomainsItem',
    'ResourceUsage',
    'ResponseBasedOriginErrorDetectionParameters',
    'Route',
    'RouteUpdateParameters',
    'Rule',
    'RuleSet',
    'RuleUpdateParameters',
    'Secret',
    'SecretParameters',
    'SecretProperties',
    'SecurityPolicy',
    'SecurityPolicyParameters',
    'SecurityPolicyProperties',
    'SecurityPolicyWebApplicationFirewallAssociation',
    'SecurityPolicyWebApplicationFirewallParameters',
    'SharedPrivateLinkResourceProperties',
    'Sku',
    'SsoUri',
    'SupportedOptimizationTypesListResult',
    'SystemData',
    'TrackedResource',
    'UrlFileExtensionMatchConditionParameters',
    'UrlFileNameMatchConditionParameters',
    'UrlPathMatchConditionParameters',
    'UrlRedirectAction',
    'UrlRedirectActionParameters',
    'UrlRewriteAction',
    'UrlRewriteActionParameters',
    'UrlSigningAction',
    'UrlSigningActionParameters',
    'UrlSigningKey',
    'UrlSigningKeyParameters',
    'UrlSigningParamIdentifier',
    'Usage',
    'UsageName',
    'UserManagedHttpsParameters',
    'ValidateCustomDomainInput',
    'ValidateCustomDomainOutput',
    'ValidateProbeInput',
    'ValidateProbeOutput',
    'ValidateSecretInput',
    'ValidateSecretOutput',
    'ValidationToken',
    'WafMetricsResponse',
    'WafMetricsResponseSeriesItem',
    'WafMetricsResponseSeriesItemDataItem',
    'WafMetricsResponseSeriesItemGroupsItem',
    'WafRankingsResponse',
    'WafRankingsResponseDataItem',
    'WafRankingsResponseDataItemMetricsItem',
    'ProfilePaged',
    'ResourceUsagePaged',
    'EndpointPaged',
    'OriginPaged',
    'OriginGroupPaged',
    'CustomDomainPaged',
    'OperationPaged',
    'EdgeNodePaged',
    'UsagePaged',
    'AFDDomainPaged',
    'AFDEndpointPaged',
    'AFDOriginGroupPaged',
    'AFDOriginPaged',
    'RoutePaged',
    'RuleSetPaged',
    'RulePaged',
    'SecurityPolicyPaged',
    'SecretPaged',
    'CdnWebApplicationFirewallPolicyPaged',
    'ManagedRuleSetDefinitionPaged',
    'SkuName',
    'ProfileResourceState',
    'OptimizationType',
    'HealthProbeRequestType',
    'ProbeProtocol',
    'ResponseBasedDetectedErrorTypes',
    'EndpointResourceState',
    'QueryStringCachingBehavior',
    'GeoFilterActions',
    'RemoteAddressOperator',
    'Transform',
    'QueryStringOperator',
    'PostArgsOperator',
    'RequestUriOperator',
    'RequestHeaderOperator',
    'RequestBodyOperator',
    'UrlPathOperator',
    'UrlFileExtensionOperator',
    'UrlFileNameOperator',
    'CookiesOperator',
    'RedirectType',
    'DestinationProtocol',
    'Algorithm',
    'ParamIndicator',
    'RouteType',
    'ForwardingProtocol',
    'QueryStringBehavior',
    'DynamicCompressionEnabled',
    'HeaderAction',
    'CacheBehavior',
    'OriginResourceState',
    'PrivateEndpointStatus',
    'OriginGroupResourceState',
    'CustomDomainResourceState',
    'CustomHttpsProvisioningState',
    'CustomHttpsProvisioningSubstate',
    'ProtocolType',
    'MinimumTlsVersion',
    'CertificateType',
    'ResourceType',
    'IdentityType',
    'ValidateSecretType',
    'Status',
    'AfdCertificateType',
    'AfdMinimumTlsVersion',
    'AfdProvisioningState',
    'DeploymentStatus',
    'DomainValidationState',
    'EnabledState',
    'AFDEndpointProtocols',
    'SharedPrivateLinkResourceStatus',
    'AfdQueryStringCachingBehavior',
    'LinkToDefaultDomain',
    'HttpsRedirect',
    'MatchProcessingBehavior',
    'PolicyEnabledState',
    'PolicyMode',
    'CustomRuleEnabledState',
    'MatchVariable',
    'Operator',
    'TransformType',
    'ActionType',
    'ManagedRuleEnabledState',
    'ProvisioningState',
    'PolicyResourceState',
]
