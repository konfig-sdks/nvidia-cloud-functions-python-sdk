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


class InstanceDto(BaseModel):
    # Unique id of the instance
    instance_id: typing.Optional[str] = Field(None, alias='instanceId')

    # Function executing on the instance
    function_id: typing.Optional[str] = Field(None, alias='functionId')

    # Function version executing on the instance
    function_version_id: typing.Optional[str] = Field(None, alias='functionVersionId')

    # GPU instance-type powering the instance
    instance_type: typing.Optional[str] = Field(None, alias='instanceType')

    # Instance status
    instance_status: typing.Optional[Literal["ACTIVE", "ERRORED", "PREEMPTED", "DELETED"]] = Field(None, alias='instanceStatus')

    # SIS request-id used to launch this instance
    sis_request_id: typing.Optional[str] = Field(None, alias='sisRequestId')

    # NVIDIA Cloud Account Id that owns the function running on the instance
    nca_id: typing.Optional[str] = Field(None, alias='ncaId')

    # GPU name powering the instance
    gpu: typing.Optional[str] = Field(None, alias='gpu')

    # Backend where the instance is running
    backend: typing.Optional[str] = Field(None, alias='backend')

    # Location such as zone name or region where the instance is running
    location: typing.Optional[str] = Field(None, alias='location')

    # Instance creation timestamp
    instance_created_at: typing.Optional[datetime] = Field(None, alias='instanceCreatedAt')

    # Instance's last updated timestamp
    instance_updated_at: typing.Optional[datetime] = Field(None, alias='instanceUpdatedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
