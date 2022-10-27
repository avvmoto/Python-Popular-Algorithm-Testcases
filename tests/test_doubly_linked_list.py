from doubly_linked_list import Node  # The test framework
import unittest


class Test_TestDoublyLinkedList(unittest.TestCase):
    def test_doubly_linked_list(self):
        head = Node(0)
        tail = Node(0)

        head.next = tail
        tail.prev = head

        def read_by(start, next_node):
            out = []
            v = start
            while v:
                out.append(v.val)
                v = next_node(v)
            return out

        def test_read(msg, expected_from_head):
            got = read_by(head, lambda v: v.next)
            self.assertEqual(got, expected_from_head, msg=msg)

            got = read_by(tail, lambda v: v.prev)
            expected_from_head.reverse()
            self.assertEqual(got, expected_from_head, msg=msg)

        test_read("empty state", [0, 0])

        v1 = Node(1)
        head.insert_after(v1)
        test_read("insert before tail", [0, 1, 0])

        v1.insert_after(Node(2))
        test_read("insert before tail 2", [0, 1, 2, 0])

        v1.insert_after(Node(3))
        test_read("insert middle", [0, 1, 3, 2, 0])

        v1.remove()
        test_read("remove 1", [0, 3, 2, 0])

        tail.prev.remove()
        test_read("remove 2", [0, 3, 0])

        head.next.remove()
        test_read("remove 3", [0, 0])
