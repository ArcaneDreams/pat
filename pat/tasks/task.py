#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from __future__ import annotations

import abc
from typing import Callable, Type

from pat.context.context import Context


def task(*, name: str, depends_on=None) -> Callable:
    """

    :param name:
    :param depends_on:
    :return:
    """
    if name is None or not isinstance(name, str):
        raise ValueError("The name is invalid or null")

    def wrapper_task_func():
        pass

    return wrapper_task_func()


def depends_on(*, task_definition: Type[Task] | str):
    """

    :param task_definition:
    :return:
    """
    if task_definition is None:
        raise ValueError("The task specified is invalid or null")
    return


class Task(abc.ABC):
    """

    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def on_can_run(self, context: Context) -> bool:
        """

        :param context:
        :return:
        """
        return False

    @abc.abstractmethod
    def on_before_run(self, context: Context):
        """

        :param context:
        :return:
        """
        if context is None:
            raise ValueError("The context specified is invalid or null")
        pass

    @abc.abstractmethod
    def on_after_run(self, context: Context) -> Context:
        pass

    @abc.abstractmethod
    def on_run(self, context: Context, *args, **kwargs):
        pass

    def run(self, context: Context, *args, **kwargs):
        pass

    def _can_run(self, context: Context) -> bool:
        return self.on_can_run(context)

    def _before_run(self, context: Context):
        return self.on_before_run(context)
