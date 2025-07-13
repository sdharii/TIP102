# class Node:
#     def __init__(self, house, score, next = None):
#         self.house = house
#         self.value = score
#         self.next = next

# For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# names = Node("Harry",Node("Ron",(Node("Hermione"))))
# print_linked_list(names)

# def count_element(house_points, score):
#     """
#     U:
#         I: head of a linked list (house_points), int (score)
#         O: return an int -> the frequency of score in the linked list
#         C: n/a
#         E: n/a
#     P:
#         initialize a current variable 
#         initialize a count variable
#         create a while loop -> while current:
#             if current.value equals score:
#                 increase count by one
#             current is now current.next
#         return count

#     """
#     current = house_points
#     count = 0

#     while current:
#         if current.value == score:
#             count += 1
#         current = current.next
    
#     return count

# house_points = Node("Gryffindor", 600, 
                # Node("Ravenclaw", 300,
                #     Node("Slytherin", 500,
                #         Node("Hufflepuff", 600))))

# score = 600
# print(count_element(house_points, score))

# class Node:
#     def __init__(self, potion, next=None):
#         self.potion = potion
#         self.next = next

# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_middle_potion(potions):
#     """
#     U:
#         I: head of a linked list (potions)
#         O: return the middle node in potions
#         C: must use the slow & fast pointer method. if there are two middle nodes, return the second middle node
#         E: no nodes or only head -> return None
#     P
#         handle edge cases
#         initialize current variable

#         while fast and fast.next exists
#             increase slow by 1
#             increase fast by 2 (fast.next)
#         return slow.potion
                    
#     """
#     if not potions or not potions.next:
#         return None
    
#     slow = potions
#     fast = potions

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow.potion

# potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
# potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

# print(find_middle_potion(potions1))
# print(find_middle_potion(potions2))

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

def reverse(events):
    """
    U:
        I: head of a linked list (events)
        O: return the head of the reversed list
        C: n/a
        E: no head - > return none ; only head -> return head
    P:
        handle edge cases
        initialize a current,previous, and next pointer

        traverse through the linked list as current node exists
            store the current.next node
            change currents next value to previous

            update prev node to current node
            update current node
        return current node

    """
    if not events:
        return None
    if not events.next:
        return events
    
    current = events
    previous = None
    next = None

    while current:  
        next = current.next
        current.next = previous

        previous = current
        current = next
    return previous

events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))
# print_linked_list(reverse(events))

def is_mirrored(head):
    """
    U:
        I: the (head) of a linked list
        O: bool -> returns True if values are the same backwards & forwards, otherwise False
        C: n/a
        E: empty linked list -> return None ; only head exists -> return head
    P
        handle edge cases
        use a two pointer method -- slow and fast 
        initialize a previous variable
        initialize a middle node
        find the middle node, reverse the second half of the linked list
            change its .next to the previous node
        
    """
    if not head:
        return None
    if not head.next:
        return True
    
    slow = head
    fast = head
    previous = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    middleNode = slow
    # print(middleNode.value) -- Checking if the middle is correct!

    current = middleNode
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    
    first_half = head
    second_half = previous

    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True
   
list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

# print(is_mirrored(list1))
# print(is_mirrored(list2))

def loop_start(path_start):
    """
    U:
        I: the head of a linked list (path_start)
        O: returns the value of the node where the cycle starts, otherwise return None
        C: n/a
        E: empty linked list -> return None

    P
        handle edge cases
        initialize a current variable 
        initialize a set to keep track of nodes seen
            if a node hasnt been seen, add it to the set
                increment current to the next node
            otherwise if a node HAS been seen, indicating its a cycle
                return node's value
        return None if there's no cycle
    """
    if not path_start:
        return None
    
    current = path_start
    seen = set()

    while current:
        if current not in seen:
            seen.add(current)
            current = current.next
        else:
            return current.value
    return None
path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1
print(loop_start(path_start))