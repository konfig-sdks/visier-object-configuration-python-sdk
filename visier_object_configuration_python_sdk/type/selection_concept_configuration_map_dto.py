# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from visier_object_configuration_python_sdk.type.analytic_object_filter_dto import AnalyticObjectFilterDTO

class RequiredSelectionConceptConfigurationMapDTO(TypedDict):
    pass

class OptionalSelectionConceptConfigurationMapDTO(TypedDict, total=False):
    # A list of analytic object filters indicating the analytic object and dimension members used  for the selection concept.   Note: If this array is empty, all filters will be removed for the concept.
    analyticObjectFiltersToMap: typing.List[AnalyticObjectFilterDTO]

class SelectionConceptConfigurationMapDTO(RequiredSelectionConceptConfigurationMapDTO, OptionalSelectionConceptConfigurationMapDTO):
    pass
