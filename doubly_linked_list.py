class Node:
    def __init__(self, val=0) -> None:
        self.val = val
        self.prev = None
        self.next = None

    def insert_after(self, v):
        v.next = self.next
        v.prev = self

        self.next.prev = v
        self.next = v

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

        self.prev = self.next = None
