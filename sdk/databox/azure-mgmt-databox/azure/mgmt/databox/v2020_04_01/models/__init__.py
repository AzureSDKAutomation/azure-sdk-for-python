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
    from ._models_py3 import AccountCredentialDetails
    from ._models_py3 import AdditionalErrorInfo
    from ._models_py3 import AddressValidationOutput
    from ._models_py3 import ApiError, ApiErrorException
    from ._models_py3 import ApplianceNetworkConfiguration
    from ._models_py3 import ArmBaseObject
    from ._models_py3 import AvailableSkuRequest
    from ._models_py3 import AzureFileFilterDetails
    from ._models_py3 import BlobFilterDetails
    from ._models_py3 import CancellationReason
    from ._models_py3 import ContactDetails
    from ._models_py3 import CopyLogDetails
    from ._models_py3 import CopyProgress
    from ._models_py3 import CreateJobValidations
    from ._models_py3 import CreateOrderLimitForSubscriptionValidationRequest
    from ._models_py3 import CreateOrderLimitForSubscriptionValidationResponseProperties
    from ._models_py3 import DataAccountDetails
    from ._models_py3 import DataBoxAccountCopyLogDetails
    from ._models_py3 import DataBoxDiskCopyLogDetails
    from ._models_py3 import DataBoxDiskCopyProgress
    from ._models_py3 import DataBoxDiskJobDetails
    from ._models_py3 import DataBoxDiskJobSecrets
    from ._models_py3 import DataBoxHeavyAccountCopyLogDetails
    from ._models_py3 import DataBoxHeavyJobDetails
    from ._models_py3 import DataBoxHeavyJobSecrets
    from ._models_py3 import DataBoxHeavySecret
    from ._models_py3 import DataBoxJobDetails
    from ._models_py3 import DataboxJobSecrets
    from ._models_py3 import DataBoxScheduleAvailabilityRequest
    from ._models_py3 import DataBoxSecret
    from ._models_py3 import DataExportDetails
    from ._models_py3 import DataImportDetails
    from ._models_py3 import DataLocationToServiceLocationMap
    from ._models_py3 import DataTransferDetailsValidationRequest
    from ._models_py3 import DataTransferDetailsValidationResponseProperties
    from ._models_py3 import DcAccessSecurityCode
    from ._models_py3 import Details
    from ._models_py3 import DiskScheduleAvailabilityRequest
    from ._models_py3 import DiskSecret
    from ._models_py3 import ErrorDetail
    from ._models_py3 import FilterFileDetails
    from ._models_py3 import HeavyScheduleAvailabilityRequest
    from ._models_py3 import JobDeliveryInfo
    from ._models_py3 import JobDetails
    from ._models_py3 import JobResource
    from ._models_py3 import JobResourceUpdateParameter
    from ._models_py3 import JobSecrets
    from ._models_py3 import JobStages
    from ._models_py3 import KeyEncryptionKey
    from ._models_py3 import ManagedDiskDetails
    from ._models_py3 import NotificationPreference
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import PackageShippingDetails
    from ._models_py3 import Preferences
    from ._models_py3 import PreferencesValidationRequest
    from ._models_py3 import PreferencesValidationResponseProperties
    from ._models_py3 import RegionConfigurationRequest
    from ._models_py3 import RegionConfigurationResponse
    from ._models_py3 import Resource
    from ._models_py3 import ResourceIdentity
    from ._models_py3 import ScheduleAvailabilityRequest
    from ._models_py3 import ScheduleAvailabilityResponse
    from ._models_py3 import ShareCredentialDetails
    from ._models_py3 import ShipmentPickUpRequest
    from ._models_py3 import ShipmentPickUpResponse
    from ._models_py3 import ShippingAddress
    from ._models_py3 import Sku
    from ._models_py3 import SkuAvailabilityValidationRequest
    from ._models_py3 import SkuAvailabilityValidationResponseProperties
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SkuCost
    from ._models_py3 import SkuInformation
    from ._models_py3 import StorageAccountDetails
    from ._models_py3 import SubscriptionIsAllowedToCreateJobValidationRequest
    from ._models_py3 import SubscriptionIsAllowedToCreateJobValidationResponseProperties
    from ._models_py3 import TransferAllDetails
    from ._models_py3 import TransferConfiguration
    from ._models_py3 import TransferConfigurationTransferAllDetails
    from ._models_py3 import TransferConfigurationTransferFilterDetails
    from ._models_py3 import TransferFilterDetails
    from ._models_py3 import TransportAvailabilityDetails
    from ._models_py3 import TransportAvailabilityRequest
    from ._models_py3 import TransportAvailabilityResponse
    from ._models_py3 import TransportPreferences
    from ._models_py3 import UnencryptedCredentials
    from ._models_py3 import UpdateJobDetails
    from ._models_py3 import ValidateAddress
    from ._models_py3 import ValidationInputRequest
    from ._models_py3 import ValidationInputResponse
    from ._models_py3 import ValidationRequest
    from ._models_py3 import ValidationResponse
