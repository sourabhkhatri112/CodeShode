class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def traverse_node(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traverse(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev

    def search_method(self, value):
        temp_node = self.head
        position = 0
        while temp_node is not None:
            if temp_node.value == value:
                print("Value found at position: ", position)
                break
            temp_node = temp_node.next
            position += 1

    def __str__(self):
        if self.head is None:
            return "List is empty"
        else:
            temp_node = self.head
            result = ""
            while temp_node is not None:
                result = result + str(temp_node.value) + "<-->"
                temp_node = temp_node.next
            return result


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.reverse_traverse()
print(new_linked_list)
new_linked_list.search_method(20)
