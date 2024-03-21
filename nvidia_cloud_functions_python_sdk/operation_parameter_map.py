operation_parameter_map = {
    '/v2/nvcf/assets-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'contentType'
            },
        ]
    },
    '/v2/nvcf/assets/{assetId}-DELETE': {
        'parameters': [
            {
                'name': 'assetId'
            },
        ]
    },
    '/v2/nvcf/assets-GET': {
        'parameters': [
        ]
    },
    '/v2/nvcf/assets/{assetId}-GET': {
        'parameters': [
            {
                'name': 'assetId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/add-PATCH': {
        'parameters': [
            {
                'name': 'authorizedParty'
            },
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/add-PATCH': {
        'parameters': [
            {
                'name': 'authorizedParty'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}-POST': {
        'parameters': [
            {
                'name': 'authorizedParties'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}-POST': {
        'parameters': [
            {
                'name': 'authorizedParties'
            },
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/remove-PATCH': {
        'parameters': [
            {
                'name': 'authorizedParty'
            },
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove-PATCH': {
        'parameters': [
            {
                'name': 'authorizedParty'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/clusterGroups-GET': {
        'parameters': [
        ]
    },
    '/v2/nvcf/exec/functions/{functionId}-POST': {
        'parameters': [
            {
                'name': 'requestBody'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'requestHeader'
            },
        ]
    },
    '/v2/nvcf/exec/functions/{functionId}/versions/{versionId}-POST': {
        'parameters': [
            {
                'name': 'requestBody'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'versionId'
            },
            {
                'name': 'requestHeader'
            },
        ]
    },
    '/v2/nvcf/exec/status/{requestId}-GET': {
        'parameters': [
            {
                'name': 'requestId'
            },
        ]
    },
    '/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
            {
                'name': 'graceful'
            },
        ]
    },
    '/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}-POST': {
        'parameters': [
            {
                'name': 'deploymentSpecifications'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}-PUT': {
        'parameters': [
            {
                'name': 'deploymentSpecifications'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/pexec/functions/{functionId}-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'NVCF-INPUT-ASSET-REFERENCES'
            },
            {
                'name': 'NVCF-POLL-SECONDS'
            },
        ]
    },
    '/v2/nvcf/pexec/functions/{functionId}/versions/{versionId}-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'versionId'
            },
            {
                'name': 'NVCF-INPUT-ASSET-REFERENCES'
            },
            {
                'name': 'NVCF-POLL-SECONDS'
            },
        ]
    },
    '/v2/nvcf/pexec/status/{requestId}-GET': {
        'parameters': [
            {
                'name': 'requestId'
            },
            {
                'name': 'NVCF-POLL-SECONDS'
            },
        ]
    },
    '/v2/nvcf/functions/{functionId}/versions-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'inferenceUrl'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'healthUri'
            },
            {
                'name': 'inferencePort'
            },
            {
                'name': 'containerArgs'
            },
            {
                'name': 'containerEnvironment'
            },
            {
                'name': 'models'
            },
            {
                'name': 'containerImage'
            },
            {
                'name': 'helmChart'
            },
            {
                'name': 'helmChartServiceName'
            },
            {
                'name': 'resources'
            },
            {
                'name': 'apiBodyFormat'
            },
        ]
    },
    '/v2/nvcf/functions/{functionId}/versions/{functionVersionId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/functions/{functionId}/versions/{functionVersionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'functionVersionId'
            },
        ]
    },
    '/v2/nvcf/functions/ids-GET': {
        'parameters': [
            {
                'name': 'visibility'
            },
        ]
    },
    '/v2/nvcf/functions/{functionId}/versions-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/functions-GET': {
        'parameters': [
            {
                'name': 'visibility'
            },
        ]
    },
    '/v2/nvcf/functions-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'inferenceUrl'
            },
            {
                'name': 'healthUri'
            },
            {
                'name': 'inferencePort'
            },
            {
                'name': 'containerArgs'
            },
            {
                'name': 'containerEnvironment'
            },
            {
                'name': 'models'
            },
            {
                'name': 'containerImage'
            },
            {
                'name': 'helmChart'
            },
            {
                'name': 'helmChartServiceName'
            },
            {
                'name': 'resources'
            },
            {
                'name': 'apiBodyFormat'
            },
        ]
    },
    '/health/**-GET': {
        'parameters': [
        ]
    },
    '/v2/nvcf/queues/functions/{functionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/v2/nvcf/queues/functions/{functionId}/versions/{versionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'versionId'
            },
        ]
    },
    '/v2/nvcf/queues/{requestId}/position-GET': {
        'parameters': [
            {
                'name': 'requestId'
            },
        ]
    },
};