except (SyntaxError, ImportError):
    from ._models import AccountCredentialDetails
    from ._models import AdditionalErrorInfo
    from ._models import AddressValidationOutput
    from ._models import ApiError, ApiErrorException
    from ._models import ApplianceNetworkConfiguration
    from ._models import ArmBaseObject
    from ._models import AvailableSkuRequest
    from ._models import AzureFileFilterDetails
    from ._models import BlobFilterDetails
    from ._models import CancellationReason
    from ._models import ContactDetails
    from ._models import CopyLogDetails
    from ._models import CopyProgress
    from ._models import CreateJobValidations
    from ._models import CreateOrderLimitForSubscriptionValidationRequest
    from ._models import CreateOrderLimitForSubscriptionValidationResponseProperties
    from ._models import DataAccountDetails
    from ._models import DataBoxAccountCopyLogDetails
    from ._models import DataBoxDiskCopyLogDetails
    from ._models import DataBoxDiskCopyProgress
    from ._models import DataBoxDiskJobDetails
    from ._models import DataBoxDiskJobSecrets
    from ._models import DataBoxHeavyAccountCopyLogDetails
    from ._models import DataBoxHeavyJobDetails
    from ._models import DataBoxHeavyJobSecrets
    from ._models import DataBoxHeavySecret
    from ._models import DataBoxJobDetails
    from ._models import DataboxJobSecrets
    from ._models import DataBoxScheduleAvailabilityRequest
    from ._models import DataBoxSecret
    from ._models import DataExportDetails
    from ._models import DataImportDetails
    from ._models import DataLocationToServiceLocationMap
    from ._models import DataTransferDetailsValidationRequest
    from ._models import DataTransferDetailsValidationResponseProperties
    from ._models import DcAccessSecurityCode
    from ._models import Details
    from ._models import DiskScheduleAvailabilityRequest
    from ._models import DiskSecret
    from ._models import ErrorDetail
    from ._models import FilterFileDetails
    from ._models import HeavyScheduleAvailabilityRequest
    from ._models import JobDeliveryInfo
    from ._models import JobDetails
    from ._models import JobResource
    from ._models import JobResourceUpdateParameter
    from ._models import JobSecrets
    from ._models import JobStages
    from ._models import KeyEncryptionKey
    from ._models import ManagedDiskDetails
    from ._models import NotificationPreference
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import PackageShippingDetails
    from ._models import Preferences
    from ._models import PreferencesValidationRequest
    from ._models import PreferencesValidationResponseProperties
    from ._models import RegionConfigurationRequest
    from ._models import RegionConfigurationResponse
    from ._models import Resource
    from ._models import ResourceIdentity
    from ._models import ScheduleAvailabilityRequest
    from ._models import ScheduleAvailabilityResponse
    from ._models import ShareCredentialDetails
    from ._models import ShipmentPickUpRequest
    from ._models import ShipmentPickUpResponse
    from ._models import ShippingAddress
    from ._models import Sku
    from ._models import SkuAvailabilityValidationRequest
    from ._models import SkuAvailabilityValidationResponseProperties
    from ._models import SkuCapacity
    from ._models import SkuCost
    from ._models import SkuInformation
    from ._models import StorageAccountDetails
    from ._models import SubscriptionIsAllowedToCreateJobValidationRequest
    from ._models import SubscriptionIsAllowedToCreateJobValidationResponseProperties
    from ._models import TransferAllDetails
    from ._models import TransferConfiguration
    from ._models import TransferConfigurationTransferAllDetails
    from ._models import TransferConfigurationTransferFilterDetails
    from ._models import TransferFilterDetails
    from ._models import TransportAvailabilityDetails
    from ._models import TransportAvailabilityRequest
    from ._models import TransportAvailabilityResponse
    from ._models import TransportPreferences
    from ._models import UnencryptedCredentials
    from ._models import UpdateJobDetails
    from ._models import ValidateAddress
    from ._models import ValidationInputRequest
    from ._models import ValidationInputResponse
    from ._models import ValidationRequest
    from ._models import ValidationResponse
