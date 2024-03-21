# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
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

from nvidia_cloud_functions_python_sdk import schemas  # noqa: F401


class InvokeFunctionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Request body for creating a job/task for inference/train using a GPU powered spot instance in cloud.
    """


    class MetaOapg:
        required = {
            "requestBody",
        }
        
        class properties:
            requestBody = schemas.DictSchema
        
            @staticmethod
            def requestHeader() -> typing.Type['RequestHeaderDto']:
                return RequestHeaderDto
            __annotations__ = {
                "requestBody": requestBody,
                "requestHeader": requestHeader,
            }
    
    requestBody: MetaOapg.properties.requestBody
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestBody"]) -> MetaOapg.properties.requestBody: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestHeader"]) -> 'RequestHeaderDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["requestBody", "requestHeader", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestBody"]) -> MetaOapg.properties.requestBody: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestHeader"]) -> typing.Union['RequestHeaderDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["requestBody", "requestHeader", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        requestBody: typing.Union[MetaOapg.properties.requestBody, dict, frozendict.frozendict, ],
        requestHeader: typing.Union['RequestHeaderDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvokeFunctionRequest':
        return super().__new__(
            cls,
            *args,
            requestBody=requestBody,
            requestHeader=requestHeader,
            _configuration=_configuration,
            **kwargs,
        )

from nvidia_cloud_functions_python_sdk.model.request_header_dto import RequestHeaderDto
