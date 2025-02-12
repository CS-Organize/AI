dictionary = {
    "name": "John",
    "age": 30,
    "isStudent": False
}

print(dictionary)

dictionary["address"] = "123 Main St"
dictionary[42] = "Seoul"

print(dictionary)

# Get the value of a key
print(dictionary["name"])
print(dictionary.get("name"))

# If the key is not found, it will return None
print(dictionary.get("phone"))
print(dictionary.get("phone", "Not Found"))

# Update the value of a key
dictionary["name"] = "Jane"
print(dictionary)

# Remove a key
del dictionary["age"]
print(dictionary)

# Get all the keys
print(dictionary.keys())

# Get all the values
print(dictionary.values())

# Get all the items
print(dictionary.items())

# Loop through the dictionary
for key in dictionary:
    print(key, dictionary[key])

for key, value in dictionary.items():
    print(key, value)

# Check if a key exists
print("name" in dictionary)
print("phone" in dictionary)

# Check if a value exists
print("John" in dictionary.values())
print("123 Main St" in dictionary.values())

# Clear the dictionary
# dictionary.clear()
dictionary = {}
print(dictionary)
