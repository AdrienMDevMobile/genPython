# coding: utf-8

"""
    Open Food Facts open-prices REST API

    Open Prices API allows you to add product prices

    The version of the OpenAPI document: 0.0.0 (api)
    Contact: contact@openfoodfacts.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class BlankEnum(str, Enum):
    """
    BlankEnum
    """

    """
    allowed enum values
    """
    EMPTY = ''

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BlankEnum from a JSON string"""
        return cls(json.loads(json_str))


