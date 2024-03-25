from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def reverse_string(input_str: str) -> str:
    stack = Stack()

    for char in input_str:
        stack.push(char)

    reversed_str = ''
    while stack.size() != 0:
        reversed_str += stack.pop()
    return reversed_str


def is_match(char1, char2):
    match_dict = {
        "}": "{",
        ")": "(",
        "]": "]",
    }
    return match_dict[char1] == char2


def is_balanced(input_str: str) -> bool:
    """A function that takes in a string and checks if each bracket in the string is opened and closed correctly."""
    stack = Stack()
    for char in input_str:
        if char == "(" or char == "{" or char == "[":
            stack.push(char)
        if char == ")" or char == "}" or char == "]":
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False
    return stack.size() == 0


if __name__ == '__main__':
    print(reverse_string('Hello World'))
    print(reverse_string("We would conquer COVID-19!!!"))
    print(is_balanced("(Hello World){}"))
    print(is_balanced("(Hello World"))
