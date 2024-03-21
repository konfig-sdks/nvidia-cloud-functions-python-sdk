# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from nvidia_cloud_functions_python_sdk.pydantic.gpu_specification_dto_availability_zones import GpuSpecificationDtoAvailabilityZones

class GpuSpecificationDto(BaseModel):
    # GPU name from the cluster
    gpu: str = Field(alias='gpu')

    # Backend/CSP where the GPU powered instance will be launched
    backend: str = Field(alias='backend')

    # Maximum number of spot instances for the deployment
    max_instances: int = Field(alias='maxInstances')

    # Minimum number of spot instances for the deployment
    min_instances: int = Field(alias='minInstances')

    # Instance type, based on GPU, assigned to a Worker
    instance_type: typing.Optional[str] = Field(None, alias='instanceType')

    availability_zones: typing.Optional[GpuSpecificationDtoAvailabilityZones] = Field(None, alias='availabilityZones')

    # Max request concurrency between 1 (default) and 1024.
    max_request_concurrency: typing.Optional[int] = Field(None, alias='maxRequestConcurrency')

    configuration: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='configuration')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
