# Examples of for loop in Python

# Calculating total expense without for loop
exp= [2340, 2500, 2100, 3100, 2980]
total = exp[0]+ exp[1]+exp[2]+exp[3]
print(total)

# Calculating total expense with for loop
total=0
for item in exp:
    total= total + item
print(total)

# Sum of first 10 natural numbers
sum = 0
for i in range(1,11):
    sum= sum+i
print(sum)

# Displaying month-wise expense
exp= [2340, 2500, 2100, 3100, 2980]
total = 0
for i in range(len(exp)):
    print('Month:', (i+1), 'Expense: ',exp[i])
    total = total+ exp[i]
print("Total: ", total)

# Finding an item using for loop with break
key_location ="chair"
locations=["garage", "living room", "chair", "closet"]
for i in locations:
    if i==key_location:
        print("Key is found in ",i)
        break
    else:
        print("Key is not found in ",i)
print("Search is over.")

# Using continue to print squares of odd numbers only
for i in range(1,11):
    if i%2==0:
        continue
    print(i*i)

# Taking multiple inputs using for loop
fruits = []
for i in range (3):
    item = input("Enter the fruit: ")
    fruits.append(item)
print("Fruits you entered are: ", fruits)

