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

from enum import Enum


class ApplicationGatewayProtocol(str, Enum):

    http = "Http"
    https = "Https"


class ProvisioningState(str, Enum):

    succeeded = "Succeeded"
    updating = "Updating"
    deleting = "Deleting"
    failed = "Failed"


class IPAllocationMethod(str, Enum):

    static = "Static"
    dynamic = "Dynamic"


class IPVersion(str, Enum):

    ipv4 = "IPv4"
    ipv6 = "IPv6"


class SecurityRuleProtocol(str, Enum):

    tcp = "Tcp"
    udp = "Udp"
    icmp = "Icmp"
    esp = "Esp"
    asterisk = "*"
    ah = "Ah"


class SecurityRuleAccess(str, Enum):

    allow = "Allow"
    deny = "Deny"


class SecurityRuleDirection(str, Enum):

    inbound = "Inbound"
    outbound = "Outbound"


class FlowLogFormatType(str, Enum):

    json = "JSON"


class RouteNextHopType(str, Enum):

    virtual_network_gateway = "VirtualNetworkGateway"
    vnet_local = "VnetLocal"
    internet = "Internet"
    virtual_appliance = "VirtualAppliance"
    none = "None"


class PublicIPAddressSkuName(str, Enum):

    basic = "Basic"
    standard = "Standard"


class PublicIPAddressSkuTier(str, Enum):

    regional = "Regional"
    global_enum = "Global"


class DdosSettingsProtectionCoverage(str, Enum):

    basic = "Basic"
    standard = "Standard"


class TransportProtocol(str, Enum):

    udp = "Udp"
    tcp = "Tcp"
    all = "All"


