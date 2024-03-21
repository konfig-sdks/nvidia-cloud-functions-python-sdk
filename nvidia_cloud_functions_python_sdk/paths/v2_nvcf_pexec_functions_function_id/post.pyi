# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from nvidia_cloud_functions_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from nvidia_cloud_functions_python_sdk.api_response import AsyncGeneratorResponse
from nvidia_cloud_functions_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nvidia_cloud_functions_python_sdk import schemas  # noqa: F401

from nvidia_cloud_functions_python_sdk.model.function_invocation_invoke_function403_response import FunctionInvocationInvokeFunction403Response as FunctionInvocationInvokeFunction403ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_invoke_function402_response import FunctionInvocationInvokeFunction402Response as FunctionInvocationInvokeFunction402ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_invoke_function_response import FunctionInvocationInvokeFunctionResponse as FunctionInvocationInvokeFunctionResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_invoke_function200_response import FunctionInvocationInvokeFunction200Response as FunctionInvocationInvokeFunction200ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_invoke_function202_response import FunctionInvocationInvokeFunction202Response as FunctionInvocationInvokeFunction202ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_invoke_function302_response import FunctionInvocationInvokeFunction302Response as FunctionInvocationInvokeFunction302ResponseSchema

from nvidia_cloud_functions_python_sdk.type.function_invocation_invoke_function202_response import FunctionInvocationInvokeFunction202Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_invoke_function200_response import FunctionInvocationInvokeFunction200Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_invoke_function403_response import FunctionInvocationInvokeFunction403Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_invoke_function302_response import FunctionInvocationInvokeFunction302Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_invoke_function_response import FunctionInvocationInvokeFunctionResponse
from nvidia_cloud_functions_python_sdk.type.function_invocation_invoke_function402_response import FunctionInvocationInvokeFunction402Response

from ...api_client import Dictionary
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_invoke_function200_response import FunctionInvocationInvokeFunction200Response as FunctionInvocationInvokeFunction200ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_invoke_function_response import FunctionInvocationInvokeFunctionResponse as FunctionInvocationInvokeFunctionResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_invoke_function202_response import FunctionInvocationInvokeFunction202Response as FunctionInvocationInvokeFunction202ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_invoke_function403_response import FunctionInvocationInvokeFunction403Response as FunctionInvocationInvokeFunction403ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_invoke_function302_response import FunctionInvocationInvokeFunction302Response as FunctionInvocationInvokeFunction302ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_invoke_function402_response import FunctionInvocationInvokeFunction402Response as FunctionInvocationInvokeFunction402ResponsePydantic

# Header params


class NVCFINPUTASSETREFERENCESSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'NVCFINPUTASSETREFERENCESSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class NVCFPOLLSECONDSSchema(
    schemas.Int32Schema
):
    pass
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'NVCF-INPUT-ASSET-REFERENCES': typing.Union[NVCFINPUTASSETREFERENCESSchema, list, tuple, ],
        'NVCF-POLL-SECONDS': typing.Union[NVCFPOLLSECONDSSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_nvcf_input_asset_references = api_client.HeaderParameter(
    name="NVCF-INPUT-ASSET-REFERENCES",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFINPUTASSETREFERENCESSchema,
)
request_header_nvcf_poll_seconds = api_client.HeaderParameter(
    name="NVCF-POLL-SECONDS",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFPOLLSECONDSSchema,
)
# Path params
FunctionIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'functionId': typing.Union[FunctionIdSchema, str, uuid.UUID, ],
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


request_path_function_id = api_client.PathParameter(
    name="functionId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FunctionIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = schemas.DictSchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
NVCFREQIDSchema = schemas.StrSchema
NVCFPERCENTCOMPLETESchema = schemas.StrSchema
NVCFSTATUSSchema = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJson = FunctionInvocationInvokeFunction200ResponseSchema
SchemaFor200ResponseBodyTextEventStream = FunctionInvocationInvokeFunctionResponseSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'NVCF-REQID': NVCFREQIDSchema,
        'NVCF-PERCENT-COMPLETE': NVCFPERCENTCOMPLETESchema,
        'NVCF-STATUS': NVCFSTATUSSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FunctionInvocationInvokeFunction200Response


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FunctionInvocationInvokeFunction200Response


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/event-stream': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextEventStream),
    },
    headers=[
        nvcf_reqid_parameter,
        nvcf_percent_complete_parameter,
        nvcf_status_parameter,
    ]
)
NVCFREQIDSchema = schemas.StrSchema
NVCFPERCENTCOMPLETESchema = schemas.StrSchema
NVCFSTATUSSchema = schemas.StrSchema
SchemaFor202ResponseBodyApplicationJson = FunctionInvocationInvokeFunction202ResponseSchema
ResponseHeadersFor202 = typing_extensions.TypedDict(
    'ResponseHeadersFor202',
    {
        'NVCF-REQID': NVCFREQIDSchema,
        'NVCF-PERCENT-COMPLETE': NVCFPERCENTCOMPLETESchema,
        'NVCF-STATUS': NVCFSTATUSSchema,
    }
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: FunctionInvocationInvokeFunction202Response


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: FunctionInvocationInvokeFunction202Response


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
    headers=[
        nvcf_reqid_parameter,
        nvcf_percent_complete_parameter,
        nvcf_status_parameter,
    ]
)
NVCFREQIDSchema = schemas.StrSchema
NVCFPERCENTCOMPLETESchema = schemas.StrSchema
NVCFSTATUSSchema = schemas.StrSchema
LocationSchema = schemas.StrSchema
SchemaFor302ResponseBodyApplicationJson = FunctionInvocationInvokeFunction302ResponseSchema
ResponseHeadersFor302 = typing_extensions.TypedDict(
    'ResponseHeadersFor302',
    {
        'NVCF-REQID': NVCFREQIDSchema,
        'NVCF-PERCENT-COMPLETE': NVCFPERCENTCOMPLETESchema,
        'NVCF-STATUS': NVCFSTATUSSchema,
        'Location': LocationSchema,
    }
)


