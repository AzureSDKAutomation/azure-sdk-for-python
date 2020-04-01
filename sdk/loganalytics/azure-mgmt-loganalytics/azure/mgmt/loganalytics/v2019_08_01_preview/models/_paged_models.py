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


class ClusterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Cluster <azure.mgmt.loganalytics.v2019_08_01_preview.models.Cluster>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Cluster]'}
    }

    def __init__(self, *args, **kwargs):

        super(ClusterPaged, self).__init__(*args, **kwargs)
class LinkedServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`LinkedService <azure.mgmt.loganalytics.v2019_08_01_preview.models.LinkedService>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LinkedService]'}
    }

    def __init__(self, *args, **kwargs):

        super(LinkedServicePaged, self).__init__(*args, **kwargs)
class DataExportPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DataExport <azure.mgmt.loganalytics.v2019_08_01_preview.models.DataExport>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DataExport]'}
    }

    def __init__(self, *args, **kwargs):

        super(DataExportPaged, self).__init__(*args, **kwargs)
class LinkedStorageAccountsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LinkedStorageAccounts <azure.mgmt.loganalytics.v2019_08_01_preview.models.LinkedStorageAccounts>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LinkedStorageAccounts]'}
    }

    def __init__(self, *args, **kwargs):

        super(LinkedStorageAccountsPaged, self).__init__(*args, **kwargs)
