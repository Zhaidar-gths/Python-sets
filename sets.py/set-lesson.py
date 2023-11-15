# set ерекшелігі - дубликатсия жасауға келмейді , және оның индексі болмайды яғни элементтер реттсіз тұрады 



# We use len() method to find the length of a set.
''''
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
print(st)
'''''

# Add жаңа элемент қосамыз ,қосатын жаңа элемент қаиталанбау керек сол кезде қосылады,және бір ғана элемент қосады
''''
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)
'''
#ал көп элемент қосу үшін uptade қолданамыз
''''
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)
'''

#exercises
''''
cities={"almaty","shymkent","astana","atrau","aktau"}
print(len(cities))

cities.add("taldykorgan")
print(len(cities))

# cities.add (input())
# print(cities)

# new_city=input("enter a city: ")

# cities.add(new_city)
# print(cities)
'''

''''
cities={"almaty","shymkent","astana","atrau","aktau"}
new_city=input("enter a city: ")
if  new_city in cities :
  cities.remove(new_city)
  print(f"{new_city} was removed fromthe set") 
else:
  print("No such city")
'''
# cities= {"almaty", "Astana", "Karaganda", "Aktau", "Transelvania"}
# new_city = input(" Enter a City: ")
# a = new_city.split()
# cities.update(a)
# print(cities)


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