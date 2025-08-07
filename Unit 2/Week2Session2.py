# Standard Problem Set
from collections import Counter

def most_endangered(species_list):
    lowestName = ""
    lowestpop = float('inf')

    for species in species_list:
        if species["population"] < lowestpop:
            lowestpop = species["population"]
            lowestName = species["name"]
        
    return lowestName

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

# print(most_endangered(species_list))

def count_endangered_species(endangered_species, observed_species):
    seen = set()

    for char in endangered_species:
        seen.add(char)

    count = 0
    for char in observed_species:
        if char in seen:
            count += 1
    return count
endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  

def navigate_research_station(station_layout, observations):
    myDict = {}
    for index, char in enumerate(station_layout):
        myDict[char] = index

    total_time = 0
    current = 0

    for char in observations:
        next_index = myDict[char]
        total_time += abs(next_index - current)
        current = next_index
    return total_time
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"
station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"
# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))

def prioritize_observations(observed_species, priority_species):
    new_List = []

    for animal in priority_species:
        new_List.append(animal)

    for animal in observed_species:
        if animal not in new_List:
            new_List.append(animal)
    return new_List
observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]
# print(prioritize_observations(observed_species2, priority_species2)) 

def distinct_averages(species_populations):
  
  
  averages = []

  while species_populations:
      minPop = min(species_populations)
      maxPop = max(species_populations)
      averages.append((minPop + maxPop)/2)
      species_populations.remove(minPop)
      species_populations.remove(maxPop)

  distinctAvg = 0
  
  if len(averages) == 1:
      return 1
  
  seen = set(averages)

  distinctAvg = len(seen)
  return distinctAvg

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

# print(distinct_averages(species_populations1))
# print(distinct_averages(species_populations2)) 

def max_species_copies(raised_species, target_species):
    raisedCount = Counter(raised_species)
    targetCount = Counter(target_species)

    copies = float('inf')

    for char in targetCount:
        if char not in raisedCount:
            return 0
        copies = min(copies, raisedCount[char]//targetCount[char])
    return copies
raised_species1 = "abcba"
target_species1 = "abc"
# print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
# print(max_species_copies(raised_species2, target_species2)) # Output: 2

def count_unique_species(ecosystem_data):
    newString = ""
    for char in ecosystem_data:
        if not char.isdigit():
            newString += " "
        else:
            newString += char

    newString = newString.split()
    print(newString)
    uniqueNums = set(newString)

    return len(uniqueNums)
ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

# print(count_unique_species(ecosystem_data1))
# print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))