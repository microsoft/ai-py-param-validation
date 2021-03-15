"""
(c) Microsoft. All rights reserved.
"""
import typing
from .validation_exception import ParameterValidationException


class ParameterTypeValidationException(ParameterValidationException):
    """
    Exception when the incoming type does not match the expected type
    """
    def __init__(self, func: typing.Callable[..., None], param: int, input_type: object, expected_type: object):
        err = "Arg type mismatch in func {} in module {}, parameter {} type does not match expected {} != {}.".format(
            func.__qualname__,
            func.__module__,
            param,
            str(input_type),
            str(expected_type)
        )
        super().__init__(err)