class ApplicationGatewayCookieBasedAffinity(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ApplicationGatewayBackendHealthServerHealth(str, Enum):

    unknown = "Unknown"
    up = "Up"
    down = "Down"
    partial = "Partial"
    draining = "Draining"


class ApplicationGatewaySkuName(str, Enum):

    standard_small = "Standard_Small"
    standard_medium = "Standard_Medium"
    standard_large = "Standard_Large"
    waf_medium = "WAF_Medium"
    waf_large = "WAF_Large"
    standard_v2 = "Standard_v2"
    waf_v2 = "WAF_v2"


class ApplicationGatewayTier(str, Enum):

    standard = "Standard"
    waf = "WAF"
    standard_v2 = "Standard_v2"
    waf_v2 = "WAF_v2"


class ApplicationGatewaySslProtocol(str, Enum):

    tl_sv1_0 = "TLSv1_0"
    tl_sv1_1 = "TLSv1_1"
    tl_sv1_2 = "TLSv1_2"


class ApplicationGatewaySslPolicyType(str, Enum):

    predefined = "Predefined"
    custom = "Custom"


class ApplicationGatewaySslPolicyName(str, Enum):

    app_gw_ssl_policy20150501 = "AppGwSslPolicy20150501"
    app_gw_ssl_policy20170401 = "AppGwSslPolicy20170401"
    app_gw_ssl_policy20170401_s = "AppGwSslPolicy20170401S"


class ApplicationGatewaySslCipherSuite(str, Enum):

    tls_ecdhe_rsa_with_aes_256_cbc_sha384 = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    tls_ecdhe_rsa_with_aes_128_cbc_sha256 = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
    tls_ecdhe_rsa_with_aes_256_cbc_sha = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
    tls_ecdhe_rsa_with_aes_128_cbc_sha = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
    tls_dhe_rsa_with_aes_256_gcm_sha384 = "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384"
    tls_dhe_rsa_with_aes_128_gcm_sha256 = "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
    tls_dhe_rsa_with_aes_256_cbc_sha = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA"
    tls_dhe_rsa_with_aes_128_cbc_sha = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA"
    tls_rsa_with_aes_256_gcm_sha384 = "TLS_RSA_WITH_AES_256_GCM_SHA384"
    tls_rsa_with_aes_128_gcm_sha256 = "TLS_RSA_WITH_AES_128_GCM_SHA256"
    tls_rsa_with_aes_256_cbc_sha256 = "TLS_RSA_WITH_AES_256_CBC_SHA256"
    tls_rsa_with_aes_128_cbc_sha256 = "TLS_RSA_WITH_AES_128_CBC_SHA256"
    tls_rsa_with_aes_256_cbc_sha = "TLS_RSA_WITH_AES_256_CBC_SHA"
    tls_rsa_with_aes_128_cbc_sha = "TLS_RSA_WITH_AES_128_CBC_SHA"
    tls_ecdhe_ecdsa_with_aes_256_gcm_sha384 = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
    tls_ecdhe_ecdsa_with_aes_128_gcm_sha256 = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
    tls_ecdhe_ecdsa_with_aes_256_cbc_sha384 = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384"
    tls_ecdhe_ecdsa_with_aes_128_cbc_sha256 = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
    tls_ecdhe_ecdsa_with_aes_256_cbc_sha = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA"
    tls_ecdhe_ecdsa_with_aes_128_cbc_sha = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA"
    tls_dhe_dss_with_aes_256_cbc_sha256 = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256"
    tls_dhe_dss_with_aes_128_cbc_sha256 = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256"
    tls_dhe_dss_with_aes_256_cbc_sha = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA"
    tls_dhe_dss_with_aes_128_cbc_sha = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA"
    tls_rsa_with_3_des_ede_cbc_sha = "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
    tls_dhe_dss_with_3_des_ede_cbc_sha = "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA"
    tls_ecdhe_rsa_with_aes_128_gcm_sha256 = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
    tls_ecdhe_rsa_with_aes_256_gcm_sha384 = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"


class ApplicationGatewayCustomErrorStatusCode(str, Enum):

    http_status403 = "HttpStatus403"
    http_status502 = "HttpStatus502"


class ApplicationGatewayRequestRoutingRuleType(str, Enum):

    basic = "Basic"
    path_based_routing = "PathBasedRouting"


class ApplicationGatewayRedirectType(str, Enum):

    permanent = "Permanent"
    found = "Found"
    see_other = "SeeOther"
    temporary = "Temporary"


class ApplicationGatewayOperationalState(str, Enum):

    stopped = "Stopped"
    starting = "Starting"
    running = "Running"
    stopping = "Stopping"


class ApplicationGatewayFirewallMode(str, Enum):

    detection = "Detection"
    prevention = "Prevention"


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"


class ExtendedLocationTypes(str, Enum):

    edge_zone = "EdgeZone"


class AzureFirewallRCActionType(str, Enum):

    allow = "Allow"
    deny = "Deny"


class AzureFirewallApplicationRuleProtocolType(str, Enum):

    http = "Http"
    https = "Https"
    mssql = "Mssql"


class AzureFirewallNatRCActionType(str, Enum):

    snat = "Snat"
    dnat = "Dnat"


class AzureFirewallNetworkRuleProtocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"
    any = "Any"
    icmp = "ICMP"


class AzureFirewallThreatIntelMode(str, Enum):

    alert = "Alert"
    deny = "Deny"
    off = "Off"


class AzureFirewallSkuName(str, Enum):

    azfw_vnet = "AZFW_VNet"
    azfw_hub = "AZFW_Hub"


class AzureFirewallSkuTier(str, Enum):

    standard = "Standard"
    premium = "Premium"


class BastionConnectProtocol(str, Enum):

    ssh = "SSH"
    rdp = "RDP"


class CommissionedState(str, Enum):

    provisioning = "Provisioning"
    provisioned = "Provisioned"
    commissioning = "Commissioning"
    commissioned = "Commissioned"
    decommissioning = "Decommissioning"
    deprovisioning = "Deprovisioning"


class DdosCustomPolicyProtocol(str, Enum):

    tcp = "Tcp"
    udp = "Udp"
    syn = "Syn"


class DdosCustomPolicyTriggerSensitivityOverride(str, Enum):

    relaxed = "Relaxed"
    low = "Low"
    default = "Default"
    high = "High"


class ProtocolType(str, Enum):

    do_not_use = "DoNotUse"
    icmp = "Icmp"
    tcp = "Tcp"
    udp = "Udp"
    gre = "Gre"
    esp = "Esp"
    ah = "Ah"
    vxlan = "Vxlan"
    all = "All"


class AuthorizationUseStatus(str, Enum):

    available = "Available"
    in_use = "InUse"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum):

    not_configured = "NotConfigured"
    configuring = "Configuring"
    configured = "Configured"
    validation_needed = "ValidationNeeded"


