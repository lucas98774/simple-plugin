""" Simple Core Process """
import pathlib

from my_app import factory, loader

def hellworld() -> None:
    print("Hellworld (from the main function)")
    return

def builtin_call() -> None:
    print('Hello! I am a built in function! I am the best')
    return

def main():
    """ Main Function """

    # load built in calls
    factory.register('hello world', hellworld)
    factory.register('built in call', builtin_call)

    # load plugins
    plugin_prefix = './plugins'
    plugin_paths = [thing.stem for thing in pathlib.Path(plugin_prefix).iterdir() if thing.is_file()]
    plugin_paths = [path for path in plugin_paths if not path.startswith('__')]
    # print(plugin_paths)
    plugin_paths = [f'plugins.{path}' for path in plugin_paths]
    # print(plugin_paths)
    loader.load_plugins(plugin_paths)

    # execute all
    for name, call in factory.callable_functions.items():
        print(f'Calling {name}')
        call()

    return

if __name__ == '__main__':
    main()