<div align="left">

[![Visit Nvidia](./header.png)](https://www.nvidia.com&#x2F;en-us&#x2F;ai&#x2F;)

# Nvidia<a id="nvidia"></a>

Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`nvidiacloudfunctions.asset_management.create_asset_and_url`](#nvidiacloudfunctionsasset_managementcreate_asset_and_url)
  * [`nvidiacloudfunctions.asset_management.delete_asset_by_id`](#nvidiacloudfunctionsasset_managementdelete_asset_by_id)
  * [`nvidiacloudfunctions.asset_management.list_assets`](#nvidiacloudfunctionsasset_managementlist_assets)
  * [`nvidiacloudfunctions.asset_management.show_details`](#nvidiacloudfunctionsasset_managementshow_details)
  * [`nvidiacloudfunctions.authorized_accounts.add_account_to_function`](#nvidiacloudfunctionsauthorized_accountsadd_account_to_function)
  * [`nvidiacloudfunctions.authorized_accounts.add_account_to_function_version`](#nvidiacloudfunctionsauthorized_accountsadd_account_to_function_version)
  * [`nvidiacloudfunctions.authorized_accounts.authorize_function_accounts`](#nvidiacloudfunctionsauthorized_accountsauthorize_function_accounts)
  * [`nvidiacloudfunctions.authorized_accounts.authorize_function_accounts_0`](#nvidiacloudfunctionsauthorized_accountsauthorize_function_accounts_0)
  * [`nvidiacloudfunctions.authorized_accounts.delete_all_extra_for_function`](#nvidiacloudfunctionsauthorized_accountsdelete_all_extra_for_function)
  * [`nvidiacloudfunctions.authorized_accounts.delete_extra_for_function_version`](#nvidiacloudfunctionsauthorized_accountsdelete_extra_for_function_version)
  * [`nvidiacloudfunctions.authorized_accounts.function_version_authorizations`](#nvidiacloudfunctionsauthorized_accountsfunction_version_authorizations)
  * [`nvidiacloudfunctions.authorized_accounts.list_for_function`](#nvidiacloudfunctionsauthorized_accountslist_for_function)
  * [`nvidiacloudfunctions.authorized_accounts.remove_from_function_authorization`](#nvidiacloudfunctionsauthorized_accountsremove_from_function_authorization)
  * [`nvidiacloudfunctions.authorized_accounts.remove_party_for_version`](#nvidiacloudfunctionsauthorized_accountsremove_party_for_version)
  * [`nvidiacloudfunctions.cluster_groups_and_gpus.list`](#nvidiacloudfunctionscluster_groups_and_gpuslist)
  * [`nvidiacloudfunctions.envelope_function_invocation.call_function`](#nvidiacloudfunctionsenvelope_function_invocationcall_function)
  * [`nvidiacloudfunctions.envelope_function_invocation.invoke_function`](#nvidiacloudfunctionsenvelope_function_invocationinvoke_function)
  * [`nvidiacloudfunctions.envelope_function_invocation.poll_for_result_using_function_invocation_request`](#nvidiacloudfunctionsenvelope_function_invocationpoll_for_result_using_function_invocation_request)
  * [`nvidiacloudfunctions.function_deployment.delete_by_id_and_version`](#nvidiacloudfunctionsfunction_deploymentdelete_by_id_and_version)
  * [`nvidiacloudfunctions.function_deployment.details`](#nvidiacloudfunctionsfunction_deploymentdetails)
  * [`nvidiacloudfunctions.function_deployment.initiate_deployment_for_version`](#nvidiacloudfunctionsfunction_deploymentinitiate_deployment_for_version)
  * [`nvidiacloudfunctions.function_deployment.update_specs`](#nvidiacloudfunctionsfunction_deploymentupdate_specs)
  * [`nvidiacloudfunctions.function_invocation.invoke_function`](#nvidiacloudfunctionsfunction_invocationinvoke_function)
  * [`nvidiacloudfunctions.function_invocation.invoke_function_0`](#nvidiacloudfunctionsfunction_invocationinvoke_function_0)
  * [`nvidiacloudfunctions.function_invocation.poll_for_result_using_function_invocation_request`](#nvidiacloudfunctionsfunction_invocationpoll_for_result_using_function_invocation_request)
  * [`nvidiacloudfunctions.function_management.create_function_version`](#nvidiacloudfunctionsfunction_managementcreate_function_version)
  * [`nvidiacloudfunctions.function_management.delete_function_version`](#nvidiacloudfunctionsfunction_managementdelete_function_version)
  * [`nvidiacloudfunctions.function_management.get_version_details`](#nvidiacloudfunctionsfunction_managementget_version_details)
  * [`nvidiacloudfunctions.function_management.list_function_ids`](#nvidiacloudfunctionsfunction_managementlist_function_ids)
  * [`nvidiacloudfunctions.function_management.list_function_versions`](#nvidiacloudfunctionsfunction_managementlist_function_versions)
  * [`nvidiacloudfunctions.function_management.list_functions`](#nvidiacloudfunctionsfunction_managementlist_functions)
  * [`nvidiacloudfunctions.function_management.register_new_function`](#nvidiacloudfunctionsfunction_managementregister_new_function)
  * [`nvidiacloudfunctions.health.get_info`](#nvidiacloudfunctionshealthget_info)
  * [`nvidiacloudfunctions.queue_details.function_queues_details`](#nvidiacloudfunctionsqueue_detailsfunction_queues_details)
  * [`nvidiacloudfunctions.queue_details.get_all_queues_details`](#nvidiacloudfunctionsqueue_detailsget_all_queues_details)
  * [`nvidiacloudfunctions.queue_details.get_queue_position_by_request_id`](#nvidiacloudfunctionsqueue_detailsget_queue_position_by_request_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=NVIDIA&serviceName=CloudFunctions&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from nvidia_cloud_functions_python_sdk import NvidiaCloudFunctions, ApiException

nvidiacloudfunctions = NvidiaCloudFunctions()

try:
    # Create Asset
    create_asset_and_url_response = (
        nvidiacloudfunctions.asset_management.create_asset_and_url(
            description="string_example",
            content_type="string_example",
        )
    )
    print(create_asset_and_url_response)
except ApiException as e:
    print("Exception when calling AssetManagementApi.create_asset_and_url: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from nvidia_cloud_functions_python_sdk import NvidiaCloudFunctions, ApiException

nvidiacloudfunctions = NvidiaCloudFunctions()


async def main():
    try:
        # Create Asset
        create_asset_and_url_response = (
            await nvidiacloudfunctions.asset_management.acreate_asset_and_url(
                description="string_example",
                content_type="string_example",
            )
        )
        print(create_asset_and_url_response)
    except ApiException as e:
        print(
            "Exception when calling AssetManagementApi.create_asset_and_url: %s\n" % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from nvidia_cloud_functions_python_sdk import NvidiaCloudFunctions, ApiException

nvidiacloudfunctions = NvidiaCloudFunctions()

try:
    # Create Asset
    create_asset_and_url_response = (
        nvidiacloudfunctions.asset_management.raw.create_asset_and_url(
            description="string_example",
            content_type="string_example",
        )
    )
    pprint(create_asset_and_url_response.body)
    pprint(create_asset_and_url_response.body["description"])
    pprint(create_asset_and_url_response.body["asset_id"])
    pprint(create_asset_and_url_response.body["upload_url"])
    pprint(create_asset_and_url_response.body["content_type"])
    pprint(create_asset_and_url_response.headers)
    pprint(create_asset_and_url_response.status)
    pprint(create_asset_and_url_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AssetManagementApi.create_asset_and_url: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `nvidiacloudfunctions.asset_management.create_asset_and_url`<a id="nvidiacloudfunctionsasset_managementcreate_asset_and_url"></a>

Creates a unique id representing an asset and a pre-signed URL to upload the  asset artifact to AWS S3 bucket for the NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_asset_and_url_response = (
    nvidiacloudfunctions.asset_management.create_asset_and_url(
        description="string_example",
        content_type="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

Asset description

##### content_type: `str`<a id="content_type-str"></a>

Content type of the asset such image/png, image/jpeg, etc.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAssetRequest`](./nvidia_cloud_functions_python_sdk/type/create_asset_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateAssetResponse`](./nvidia_cloud_functions_python_sdk/pydantic/create_asset_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/assets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.asset_management.delete_asset_by_id`<a id="nvidiacloudfunctionsasset_managementdelete_asset_by_id"></a>

Deletes asset belonging to the current NVIDIA Cloud Account. Requires either  a bearer token or an api-key with 'invoke_function' scope in the HTTP  Authorization header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nvidiacloudfunctions.asset_management.delete_asset_by_id(
    asset_id="assetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `str`<a id="asset_id-str"></a>

Id of the asset to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/assets/{assetId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.asset_management.list_assets`<a id="nvidiacloudfunctionsasset_managementlist_assets"></a>

List assets owned by the current NVIDIA Cloud Account. Requires either a  bearer token or an api-key with invoke_function scope in the HTTP Authorization  header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_assets_response = nvidiacloudfunctions.asset_management.list_assets()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListAssetsResponse`](./nvidia_cloud_functions_python_sdk/pydantic/list_assets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/assets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.asset_management.show_details`<a id="nvidiacloudfunctionsasset_managementshow_details"></a>

Returns details for the specified asset-id belonging to the current NVIDIA  Cloud Account. Requires either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_details_response = nvidiacloudfunctions.asset_management.show_details(
    asset_id="assetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_id: `str`<a id="asset_id-str"></a>

Asset id

#### 🔄 Return<a id="🔄-return"></a>

[`AssetResponse`](./nvidia_cloud_functions_python_sdk/pydantic/asset_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/assets/{assetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.add_account_to_function`<a id="nvidiacloudfunctionsauthorized_accountsadd_account_to_function"></a>

Adds the specified NVIDIA Cloud Account to the set of authorized accounts that  are can invoke all the versions of the specified function. If the specified  function does not have any existing inheritable authorized accounts, it results  in a response with status 404. If the specified account is already in the set  of existing inheritable authorized accounts, it results in a response with  status code 409. If a function is public, then Account Admin cannot perform  this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_account_to_function_response = (
    nvidiacloudfunctions.authorized_accounts.add_account_to_function(
        authorized_party={
            "nca_id": "nca_id_example",
        },
        function_id="functionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorized_party: [`AuthorizedPartyDto`](./nvidia_cloud_functions_python_sdk/type/authorized_party_dto.py)<a id="authorized_party-authorizedpartydtonvidia_cloud_functions_python_sdktypeauthorized_party_dtopy"></a>


##### function_id: `str`<a id="function_id-str"></a>

Function id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchAuthorizedPartyRequest`](./nvidia_cloud_functions_python_sdk/type/patch_authorized_party_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/add` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.add_account_to_function_version`<a id="nvidiacloudfunctionsauthorized_accountsadd_account_to_function_version"></a>

Adds the specified NVIDIA Cloud Account to the set of authorized accounts that  can invoke the specified function version. If the specified function version  does not have any existing inheritable authorized accounts, it results in a  response with status 404. If the specified account is already in the set of  existing authorized accounts that are directly associated with the function  version, it results in a response wit status code 409. If a function is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_account_to_function_version_response = (
    nvidiacloudfunctions.authorized_accounts.add_account_to_function_version(
        authorized_party={
            "nca_id": "nca_id_example",
        },
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorized_party: [`AuthorizedPartyDto`](./nvidia_cloud_functions_python_sdk/type/authorized_party_dto.py)<a id="authorized_party-authorizedpartydtonvidia_cloud_functions_python_sdktypeauthorized_party_dtopy"></a>


##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchAuthorizedPartyRequest`](./nvidia_cloud_functions_python_sdk/type/patch_authorized_party_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/add` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.authorize_function_accounts`<a id="nvidiacloudfunctionsauthorized_accountsauthorize_function_accounts"></a>

Authorizes additional NVIDIA Cloud Accounts to invoke a specific function  version. By default, a function belongs to the NVIDIA Cloud Account that  created it, and the credentials used for function invocation must reference  the same NVIDIA Cloud Account. Upon invocation of this endpoint, any existing  authorized accounts will be overwritten by the newly specified authorized  accounts. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authorize_function_accounts_response = (
    nvidiacloudfunctions.authorized_accounts.authorize_function_accounts(
        authorized_parties=[
            {
                "nca_id": "nca_id_example",
            }
        ],
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorized_parties: List[`AuthorizedPartyDto`]<a id="authorized_parties-listauthorizedpartydto"></a>

Parties authorized to invoke function

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizedPartiesRequest`](./nvidia_cloud_functions_python_sdk/type/authorized_parties_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.authorize_function_accounts_0`<a id="nvidiacloudfunctionsauthorized_accountsauthorize_function_accounts_0"></a>

Authorizes additional NVIDIA Cloud Accounts to invoke any version of the  specified function. By default, a function belongs to the NVIDIA Cloud Account  that created it, and the credentials used for function invocation must  reference the same NVIDIA Cloud Account. Upon invocation of this endpoint, any  existing authorized accounts will be overwritten by the newly specified  authorized accounts. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
authorize_function_accounts_0_response = (
    nvidiacloudfunctions.authorized_accounts.authorize_function_accounts_0(
        authorized_parties=[
            {
                "nca_id": "nca_id_example",
            }
        ],
        function_id="functionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorized_parties: List[`AuthorizedPartyDto`]<a id="authorized_parties-listauthorizedpartydto"></a>

Parties authorized to invoke function

##### function_id: `str`<a id="function_id-str"></a>

Function id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthorizedPartiesRequest`](./nvidia_cloud_functions_python_sdk/type/authorized_parties_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.delete_all_extra_for_function`<a id="nvidiacloudfunctionsauthorized_accountsdelete_all_extra_for_function"></a>

Deletes all the extra NVIDIA Cloud Accounts that were authorized to invoke the  function and all its versions. If a function version has its own set of  authorized accounts, those are not deleted. If the specified function is  public, then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_all_extra_for_function_response = (
    nvidiacloudfunctions.authorized_accounts.delete_all_extra_for_function(
        function_id="functionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.delete_extra_for_function_version`<a id="nvidiacloudfunctionsauthorized_accountsdelete_extra_for_function_version"></a>

Deletes all the authorized accounts that are directly associated with the  specified function version. Authorized parties that are inherited by the  function version are not deleted. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_extra_for_function_version_response = (
    nvidiacloudfunctions.authorized_accounts.delete_extra_for_function_version(
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.function_version_authorizations`<a id="nvidiacloudfunctionsauthorized_accountsfunction_version_authorizations"></a>

Gets NVIDIA Cloud Account IDs that are authorized to invoke specified function  version. Response includes authorized accounts that were added specifically  to the function version and the inherited authorized accounts that were  added at the function level. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
function_version_authorizations_response = (
    nvidiacloudfunctions.authorized_accounts.function_version_authorizations(
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version

#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.list_for_function`<a id="nvidiacloudfunctionsauthorized_accountslist_for_function"></a>

Lists NVIDIA Cloud Account IDs that are authorized to invoke any version of the  specified function. The response includes an array showing authorized accounts  for each version. Individual versions of a function can have their own  authorized accounts. So, each object in the array can have different  authorized accounts listed. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_function_response = nvidiacloudfunctions.authorized_accounts.list_for_function(
    function_id="functionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

#### 🔄 Return<a id="🔄-return"></a>

[`ListAuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/list_authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.remove_from_function_authorization`<a id="nvidiacloudfunctionsauthorized_accountsremove_from_function_authorization"></a>

Removes the specified NVIDIA Cloud Account from the set of authorized accounts  that can invoke all the versions of the specified function. If the specified  function does not have any existing inheritable authorized parties, it results  in a response with status 404. Also, if the specified account is not in the  existing set of inheritable authorized accounts, it results in a response with  status 400. If the specified function is public, then Account Admin cannot  perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_from_function_authorization_response = (
    nvidiacloudfunctions.authorized_accounts.remove_from_function_authorization(
        authorized_party={
            "nca_id": "nca_id_example",
        },
        function_id="functionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorized_party: [`AuthorizedPartyDto`](./nvidia_cloud_functions_python_sdk/type/authorized_party_dto.py)<a id="authorized_party-authorizedpartydtonvidia_cloud_functions_python_sdktypeauthorized_party_dtopy"></a>


##### function_id: `str`<a id="function_id-str"></a>

Function id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchAuthorizedPartyRequest`](./nvidia_cloud_functions_python_sdk/type/patch_authorized_party_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/remove` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.authorized_accounts.remove_party_for_version`<a id="nvidiacloudfunctionsauthorized_accountsremove_party_for_version"></a>

Removes the specified NVIDIA Cloud Account from the set of authorized accounts  that are directly associated with specified function version. If the specified  function version does not have any of its own(not inherited) authorized  accounts, it results in a response with status 404. Also, if the specified  authorized account is not in the set of existing authorized parties that are  directly associated with the specified function version, it results in a  response with status code 400. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this functionality mandates the inclusion of a bearer token with the  'authorize_clients' scope in the HTTP Authorization header 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_party_for_version_response = (
    nvidiacloudfunctions.authorized_accounts.remove_party_for_version(
        authorized_party={
            "nca_id": "nca_id_example",
        },
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorized_party: [`AuthorizedPartyDto`](./nvidia_cloud_functions_python_sdk/type/authorized_party_dto.py)<a id="authorized_party-authorizedpartydtonvidia_cloud_functions_python_sdktypeauthorized_party_dtopy"></a>


##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchAuthorizedPartyRequest`](./nvidia_cloud_functions_python_sdk/type/patch_authorized_party_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthorizedPartiesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/authorized_parties_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/authorizations/functions/{functionId}/versions/{functionVersionId}/remove` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.cluster_groups_and_gpus.list`<a id="nvidiacloudfunctionscluster_groups_and_gpuslist"></a>

Lists Cluster Groups for the current account. The response includes cluster  groups defined specifically in the current account and publicly available  cluster groups such as GFN, OCI, etc. Requires a bearer token with 'list_cluster_groups' scope in HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = nvidiacloudfunctions.cluster_groups_and_gpus.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ClusterGroupsResponse`](./nvidia_cloud_functions_python_sdk/pydantic/cluster_groups_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/clusterGroups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.envelope_function_invocation.call_function`<a id="nvidiacloudfunctionsenvelope_function_invocationcall_function"></a>

Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
call_function_response = (
    nvidiacloudfunctions.envelope_function_invocation.call_function(
        request_body={},
        function_id="functionId_example",
        request_header={
            "poll_duration_seconds": 300,
        },
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_body: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="request_body-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### function_id: `str`<a id="function_id-str"></a>

##### request_header: [`RequestHeaderDto`](./nvidia_cloud_functions_python_sdk/type/request_header_dto.py)<a id="request_header-requestheaderdtonvidia_cloud_functions_python_sdktyperequest_header_dtopy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvokeFunctionRequest`](./nvidia_cloud_functions_python_sdk/type/invoke_function_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InvokeFunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/invoke_function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/exec/functions/{functionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.envelope_function_invocation.invoke_function`<a id="nvidiacloudfunctionsenvelope_function_invocationinvoke_function"></a>

Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invoke_function_response = (
    nvidiacloudfunctions.envelope_function_invocation.invoke_function(
        request_body={},
        function_id="functionId_example",
        version_id="versionId_example",
        request_header={
            "poll_duration_seconds": 300,
        },
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_body: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="request_body-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### function_id: `str`<a id="function_id-str"></a>

##### version_id: `str`<a id="version_id-str"></a>

##### request_header: [`RequestHeaderDto`](./nvidia_cloud_functions_python_sdk/type/request_header_dto.py)<a id="request_header-requestheaderdtonvidia_cloud_functions_python_sdktyperequest_header_dtopy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InvokeFunctionRequest`](./nvidia_cloud_functions_python_sdk/type/invoke_function_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InvokeFunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/invoke_function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/exec/functions/{functionId}/versions/{versionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.envelope_function_invocation.poll_for_result_using_function_invocation_request`<a id="nvidiacloudfunctionsenvelope_function_invocationpoll_for_result_using_function_invocation_request"></a>

Retrieves the status of an in-progress or pending request using its unique  invocation request ID. If the result is available, it will be included in  the response, marking the request as fulfilled. Conversely, if the result is  not yet available, the request is deemed pending. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
poll_for_result_using_function_invocation_request_response = nvidiacloudfunctions.envelope_function_invocation.poll_for_result_using_function_invocation_request(
    request_id="requestId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

Function invocation request id

#### 🔄 Return<a id="🔄-return"></a>

[`InvokeFunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/invoke_function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/exec/status/{requestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_deployment.delete_by_id_and_version`<a id="nvidiacloudfunctionsfunction_deploymentdelete_by_id_and_version"></a>

Deletes the deployment associated with the specified function. Upon  deletion, any active instances will be terminated, and the function's status  will transition to 'INACTIVE'. To undeploy a function version gracefully,  specify 'graceful=true' query parameter, allowing current tasks to complete  before terminating the instances. If the specified function version is public,  then Account Admin cannot perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_and_version_response = (
    nvidiacloudfunctions.function_deployment.delete_by_id_and_version(
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
        graceful=False,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version id

##### graceful: `bool`<a id="graceful-bool"></a>

Query param to deactivate function for graceful shutdown

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_deployment.details`<a id="nvidiacloudfunctionsfunction_deploymentdetails"></a>

Allows Account Admins to retrieve the deployment details of the specified  function version. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
details_response = nvidiacloudfunctions.function_deployment.details(
    function_id="functionId_example",
    function_version_id="functionVersionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version id

#### 🔄 Return<a id="🔄-return"></a>

[`DeploymentResponse`](./nvidia_cloud_functions_python_sdk/pydantic/deployment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_deployment.initiate_deployment_for_version`<a id="nvidiacloudfunctionsfunction_deploymentinitiate_deployment_for_version"></a>

Initiates deployment for the specified function version. Upon invocation of  this endpoint, the function's status transitions to 'DEPLOYING'. If the  specified function version is public, then Account Admin cannot perform this  operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_deployment_for_version_response = (
    nvidiacloudfunctions.function_deployment.initiate_deployment_for_version(
        deployment_specifications=[
            {
                "gpu": "gpu_example",
                "backend": "backend_example",
                "max_instances": 1,
                "min_instances": 1,
            }
        ],
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### deployment_specifications: List[`GpuSpecificationDto`]<a id="deployment_specifications-listgpuspecificationdto"></a>

Deployment specs with Backend, GPU, instance-type, etc. details

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionDeploymentRequest`](./nvidia_cloud_functions_python_sdk/type/function_deployment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeploymentResponse`](./nvidia_cloud_functions_python_sdk/pydantic/deployment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_deployment.update_specs`<a id="nvidiacloudfunctionsfunction_deploymentupdate_specs"></a>

Updates the deployment specs of the specified function version. It's important  to note that GPU type and backend configurations cannot be modified through  this endpoint. If the specified function is public, then Account Admin cannot  perform this operation. Access to this endpoint mandates a bearer token with 'deploy_function' scope in the  HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_specs_response = nvidiacloudfunctions.function_deployment.update_specs(
    deployment_specifications=[
        {
            "gpu": "gpu_example",
            "backend": "backend_example",
            "max_instances": 1,
            "min_instances": 1,
        }
    ],
    function_id="functionId_example",
    function_version_id="functionVersionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### deployment_specifications: List[`GpuSpecificationDto`]<a id="deployment_specifications-listgpuspecificationdto"></a>

Deployment specs with Backend, GPU, instance-type, etc. details

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Function version id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FunctionDeploymentRequest`](./nvidia_cloud_functions_python_sdk/type/function_deployment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeploymentResponse`](./nvidia_cloud_functions_python_sdk/pydantic/deployment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/deployments/functions/{functionId}/versions/{functionVersionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_invocation.invoke_function`<a id="nvidiacloudfunctionsfunction_invocationinvoke_function"></a>

Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invoke_function_response = nvidiacloudfunctions.function_invocation.invoke_function(
    function_id="functionId_example",
    nvcf_input_asset_references=["string_example"],
    nvcf_poll_seconds=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

##### nvcf_input_asset_references: List[`str`]<a id="nvcf_input_asset_references-liststr"></a>

##### nvcf_poll_seconds: `int`<a id="nvcf_poll_seconds-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`FunctionInvocationInvokeFunction200Response`](./nvidia_cloud_functions_python_sdk/pydantic/function_invocation_invoke_function200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/pexec/functions/{functionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_invocation.invoke_function_0`<a id="nvidiacloudfunctionsfunction_invocationinvoke_function_0"></a>

Invokes the specified function that was successfully deployed. If the version  is not specified, any active function versions will handle the request. If  the version is specified in the URI, then the request is exclusively processed  by the designated version of the function. By default, this endpoint will block  for 5 seconds. If the request is not fulfilled before the timeout, it's status  is considered in-progress or pending and the response includes HTTP status code  202 with an invocation request ID, indicating that the client should commence  polling for the result using the invocation request ID. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with 'invoke_function'  scope in the HTTP Authorization header. Additionally, this endpoint has the  capability to provide updates on the progress of the request, contingent  upon the workload's provision of such information. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invoke_function_0_response = nvidiacloudfunctions.function_invocation.invoke_function_0(
    function_id="functionId_example",
    version_id="versionId_example",
    nvcf_input_asset_references=["string_example"],
    nvcf_poll_seconds=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

##### version_id: `str`<a id="version_id-str"></a>

##### nvcf_input_asset_references: List[`str`]<a id="nvcf_input_asset_references-liststr"></a>

##### nvcf_poll_seconds: `int`<a id="nvcf_poll_seconds-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`FunctionInvocationInvokeFunction200Response`](./nvidia_cloud_functions_python_sdk/pydantic/function_invocation_invoke_function200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/pexec/functions/{functionId}/versions/{versionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_invocation.poll_for_result_using_function_invocation_request`<a id="nvidiacloudfunctionsfunction_invocationpoll_for_result_using_function_invocation_request"></a>

Retrieves the status of an in-progress or pending request using its unique  invocation request ID. If the result is available, it will be included in  the response, marking the request as fulfilled. Conversely, if the result is  not yet available, the request is deemed pending. Access to this endpoint  mandates inclusion of either a bearer token or an api-key with  'invoke_function' scope in the HTTP Authorization header. In-progress responses are returned in order. If no in-progress response is received  during polling you will receive the most recent in-progress response. Only the first  256 unread in-progress messages are kept. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
poll_for_result_using_function_invocation_request_response = nvidiacloudfunctions.function_invocation.poll_for_result_using_function_invocation_request(
    request_id="requestId_example",
    nvcf_poll_seconds=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

Function invocation request id

##### nvcf_poll_seconds: `int`<a id="nvcf_poll_seconds-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionInvocationPollForResultUsingFunctionInvocationRequestResponse`](./nvidia_cloud_functions_python_sdk/pydantic/function_invocation_poll_for_result_using_function_invocation_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/pexec/status/{requestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.create_function_version`<a id="nvidiacloudfunctionsfunction_managementcreate_function_version"></a>

Creates a version of the specified function within the authenticated NVIDIA  Cloud Account. Requires a bearer token with 'register_function' scope in the  HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_function_version_response = (
    nvidiacloudfunctions.function_management.create_function_version(
        name="gBAMDTMv2D2ylmgd10Z3UB6UkJSIS",
        inference_url="string_example",
        function_id="functionId_example",
        health_uri="string_example",
        inference_port=1,
        container_args="string_example",
        container_environment=[
            {
                "key": "key_example",
                "value": "value_example",
            }
        ],
        models=[
            {
                "version": "version_example",
                "name": "name_example",
                "uri": "uri_example",
            }
        ],
        container_image="string_example",
        helm_chart="string_example",
        helm_chart_service_name="string_example",
        resources=[
            {
                "version": "version_example",
                "name": "name_example",
                "uri": "uri_example",
            }
        ],
        api_body_format="PREDICT_V2",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters

##### inference_url: `str`<a id="inference_url-str"></a>

Entrypoint for invoking the container to process a request

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### health_uri: `str`<a id="health_uri-str"></a>

Health endpoint for the container or the helmChart

##### inference_port: `int`<a id="inference_port-int"></a>

Optional port number where the inference listener is running. Defaults to 8000  for Triton. 

##### container_args: `str`<a id="container_args-str"></a>

Args to be passed when launching the container

##### container_environment: List[`ContainerEnvironmentEntryDto`]<a id="container_environment-listcontainerenvironmententrydto"></a>

Environment settings for launching the container

##### models: List[`ArtifactDto`]<a id="models-listartifactdto"></a>

Optional set of models

##### container_image: `str`<a id="container_image-str"></a>

Optional custom container image

##### helm_chart: `str`<a id="helm_chart-str"></a>

Optional Helm Chart

##### helm_chart_service_name: `str`<a id="helm_chart_service_name-str"></a>

Helm Chart Service Name is required when helmChart property is specified 

##### resources: List[`ArtifactDto`]<a id="resources-listartifactdto"></a>

Optional set of resources

##### api_body_format: `str`<a id="api_body_format-str"></a>

Invocation request body format

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateFunctionRequest`](./nvidia_cloud_functions_python_sdk/type/create_function_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateFunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/create_function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions/{functionId}/versions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.delete_function_version`<a id="nvidiacloudfunctionsfunction_managementdelete_function_version"></a>

Deletes the specified function version in the authenticated NVIDIA Cloud  Account. Requires a bearer token with 'delete_function' scope in the HTTP  Authorization header. If the function version is public, then Account Admin  cannot delete the function. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
nvidiacloudfunctions.function_management.delete_function_version(
    function_id="functionId_example",
    function_version_id="functionVersionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Version id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions/{functionId}/versions/{functionVersionId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.get_version_details`<a id="nvidiacloudfunctionsfunction_managementget_version_details"></a>

Retrieves detailed information of the specified function version in the  authenticated NVIDIA Cloud Account. Requires either a bearer token or an  api-key with 'list_functions' or 'list_functions_details' scopes in the HTTP  Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_version_details_response = (
    nvidiacloudfunctions.function_management.get_version_details(
        function_id="functionId_example",
        function_version_id="functionVersionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### function_version_id: `str`<a id="function_version_id-str"></a>

Version id 

#### 🔄 Return<a id="🔄-return"></a>

[`FunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions/{functionId}/versions/{functionVersionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.list_function_ids`<a id="nvidiacloudfunctionsfunction_managementlist_function_ids"></a>

Lists ids of all the functions in the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_function_ids_response = nvidiacloudfunctions.function_management.list_function_ids(
    visibility=["authorized", "private", "public"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### visibility: List[`str`]<a id="visibility-liststr"></a>

Query param 'visibility' indicates the kind of functions to be included  in the response. 

#### 🔄 Return<a id="🔄-return"></a>

[`ListFunctionIdsResponse`](./nvidia_cloud_functions_python_sdk/pydantic/list_function_ids_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions/ids` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.list_function_versions`<a id="nvidiacloudfunctionsfunction_managementlist_function_versions"></a>

Lists details of all the versions of the specified function in the authenticated  NVIDIA Cloud Account. Requires either a bearer token or an api-key with  'list_functions' or 'list_functions_details' scopes in the HTTP Authorization  header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_function_versions_response = (
    nvidiacloudfunctions.function_management.list_function_versions(
        function_id="functionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

#### 🔄 Return<a id="🔄-return"></a>

[`ListFunctionsResponse`](./nvidia_cloud_functions_python_sdk/pydantic/list_functions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions/{functionId}/versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.list_functions`<a id="nvidiacloudfunctionsfunction_managementlist_functions"></a>

Lists all the functions associated with the authenticated NVIDIA Cloud Account.  Requires either a bearer token or an api-key with 'list_functions' or  'list_functions_details' scopes in the HTTP Authorization header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_functions_response = nvidiacloudfunctions.function_management.list_functions(
    visibility=["authorized", "private", "public"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### visibility: List[`str`]<a id="visibility-liststr"></a>

Query param 'visibility' indicates the kind of functions to be included  in the response. 

#### 🔄 Return<a id="🔄-return"></a>

[`ListFunctionsResponse`](./nvidia_cloud_functions_python_sdk/pydantic/list_functions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.function_management.register_new_function`<a id="nvidiacloudfunctionsfunction_managementregister_new_function"></a>

Creates a new function within the authenticated NVIDIA Cloud Account. Requires a  bearer token with 'register_function' scope in the HTTP Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_new_function_response = (
    nvidiacloudfunctions.function_management.register_new_function(
        name="gBAMDTMv2D2ylmgd10Z3UB6UkJSIS",
        inference_url="string_example",
        health_uri="string_example",
        inference_port=1,
        container_args="string_example",
        container_environment=[
            {
                "key": "key_example",
                "value": "value_example",
            }
        ],
        models=[
            {
                "version": "version_example",
                "name": "name_example",
                "uri": "uri_example",
            }
        ],
        container_image="string_example",
        helm_chart="string_example",
        helm_chart_service_name="string_example",
        resources=[
            {
                "version": "version_example",
                "name": "name_example",
                "uri": "uri_example",
            }
        ],
        api_body_format="PREDICT_V2",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Function name must start with lowercase/uppercase/digit and can only contain lowercase, uppercase, digit, hyphen, and underscore characters

##### inference_url: `str`<a id="inference_url-str"></a>

Entrypoint for invoking the container to process a request

##### health_uri: `str`<a id="health_uri-str"></a>

Health endpoint for the container or the helmChart

##### inference_port: `int`<a id="inference_port-int"></a>

Optional port number where the inference listener is running. Defaults to 8000  for Triton. 

##### container_args: `str`<a id="container_args-str"></a>

Args to be passed when launching the container

##### container_environment: List[`ContainerEnvironmentEntryDto`]<a id="container_environment-listcontainerenvironmententrydto"></a>

Environment settings for launching the container

##### models: List[`ArtifactDto`]<a id="models-listartifactdto"></a>

Optional set of models

##### container_image: `str`<a id="container_image-str"></a>

Optional custom container image

##### helm_chart: `str`<a id="helm_chart-str"></a>

Optional Helm Chart

##### helm_chart_service_name: `str`<a id="helm_chart_service_name-str"></a>

Helm Chart Service Name is required when helmChart property is specified 

##### resources: List[`ArtifactDto`]<a id="resources-listartifactdto"></a>

Optional set of resources

##### api_body_format: `str`<a id="api_body_format-str"></a>

Invocation request body format

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateFunctionRequest`](./nvidia_cloud_functions_python_sdk/type/create_function_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateFunctionResponse`](./nvidia_cloud_functions_python_sdk/pydantic/create_function_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/functions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.health.get_info`<a id="nvidiacloudfunctionshealthget_info"></a>

Get Health Information about this service

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = nvidiacloudfunctions.health.get_info()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthComponent`](./nvidia_cloud_functions_python_sdk/pydantic/health_component.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/health/**` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.queue_details.function_queues_details`<a id="nvidiacloudfunctionsqueue_detailsfunction_queues_details"></a>

Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
function_queues_details_response = (
    nvidiacloudfunctions.queue_details.function_queues_details(
        function_id="functionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

#### 🔄 Return<a id="🔄-return"></a>

[`GetQueuesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/get_queues_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/queues/functions/{functionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.queue_details.get_all_queues_details`<a id="nvidiacloudfunctionsqueue_detailsget_all_queues_details"></a>

Provides details of all the queues associated with the specified function.  If a function has multiple versions and they are all deployed, then the  response includes details of all the queues. If the specified function  is public, then Account Admin cannot perform this operation. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_queues_details_response = (
    nvidiacloudfunctions.queue_details.get_all_queues_details(
        function_id="functionId_example",
        version_id="versionId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### function_id: `str`<a id="function_id-str"></a>

Function id

##### version_id: `str`<a id="version_id-str"></a>

Function version id

#### 🔄 Return<a id="🔄-return"></a>

[`GetQueuesResponse`](./nvidia_cloud_functions_python_sdk/pydantic/get_queues_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/queues/functions/{functionId}/versions/{versionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `nvidiacloudfunctions.queue_details.get_queue_position_by_request_id`<a id="nvidiacloudfunctionsqueue_detailsget_queue_position_by_request_id"></a>

Using the specified function invocation request id, returns the estimated  position of the corresponding message up to 1000 in the queue. Requires a bearer token or an api-key with 'queue_details' scope in the HTTP  Authorization header. 

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_queue_position_by_request_id_response = (
    nvidiacloudfunctions.queue_details.get_queue_position_by_request_id(
        request_id="requestId_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

Function invocation request id

#### 🔄 Return<a id="🔄-return"></a>

[`GetPositionInQueueResponse`](./nvidia_cloud_functions_python_sdk/pydantic/get_position_in_queue_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/nvcf/queues/{requestId}/position` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
