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

from visier_object_configuration_python_sdk.pydantic.dimension_member_dto_dimension_member import DimensionMemberDTODimensionMember

class DimensionMemberDTO(BaseModel):
    dimension_member: typing.Optional[DimensionMemberDTODimensionMember] = Field(None, alias='dimensionMember')
    class Config:
        arbitrary_types_allowed = True
