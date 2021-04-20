# Проработать встроенние функции множеств.
# Встроенние функции можно взять на сайте (https://www.programiz.com/python-programming/set),
# раздел “Built-in Functions with Set”.
# Но на єтом сайте приведени примери для списков, Задача переделать примери для множеств.


# add
my_set = {1, 3}
print(my_set)

my_set.add(2)
print(my_set)

vowels = {'a', 'e', 'i', 'u'}
vowels.add('o')
print(vowels)

vowels.add('a')
print(vowels)

vowels = {'a', 'e', 'u'}
tup = ('i', 'o')
vowels.add(tup)
print(vowels)

vowels.add(tup)
print(vowels)


# clear
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)
vowels.clear()
print(vowels)


# copy
numbers = {1, 2, 3, 4}
new_numbers = numbers
print(numbers, new_numbers)
print(id(numbers), id(new_numbers))

new_numbers.add(5)
print(numbers, new_numbers)
print(id(numbers), id(new_numbers))

numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()
print(numbers, new_numbers)
print(id(numbers), id(new_numbers))

new_numbers.add(5)
print(numbers, new_numbers)
print(id(numbers), id(new_numbers))


# difference
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.difference(b))
print(b.difference(a))
print(a - b)
print(b - a)


# difference_update
a = {'a', 'c', 'g', 'd'}
b = {'c', 'f', 'g'}
result = a.difference_update(b)
print(a)
print(b)
print(result)


# discard
numbers = {2, 3, 4, 5}
print(numbers)
numbers.discard(3)
print(numbers)

numbers.discard(10)
print(numbers)

numbers = {2, 3, 5, 4}
print(numbers)
print(numbers.discard(3))
print(numbers)


# intersection
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.intersection(b))
print(b.intersection(a))
print(a & b)

a = {2, 3, 5, 4}
b = {2, 5, 100}
c = {2, 3, 8, 9, 10}
print(b.intersection(a))
print(b.intersection(c))
print(a.intersection(c))
print(c.intersection(a, b))

a = {100, 7, 8}
b = {200, 4, 5}
c = {300, 2, 3}
d = {100, 200, 300}
print(a.intersection(d))
print(b.intersection(d))
print(c.intersection(d))
print(a.intersection(b, c, d))

a = {100, 7, 8}
b = {200, 4, 5}
c = {300, 2, 3, 7}
d = {100, 200, 300}
print(a & c)
print(a & d)
print(a & c & d)
print(a & b & c & d)


# intersection_update
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
result = a.intersection_update(b)
print(result)
print(a)
print(b)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5, 6}
c = {4, 5, 6, 9, 10}
result = c.intersection_update(b, a)
print(result)
print(c)
print(b)
print(a)


# isdisjoint
a = {1, 2, 3, 4}
b = {5, 6, 7}
c = {4, 5, 6}
print(a.isdisjoint(b))
print(a.isdisjoint(c))

a = {'a', 'b', 'c', 'd'}
b = ['b', 'e', 'f']
c = '5de4'
d = {1: 'a', 2: 'b'}
e = {'a': 1, 'b': 2}
print('are a and b disjoint?', a.isdisjoint(b))
print('are a and c disjoint?', a.isdisjoint(c))
print('are a and d disjoint?', a.isdisjoint(d))
print('are a and e disjoint?', a.isdisjoint(e))


# issubset
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 4, 5}
print(a.issubset(b))
print(b.issubset(a))
print(a.issubset(c))
print(c.issubset(b))


# issuperset
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
c = {1, 2, 3}
print(a.issuperset(b))
print(b.issuperset(a))
print(c.issuperset(b))


# pop
a = {'a', 'b', 'c', 'd'}
print(a.pop())
print(a)


# remove
language = {'English', 'French', 'German'}
language.remove('German')
print('Updated language set:', language)


# # symmetric_difference
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
a.symmetric_difference(b)
b.symmetric_difference(a)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a ^ b)
print(b ^ a)

