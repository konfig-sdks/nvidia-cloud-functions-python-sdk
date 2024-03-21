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

from nvidia_cloud_functions_python_sdk.type.asset_dto import AssetDto

class RequiredListAssetsResponse(TypedDict):
    pass

class OptionalListAssetsResponse(TypedDict, total=False):
    # List of assets uploaded for the nca id
    assets: typing.List[AssetDto]

class ListAssetsResponse(RequiredListAssetsResponse, OptionalListAssetsResponse):
    pass
