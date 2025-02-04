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

from visier_object_configuration_python_sdk.pydantic.perspective_node_dto import PerspectiveNodeDTO

class PerspectiveConfigurationDTO(BaseModel):
    # The UUID of the perspective.
    perspective_id: typing.Optional[str] = Field(None, alias='perspectiveId')

    # The display name of the perspective.
    perspective_name: typing.Optional[str] = Field(None, alias='perspectiveName')

    # A list of nodes in the perspective.
    perspective_nodes: typing.Optional[typing.List[PerspectiveNodeDTO]] = Field(None, alias='perspectiveNodes')
    class Config:
        arbitrary_types_allowed = True
