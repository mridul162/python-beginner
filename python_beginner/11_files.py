f = open("C:\\data\\fun.txt", "r+")
# f.write("I love C")
print(f.read())
f.close()

print(f.closed)
#######################################

# f = open("C:\\data\\funny.txt", "r")
# f_out = open("C:\\data\\funny_wc.txt", "w")
# for line in f:
#     tokens = line.split(' ')
#     f_out.write(" wordcount: "+ str(len(tokens))+ " " +line)
#     print(len(tokens))
# f.close()
# f_out.close()

#######################################
# With Statement
#######################################
with open("C:\\data\\funny.txt", "r") as f:
    print(f.read())
print(f.closed)
