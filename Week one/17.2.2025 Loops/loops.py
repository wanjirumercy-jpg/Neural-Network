# For loop
fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(fruit)


# Loop with range()
for i in range(5):
    print(i)

print("A range of 10")
for letter in range(10):
    print(letter)


# While Loop
# Repeat as long as a condition is True
i = 1
while i <= 5:
    print(i)
    i += 1


a = 0
while a <= 10:
    print(a)
    a += 2


# Using break to exit the loop
i = 1
while i < 10:
    if i == 5:
        break #Stops the loop when i is 5
    print(i)
    i += 1


#Loop Control Statements
# Using continue
for i in range(5):
    if i == 2:
        continue  #Skips when i is 2
    print(i)

#Using pass
for i in range(5):
    pass #Placeholder for future code


#Looping Through a Dictionary
#Loop through keys
student = {'name':'Mercy','age':22, 'course':'Data Science'}
for key in student:
    print(key)


# Loop through values
for value in student.values():
    print(value)


# Loop Through both keys and values
for key, value in student.items():
    print(f"{key}: {value}")


# Nested Loops
for i in range(1, 5): #Outer loop
    for j in range(1, 5): #Inner loop
        print(f"{i} x {j} = {i * j}")
    print("-----------")


# Using else with Loops
# With for loop
for i in range(5):
    print(i)

else:
    print("Loop completed!")


# With while loop
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop ended normally")


# Looping Through a String 
#Print each character
word = "Python"
for char in word:
    print(char)


# Looping Through a list with index (enumerate)
colors = ["red","green","blue"]
for index, color in enumerate(colors):
    print(f"Index {index}:{color}")


# EXAMPLE : LOOPING THROUGH A LIST OF DICTIONARIES (Dataset)
transactions = [
    {"customer":"Alice","amount":2500,"status":"Completed"},
    {"customer":"Bob","amount":150,"status":"Pending"},
    {"customer":"Charlie","amount":3200,"status":"Completed"},
    {"customer":"David","amount":500,"status":"Failed"}
]

#Print all transactions
for transaction in transactions:
    print(transaction)


# Filter and Print Only Completed Transactions
for transaction in transactions:
    if transaction['status'] == "Completed":
        print(f"Customer: {transaction['customer']}, Amount: {transaction['amount']}")


# Find the total amount of all transactions
total_amount = 0
for transaction in transactions:
    total_amount += transaction["amount"]

print(f"Total Amount: {total_amount}")


# Count the Number of completed transactions
count = 0
for transaction in transactions:
    if transaction["status"] == "Completed":
        count += 1

print(f"Total Comleted Transactions: {count}")


# Using enumerate() to track indexes
for index, transaction in enumerate(transactions, start=1):
    print(f"Transaction {index}: {transaction['customer']} paid {transaction['amount']}")


# # Advanced Use Case: Looping Through a Pandas DataFrame
# import pandas as pd

# #Creating a DataFrame
# data = {
#     "Customer":["Alice","Bob","Charlie","David","Eve"],
#     "Amount": [2500, 150, 3200, 500, 1000],
#     "Status": ["Completed","Pending","Completed","Failed","Completed"]

# }

# df = pd.DataFrame(data)
# print(df)































































































































