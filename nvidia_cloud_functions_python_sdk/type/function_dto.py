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

from nvidia_cloud_functions_python_sdk.type.artifact_dto import ArtifactDto
from nvidia_cloud_functions_python_sdk.type.container_environment_entry_dto import ContainerEnvironmentEntryDto
from nvidia_cloud_functions_python_sdk.type.instance_dto import InstanceDto

class RequiredFunctionDto(TypedDict):
    # Unique function id
    id: str

    # NVIDIA Cloud Account Id
    ncaId: str

    # Unique function version id
    versionId: str

    # Function name
    name: str

    # Function status
    status: str

    # Health endpoint for the container or helmChart
    healthUri: str

    # Function creation timestamp
    createdAt: datetime

class OptionalFunctionDto(TypedDict, total=False):
    # Entrypoint for invoking the container to process requests
    inferenceUrl: str

    # Indicates whether the function is owned by another account. If the account  that is being used to lookup functions happens to be authorized to invoke/list  this function which is owned by a different account, then this field is set  to true and ncaId will contain the id of the account that owns the function.  Otherwise, this field is not set as it defaults to false. 
    ownedByDifferentAccount: bool

    # Optional port number where the inference listener is running - defaults to 8000 for Triton
    inferencePort: int

    # Args used to launch the container
    containerArgs: str

    # Environment settings used to launch the container
    containerEnvironment: typing.List[ContainerEnvironmentEntryDto]

    # Optional set of models
    models: typing.List[ArtifactDto]

    # Optional custom container
    containerImage: str

    # Invocation request body format
    apiBodyFormat: str

    # Optional Helm Chart
    helmChart: str

    # Helm Chart Service Name specified only when helmChart property is specified 
    helmChartServiceName: str

    # List of active instances for this function.
    activeInstances: typing.List[InstanceDto]

    # Optional set of resources.
    resources: typing.List[ArtifactDto]

class FunctionDto(RequiredFunctionDto, OptionalFunctionDto):
    pass
