from unittest import TestCase
from unittest.mock import patch, call
from linked_list import Node, LinkedList

class TestLinkedList(TestCase):
    def test_init_Node(self):
        new_node = Node(1)
        self.assertEqual(Node, type(new_node))

    def test_init_LinkedList(self):
        new_linked_list = LinkedList()
        self.assertEqual(LinkedList, type(new_linked_list))

    def test_insert(self):
        new_linked_list = LinkedList()
        new_linked_list.insert(1)
        self.assertIsNotNone(new_linked_list.head)

    @patch('builtins.print')
    def test_display(self, mock_print):
        new_linked_list = LinkedList()
        new_linked_list.insert(1)
        new_linked_list.insert(2)
        new_linked_list.insert(3)
        new_linked_list.insert(3)
        new_linked_list.insert(2)
        new_linked_list.insert(1)
        new_linked_list.display()
        self.assertEqual(
            mock_print.mock_calls,
            [call(1),call(2),call(3),call(3),call(2),call(1)]
        )

if __name__ == '__main__':
    unittest.main()