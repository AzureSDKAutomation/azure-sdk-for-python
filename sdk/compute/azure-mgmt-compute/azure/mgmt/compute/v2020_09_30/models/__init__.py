# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessUri
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import CreationData
    from ._models_py3 import DataDiskImageEncryption
    from ._models_py3 import Disallowed
    from ._models_py3 import Disk
    from ._models_py3 import DiskAccess
    from ._models_py3 import DiskAccessList
    from ._models_py3 import DiskAccessUpdate
    from ._models_py3 import DiskEncryptionSet
    from ._models_py3 import DiskEncryptionSetList
    from ._models_py3 import DiskEncryptionSetUpdate
    from ._models_py3 import DiskImageEncryption
    from ._models_py3 import DiskList
    from ._models_py3 import DiskRestorePoint
    from ._models_py3 import DiskRestorePointList
    from ._models_py3 import DiskSku
    from ._models_py3 import DiskUpdate
    from ._models_py3 import Encryption
    from ._models_py3 import EncryptionImages
    from ._models_py3 import EncryptionSetIdentity
    from ._models_py3 import EncryptionSettingsCollection
    from ._models_py3 import EncryptionSettingsElement
    from ._models_py3 import ExtendedLocation
    from ._models_py3 import Gallery
    from ._models_py3 import GalleryApplication
    from ._models_py3 import GalleryApplicationList
    from ._models_py3 import GalleryApplicationUpdate
    from ._models_py3 import GalleryApplicationVersion
    from ._models_py3 import GalleryApplicationVersionList
    from ._models_py3 import GalleryApplicationVersionPublishingProfile
    from ._models_py3 import GalleryApplicationVersionUpdate
    from ._models_py3 import GalleryArtifactPublishingProfileBase
    from ._models_py3 import GalleryArtifactSource
    from ._models_py3 import GalleryArtifactVersionSource
    from ._models_py3 import GalleryDataDiskImage
    from ._models_py3 import GalleryDiskImage
    from ._models_py3 import GalleryDiskImageSource
    from ._models_py3 import GalleryIdentifier
    from ._models_py3 import GalleryImage
    from ._models_py3 import GalleryImageFeature
    from ._models_py3 import GalleryImageIdentifier
    from ._models_py3 import GalleryImageList
    from ._models_py3 import GalleryImageUpdate
    from ._models_py3 import GalleryImageVersion
    from ._models_py3 import GalleryImageVersionList
    from ._models_py3 import GalleryImageVersionPublishingProfile
    from ._models_py3 import GalleryImageVersionStorageProfile
    from ._models_py3 import GalleryImageVersionUpdate
    from ._models_py3 import GalleryList
    from ._models_py3 import GalleryOSDiskImage
    from ._models_py3 import GalleryUpdate
    from ._models_py3 import GrantAccessData
    from ._models_py3 import ImageDiskReference
    from ._models_py3 import ImagePurchasePlan
    from ._models_py3 import InnerError
    from ._models_py3 import KeyForDiskEncryptionSet
    from ._models_py3 import KeyVaultAndKeyReference
    from ._models_py3 import KeyVaultAndSecretReference
    from ._models_py3 import ManagedArtifact
    from ._models_py3 import OSDiskImageEncryption
    from ._models_py3 import PirResource
    from ._models_py3 import PirSharedGalleryResource
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import ProxyOnlyResource
    from ._models_py3 import PurchasePlan
    from ._models_py3 import RecommendedMachineConfiguration
    from ._models_py3 import RegionalReplicationStatus
    from ._models_py3 import ReplicationStatus
    from ._models_py3 import Resource
    from ._models_py3 import ResourceRange
    from ._models_py3 import ResourceUriList
    from ._models_py3 import ShareInfoElement
    from ._models_py3 import SharedGallery
    from ._models_py3 import SharedGalleryImage
    from ._models_py3 import SharedGalleryImageList
    from ._models_py3 import SharedGalleryImageVersion
    from ._models_py3 import SharedGalleryImageVersionList
    from ._models_py3 import SharedGalleryList
    from ._models_py3 import SharingProfile
    from ._models_py3 import SharingProfileGroup
    from ._models_py3 import SharingUpdate
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotList
    from ._models_py3 import SnapshotSku
    from ._models_py3 import SnapshotUpdate
    from ._models_py3 import SourceVault
    from ._models_py3 import TargetRegion
    from ._models_py3 import UpdateResourceDefinition
    from ._models_py3 import UserArtifactManage
    from ._models_py3 import UserArtifactSource
