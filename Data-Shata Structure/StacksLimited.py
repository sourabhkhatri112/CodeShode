class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(i) for i in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "Stack is already full"
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "No Element"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "No element to peek"
        else:
            print(self.list[len(self.list) - 1])

    def delete(self):
        self.list = None


custom_stack = Stack(4)
custom_stack.push(10)
custom_stack.push(20)
custom_stack.push(30)
custom_stack.push(40)
custom_stack.push(50)   # Wont be filled as stack is full already
custom_stack.push(60)   # Wont be filled as stack is full already
custom_stack.pop()
print(custom_stack)
