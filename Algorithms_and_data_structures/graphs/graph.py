import numpy as np
from pqdict import PQDict


class Graph:
    def __init__(self, board: np.ndarray):
        self.board = board
        self.dist = {}  # length of the shortest path from starting node to V node
        self.prev_on_path = (
            {}
        )  # predecessor V on shortest path from starting node to V node
        self.graph_as_dict = self.__create_graph_from_array(board)
        self.start_key = "R0C0"
        self.calculated_distance = False

    def __create_graph_from_array(self, board: np.ndarray) -> dict:
        height, width = board.shape
        graph = {}
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                values = []
                values.append(("val", value))
                if j - 1 >= 0:
                    values.append((f"R{i}C{j - 1}", board[i][j - 1]))
                if j + 1 < width:
                    values.append((f"R{i}C{j + 1}", board[i][j + 1]))
                if i - 1 >= 0:
                    values.append((f"R{i - 1}C{j}", board[i - 1][j]))
                if i + 1 < height:
                    values.append((f"R{i + 1}C{j}", board[i + 1][j]))
                graph[f"R{i}C{j}"] = values
                self.dist[f"R{i}C{j}"] = np.inf
        return graph

    def dijkstra(self, start_key: str = "R0C0"):
        queue = PQDict()
        queue[start_key] = 0
        self.dist[start_key] = 0
        self.start_key = start_key

        while len(queue) > 0:
            v, _ = queue.popitem()
            for neighbour, cost in self.graph_as_dict[v]:
                if cost == 0:
                    pass
                if neighbour == "val":
                    continue
                if (
                    not neighbour in self.dist
                    or self.dist[neighbour] > self.dist[v] + cost
                ):
                    self.dist[neighbour] = self.dist[v] + cost
                    self.prev_on_path[neighbour] = v
                    queue[neighbour] = self.dist[neighbour]
        self.calculated_distance = True

    def display_result(self, target_node: str):
        if not self.calculated_distance:
            raise Exception(
                f"You must call method 'dijkstra'. "
                f"Distance and optimal path from starting point was not calculated"
            )
        empty = []
        for i in range(self.board.shape[0]):
            empty.append([])
            for j in range(self.board.shape[1]):
                empty[i].append("-")
        path = self.show_raw_path(target_node)
        for node in path:
            col_idx = node.find("C")
            row = node[1:col_idx]
            col = node[col_idx + 1 :]
            empty[int(row)][int(col)] = str(self.board[int(row), int(col)])
        for line in empty:
            print(line)

    def show_raw_path(self, target_node: str):
        if not self.calculated_distance:
            raise Exception(
                f"You must call method 'dijkstra'. "
                f"Distance and optimal path from starting point was not calculated"
            )
        path = []
        current = target_node
        path.append(current)
        while current != self.start_key:
            current = self.prev_on_path[current]
            path.insert(0, current)
        return path

    def distance(self, target_node: str):
        if not self.calculated_distance:
            raise Exception(
                f"You must call method 'dijkstra'. "
                f"Distance and optimal path from starting point was not calculated"
            )
        return self.dist[target_node]
