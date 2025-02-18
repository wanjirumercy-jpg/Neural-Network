# List is a collection of items in Python that is ordered and mutable(Can be changed)
# It is defined using a square bracjket; []

fruits = ['mango','apple','banana']
print(fruits)


# Creating Lists
numbers = [1, 2, 3, 4, 5] # a list of integers
names = ['Joan','Daniel', 'Jerry','Sam','Dora'] # a list of stings
mixed = ['Nancy',7,True,0.34] # List with different data types
empty_list = [] # An empty list
print(numbers)
print(names)
print(mixed)
print(empty_list)


# Accessing Elements in a list
animals = ['cow','goat','sheep']
#Accessing the first element
print(animals[0])
#Accessing the last element
print(animals[2])


# Modifying Lists
names = ['Joy','Jeff','Cherry']
names[1] = 'Rose' #Change 'Jeff' to 'Rose'
print(names)


# Adding Elements to a list, usingg either append(),insert(), or extend()
food = ['Pilau','Rice']
food.append("Yams") # Adds at the end
print(food)


food.insert(1, 'Ugali') #inserts at index 1
print(food)


food.insert(2, 'Potatoes')
print(food)


more_food = ['Githeri','Kales']
food.extend(more_food) #Add multiple items
print(food)


#Removing Elements from a List, using either remove(),pop(), or del
drinks = ['Tea', 'Coffee','Chocolate']
drinks.remove('Coffee')
print(drinks)


drinks.pop(0) #Removes the first element
print(drinks)

del drinks[0]
print(drinks)


# Looping Through a List
fruits = ['Apple','Banana','Cherry']
for fruit in fruits:
    print(fruit)


# Checking if an Item Exists in a List
fruits = ['Apple','Banana','Cherry']
if 'Banana' in fruits:
    print('Banana is in the list!')


# Sorting and Reversing a List
numbers = [3, 1, 4, 2, 5]
numbers.sort()
print(numbers)


numbers.reverse()
print(numbers)


# List Comprehension 
numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)


original = [1, 2, 3]
copy_list = original.copy()
print(copy_list)


# Finding the Length of a List
fruits = ['Apple','Banana','Cherry']
print(len(fruits))


# Exercise
colors = ['Red','Blue','Pink','Orange','Yellow']
print(colors)

colors.append('Purple')
print(colors)

colors.remove('Red')
print(colors)

for color in colors:
    print(color)














































































































































































