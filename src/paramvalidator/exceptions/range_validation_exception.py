"""
(c) Microsoft. All rights reserved.
"""
import typing
from .validation_exception import ParameterValidationException


class ParameterRangeValidationException(ParameterValidationException):
    """
    Exception when incoming value is None but None is not allowed.
    """
    def __init__(self, func: typing.Callable[..., None], param: int, range : tuple, value : object):
        err = "Out of range parameter {} in func {} in module {} , value {} not in range {}.".format(
            param,
            func.__qualname__,
            func.__module__,
            str(value),
            range
        )
        super().__init__(err)
