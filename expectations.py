"""
Expectations that pertain to a single column and can be made more efficiently
"""

from abc import ABC
import enum
import json


EXPECTATIONS = {
    'not_null': 'expect_column_values_to_not_be_null',
    'in_set': 'expect_column_values_to_be_in_set',
    'not_in_set': 'expect_column_values_to_not_be_in_set',
    'between': 'expect_column_values_to_be_between',
    'regex': 'expect_column_values_to_match_regex',
}


def make(friendly_expectation_type, **kwargs):
    ge_expectation_type = EXPECTATIONS.get(friendly_expectation_type)
    assert ge_expectation_type is not None
    data = {
        "expectation_type": ge_expectation_type,
        "kwargs": kwargs,
    }
    return data
