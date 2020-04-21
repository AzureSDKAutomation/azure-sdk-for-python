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


class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.relay.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class RelayNamespacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RelayNamespace <azure.mgmt.relay.models.RelayNamespace>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RelayNamespace]'}
    }

    def __init__(self, *args, **kwargs):

        super(RelayNamespacePaged, self).__init__(*args, **kwargs)
class AuthorizationRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AuthorizationRule <azure.mgmt.relay.models.AuthorizationRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AuthorizationRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(AuthorizationRulePaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.relay.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class PrivateLinkResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkResource <azure.mgmt.relay.models.PrivateLinkResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkResourcePaged, self).__init__(*args, **kwargs)
class HybridConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`HybridConnection <azure.mgmt.relay.models.HybridConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[HybridConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(HybridConnectionPaged, self).__init__(*args, **kwargs)
class WcfRelayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WcfRelay <azure.mgmt.relay.models.WcfRelay>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WcfRelay]'}
    }

    def __init__(self, *args, **kwargs):

        super(WcfRelayPaged, self).__init__(*args, **kwargs)
