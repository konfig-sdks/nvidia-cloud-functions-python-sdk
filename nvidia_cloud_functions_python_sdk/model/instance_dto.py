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


class InstanceDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Data Transfer Object(DTO) representing a spot instance
    """


    class MetaOapg:
        
        class properties:
            instanceId = schemas.StrSchema
            functionId = schemas.UUIDSchema
            functionVersionId = schemas.UUIDSchema
            instanceType = schemas.StrSchema
            
            
            class instanceStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTIVE": "ACTIVE",
                        "ERRORED": "ERRORED",
                        "PREEMPTED": "PREEMPTED",
                        "DELETED": "DELETED",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def ERRORED(cls):
                    return cls("ERRORED")
                
                @schemas.classproperty
                def PREEMPTED(cls):
                    return cls("PREEMPTED")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
            sisRequestId = schemas.UUIDSchema
            ncaId = schemas.StrSchema
            gpu = schemas.StrSchema
            backend = schemas.StrSchema
            location = schemas.StrSchema
            instanceCreatedAt = schemas.DateTimeSchema
            instanceUpdatedAt = schemas.DateTimeSchema
            __annotations__ = {
                "instanceId": instanceId,
                "functionId": functionId,
                "functionVersionId": functionVersionId,
                "instanceType": instanceType,
                "instanceStatus": instanceStatus,
                "sisRequestId": sisRequestId,
                "ncaId": ncaId,
                "gpu": gpu,
                "backend": backend,
                "location": location,
                "instanceCreatedAt": instanceCreatedAt,
                "instanceUpdatedAt": instanceUpdatedAt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceId"]) -> MetaOapg.properties.instanceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionId"]) -> MetaOapg.properties.functionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionVersionId"]) -> MetaOapg.properties.functionVersionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceType"]) -> MetaOapg.properties.instanceType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceStatus"]) -> MetaOapg.properties.instanceStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sisRequestId"]) -> MetaOapg.properties.sisRequestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ncaId"]) -> MetaOapg.properties.ncaId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gpu"]) -> MetaOapg.properties.gpu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backend"]) -> MetaOapg.properties.backend: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceCreatedAt"]) -> MetaOapg.properties.instanceCreatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceUpdatedAt"]) -> MetaOapg.properties.instanceUpdatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["instanceId", "functionId", "functionVersionId", "instanceType", "instanceStatus", "sisRequestId", "ncaId", "gpu", "backend", "location", "instanceCreatedAt", "instanceUpdatedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceId"]) -> typing.Union[MetaOapg.properties.instanceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionId"]) -> typing.Union[MetaOapg.properties.functionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionVersionId"]) -> typing.Union[MetaOapg.properties.functionVersionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceType"]) -> typing.Union[MetaOapg.properties.instanceType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceStatus"]) -> typing.Union[MetaOapg.properties.instanceStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sisRequestId"]) -> typing.Union[MetaOapg.properties.sisRequestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ncaId"]) -> typing.Union[MetaOapg.properties.ncaId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gpu"]) -> typing.Union[MetaOapg.properties.gpu, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backend"]) -> typing.Union[MetaOapg.properties.backend, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceCreatedAt"]) -> typing.Union[MetaOapg.properties.instanceCreatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceUpdatedAt"]) -> typing.Union[MetaOapg.properties.instanceUpdatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["instanceId", "functionId", "functionVersionId", "instanceType", "instanceStatus", "sisRequestId", "ncaId", "gpu", "backend", "location", "instanceCreatedAt", "instanceUpdatedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        instanceId: typing.Union[MetaOapg.properties.instanceId, str, schemas.Unset] = schemas.unset,
        functionId: typing.Union[MetaOapg.properties.functionId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        functionVersionId: typing.Union[MetaOapg.properties.functionVersionId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        instanceType: typing.Union[MetaOapg.properties.instanceType, str, schemas.Unset] = schemas.unset,
        instanceStatus: typing.Union[MetaOapg.properties.instanceStatus, str, schemas.Unset] = schemas.unset,
        sisRequestId: typing.Union[MetaOapg.properties.sisRequestId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        ncaId: typing.Union[MetaOapg.properties.ncaId, str, schemas.Unset] = schemas.unset,
        gpu: typing.Union[MetaOapg.properties.gpu, str, schemas.Unset] = schemas.unset,
        backend: typing.Union[MetaOapg.properties.backend, str, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, str, schemas.Unset] = schemas.unset,
        instanceCreatedAt: typing.Union[MetaOapg.properties.instanceCreatedAt, str, datetime, schemas.Unset] = schemas.unset,
        instanceUpdatedAt: typing.Union[MetaOapg.properties.instanceUpdatedAt, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstanceDto':
        return super().__new__(
            cls,
            *args,
            instanceId=instanceId,
            functionId=functionId,
            functionVersionId=functionVersionId,
            instanceType=instanceType,
            instanceStatus=instanceStatus,
            sisRequestId=sisRequestId,
            ncaId=ncaId,
            gpu=gpu,
            backend=backend,
            location=location,
            instanceCreatedAt=instanceCreatedAt,
            instanceUpdatedAt=instanceUpdatedAt,
            _configuration=_configuration,
            **kwargs,
        )
