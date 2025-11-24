import numpy as np

__A__= 20 # python identifiers are case_sensitive
a=30
print(f"My number is {__A__}")

class MyClass:
    print("This is inside " \
    "my class.")

# Python list (array)
myList = ["Uwambere", "Uwakabiri", 
          "Uwagatatu"]
print(myList)

myQoutedNames = """Abana"""


# My single_line comment
"""
These scripts will be ignored!
print("The first.")
print("The second.")
"""

print(myQoutedNames)

# structuring in python
age, weight, name = 10, 2, "John kagabo" #,20
print(age, weight, name)

x=y=z="Orange"
print(x)
print(y)
print(z)

x=y=z="Orange","yellow" # python tuple
print(x)
print(y)
print(z)

fruits = ("apple", "banana", "cherry", "pineapple", "mango", "strawberries")
x, y, *z = fruits
print(x)
print(y)
print(z)

def myfunc():
    global q
    q = "Fantastic"

myfunc()
print("Python is "+ q)

# my_name = bytes ("Mugisha chrispin")
# print(my_name)

num = 7
print(complex(7))
# print(int(complex(7)))

my_str = "Hello world"
print(my_str[-10:-20:-1]) 
# reversing a string

my_str2 = " Helllo, world"
print(my_str2.strip()) # removes right and left spaces/tabs
print(my_str2.replace(" ", ""))

def my_converter(x):
    return x * 0.3848

txt = f"A plane can fly at a {my_converter(30000)} meter altitude"
print(txt)


price = 12.121244
formated_price = f"The formated price is {price:.2f}"
print(formated_price)

txt2 = 'The universe is {:,.2f} years old.'.format(13031000000.22123123)
print(txt2)

txt3 = "Hello world".index("world")
print(txt3)
txt3 = "Hello world".find("world")
print(txt3)

txt3 = "  Hello123  "
print(txt3.isalpha())   # False (digits present)
print(txt3.isdecimal()) # False (not only digits)
print(txt3.isdigit())   # False (same reason)
print(txt3.isnumeric()) # False
print(txt3.lower())     # "  hello123  "
print(txt3.islower())   # False
print(txt3.upper())     # "  HELLO123  "
print(txt3.isupper())   # False
print(txt3.swapcase())  # "  hELLO123  "
print(txt3.isspace())   # False
print(txt3.strip())     # "Hello123"
print(txt3.rstrip())    # "  Hello123"
print(txt3.lstrip())    # "Hello123  "

x=5
print(x|3)
x=["apple", "banana"]
print("banana" in x)
x=["apple", "banana"]
print("pineapple" not in x)
x=["apple", "banana"]
print("Apple" in x)

print("Apple" is 'apple')
print("Apple" == 'apple')
print("Apple" == 'Apple')

my_list = [10, "hello", 3.14, True, None, [1, 2], (3, 4), {5, 6}, {"a": 1}, b"bytes", bytearray(b"hi"), complex(2, 3)]
# ordered, mutable, allows duplicates — use for general sequences — can store any datatypes
print(my_list)

my_tuple = (42, "apple", 2.5, False, None, [7, 8], (9, 10), {11, 12}, {"b": 2}, b"data", bytearray(b"xy"), complex(5, 6))
# ordered, immutable, allows duplicates — use for fixed data — can store any datatypes
print(my_tuple)

my_set = {1, "hi", 3.14, True, None, (1, 2), frozenset({3, 4}), b"bytes"}
# unordered, mutable, unique — use for unique values and fast membership — only hashable datatypes allowed (no list, set, dict, bytearray)
print(my_set)

my_dict = {
    "name": "Mchiir",
    1: "integer key",
    2.5: ["a", "list", "value"],
    (3, 4): {"nested": "dict"},
    frozenset({5, 6}): (7, 8),
    b"bytes": True,
    None: complex(7, 8)
}
# ordered (3.7+), mutable, unique keys — use for key-value mappings — keys hashable, values can be any datatype
print(my_dict)

list=["pineapple", "papaya", "mango"]
def count_vowels(word):
    return sum(ch in 'aeiuo' for ch in word.lower())

list.sort(key=count_vowels)

list[3:2]=['watermelon', 'cherry', 'strarberry']
print(list)

list=['apple','banana', 'cherry', 'aaa']
[print(x) for x in list if x in list]
myVar = [print(x) for x in list if x in list]
print(myVar)
balance=[2000, 500, 100, 31, 3000, 500, 4000]
print(max(balance))
print(list)

list=["pineapple", "papaya", "mango"]
def count_vowels(word):
    return sum(ch in 'aeiuo' for ch in word.lower())

list.sort(key=count_vowels) # sort by "more vowels" last
print(list)

def sum_numbers(*numbers): # returns a list
    total = 0
    for num in numbers:
        total += num
    return total

# arbitrary arguments (*args)
print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(10, 20, 30, 40)) # Output: 100

def format_user_info(names, age, city):
    return f"{names} is {age} years old and lives in {city}"

print(format_user_info(names="Alice", age=10, city="New York")) # Keyword arguments

def get_user_info(**user_info): # returns a dictionary
    return f"{user_info['names']} is {user_info['age']} years old and lives in {user_info['city']}"

print(get_user_info(names="Kamali", age=20, city="kigali")) # arbitrary keyword arguments

"""
# Quiz/CAT

print(sum([i > 2 for i in [1,2,3,4]]))
print([i**2 for i in range(6) if i % 2])

for i in range(3):
    x=i
def test():
    print(x)
test() # 2

fruits = ("apple", "banana", "grape", "mango", "watermelon", "pear", "cherry")
first, *middle, last = fruits
print(first, middle, last)

print([False]*3 == [0]*3)

def func(a=[]):
    a.append(len(a))
    return a

print(func())
print(func())
print(func())


def f(n):
    return n if n<=1 else f(n-1)+f(n-2)

print(f(6))
"""