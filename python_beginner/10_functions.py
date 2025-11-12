# An example of functions in Python
tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

# Without using functions, repeating same statements
total = 0
for item in tom_exp_list:
    total= total+item
print("Tom's total expenses: ", total)

total = 0
for item in joe_exp_list:
    total= total+item
print("Joe's total expenses: ", total)

# Using functions to avoid repetition
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total+item
    return total

toms_total= calculate_total(tom_exp_list)
joes_total= calculate_total(joe_exp_list)

print("Tom's total expenses: ", toms_total)
print("Joe's total expenses: ", joes_total)

# Function with default argument
# total=0           # global variable
def sum(a,b=0):
    """
    This function takes two arguments which are integer numbers,
    and it will return sum of them as an output.
    :param a:
    :param b:
    :return: 
    """
    print("a: ", a)
    print("b: ", b)
    total= a+b      # local variable
    print("Total Inside: ", total) #
    return total  

n = sum(5)
print("Total Outside: ", n)
print("Total Outside: ", total)