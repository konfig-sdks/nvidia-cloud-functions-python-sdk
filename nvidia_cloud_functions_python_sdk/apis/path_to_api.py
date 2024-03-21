import typing_extensions

from nvidia_cloud_functions_python_sdk.paths import PathValues
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_deployments_functions_function_id_versions_function_version_id import V2NvcfDeploymentsFunctionsFunctionIdVersionsFunctionVersionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_pexec_functions_function_id import V2NvcfPexecFunctionsFunctionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_pexec_functions_function_id_versions_version_id import V2NvcfPexecFunctionsFunctionIdVersionsVersionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_exec_functions_function_id import V2NvcfExecFunctionsFunctionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_exec_functions_function_id_versions_version_id import V2NvcfExecFunctionsFunctionIdVersionsVersionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_functions_function_id_versions import V2NvcfFunctionsFunctionIdVersions
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_functions import V2NvcfFunctions
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_authorizations_functions_function_id_versions_function_version_id import V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_authorizations_functions_function_id import V2NvcfAuthorizationsFunctionsFunctionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_assets import V2NvcfAssets
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_authorizations_functions_function_id_versions_function_version_id_remove import V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionIdRemove
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_authorizations_functions_function_id_versions_function_version_id_add import V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionIdAdd
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_authorizations_functions_function_id_remove import V2NvcfAuthorizationsFunctionsFunctionIdRemove
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_authorizations_functions_function_id_add import V2NvcfAuthorizationsFunctionsFunctionIdAdd
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_queues_functions_function_id_versions_version_id import V2NvcfQueuesFunctionsFunctionIdVersionsVersionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_queues_functions_function_id import V2NvcfQueuesFunctionsFunctionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_queues_request_id_position import V2NvcfQueuesRequestIdPosition
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_pexec_status_request_id import V2NvcfPexecStatusRequestId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_functions_function_id_versions_function_version_id import V2NvcfFunctionsFunctionIdVersionsFunctionVersionId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_functions_ids import V2NvcfFunctionsIds
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_exec_status_request_id import V2NvcfExecStatusRequestId
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_cluster_groups import V2NvcfClusterGroups
from nvidia_cloud_functions_python_sdk.apis.paths.v2_nvcf_assets_asset_id import V2NvcfAssetsAssetId
from nvidia_cloud_functions_python_sdk.apis.paths.health_ import Health

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_NVCF_DEPLOYMENTS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID: V2NvcfDeploymentsFunctionsFunctionIdVersionsFunctionVersionId,
        PathValues.V2_NVCF_PEXEC_FUNCTIONS_FUNCTION_ID: V2NvcfPexecFunctionsFunctionId,
        PathValues.V2_NVCF_PEXEC_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID: V2NvcfPexecFunctionsFunctionIdVersionsVersionId,
        PathValues.V2_NVCF_EXEC_FUNCTIONS_FUNCTION_ID: V2NvcfExecFunctionsFunctionId,
        PathValues.V2_NVCF_EXEC_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID: V2NvcfExecFunctionsFunctionIdVersionsVersionId,
        PathValues.V2_NVCF_FUNCTIONS_FUNCTION_ID_VERSIONS: V2NvcfFunctionsFunctionIdVersions,
        PathValues.V2_NVCF_FUNCTIONS: V2NvcfFunctions,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID: V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionId,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID: V2NvcfAuthorizationsFunctionsFunctionId,
        PathValues.V2_NVCF_ASSETS: V2NvcfAssets,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID_REMOVE: V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionIdRemove,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID_ADD: V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionIdAdd,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_REMOVE: V2NvcfAuthorizationsFunctionsFunctionIdRemove,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_ADD: V2NvcfAuthorizationsFunctionsFunctionIdAdd,
        PathValues.V2_NVCF_QUEUES_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID: V2NvcfQueuesFunctionsFunctionIdVersionsVersionId,
        PathValues.V2_NVCF_QUEUES_FUNCTIONS_FUNCTION_ID: V2NvcfQueuesFunctionsFunctionId,
        PathValues.V2_NVCF_QUEUES_REQUEST_ID_POSITION: V2NvcfQueuesRequestIdPosition,
        PathValues.V2_NVCF_PEXEC_STATUS_REQUEST_ID: V2NvcfPexecStatusRequestId,
        PathValues.V2_NVCF_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID: V2NvcfFunctionsFunctionIdVersionsFunctionVersionId,
        PathValues.V2_NVCF_FUNCTIONS_IDS: V2NvcfFunctionsIds,
        PathValues.V2_NVCF_EXEC_STATUS_REQUEST_ID: V2NvcfExecStatusRequestId,
        PathValues.V2_NVCF_CLUSTER_GROUPS: V2NvcfClusterGroups,
        PathValues.V2_NVCF_ASSETS_ASSET_ID: V2NvcfAssetsAssetId,
        PathValues.HEALTH_: Health,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_NVCF_DEPLOYMENTS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID: V2NvcfDeploymentsFunctionsFunctionIdVersionsFunctionVersionId,
        PathValues.V2_NVCF_PEXEC_FUNCTIONS_FUNCTION_ID: V2NvcfPexecFunctionsFunctionId,
        PathValues.V2_NVCF_PEXEC_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID: V2NvcfPexecFunctionsFunctionIdVersionsVersionId,
        PathValues.V2_NVCF_EXEC_FUNCTIONS_FUNCTION_ID: V2NvcfExecFunctionsFunctionId,
        PathValues.V2_NVCF_EXEC_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID: V2NvcfExecFunctionsFunctionIdVersionsVersionId,
        PathValues.V2_NVCF_FUNCTIONS_FUNCTION_ID_VERSIONS: V2NvcfFunctionsFunctionIdVersions,
        PathValues.V2_NVCF_FUNCTIONS: V2NvcfFunctions,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID: V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionId,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID: V2NvcfAuthorizationsFunctionsFunctionId,
        PathValues.V2_NVCF_ASSETS: V2NvcfAssets,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID_REMOVE: V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionIdRemove,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID_ADD: V2NvcfAuthorizationsFunctionsFunctionIdVersionsFunctionVersionIdAdd,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_REMOVE: V2NvcfAuthorizationsFunctionsFunctionIdRemove,
        PathValues.V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_ADD: V2NvcfAuthorizationsFunctionsFunctionIdAdd,
        PathValues.V2_NVCF_QUEUES_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID: V2NvcfQueuesFunctionsFunctionIdVersionsVersionId,
        PathValues.V2_NVCF_QUEUES_FUNCTIONS_FUNCTION_ID: V2NvcfQueuesFunctionsFunctionId,
        PathValues.V2_NVCF_QUEUES_REQUEST_ID_POSITION: V2NvcfQueuesRequestIdPosition,
        PathValues.V2_NVCF_PEXEC_STATUS_REQUEST_ID: V2NvcfPexecStatusRequestId,
        PathValues.V2_NVCF_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID: V2NvcfFunctionsFunctionIdVersionsFunctionVersionId,
        PathValues.V2_NVCF_FUNCTIONS_IDS: V2NvcfFunctionsIds,
        PathValues.V2_NVCF_EXEC_STATUS_REQUEST_ID: V2NvcfExecStatusRequestId,
        PathValues.V2_NVCF_CLUSTER_GROUPS: V2NvcfClusterGroups,
        PathValues.V2_NVCF_ASSETS_ASSET_ID: V2NvcfAssetsAssetId,
        PathValues.HEALTH_: Health,
    }
)
