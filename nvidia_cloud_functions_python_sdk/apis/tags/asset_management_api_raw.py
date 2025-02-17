# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_assets.post import CreateAssetAndUrlRaw
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_assets_asset_id.delete import DeleteAssetByIdRaw
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_assets.get import ListAssetsRaw
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_assets_asset_id.get import ShowDetailsRaw


class AssetManagementApiRaw(
    CreateAssetAndUrlRaw,
    DeleteAssetByIdRaw,
    ListAssetsRaw,
    ShowDetailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
