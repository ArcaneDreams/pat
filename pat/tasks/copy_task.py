#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from pat.context.context import Context
from pat.tasks.build_task import BuildTask
from pat.tasks.task import Task, depends_on


@depends_on(task_class_type=BuildTask)
class CopyTask(Task):
    """

    """

    def __init__(self):
        super(CopyTask, self).__init__()

    def on_can_run(self, context: Context) -> bool:
        """

        :param context:
        :return:
        """
        pass

    def on_before_run(self, context: Context):
        """

        :param context:
        :return:
        """
        pass

    def on_after_run(self, context: Context) -> Context:
        """

        :param context:
        :return:
        """
        pass

    def on_run(self, context: Context, *args, **kwargs):
        pass
