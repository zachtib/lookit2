import os
from os.path import dirname
from importlib import import_module

import plugins

class PluginLoader:
    __MainModule = '__init__'
    def __init__(self):
        super().__init__()
        self.__plugins = {}

    def load_from_directory(self, path):
        for name in os.listdir(path):
            location = os.path.join(path, name)
            if not os.path.isdir(location) or not self.__MainModule + ".py" in os.listdir(location):
                continue
            tmpmodule = import_module('.' + name, 'plugins')
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
    loader.load_from_directory(os.path.abspath(dirname(__file__) + '/../plugins'))

    plugins = loader.get_plugin_names()
    print(plugins)

    for name in plugins:
        plugin = loader.get_plugin(name)
        print(plugin)
        print(plugin.do_upload("Foobar"))