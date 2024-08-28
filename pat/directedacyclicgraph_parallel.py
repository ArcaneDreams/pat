#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from pat.tasks.task import Task


class DirectedAcyclicGraphParallel:
    """
    Directed Acyclic Graph
    """

    def __init__(self):
        """

        """
        self.graph = {}

    def add_task(self, task: Task):
        """
        Add the task to the graph if it does not exist.
        :param task:
        :return:
        """
        if not task:
            raise ValueError("Task cannot be empty")
        if task not in self.graph:
            self.graph[task] = []

    def add_task_dependency(self, task: Task, dependent_task: Task):
        """
        Add a new dependency on a task.
        :param task:
        :param dependent_task:
        :return:
        """
        if not task:
            raise ValueError("Task cannot be empty")
        if not dependent_task:
            raise ValueError("Task cannot be empty")

        if task not in self.graph:
            self.add_task(task)
        if dependent_task not in self.graph:
            self.add_task(dependent_task)

        # Check if adding this edge creates a cycle
        if not self._creates_cycle(task, dependent_task):
            self.graph[task].append(dependent_task)
        else:
            raise ValueError("Adding this edge would create a cycle")

    def _creates_cycle(self, start_task, end_task):
        """
        Determine whether there is a cycle between the task specified and the end one.
        :param start_task:
        :param end_task:
        :return:
        """
        visited = set()
        return self._has_path(end_task, start_task, visited)

    def _has_path(self, current_task, target_task, visited_tasks):
        """
        Determine whether there is a path from the task specified to the target one.
        :param current_task:
        :param target_task:
        :param visited_tasks:
        :return:
        """
        if current_task == target_task:
            return True
        visited_tasks.add(current_task)
        for neighbor in self.graph.get(current_task, []):
            if neighbor not in visited_tasks:
                if self._has_path(neighbor, target_task, visited_tasks):
                    return True
        return False

    def topological_sort(self):
        """
        Perform topological sort and return tasks grouped by levels.
        Each level represents tasks that can be executed concurrently.
        """
        in_degree = {u: 0 for u in self.graph}  # Initialize in-degree of all vertices to 0
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1  # Count in-degrees

        queue = [u for u in in_degree if in_degree[u] == 0]  # Start with vertices with 0 in-degree
        levels = []  # List of lists, each inner list is a level of concurrently executable tasks

        while queue:
            next_queue = []
            current_level = []

            for u in queue:
                current_level.append(u)

                for v in self.graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        next_queue.append(v)

            levels.append(current_level)
            queue = next_queue

        return levels

    def __str__(self):
        return str(self.graph)
