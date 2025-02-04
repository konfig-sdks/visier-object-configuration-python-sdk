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

class RequiredSelectionConceptConfigurationDTO(TypedDict):
    pass

class OptionalSelectionConceptConfigurationDTO(TypedDict, total=False):
    # A list of analytic object filters indicating the analytic object and dimension used for this selection concept.
    analyticObjectFilters: typing.List[AnalyticObjectFilterDTO]

class SelectionConceptConfigurationDTO(RequiredSelectionConceptConfigurationDTO, OptionalSelectionConceptConfigurationDTO):
    pass
