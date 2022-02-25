programming_dictionary = {
    "Bug": "A software error", 
    "Function": "A group of statements that perform a task", "Variable": "A name that holds a value", 
    "List": "A collection of items", 
    "Dictionary": "A collection of key-value pairs",
    }

# retrieve items from the dictionary
print(programming_dictionary["Bug"])

# adding new items to the dictionary
programming_dictionary["Boolean"] = "True or False"
print(programming_dictionary)

# empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
print(programming_dictionary)

# edit an item in the dictionary
programming_dictionary["Bug"] = "bug?"
print(programming_dictionary)

# loop through the dictionary
for key, value in programming_dictionary.items():
    print(key, value)