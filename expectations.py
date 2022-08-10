"""
Expectations that pertain to a single column and can be made more efficiently
"""

from abc import ABC
import enum
import json


class Expectation(ABC):

    EXPECTATION_TYPE = None

    @classmethod
    def make(cls, **kwargs):
        data = {
            "expectation_type": cls.EXPECTATION_TYPE,
            "kwargs": kwargs,
        }
        return data


class NotNull(Expectation):
    EXPECTATION_TYPE = "expect_column_values_to_not_be_null"


class InSet(Expectation):
    EXPECTATION_TYPE = "expect_column_values_to_be_in_set"


class Between(Expectation):
    EXPECTATION_TYPE = "expect_column_values_to_be_between"


class Regex(Expectation):
    EXPECTATION_TYPE = "expect_column_values_to_match_regex"


EXPECTATIONS = {
    'not_null': NotNull,
    'in_set': InSet,
    'between': Between,
    'regex': Regex,
}
