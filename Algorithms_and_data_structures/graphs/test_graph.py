import pytest
import numpy as np
from pipeline import read_input_as_np_array
from graph import Graph


@pytest.fixture
def graph_instance():
    return Graph(read_input_as_np_array("graf1.txt"))


def test_creating_graph_stucture(graph_instance):
    board = read_input_as_np_array("graf1.txt")
    assert len(graph_instance.graph_as_dict) == board.shape[0] * board.shape[1]


def test_distance_path(graph_instance):
    graph_instance.dijkstra()
    assert graph_instance.distance("R11C3") == 15
    graph_instance.dijkstra("R5C2")
    assert graph_instance.distance("R11C3") == 6
    graph_instance.dijkstra("R2C1")
    assert graph_instance.distance("R3C0") == 18


def test_results_without_dijkstra_calling(graph_instance):
    with pytest.raises(Exception):
        graph_instance.distance("R4C4")
    with pytest.raises(Exception):
        graph_instance.display_result("R4C4")
    with pytest.raises(Exception):
        graph_instance.show_raw_path("R4C4")


def test_raw_path(graph_instance):
    graph_instance.dijkstra("R1C1")
    assert graph_instance.show_raw_path("R2C1") == ["R1C1", "R2C1"]
    assert graph_instance.show_raw_path("R11C3") == [
        "R1C1",
        "R0C1",
        "R0C2",
        "R0C3",
        "R1C3",
        "R2C3",
        "R2C4",
        "R3C4",
        "R4C4",
        "R5C4",
        "R6C4",
        "R7C4",
        "R8C4",
        "R9C4",
        "R9C3",
        "R10C3",
        "R11C3",
    ]
