import numpy as np
from graph import Graph


def read_input_as_np_array(path) -> np.ndarray:
    board = []
    with open(path, "r") as file:
        for i, line in enumerate(file):
            board.append([])
            line = line.rstrip()
            for number in line:
                board[i].append(int(number))
    return np.array(board)


target_node = "R11C3"
r = read_input_as_np_array("graf1.txt")
graph = Graph(r)
graph.dijkstra("R1C1")
graph.show_raw_path(target_node)
graph.display_result(target_node)
print(graph.distance(target_node))
