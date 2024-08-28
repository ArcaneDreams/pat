#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.
from pat.tasks.task import Task


class DirectedAcyclicGraph:
    """
    Directed Acyclic Graph
    """

    def __init__(self):
        """

        """
        self.task_graph = {}

    def add_task(self, task: Task):
        """
        Add a task
        :param task:
        :return:
        """
        if task not in self.task_graph:
            self.task_graph[task] = []

    def add_task_dependency(self, task: Task, dependent_task: Task):
        """
        Add a dependency between two tasks
        :param task:
        :param dependent_task:
        :return:
        """
        if task not in self.task_graph:
            self.add_task(task)
        if dependent_task not in self.task_graph:
            self.add_task(dependent_task)

        # Check if adding this edge creates a cycle
        if not self._creates_cycle(task, dependent_task):
            self.task_graph[task].append(dependent_task)
        else:
            raise ValueError("Adding this edge would create a cycle")

    def _creates_cycle(self, start_task, end_task):
        """

        :param start_task:
        :param end_task:
        :return:
        """
        visited = set()
        return self._has_path(end_task, start_task, visited)

    def _has_path(self, current_task, target_task, visited):
        """

        :param current_task:
        :param target_task:
        :param visited:
        :return:
        """
        if current_task == target_task:
            return True
        visited.add(current_task)
        for neighbor in self.task_graph.get(current_task, []):
            if neighbor not in visited:
                if self._has_path(neighbor, target_task, visited):
                    return True
        return False

    def topological_sort(self):
        """

        :return:
        """
        visited = set()
        stack = []

        for vertex in self.task_graph:
            if vertex not in visited:
                self._topological_sort_util(vertex, visited, stack)

        return stack[::-1]

    def _topological_sort_util(self, vertex, visited, stack):
        """

        :param vertex:
        :param visited:
        :param stack:
        :return:
        """
        visited.add(vertex)
        for neighbor in self.task_graph[vertex]:
            if neighbor not in visited:
                self._topological_sort_util(neighbor, visited, stack)
        stack.append(vertex)

    def __str__(self) -> str:
        """

        :return:
        """
        return str(self.task_graph)

# Example usage
# dag = DAG()
# dag.add_vertex('A')
# dag.add_vertex('B')
# dag.add_edge('A', 'B')
# dag.add_edge('A', 'C')
# dag.add_edge('B', 'D')
# dag.add_edge('C', 'D')
#
# print("Graph:", dag)
# print("Topological Sort:", dag.topological_sort())