class ExpressRouteCircuitPeeringState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class ExpressRoutePeeringType(str, Enum):

    azure_public_peering = "AzurePublicPeering"
    azure_private_peering = "AzurePrivatePeering"
    microsoft_peering = "MicrosoftPeering"


class ExpressRoutePeeringState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class CircuitConnectionStatus(str, Enum):

    connected = "Connected"
    connecting = "Connecting"
    disconnected = "Disconnected"


class ExpressRouteCircuitSkuTier(str, Enum):

    standard = "Standard"
    premium = "Premium"
    basic = "Basic"
    local = "Local"


class ExpressRouteCircuitSkuFamily(str, Enum):

    unlimited_data = "UnlimitedData"
    metered_data = "MeteredData"


class ServiceProviderProvisioningState(str, Enum):

    not_provisioned = "NotProvisioned"
    provisioning = "Provisioning"
    provisioned = "Provisioned"
    deprovisioning = "Deprovisioning"


class ExpressRouteLinkMacSecCipher(str, Enum):

    gcm_aes256 = "GcmAes256"
    gcm_aes128 = "GcmAes128"
    gcm_aes_xpn128 = "GcmAesXpn128"
    gcm_aes_xpn256 = "GcmAesXpn256"


class ExpressRouteLinkMacSecSciState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class ExpressRouteLinkConnectorType(str, Enum):

    lc = "LC"
    sc = "SC"


class ExpressRouteLinkAdminState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ExpressRoutePortsEncapsulation(str, Enum):

    dot1_q = "Dot1Q"
    qin_q = "QinQ"


class FirewallPolicyIntrusionDetectionStateType(str, Enum):

    off = "Off"
    alert = "Alert"
    deny = "Deny"


class FirewallPolicyIntrusionDetectionProtocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"
    icmp = "ICMP"
    any = "ANY"


class FirewallPolicySkuTier(str, Enum):

    standard = "Standard"
    premium = "Premium"


class FirewallPolicyNatRuleCollectionActionType(str, Enum):

    dnat = "DNAT"


class FirewallPolicyFilterRuleCollectionActionType(str, Enum):

    allow = "Allow"
    deny = "Deny"


class FirewallPolicyRuleApplicationProtocolType(str, Enum):

    http = "Http"
    https = "Https"


class FirewallPolicyRuleNetworkProtocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"
    any = "Any"
    icmp = "ICMP"


class IpAllocationType(str, Enum):

    undefined = "Undefined"
    hypernet = "Hypernet"


class LoadBalancerSkuName(str, Enum):

    basic = "Basic"
    standard = "Standard"


class LoadBalancerSkuTier(str, Enum):

    regional = "Regional"
    global_enum = "Global"


class LoadDistribution(str, Enum):

    default = "Default"
    source_ip = "SourceIP"
    source_ip_protocol = "SourceIPProtocol"


class ProbeProtocol(str, Enum):

    http = "Http"
    tcp = "Tcp"
    https = "Https"


class LoadBalancerOutboundRuleProtocol(str, Enum):

    tcp = "Tcp"
    udp = "Udp"
    all = "All"


class NatGatewaySkuName(str, Enum):

    standard = "Standard"


