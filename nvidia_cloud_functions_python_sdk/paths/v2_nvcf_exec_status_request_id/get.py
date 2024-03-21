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

from nvidia_cloud_functions_python_sdk.model.invoke_function_response import InvokeFunctionResponse as InvokeFunctionResponseSchema

from nvidia_cloud_functions_python_sdk.type.invoke_function_response import InvokeFunctionResponse

from ...api_client import Dictionary
from nvidia_cloud_functions_python_sdk.pydantic.invoke_function_response import InvokeFunctionResponse as InvokeFunctionResponsePydantic

from . import path

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
SchemaFor200ResponseBodyApplicationJson = InvokeFunctionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: InvokeFunctionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: InvokeFunctionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor202ResponseBodyApplicationJson = InvokeFunctionResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: InvokeFunctionResponse


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: InvokeFunctionResponse


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
LocationSchema = schemas.StrSchema
location_parameter = api_client.HeaderParameter(
    name="Location",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LocationSchema,
)
SchemaFor302ResponseBodyApplicationJson = InvokeFunctionResponseSchema
ResponseHeadersFor302 = typing_extensions.TypedDict(
    'ResponseHeadersFor302',
    {
        'Location': LocationSchema,
    }
)


@dataclass
class ApiResponseFor302(api_client.ApiResponse):
    body: InvokeFunctionResponse


@dataclass
class ApiResponseFor302Async(api_client.AsyncApiResponse):
    body: InvokeFunctionResponse


_response_for_302 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor302,
    response_cls_async=ApiResponseFor302Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor302ResponseBodyApplicationJson),
    },
    headers=[
        location_parameter,
    ]
)
SchemaFor402ResponseBodyApplicationJson = InvokeFunctionResponseSchema


@dataclass
class ApiResponseFor402(api_client.ApiResponse):
    body: InvokeFunctionResponse


@dataclass
class ApiResponseFor402Async(api_client.AsyncApiResponse):
    body: InvokeFunctionResponse


_response_for_402 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor402,
    response_cls_async=ApiResponseFor402Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor402ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = InvokeFunctionResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: InvokeFunctionResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: InvokeFunctionResponse


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
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if request_id is not None:
            _path_params["requestId"] = request_id
        args.path = _path_params
        return args

    async def _apoll_for_result_using_function_invocation_request_oapg(
        self,
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
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/nvcf/exec/status/{requestId}',
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
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/nvcf/exec/status/{requestId}',
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

    @api_client.DeprecationWarningOnce(prefix="envelope_function_invocation")
    async def apoll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
        )
        return await self._apoll_for_result_using_function_invocation_request_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="envelope_function_invocation")
    def poll_for_result_using_function_invocation_request(
        self,
        request_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
        )
        return self._poll_for_result_using_function_invocation_request_oapg(
            path_params=args.path,
        )

class PollForResultUsingFunctionInvocationRequest(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="envelope_function_invocation")
    async def apoll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        validate: bool = False,
        **kwargs,
    ) -> InvokeFunctionResponsePydantic:
        raw_response = await self.raw.apoll_for_result_using_function_invocation_request(
            request_id=request_id,
            **kwargs,
        )
        if validate:
            return InvokeFunctionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(InvokeFunctionResponsePydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="envelope_function_invocation")
    def poll_for_result_using_function_invocation_request(
        self,
        request_id: str,
        validate: bool = False,
    ) -> InvokeFunctionResponsePydantic:
        raw_response = self.raw.poll_for_result_using_function_invocation_request(
            request_id=request_id,
        )
        if validate:
            return InvokeFunctionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(InvokeFunctionResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="envelope_function_invocation")
    async def aget(
        self,
        request_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
        )
        return await self._apoll_for_result_using_function_invocation_request_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="envelope_function_invocation")
    def get(
        self,
        request_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._poll_for_result_using_function_invocation_request_mapped_args(
            request_id=request_id,
        )
        return self._poll_for_result_using_function_invocation_request_oapg(
            path_params=args.path,
        )

