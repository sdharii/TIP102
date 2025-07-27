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

# print(find_flower(flower_field, "Lilac"))
# print(find_flower(flower_field, "Hibiscus"))

# Advanced Problem Set

def leftmost_path(root):
    if root is None:
        return []
    
    if not root.left:
        return [root.val]
    
    left = leftmost_path(root.left)
    return [root.val] + left
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

# print(leftmost_path(system_a))
# print(leftmost_path(system_b))

def leftmost_path2(root): # Same problem as above, just done iteratively
    result = []
    current = root
    result.append(current.val)
    
    while current.left:
        result.append(current.left.val)
        current = current.left
    return result

system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))
# print(leftmost_path2(system_a))
# print(leftmost_path2(system_b))

def count_species(node):
    if node is None:
        return 0
    
    return 1 + count_species(node.left) + count_species(node.right)
food_chain = TreeNode("Shark", 
                    TreeNode("Grouper", TreeNode("Conch"), TreeNode("Tang")),
                            TreeNode("Snapper", None, TreeNode("Zooplankton")))

# print(count_species(food_chain))

def explore_reef(root):
    if root is None:
        return []
    
    return [root.val] + explore_reef(root.left) + explore_reef(root.right)
reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))

# print(explore_reef(reef))

def get_decisions(node):
    if not node.left or not node.right:
        return node.val
    
    left = get_decisions(node.left)
    right = get_decisions(node.right)

    if node.val == "AND":
        return left and right
    elif node.val == "OR":
        return left or right
root = TreeNode("AND")
root.left = TreeNode("OR")
root.right = TreeNode("AND")
root.left.left = TreeNode(True)
root.left.right = TreeNode(False)
root.right.left = TreeNode(True)
root.right.right = TreeNode(False)
# print(get_decisions(root))

def is_uniform(root):
    if root is None:
        return True
    
    def search(node):
        if node is None:
            return True
        if node.val != root.val:
            return False
        return search(node.left) and search(node.right)

    return search(root)
coral = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1))
coral2 = TreeNode(1, TreeNode(2), TreeNode(1))

# print(is_uniform(coral))
# print(is_uniform(coral2))

def find_largest_pearl(root):
  if root is None:
      return 0
  
  left = find_largest_pearl(root.left)
  right = find_largest_pearl(root.right)

  largest = root.val

  if left > largest:
      largest = left
  if right > largest:
      largest = right
    
  return largest

    
oysters = TreeNode(7, TreeNode(6, TreeNode(5), TreeNode(1)), TreeNode(0))
oysters2 = TreeNode(1, TreeNode(0), TreeNode(1))

print(find_largest_pearl(oysters))
print(find_largest_pearl(oysters2))