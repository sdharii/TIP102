# Standard Problem Set

def reverse_sentence(sentence):
    split_words = sentence.split()

    reversed = " ".join(split_words[::-1])
    return reversed
sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

sentence = "Pooh"
# print(reverse_sentence(sentence))

def goldilocks_approved(nums):
    minimun = min(nums)
    maximum = max(nums)

    for number in nums:
        if number == minimun or number == maximum:
            continue
        elif (minimun < number < maximum):
            return number
    return -1

nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums))

nums = [1, 2]
# print(goldilocks_approved(nums))

nums = [2, 1, 3]
# print(goldilocks_approved(nums))

def delete_minimum_elements(hunny_jar_sizes):
    elementList = []

    while hunny_jar_sizes:
        minimum = min(hunny_jar_sizes)
        for number in hunny_jar_sizes:
            if number == minimum:
                elementList.append(number)
                hunny_jar_sizes.remove(number)
            
    return elementList
hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes))
        
def sum_of_digits(num):
    sum = 0
    while (num > 0):
        sum += num % 10
        num = num // 10
    return sum
num = 423
# print(sum_of_digits(num))

num = 4
# print(sum_of_digits(num))

def final_value_after_operations(operations):
    tigger = 1

    for action in operations:
        if action == "bouncy" or action == "flouncy":
            tigger += 1
        elif action == "trouncy" or "pouncy":
            tigger -= 1
        else:
            continue
    return tigger
operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))

def is_acronym(words, s):
    acronym = ""

    for word in words:
        acronym += "".join(word[0])
    # print(acronym)
    if acronym == s:
        return True
    else:
        return False
    
words = ["christopher", "robin", "milne"]
s = "crm"
# print(is_acronym(words, s))

def make_divisible_by_3(nums):
    minimum = 0

    for number in nums:
        if number % 3 != 0:
            minimum += 1
    return minimum
nums = [1, 2, 3, 4]
# print(make_divisible_by_3(nums))

nums = [3, 6, 9]
# print(make_divisible_by_3(nums))

def exclusive_elemts(lst1, lst2):
    newList = []

    for word in lst1:
        if word not in lst2:
            newList.append(word)
    
    for word in lst2:
        if word not in lst1:
            newList.append(word)
    return newList
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
# print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
# print(exclusive_elemts(lst1, lst2))

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
# print(exclusive_elemts(lst1, lst2))

def merge_alternately(word1, word2):
    mergedWord = ""

    for char1, char2 in zip(word1, word2):
        mergedWord += char1 + char2
    return mergedWord
word1 = "wol"
word2 = "oze"
# print(merge_alternately(word1, word2))

def good_pairs(pile1, pile2, k):
    goodPairs = 0

    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j]*k) == 0:
                goodPairs += 1
    return goodPairs
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))
