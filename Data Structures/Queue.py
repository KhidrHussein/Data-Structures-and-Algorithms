import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


def place_orders(orders: list) -> None:
    order_queue = Queue()
    for order in orders:
        print(f"Placing order for: {order}")
        time.sleep(0.5)
        order_queue.enqueue(order)
    serve_order(order_queue)


def serve_order(orders: Queue) -> None:
    time.sleep(1)
    while orders.size() != 0:
        time.sleep(2)
        print(f"Serving order for: {orders.dequeue()}")


def print_binary_numbers(n: int) -> None:
    queue = Queue()
    queue.enqueue('1')

    for i in range(n):
        front_num: str = queue.front()
        print(front_num)
        queue.enqueue(front_num + '0')
        queue.enqueue(front_num + '1')
        # print(queue.buffer)  # For debugging purposes
        queue.dequeue()
        i += 1


if __name__ == '__main__':
    # A test_queue data structure can be implemented in python using a list, but this is not very efficient
    # due to the memory allocation issues due to the dynamic array of a list

    q = []

    # The test_queue is implemented by using the insert method of a list, we insert every new item at index zero.
    q.insert(0, 12)
    q.insert(0, 13)
    # print(q)

    # A more efficient method is using deque(double ended test_queue) from collections just as we've implemented
    # in stack. But this time, instead of appending, we're using 'appendleft' for adding items to the test_queue

    test_queue = deque()

    test_queue.appendleft(21)
    test_queue.appendleft(12)
    test_queue.appendleft(43)

    # print(test_queue.pop())  # output is 21

    # Testing our ordering threads
    customer_orders = ['pizza', 'pasta', 'samosa', 'biryani', 'burger']
    # place_orders(customer_orders)

    # Testing out the print binary numbers function
    print_binary_numbers(10)
