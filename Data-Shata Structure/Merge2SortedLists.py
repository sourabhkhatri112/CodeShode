class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.length += 1

    def __str__(self):
        if self.length == 0:
            return "List is empty"
        else:
            temp_node = self.head
            result = ""
            while temp_node is not None:
                result = result + str(temp_node.data) + "-->"
                temp_node = temp_node.next
            return result

    @classmethod
    def append_to_array(self, array, linked_list):
        if linked_list.length == 0:
            pass
        else:
            temp_node = linked_list.head
            while temp_node is not None:
                array.append(temp_node.data)
                temp_node = temp_node.next

            for i in range(len(array)-1):
                for j in range(len(array)-1):
                    if array[j] > array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
            return array

# This method merge 2 linked lists into Array, sort it & then put it again into combined linked list
    def merge_list(self, new_linked_list_1, new_linked_list_2):
        array = []
        LinkedList.append_to_array(array, new_linked_list_1)
        LinkedList.append_to_array(array, new_linked_list_2)
        return array

# This method merge 2 linked list in an unsorted combined list, and then sort that linked list
    def merge_linked_list(self, new_linked_list_1, new_linked_list_2, merged_linked_list):
        temp_node = new_linked_list_1.head
        while temp_node is not None:
            merged_linked_list.append(temp_node.data)
            temp_node = temp_node.next

        temp_node = new_linked_list_2.head
        while temp_node is not None:
            merged_linked_list.append(temp_node.data)
            temp_node = temp_node.next

        for i in range(merged_linked_list.length - 1):
            temp_node = merged_linked_list.head
            for j in range(merged_linked_list.length - 1):
                if temp_node.next is not None:
                    if temp_node.data > temp_node.next.data:
                        temp_node.data, temp_node.next.data = temp_node.next.data, temp_node.data
                        temp_node = temp_node.next
                    else:
                        temp_node = temp_node.next
        print(merged_linked_list)
        return 0


new_linked_list_1 = LinkedList()
new_linked_list_1.append(10)
new_linked_list_1.append(20)
new_linked_list_1.append(30)
new_linked_list_1.append(40)
print(new_linked_list_1)

new_linked_list_2 = LinkedList()
new_linked_list_2.append(5)
new_linked_list_2.append(10)
new_linked_list_2.append(15)
new_linked_list_2.append(20)
print(new_linked_list_2)
merged_linked_list = LinkedList()

print(LinkedList().merge_linked_list(new_linked_list_1, new_linked_list_2, merged_linked_list))

#   array = new_linked_list_2.merge_list(new_linked_list_1, new_linked_list_2)

