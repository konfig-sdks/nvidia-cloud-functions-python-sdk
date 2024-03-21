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

from nvidia_cloud_functions_python_sdk.pydantic.cluster import Cluster
from nvidia_cloud_functions_python_sdk.pydantic.cluster_group_authorized_nca_ids import ClusterGroupAuthorizedNcaIds
from nvidia_cloud_functions_python_sdk.pydantic.gpu import Gpu

class ClusterGroup(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    nca_id: typing.Optional[str] = Field(None, alias='ncaId')

    authorized_nca_ids: typing.Optional[ClusterGroupAuthorizedNcaIds] = Field(None, alias='authorizedNcaIds')

    gpus: typing.Optional[typing.List[Gpu]] = Field(None, alias='gpus')

    clusters: typing.Optional[typing.List[Cluster]] = Field(None, alias='clusters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
