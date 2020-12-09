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


class VaultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Vault <azure.mgmt.keyvault.v2019_09_01.models.Vault>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Vault]'}
    }

    def __init__(self, *args, **kwargs):

        super(VaultPaged, self).__init__(*args, **kwargs)
class DeletedVaultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DeletedVault <azure.mgmt.keyvault.v2019_09_01.models.DeletedVault>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DeletedVault]'}
    }

    def __init__(self, *args, **kwargs):

        super(DeletedVaultPaged, self).__init__(*args, **kwargs)
class ResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Resource <azure.mgmt.keyvault.v2019_09_01.models.Resource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Resource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourcePaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.keyvault.v2019_09_01.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class KeyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Key <azure.mgmt.keyvault.v2019_09_01.models.Key>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Key]'}
    }

    def __init__(self, *args, **kwargs):

        super(KeyPaged, self).__init__(*args, **kwargs)
