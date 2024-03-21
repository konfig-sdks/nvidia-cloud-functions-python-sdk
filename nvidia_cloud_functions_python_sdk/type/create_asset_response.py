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


class RequiredCreateAssetResponse(TypedDict):
    pass

class OptionalCreateAssetResponse(TypedDict, total=False):
    # Asset description to be used when uploading the asset
    description: str

    # Unique id of the asset to be uploaded to AWS S3 bucket
    assetId: str

    # Pre-signed upload URL to upload asset
    uploadUrl: str

    # Content type of the asset such image/png, image/jpeg, etc.
    contentType: str

class CreateAssetResponse(RequiredCreateAssetResponse, OptionalCreateAssetResponse):
    pass
