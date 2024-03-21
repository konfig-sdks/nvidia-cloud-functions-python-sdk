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

from nvidia_cloud_functions_python_sdk.model.function_invocation_poll_for_result_using_function_invocation_request402_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest402Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest402ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_poll_for_result_using_function_invocation_request403_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest403Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest403ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_poll_for_result_using_function_invocation_request302_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest302Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest302ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_poll_for_result_using_function_invocation_request202_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest202Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest202ResponseSchema
from nvidia_cloud_functions_python_sdk.model.function_invocation_poll_for_result_using_function_invocation_request_response import FunctionInvocationPollForResultUsingFunctionInvocationRequestResponse as FunctionInvocationPollForResultUsingFunctionInvocationRequestResponseSchema

from nvidia_cloud_functions_python_sdk.type.function_invocation_poll_for_result_using_function_invocation_request403_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest403Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_poll_for_result_using_function_invocation_request302_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest302Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_poll_for_result_using_function_invocation_request202_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest202Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_poll_for_result_using_function_invocation_request402_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest402Response
from nvidia_cloud_functions_python_sdk.type.function_invocation_poll_for_result_using_function_invocation_request_response import FunctionInvocationPollForResultUsingFunctionInvocationRequestResponse

from ...api_client import Dictionary
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_poll_for_result_using_function_invocation_request_response import FunctionInvocationPollForResultUsingFunctionInvocationRequestResponse as FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_poll_for_result_using_function_invocation_request202_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest202Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest202ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_poll_for_result_using_function_invocation_request403_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest403Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest403ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_poll_for_result_using_function_invocation_request402_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest402Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest402ResponsePydantic
from nvidia_cloud_functions_python_sdk.pydantic.function_invocation_poll_for_result_using_function_invocation_request302_response import FunctionInvocationPollForResultUsingFunctionInvocationRequest302Response as FunctionInvocationPollForResultUsingFunctionInvocationRequest302ResponsePydantic

from . import path

# Header params


class NVCFPOLLSECONDSSchema(
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        inclusive_maximum = 300
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'NVCF-POLL-SECONDS': typing.Union[NVCFPOLLSECONDSSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_nvcf_poll_seconds = api_client.HeaderParameter(
    name="NVCF-POLL-SECONDS",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFPOLLSECONDSSchema,
)
# Path params
RequestIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'requestId': typing.Union[RequestIdSchema, str, uuid.UUID, ],
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


request_path_request_id = api_client.PathParameter(
    name="requestId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RequestIdSchema,
    required=True,
)
NVCFREQIDSchema = schemas.StrSchema
nvcf_reqid_parameter = api_client.HeaderParameter(
    name="NVCF-REQID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFREQIDSchema,
)
NVCFPERCENTCOMPLETESchema = schemas.StrSchema
nvcf_percent_complete_parameter = api_client.HeaderParameter(
    name="NVCF-PERCENT-COMPLETE",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFPERCENTCOMPLETESchema,
)
NVCFSTATUSSchema = schemas.StrSchema
nvcf_status_parameter = api_client.HeaderParameter(
    name="NVCF-STATUS",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFSTATUSSchema,
)
SchemaFor200ResponseBodyApplicationJson = FunctionInvocationPollForResultUsingFunctionInvocationRequestResponseSchema
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
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequestResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequestResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        nvcf_reqid_parameter,
        nvcf_percent_complete_parameter,
        nvcf_status_parameter,
    ]
)
NVCFREQIDSchema = schemas.StrSchema
nvcf_reqid_parameter = api_client.HeaderParameter(
    name="NVCF-REQID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFREQIDSchema,
)
NVCFPERCENTCOMPLETESchema = schemas.StrSchema
nvcf_percent_complete_parameter = api_client.HeaderParameter(
    name="NVCF-PERCENT-COMPLETE",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFPERCENTCOMPLETESchema,
)
NVCFSTATUSSchema = schemas.StrSchema
nvcf_status_parameter = api_client.HeaderParameter(
    name="NVCF-STATUS",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFSTATUSSchema,
)
SchemaFor202ResponseBodyApplicationJson = FunctionInvocationPollForResultUsingFunctionInvocationRequest202ResponseSchema
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
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest202Response


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest202Response


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
nvcf_reqid_parameter = api_client.HeaderParameter(
    name="NVCF-REQID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFREQIDSchema,
)
NVCFPERCENTCOMPLETESchema = schemas.StrSchema
nvcf_percent_complete_parameter = api_client.HeaderParameter(
    name="NVCF-PERCENT-COMPLETE",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFPERCENTCOMPLETESchema,
)
NVCFSTATUSSchema = schemas.StrSchema
nvcf_status_parameter = api_client.HeaderParameter(
    name="NVCF-STATUS",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NVCFSTATUSSchema,
)
LocationSchema = schemas.StrSchema
location_parameter = api_client.HeaderParameter(
    name="Location",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LocationSchema,
)
SchemaFor302ResponseBodyApplicationJson = FunctionInvocationPollForResultUsingFunctionInvocationRequest302ResponseSchema
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
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest302Response


@dataclass
class ApiResponseFor302Async(api_client.AsyncApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest302Response


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
SchemaFor402ResponseBodyApplicationJson = FunctionInvocationPollForResultUsingFunctionInvocationRequest402ResponseSchema


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest402Response


@dataclass
class ApiResponseFor402Async(api_client.AsyncApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest402Response


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    response_cls_async=ApiResponseFor402Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor402ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = FunctionInvocationPollForResultUsingFunctionInvocationRequest403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: FunctionInvocationPollForResultUsingFunctionInvocationRequest403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '202': _response_for_202,
    '302': _response_for_302,
    '402': _response_for_402,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _poll_for_result_using_function_invocation_request_mapped_args(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        if nvcf_poll_seconds is not None:
            _header_params["NVCF-POLL-SECONDS"] = nvcf_poll_seconds
        if request_id is not None:
            _path_params["requestId"] = request_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _apoll_for_result_using_function_invocation_request_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Poll For Result Using Function Invocation Request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_request_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/nvcf/pexec/status/{requestId}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _poll_for_result_using_function_invocation_request_oapg(
        self,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Poll For Result Using Function Invocation Request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_request_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/nvcf/pexec/status/{requestId}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class PollForResultUsingFunctionInvocationRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apoll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return await self._apoll_for_result_using_function_invocation_request_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def poll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return self._poll_for_result_using_function_invocation_request_oapg(
            header_params=args.header,
            path_params=args.path,
        )

class PollForResultUsingFunctionInvocationRequest(BaseApi):

    async def apoll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic:
        raw_response = await self.raw.apoll_for_result_using_function_invocation_request(
            request_id=request_id,
            nvcf_poll_seconds=nvcf_poll_seconds,
            **kwargs,
        )
        if validate:
            return FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic, raw_response.body)
    
    
    def poll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
        validate: bool = False,
    ) -> FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic:
        raw_response = self.raw.poll_for_result_using_function_invocation_request(
            request_id=request_id,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        if validate:
            return FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FunctionInvocationPollForResultUsingFunctionInvocationRequestResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return await self._apoll_for_result_using_function_invocation_request_oapg(
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        request_id: str,
        nvcf_poll_seconds: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
            nvcf_poll_seconds=nvcf_poll_seconds,
        )
        return self._poll_for_result_using_function_invocation_request_oapg(
            header_params=args.header,
            path_params=args.path,
        )

