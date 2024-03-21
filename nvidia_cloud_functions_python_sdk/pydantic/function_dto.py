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
from nvidia_cloud_functions_python_sdk.pydantic.instance_dto import InstanceDto

class FunctionDto(BaseModel):
    # Unique function id
    id: str = Field(alias='id')

    # NVIDIA Cloud Account Id
    nca_id: str = Field(alias='ncaId')

    # Unique function version id
    version_id: str = Field(alias='versionId')

    # Function name
    name: str = Field(alias='name')

    # Function status
    status: Literal["ACTIVE", "DEPLOYING", "ERROR", "INACTIVE", "DELETED"] = Field(alias='status')

    # Health endpoint for the container or helmChart
    health_uri: str = Field(alias='healthUri')

    # Function creation timestamp
    created_at: datetime = Field(alias='createdAt')

    # Entrypoint for invoking the container to process requests
    inference_url: typing.Optional[str] = Field(None, alias='inferenceUrl')

    # Indicates whether the function is owned by another account. If the account  that is being used to lookup functions happens to be authorized to invoke/list  this function which is owned by a different account, then this field is set  to true and ncaId will contain the id of the account that owns the function.  Otherwise, this field is not set as it defaults to false. 
    owned_by_different_account: typing.Optional[bool] = Field(None, alias='ownedByDifferentAccount')

    # Optional port number where the inference listener is running - defaults to 8000 for Triton
    inference_port: typing.Optional[int] = Field(None, alias='inferencePort')

    # Args used to launch the container
    container_args: typing.Optional[str] = Field(None, alias='containerArgs')

    # Environment settings used to launch the container
    container_environment: typing.Optional[typing.List[ContainerEnvironmentEntryDto]] = Field(None, alias='containerEnvironment')

    # Optional set of models
    models: typing.Optional[typing.List[ArtifactDto]] = Field(None, alias='models')

    # Optional custom container
    container_image: typing.Optional[str] = Field(None, alias='containerImage')

    # Invocation request body format
    api_body_format: typing.Optional[Literal["PREDICT_V2", "CUSTOM"]] = Field(None, alias='apiBodyFormat')

    # Optional Helm Chart
    helm_chart: typing.Optional[str] = Field(None, alias='helmChart')

    # Helm Chart Service Name specified only when helmChart property is specified 
    helm_chart_service_name: typing.Optional[str] = Field(None, alias='helmChartServiceName')

    # List of active instances for this function.
    active_instances: typing.Optional[typing.List[InstanceDto]] = Field(None, alias='activeInstances')

    # Optional set of resources.
    resources: typing.Optional[typing.List[ArtifactDto]] = Field(None, alias='resources')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
