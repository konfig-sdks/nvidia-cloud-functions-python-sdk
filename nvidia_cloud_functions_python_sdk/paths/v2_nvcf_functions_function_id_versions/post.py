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

from nvidia_cloud_functions_python_sdk.model.artifact_dto import ArtifactDto as ArtifactDtoSchema
from nvidia_cloud_functions_python_sdk.model.container_environment_entry_dto import ContainerEnvironmentEntryDto as ContainerEnvironmentEntryDtoSchema
from nvidia_cloud_functions_python_sdk.model.create_function_response import CreateFunctionResponse as CreateFunctionResponseSchema
from nvidia_cloud_functions_python_sdk.model.create_function_request import CreateFunctionRequest as CreateFunctionRequestSchema

from nvidia_cloud_functions_python_sdk.type.artifact_dto import ArtifactDto
from nvidia_cloud_functions_python_sdk.type.create_function_response import CreateFunctionResponse
from nvidia_cloud_functions_python_sdk.type.create_function_request import CreateFunctionRequest
from nvidia_cloud_functions_python_sdk.type.container_environment_entry_dto import ContainerEnvironmentEntryDto

from ...api_client import Dictionary
from nvidia_cloud_functions_python_sdk.pydantic.artifact_dto import ArtifactDto as ArtifactDtoPydantic
from nvidia_cloud_functions_python_sdk.pydantic.create_function_request import CreateFunctionRequest as CreateFunctionRequestPydantic
from nvidia_cloud_functions_python_sdk.pydantic.container_environment_entry_dto import ContainerEnvironmentEntryDto as ContainerEnvironmentEntryDtoPydantic
from nvidia_cloud_functions_python_sdk.pydantic.create_function_response import CreateFunctionResponse as CreateFunctionResponsePydantic

from . import path

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
SchemaForRequestBodyApplicationJson = CreateFunctionRequestSchema


request_body_create_function_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = CreateFunctionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CreateFunctionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CreateFunctionResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_function_version_mapped_args(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if inference_url is not None:
            _body["inferenceUrl"] = inference_url
        if health_uri is not None:
            _body["healthUri"] = health_uri
        if inference_port is not None:
            _body["inferencePort"] = inference_port
        if container_args is not None:
            _body["containerArgs"] = container_args
        if container_environment is not None:
            _body["containerEnvironment"] = container_environment
        if models is not None:
            _body["models"] = models
        if container_image is not None:
            _body["containerImage"] = container_image
        if helm_chart is not None:
            _body["helmChart"] = helm_chart
        if helm_chart_service_name is not None:
            _body["helmChartServiceName"] = helm_chart_service_name
        if resources is not None:
            _body["resources"] = resources
        if api_body_format is not None:
            _body["apiBodyFormat"] = api_body_format
        args.body = _body
        if function_id is not None:
            _path_params["functionId"] = function_id
        args.path = _path_params
        return args

    async def _acreate_function_version_oapg(
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
        Create Function Version
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/v2/nvcf/functions/{functionId}/versions',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_create_function_request.serialize(body, content_type)
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


    def _create_function_version_oapg(
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
        Create Function Version
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/v2/nvcf/functions/{functionId}/versions',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_create_function_request.serialize(body, content_type)
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


class CreateFunctionVersionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_function_version(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_function_version_mapped_args(
            name=name,
            inference_url=inference_url,
            function_id=function_id,
            health_uri=health_uri,
            inference_port=inference_port,
            container_args=container_args,
            container_environment=container_environment,
            models=models,
            container_image=container_image,
            helm_chart=helm_chart,
            helm_chart_service_name=helm_chart_service_name,
            resources=resources,
            api_body_format=api_body_format,
        )
        return await self._acreate_function_version_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_function_version(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_function_version_mapped_args(
            name=name,
            inference_url=inference_url,
            function_id=function_id,
            health_uri=health_uri,
            inference_port=inference_port,
            container_args=container_args,
            container_environment=container_environment,
            models=models,
            container_image=container_image,
            helm_chart=helm_chart,
            helm_chart_service_name=helm_chart_service_name,
            resources=resources,
            api_body_format=api_body_format,
        )
        return self._create_function_version_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateFunctionVersion(BaseApi):

    async def acreate_function_version(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CreateFunctionResponsePydantic:
        raw_response = await self.raw.acreate_function_version(
            name=name,
            inference_url=inference_url,
            function_id=function_id,
            health_uri=health_uri,
            inference_port=inference_port,
            container_args=container_args,
            container_environment=container_environment,
            models=models,
            container_image=container_image,
            helm_chart=helm_chart,
            helm_chart_service_name=helm_chart_service_name,
            resources=resources,
            api_body_format=api_body_format,
            **kwargs,
        )
        if validate:
            return CreateFunctionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateFunctionResponsePydantic, raw_response.body)
    
    
    def create_function_version(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CreateFunctionResponsePydantic:
        raw_response = self.raw.create_function_version(
            name=name,
            inference_url=inference_url,
            function_id=function_id,
            health_uri=health_uri,
            inference_port=inference_port,
            container_args=container_args,
            container_environment=container_environment,
            models=models,
            container_image=container_image,
            helm_chart=helm_chart,
            helm_chart_service_name=helm_chart_service_name,
            resources=resources,
            api_body_format=api_body_format,
        )
        if validate:
            return CreateFunctionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CreateFunctionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_function_version_mapped_args(
            name=name,
            inference_url=inference_url,
            function_id=function_id,
            health_uri=health_uri,
            inference_port=inference_port,
            container_args=container_args,
            container_environment=container_environment,
            models=models,
            container_image=container_image,
            helm_chart=helm_chart,
            helm_chart_service_name=helm_chart_service_name,
            resources=resources,
            api_body_format=api_body_format,
        )
        return await self._acreate_function_version_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        inference_url: str,
        function_id: str,
        health_uri: typing.Optional[str] = None,
        inference_port: typing.Optional[int] = None,
        container_args: typing.Optional[str] = None,
        container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = None,
        models: typing.Optional[typing.List[ArtifactDto]] = None,
        container_image: typing.Optional[str] = None,
        helm_chart: typing.Optional[str] = None,
        helm_chart_service_name: typing.Optional[str] = None,
        resources: typing.Optional[typing.List[ArtifactDto]] = None,
        api_body_format: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_function_version_mapped_args(
            name=name,
            inference_url=inference_url,
            function_id=function_id,
            health_uri=health_uri,
            inference_port=inference_port,
            container_args=container_args,
            container_environment=container_environment,
            models=models,
            container_image=container_image,
            helm_chart=helm_chart,
            helm_chart_service_name=helm_chart_service_name,
            resources=resources,
            api_body_format=api_body_format,
        )
        return self._create_function_version_oapg(
            body=args.body,
            path_params=args.path,
        )

