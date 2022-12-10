""" Module to make factory for calls"""

from typing import Callable, Dict

# NOTE: this could also be a list in this example
callable_functions: Dict[str, Callable[[], None]] = {}

# NOTE: both of these functions just modify the callable functions available
def register(callable_name:str, callable_func: Callable[[], None]) -> None:
    callable_functions[callable_name] = callable_func
    return

def unregister(callable_name:str) -> None:
    callable_functions.pop(callable_name)
    return

# in the example from arjan codes, a create function was required to make a character ... 
# in this example that step is not needed