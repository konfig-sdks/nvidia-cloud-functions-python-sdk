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

from nvidia_cloud_functions_python_sdk.pydantic.deployment_health_dto import DeploymentHealthDto
from nvidia_cloud_functions_python_sdk.pydantic.gpu_specification_dto import GpuSpecificationDto

class FunctionDeploymentDto(BaseModel):
    # Function id
    function_id: str = Field(alias='functionId')

    # Function version id
    function_version_id: str = Field(alias='functionVersionId')

    # NVIDIA Cloud Account Id
    nca_id: str = Field(alias='ncaId')

    # Function status
    function_status: Literal["ACTIVE", "DEPLOYING", "ERROR", "INACTIVE", "DELETED"] = Field(alias='functionStatus')

    # SQS Request Queue URL
    request_queue_url: str = Field(alias='requestQueueUrl')

    # Function deployment details
    deployment_specifications: typing.List[GpuSpecificationDto] = Field(alias='deploymentSpecifications')

    # Health info for a deployment specification is included only if there are any  issues/errors. 
    health_info: typing.Optional[typing.List[DeploymentHealthDto]] = Field(None, alias='healthInfo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
