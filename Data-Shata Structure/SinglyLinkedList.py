'''
No nodes --> So Head & Tail points to NONE & Length will be 0
class LinkedList:
    def __init__(self):
        self.value = None
        self.Next = None
        self.length = 0

new_Linked_List = LinkedList()
print(new_Linked_List.length);
'''

'''
Only 1 node --> So Point Head & Tail to this only node 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
print(LinkedList(10).head.value)
'''

# Every Node will have 1 Value & 1 Reference i.e (next)
# Everything will be handled by "append()" method so constructor simply initialises the Head & Tail instead of
# adding any new head or tail to it
'''
Inside Append() call the NODE method first to create it & then check for conditions below to fit inside the LinkedList 
Conditions to Add any Node
i) check head is empty --> Means no node is present in list then point both head & tail to this node
ii) head not empty --> Here add the last node's next to the new node i.e (Tail.next because tail will naturally be at the last node) 
& THEN MOVE THE TAIL TO THIS NEW NODE 
'''

'''
Inside __self__ : Pick one temp_node and point it to "head" & then iterate it gradually
If its not None --> Print its value & then check if its "NEXT" is none or Not.
If its NEXT is "non None" --> point temp_node to the next node and print its value again
Keep repeating until whole list is printed
'''

'''
class Node:
    def __init__(self, value):
        self.value = value
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
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, pos):
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for i in range(pos - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result = result + str(temp_node.value)
            if temp_node.next is not None:
                result = result + "->"
            temp_node = temp_node.next
        return result


new_linked_list = LinkedList()
new_linked_list.insert(10, 0)
new_linked_list.insert(20, -3)
new_linked_list.insert(40, -3)

print(new_linked_list)
'''


class Node:
    def __init__(self, value):
        self.value = value
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
            self.tail = new_node
        self.length += 1

    def insert(self, value, position):
        new_node = Node(value)
        if position < 0 or position > self.length:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for i in range(position - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1

    def pop_last(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -= 1

    def pop_mid(self, position):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev = self.head
            for i in range(position - 1):
                prev = prev.next
            popped_node = prev.next
            prev.next = popped_node.next
            popped_node.next = None
            self.length -= 1

    def reverse_list(self):
        if self.length == 0 or self.length == 1:
            return "Cannot reverse. Not enough elements"
        else:
            prev_node = None
            current_node = self.head
            while current_node is not None:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
            self.head = prev_node

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result = result + str(temp_node.value)
            if temp_node.next is not None:
                result = result + '->'
            temp_node = temp_node.next
        return result


new_Linked_List = LinkedList()

new_Linked_List.append(10)
new_Linked_List.append(20)
new_Linked_List.append(30)
new_Linked_List.append(40)
new_Linked_List.append(50)
print(new_Linked_List)
new_Linked_List.pop_mid(3)
print(new_Linked_List)
new_Linked_List.pop_mid(2)
print(new_Linked_List)
new_Linked_List.reverse_list()
print(new_Linked_List)
