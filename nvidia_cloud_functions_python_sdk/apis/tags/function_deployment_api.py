# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_deployments_functions_function_id_versions_function_version_id.delete import DeleteByIdAndVersion
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_deployments_functions_function_id_versions_function_version_id.get import Details
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_deployments_functions_function_id_versions_function_version_id.post import InitiateDeploymentForVersion
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_deployments_functions_function_id_versions_function_version_id.put import UpdateSpecs
from nvidia_cloud_functions_python_sdk.apis.tags.function_deployment_api_raw import FunctionDeploymentApiRaw


class FunctionDeploymentApi(
    DeleteByIdAndVersion,
    Details,
    InitiateDeploymentForVersion,
    UpdateSpecs,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FunctionDeploymentApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FunctionDeploymentApiRaw(api_client)
