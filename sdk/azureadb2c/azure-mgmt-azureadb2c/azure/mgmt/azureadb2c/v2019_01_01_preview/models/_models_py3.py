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
from msrest.exceptions import HttpOperationError


class AsyncOperationStatus(Model):
    """The async operation status.

    :param subscription_id: Subscription ID that the resource belongs to.
    :type subscription_id: str
    :param id: The GET resource path for the operation.
    :type id: str
    :param name: The operation ID.
    :type name: str
    :param status: The status of the operation. Possible values include:
     'Succeeded', 'Pending', 'Failed'
    :type status: str or
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.StatusType
    :param start_time: Start time of the async operation.
    :type start_time: str
    :param end_time: End time of the async operation.
    :type end_time: str
    :param billing_config: The billing configuration for the tenant.
    :type billing_config:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CTenantResourcePropertiesBillingConfig
    :param tenant_id: An identifier of the B2C tenant.
    :type tenant_id: str
    :param error: Error response if async operation failed.
    :type error:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.AsyncOperationStatusError
    """

    _attribute_map = {
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'StatusType'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'end_time': {'key': 'endTime', 'type': 'str'},
        'billing_config': {'key': 'properties.billingConfig', 'type': 'B2CTenantResourcePropertiesBillingConfig'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'error': {'key': 'error', 'type': 'AsyncOperationStatusError'},
    }

    def __init__(self, *, subscription_id: str=None, id: str=None, name: str=None, status=None, start_time: str=None, end_time: str=None, billing_config=None, tenant_id: str=None, error=None, **kwargs) -> None:
        super(AsyncOperationStatus, self).__init__(**kwargs)
        self.subscription_id = subscription_id
        self.id = id
        self.name = name
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.billing_config = billing_config
        self.tenant_id = tenant_id
        self.error = error


class AsyncOperationStatusError(Model):
    """Error response if async operation failed.

    :param code: Error code.
    :type code: str
    :param message: Error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(AsyncOperationStatusError, self).__init__(**kwargs)
        self.code = code
        self.message = message


class B2CResourceSKU(Model):
    """SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C
    billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).

    :param name: The name of the SKU for the tenant. Possible values include:
     'Standard', 'PremiumP1', 'PremiumP2'
    :type name: str or
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CResourceSKUName
    :param tier: The tier of the tenant. Possible values include: 'A0'
    :type tier: str or
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CResourceSKUTier
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'B2CResourceSKUName'},
        'tier': {'key': 'tier', 'type': 'B2CResourceSKUTier'},
    }

    def __init__(self, *, name=None, tier=None, **kwargs) -> None:
        super(B2CResourceSKU, self).__init__(**kwargs)
        self.name = name
        self.tier = tier


class B2CTenantResource(Model):
    """B2CTenantResource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of the B2C tenant resource. Possible values include:
     'Microsoft.AzureActiveDirectory/b2cDirectories'
    :vartype type: str or
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.TypeValue
    :param sku: Required.
    :type sku:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CResourceSKU
    :param billing_config: The billing configuration for the tenant.
    :type billing_config:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CTenantResourcePropertiesBillingConfig
    :param tenant_id: An identifier of the B2C tenant.
    :type tenant_id: str
    :ivar id: An identifier that represents the B2C tenant resource.
    :vartype id: str
    :ivar name: The name of the B2C tenant resource.
    :vartype name: str
    :param location: Required. The location in which the resource is hosted
     and data resides. Refer to [this
     documentation](https://aka.ms/B2CDataResidency) to see valid data
     residency locations. Please choose one of 'United States', 'Europe', and
     'Asia Pacific'.
    :type location: str
    :param tags: Resource Tags
    :type tags: dict[str, str]
    """

    _validation = {
        'type': {'readonly': True},
        'sku': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'TypeValue'},
        'sku': {'key': 'sku', 'type': 'B2CResourceSKU'},
        'billing_config': {'key': 'properties.billingConfig', 'type': 'B2CTenantResourcePropertiesBillingConfig'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, sku, location: str, billing_config=None, tenant_id: str=None, tags=None, **kwargs) -> None:
        super(B2CTenantResource, self).__init__(**kwargs)
        self.type = None
        self.sku = sku
        self.billing_config = billing_config
        self.tenant_id = tenant_id
        self.id = None
        self.name = None
        self.location = location
        self.tags = tags


class B2CTenantResourcePropertiesBillingConfig(Model):
    """The billing configuration for the tenant.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param billing_type: The type of billing. Will be MAU for all new
     customers. If 'Auths', it can be updated to 'MAU'. Cannot be changed if
     value is 'MAU'. Learn more about Azure AD B2C billing at
     [aka.ms/b2cBilling](https://aka.ms/b2cbilling). Possible values include:
     'MAU', 'Auths'
    :type billing_type: str or
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.BillingType
    :ivar effective_start_date_utc: The data from which the billing type took
     effect
    :vartype effective_start_date_utc: str
    """

    _validation = {
        'effective_start_date_utc': {'readonly': True},
    }

    _attribute_map = {
        'billing_type': {'key': 'billingType', 'type': 'BillingType'},
        'effective_start_date_utc': {'key': 'effectiveStartDateUtc', 'type': 'str'},
    }

    def __init__(self, *, billing_type=None, **kwargs) -> None:
        super(B2CTenantResourcePropertiesBillingConfig, self).__init__(**kwargs)
        self.billing_type = billing_type
        self.effective_start_date_utc = None


