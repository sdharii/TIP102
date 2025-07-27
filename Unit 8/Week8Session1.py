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

def right_vine2(root): # This is the same as the prev problem, just done recursively
    if root.right is None:
        return [root.val]
    
    right = right_vine(root.right)
    return [root.val] + right

# print(right_vine2(ivy1))
# print(right_vine2(ivy2))


def count_leaves(root):  
    if root is None:
        return 0
    
    if root.right is None and root.left is None:
        return 1 
    
    left = count_leaves(root.left)
    right = count_leaves(root.right)

    return left + right #returns amount of leafs
oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
# print(count_leaves(oak1))
# print(count_leaves(oak2)) 
        
def survey_tree(root):
    if root is None:
        return []
    
    left = survey_tree(root.left)
    right = survey_tree(root.right)
    
    return left + right + [root.val]

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))

def harvest_berries(root, threshold):
    if root is None:
        return 0
    
    left = harvest_berries(root.left, threshold)
    right = harvest_berries(root.right, threshold)

    if root.val > threshold:
        return root.val + left + right
    else:
        return left + right 
bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))

def find_flower(root, flower):
    if root is None:
        return False
  
    if root.val == flower:
        return True
    
    return find_flower(root.left, flower) or find_flower(root.right, flower)


flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                                TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))
print(find_flower(flower_field, "Hibiscus"))
