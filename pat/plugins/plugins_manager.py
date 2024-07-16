#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
import os
import sys
from importlib.metadata import entry_points


class PluginsManager(object):
    """
    Manager class for handling the instantiation and usage of plugins in the tool
    """
    def __init__(self):
        """
        The base constructor
        """
        pass

    def find_plugins(self):
        """
        Find plugins based on installed packages under site-packages
        :return:
        """
        discovered_plugins = entry_points(group='pat.plugins')
        if not discovered_plugins:
            raise ValueError("The entrypoints retrieved are invalid or null")

        for plugin in discovered_plugins:
            if not plugin:
                raise ValueError("The plugin found is invalid or null")

    def load_plugins_from_paths(self, *paths):
        """

        :param paths:
        :return:
        """
        if not paths:
            raise ValueError("The paths specified are invalid or null")

        for path in paths:
            if not path:
                raise ValueError("The path is invalid or null")
            if not os.path.exists(path):
                raise IOError("The path specified could not be found {}".format(path))
