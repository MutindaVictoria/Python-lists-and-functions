#1. Write a Python program to get a single string from two given strings, 
#separated by a space, 
#and swap the first two characters of each string
a="move"

b="along"

x=a[0:2]

a=a.replace(a[0:2],b[0:2])

b=b.replace(b[0:2],x)

print(a,b)


#Write a Python function that takes a list of words and 
#returns the longest word and the length of the longest one
def longest_words(words):
    longest_word = ""
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)
    return longest_word,longest_length
print(longest_words(["Patricia","Josphine","Bernard"]))




#Write a Python program that accepts a comma-separated sequence of words as input and 
#prints the distinct words in sorted form (alphanumerically).

items = ("red,white,move,movement,writers")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


#Write a Python function that takes two lists and
 #returns True if they have at least one common member.
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(common_data([1,2,3,4,5], [5,6,7,8,9]))


#Write a Python program to convert a list to a list of dictionaries.
#Sample 
#lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])


#Write a Python program to check whether all dictionaries in a list are empty or not

my_list = [{},{},{}]
my_list1 = [{1:2},{},{}]
print(all(not d for d in my_list))

#Find the common numbers in two lists (without using a tuple or set) 
#list_a = 1, 2, 3, 4, 
#list_b = 2, 3, 4, 5


list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common = [a for a in list_a if a in list_b]
print(common)

#Use a nested list comprehension to find all of the 
#numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

numbers=[num for num in range(1,1001) if [div for div in range(2,10) if num%div == 0]]

#10. Write a Python function to remove all vowels in a string

input_string = "movement"
result = input_string

vowels = ('a', 'e', 'i', 'o', 'u')

for x in input_string.lower():
    if x in vowels:
        result = result.replace(x, "")

print('After removing vowels : ', result)