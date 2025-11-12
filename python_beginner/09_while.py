# An example of while loop
i=1
while i<=5:
    print(i)
    i = i+1

# Calculating total expense without while loop
exp= [2340, 2500, 2100, 3100, 2980]
total = exp[0]+ exp[1]+exp[2]+exp[3]
print(total)

# Calculating total expense with while loop
total=0
i = 0
while i < len(exp):
    total= total + exp[i]
    i = i+1
print(total)

# Sum of first 10 natural numbers
sum = 0
i = 1
while i<=10:
    sum= sum+i
    i = i+1
print(sum)

# Displaying month-wise expense
exp= [2340, 2500, 2100, 3100, 2980]
total = 0
i = 0
while i < len(exp):
    print('Month:', (i+1), 'Expense: ',exp[i])
    total = total+ exp[i]
    i = i+1
print("Total: ", total)

# Finding an item using while loop with break
key_location ="chair"
locations=["garage", "living room", "chair", "closet"]
index=0
while index < len(locations):  
    if locations[index]==key_location:
        print("Key is found in ",locations[index])
        break
    else:
        print("Key is not found in ",locations[index])
    index = index+1
print("Search is over.")

# Using continue to print squares of odd numbers only
num=1
while num<=10:
    if num%2==0:
        num = num+1
        continue
    print(num*num)
    num = num+1

# Taking multiple inputs using while loop
count=0
fruits = []
while count<3:
    item = input("Enter the fruit: ")
    fruits.append(item)
    count = count+1
print("Fruits you entered are: ", fruits)