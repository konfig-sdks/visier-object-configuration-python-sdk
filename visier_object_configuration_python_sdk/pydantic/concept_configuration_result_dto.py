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


class ConceptConfigurationResultDTO(BaseModel):
    # The unique identifier of the configured concept.
    concept_id: typing.Optional[str] = Field(None, alias='conceptId')

    # The unique identifier of the system-generated project.
    project_id: typing.Optional[str] = Field(None, alias='projectId')

    # A meaningful message about the API result.
    message: typing.Optional[str] = Field(None, alias='message')
    class Config:
        arbitrary_types_allowed = True
