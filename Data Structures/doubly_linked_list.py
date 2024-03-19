class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, itr, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        print(f"There are {count} members in the linked list.")
        return count

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_forward(self):
        if self.head is None:
            print("Double linked list is empty")
            return
        itr = self.head
        dllstr = ''  # Double Linked List String
        while itr:
            dllstr += str(itr.data) + "--->"
            itr = itr.next
        print(dllstr)

    def print_backward(self):
        if self.head is None:
            print("Double linked list is empty")
            return
        last_node = self.get_last_node()
        itr = last_node
        dllstr = ''  # Double Link List String
        while itr:
            dllstr += str(itr.data) + "--->"
            itr = itr.prev
        print("Doubled linked list in reverse:", dllstr)


dll = DoublyLinkedList()
dll.insert_values(["apple", "banana", "cherry", "pear"])
dll.print_forward()
dll.print_backward()
