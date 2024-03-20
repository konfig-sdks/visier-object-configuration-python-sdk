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

from visier_object_configuration_python_sdk.type.calculation_concept_dto import CalculationConceptDTO

class RequiredCalculationConceptListDTO(TypedDict):
    pass

class OptionalCalculationConceptListDTO(TypedDict, total=False):
    # A list of objects representing calculation concepts.
    concepts: typing.List[CalculationConceptDTO]

class CalculationConceptListDTO(RequiredCalculationConceptListDTO, OptionalCalculationConceptListDTO):
    pass
