# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_object_configuration_python_sdk import schemas  # noqa: F401


class PerspectiveConfigurationDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            perspectiveId = schemas.StrSchema
            perspectiveName = schemas.StrSchema
            
            
            class perspectiveNodes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PerspectiveNodeDTO']:
                        return PerspectiveNodeDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PerspectiveNodeDTO'], typing.List['PerspectiveNodeDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'perspectiveNodes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PerspectiveNodeDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "perspectiveId": perspectiveId,
                "perspectiveName": perspectiveName,
                "perspectiveNodes": perspectiveNodes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["perspectiveId"]) -> MetaOapg.properties.perspectiveId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["perspectiveName"]) -> MetaOapg.properties.perspectiveName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["perspectiveNodes"]) -> MetaOapg.properties.perspectiveNodes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["perspectiveId", "perspectiveName", "perspectiveNodes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["perspectiveId"]) -> typing.Union[MetaOapg.properties.perspectiveId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["perspectiveName"]) -> typing.Union[MetaOapg.properties.perspectiveName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["perspectiveNodes"]) -> typing.Union[MetaOapg.properties.perspectiveNodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["perspectiveId", "perspectiveName", "perspectiveNodes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        perspectiveId: typing.Union[MetaOapg.properties.perspectiveId, str, schemas.Unset] = schemas.unset,
        perspectiveName: typing.Union[MetaOapg.properties.perspectiveName, str, schemas.Unset] = schemas.unset,
        perspectiveNodes: typing.Union[MetaOapg.properties.perspectiveNodes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PerspectiveConfigurationDTO':
        return super().__new__(
            cls,
            *args,
            perspectiveId=perspectiveId,
            perspectiveName=perspectiveName,
            perspectiveNodes=perspectiveNodes,
            _configuration=_configuration,
            **kwargs,
        )

from visier_object_configuration_python_sdk.model.perspective_node_dto import PerspectiveNodeDTO
