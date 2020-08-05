# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ComparisonOperationType(str, Enum):
    """the operator that is used to compare the metric data and the threshold.
    """

    equals = "Equals"
    not_equals = "NotEquals"
    greater_than = "GreaterThan"
    greater_than_or_equal = "GreaterThanOrEqual"
    less_than = "LessThan"
    less_than_or_equal = "LessThanOrEqual"

class EventLevel(str, Enum):
    """the event level
    """

    critical = "Critical"
    error = "Error"
    warning = "Warning"
    informational = "Informational"
    verbose = "Verbose"

class MetricStatisticType(str, Enum):
    """the metric statistic type. How the metrics from multiple instances are combined.
    """

    average = "Average"
    min = "Min"
    max = "Max"
    sum = "Sum"

class RecurrenceFrequency(str, Enum):
    """the recurrence frequency. How often the schedule profile should take effect. This value must be
    Week, meaning each week will have the same set of profiles. For example, to set a daily
    schedule, set **schedule** to every day of the week. The frequency property specifies that the
    schedule is repeated weekly.
    """

    none = "None"
    second = "Second"
    minute = "Minute"
    hour = "Hour"
    day = "Day"
    week = "Week"
    month = "Month"
    year = "Year"

class ScaleDirection(str, Enum):
    """the scale direction. Whether the scaling action increases or decreases the number of instances.
    """

    none = "None"
    increase = "Increase"
    decrease = "Decrease"

class ScaleRuleMetricDimensionOperationType(str, Enum):
    """the dimension operator. Only 'Equals' and 'NotEquals' are supported. 'Equals' being equal to
    any of the values. 'NotEquals' being not equal to all of the values
    """

    equals = "Equals"
    not_equals = "NotEquals"

class ScaleType(str, Enum):
    """the type of action that should occur when the scale rule fires.
    """

    change_count = "ChangeCount"
    percent_change_count = "PercentChangeCount"
    exact_count = "ExactCount"

class TimeAggregationType(str, Enum):
    """time aggregation type. How the data that is collected should be combined over time. The default
    value is Average.
    """

    average = "Average"
    minimum = "Minimum"
    maximum = "Maximum"
    total = "Total"
    count = "Count"
    last = "Last"
