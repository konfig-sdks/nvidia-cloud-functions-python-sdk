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


class DeploymentHealthDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Data Transfer Object(DTO) representing deployment error
    """


    class MetaOapg:
        required = {
            "backend",
            "error",
            "gpu",
        }
        
        class properties:
            gpu = schemas.StrSchema
            backend = schemas.StrSchema
            error = schemas.StrSchema
            sisRequestId = schemas.UUIDSchema
            instanceType = schemas.StrSchema
            __annotations__ = {
                "gpu": gpu,
                "backend": backend,
                "error": error,
                "sisRequestId": sisRequestId,
                "instanceType": instanceType,
            }
    
    backend: MetaOapg.properties.backend
    error: MetaOapg.properties.error
    gpu: MetaOapg.properties.gpu
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpu"]) -> MetaOapg.properties.gpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backend"]) -> MetaOapg.properties.backend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sisRequestId"]) -> MetaOapg.properties.sisRequestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceType"]) -> MetaOapg.properties.instanceType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gpu", "backend", "error", "sisRequestId", "instanceType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpu"]) -> MetaOapg.properties.gpu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backend"]) -> MetaOapg.properties.backend: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sisRequestId"]) -> typing.Union[MetaOapg.properties.sisRequestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceType"]) -> typing.Union[MetaOapg.properties.instanceType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gpu", "backend", "error", "sisRequestId", "instanceType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        backend: typing.Union[MetaOapg.properties.backend, str, ],
        error: typing.Union[MetaOapg.properties.error, str, ],
        gpu: typing.Union[MetaOapg.properties.gpu, str, ],
        sisRequestId: typing.Union[MetaOapg.properties.sisRequestId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        instanceType: typing.Union[MetaOapg.properties.instanceType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeploymentHealthDto':
        return super().__new__(
            cls,
            *args,
            backend=backend,
            error=error,
            gpu=gpu,
            sisRequestId=sisRequestId,
            instanceType=instanceType,
            _configuration=_configuration,
            **kwargs,
        )
