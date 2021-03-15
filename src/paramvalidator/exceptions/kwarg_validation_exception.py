"""
(c) Microsoft. All rights reserved.
"""
import typing
from .validation_exception import ParameterValidationException


class ParameterKwargValidationException(ParameterValidationException):
    """
    Exception when an expected kwarg is not present
    """
    def __init__(self, func: typing.Callable[..., None], expected: str):
        err = "Missing required kwarg - {} - in func {} in module {}.".format(
            expected,
            func.__qualname__,
            func.__module__
        )
        super().__init__(err)
