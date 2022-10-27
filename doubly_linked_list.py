from __future__ import annotations


class Node:
    """Node implements node of doubly linked list, which implements insert_after and remove.
    A node can store prev[Node], next[Node], val[int].
    """

    def __init__(self, val=0) -> None:
        self.val = val
        self.prev = None
        self.next = None

    def insert_after(self, v: Node):
        """insert_after inserts v[Node] after the node `self` in the doubly linked list.

        Args:
            v (Node): a node to be inserted.
        """
        v.next = self.next
        v.prev = self

        self.next.prev = v
        self.next = v

    def remove(self):
        """remove removes the node `self` from the doubly linked list."""
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next = None
        self.prev = None
