#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from __future__ import annotations

import abc
from typing import Callable, Type

import functools

from pat.context.context import Context


def task(func, *, name: str, depends_on=None) -> Callable:
    """

    :param name:
    :param depends_on:
    :return:
    """
    if name is None or not isinstance(name, str):
        raise ValueError("The name is invalid or null")

    @functools.wraps(func)
    def wrapper_task_func():
        return func()

    return wrapper_task_func


def depends_on(cls, *, task_class_type: Type[Task] | str) -> Callable:
    """

    :param cls:
    :rtype: object
    :param task_class_type:
    :return:
    """
    if not cls:
        raise ValueError("The class is invalid or null")
    if task_class_type is None:
        raise ValueError("The task specified is invalid or null")

    original_init = cls.__init__

    def depends_on_func_wrapper(cls):
        """

        :param cls:
        :return:
        """

        def new_init(self, *args, **kwargs):
            """

            :param self:
            :param args:
            :param kwargs:
            :return:
            """
            original_init(self, *args, **kwargs)
            if task_class_type not in cls.__bases__:
                return

        return new_init

    return depends_on_func_wrapper


class Task(abc.ABC):
    """
    Defines the base task implementation
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
