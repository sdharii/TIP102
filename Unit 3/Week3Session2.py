# Standard Problem Set
from collections import deque

def manage_stage_changes(changes):
    stack = []
    cancelledStack = []
    for action in changes:
        if "Schedule" in action:
            stack.append(action[-1])
        elif action == "Cancel":
            cancelledStack.append(stack.pop())
        elif action == "Reschedule" and cancelledStack:
            stack.append(cancelledStack.pop())
    return stack
# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

def process_performance_requests(requests):
    requests = sorted(requests)
    queue = deque()

    for tuple in requests:
        queue.append(tuple[1])
    
    result = []

    while queue:
        result.append(queue.pop())
    return result
# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

def collect_festival_points(points):
    stack = []

    for num in points:
        stack.append(num)
    
    total = 0
    while stack:
        total += stack.pop()
    return total
# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

def booth_navigation(clues):
    stack = []
    backtrackStack = []

    for clue in clues:
        if clue == "back" and stack:
            stack.pop()
        elif clue != "back":
            stack.append(clue)
    return stack
# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 

def merge_schedules(schedule1, schedule2):
    result = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 <len(schedule1) and pointer2< len(schedule2):
        result.append(schedule1[pointer1])
        result.append(schedule2[pointer2])

        pointer1 += 1
        pointer2 += 1
    
    if schedule1:
        result.append(schedule1[pointer1:])
    if schedule2:
        result.append(schedule2[pointer2:])
    
    return ''.join(result)
# print(merge_schedules("abc", "pqr")) 
# print(merge_schedules("ab", "pqrs")) 
# print(merge_schedules("abcd", "pq")) 

def next_greater_event(schedule1, schedule2):
    ans = [0] * len(schedule1)
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(schedule1):
        for num in schedule2:
            if num == schedule1[pointer1 + 1 ] :
                ans[pointer1] = num
                pointer1 += 1
            else:
                ans[pointer1] = -1
                pointer1 += 1
    return ans
print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4])) 
