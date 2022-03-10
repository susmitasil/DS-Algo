class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self):
        print(" "*self.get_level()*3+"|__",  self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_2(self, level=0):
        print(" "*level*3+"|__",  self.data)
        if self.children:
            for child in self.children:
                child.print_tree_2(level+1)

if __name__ == "__main__":
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    mobiles =TreeNode("Mobiles")
    tv= TreeNode("TV")

    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Dell"))

    mobiles.add_child(TreeNode("Nokia"))
    mobiles.add_child(TreeNode("Redmi"))
    mobiles.add_child(TreeNode("Apple"))

    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Onida"))

    root.add_child(laptop)
    root.add_child(mobiles)
    root.add_child(tv)

    # root.print_tree()
    root.print_tree_2()
    print(tv.get_level())