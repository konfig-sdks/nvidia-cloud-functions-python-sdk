# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nvidia_cloud_functions_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_NVCF_DEPLOYMENTS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID = "/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}"
    V2_NVCF_PEXEC_FUNCTIONS_FUNCTION_ID = "/v2/nvcf/pexec/functions/{functionId}"
    V2_NVCF_PEXEC_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID = "/v2/nvcf/pexec/functions/{functionId}/versions/{versionId}"
    V2_NVCF_EXEC_FUNCTIONS_FUNCTION_ID = "/v2/nvcf/exec/functions/{functionId}"
    V2_NVCF_EXEC_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID = "/v2/nvcf/exec/functions/{functionId}/versions/{versionId}"
    V2_NVCF_FUNCTIONS_FUNCTION_ID_VERSIONS = "/v2/nvcf/functions/{functionId}/versions"
    V2_NVCF_FUNCTIONS = "/v2/nvcf/functions"
    V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID = "/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}"
    V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID = "/v2/nvcf/authorizations/functions/{functionId}"
    V2_NVCF_ASSETS = "/v2/nvcf/assets"
    V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID_REMOVE = "/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove"
    V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID_ADD = "/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/add"
    V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_REMOVE = "/v2/nvcf/authorizations/functions/{functionId}/remove"
    V2_NVCF_AUTHORIZATIONS_FUNCTIONS_FUNCTION_ID_ADD = "/v2/nvcf/authorizations/functions/{functionId}/add"
    V2_NVCF_QUEUES_FUNCTIONS_FUNCTION_ID_VERSIONS_VERSION_ID = "/v2/nvcf/queues/functions/{functionId}/versions/{versionId}"
    V2_NVCF_QUEUES_FUNCTIONS_FUNCTION_ID = "/v2/nvcf/queues/functions/{functionId}"
    V2_NVCF_QUEUES_REQUEST_ID_POSITION = "/v2/nvcf/queues/{requestId}/position"
    V2_NVCF_PEXEC_STATUS_REQUEST_ID = "/v2/nvcf/pexec/status/{requestId}"
    V2_NVCF_FUNCTIONS_FUNCTION_ID_VERSIONS_FUNCTION_VERSION_ID = "/v2/nvcf/functions/{functionId}/versions/{functionVersionId}"
    V2_NVCF_FUNCTIONS_IDS = "/v2/nvcf/functions/ids"
    V2_NVCF_EXEC_STATUS_REQUEST_ID = "/v2/nvcf/exec/status/{requestId}"
    V2_NVCF_CLUSTER_GROUPS = "/v2/nvcf/clusterGroups"
    V2_NVCF_ASSETS_ASSET_ID = "/v2/nvcf/assets/{assetId}"
    HEALTH_ = "/health/**"
