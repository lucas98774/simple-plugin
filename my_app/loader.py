""" Module to load plugins """
from typing import Callable, List
import importlib

# NOTE: in this case the module interface is just a callable that accepts no args and prints something out
ModuleInterface = Callable[[], type(None)]

def load_module(name: str) -> ModuleInterface:
    """
    Function to load a module

    Parameters
    ----------
    name : str
        name of the module to load

    Returns
    -------
    module : Callable
        module that is a callable
    
    """
    return importlib.import_module(name)


def load_plugins(plugins: List[str]) -> None:
    """
    Function to load the plugins

    Parameters
    ----------
    plugins : List[str]
        names of the plugins to load (paths)
    
    Returns
    -------
    """
    for plugin_file in plugins:
        plugin = load_module(plugin_file)

        # NOTE: the plugin must do the registration bec there is must define 
        # what the callable is and the associated call
        # the register of the plugin will call the factory.register
        plugin.register()

    return



