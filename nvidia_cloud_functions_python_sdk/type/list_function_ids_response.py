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

from nvidia_cloud_functions_python_sdk.type.list_function_ids_response_function_ids import ListFunctionIdsResponseFunctionIds

class RequiredListFunctionIdsResponse(TypedDict):
    functionIds: ListFunctionIdsResponseFunctionIds

class OptionalListFunctionIdsResponse(TypedDict, total=False):
    pass

class ListFunctionIdsResponse(RequiredListFunctionIdsResponse, OptionalListFunctionIdsResponse):
    pass
