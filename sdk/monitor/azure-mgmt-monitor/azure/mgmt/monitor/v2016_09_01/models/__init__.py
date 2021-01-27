# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ErrorResponse
    from ._models_py3 import LocalizableString
    from ._models_py3 import LogSettings
    from ._models_py3 import Metric
    from ._models_py3 import MetricCollection
    from ._models_py3 import MetricSettings
    from ._models_py3 import MetricValue
    from ._models_py3 import Resource
    from ._models_py3 import RetentionPolicy
    from ._models_py3 import ServiceDiagnosticSettingsResource
    from ._models_py3 import ServiceDiagnosticSettingsResourcePatch
except (SyntaxError, ImportError):
    from ._models import ErrorResponse  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import LogSettings  # type: ignore
    from ._models import Metric  # type: ignore
    from ._models import MetricCollection  # type: ignore
    from ._models import MetricSettings  # type: ignore
    from ._models import MetricValue  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RetentionPolicy  # type: ignore
    from ._models import ServiceDiagnosticSettingsResource  # type: ignore
    from ._models import ServiceDiagnosticSettingsResourcePatch  # type: ignore

from ._monitor_client_enums import (
    Unit,
)

__all__ = [
    'ErrorResponse',
    'LocalizableString',
    'LogSettings',
    'Metric',
    'MetricCollection',
    'MetricSettings',
    'MetricValue',
    'Resource',
    'RetentionPolicy',
    'ServiceDiagnosticSettingsResource',
    'ServiceDiagnosticSettingsResourcePatch',
    'Unit',
]
