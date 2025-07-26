# Standard Problems
from collections import deque

def print_tree(root):

    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

# print_tree(root)

def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    elif root.val == "-":
        return root.right.val - root.left.val
    else:
        return root.left.val * root.right.val
    
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

def right_vine(root):
    current = root
    result = []
    result.append(root.val)
    while current.right:
        result.append(current.right.val)
        current = current.right
    return result

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# def right_vine(root): COME BACK TO DO RECURSIVELY

# def count_leaves(root):  COME BACK LATER
#     current = root

#     if root is None:
#         return 0
    
#     if current:
    
#     if current.left is None and current.right is None:
#         current = root
#         return 1 + count_leaves(current.right)
    

#     # count = 0
#     # current = root

#     # while current.left:
        
def survey_tree(root):
    if root is None:
        return []
    
    left = survey_tree(root.left)
    right = survey_tree(root.right)
    
    return left + right + [root.val]

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))
    
        

