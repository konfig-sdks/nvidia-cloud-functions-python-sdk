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

from nvidia_cloud_functions_python_sdk.type.gpu_specification_dto_availability_zones import GpuSpecificationDtoAvailabilityZones

class RequiredGpuSpecificationDto(TypedDict):
    # GPU name from the cluster
    gpu: str

    # Backend/CSP where the GPU powered instance will be launched
    backend: str

    # Maximum number of spot instances for the deployment
    maxInstances: int

    # Minimum number of spot instances for the deployment
    minInstances: int

class OptionalGpuSpecificationDto(TypedDict, total=False):
    # Instance type, based on GPU, assigned to a Worker
    instanceType: str

    availabilityZones: GpuSpecificationDtoAvailabilityZones

    # Max request concurrency between 1 (default) and 1024.
    maxRequestConcurrency: int

    configuration: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class GpuSpecificationDto(RequiredGpuSpecificationDto, OptionalGpuSpecificationDto):
    pass
