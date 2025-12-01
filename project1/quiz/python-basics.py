# print(bool([]) == False)

# (a := 2025, 2026)
# (a, b := 15, 16)
# print(f"{a=} {b=}")

# a=list(range(10))
# print(a[2:8:3])

# arr = [1,2,3]
# for i in arr[:]:
#     arr.remove(i)
# print(arr)

# i = 0
# while i < 3:
#     if i == 1:
#         break
#     print(i)
#     i += 1
# else:
#     print("Done")

# def status():
#     print(flag)
# flag = True
# status()

# list1 = [2,8,0,6]
# list2 = [2,7,5]
# def test(list):
#     for i in list:
#         list.remove(i)
#         print(i, end="")
# test(list1)
# test(list2)

# for i in range(3):
#     x = i
# def test():
#     print(x)
# test()

# print(sum([i > 2 for i in [0,1,2,3,4]]))

# arr = [1, 2, 3]
# for i in arr:
#     arr.remove(i)
# print(i)

# def mystery(nums):
#     return [n for n in nums if nums.count(n) == 1]
# print(mystery([1,2,2,3,4,4,5]))

# x = 1
# def a():
#     global x
#     x = 2
# def b():
#     print(x, end="")
# b()
# a()
# b()

# int = 10
# list = [20, 30]
# def modify(int, list):
#     int += 30
#     list.append(int)
# modify(int, list)
# print(int)
# print(list)

# def func(a, b, c=5):
#     print(a, b, c)
# func(1, c=10, b=2)

# n = 12345
# my_sum = 0
# while n > 0:
#     my_sum += n % 10
#     n //= 10
# print(my_sum)

# def outer_function():
#     x = 10
#     def inner_function():
#         return x
#     return inner_function
# f = outer_function()
# print(f())

# x = [1, 2, 3]
# y = x
# x.append(4)
# print(y)

# y3 = ["Y3A", "Y3B", "Y3C", "Y3D"]
# for i in y3:
#     y3.remove(i)
# print(i)

# print([] is not [])

# x = 'abcd'
# for i in range(len(x)):
#     x = 'a' * (i + 1)
# print(x)

# def demo(*args, **kwargs):
#     print(args, kwargs)
# demo(1,2,3,4)

# x = "awesome"
# def myFunc():
#     x = "fantastic"
#     print("Python is " + x)
# myFunc()
# print("Python is " + x)

# print(bool([]) == False)

# def simple_function(x, y=None):
#     if y is None:
#         y = []
#     y.append(x)
#     return y
# result1 = simple_function(1)
# result2 = simple_function(2, [])
# result3 = simple_function(3)
# print(result1)
# print(result2)
# print(result3)

# fruits = ("apple", "banana", "grape", "mango", "watermelon", "pear", "cherry")
# first, *middle, last = fruits
# print(first, middle, last)

# def simple_function(x, y=None):
#     if y is None:
#         y = []
#     y.append(x)
#     return y
# result1 = simple_function(1, [9,5])
# result2 = simple_function(2, [0])
# result3 = simple_function(3)
# print(result1)
# print(result2)
# print(result3)

# def add_five(n):
#     n += 5
# value = 10
# add_five(value)
# print(value)

# a = []
# b = [a.append(i) for i in range(5)]
# print(a)
# print(b)

# list1 = ["Banana", "Apple", "Mango", "Orange"]
# list2 = ["Banana", "Apple", "Mango"]
# def test(list):
#     for i in list:
#         list.remove(i)
#         print(i)
# test(list1)
# test(list2)

# if False:
#     pass
# else:
#     print("True branch")

# def g(a):
#     return a == a[::-1]
# print("school")

# x = 1
# def test():
#     global x
#     for x in range(3):
#         pass
# test()
# print(x)

# def func(a=[]):
#     a.append(len(a))
#     return a
# print(func())
# print(func())

# print([] is False)

# print([False] * 3 == [0] * 3)

# code = 501
# if not (code >= 100 and code <= 200):
#    print("1")
# if not (code >= 400 or code == 501):
#    print("2")

# x = {i: i*i for i in range(3)}
# print(x)

# x = {1,2,3}
# y = {3,4,5}
# print(x & y)

# print(len([i for i in range(20) if i % 3 == 0 and i % 5 == 0]))

# print(sorted([10,2,9], key=str))

# def f(n):
#     return n if n <= 1 else f(n-1) + f(n-2)
# print(f(6))

# a = [i**2 for i in range(6) if i % 2]
# print(a)

# print([] == False)