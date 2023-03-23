from tree import Tree
from copy import deepcopy
import sys

sys.setrecursionlimit(10000)


class AVL(Tree):
    def __init__(self, key, val=None, size=1, height=1):
        super().__init__(key=key, val=val, size=size)
        self.height = height

    def insert(self, key, val=None):
        if key is None:
            raise Exception(f"Pass None as Key, key")
        if val is None:
            val = key
        if self is None:
            return AVL(key=key, val=val, size=1)
        if key < self.key:
            self.left = AVL.insert(self.left, key, val)
        elif key > self.key:
            self.right = AVL.insert(self.right, key, val)
        else:
            self.value = val
        l_height = self.left.height if self.left else 0
        r_height = self.right.height if self.right else 0
        self.height = max(l_height, r_height) + 1
        tmp_size = 1
        if self.left:
            tmp_size += self.left.size
        if self.right:
            tmp_size += self.right.size
        self.size = tmp_size
        balance = self.get_balance()
        if not -2 < balance < 2:
            self.rebalance_tree(balance)
        return self

    def delete(self, key):
        if self is None:
            raise Exception(f"This node does not exists, that means that key: {key} does not exist in this tree")
        if self.key > key:
            self.left = AVL.delete(self.left, key)
        elif self.key < key:
            self.right = AVL.delete(self.right, key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            tmp = deepcopy(self)
            self.rebuild_node(AVL._min(tmp.right))
            self.right = AVL._delete_min(tmp.right)
            self.left = tmp.left
        l_height = self.left.height if self.left else 0
        r_height = self.right.height if self.right else 0
        self.height = max(l_height, r_height) + 1
        self.size = 1
        must_rebalance_subtree = False
        if self.left:
            self.size += self.left.size
            must_rebalance_subtree = True
        if self.right:
            self.size += self.right.size
            must_rebalance_subtree = True
        balance = self.get_balance()
        if not -2 < balance < 2:
            self.rebalance_tree(balance)
        if must_rebalance_subtree:
            update_height(self)
            rebalance_subtree(self)
        return self

    def get_balance(self):
        l_height = self.left.height if self.left else 0
        r_height = self.right.height if self.right else 0
        return r_height - l_height

    def rebalance_tree(self, root_balance):
        if root_balance > 2:
            self.right.rebalance_tree(root_balance - 1)
        if root_balance < -2:
            self.left.rebalance_tree(root_balance + 1)
        if root_balance == 2:
            if self.right.get_balance() == -1:
                new_child = right_rotation(self.right)
                self.right = new_child
            new_self = left_rotation(self)
            self.rebuild_node(new_self)
        else:
            if self.left.get_balance() == 1:
                new_child = left_rotation(self.left)
                self.left = new_child
            new_self = right_rotation(self)
            self.rebuild_node(new_self)

    def rebuild_node(self, node):
        super().rebuild_node(node)
        self.height = node.height


def right_rotation(node):
    old_root = deepcopy(node)
    old_branch = deepcopy(node.left)
    old_leaf = deepcopy(node.left.right)
    node, node.right, node.right.left = old_branch, old_root, old_leaf
    update_height(node)
    update_size(node)
    return node


def left_rotation(node):
    old_root = deepcopy(node)
    old_branch = deepcopy(node.right)
    old_leaf = deepcopy(node.right.left)
    node, node.left, node.left.right = old_branch, old_root, old_leaf
    update_height(node)
    update_size(node)
    return node


def update_height(node):
    if node.left:
        update_height(node.left)
    if node.right:
        update_height(node.right)
    if not node.left and not node.right:
        node.height = 1
        return
    l_height = node.left.height if node.left else 0
    r_height = node.right.height if node.right else 0
    node.height = max(l_height, r_height) + 1


def update_size(node):
    if node.left:
        update_size(node.left)
    if node.right:
        update_size(node.right)
    if not node.left and not node.right:
        node.size = 1
        return
    l_size = node.left.size if node.left else 0
    r_size = node.right.size if node.right else 0
    node.size = l_size + r_size + 1


def rebalance_subtree(root):
    if not root.left and not root.right:
        return
    balance = root.get_balance()
    if not -2 < balance < 2:
        root.rebalance_tree(balance)
    if root.left:
        rebalance_subtree(root.left)
    if root.right:
        rebalance_subtree(root.right)
