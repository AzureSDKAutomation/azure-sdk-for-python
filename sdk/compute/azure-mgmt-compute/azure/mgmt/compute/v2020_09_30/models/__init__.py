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
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import DataDiskImageEncryption
    from ._models_py3 import Disallowed
    from ._models_py3 import DiskImageEncryption
    from ._models_py3 import EncryptionImages
    from ._models_py3 import Gallery
    from ._models_py3 import GalleryApplication
    from ._models_py3 import GalleryApplicationUpdate
    from ._models_py3 import GalleryApplicationVersion
    from ._models_py3 import GalleryApplicationVersionPublishingProfile
    from ._models_py3 import GalleryApplicationVersionUpdate
    from ._models_py3 import GalleryArtifactPublishingProfileBase
    from ._models_py3 import GalleryArtifactSource
    from ._models_py3 import GalleryArtifactVersionSource
    from ._models_py3 import GalleryDataDiskImage
    from ._models_py3 import GalleryDiskImage
    from ._models_py3 import GalleryIdentifier
    from ._models_py3 import GalleryImage
    from ._models_py3 import GalleryImageFeature
    from ._models_py3 import GalleryImageIdentifier
    from ._models_py3 import GalleryImageUpdate
    from ._models_py3 import GalleryImageVersion
    from ._models_py3 import GalleryImageVersionPublishingProfile
    from ._models_py3 import GalleryImageVersionStorageProfile
    from ._models_py3 import GalleryImageVersionUpdate
    from ._models_py3 import GalleryOSDiskImage
    from ._models_py3 import GalleryUpdate
    from ._models_py3 import ImagePurchasePlan
    from ._models_py3 import InnerError
    from ._models_py3 import ManagedArtifact
    from ._models_py3 import OSDiskImageEncryption
    from ._models_py3 import PirResource
    from ._models_py3 import PirSharedGalleryResource
    from ._models_py3 import RecommendedMachineConfiguration
    from ._models_py3 import RegionalReplicationStatus
    from ._models_py3 import ReplicationStatus
    from ._models_py3 import Resource
    from ._models_py3 import ResourceRange
    from ._models_py3 import SharedGallery
    from ._models_py3 import SharedGalleryImage
    from ._models_py3 import SharedGalleryImageVersion
    from ._models_py3 import SharingProfile
    from ._models_py3 import SharingProfileGroup
    from ._models_py3 import SharingUpdate
    from ._models_py3 import TargetRegion
    from ._models_py3 import UpdateResourceDefinition
    from ._models_py3 import UserArtifactSource
except (SyntaxError, ImportError):
    from ._models import ApiError
    from ._models import ApiErrorBase
    from ._models import DataDiskImageEncryption
    from ._models import Disallowed
    from ._models import DiskImageEncryption
    from ._models import EncryptionImages
    from ._models import Gallery
    from ._models import GalleryApplication
    from ._models import GalleryApplicationUpdate
    from ._models import GalleryApplicationVersion
    from ._models import GalleryApplicationVersionPublishingProfile
    from ._models import GalleryApplicationVersionUpdate
    from ._models import GalleryArtifactPublishingProfileBase
    from ._models import GalleryArtifactSource
    from ._models import GalleryArtifactVersionSource
    from ._models import GalleryDataDiskImage
    from ._models import GalleryDiskImage
    from ._models import GalleryIdentifier
    from ._models import GalleryImage
    from ._models import GalleryImageFeature
    from ._models import GalleryImageIdentifier
    from ._models import GalleryImageUpdate
    from ._models import GalleryImageVersion
    from ._models import GalleryImageVersionPublishingProfile
    from ._models import GalleryImageVersionStorageProfile
    from ._models import GalleryImageVersionUpdate
    from ._models import GalleryOSDiskImage
    from ._models import GalleryUpdate
    from ._models import ImagePurchasePlan
    from ._models import InnerError
    from ._models import ManagedArtifact
    from ._models import OSDiskImageEncryption
    from ._models import PirResource
    from ._models import PirSharedGalleryResource
    from ._models import RecommendedMachineConfiguration
    from ._models import RegionalReplicationStatus
    from ._models import ReplicationStatus
    from ._models import Resource
    from ._models import ResourceRange
    from ._models import SharedGallery
    from ._models import SharedGalleryImage
    from ._models import SharedGalleryImageVersion
    from ._models import SharingProfile
    from ._models import SharingProfileGroup
    from ._models import SharingUpdate
    from ._models import TargetRegion
    from ._models import UpdateResourceDefinition
    from ._models import UserArtifactSource