from ._paged_models import JobResourcePaged
from ._paged_models import OperationPaged
from ._paged_models import SkuInformationPaged
from ._paged_models import UnencryptedCredentialsPaged
from ._data_box_management_client_enums import (
    DataAccountType,
    ShareDestinationFormatType,
    AccessProtocol,
    AddressValidationStatus,
    AddressType,
    TransferType,
    SkuName,
    SkuDisabledReason,
    NotificationStageName,
    ValidationStatus,
    CopyStatus,
    TransferConfigurationType,
    FilterFileType,
    LogCollectionLevel,
    StageName,
    StageStatus,
    TransportShipmentTypes,
    KekType,
    JobDeliveryType,
    OverallValidationStatus,
)

__all__ = [
    'AccountCredentialDetails',
    'AdditionalErrorInfo',
    'AddressValidationOutput',
    'ApiError', 'ApiErrorException',
    'ApplianceNetworkConfiguration',
    'ArmBaseObject',
    'AvailableSkuRequest',
    'AzureFileFilterDetails',
    'BlobFilterDetails',
    'CancellationReason',
    'ContactDetails',
    'CopyLogDetails',
    'CopyProgress',
    'CreateJobValidations',
    'CreateOrderLimitForSubscriptionValidationRequest',
    'CreateOrderLimitForSubscriptionValidationResponseProperties',
    'DataAccountDetails',
    'DataBoxAccountCopyLogDetails',
    'DataBoxDiskCopyLogDetails',
    'DataBoxDiskCopyProgress',
    'DataBoxDiskJobDetails',
    'DataBoxDiskJobSecrets',
    'DataBoxHeavyAccountCopyLogDetails',
    'DataBoxHeavyJobDetails',
    'DataBoxHeavyJobSecrets',
    'DataBoxHeavySecret',
    'DataBoxJobDetails',
    'DataboxJobSecrets',
    'DataBoxScheduleAvailabilityRequest',
    'DataBoxSecret',
    'DataExportDetails',
    'DataImportDetails',
    'DataLocationToServiceLocationMap',
    'DataTransferDetailsValidationRequest',
    'DataTransferDetailsValidationResponseProperties',
    'DcAccessSecurityCode',
    'Details',
    'DiskScheduleAvailabilityRequest',
    'DiskSecret',
    'ErrorDetail',
    'FilterFileDetails',
    'HeavyScheduleAvailabilityRequest',
    'JobDeliveryInfo',
    'JobDetails',
    'JobResource',
    'JobResourceUpdateParameter',
    'JobSecrets',
    'JobStages',
    'KeyEncryptionKey',
    'ManagedDiskDetails',
    'NotificationPreference',
    'Operation',
    'OperationDisplay',
    'PackageShippingDetails',
    'Preferences',
    'PreferencesValidationRequest',
    'PreferencesValidationResponseProperties',
    'RegionConfigurationRequest',
    'RegionConfigurationResponse',
    'Resource',
    'ResourceIdentity',
    'ScheduleAvailabilityRequest',
    'ScheduleAvailabilityResponse',
    'ShareCredentialDetails',
    'ShipmentPickUpRequest',
    'ShipmentPickUpResponse',
    'ShippingAddress',
    'Sku',
    'SkuAvailabilityValidationRequest',
    'SkuAvailabilityValidationResponseProperties',
    'SkuCapacity',
    'SkuCost',
    'SkuInformation',
    'StorageAccountDetails',
    'SubscriptionIsAllowedToCreateJobValidationRequest',
    'SubscriptionIsAllowedToCreateJobValidationResponseProperties',
    'TransferAllDetails',
    'TransferConfiguration',
    'TransferConfigurationTransferAllDetails',
    'TransferConfigurationTransferFilterDetails',
    'TransferFilterDetails',
    'TransportAvailabilityDetails',
    'TransportAvailabilityRequest',
    'TransportAvailabilityResponse',
    'TransportPreferences',
    'UnencryptedCredentials',
    'UpdateJobDetails',
    'ValidateAddress',
    'ValidationInputRequest',
    'ValidationInputResponse',
    'ValidationRequest',
    'ValidationResponse',
    'OperationPaged',
    'JobResourcePaged',
    'UnencryptedCredentialsPaged',
    'SkuInformationPaged',
    'DataAccountType',
    'ShareDestinationFormatType',
    'AccessProtocol',
    'AddressValidationStatus',
    'AddressType',
    'TransferType',
    'SkuName',
    'SkuDisabledReason',
    'NotificationStageName',
    'ValidationStatus',
    'CopyStatus',
    'TransferConfigurationType',
    'FilterFileType',
    'LogCollectionLevel',
    'StageName',
    'StageStatus',
    'TransportShipmentTypes',
    'KekType',
    'JobDeliveryType',
    'OverallValidationStatus',
]
