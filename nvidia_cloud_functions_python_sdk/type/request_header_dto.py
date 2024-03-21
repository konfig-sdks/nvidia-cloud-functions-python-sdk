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

from nvidia_cloud_functions_python_sdk.type.metering_data_entry_dto import MeteringDataEntryDto
from nvidia_cloud_functions_python_sdk.type.request_header_dto_input_asset_references import RequestHeaderDtoInputAssetReferences

class RequiredRequestHeaderDto(TypedDict):
    pass

class OptionalRequestHeaderDto(TypedDict, total=False):
    inputAssetReferences: RequestHeaderDtoInputAssetReferences

    # Metadata used for billing/metering purposes.
    meteringData: typing.List[MeteringDataEntryDto]

    # Polling timeout duration.
    pollDurationSeconds: int

class RequestHeaderDto(RequiredRequestHeaderDto, OptionalRequestHeaderDto):
    pass
