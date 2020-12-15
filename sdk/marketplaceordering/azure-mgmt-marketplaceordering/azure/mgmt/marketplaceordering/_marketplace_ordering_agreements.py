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

from ._configuration import MarketplaceOrderingAgreementsConfiguration
from .operations import MarketplaceAgreementsOperations
from .operations import Operations
from . import models


class MarketplaceOrderingAgreements(SDKClient):
    """REST API for MarketplaceOrdering Agreements.

    :ivar config: Configuration for client.
    :vartype config: MarketplaceOrderingAgreementsConfiguration

    :ivar marketplace_agreements: MarketplaceAgreements operations
    :vartype marketplace_agreements: azure.mgmt.marketplaceordering.operations.MarketplaceAgreementsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.marketplaceordering.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription ID that identifies an Azure
     subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = MarketplaceOrderingAgreementsConfiguration(credentials, subscription_id, base_url)
        super(MarketplaceOrderingAgreements, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.marketplace_agreements = MarketplaceAgreementsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
