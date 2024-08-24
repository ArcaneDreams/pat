#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
import importlib
import inspect
import pkgutil
from typing import Type


def find_classes_with_base(package_name, base_class) -> list[Type]:
    """
    Finds and prints all classes in the specified package that inherit from the given base class.

    :param package_name: The name of the package to search.
    :param base_class: The base class to filter by.
    """
    if not package_name:
        raise ValueError("The package name specified is invalid or null")

    if not isinstance(package_name, str):
        raise ValueError("The package name must be a string")

    # Import the package
    package = importlib.import_module(package_name)

    if not package:
        raise ValueError("The package name could not be imported")

    classes_found: list[Type] = []

    # Iterate through the modules in the package
    for _, module_name, _ in pkgutil.iter_modules(package.__path__, package_name + '.'):
        try:
            # Import the module
            module = importlib.import_module(module_name)
            print(f"Scanning Module: {module_name}")

            # Iterate over the members of the module
            for name, member in inspect.getmembers(module, inspect.isclass):
                # Check if the class is a subclass of the specified base class and is defined in the module
                if issubclass(member, base_class) and member is not base_class and member.__module__ == module_name:
                    classes_found.append(member)
        except ImportError as e:
            print(f"Failed: Unable to import \"{module_name}\": {e}")

    return classes_found