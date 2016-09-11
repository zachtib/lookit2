import os
import re
from importlib import import_module
from importlib.machinery import SourceFileLoader
from os.path import dirname, splitext

class PluginLoader:
    __MainModule = '__init__'
    def __init__(self):
        super().__init__()
        self.__plugins = {}

    def load_from_directory(self, path):
        print('Loading plugins from', path)
        mod_name = lambda fp: '.' + splitext(fp)[0]

        for name in os.listdir(path):
            print('Attempting to load', mod_name(name))
            if name.endswith('.py') and not name.startswith('__'):
                n = mod_name(name)
                p = os.path.abspath(os.path.join(path, name))
                print(n, p)
                loader = SourceFileLoader(n, p)
                tmpmodule = loader.load_module()
                if hasattr(tmpmodule, 'get_plugin'):
                    if (callable(tmpmodule.get_plugin)):
                        self.__plugins[name] = tmpmodule.get_plugin()
                    else:
                        print(name, 'module get_plugin is not callable')
                else:
                    print(name, 'has no attribute get_plugin')

    def get_plugin_names(self):
        return self.__plugins.keys()

    def get_plugin(self, name):
        return self.__plugins[name]

if __name__ == '__main__':
    loader = PluginLoader()
    loader.load_from_directory(os.path.abspath(dirname(__file__) + '/plugins'))

    plugins = loader.get_plugin_names()
    print(plugins)

    for name in plugins:
        plugin = loader.get_plugin(name)
        print(plugin)
        print(plugin.do_upload("Foobar"))