except (SyntaxError, ImportError):
    from ._models import AccessUri  # type: ignore
    from ._models import ApiError  # type: ignore
    from ._models import ApiErrorBase  # type: ignore
    from ._models import CreationData  # type: ignore
    from ._models import DataDiskImageEncryption  # type: ignore
    from ._models import Disallowed  # type: ignore
    from ._models import Disk  # type: ignore
    from ._models import DiskAccess  # type: ignore
    from ._models import DiskAccessList  # type: ignore
    from ._models import DiskAccessUpdate  # type: ignore
    from ._models import DiskEncryptionSet  # type: ignore
    from ._models import DiskEncryptionSetList  # type: ignore
    from ._models import DiskEncryptionSetUpdate  # type: ignore
    from ._models import DiskImageEncryption  # type: ignore
    from ._models import DiskList  # type: ignore
    from ._models import DiskRestorePoint  # type: ignore
    from ._models import DiskRestorePointList  # type: ignore
    from ._models import DiskSku  # type: ignore
    from ._models import DiskUpdate  # type: ignore
    from ._models import Encryption  # type: ignore
    from ._models import EncryptionImages  # type: ignore
    from ._models import EncryptionSetIdentity  # type: ignore
    from ._models import EncryptionSettingsCollection  # type: ignore
    from ._models import EncryptionSettingsElement  # type: ignore
    from ._models import ExtendedLocation  # type: ignore
    from ._models import Gallery  # type: ignore
    from ._models import GalleryApplication  # type: ignore
    from ._models import GalleryApplicationList  # type: ignore
    from ._models import GalleryApplicationUpdate  # type: ignore
    from ._models import GalleryApplicationVersion  # type: ignore
    from ._models import GalleryApplicationVersionList  # type: ignore
    from ._models import GalleryApplicationVersionPublishingProfile  # type: ignore
    from ._models import GalleryApplicationVersionUpdate  # type: ignore
    from ._models import GalleryArtifactPublishingProfileBase  # type: ignore
    from ._models import GalleryArtifactSource  # type: ignore
    from ._models import GalleryArtifactVersionSource  # type: ignore
    from ._models import GalleryDataDiskImage  # type: ignore
    from ._models import GalleryDiskImage  # type: ignore
    from ._models import GalleryDiskImageSource  # type: ignore
    from ._models import GalleryIdentifier  # type: ignore
    from ._models import GalleryImage  # type: ignore
    from ._models import GalleryImageFeature  # type: ignore
    from ._models import GalleryImageIdentifier  # type: ignore
    from ._models import GalleryImageList  # type: ignore
    from ._models import GalleryImageUpdate  # type: ignore
    from ._models import GalleryImageVersion  # type: ignore
    from ._models import GalleryImageVersionList  # type: ignore
    from ._models import GalleryImageVersionPublishingProfile  # type: ignore
    from ._models import GalleryImageVersionStorageProfile  # type: ignore
    from ._models import GalleryImageVersionUpdate  # type: ignore
    from ._models import GalleryList  # type: ignore
    from ._models import GalleryOSDiskImage  # type: ignore
    from ._models import GalleryUpdate  # type: ignore
    from ._models import GrantAccessData  # type: ignore
    from ._models import ImageDiskReference  # type: ignore
    from ._models import ImagePurchasePlan  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import KeyForDiskEncryptionSet  # type: ignore
    from ._models import KeyVaultAndKeyReference  # type: ignore
    from ._models import KeyVaultAndSecretReference  # type: ignore
    from ._models import ManagedArtifact  # type: ignore
    from ._models import OSDiskImageEncryption  # type: ignore
    from ._models import PirResource  # type: ignore
    from ._models import PirSharedGalleryResource  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import ProxyOnlyResource  # type: ignore
    from ._models import PurchasePlan  # type: ignore
    from ._models import RecommendedMachineConfiguration  # type: ignore
    from ._models import RegionalReplicationStatus  # type: ignore
    from ._models import ReplicationStatus  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceRange  # type: ignore
    from ._models import ResourceUriList  # type: ignore
    from ._models import ShareInfoElement  # type: ignore
    from ._models import SharedGallery  # type: ignore
    from ._models import SharedGalleryImage  # type: ignore
    from ._models import SharedGalleryImageList  # type: ignore
    from ._models import SharedGalleryImageVersion  # type: ignore
    from ._models import SharedGalleryImageVersionList  # type: ignore
    from ._models import SharedGalleryList  # type: ignore
    from ._models import SharingProfile  # type: ignore
    from ._models import SharingProfileGroup  # type: ignore
    from ._models import SharingUpdate  # type: ignore
    from ._models import Snapshot  # type: ignore
    from ._models import SnapshotList  # type: ignore
    from ._models import SnapshotSku  # type: ignore
    from ._models import SnapshotUpdate  # type: ignore
    from ._models import SourceVault  # type: ignore
    from ._models import TargetRegion  # type: ignore
    from ._models import UpdateResourceDefinition  # type: ignore
    from ._models import UserArtifactManage  # type: ignore
    from ._models import UserArtifactSource  # type: ignore

