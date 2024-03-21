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


class RequiredInstanceDto(TypedDict):
    pass

class OptionalInstanceDto(TypedDict, total=False):
    # Unique id of the instance
    instanceId: str

    # Function executing on the instance
    functionId: str

    # Function version executing on the instance
    functionVersionId: str

    # GPU instance-type powering the instance
    instanceType: str

    # Instance status
    instanceStatus: str

    # SIS request-id used to launch this instance
    sisRequestId: str

    # NVIDIA Cloud Account Id that owns the function running on the instance
    ncaId: str

    # GPU name powering the instance
    gpu: str

    # Backend where the instance is running
    backend: str

    # Location such as zone name or region where the instance is running
    location: str

    # Instance creation timestamp
    instanceCreatedAt: datetime

    # Instance's last updated timestamp
    instanceUpdatedAt: datetime

class InstanceDto(RequiredInstanceDto, OptionalInstanceDto):
    pass
