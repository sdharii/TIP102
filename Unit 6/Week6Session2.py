class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    current = clues

    while current:
        if current.next == clues:
            return True
        current = current.next
    return False
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_timelines(known_timeline, witness_timeline):
   
    dummy = Node(0)
    current = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            current.next = known_timeline
            known_timeline = known_timeline.next
        else:
            current.next = witness_timeline
            witness_timeline = witness_timeline.next
        current = current.next

    if known_timeline:
        current.next = known_timeline
    else:
        current.next = witness_timeline

    return dummy.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))