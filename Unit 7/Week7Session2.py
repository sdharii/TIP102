# Standard Problems

def find_perfect_song(playlist, length):
    left = 0
    right = len(playlist) - 1

    while left <= right:
        mid = (left + right) // 2

        if playlist[mid] == length:
            return mid
        elif playlist[mid] < length:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# print(find_perfect_song([101, 102, 103, 104, 105], 103))
# print(find_perfect_song([201, 202, 203, 204, 205], 206))

def can_attend(tour_dates, available):
    if not tour_dates:
        return False
    
    if tour_dates[0] == available:
        return True
    else:
        return can_attend(tour_dates[1:], available)
# print(can_attend([1, 3, 7, 10, 12], 12))
# print(can_attend([1, 3, 7, 10, 12], 5))

def my_sqrt(x):
    left = 0
    right = x

    if x < 2:
        return x
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right 
# print(my_sqrt(4))
# print(my_sqrt(8))

def get_group_sum(group_sizes, room_capacity):
    group_sizes.sort()
    max_sum = -1
    n = len(group_sizes)

    for i in range(n-1):
        left = i + 1
        right = n - 1
        best = -1
        while left <= right:
            mid = (left+right) // 2
            total = group_sizes[i] + group_sizes[mid]
            if total < room_capacity:
                best = total
                left = mid + 1
            else:
                right = mid - 1
        if best != -1:
            max_sum = max(max_sum,best)
    return max_sum
# print(get_group_sum([1,20,10,14,3,5,4,2], 12))
# print(get_group_sum([10,20,30], 15))

def merged_tracks(track1,track2):
    if not track1:
        return track2
    if not track2:
        return track1
    
    if track1[0] < track2[0]:
        return [track1[0]] + merged_tracks(track1[1:], track2)
    else:
        return [track2[0]] + merged_tracks(track1, track2[1:])
track1 = [1, 3, 5]
track2 = [2, 4, 6]
track3 = [10, 20]
track4 = [15, 30]

print(merged_tracks(track1, track2))
print(merged_tracks(track3, track4))