class NetworkOperationStatus(str, Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"


class Access(str, Enum):

    allow = "Allow"
    deny = "Deny"


class AuthenticationMethod(str, Enum):

    eaptls = "EAPTLS"
    eapmscha_pv2 = "EAPMSCHAPv2"


class EffectiveSecurityRuleProtocol(str, Enum):

    tcp = "Tcp"
    udp = "Udp"
    all = "All"


class EffectiveRouteSource(str, Enum):

    unknown = "Unknown"
    user = "User"
    virtual_network_gateway = "VirtualNetworkGateway"
    default = "Default"


class EffectiveRouteState(str, Enum):

    active = "Active"
    invalid = "Invalid"


class InboundSecurityRulesProtocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"


class AssociationType(str, Enum):

    associated = "Associated"
    contains = "Contains"


class Direction(str, Enum):

    inbound = "Inbound"
    outbound = "Outbound"


class IpFlowProtocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"


class NextHopType(str, Enum):

    internet = "Internet"
    virtual_appliance = "VirtualAppliance"
    virtual_network_gateway = "VirtualNetworkGateway"
    vnet_local = "VnetLocal"
    hyper_net_gateway = "HyperNetGateway"
    none = "None"


class PcProtocol(str, Enum):

    tcp = "TCP"
    udp = "UDP"
    any = "Any"


class PcStatus(str, Enum):

    not_started = "NotStarted"
    running = "Running"
    stopped = "Stopped"
    error = "Error"
    unknown = "Unknown"


class PcError(str, Enum):

    internal_error = "InternalError"
    agent_stopped = "AgentStopped"
    capture_failed = "CaptureFailed"
    local_file_failed = "LocalFileFailed"
    storage_failed = "StorageFailed"


class Protocol(str, Enum):

    tcp = "Tcp"
    http = "Http"
    https = "Https"
    icmp = "Icmp"


class HTTPMethod(str, Enum):

    get = "Get"


class Origin(str, Enum):

    local = "Local"
    inbound = "Inbound"
    outbound = "Outbound"


class Severity(str, Enum):

    error = "Error"
    warning = "Warning"


class IssueType(str, Enum):

    unknown = "Unknown"
    agent_stopped = "AgentStopped"
    guest_firewall = "GuestFirewall"
    dns_resolution = "DnsResolution"
    socket_bind = "SocketBind"
    network_security_rule = "NetworkSecurityRule"
    user_defined_route = "UserDefinedRoute"
    port_throttled = "PortThrottled"
    platform = "Platform"


class ConnectionStatus(str, Enum):

    unknown = "Unknown"
    connected = "Connected"
    disconnected = "Disconnected"
    degraded = "Degraded"


class VerbosityLevel(str, Enum):

    normal = "Normal"
    minimum = "Minimum"
    full = "Full"


class EndpointType(str, Enum):

    azure_vm = "AzureVM"
    azure_vnet = "AzureVNet"
    azure_subnet = "AzureSubnet"
    external_address = "ExternalAddress"
    mma_workspace_machine = "MMAWorkspaceMachine"
    mma_workspace_network = "MMAWorkspaceNetwork"


class ConnectionMonitorEndpointFilterType(str, Enum):

    include = "Include"


class ConnectionMonitorEndpointFilterItemType(str, Enum):

    agent_address = "AgentAddress"


class CoverageLevel(str, Enum):

    default = "Default"
    low = "Low"
    below_average = "BelowAverage"
    average = "Average"
    above_average = "AboveAverage"
    full = "Full"


class ConnectionMonitorTestConfigurationProtocol(str, Enum):

    tcp = "Tcp"
    http = "Http"
    icmp = "Icmp"


class PreferredIPVersion(str, Enum):

    ipv4 = "IPv4"
    ipv6 = "IPv6"


class HTTPConfigurationMethod(str, Enum):

    get = "Get"
    post = "Post"


class DestinationPortBehavior(str, Enum):

    none = "None"
    listen_if_available = "ListenIfAvailable"


class OutputType(str, Enum):

    workspace = "Workspace"


class ConnectionState(str, Enum):

    reachable = "Reachable"
    unreachable = "Unreachable"
    unknown = "Unknown"


class EvaluationState(str, Enum):

    not_started = "NotStarted"
    in_progress = "InProgress"
    completed = "Completed"


class ConnectionMonitorType(str, Enum):

    multi_endpoint = "MultiEndpoint"
    single_source_destination = "SingleSourceDestination"


class ConnectionMonitorSourceStatus(str, Enum):

    unknown = "Unknown"
    active = "Active"
    inactive = "Inactive"


class PublicIPPrefixSkuName(str, Enum):

    standard = "Standard"


class PublicIPPrefixSkuTier(str, Enum):

    regional = "Regional"
    global_enum = "Global"


class SecurityProviderName(str, Enum):

    zscaler = "ZScaler"
    iboss = "IBoss"
    checkpoint = "Checkpoint"


class SecurityPartnerProviderConnectionStatus(str, Enum):

    unknown = "Unknown"
    partially_connected = "PartiallyConnected"
    connected = "Connected"
    not_connected = "NotConnected"


class VirtualNetworkPeeringState(str, Enum):

    initiated = "Initiated"
    connected = "Connected"
    disconnected = "Disconnected"


class VirtualNetworkGatewayType(str, Enum):

    vpn = "Vpn"
    express_route = "ExpressRoute"
    local_gateway = "LocalGateway"


class VpnType(str, Enum):

    policy_based = "PolicyBased"
    route_based = "RouteBased"


class VpnGatewayGeneration(str, Enum):

    none = "None"
    generation1 = "Generation1"
    generation2 = "Generation2"


class VirtualNetworkGatewaySkuName(str, Enum):

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"
    ultra_performance = "UltraPerformance"
    vpn_gw1 = "VpnGw1"
    vpn_gw2 = "VpnGw2"
    vpn_gw3 = "VpnGw3"
    vpn_gw4 = "VpnGw4"
    vpn_gw5 = "VpnGw5"
    vpn_gw1_az = "VpnGw1AZ"
    vpn_gw2_az = "VpnGw2AZ"
    vpn_gw3_az = "VpnGw3AZ"
    vpn_gw4_az = "VpnGw4AZ"
    vpn_gw5_az = "VpnGw5AZ"
    er_gw1_az = "ErGw1AZ"
    er_gw2_az = "ErGw2AZ"
    er_gw3_az = "ErGw3AZ"


class VirtualNetworkGatewaySkuTier(str, Enum):

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"
    ultra_performance = "UltraPerformance"
    vpn_gw1 = "VpnGw1"
    vpn_gw2 = "VpnGw2"
    vpn_gw3 = "VpnGw3"
    vpn_gw4 = "VpnGw4"
    vpn_gw5 = "VpnGw5"
    vpn_gw1_az = "VpnGw1AZ"
    vpn_gw2_az = "VpnGw2AZ"
    vpn_gw3_az = "VpnGw3AZ"
    vpn_gw4_az = "VpnGw4AZ"
    vpn_gw5_az = "VpnGw5AZ"
    er_gw1_az = "ErGw1AZ"
    er_gw2_az = "ErGw2AZ"
    er_gw3_az = "ErGw3AZ"


class VpnClientProtocol(str, Enum):

    ike_v2 = "IkeV2"
    sstp = "SSTP"
    open_vpn = "OpenVPN"


class IpsecEncryption(str, Enum):

    none = "None"
    des = "DES"
    des3 = "DES3"
    aes128 = "AES128"
    aes192 = "AES192"
    aes256 = "AES256"
    gcmaes128 = "GCMAES128"
    gcmaes192 = "GCMAES192"
    gcmaes256 = "GCMAES256"


class IpsecIntegrity(str, Enum):

    md5 = "MD5"
    sha1 = "SHA1"
    sha256 = "SHA256"
    gcmaes128 = "GCMAES128"
    gcmaes192 = "GCMAES192"
    gcmaes256 = "GCMAES256"


class IkeEncryption(str, Enum):

    des = "DES"
    des3 = "DES3"
    aes128 = "AES128"
    aes192 = "AES192"
    aes256 = "AES256"
    gcmaes256 = "GCMAES256"
    gcmaes128 = "GCMAES128"


class IkeIntegrity(str, Enum):

    md5 = "MD5"
    sha1 = "SHA1"
    sha256 = "SHA256"
    sha384 = "SHA384"
    gcmaes256 = "GCMAES256"
    gcmaes128 = "GCMAES128"


class DhGroup(str, Enum):

    none = "None"
    dh_group1 = "DHGroup1"
    dh_group2 = "DHGroup2"
    dh_group14 = "DHGroup14"
    dh_group2048 = "DHGroup2048"
    ecp256 = "ECP256"
    ecp384 = "ECP384"
    dh_group24 = "DHGroup24"


class PfsGroup(str, Enum):

    none = "None"
    pfs1 = "PFS1"
    pfs2 = "PFS2"
    pfs2048 = "PFS2048"
    ecp256 = "ECP256"
    ecp384 = "ECP384"
    pfs24 = "PFS24"
    pfs14 = "PFS14"
    pfsmm = "PFSMM"


class BgpPeerState(str, Enum):

    unknown = "Unknown"
    stopped = "Stopped"
    idle = "Idle"
    connecting = "Connecting"
    connected = "Connected"


class ProcessorArchitecture(str, Enum):

    amd64 = "Amd64"
    x86 = "X86"


class VirtualNetworkGatewayConnectionStatus(str, Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"


class VirtualNetworkGatewayConnectionType(str, Enum):

    ipsec = "IPsec"
    vnet2_vnet = "Vnet2Vnet"
    express_route = "ExpressRoute"
    vpn_client = "VPNClient"


class VirtualNetworkGatewayConnectionProtocol(str, Enum):

    ik_ev2 = "IKEv2"
    ik_ev1 = "IKEv1"


class VirtualNetworkGatewayConnectionMode(str, Enum):

    default = "Default"
    responder_only = "ResponderOnly"
    initiator_only = "InitiatorOnly"


class OfficeTrafficCategory(str, Enum):

    optimize = "Optimize"
    optimize_and_allow = "OptimizeAndAllow"
    all = "All"
    none = "None"


class RoutingState(str, Enum):

    none = "None"
    provisioned = "Provisioned"
    provisioning = "Provisioning"
    failed = "Failed"


class HubBgpConnectionStatus(str, Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"


class VpnConnectionStatus(str, Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"


class VirtualWanSecurityProviderType(str, Enum):

    external = "External"
    native = "Native"


class TunnelConnectionStatus(str, Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"


class HubVirtualNetworkConnectionStatus(str, Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"


class VpnGatewayTunnelingProtocol(str, Enum):

    ike_v2 = "IkeV2"
    open_vpn = "OpenVPN"


class VpnAuthenticationType(str, Enum):

    certificate = "Certificate"
    radius = "Radius"
    aad = "AAD"


class WebApplicationFirewallEnabledState(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class WebApplicationFirewallMode(str, Enum):

    prevention = "Prevention"
    detection = "Detection"


class WebApplicationFirewallRuleType(str, Enum):

    match_rule = "MatchRule"
    invalid = "Invalid"


class WebApplicationFirewallMatchVariable(str, Enum):

    remote_addr = "RemoteAddr"
    request_method = "RequestMethod"
    query_string = "QueryString"
    post_args = "PostArgs"
    request_uri = "RequestUri"
    request_headers = "RequestHeaders"
    request_body = "RequestBody"
    request_cookies = "RequestCookies"


class WebApplicationFirewallOperator(str, Enum):

    ip_match = "IPMatch"
    equal = "Equal"
    contains = "Contains"
    less_than = "LessThan"
    greater_than = "GreaterThan"
    less_than_or_equal = "LessThanOrEqual"
    greater_than_or_equal = "GreaterThanOrEqual"
    begins_with = "BeginsWith"
    ends_with = "EndsWith"
    regex = "Regex"
    geo_match = "GeoMatch"


class WebApplicationFirewallTransform(str, Enum):

    lowercase = "Lowercase"
    trim = "Trim"
    url_decode = "UrlDecode"
    url_encode = "UrlEncode"
    remove_nulls = "RemoveNulls"
    html_entity_decode = "HtmlEntityDecode"


class WebApplicationFirewallAction(str, Enum):

    allow = "Allow"
    block = "Block"
    log = "Log"


class WebApplicationFirewallPolicyResourceState(str, Enum):

    creating = "Creating"
    enabling = "Enabling"
    enabled = "Enabled"
    disabling = "Disabling"
    disabled = "Disabled"
    deleting = "Deleting"


class OwaspCrsExclusionEntryMatchVariable(str, Enum):

    request_header_names = "RequestHeaderNames"
    request_cookie_names = "RequestCookieNames"
    request_arg_names = "RequestArgNames"


class OwaspCrsExclusionEntrySelectorMatchOperator(str, Enum):

    equals = "Equals"
    contains = "Contains"
    starts_with = "StartsWith"
    ends_with = "EndsWith"
    equals_any = "EqualsAny"


class ManagedRuleEnabledState(str, Enum):

    disabled = "Disabled"
