import os
import imp
from os.path import dirname, basename, isfile
import glob

class PluginLoader:
    __MainModule = '__init__'
    def __init__(self):
        super().__init__()
        self.plugins = []

    def load_from_directory(self, path):
        for item in os.listdir(path):
            location = os.path.join(path, item)
            if not os.path.isdir(location) or not self.__MainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(self.__MainModule, [location])
            print(info)

if __name__ == '__main__':
    loader = PluginLoader()
    loader.load_from_directory(os.path.abspath(dirname(__file__) + '/../plugins'))