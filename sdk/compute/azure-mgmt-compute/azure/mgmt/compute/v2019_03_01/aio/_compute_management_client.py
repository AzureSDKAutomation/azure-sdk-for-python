# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ComputeManagementClientConfiguration
from .operations import Operations
from .operations import AvailabilitySetsOperations
from .operations import ProximityPlacementGroupsOperations
from .operations import DedicatedHostGroupsOperations
from .operations import DedicatedHostsOperations
from .operations import VirtualMachineExtensionImagesOperations
from .operations import VirtualMachineExtensionsOperations
from .operations import VirtualMachineImagesOperations
from .operations import UsageOperations
from .operations import VirtualMachinesOperations
from .operations import VirtualMachineSizesOperations
from .operations import ImagesOperations
from .operations import VirtualMachineScaleSetsOperations
from .operations import VirtualMachineScaleSetExtensionsOperations
from .operations import VirtualMachineScaleSetRollingUpgradesOperations
from .operations import VirtualMachineScaleSetVMsOperations
from .operations import LogAnalyticsOperations
from .operations import VirtualMachineRunCommandsOperations
from .operations import GalleriesOperations
from .operations import GalleryImagesOperations
from .operations import GalleryImageVersionsOperations
from .operations import GalleryApplicationsOperations
from .operations import GalleryApplicationVersionsOperations
from .operations import DisksOperations
from .operations import SnapshotsOperations
from .. import models


class ComputeManagementClient(object):
    """Compute Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.compute.v2019_03_01.aio.operations.Operations
    :ivar availability_sets: AvailabilitySetsOperations operations
    :vartype availability_sets: azure.mgmt.compute.v2019_03_01.aio.operations.AvailabilitySetsOperations
    :ivar proximity_placement_groups: ProximityPlacementGroupsOperations operations
    :vartype proximity_placement_groups: azure.mgmt.compute.v2019_03_01.aio.operations.ProximityPlacementGroupsOperations
    :ivar dedicated_host_groups: DedicatedHostGroupsOperations operations
    :vartype dedicated_host_groups: azure.mgmt.compute.v2019_03_01.aio.operations.DedicatedHostGroupsOperations
    :ivar dedicated_hosts: DedicatedHostsOperations operations
    :vartype dedicated_hosts: azure.mgmt.compute.v2019_03_01.aio.operations.DedicatedHostsOperations
    :ivar virtual_machine_extension_images: VirtualMachineExtensionImagesOperations operations
    :vartype virtual_machine_extension_images: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineExtensionImagesOperations
    :ivar virtual_machine_extensions: VirtualMachineExtensionsOperations operations
    :vartype virtual_machine_extensions: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineExtensionsOperations
    :ivar virtual_machine_images: VirtualMachineImagesOperations operations
    :vartype virtual_machine_images: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineImagesOperations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.compute.v2019_03_01.aio.operations.UsageOperations
    :ivar virtual_machines: VirtualMachinesOperations operations
    :vartype virtual_machines: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachinesOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineSizesOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.compute.v2019_03_01.aio.operations.ImagesOperations
    :ivar virtual_machine_scale_sets: VirtualMachineScaleSetsOperations operations
    :vartype virtual_machine_scale_sets: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineScaleSetsOperations
    :ivar virtual_machine_scale_set_extensions: VirtualMachineScaleSetExtensionsOperations operations
    :vartype virtual_machine_scale_set_extensions: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineScaleSetExtensionsOperations
    :ivar virtual_machine_scale_set_rolling_upgrades: VirtualMachineScaleSetRollingUpgradesOperations operations
    :vartype virtual_machine_scale_set_rolling_upgrades: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineScaleSetRollingUpgradesOperations
    :ivar virtual_machine_scale_set_vms: VirtualMachineScaleSetVMsOperations operations
    :vartype virtual_machine_scale_set_vms: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineScaleSetVMsOperations
    :ivar log_analytics: LogAnalyticsOperations operations
    :vartype log_analytics: azure.mgmt.compute.v2019_03_01.aio.operations.LogAnalyticsOperations
    :ivar virtual_machine_run_commands: VirtualMachineRunCommandsOperations operations
    :vartype virtual_machine_run_commands: azure.mgmt.compute.v2019_03_01.aio.operations.VirtualMachineRunCommandsOperations
    :ivar galleries: GalleriesOperations operations
    :vartype galleries: azure.mgmt.compute.v2019_03_01.aio.operations.GalleriesOperations
    :ivar gallery_images: GalleryImagesOperations operations
    :vartype gallery_images: azure.mgmt.compute.v2019_03_01.aio.operations.GalleryImagesOperations
    :ivar gallery_image_versions: GalleryImageVersionsOperations operations
    :vartype gallery_image_versions: azure.mgmt.compute.v2019_03_01.aio.operations.GalleryImageVersionsOperations
    :ivar gallery_applications: GalleryApplicationsOperations operations
    :vartype gallery_applications: azure.mgmt.compute.v2019_03_01.aio.operations.GalleryApplicationsOperations
    :ivar gallery_application_versions: GalleryApplicationVersionsOperations operations
    :vartype gallery_application_versions: azure.mgmt.compute.v2019_03_01.aio.operations.GalleryApplicationVersionsOperations
    :ivar disks: DisksOperations operations
    :vartype disks: azure.mgmt.compute.v2019_03_01.aio.operations.DisksOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: azure.mgmt.compute.v2019_03_01.aio.operations.SnapshotsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ComputeManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.proximity_placement_groups = ProximityPlacementGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dedicated_host_groups = DedicatedHostGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dedicated_hosts = DedicatedHostsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_extension_images = VirtualMachineExtensionImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_extensions = VirtualMachineExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_images = VirtualMachineImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.images = ImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_sets = VirtualMachineScaleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_extensions = VirtualMachineScaleSetExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_rolling_upgrades = VirtualMachineScaleSetRollingUpgradesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_vms = VirtualMachineScaleSetVMsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.log_analytics = LogAnalyticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_run_commands = VirtualMachineRunCommandsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.galleries = GalleriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_images = GalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_image_versions = GalleryImageVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_applications = GalleryApplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_application_versions = GalleryApplicationVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disks = DisksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.snapshots = SnapshotsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ComputeManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
