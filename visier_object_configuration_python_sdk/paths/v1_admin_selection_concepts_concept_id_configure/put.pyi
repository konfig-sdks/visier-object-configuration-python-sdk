# coding: utf-8

"""
    Visier Object Configuration APIs

    Visier APIs for managing objects in studio experience

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_object_configuration_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_object_configuration_python_sdk.api_response import AsyncGeneratorResponse
from visier_object_configuration_python_sdk import api_client, exceptions
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

from visier_object_configuration_python_sdk.model.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO as SelectionConceptConfigurationMapDTOSchema
from visier_object_configuration_python_sdk.model.status import Status as StatusSchema
from visier_object_configuration_python_sdk.model.analytic_object_filter_dto import AnalyticObjectFilterDTO as AnalyticObjectFilterDTOSchema
from visier_object_configuration_python_sdk.model.concept_configuration_result_dto import ConceptConfigurationResultDTO as ConceptConfigurationResultDTOSchema

from visier_object_configuration_python_sdk.type.analytic_object_filter_dto import AnalyticObjectFilterDTO
from visier_object_configuration_python_sdk.type.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO
from visier_object_configuration_python_sdk.type.status import Status
from visier_object_configuration_python_sdk.type.concept_configuration_result_dto import ConceptConfigurationResultDTO

from ...api_client import Dictionary
from visier_object_configuration_python_sdk.pydantic.analytic_object_filter_dto import AnalyticObjectFilterDTO as AnalyticObjectFilterDTOPydantic
from visier_object_configuration_python_sdk.pydantic.concept_configuration_result_dto import ConceptConfigurationResultDTO as ConceptConfigurationResultDTOPydantic
from visier_object_configuration_python_sdk.pydantic.status import Status as StatusPydantic
from visier_object_configuration_python_sdk.pydantic.selection_concept_configuration_map_dto import SelectionConceptConfigurationMapDTO as SelectionConceptConfigurationMapDTOPydantic

# Path params
ConceptIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'conceptId': typing.Union[ConceptIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_concept_id = api_client.PathParameter(
    name="conceptId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConceptIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = SelectionConceptConfigurationMapDTOSchema


request_body_selection_concept_configuration_map_dto = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ConceptConfigurationResultDTOSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ConceptConfigurationResultDTO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ConceptConfigurationResultDTO


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _map_selection_concept_mapped_args(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if analytic_object_filters_to_map is not None:
            _body["analyticObjectFiltersToMap"] = analytic_object_filters_to_map
        args.body = _body
        if concept_id is not None:
            _path_params["conceptId"] = concept_id
        args.path = _path_params
        return args

    async def _amap_selection_concept_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Map dimension members to a selection concept
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_concept_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/admin/selection-concepts/{conceptId}/configure',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_selection_concept_configuration_map_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _map_selection_concept_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Map dimension members to a selection concept
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_concept_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/admin/selection-concepts/{conceptId}/configure',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_selection_concept_configuration_map_dto.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class MapSelectionConceptRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def amap_selection_concept(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._map_selection_concept_mapped_args(
            concept_id=concept_id,
            analytic_object_filters_to_map=analytic_object_filters_to_map,
        )
        return await self._amap_selection_concept_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def map_selection_concept(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._map_selection_concept_mapped_args(
            concept_id=concept_id,
            analytic_object_filters_to_map=analytic_object_filters_to_map,
        )
        return self._map_selection_concept_oapg(
            body=args.body,
            path_params=args.path,
        )

class MapSelectionConcept(BaseApi):

    async def amap_selection_concept(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ConceptConfigurationResultDTOPydantic:
        raw_response = await self.raw.amap_selection_concept(
            concept_id=concept_id,
            analytic_object_filters_to_map=analytic_object_filters_to_map,
            **kwargs,
        )
        if validate:
            return ConceptConfigurationResultDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConceptConfigurationResultDTOPydantic, raw_response.body)
    
    
    def map_selection_concept(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
        validate: bool = False,
    ) -> ConceptConfigurationResultDTOPydantic:
        raw_response = self.raw.map_selection_concept(
            concept_id=concept_id,
            analytic_object_filters_to_map=analytic_object_filters_to_map,
        )
        if validate:
            return ConceptConfigurationResultDTOPydantic(**raw_response.body)
        return api_client.construct_model_instance(ConceptConfigurationResultDTOPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._map_selection_concept_mapped_args(
            concept_id=concept_id,
            analytic_object_filters_to_map=analytic_object_filters_to_map,
        )
        return await self._amap_selection_concept_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        concept_id: str,
        analytic_object_filters_to_map: typing.Optional[typing.List[AnalyticObjectFilterDTO]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._map_selection_concept_mapped_args(
            concept_id=concept_id,
            analytic_object_filters_to_map=analytic_object_filters_to_map,
        )
        return self._map_selection_concept_oapg(
            body=args.body,
            path_params=args.path,
        )

