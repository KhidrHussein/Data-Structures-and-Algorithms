class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):  # Take note of the recursion being used to print every child of every node
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    phone = TreeNode("Phone")
    tv = TreeNode("TV")

    laptop.add_child(TreeNode("MAC Air"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    phone.add_child(TreeNode("IPhone"))
    phone.add_child(TreeNode("Google Pixel"))
    phone.add_child(TreeNode("Vivo"))

    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    product_tree = build_product_tree()
    product_tree.print_tree()
