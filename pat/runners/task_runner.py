#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
import abc

from pat.helpers.helpers_type import find_classes_with_base_in_package
from pat.tasks.task import Task


class TaskRunner(abc.ABC):
    """
    Class responsible for loading task types and running afterwards.
    """

    def __init__(self, *, module_paths: list[str]):
        """

        :param module_paths:
        """
        if not module_paths:
            raise ValueError('module_paths cannot be empty')
        self.module_paths = module_paths
        self.load_tasks()

    def load_tasks(self):
        """

        :return:
        """
        types = find_classes_with_base_in_package(__package__, Task)
        return

    def add_targets(self, *targets):
        """

        :param targets:
        :return:
        """
        if not targets:
            raise ValueError("The targets are invalid or null")
        if not any(targets):
            raise ValueError("The targets are invalid or null")
        return

    def run(self):
        """
        Run the task runner
        :return:
        """

        try:
            self.on_run()
        except:
            pass
        pass

    @abc.abstractmethod
    def on_run(self):
        pass
