class TreeNode:  # This tree has been tweaked to accept both name and designations as input parameters. It can then
    # print the tree with either only the name, only the designation, or both names and designation
    def __init__(self, data: dict):
        self.data = data
        self.name = data["name"]
        self.designation = data["designation"]
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self) -> int:
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, spec):  # Take note of the recursion being used to print every child of every node
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if spec == "name":
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree("name")
        elif spec == "designation":
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree("designation")
        elif spec == "both":
            print(f"{prefix}{self.name} ({self.designation})")
            if self.children:
                for child in self.children:
                    child.print_tree("both")
        else:
            "Invalid input to the method!!!"


def build_management_tree():
    root = TreeNode({"name": "Nilupul",
                     "designation": "CEO"})

    cto = TreeNode({"name": "Chimnay",
                    "designation": "CTO"})
    infra_head = TreeNode({"name": "Vishwa",
                           "designation": "Infrastructure head"})
    cloud_manager = TreeNode({"name": "Dhaval",
                              "designation": "Cloud Manager"})
    app_manager = TreeNode({"name": "Ahbijit",
                            "designation": "Application Manager"})

    app_head = TreeNode({"name": "Aamir",
                         "designation": "Application head"})

    hr_head = TreeNode({"name": "Gels",
                        "designation": "HR Head"})
    rec_manager = TreeNode({"name": "Peter",
                            "designation": "Recruitment Manager"})
    pol_manager = TreeNode({"name": "Waqas",
                            "designation": "Policy Manager"})

    root.add_child(cto)
    root.add_child(hr_head)
    cto.add_child(infra_head)
    cto.add_child(app_head)
    hr_head.add_child(rec_manager)
    hr_head.add_child(pol_manager)
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("designation")  # prints only designation hierarchy
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
