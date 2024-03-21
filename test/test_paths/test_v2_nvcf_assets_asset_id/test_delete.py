# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

import unittest
from unittest.mock import patch

import urllib3

import nvidia_cloud_functions_python_sdk
from nvidia_cloud_functions_python_sdk.paths.v2_nvcf_assets_asset_id import delete
from nvidia_cloud_functions_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2NvcfAssetsAssetId(ApiTestMixin, unittest.TestCase):
    """
    V2NvcfAssetsAssetId unit test stubs
        Delete Asset
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