@dataclass
class ApiResponseFor302(api_client.ApiResponse):
    body: FunctionInvocationInvokeFunction302Response


@dataclass
class ApiResponseFor302Async(api_client.AsyncApiResponse):
    body: FunctionInvocationInvokeFunction302Response


_response_for_302 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor302,
    response_cls_async=ApiResponseFor302Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor302ResponseBodyApplicationJson),
    },
    headers=[
        nvcf_reqid_parameter,
        nvcf_percent_complete_parameter,
        nvcf_status_parameter,
        location_parameter,
    ]
)
SchemaFor402ResponseBodyApplicationJson = FunctionInvocationInvokeFunction402ResponseSchema


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    body: FunctionInvocationInvokeFunction402Response


@dataclass
class ApiResponseFor402Async(api_client.AsyncApiResponse):
    body: FunctionInvocationInvokeFunction402Response


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    response_cls_async=ApiResponseFor402Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor402ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = FunctionInvocationInvokeFunction403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: FunctionInvocationInvokeFunction403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: FunctionInvocationInvokeFunction403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
    'text/event-stream',
)


class BaseApi(api_client.Api):

    def _invoke_function_mapped_args(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        args.body = _body
        if nvcf_input_asset_references is not None:
            _header_params["NVCF-INPUT-ASSET-REFERENCES"] = nvcf_input_asset_references
        if nvcf_poll_seconds is not None:
            _header_params["NVCF-POLL-SECONDS"] = nvcf_poll_seconds
        if function_id is not None:
            _path_params["functionId"] = function_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _ainvoke_function_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Call Function
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_function_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_nvcf_input_asset_references,
            request_header_nvcf_poll_seconds,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
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
            path_template='/v2/nvcf/pexec/functions/{functionId}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
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


    def _invoke_function_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Call Function
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_function_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_nvcf_input_asset_references,
            request_header_nvcf_poll_seconds,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
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
            path_template='/v2/nvcf/pexec/functions/{functionId}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_body.serialize(body, content_type)
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class InvokeFunctionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ainvoke_function(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._invoke_function_mapped_args(
            function_id=function_id,
            nvcf_input_asset_references=nvcf_input_asset_references,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return await self._ainvoke_function_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def invoke_function(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._invoke_function_mapped_args(
            function_id=function_id,
            nvcf_input_asset_references=nvcf_input_asset_references,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return self._invoke_function_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class InvokeFunction(BaseApi):

    async def ainvoke_function(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> FunctionInvocationInvokeFunction200ResponsePydantic:
        raw_response = await self.raw.ainvoke_function(
            function_id=function_id,
            nvcf_input_asset_references=nvcf_input_asset_references,
            nvcf_poll_seconds=nvcf_poll_seconds,
            **kwargs,
        )
        if validate:
            return FunctionInvocationInvokeFunction200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FunctionInvocationInvokeFunction200ResponsePydantic, raw_response.body)
    
    
    def invoke_function(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
        validate: bool = False,
    ) -> FunctionInvocationInvokeFunction200ResponsePydantic:
        raw_response = self.raw.invoke_function(
            function_id=function_id,
            nvcf_input_asset_references=nvcf_input_asset_references,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        if validate:
            return FunctionInvocationInvokeFunction200ResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FunctionInvocationInvokeFunction200ResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._invoke_function_mapped_args(
            function_id=function_id,
            nvcf_input_asset_references=nvcf_input_asset_references,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return await self._ainvoke_function_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        function_id: str,
        nvcf_input_asset_references: typing.Optional[typing.List[str]] = None,
        nvcf_poll_seconds: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._invoke_function_mapped_args(
            function_id=function_id,
            nvcf_input_asset_references=nvcf_input_asset_references,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return self._invoke_function_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

