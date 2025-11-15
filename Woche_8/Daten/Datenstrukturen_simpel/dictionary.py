# store data values in key:value pairs (changeable)
# key values cannot be duplicates ("name" can't be used twice)
person = {
    "name": "Frieder", 
    "city": "Rapperswil"
}
print(person["name"])
print(person["city"])

# changeable

get(key) – Returns the value for the key:
print(person.get("name"))  # Outputs: Alice
keys() – Returns a list of all keys:
print(person.keys())  # Outputs: dict_keys(['name', 'age'])
values() – Returns a list of all values:
print(person.values())  # Outputs: dict_values(['Alice', 25])
items() – Returns all key-value pairs:
print(person.items())  # Outputs: dict_items([('name', 'Alice'), ('age', 25)])
update() – Adds or updates items:
person.update({"city": "Mumbai"})
pop(key) – Removes a key-value pair by key:
person.pop("age")
clear() – Removes all items from the dictionary:
person.clear()