"""
(c) Microsoft. All rights reserved.
"""
import typing
from .validation_exception import ParameterValidationException


class ParameterCountValidationException(ParameterValidationException):
    """
    Exception when an expected kwarg is not present
    """
    def __init__(self, func: typing.Callable[..., None], recieved: int):
        err = "Expected {} args in func {} in module {} but {} were given.".format(
            func.__code__.co_argcount,
            func.__qualname__,
            func.__module__,
            recieved
        )
        super().__init__(err)
