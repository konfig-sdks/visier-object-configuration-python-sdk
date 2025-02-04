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


class CalculationConceptListDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class concepts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CalculationConceptDTO']:
                        return CalculationConceptDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CalculationConceptDTO'], typing.List['CalculationConceptDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'concepts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CalculationConceptDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "concepts": concepts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["concepts"]) -> MetaOapg.properties.concepts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["concepts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["concepts"]) -> typing.Union[MetaOapg.properties.concepts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["concepts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        concepts: typing.Union[MetaOapg.properties.concepts, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CalculationConceptListDTO':
        return super().__new__(
            cls,
            *args,
            concepts=concepts,
            _configuration=_configuration,
            **kwargs,
        )

from visier_object_configuration_python_sdk.model.calculation_concept_dto import CalculationConceptDTO
