"""
(c) Microsoft. All rights reserved.
"""


class ParameterValidationException(Exception):
    """
    Base exception for parameter validation
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
