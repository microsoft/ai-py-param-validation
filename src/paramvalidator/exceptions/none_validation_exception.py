"""
(c) Microsoft. All rights reserved.
"""
import typing
from .validation_exception import ParameterValidationException


class ParameterNoneValidationException(ParameterValidationException):
    """
    Exception when incoming value is None but None is not allowed.
    """
    def __init__(self, func: typing.Callable[..., None], param: int):
        err = "Unexpected None value found in func {} in module {}, parameter {}.".format(
            func.__qualname__,
            func.__module__,
            param
        )
        super().__init__(err)
