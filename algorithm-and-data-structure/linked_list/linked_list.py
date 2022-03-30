from time import sleep


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, data):
        current = self.head
        isItemFound = False

        if current != None:
            if current.data == data:
                isItemFound = True
                self.head = current.next

            if isItemFound == False:
                while current.next:
                    next = current.next
                    if next.data == data:
                        current.next = next.next
                        isItemFound = True
                        break
                    current = current.next

        if isItemFound == False:
            print("Item " + str(data) + " not found!")


    def display(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.delete(10)
    linked_list.display()