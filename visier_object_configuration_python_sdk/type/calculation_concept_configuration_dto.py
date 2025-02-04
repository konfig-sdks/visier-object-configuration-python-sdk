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

from visier_object_configuration_python_sdk.type.perspective_configuration_dto import PerspectiveConfigurationDTO

class RequiredCalculationConceptConfigurationDTO(TypedDict):
    pass

class OptionalCalculationConceptConfigurationDTO(TypedDict, total=False):
    # A list of objects representing the perspectives in the calculation concept.
    perspectives: typing.List[PerspectiveConfigurationDTO]

class CalculationConceptConfigurationDTO(RequiredCalculationConceptConfigurationDTO, OptionalCalculationConceptConfigurationDTO):
    pass
