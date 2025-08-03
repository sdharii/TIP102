# Standard Problem Set

from collections import Counter


def lineup(artists, set_times):
    myDict = {}

    for index, artist in enumerate(artists):
        myDict[artist] = set_times[index]
    return myDict
artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

def get_artist_info(artist, festival_schedule):
    if artist not in festival_schedule:
        return {"message":"Artist not found"}
    
    return festival_schedule[artist]
festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

def total_sales(ticket_sales):
    total = 0

    for entry in ticket_sales:
        total += ticket_sales[entry]
    return total
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

def identify_conflicts(venue1_schedule, venue2_schedule):
    sameSetTimes = {}

    
    for artist in venue2_schedule:
        if artist in venue1_schedule and venue2_schedule[artist] == venue1_schedule[artist]:
            sameSetTimes[artist] = venue2_schedule[artist]
    return sameSetTimes
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))

def best_set(votes):
    freqMap = {}

    for artist in votes.values():
        freqMap[artist] = freqMap.get(artist, 0) +1
    
    return next(iter(freqMap))

        

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

# print(best_set(votes1))
# print(best_set(votes2))

def max_audience_performances(audiences):
    total = 0
    maximum = max(audiences)

    for size in audiences:
        if size == maximum:
            total += size
    return total

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

def num_popular_pairs(popularity_scores):
    freq_map = Counter(popularity_scores)
    count = 0
    for freq in freq_map.values():
        if freq > 1:
            count += (freq * (freq - 1)) // 2
    return count

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3)) 

def find_stage_arrangement_difference(s, t):
    s1Dict = {}
    t1Dict = {}

    total = 0

    for index, name in enumerate(s):
        s1Dict[name] = index

    for index, name in enumerate(t):
        t1Dict[name] = index

    for name in s:
        absSum = abs(s1Dict[name]-t1Dict[name])
        total += absSum
    return total
s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

# print(find_stage_arrangement_difference(s1, t1))
# print(find_stage_arrangement_difference(s2, t2))

def num_VIP_guests(vip_passes, guests):
    vip_set = set()

    for char in vip_passes:
        vip_set.add(char)
    
    count = 0

    for char in guests:
        if char in vip_set:
            count += 1
    return count
vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

# print(num_VIP_guests(vip_passes1, guests1))
# print(num_VIP_guests(vip_passes2, guests2))

def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}
    
    for char, genre in zip(pattern, genres):
        if char in char_to_genre:
            if char_to_genre[char] != genre:
                return False
        else:
            char_to_genre[char] = genre

        if genre in genre_to_char:
            if genre_to_char[genre] != char:
                return False
        else:
            genre_to_char[genre] = char

    return True
pattern1 = "abba"
schedule1 = "rock jazz jazz rock"

pattern2 = "abba"
schedule2 = "rock jazz jazz blues"

pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"

# print(schedule_pattern(pattern1, schedule1))
# print(schedule_pattern(pattern2, schedule2))
# print(schedule_pattern(pattern3, schedule3))

def sort_performers(performer_names, performance_times):
    Dict = {}

    for index, performer in enumerate(performer_names):
        Dict[performer] = performance_times[index]

    Dict = sorted(Dict)

    print(Dict)
    # for performer in Dict.keys():
    #     return list(performer)

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))
