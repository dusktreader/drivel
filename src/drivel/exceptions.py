"""
Provide custom exceptions.
"""

import buzz
from rich import traceback


# Enables prettified traceback printing via rich
traceback.install()


class DrivelException(buzz.Buzz):
    pass


class ThemeNotFound(DrivelException):
    pass


class ThemeReadError(DrivelException):
    pass
