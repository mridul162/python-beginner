# Creating a JSON file
book = {}
book['tom']={
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': '39393939'
}

book['bob']={
    'name': 'bob',
    'address': '1 red street, NY',
    'phone': '23232323'
}

# Writing to a JSON file
import json
s= json.dumps(book)         # Convert dictionary to JSON string
with open("D:\\programming\\python\\python_beginner\\book.txt", "w") as f:
    f.write(s)