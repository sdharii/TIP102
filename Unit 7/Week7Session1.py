# Standard Problems

# def count_suits_iterative(suits):
#     count = 0

#     for suit in suits:
#         count += 1
#     return count

# def count_suits_recursive(suits):
#     if not suits:
#         return 0
#     return 1 + count_suits_recursive(suits[1:])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])
# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

def count_suits_iterative(suits):
    if not suits:
        return 0
    seen = set()
    count = 0

    for suit in suits:
        if suit not in seen:
            seen.add(suit)
            count +=1
        else:
            continue
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    if suits[0] in suits[1:]:
        return 0 + count_suits_recursive(suits[1:])
    else:
        return 1 + count_suits_recursive(suits[1:])
# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

def fibonacci_growth(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci_growth(n-1) + fibonacci_growth(n-2)
# print(fibonacci_growth(5))
# print(fibonacci_growth(8))

def power_of_four(n):
    if n == 0:
        return 1
    elif n > 0:
        return 4 * power_of_four(n-1)
    else:
        return 1 / power_of_four(-n)
# print(power_of_four(2))
# print(power_of_four(-2))

def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    
    max = strongest_avenger(strengths[1:])

    if strengths[0] > max:
        return strengths[0]
    else:
        return max
# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))

def count_deposits(resources):
    if not resources:
        return 0
    if resources[0] == "V":
        return 1 + count_deposits(resources[1:])
    else:
        return 0 + count_deposits(resources[1:])
# print(count_deposits("VVVVV"))
# print(count_deposits("VXVYGA"))

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    dummy = Node(0)
    if not mission1:
        return mission2
    if not mission2:
        return mission1
    
    if mission1.value < mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))