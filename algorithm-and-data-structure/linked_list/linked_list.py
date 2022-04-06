class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_begining(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        is_item_found = False

        if current != None:
            if current.data == data:
                is_item_found = True
                self.head = current.next

            if is_item_found == False:
                while current.next:
                    next = current.next
                    if next.data == data:
                        current.next = next.next
                        is_item_found = True
                        break
                    current = current.next

        if is_item_found == False:
            print("Item " + str(data) + " not found!")


    def display(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_begining(1)
    linked_list.insert_at_begining(2)
    linked_list.insert_at_begining(3)
    linked_list.display()