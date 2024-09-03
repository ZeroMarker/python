from sys import getsizeof


numbers = [1, 2, 3, 4, 5, 6]

print(numbers[::2])
print(numbers[::-1])

first, second, *other = numbers

print(first)
print(other)


def multiply(*nums):
    total = 1
    for number in nums:
        total *= number
    return total


print(multiply(2, 3, 4))

del numbers[0:3]
print(numbers)

for index, item in enumerate(numbers):
    print(index, item)


items = [
    ("Product1", 10),
    ("Product2", 7),
    ("Product3", 9),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item, reverse=True)
items.sort(key=lambda item: item[1])
print(items)

print(list(filter(lambda item: item[1] >= 9, items)))

filtered = [item for item in items if item[1] >= 9]

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

nums = [1, 1, 2, 3, 4]
first = set(nums)
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

values = {x: x * 2 for x in range(5)}
print(values)

generator = (x * 2 for x in range(5))
print(generator)
print(getsizeof(generator))

arr = [1, 2, 3]
print(*arr)

one = {"x": 1}
two = {"x": 10, "y": 2}
combined = {**one, **two, "z": 1}
print(combined)