class B2CTenantUpdateRequest(Model):
    """The request body to update the Azure AD B2C tenant resource.

    :param sku:
    :type sku:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CResourceSKU
    :param billing_config: The billing configuration for the tenant.
    :type billing_config:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CTenantResourcePropertiesBillingConfig
    :param tenant_id: An identifier of the B2C tenant.
    :type tenant_id: str
    :param tags: Resource Tags
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'B2CResourceSKU'},
        'billing_config': {'key': 'properties.billingConfig', 'type': 'B2CTenantResourcePropertiesBillingConfig'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, sku=None, billing_config=None, tenant_id: str=None, tags=None, **kwargs) -> None:
        super(B2CTenantUpdateRequest, self).__init__(**kwargs)
        self.sku = sku
        self.billing_config = billing_config
        self.tenant_id = tenant_id
        self.tags = tags


class CheckNameAvailabilityRequestBody(Model):
    """The information required to check the availability of the name for the
    tenant.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The domain name to check for availability.
    :type name: str
    :param country_code: Required.
    :type country_code: str
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
    }

    def __init__(self, *, name: str, country_code: str, **kwargs) -> None:
        super(CheckNameAvailabilityRequestBody, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code


class CloudError(Model):
    """An error response for a resource management request.

    :param error:
    :type error:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.ErrorResponse
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CreateTenantRequestBody(Model):
    """The information needed to create the Azure AD B2C tenant and corresponding
    Azure resource, which is used for billing purposes.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The location in which the resource is hosted
     and data resides. Refer to [this
     documentation](https://aka.ms/B2CDataResidency) to see valid data
     residency locations. Please choose one of 'United States', 'Europe', and
     'Asia Pacific'.
    :type location: str
    :param properties: Required.
    :type properties:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.CreateTenantRequestBodyProperties
    :param sku: Required.
    :type sku:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.B2CResourceSKU
    :param tags: Resource Tags
    :type tags: dict[str, str]
    """

    _validation = {
        'location': {'required': True},
        'properties': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'CreateTenantRequestBodyProperties'},
        'sku': {'key': 'sku', 'type': 'B2CResourceSKU'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, properties, sku, tags=None, **kwargs) -> None:
        super(CreateTenantRequestBody, self).__init__(**kwargs)
        self.location = location
        self.properties = properties
        self.sku = sku
        self.tags = tags


class CreateTenantRequestBodyProperties(Model):
    """CreateTenantRequestBodyProperties.

    :param display_name: The display name of the B2C tenant.
    :type display_name: str
    :param country_code:
    :type country_code: str
    """

    _attribute_map = {
        'display_name': {'key': 'createTenantProperties.displayName', 'type': 'str'},
        'country_code': {'key': 'createTenantProperties.countryCode', 'type': 'str'},
    }

    def __init__(self, *, display_name: str=None, country_code: str=None, **kwargs) -> None:
        super(CreateTenantRequestBodyProperties, self).__init__(**kwargs)
        self.display_name = display_name
        self.country_code = country_code


class ErrorAdditionalInfo(Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(Model):
    """Error Response.

    Common error response for all Azure Resource Manager APIs to return error
    details for failed operations. (This also follows the OData error response
    format.).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details:
     list[~azure.mgmt.azureadb2c.v2019_01_01_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.azureadb2c.v2019_01_01_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class NameAvailabilityResponse(Model):
    """Response of the CheckNameAvailability operation.

    :param message: Description of the reason if name is not available.
    :type message: str
    :param name_available: True if the name is available and can be used to
     create a new tenant. Otherwise false.
    :type name_available: bool
    :param reason: Possible values include: 'AlreadyExists', 'Invalid'
    :type reason: str or
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.NameAvailabilityReasonType
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'NameAvailabilityReasonType'},
    }

    def __init__(self, *, message: str=None, name_available: bool=None, reason=None, **kwargs) -> None:
        super(NameAvailabilityResponse, self).__init__(**kwargs)
        self.message = message
        self.name_available = name_available
        self.reason = reason


class Operation(Model):
    """Microsoft.AzureActiveDirectory REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The object that represents the operation.
    :type display:
     ~azure.mgmt.azureadb2c.v2019_01_01_preview.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(self, *, display=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display


class OperationDisplay(Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft.AzureActiveDirectory.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed: GuestUsages,
     etc.
    :vartype resource: str
    :ivar operation: Operation type: Read, write, delete, etc.
    :vartype operation: str
    :param description: Friendly name of the operation
    :type description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, **kwargs) -> None:
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = description
