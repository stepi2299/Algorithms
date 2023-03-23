import pytest

from bst import BST
from avl import AVL

input_values = [7, 2, 11, 56, 1, 13, 3]


@pytest.fixture
def bst_instance():
    bst = BST(input_values[0])
    for i in input_values[1:]:
        bst.insert(i)
    bst.display()
    return bst


@pytest.fixture
def avl_instance():
    avl = AVL(input_values[0])
    for i in input_values[1:]:
        avl.insert(i)
    return avl


def test_bst_values(bst_instance):
    in_val = input_values.copy()
    tree_values = bst_instance.get_all_tree_values()
    assert len(tree_values) == len(in_val)
    assert tree_values.sort() == in_val.sort()


def test_avl_values(avl_instance):
    in_val = input_values.copy()
    tree_values = avl_instance.get_all_tree_values()
    assert len(tree_values) == len(input_values)
    assert tree_values.sort() == in_val.sort()


def test_bst_size(bst_instance):
    assert bst_instance.size == len(input_values)


def test_avl_size(avl_instance):
    assert avl_instance.size == len(input_values)


@pytest.mark.parametrize("val", [7, 2, 11, 56, 1, 13, 3])
def test_bst_get_val(bst_instance, val):
    if val in input_values:
        receive_val = bst_instance.get(val)
        assert receive_val == val
    else:
        with pytest.raises(Exception):
            receive_val = bst_instance.get(val)


@pytest.mark.parametrize("val", [7, 2, 11, 56, 1, 13, 3])
def test_avl_get_val(avl_instance, val):
    if val in input_values:
        receive_val = avl_instance.get(val)
        assert receive_val == val
    else:
        with pytest.raises(Exception):
            receive_val = avl_instance.get(val)


@pytest.mark.parametrize("val", [11, 111, 4, 1, -1])
def test_bst_insert_val(bst_instance, val):
    bst_instance.insert(val)
    in_val = input_values.copy()
    all_val = bst_instance.get_all_tree_values()
    if val in [1, 11]:
        assert len(all_val) == len(input_values)
        assert bst_instance.size == len(input_values)
    else:
        assert len(all_val) == len(input_values) + 1
        assert bst_instance.size == len(input_values) + 1
    in_val.append(val)
    assert in_val.sort() == all_val.sort()


def test_valid_place_for_values_bst(bst_instance):
    l = bst_instance.left
    assert l.left.key < l.key
    assert l.right.key > l.key
    r = bst_instance.right
    assert r.right.key > r.key
    bst_instance.insert(10)
    assert r.left.key == 10


def test_rebalance_avl(avl_instance):
    assert avl_instance.height == 3
    avl_instance.insert(10)
    assert avl_instance.height == 4


@pytest.mark.parametrize("val", [11, 111, 4, 1, -1])
def test_avl_insert_val(avl_instance, val):
    avl_instance.insert(val)
    in_val = input_values.copy()
    all_val = avl_instance.get_all_tree_values()
    if val in [1, 11]:
        assert len(all_val) == len(input_values)
        assert avl_instance.size == len(input_values)
    else:
        assert len(all_val) == len(input_values) + 1
        assert avl_instance.size == len(input_values) + 1
    in_val.append(val)
    assert in_val.sort() == all_val.sort()


@pytest.mark.parametrize("val", [7, 2, 11, 56, 1, 13, 3, 5])
def test_bst_delete_val(bst_instance, val):
    if val in input_values:
        bst_instance.delete(val)
        in_val = input_values.copy()
        all_val = bst_instance.get_all_tree_values()
        assert len(all_val) == len(input_values) - 1
        in_val.remove(val)
        assert in_val.sort() == all_val.sort()
    else:
        with pytest.raises(Exception):
            bst_instance.delete(val)


@pytest.mark.parametrize("val", [7, 2, 11, 56, 1, 13, 3, 5])
def test_avl_delete_val(avl_instance, val):
    if val in input_values:
        avl_instance.delete(val)
        in_val = input_values.copy()
        all_val = avl_instance.get_all_tree_values()
        assert len(all_val) == len(input_values) - 1
        in_val.remove(val)
        assert in_val.sort() == all_val.sort()
    else:
        with pytest.raises(Exception):
            avl_instance.delete(val)
