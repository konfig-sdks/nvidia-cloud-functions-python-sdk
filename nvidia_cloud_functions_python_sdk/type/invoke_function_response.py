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


class RequiredInvokeFunctionResponse(TypedDict):
    pass

class OptionalInvokeFunctionResponse(TypedDict, total=False):
    # Request id
    reqId: str

    # Status of the task/job executing cloud function.
    status: str

    # For large results, responseReference will be a pre-signeddownload URL.
    responseReference: str

    # Progress indicator for the task/job executing cloud function.
    percentComplete: int

    # Error code from the container while executing cloud function.
    errorCode: int

    # Response/result of size < 5MB size for the task/job executing cloud function.
    response: str

class InvokeFunctionResponse(RequiredInvokeFunctionResponse, OptionalInvokeFunctionResponse):
    pass
