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


class FunctionInvocationPollForResultUsingFunctionInvocationRequest402Response(BaseModel):
    short: typing.Optional[int] = Field(None, alias='short')

    char: typing.Optional[str] = Field(None, alias='char')

    int_: typing.Optional[int] = Field(None, alias='int')

    long: typing.Optional[int] = Field(None, alias='long')

    float_: typing.Optional[typing.Union[int, float]] = Field(None, alias='float')

    double: typing.Optional[typing.Union[int, float]] = Field(None, alias='double')

    direct: typing.Optional[bool] = Field(None, alias='direct')

    read_only: typing.Optional[bool] = Field(None, alias='readOnly')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
