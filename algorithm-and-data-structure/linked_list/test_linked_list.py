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

    @patch('builtins.print')
    def test_delete_found_on_the_first_node(self, mock_print):
        new_linked_list = LinkedList()
        new_linked_list.insert(1)
        new_linked_list.insert(2)
        new_linked_list.insert(3)
        new_linked_list.delete(1)
        new_linked_list.display()
        self.assertEqual(
            mock_print.mock_calls,
            [call(2),call(3)]
        )

    @patch('builtins.print')
    def test_delete_found_on_the_middle_node(self, mock_print):
        new_linked_list = LinkedList()
        new_linked_list.insert(1)
        new_linked_list.insert(2)
        new_linked_list.insert(3)
        new_linked_list.delete(2)
        new_linked_list.display()
        self.assertEqual(
            mock_print.mock_calls,
            [call(1),call(3)]
        )

    @patch('builtins.print')
    def test_delete_found_on_the_last_node(self, mock_print):
        new_linked_list = LinkedList()
        new_linked_list.insert(1)
        new_linked_list.insert(2)
        new_linked_list.insert(3)
        new_linked_list.delete(3)
        new_linked_list.display()
        self.assertEqual(
            mock_print.mock_calls,
            [call(1),call(2)]
        )

    @patch('builtins.print')
    def test_delete_on_None_head(self, mock_print):
        new_linked_list = LinkedList()
        new_linked_list.delete(3)
        new_linked_list.display()
        self.assertEqual(
            mock_print.mock_calls,
            [call("Item 3 not found!")]
        )

    @patch('builtins.print')
    def test_delete_item_not_found(self, mock_print):
        new_linked_list = LinkedList()
        new_linked_list.insert(1)
        new_linked_list.insert(2)
        new_linked_list.insert(3)
        new_linked_list.delete(100)
        new_linked_list.display()
        self.assertEqual(
            mock_print.mock_calls,
            [call("Item 100 not found!"),call(1),call(2),call(3)]
        )

if __name__ == '__main__':
    unittest.main()