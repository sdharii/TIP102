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

# print_linked_list(merge_timelines(known_timeline, witness_timeline))

def collect_false_evidence(evidence):
    """
    U:
        I: head of a linked list (evidence)
        O: returns an array containing values that are valid clues
        C: can be in any order when returned
        E: empty LL -> return None, only 1 node - > return head
    P:
        init current pointer to head
        init a set to keep track of visited nodes
        while theres a current node,
            if current isnt in the set, add it to set
            otherwise return current
    """
    current = evidence
    visited = set()

    if not evidence:
        return None
    if not evidence.next:
        return []

    while current:
        if current not in visited:
            visited.add(current)
            current = current.next 
        else:
            break
    else:
        return []
    
    result = []
    start = current
    while True:
        result.append(current.value)
        current = current.next
        if current == start:
            break
    return result

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))

def partition(suspect_ratings, threshold):
    """
    U:  
        I: head of a linked list (suspect_ratings), int (threshold)
        O: return the head of the partitioned list
        C: values greater than threshold come before nodes with values less than or equal to threshold
        E: empty LL -> return None ; one node -> return head
    P:
        create a dummy node
        create a prev variable set to None
        init a current pointer to head
        while theres a current node, 
        if the current value is greater than threshold
            dummy.next = current
            holder = current.next
            prev = current
            current.next = prev
            current = holder
        else if the current value is <= threshold
            prev.next = current
        return dummy.next
    """
    highdummy = Node(0)
    lowdummy = Node(0)

    hightail = highdummy
    lowtail = lowdummy
    current = suspect_ratings

    while current:
        next = current.next
        current.next = None

        if current.value > threshold:
            hightail.next = current
            hightail = hightail.next
        else:
            lowtail.next = current
            lowtail = lowtail.next
        
        current = next
    hightail.next = lowdummy.next
    return highdummy.next
        
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

# print_linked_list(partition(suspect_ratings, 3))

def merge_times(known_timeline, witness_timeline):
    dummy = Node(0)
    dummyhead = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            dummyhead.next = known_timeline
            known_timeline = known_timeline.next
        elif known_timeline.value >= witness_timeline.value:
            dummyhead.next = witness_timeline
            witness_timeline = witness_timeline.next
        
    dummyhead = dummyhead.next

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

# print_linked_list(merge_timelines(known_timeline, witness_timeline))

def rotate_right(head, k):
    """
    U: 
        I: head of a linked list (evidence), int (k)
        O: return the head of the rotateed list
        C: must rotate the list to the right by 'k' spaces
        E: empty list -> return None ; one node -> return head
    P
        1. count the length of the linked list
        2. set k = k % length to handle over-rotation
        3. if k == 0, no rotation is needed -> return head
        4. use two pointers:
            - fast: moves k steps
            - slow: starts at the dummy node
        5. move fast and slow until fast.next is None
        6. set new_head = slow.next
        7. set slow.next = None to break the link
        8. connect the original tail to the original head
        9. return new_head
    """
    if not head or not head.next or k == 0:
        return head
    
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    tail = current

    k = k % length
    if k == 0:
        return head
    
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    
    new_head = slow.next
    slow.next = None

    fast.next = head
    return new_head
evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

# print_linked_list(rotate_right(evidence_list1, 2))
# print_linked_list(rotate_right(evidence_list2, 4))

def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    current = dummy
    carry = 0

    while head_a or head_b or carry:
        digit1 = head_a.value if head_a else 0
        digit2 = head_b.value if head_b else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        digit = total % 10

        current.next = Node(digit)
        current = current.next

        if head_a:
            head_a = head_a.next
        if head_b:
            head_b = head_b.next
    return dummy.next
head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))
print(7%10)
