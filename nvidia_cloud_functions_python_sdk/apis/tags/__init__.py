# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nvidia_cloud_functions_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHORIZED_ACCOUNTS = "Authorized Accounts"
    FUNCTION_MANAGEMENT = "Function Management"
    ASSET_MANAGEMENT = "Asset Management"
    FUNCTION_DEPLOYMENT = "Function Deployment"
    FUNCTION_INVOCATION = "Function Invocation"
    ENVELOPE_FUNCTION_INVOCATION = "Envelope Function Invocation"
    QUEUE_DETAILS = "Queue Details"
    CLUSTER_GROUPS_AND_GPUS = "Cluster Groups and GPUs"
    HEALTH = "Health"
