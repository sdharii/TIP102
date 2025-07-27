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

def count_odd_splits(root):
    if root is None:
        return 0
    
    left = count_odd_splits(root.left)
    right = count_odd_splits(root.right)

    if root.val % 2 == 1:
        return 1 + left + right
    if root.val % 2 == 0:
        return 0 + left + right
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

def find_flower(inventory, name):
    if not inventory:
        return False
    
    if inventory.val == name:
        return True
    
    return find_flower(inventory.left, name) or find_flower(inventory.right, name)
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    
    if collection.val == name:
        return collection
    
    if collection.val < name:
        collection.right = add_plant(collection.right, name)
    else:
        collection.left = add_plant(collection.left, name)
    
    return collection
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)
# print_tree(add_plant(collection, "Aloe"))

# def sort_plants(collection):
#     if not collection:
#         return []
#     else:
#         left = [sort_plants(collection.left)]
#         right = [sort_plants(collection.right)]
#         return left + [(collection.key, collection.val)] + right
# values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
# collection = build_tree(values)

# print(sort_plants(collection))

class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant price
        self.val = val      # Plant name
        self.left = left
        self.right = right

def pick_plant(root, budget):
    flower = None

    while root:
        if budget > root.val:
            flower = root
            root = root.right
        else:
            root = root.left

    if flower is not None:
        return flower.key
    else:
        return None

values = [(50, "Fiddle Leaf Fig"), (25, "Monstera"), (70, "Snake Plant"), (15, "Aloe"), 
            (40, "Pothos"), (60, "Fern"), (80, "ZZ Plant")]
inventory = build_tree(values)

# print(pick_plant(inventory, 50)) 
# print(pick_plant(inventory, 25)) 
# print(pick_plant(inventory, 15)) 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    if not collection: 
        return None
    
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        if not collection.left and not collection.right: # No Children
            return None
        # One Child
        elif not collection.left:
            return collection.right
        elif not collection.right:
            return collection.left
        else:
            predecessor = collection.left
            while predecessor.right:
                predecessor = predecessor.right
            collection.val = predecessor.val

            collection.left = remove_plant(collection.left, predecessor.val)
    return collection
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)
print_tree(remove_plant(collection, "Pilea"))
    
        



    