from pat.tasks.task import Task


class DAG:
    """
    Directed Acyclic Graph
    """
    def __init__(self):
        """

        """
        self.graph = {}

    def add_vertex(self, task: Task):
        """

        :param task:
        :return:
        """
        if task not in self.graph:
            self.graph[task] = []

    def add_edge(self, task: Task, dependent_task: Task):
        """

        :param task:
        :param dependent_task:
        :return:
        """
        if task not in self.graph:
            self.add_vertex(task)
        if dependent_task not in self.graph:
            self.add_vertex(dependent_task)

        # Check if adding this edge creates a cycle
        if not self._creates_cycle(task, dependent_task):
            self.graph[task].append(dependent_task)
        else:
            raise ValueError("Adding this edge would create a cycle")

    def _creates_cycle(self, start_vertex, end_vertex):
        """

        :param start_vertex:
        :param end_vertex:
        :return:
        """
        visited = set()
        return self._has_path(end_vertex, start_vertex, visited)

    def _has_path(self, current_vertex, target_vertex, visited):
        """

        :param current_vertex:
        :param target_vertex:
        :param visited:
        :return:
        """
        if current_vertex == target_vertex:
            return True
        visited.add(current_vertex)
        for neighbor in self.graph.get(current_vertex, []):
            if neighbor not in visited:
                if self._has_path(neighbor, target_vertex, visited):
                    return True
        return False

    def topological_sort(self):
        """

        :return:
        """
        visited = set()
        stack = []

        for vertex in self.graph:
            if vertex not in visited:
                self._topological_sort_util(vertex, visited, stack)

        return stack[::-1]

    def _topological_sort_util(self, vertex, visited, stack):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._topological_sort_util(neighbor, visited, stack)
        stack.append(vertex)

    def __str__(self):
        return str(self.graph)


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
