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

from nvidia_cloud_functions_python_sdk.model.function_deployment_request import FunctionDeploymentRequest as FunctionDeploymentRequestSchema
from nvidia_cloud_functions_python_sdk.model.gpu_specification_dto import GpuSpecificationDto as GpuSpecificationDtoSchema
from nvidia_cloud_functions_python_sdk.model.deployment_response import DeploymentResponse as DeploymentResponseSchema

from nvidia_cloud_functions_python_sdk.type.function_deployment_request import FunctionDeploymentRequest
from nvidia_cloud_functions_python_sdk.type.gpu_specification_dto import GpuSpecificationDto
from nvidia_cloud_functions_python_sdk.type.deployment_response import DeploymentResponse

from ...api_client import Dictionary
from nvidia_cloud_functions_python_sdk.pydantic.function_deployment_request import FunctionDeploymentRequest as FunctionDeploymentRequestPydantic
from nvidia_cloud_functions_python_sdk.pydantic.gpu_specification_dto import GpuSpecificationDto as GpuSpecificationDtoPydantic
from nvidia_cloud_functions_python_sdk.pydantic.deployment_response import DeploymentResponse as DeploymentResponsePydantic

# Path params
FunctionIdSchema = schemas.UUIDSchema
FunctionVersionIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'functionId': typing.Union[FunctionIdSchema, str, uuid.UUID, ],
        'functionVersionId': typing.Union[FunctionVersionIdSchema, str, uuid.UUID, ],
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
request_path_function_version_id = api_client.PathParameter(
    name="functionVersionId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FunctionVersionIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = FunctionDeploymentRequestSchema


request_body_function_deployment_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = DeploymentResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DeploymentResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DeploymentResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _initiate_deployment_for_version_mapped_args(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if deployment_specifications is not None:
            _body["deploymentSpecifications"] = deployment_specifications
        args.body = _body
        if function_id is not None:
            _path_params["functionId"] = function_id
        if function_version_id is not None:
            _path_params["functionVersionId"] = function_version_id
        args.path = _path_params
        return args

    async def _ainitiate_deployment_for_version_oapg(
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
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Deploy Function
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_function_id,
            request_path_function_version_id,
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
            path_template='/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_function_deployment_request.serialize(body, content_type)
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


    def _initiate_deployment_for_version_oapg(
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
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Deploy Function
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_function_id,
            request_path_function_version_id,
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
            path_template='/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_function_deployment_request.serialize(body, content_type)
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


class InitiateDeploymentForVersionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ainitiate_deployment_for_version(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_deployment_for_version_mapped_args(
            deployment_specifications=deployment_specifications,
            function_id=function_id,
            function_version_id=function_version_id,
        )
        return await self._ainitiate_deployment_for_version_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def initiate_deployment_for_version(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_deployment_for_version_mapped_args(
            deployment_specifications=deployment_specifications,
            function_id=function_id,
            function_version_id=function_version_id,
        )
        return self._initiate_deployment_for_version_oapg(
            body=args.body,
            path_params=args.path,
        )

class InitiateDeploymentForVersion(BaseApi):

    async def ainitiate_deployment_for_version(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        validate: bool = False,
        **kwargs,
    ) -> DeploymentResponsePydantic:
        raw_response = await self.raw.ainitiate_deployment_for_version(
            deployment_specifications=deployment_specifications,
            function_id=function_id,
            function_version_id=function_version_id,
            **kwargs,
        )
        if validate:
            return DeploymentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DeploymentResponsePydantic, raw_response.body)
    
    
    def initiate_deployment_for_version(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        validate: bool = False,
    ) -> DeploymentResponsePydantic:
        raw_response = self.raw.initiate_deployment_for_version(
            deployment_specifications=deployment_specifications,
            function_id=function_id,
            function_version_id=function_version_id,
        )
        if validate:
            return DeploymentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DeploymentResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initiate_deployment_for_version_mapped_args(
            deployment_specifications=deployment_specifications,
            function_id=function_id,
            function_version_id=function_version_id,
        )
        return await self._ainitiate_deployment_for_version_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        deployment_specifications: typing.List[GpuSpecificationDto],
        function_id: str,
        function_version_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initiate_deployment_for_version_mapped_args(
            deployment_specifications=deployment_specifications,
            function_id=function_id,
            function_version_id=function_version_id,
        )
        return self._initiate_deployment_for_version_oapg(
            body=args.body,
            path_params=args.path,
        )

