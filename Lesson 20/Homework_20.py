
# --------------------TASK DESCRIPTIONS-------------------------------
# ------Task1: Binary Tree - functions printLeafNodes & countEdges



# -----------GLOBAL Variables----------------
global Task_list
Task_list = []


# -----------MAIN CLASSES----------------
class Task():
    def __init__(self, name):
        assert isinstance(name, str), "'name' must be a string!!!"
        self.Function = object
        Task_list.append(self)
        self.name = f"Task{Task_list.index(self) + 1}: {name}"

    def __str__(self):
        return self.name

    def write_function(self, object101):
        self.Function = object101

    def __call__(self):
        Looper = "y"
        while Looper == "y":
            self.Function()
            Replay = input("\nWant to try again? Enter 'y' if yes or ANY other key to continue: ")
            if Replay == "y":
                continue
            else:
                Looper = Replay


# -----------CUSTOM FUNCTIONS----------------

# -----------TASK OBJECTS----------------

Task01 = Task("Binary Tree - functions printLeafNodes & countEdges")



def task1_body():
    # ----------------Task Variables----------------------------------
    # ----------------Task Classes------------------------------------
    class TreeNode():
        def __init__(self,key):
            self.key=key
            self.left = None
            self.right = None
    class BinaryTree:
        def __init__(self):
            self.root = None
            self.edge_count = 0
        def insert(self,key):
            self.root = self._insert(self.root, key)
        def _insert(self, node, key):
            if node is None:
                return TreeNode(key)
            if key < node.key:
                node.left = self._insert(node.left,key)
            elif key > node.key:
                node.right = self._insert(node.right,key)
            return node
        def print_Leafs(self,node):
            if node:
                if node.left is None and node.right is None:
                    print(node.key, end=" -> ")
                if node.left:
                    self.print_Leafs(node.left)
                if node.right:
                    self.print_Leafs(node.right)
            else:
                return
        def count_Edges(self,node):
            if node:
                if node.left:
                    self.edge_count += 1
                    self.count_Edges(node.left)
                if node.right:
                    self.edge_count += 1
                    self.count_Edges(node.right)

            return self.edge_count

    # ----------------Task Functions----------------------------------
    # ----------------Task BODY---------------------------------------
    binTree = BinaryTree()
    binTree.insert(11)
    binTree.insert(6)
    binTree.insert(8)
    binTree.insert(12)
    binTree.insert(9)
    binTree.insert(14)
    binTree.insert(35)
    binTree.insert(3)
    binTree.insert(13)
    print("Leaf node keys: ", end ="")
    binTree.print_Leafs(binTree.root)
    print(f"\nCount of edges is: {binTree.count_Edges(binTree.root)}")
Task01.write_function(task1_body)


# -------------MAIN CODE---------------------------------------------------------------------

for task in Task_list:
    Task_status = input(f"\nDo you want to do - {task}? \n(Enter 'y' for YES or any key for NO) ")
    if Task_status == "y":
        task()
    else:
        print(f" \n{task} - Skipped")
print("\n ---THE END---")
