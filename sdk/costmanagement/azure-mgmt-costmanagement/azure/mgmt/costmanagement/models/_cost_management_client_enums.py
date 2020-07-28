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

from enum import Enum


class ReportTimeframeType(str, Enum):

    week_to_date = "WeekToDate"
    month_to_date = "MonthToDate"
    year_to_date = "YearToDate"
    custom = "Custom"


class ReportGranularityType(str, Enum):

    daily = "Daily"
    monthly = "Monthly"


class ReportConfigColumnType(str, Enum):

    tag = "Tag"
    dimension = "Dimension"


class OperatorType(str, Enum):

    in_enum = "In"
    contains = "Contains"


class ChartType(str, Enum):

    area = "Area"
    line = "Line"
    stacked_column = "StackedColumn"
    grouped_column = "GroupedColumn"
    table = "Table"


class AccumulatedType(str, Enum):

    true = "true"
    false = "false"


class MetricType(str, Enum):

    actual_cost = "ActualCost"
    amortized_cost = "AmortizedCost"
    ahub = "AHUB"


class KpiTypeType(str, Enum):

    forecast = "Forecast"
    budget = "Budget"


class PivotTypeType(str, Enum):

    dimension = "Dimension"
    tag_key = "TagKey"


class InsightsStatus(str, Enum):

    new = "New"
    dismissed = "Dismissed"
    acknowledged = "Acknowledged"
    resolved = "Resolved"


class AlertType(str, Enum):

    budget = "Budget"
    invoice = "Invoice"
    credit = "Credit"
    quota = "Quota"
    general = "General"
    x_cloud = "xCloud"
    budget_forecast = "BudgetForecast"


class AlertCategory(str, Enum):

    cost = "Cost"
    usage = "Usage"
    billing = "Billing"
    system = "System"


class AlertCriteria(str, Enum):

    cost_threshold_exceeded = "CostThresholdExceeded"
    usage_threshold_exceeded = "UsageThresholdExceeded"
    credit_threshold_approaching = "CreditThresholdApproaching"
    credit_threshold_reached = "CreditThresholdReached"
    quota_threshold_approaching = "QuotaThresholdApproaching"
    quota_threshold_reached = "QuotaThresholdReached"
    multi_currency = "MultiCurrency"
    forecast_cost_threshold_exceeded = "ForecastCostThresholdExceeded"
    forecast_usage_threshold_exceeded = "ForecastUsageThresholdExceeded"
    invoice_due_date_approaching = "InvoiceDueDateApproaching"
    invoice_due_date_reached = "InvoiceDueDateReached"
    cross_cloud_new_data_available = "CrossCloudNewDataAvailable"
    cross_cloud_collection_error = "CrossCloudCollectionError"
    general_threshold_error = "GeneralThresholdError"


class AlertSource(str, Enum):

    preset = "Preset"
    user = "User"


class AlertTimeGrainType(str, Enum):

    none = "None"
    monthly = "Monthly"
    quarterly = "Quarterly"
    annually = "Annually"
    billing_month = "BillingMonth"
    billing_quarter = "BillingQuarter"
    billing_annual = "BillingAnnual"


class AlertOperator(str, Enum):

    none = "None"
    equal_to = "EqualTo"
    greater_than = "GreaterThan"
    greater_than_or_equal_to = "GreaterThanOrEqualTo"
    less_than = "LessThan"
    less_than_or_equal_to = "LessThanOrEqualTo"


class AlertStatus(str, Enum):

    none = "None"
    active = "Active"
    overridden = "Overridden"
    resolved = "Resolved"
    dismissed = "Dismissed"


class ForecastType(str, Enum):

    usage = "Usage"
    actual_cost = "ActualCost"
    amortized_cost = "AmortizedCost"


class ForecastTimeframeType(str, Enum):

    month_to_date = "MonthToDate"
    billing_month_to_date = "BillingMonthToDate"
    the_last_month = "TheLastMonth"
    the_last_billing_month = "TheLastBillingMonth"
    week_to_date = "WeekToDate"
    custom = "Custom"


class GranularityType(str, Enum):

    daily = "Daily"


class QueryColumnType(str, Enum):

    tag = "Tag"
    dimension = "Dimension"


class ExportType(str, Enum):

    usage = "Usage"
    actual_cost = "ActualCost"
    amortized_cost = "AmortizedCost"


class TimeframeType(str, Enum):

    month_to_date = "MonthToDate"
    billing_month_to_date = "BillingMonthToDate"
    the_last_month = "TheLastMonth"
    the_last_billing_month = "TheLastBillingMonth"
    week_to_date = "WeekToDate"
    custom = "Custom"


class StatusType(str, Enum):

    active = "Active"
    inactive = "Inactive"


class RecurrenceType(str, Enum):

    daily = "Daily"
    weekly = "Weekly"
    monthly = "Monthly"
    annually = "Annually"


class FormatType(str, Enum):

    csv = "Csv"


class ExecutionType(str, Enum):

    on_demand = "OnDemand"
    scheduled = "Scheduled"


class ExecutionStatus(str, Enum):

    queued = "Queued"
    in_progress = "InProgress"
    completed = "Completed"
    failed = "Failed"
    timeout = "Timeout"
    new_data_not_available = "NewDataNotAvailable"
    data_not_available = "DataNotAvailable"


class ExternalCloudProviderType(str, Enum):

    external_subscriptions = "externalSubscriptions"
    external_billing_accounts = "externalBillingAccounts"
