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

# Standard Problem Set

def merge_orders(order1, order2):
    if not order1:
        return order2
    if not order2:
        return order1
    
    new_node = TreeNode(order1.val + order2.val)

    new_node.left = merge_orders(order1.left, order2.left)
    new_node.right = merge_orders(order1.right, order2.right)

    return new_node 
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)
# print_tree(merge_orders(order1, order2))

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []
    
    queue = deque([design])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print(result)

croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
# print_design(croquembouche)

def max_tiers(cake):
    if cake is None:
        return 0
    
    left = max_tiers(cake.left)
    right = max_tiers(cake.right)

    return 1 + max(left, right)
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers(cake))

def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False
    
    if not inventory.left and not inventory.right:
        return inventory.val == order_size
    
    remaining = order_size - inventory.val
    return (can_fulfill_order(inventory.left, remaining) or can_fulfill_order(inventory.right, remaining))
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))

def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    
    result = []
    queue = deque([cupcakes])
    left_to_right = True

    while queue:
        levels = len(queue)
        nodeLevel = deque()

        for _ in range (levels):
            nodes = queue.popleft()

            if left_to_right:
                nodeLevel.append(nodes.val)
            else:
                nodeLevel.appendleft(nodes.val)
            
            if nodes.left:
                queue.append(nodes.left)
            if nodes.right:
                queue.append(nodes.right)
        result.extend(nodeLevel)
        left_to_right = not left_to_right
    return result
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))

