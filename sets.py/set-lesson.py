# HOME WORK

#Livel 1

#Task 1
it_companies={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#task 2
it_companies={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

# Task 3
it_companies={'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.update({'Twitter', 'Instagram', 'YouTube'})
print(it_companies)

# Task 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('Microsoft')
print(it_companies)


# Livel 2

#task 1
A={11,22,33,44,55}
B={11,22,33,44,55,66,77,88,99}

print(A.union(B))

#task 2
A={11,22,33,44,55}
B={11,22,33,44,55,66,77,88,99}
print(A.intersection(B))

# task 3
print(A.issubset(B))

#task 4
print(A.isdisjoint(B))


# task 5

print(A.union(B))

print(B.union(A))


#task 6
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

#task 7

# del A, B, it_companies



# Livel 3

# task 1

age = [ 19, 24, 25, 26, 24, 25, 24,15, 22, 43]

age = set(age)
print(age)
print('length of the set:', len(age))


#task 2
# string: форма переменной/тип данных
# lists: может быть изменен, упорядочен, не уникален, []
# tuples: не может быть изменен, упорядочен, не уникален, ()
# set: можно добавлять и удалять, но существующие элементы нельзя превращать в другие элементы, неупорядоченные, уникальные, {}

#task 3
words = {'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
print(len(words))