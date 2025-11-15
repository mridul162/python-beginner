# File Handling in Python
# r - read
# w - write
# a - append
# r+ - read and write

# 1. Open a file
f = open("D:\\programming\\python\\python_beginner\\fun.txt", "r+")
# f.write("I love C")       # Write to the file (overwrites existing content)
print(f.read())             # Read the file content
f.close()                   # Close the file
print(f.closed)             # Check if the file is closed

# 2. Append to a file
f = open("D:\\programming\\python\\python_beginner\\fun.txt", "a")
f.write("\nI love Python") # Append to the file
f.close()

# 3. Read line by line
print("Reading line by line:")
f = open("D:\\programming\\python\\python_beginner\\funny.txt", "r")
f_out = open("funny_wc.txt", "w") # Output file to write word counts
for line in f:
    tokens = line.split(' ')      # Split line into words
    f_out.write(" wordcount: "+ str(len(tokens))+ " " +line) 
    print(len(tokens))       
f.close()
f_out.close()

# 4. Using 'with' statement
with open("D:\\programming\\python\\python_beginner\\funny.txt", "r") as f:
    print(f.read())
print(f.closed)
