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


class FunctionDeploymentDto(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Function deployment response
    """


    class MetaOapg:
        required = {
            "functionId",
            "requestQueueUrl",
            "functionVersionId",
            "functionStatus",
            "ncaId",
            "deploymentSpecifications",
        }
        
        class properties:
            functionId = schemas.UUIDSchema
            functionVersionId = schemas.UUIDSchema
            ncaId = schemas.StrSchema
            
            
            class functionStatus(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTIVE": "ACTIVE",
                        "DEPLOYING": "DEPLOYING",
                        "ERROR": "ERROR",
                        "INACTIVE": "INACTIVE",
                        "DELETED": "DELETED",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def DEPLOYING(cls):
                    return cls("DEPLOYING")
                
                @schemas.classproperty
                def ERROR(cls):
                    return cls("ERROR")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
            requestQueueUrl = schemas.StrSchema
            
            
            class deploymentSpecifications(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GpuSpecificationDto']:
                        return GpuSpecificationDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GpuSpecificationDto'], typing.List['GpuSpecificationDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deploymentSpecifications':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GpuSpecificationDto':
                    return super().__getitem__(i)
            
            
            class healthInfo(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DeploymentHealthDto']:
                        return DeploymentHealthDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DeploymentHealthDto'], typing.List['DeploymentHealthDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'healthInfo':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DeploymentHealthDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "functionId": functionId,
                "functionVersionId": functionVersionId,
                "ncaId": ncaId,
                "functionStatus": functionStatus,
                "requestQueueUrl": requestQueueUrl,
                "deploymentSpecifications": deploymentSpecifications,
                "healthInfo": healthInfo,
            }
    
    functionId: MetaOapg.properties.functionId
    requestQueueUrl: MetaOapg.properties.requestQueueUrl
    functionVersionId: MetaOapg.properties.functionVersionId
    functionStatus: MetaOapg.properties.functionStatus
    ncaId: MetaOapg.properties.ncaId
    deploymentSpecifications: MetaOapg.properties.deploymentSpecifications
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionId"]) -> MetaOapg.properties.functionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionVersionId"]) -> MetaOapg.properties.functionVersionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ncaId"]) -> MetaOapg.properties.ncaId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionStatus"]) -> MetaOapg.properties.functionStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestQueueUrl"]) -> MetaOapg.properties.requestQueueUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deploymentSpecifications"]) -> MetaOapg.properties.deploymentSpecifications: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["healthInfo"]) -> MetaOapg.properties.healthInfo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["functionId", "functionVersionId", "ncaId", "functionStatus", "requestQueueUrl", "deploymentSpecifications", "healthInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionId"]) -> MetaOapg.properties.functionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionVersionId"]) -> MetaOapg.properties.functionVersionId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ncaId"]) -> MetaOapg.properties.ncaId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionStatus"]) -> MetaOapg.properties.functionStatus: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestQueueUrl"]) -> MetaOapg.properties.requestQueueUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deploymentSpecifications"]) -> MetaOapg.properties.deploymentSpecifications: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["healthInfo"]) -> typing.Union[MetaOapg.properties.healthInfo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["functionId", "functionVersionId", "ncaId", "functionStatus", "requestQueueUrl", "deploymentSpecifications", "healthInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        functionId: typing.Union[MetaOapg.properties.functionId, str, uuid.UUID, ],
        requestQueueUrl: typing.Union[MetaOapg.properties.requestQueueUrl, str, ],
        functionVersionId: typing.Union[MetaOapg.properties.functionVersionId, str, uuid.UUID, ],
        functionStatus: typing.Union[MetaOapg.properties.functionStatus, str, ],
        ncaId: typing.Union[MetaOapg.properties.ncaId, str, ],
        deploymentSpecifications: typing.Union[MetaOapg.properties.deploymentSpecifications, list, tuple, ],
        healthInfo: typing.Union[MetaOapg.properties.healthInfo, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FunctionDeploymentDto':
        return super().__new__(
            cls,
            *args,
            functionId=functionId,
            requestQueueUrl=requestQueueUrl,
            functionVersionId=functionVersionId,
            functionStatus=functionStatus,
            ncaId=ncaId,
            deploymentSpecifications=deploymentSpecifications,
            healthInfo=healthInfo,
            _configuration=_configuration,
            **kwargs,
        )

from nvidia_cloud_functions_python_sdk.model.deployment_health_dto import DeploymentHealthDto
from nvidia_cloud_functions_python_sdk.model.gpu_specification_dto import GpuSpecificationDto
