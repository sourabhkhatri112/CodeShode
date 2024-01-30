class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(i) for i in self.list]
        return ' '.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[0]

    def delete(self):
        self.list = None


custom_list = Queue()
custom_list.enqueue(10)
custom_list.enqueue(20)
custom_list.enqueue(30)
custom_list.enqueue(40)
print(custom_list)
custom_list.dequeue()
print(custom_list)
