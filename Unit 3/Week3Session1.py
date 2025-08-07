# Standard Problem Set
from collections import deque

def is_valid_post_format(posts):
    mapping = {')':'(', '}':'{',']':'['}
    stack = []

    for char in posts:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

def reverse_comments_queue(comments):
    queue = deque()

    for comment in comments:
        queue.append(comment)
    
    newList = []
    while queue:
        newList.append(queue.pop())
    return newList
# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

def is_symmetrical_title(title):
    left = 0
    right = len(title)-1

    while left < right:
        if title[left] == " ":
            left += 1
            continue
        if title[right] == " ":
            right -= 1
            continue
        
        if title[left].lower() == title[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True
# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

def clean_post(post):
    stack = []

    for char in post:
        if stack:
            top = stack[-1]

            if char.lower() == top.lower() and char != top:
                stack.pop()
                continue
        stack.append(char)
    return ''.join(stack)
# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s")) 

def edit_post(post):
    queue = deque()

    splitpost = post.split()

    for word in splitpost:
        queue.append(word[::-1])
    
    reversed = []

    while queue:
        reversed.append(queue.popleft())

    return " ".join(reversed)
# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 

def post_compare(draft1, draft2):
   def process(text):
       stack = []
       for char in text:
           if char == '#':
               if stack:
                   stack.pop()
           else:
               stack.append(char)
       return stack
   return process(draft1) == process(draft2)
print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 