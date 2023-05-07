# 1. Write a Python program to get a single string from two given strings,
# separated by a space, and swap the first two characters of each string


def swap_string_chars(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " + new_str2


x = "leila"
y = "Ashur"
print(swap_string_chars(x, y))  # Output: "wollo herld"

# 2.  Write a Python function that takes a list of words and
# returns the longest word and the length of the longest one
def longest(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)
word = ["Table", "Chair", "Calender", "Spoon"]

longest, length = longest(word)
print(f"The longest word is '{longest}', which has a length of {length} characters.")            

# # Write a Python function that takes two lists and returns
# # True if they have at least one common member.
def common_member(list1, list2):
   
    for item in list1:
        if item in list2:
            return True
        else:
          return False
list1=[1,2,3,4]      
list2=[3,8,5,6]
result=(common_member(list1,list2))
print(result)
# # 5. Write a Python program to convert a list to a list of dictionaries.
# # Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
keys = ["color_name", "color_code"]
values = [["Black", "#000000"], ["Red", "#FF0000"], ["Maroon", "#800000"], ["Yellow", "#FFFF00"]]

empty = []
for sublist in values:
    dictionary = dict(zip(keys, sublist))
    empty.append(dictionary)


print(empty)
# # 6. Write a Python program to check whether all dictionaries in a list are empty or not
empty_dictionaries = [{},{},{}]
if empty_dictionaries == []:
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")
# # 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
# even_numbers = [num for num in numbers if num % 2 ==0]
# print(even_numbers)
# # 8. Find the common numbers in two lists (without using a tuple or set)
list_a = 1, 2, 3, 4,
list_b = 2, 3, 4, 5
common_numbers = [a for a in list_b]
print(common_numbers)
# # 9. Use a nested list comprehension to find all of the numbers from 1-1000
 # that are divisible by any single digit besides 1 (2-9)
 
# # Write a Python function to remove all vowels in a string 
def remove_vowels(string):
  
    vowels = "aeiouAEIOU"
    return "".join([char for char in string if char not in vowels])
result=remove_vowels("laptop")
print(result)
       
        
