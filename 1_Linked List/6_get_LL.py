class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
        def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

        def print_list(self):
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

        def append(self, value):
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

        def get(self, index):
            if index < 0 or index >= self.length:
                return "Index out of range"
            else:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                return temp
        
my_linked_list = LinkedList(11)

my_linked_list.append(22)
my_linked_list.append(33)
my_linked_list.append(44)

print(my_linked_list.get(3))
