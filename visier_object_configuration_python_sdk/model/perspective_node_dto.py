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


class PerspectiveNodeDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            selectionConceptUuid = schemas.StrSchema
            symbolName = schemas.StrSchema
            
            
            class analyticObjectFilters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AnalyticObjectFilterDTO']:
                        return AnalyticObjectFilterDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AnalyticObjectFilterDTO'], typing.List['AnalyticObjectFilterDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'analyticObjectFilters':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AnalyticObjectFilterDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "selectionConceptUuid": selectionConceptUuid,
                "symbolName": symbolName,
                "analyticObjectFilters": analyticObjectFilters,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectionConceptUuid"]) -> MetaOapg.properties.selectionConceptUuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbolName"]) -> MetaOapg.properties.symbolName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyticObjectFilters"]) -> MetaOapg.properties.analyticObjectFilters: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["selectionConceptUuid", "symbolName", "analyticObjectFilters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectionConceptUuid"]) -> typing.Union[MetaOapg.properties.selectionConceptUuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbolName"]) -> typing.Union[MetaOapg.properties.symbolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyticObjectFilters"]) -> typing.Union[MetaOapg.properties.analyticObjectFilters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["selectionConceptUuid", "symbolName", "analyticObjectFilters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        selectionConceptUuid: typing.Union[MetaOapg.properties.selectionConceptUuid, str, schemas.Unset] = schemas.unset,
        symbolName: typing.Union[MetaOapg.properties.symbolName, str, schemas.Unset] = schemas.unset,
        analyticObjectFilters: typing.Union[MetaOapg.properties.analyticObjectFilters, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PerspectiveNodeDTO':
        return super().__new__(
            cls,
            *args,
            selectionConceptUuid=selectionConceptUuid,
            symbolName=symbolName,
            analyticObjectFilters=analyticObjectFilters,
            _configuration=_configuration,
            **kwargs,
        )

from visier_object_configuration_python_sdk.model.analytic_object_filter_dto import AnalyticObjectFilterDTO
