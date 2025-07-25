#Standard Problem Set

def welcome():
    print("Welcome to the Hundred Acre Wood!")

# welcome()

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Michael")
# greeting("Winnie the Pooh")

def print_catchphrase(character):
    match character:
        case "Pooh":
            print("Oh bother!")
        case "Tigger":
            print("TTFN: Ta-Ta for now!")
        case "Eeyore":
            print("Thanks for noticing me.")
        case "Christopher Robin":
            print("Silly old bear.")
        case _:
            print(f"Sorry! I don't know {character}'s catchphrase!")

# character = "Pooh"
# print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)

def get_items(items, x):
    length = len(items)-1
    
    if x > length:
        print( None)
    else:
        print(items[x])

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
# get_items(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
# get_items(items, x)

def sum_honey(hunny_jars):
    count = 0
    for jar in hunny_jars:
        count += jar
    return count
hunny_jars = [2, 3, 4, 5]
# print(sum_honey(hunny_jars))

hunny_jars = []
# print(sum_honey(hunny_jars))

def doubled(hunny_jars):
    for jar in range(len(hunny_jars)):
        hunny_jars[jar] = hunny_jars[jar] * 2
    return hunny_jars
hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))

def count_less_than(race_times, threshold):
    count = 0
    for race in range(len(race_times)):
        if race_times[race] < threshold:
            count += 1
    return count
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
# print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
# print(count_less_than(race_times, threshold))

def print_todo_list(task):
    print("Pooh's To Dos:")
    for i, action in enumerate(task):
        print(f"{i+1}. {action}")
task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

task = []
# print_todo_list(task)

def can_pair(item_quantities):
    for item in item_quantities:
        if item % 2 != 0:
            return False
    return True
pass
item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

item_quantities = []
# print(can_pair(item_quantities))

def split_haycorns(quantity):
    result = []
    count = 1
    for _ in range(quantity):
        if quantity % count == 0:
            result.append(count)
        count += 1
    return result
quantity = 6
# print(split_haycorns(quantity))

quantity = 1
# print(split_haycorns(quantity))

def tiggerfy(s):
    result = ""
    for letter in s.lower():
        if letter not in ('t','i','g','e','r'):
            result += letter
    return f'"{result}"'
s = "suspicerous"
# print(tiggerfy(s))

s = "Trigger"
# print(tiggerfy(s))

s = "Hunny"
# print(tiggerfy(s))

def locate_thistles(items):
    result = []
    for index, item in enumerate(items):
        if item == "thistle":
            result.append(index)
    return result
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
