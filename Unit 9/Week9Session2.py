# Standard Problem Set

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


def height(node):
        if node is None:
            return 0
        
        return 1 + max(height(node.left), height(node.right))
        
def is_balanced(display):

    if not display:
        return True
    
    leftHeight = height(display.left)
    rightHeight = height(display.right)
    
    if abs(leftHeight - rightHeight) > 1:
        return False
    
    return is_balanced(display.left) and is_balanced(display.right)
baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
display1 = build_tree(baked_goods)
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


# print(is_balanced(display1)) 
# print(is_balanced(display2))  

def sum_each_days_orders(orders):
    if orders is None:
        return []
    
    queue = []
    result = []

    queue.append(orders)
    current_level = 0

    while queue:
        len_queue = len(queue)
        result.append([])

        for _ in range(len_queue):
            node = queue.pop(0)
            result.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        current_level += 1
    return result
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

# print(sum_each_days_orders(orders))

def mirror_tree(root):
    if not root:
        return []
    
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)

    return root
body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)
# print_tree(mirror_tree(vampire))
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)
# print_tree(mirror_tree(spooky_tree)) 

def max_pumpkins_path(root):
    if not root:
        return []
    
    bestPath = []
    max_sum = float('-inf')

    #helper
    def dfsHelper(node, path, total):
        nonlocal max_sum, bestPath

        if not node:
            return
        
        path.append(node.val)
        total += node.val

        if not node.left and not node.right:
            if total > max_sum:
                max_sum = total
                bestPath = list(path)

        dfsHelper(node.left, path, total)
        dfsHelper(node.right, path, total)

        path.pop()
    dfsHelper(root, [], 0)
    return bestPath
pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
root1 = build_tree(pumpkin_quantities)
pumpkin_quantities = [12,3, 8, 4, 50, None, 10]
root2 = build_tree(pumpkin_quantities)
# print(max_pumpkins_path(root1)) 
# print(max_pumpkins_path(root2))

def largest_pumpkins(pumpkin_patch):
    if not pumpkin_patch:
        return []
    
    result = []
    queue = deque([pumpkin_patch])

    while queue:
        levels = len(queue)
        max_value = float('-inf')

        for _ in range(levels):
            node = queue.popleft()
            max_value = max(max_value, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(max_value)

    return result
pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)

# print(largest_pumpkins(pumpkin_patch))

def count_clusters(hotel):
    def dfs(node, theme):
        if not node or (id(node)) in visited or node.val != theme:
            return
        
        visited.add(id(node))
        dfs(node.left, theme)
        dfs(node.right, theme)
    visited = set()
    clusterCount = 0

    def traverse(node):
        nonlocal clusterCount
        if not node:
            return
        if (id(node)) not in visited:
            dfs(node, node.val)
            clusterCount += 1
        traverse(node.left)
        traverse(node.right)
    traverse (hotel)
    return clusterCount
themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
hotel = build_tree(themes)

print(count_clusters(themes))