a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e'}
c = {}
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a.symmetric_difference(c))
print(b.symmetric_difference(c))

a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e'}
print(a ^ b)
print(b ^ a)
print(a ^ a)
print(b ^ b)


# symmetric_difference_update
a = {'a', 'c', 'd'}
b = {'c', 'd', 'e'}
result = a.symmetric_difference_update(b)
print(a)
print(b)
print(result)


# union
a = {'a', 'c', 'd'}
b = {'c', 'd', 2}
c = {1, 2, 3}
print(a.union(b))
print(b.union(c))
print(a.union(b, c))
print(a.union())

a = {'a', 'c', 'd'}
b = {'c', 'd', 2}
c = {1, 2, 3}
print(a | b)
print(b | c)
print(a | b | c)


# update
a = {'a', 'b'}
b = {1, 2, 3}
result = a.update(b)
print(a)
print(result)

string_alphabet = 'abc'
numbers_set = {1, 2}
numbers_set.update(string_alphabet)
print(numbers_set)

info_dictionary = {'key': 1, 'lock': 2}
numbers_set = {'a', 'b'}
numbers_set.update(info_dictionary)
print(numbers_set)


# Built-in Functions with Set
# all()
a = {1, 3, 4, 5}
print(all(a))

a = {0, False}
print(all(a))

a = {1, 3, 4, 0}
print(all(a))

a = {0, False, 5}
print(all(a))

a = set()
print(all(a))

s = {"This is good"}
print(all(s))

s = {'000'}
print(all(s))

s = {''}
print(all(s))


# any()
s = {1, 3, 4, 0}
print(any(s))

s = {0, False}
print(any(s))

s = {0, False, 5}
print(any(s))

s = set()
print(any(s))

s = {"This is good"}
print(any(s))

s = {'000'}
print(any(s))

s = {''}
print(any(s))


# enumerate()
grocery = {'bread', 'milk', 'butter'}
enumerateGrocery = enumerate(grocery)
print(grocery, enumerateGrocery)
print(type(enumerateGrocery))
print(set(enumerateGrocery))

enumerateGrocery = enumerate(grocery, 10)
print(set(enumerateGrocery))

grocery = {'bread', 'milk', 'butter'}
for item in enumerate(grocery):
    print(item)

for count, item in enumerate(grocery):
    print(count, item)

for count, item in enumerate(grocery, 100):
    print(count, item)


# len()
test = set()
print(len(test))

test = {1, 2, 3}
print(len(test))

testRange = set(range(1, 10))
print(type(testRange), len(testRange))

test = {''}
print(len(test))

testSet = {1, 2}
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))


# max()
number = {3, 2, 8, 5, 10, 6}
largest_number = max(number)
print(largest_number)

languages = {"Python", "C Programming", "Java", "JavaScript"}
largest_string = max(languages)
print(largest_string)

result = max({4, -5, 23, 5})
print(result)


# min()
number = {3, 2, 8, 5, 10, 6}
smallest_number = min(number)
print(smallest_number)

languages = {"Python", "C Programming", "Java", "JavaScript"}
smallest_string = min(languages)
print(smallest_string)

result = min({4, -5, 23, 5})
print(result)


# sorted()
a = {'e', 'a', 'u', 'o', 'i'}
print(set(sorted(a)))

a = {'Python'}
print(set(sorted(a)))

a = {'e', 'a', 'u', 'o', 'i'}
print(set(sorted(a)))

py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))

frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))


# sum()
numbers = {2.5, 3, 4, -5}
numbers_sum = sum(numbers)
print(numbers_sum)

numbers_sum = sum(numbers, 10)
print(numbers_sum)

start = 10
numbers_sum = sum(numbers, start)
print(numbers_sum)


# Frozensets
a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])
print(a.isdisjoint(b))
print(a.difference(b))

frozenset({1, 2})
print(a | b)
