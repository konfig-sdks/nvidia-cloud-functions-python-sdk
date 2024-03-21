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

from nvidia_cloud_functions_python_sdk.pydantic.artifact_dto import ArtifactDto
from nvidia_cloud_functions_python_sdk.pydantic.container_environment_entry_dto import ContainerEnvironmentEntryDto

class CreateFunctionRequest(BaseModel):
    # Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters
    name: str = Field(alias='name')

    # Entrypoint for invoking the container to process a request
    inference_url: str = Field(alias='inferenceUrl')

    # Health endpoint for the container or the helmChart
    health_uri: typing.Optional[str] = Field(None, alias='healthUri')

    # Optional port number where the inference listener is running. Defaults to 8000  for Triton. 
    inference_port: typing.Optional[int] = Field(None, alias='inferencePort')

    # Args to be passed when launching the container
    container_args: typing.Optional[str] = Field(None, alias='containerArgs')

    # Environment settings for launching the container
    container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = Field(None, alias='containerEnvironment')

    # Optional set of models
    models: typing.Optional[typing.List[ArtifactDto]] = Field(None, alias='models')

    # Optional custom container image
    container_image: typing.Optional[str] = Field(None, alias='containerImage')

    # Optional Helm Chart
    helm_chart: typing.Optional[str] = Field(None, alias='helmChart')

    # Helm Chart Service Name is required when helmChart property is specified 
    helm_chart_service_name: typing.Optional[str] = Field(None, alias='helmChartServiceName')

    # Optional set of resources
    resources: typing.Optional[typing.List[ArtifactDto]] = Field(None, alias='resources')

    # Invocation request body format
    api_body_format: typing.Optional[Literal["PREDICT_V2", "CUSTOM"]] = Field(None, alias='apiBodyFormat')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
