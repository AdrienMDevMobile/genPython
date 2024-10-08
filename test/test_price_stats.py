# coding: utf-8

"""
    Open Food Facts open-prices REST API

    Open Prices API allows you to add product prices

    The version of the OpenAPI document: 0.0.0 (api)
    Contact: contact@openfoodfacts.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.price_stats import PriceStats

class TestPriceStats(unittest.TestCase):
    """PriceStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceStats:
        """Test PriceStats
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceStats`
        """
        model = PriceStats()
        if include_optional:
            return PriceStats(
                price__count = 56,
                price__min = -100000000,
                price__max = -100000000,
                price__avg = -100000000
            )
        else:
            return PriceStats(
                price__count = 56,
                price__min = -100000000,
                price__max = -100000000,
                price__avg = -100000000,
        )
        """

    def testPriceStats(self):
        """Test PriceStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
