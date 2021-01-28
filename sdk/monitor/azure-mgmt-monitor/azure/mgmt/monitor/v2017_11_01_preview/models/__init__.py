# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Baseline
    from ._models_py3 import BaselineMetadataValue
    from ._models_py3 import BaselineResponse
    from ._models_py3 import CalculateBaselineResponse
    from ._models_py3 import ErrorResponse
    from ._models_py3 import LocalizableString
    from ._models_py3 import TimeSeriesInformation
except (SyntaxError, ImportError):
    from ._models import Baseline  # type: ignore
    from ._models import BaselineMetadataValue  # type: ignore
    from ._models import BaselineResponse  # type: ignore
    from ._models import CalculateBaselineResponse  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import TimeSeriesInformation  # type: ignore

from ._monitor_client_enums import (
    ResultType,
    Sensitivity,
)

__all__ = [
    'Baseline',
    'BaselineMetadataValue',
    'BaselineResponse',
    'CalculateBaselineResponse',
    'ErrorResponse',
    'LocalizableString',
    'TimeSeriesInformation',
    'ResultType',
    'Sensitivity',
]
