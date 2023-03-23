from tree import Tree
from copy import deepcopy
import sys

sys.setrecursionlimit(500000)


class BST(Tree):
    def __init__(self, key, val=None, size=1):
        super().__init__(key=key, val=val, size=size)

    def insert(self, key, val=None):
        if key is None:
            raise Exception(f"Pass None as Key, key")
        if val is None:
            val = key
        if self is None:
            return BST(key=key, val=val, size=1)
        if key < self.key:
            self.left = BST.insert(self.left, key, val)
        elif key > self.key:
            self.right = BST.insert(self.right, key, val)
        else:
            self.value = val
        tmp_size = 1
        if self.left:
            tmp_size += self.left.size
        if self.right:
            tmp_size += self.right.size
        self.size = tmp_size
        return self

    def delete(self, key):
        if self is None:
            raise Exception(f"This node does not exists, that means that key: {key} does not exist in this tree")
        if self.key > key:
            self.left = BST.delete(self.left, key)
        elif self.key < key:
            self.right = BST.delete(self.right, key)
        else:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            tmp = deepcopy(self)
            self.rebuild_node(BST._min(tmp.right))
            self.right = BST._delete_min(tmp.right)
            self.left = tmp.left
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size
        return self
