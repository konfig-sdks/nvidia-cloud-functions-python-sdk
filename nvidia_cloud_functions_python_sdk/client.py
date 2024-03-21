# coding: utf-8
"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

import typing
import inspect
from datetime import date, datetime
from nvidia_cloud_functions_python_sdk.client_custom import ClientCustom
from nvidia_cloud_functions_python_sdk.configuration import Configuration
from nvidia_cloud_functions_python_sdk.api_client import ApiClient
from nvidia_cloud_functions_python_sdk.type_util import copy_signature
from nvidia_cloud_functions_python_sdk.apis.tags.asset_management_api import AssetManagementApi
from nvidia_cloud_functions_python_sdk.apis.tags.authorized_accounts_api import AuthorizedAccountsApi
from nvidia_cloud_functions_python_sdk.apis.tags.cluster_groups_and_gpus_api import ClusterGroupsAndGPUsApi
from nvidia_cloud_functions_python_sdk.apis.tags.envelope_function_invocation_api import EnvelopeFunctionInvocationApi
from nvidia_cloud_functions_python_sdk.apis.tags.function_deployment_api import FunctionDeploymentApi
from nvidia_cloud_functions_python_sdk.apis.tags.function_invocation_api import FunctionInvocationApi
from nvidia_cloud_functions_python_sdk.apis.tags.function_management_api import FunctionManagementApi
from nvidia_cloud_functions_python_sdk.apis.tags.health_api import HealthApi
from nvidia_cloud_functions_python_sdk.apis.tags.queue_details_api import QueueDetailsApi



class NvidiaCloudFunctions(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.asset_management: AssetManagementApi = AssetManagementApi(api_client)
        self.authorized_accounts: AuthorizedAccountsApi = AuthorizedAccountsApi(api_client)
        self.cluster_groups_and_gpus: ClusterGroupsAndGPUsApi = ClusterGroupsAndGPUsApi(api_client)
        self.envelope_function_invocation: EnvelopeFunctionInvocationApi = EnvelopeFunctionInvocationApi(api_client)
        self.function_deployment: FunctionDeploymentApi = FunctionDeploymentApi(api_client)
        self.function_invocation: FunctionInvocationApi = FunctionInvocationApi(api_client)
        self.function_management: FunctionManagementApi = FunctionManagementApi(api_client)
        self.health: HealthApi = HealthApi(api_client)
        self.queue_details: QueueDetailsApi = QueueDetailsApi(api_client)
