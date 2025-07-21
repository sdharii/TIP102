def find_cruise_length(cruise_lengths, vacation_length):
    """
    U:
        I: int (vacation_length), list of ints (cruise_lengths)
        O: bool -> true if cruise length matches vacation_length, otherwise false
        C: n/a
        E: empty list -> false
    P:
        1. init a left and right pointer
        2. do a binary search
            if mid is == vacation_length, return mid
            if mid is < vacation length
                left = mid + 1
            if mid is > vacation length
                right = mid - 1
        return false
    """
    left = 0
    right = len(cruise_lengths) - 1

    while left <= right:
        mid = (left + right ) // 2

        if cruise_lengths[mid] == vacation_length:
            return True
        
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
        else:
            right = mid - 1
    return False
# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

def binary_search(cabins, preferred_deck, left, right):
    if left > right:
        return left
    
    mid = (left + right) // 2

    if cabins[mid] == preferred_deck:
        return mid
    
    if cabins[mid] > preferred_deck:
        return binary_search(cabins, preferred_deck, left, mid-1) 
    if cabins[mid] < preferred_deck:
        return binary_search(cabins, preferred_deck, mid + 1, right)

def find_cabin_index(cabins, preferred_deck):
    """
    U:
        I: list of ints (cabins), int (preferred_deck)
        O: the index of preferred_deck, otherwise return the index where it would be
        C: must use recursion, must have O(log n)
        E: empty list -> return 0
    P:
        init left and right
        find mid point
        create base cases: 
            if mid == preferred_deck, return mid
        
    """
    left = 0
    right = len(cabins) - 1
    return binary_search(cabins, preferred_deck, left, right)

   

    
# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))

def count_checked_in_passengers(rooms):
    """
    U:
        I: list of ints (rooms) -> 1, checked in; 0, not checked in
        O: returns the total of number of checked in passengers
        C: must be O(log n) time
        E:
    P:
        init left and right pointers
        init mid
        If rooms[mid -1] = 0 and rooms[mid] = 1
            return len(rooms[mid:])
        Else left = mid + 1 for rooms[mid] = 0
        Else right = mid - 1 for rooms[mid] = 1
        return 0

    """
    left = 0
    right = len(rooms) - 1

    while left <= right:
        mid = (left + right) // 2

        if rooms[mid -1] == 0 and rooms[mid] == 1:
            return len(rooms[mid:])
        elif rooms[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1
    return 0
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]
# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))

def is_profitable(excursion_counts):
    
    pass