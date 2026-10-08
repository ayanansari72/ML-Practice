# items={ "Ayan": 25,
#         "Saniya": 30, 
#         "ayaz": 22,
#         0: "zero"


# }
# print(items,type(items))
# print(len(items))  # prints the number of key-value pairs in the dictionary
# print(items["Ayan"])  # Accessing value using key
# print(items)
# items["Ayan"]=26  # Updating value for key "Ayan"
# print(items)

#methods in dictionary
items={ "Ayan": 25,
        "Saniya": 30, 
        "ayaz": 22,
        0: "zero"
}
print(items.keys())  # prints all the keys in the dictionary
print(items.values())  # prints all the values in the dictionary
print(items.items())  # prints all the key-value pairs as tuples in a list
print(items.get("Saniya"))  # Accessing value using get() method
print(items.get("Unknown", "Not Found"))  # Accessing non-existing key with default value
print(items)
items.update({"Ayan": 27, "NewKey": "NewValue"})  # Updating existing key and adding new key-value pair
items.update({"Saniya": 31})  # Updating existing key
print(items)
items["Ayan"]=26  # Another way to update existing key

print(items)
items.pop("ayaz")  # Removing key-value pair using pop() method
print(items) 
items.popitem()  # Removing the last inserted key-value pair
print(items)      