from ._compute_management_client_enums import (
    AccessLevel,
    AggregatedReplicationState,
    DiskCreateOption,
    DiskEncryptionSetIdentityType,
    DiskEncryptionSetType,
    DiskState,
    DiskStorageAccountTypes,
    EncryptionType,
    ExtendedLocationTypes,
    GalleryApplicationVersionPropertiesProvisioningState,
    GalleryImagePropertiesProvisioningState,
    GalleryImageVersionPropertiesProvisioningState,
    GalleryPropertiesProvisioningState,
    GallerySharingPermissionTypes,
    HostCaching,
    HyperVGeneration,
    NetworkAccessPolicy,
    OperatingSystemStateTypes,
    OperatingSystemTypes,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ReplicationState,
    ReplicationStatusTypes,
    SelectPermissions,
    SharedToValues,
    SharingProfileGroupTypes,
    SharingUpdateOperationTypes,
    SnapshotStorageAccountTypes,
    StorageAccountType,
)

__all__ = [
    'AccessUri',
    'ApiError',
    'ApiErrorBase',
    'CreationData',
    'DataDiskImageEncryption',
    'Disallowed',
    'Disk',
    'DiskAccess',
    'DiskAccessList',
    'DiskAccessUpdate',
    'DiskEncryptionSet',
    'DiskEncryptionSetList',
    'DiskEncryptionSetUpdate',
    'DiskImageEncryption',
    'DiskList',
    'DiskRestorePoint',
    'DiskRestorePointList',
    'DiskSku',
    'DiskUpdate',
    'Encryption',
    'EncryptionImages',
    'EncryptionSetIdentity',
    'EncryptionSettingsCollection',
    'EncryptionSettingsElement',
    'ExtendedLocation',
    'Gallery',
    'GalleryApplication',
    'GalleryApplicationList',
    'GalleryApplicationUpdate',
    'GalleryApplicationVersion',
    'GalleryApplicationVersionList',
    'GalleryApplicationVersionPublishingProfile',
    'GalleryApplicationVersionUpdate',
    'GalleryArtifactPublishingProfileBase',
    'GalleryArtifactSource',
    'GalleryArtifactVersionSource',
    'GalleryDataDiskImage',
    'GalleryDiskImage',
    'GalleryDiskImageSource',
    'GalleryIdentifier',
    'GalleryImage',
    'GalleryImageFeature',
    'GalleryImageIdentifier',
    'GalleryImageList',
    'GalleryImageUpdate',
    'GalleryImageVersion',
    'GalleryImageVersionList',
    'GalleryImageVersionPublishingProfile',
    'GalleryImageVersionStorageProfile',
    'GalleryImageVersionUpdate',
    'GalleryList',
    'GalleryOSDiskImage',
    'GalleryUpdate',
    'GrantAccessData',
    'ImageDiskReference',
    'ImagePurchasePlan',
    'InnerError',
    'KeyForDiskEncryptionSet',
    'KeyVaultAndKeyReference',
    'KeyVaultAndSecretReference',
    'ManagedArtifact',
    'OSDiskImageEncryption',
    'PirResource',
    'PirSharedGalleryResource',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'ProxyOnlyResource',
    'PurchasePlan',
    'RecommendedMachineConfiguration',
    'RegionalReplicationStatus',
    'ReplicationStatus',
    'Resource',
    'ResourceRange',
    'ResourceUriList',
    'ShareInfoElement',
    'SharedGallery',
    'SharedGalleryImage',
    'SharedGalleryImageList',
    'SharedGalleryImageVersion',
    'SharedGalleryImageVersionList',
    'SharedGalleryList',
    'SharingProfile',
    'SharingProfileGroup',
    'SharingUpdate',
    'Snapshot',
    'SnapshotList',
    'SnapshotSku',
    'SnapshotUpdate',
    'SourceVault',
    'TargetRegion',
    'UpdateResourceDefinition',
    'UserArtifactManage',
    'UserArtifactSource',
    'AccessLevel',
    'AggregatedReplicationState',
    'DiskCreateOption',
    'DiskEncryptionSetIdentityType',
    'DiskEncryptionSetType',
    'DiskState',
    'DiskStorageAccountTypes',
    'EncryptionType',
    'ExtendedLocationTypes',
    'GalleryApplicationVersionPropertiesProvisioningState',
    'GalleryImagePropertiesProvisioningState',
    'GalleryImageVersionPropertiesProvisioningState',
    'GalleryPropertiesProvisioningState',
    'GallerySharingPermissionTypes',
    'HostCaching',
    'HyperVGeneration',
    'NetworkAccessPolicy',
    'OperatingSystemStateTypes',
    'OperatingSystemTypes',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ReplicationState',
    'ReplicationStatusTypes',
    'SelectPermissions',
    'SharedToValues',
    'SharingProfileGroupTypes',
    'SharingUpdateOperationTypes',
    'SnapshotStorageAccountTypes',
    'StorageAccountType',
]
