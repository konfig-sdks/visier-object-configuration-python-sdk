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
from pydantic import BaseModel, Field, RootModel

from visier_object_configuration_python_sdk.pydantic.dimension_filter_dto import DimensionFilterDTO

class AnalyticObjectFilterDTO(BaseModel):
    # The UUID of the analytic object used in the selection concept.
    analytic_object_uuid: typing.Optional[str] = Field(None, alias='analyticObjectUuid')

    # The symbol name of the analytic object.
    symbol_name: typing.Optional[str] = Field(None, alias='symbolName')

    # A list of dimensions included in the concept.
    dimensions: typing.Optional[typing.List[DimensionFilterDTO]] = Field(None, alias='dimensions')
    class Config:
        arbitrary_types_allowed = True
