import os
from os.path import splitext

from importlib.machinery import SourceFileLoader

from util import dprint as print

class PluginLoader:
    __MainModule = '__init__'

    def __init__(self):
        super().__init__()
        self.__plugins = {}

    def __hascallable(self, module, name):
        if (hasattr(module, name)):
            if (callable(getattr(module, name))):
                return True
        return False

    def load_from_directory(self, path):
        print('Loading plugins from', path)
        mod_name = lambda fp: '.' + splitext(fp)[0]

        for name in os.listdir(path):
            print('Attempting to load', mod_name(name))
            if name.endswith('.py') and not name.startswith('__'):
                n = mod_name(name)
                p = os.path.abspath(os.path.join(path, name))
                loader = SourceFileLoader(n, p)
                tmpmodule = loader.load_module()
                if self.__hascallable(tmpmodule, 'get_plugin'):
                    plugin = tmpmodule.get_plugin()
                    self.__plugins[name] = plugin


    def get_plugin_names(self):
        return self.__plugins.keys()

    def get_plugin(self, name):
        return self.__plugins[name]

if __name__ == '__main__':
    loader = PluginLoader()
    loader.load_from_directory(os.path.abspath(os.path.dirname(__file__) + '/plugins'))

    plugins = loader.get_plugin_names()
    print(plugins)

    for name in plugins:
        plugin = loader.get_plugin(name)
        print(name, plugin)
        print(name, plugin.do_upload("Foobar"))