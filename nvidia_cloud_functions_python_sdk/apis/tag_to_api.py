import typing_extensions

from nvidia_cloud_functions_python_sdk.apis.tags import TagValues
from nvidia_cloud_functions_python_sdk.apis.tags.authorized_accounts_api import AuthorizedAccountsApi
from nvidia_cloud_functions_python_sdk.apis.tags.function_management_api import FunctionManagementApi
from nvidia_cloud_functions_python_sdk.apis.tags.asset_management_api import AssetManagementApi
from nvidia_cloud_functions_python_sdk.apis.tags.function_deployment_api import FunctionDeploymentApi
from nvidia_cloud_functions_python_sdk.apis.tags.function_invocation_api import FunctionInvocationApi
from nvidia_cloud_functions_python_sdk.apis.tags.envelope_function_invocation_api import EnvelopeFunctionInvocationApi
from nvidia_cloud_functions_python_sdk.apis.tags.queue_details_api import QueueDetailsApi
from nvidia_cloud_functions_python_sdk.apis.tags.cluster_groups_and_gpus_api import ClusterGroupsAndGPUsApi
from nvidia_cloud_functions_python_sdk.apis.tags.health_api import HealthApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHORIZED_ACCOUNTS: AuthorizedAccountsApi,
        TagValues.FUNCTION_MANAGEMENT: FunctionManagementApi,
        TagValues.ASSET_MANAGEMENT: AssetManagementApi,
        TagValues.FUNCTION_DEPLOYMENT: FunctionDeploymentApi,
        TagValues.FUNCTION_INVOCATION: FunctionInvocationApi,
        TagValues.ENVELOPE_FUNCTION_INVOCATION: EnvelopeFunctionInvocationApi,
        TagValues.QUEUE_DETAILS: QueueDetailsApi,
        TagValues.CLUSTER_GROUPS_AND_GPUS: ClusterGroupsAndGPUsApi,
        TagValues.HEALTH: HealthApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHORIZED_ACCOUNTS: AuthorizedAccountsApi,
        TagValues.FUNCTION_MANAGEMENT: FunctionManagementApi,
        TagValues.ASSET_MANAGEMENT: AssetManagementApi,
        TagValues.FUNCTION_DEPLOYMENT: FunctionDeploymentApi,
        TagValues.FUNCTION_INVOCATION: FunctionInvocationApi,
        TagValues.ENVELOPE_FUNCTION_INVOCATION: EnvelopeFunctionInvocationApi,
        TagValues.QUEUE_DETAILS: QueueDetailsApi,
        TagValues.CLUSTER_GROUPS_AND_GPUS: ClusterGroupsAndGPUsApi,
        TagValues.HEALTH: HealthApi,
    }
)
