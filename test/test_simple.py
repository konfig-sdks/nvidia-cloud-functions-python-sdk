# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

import unittest

import os
from pprint import pprint
from nvidia_cloud_functions_python_sdk import NvidiaCloudFunctions

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        nvidiacloudfunctions = NvidiaCloudFunctions(
        )
        self.assertIsNotNone(nvidiacloudfunctions)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
