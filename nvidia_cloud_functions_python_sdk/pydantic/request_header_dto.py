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

from nvidia_cloud_functions_python_sdk.pydantic.metering_data_entry_dto import MeteringDataEntryDto
from nvidia_cloud_functions_python_sdk.pydantic.request_header_dto_input_asset_references import RequestHeaderDtoInputAssetReferences

class RequestHeaderDto(BaseModel):
    input_asset_references: typing.Optional[RequestHeaderDtoInputAssetReferences] = Field(None, alias='inputAssetReferences')

    # Metadata used for billing/metering purposes.
    metering_data: typing.Optional[typing.List[MeteringDataEntryDto]] = Field(None, alias='meteringData')

    # Polling timeout duration.
    poll_duration_seconds: typing.Optional[int] = Field(None, alias='pollDurationSeconds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
