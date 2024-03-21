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

class RequiredCreateFunctionRequest(TypedDict):
    # Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters
    name: str

    # Entrypoint for invoking the container to process a request
    inferenceUrl: str

class OptionalCreateFunctionRequest(TypedDict, total=False):
    # Health endpoint for the container or the helmChart
    healthUri: str

    # Optional port number where the inference listener is running. Defaults to 8000  for Triton. 
    inferencePort: int

    # Args to be passed when launching the container
    containerArgs: str

    # Environment settings for launching the container
    containerEnvironment: typing.List[ContainerEnvironmentEntryDto]

    # Optional set of models
    models: typing.List[ArtifactDto]

    # Optional custom container image
    containerImage: str

    # Optional Helm Chart
    helmChart: str

    # Helm Chart Service Name is required when helmChart property is specified 
    helmChartServiceName: str

    # Optional set of resources
    resources: typing.List[ArtifactDto]

    # Invocation request body format
    apiBodyFormat: str

class CreateFunctionRequest(RequiredCreateFunctionRequest, OptionalCreateFunctionRequest):
    pass