from ._paged_models import GalleryApplicationPaged
from ._paged_models import GalleryApplicationVersionPaged
from ._paged_models import GalleryImagePaged
from ._paged_models import GalleryImageVersionPaged
from ._paged_models import GalleryPaged
from ._paged_models import SharedGalleryImagePaged
from ._paged_models import SharedGalleryImageVersionPaged
from ._paged_models import SharedGalleryPaged
from ._compute_management_client_enums import (
    GallerySharingPermissionTypes,
    SharingProfileGroupTypes,
    OperatingSystemTypes,
    AggregatedReplicationState,
    ReplicationState,
    OperatingSystemStateTypes,
    HyperVGeneration,
    StorageAccountType,
    HostCaching,
    SharingUpdateOperationTypes,
    Permissions,
    ReplicationStatusTypes,
    SharedToValues,
)

__all__ = [
    'ApiError',
    'ApiErrorBase',
    'DataDiskImageEncryption',
    'Disallowed',
    'DiskImageEncryption',
    'EncryptionImages',
    'Gallery',
    'GalleryApplication',
    'GalleryApplicationUpdate',
    'GalleryApplicationVersion',
    'GalleryApplicationVersionPublishingProfile',
    'GalleryApplicationVersionUpdate',
    'GalleryArtifactPublishingProfileBase',
    'GalleryArtifactSource',
    'GalleryArtifactVersionSource',
    'GalleryDataDiskImage',
    'GalleryDiskImage',
    'GalleryIdentifier',
    'GalleryImage',
    'GalleryImageFeature',
    'GalleryImageIdentifier',
    'GalleryImageUpdate',
    'GalleryImageVersion',
    'GalleryImageVersionPublishingProfile',
    'GalleryImageVersionStorageProfile',
    'GalleryImageVersionUpdate',
    'GalleryOSDiskImage',
    'GalleryUpdate',
    'ImagePurchasePlan',
    'InnerError',
    'ManagedArtifact',
    'OSDiskImageEncryption',
    'PirResource',
    'PirSharedGalleryResource',
    'RecommendedMachineConfiguration',
    'RegionalReplicationStatus',
    'ReplicationStatus',
    'Resource',
    'ResourceRange',
    'SharedGallery',
    'SharedGalleryImage',
    'SharedGalleryImageVersion',
    'SharingProfile',
    'SharingProfileGroup',
    'SharingUpdate',
    'TargetRegion',
    'UpdateResourceDefinition',
    'UserArtifactSource',
    'GalleryPaged',
    'GalleryImagePaged',
    'GalleryImageVersionPaged',
    'GalleryApplicationPaged',
    'GalleryApplicationVersionPaged',
    'SharedGalleryPaged',
    'SharedGalleryImagePaged',
    'SharedGalleryImageVersionPaged',
    'GallerySharingPermissionTypes',
    'SharingProfileGroupTypes',
    'OperatingSystemTypes',
    'AggregatedReplicationState',
    'ReplicationState',
    'OperatingSystemStateTypes',
    'HyperVGeneration',
    'StorageAccountType',
    'HostCaching',
    'SharingUpdateOperationTypes',
    'Permissions',
    'ReplicationStatusTypes',
    'SharedToValues',
]
