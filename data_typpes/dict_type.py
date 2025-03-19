
person = {
    "name" : "John",
    "age" : 30,
    "address" : "Benguluru"
}

print(person)
print(person["name"])
print(person.get("age"))
print(person.get("phone", "Phone number not available"))
print(person.get("phone"))
print(person.keys())
print(person.values())
print(person.items())

person["name"] = "Jane"
print(person)
person["Job"] = "Developer"
print(person)

person.pop("Job")
print(person)

for key,val in person.items():
    print(f" {key} : {val}")

for key in person.keys():
    print(f" {key} : {person[key]}")
    
for val in person.values():
    print(val)

if "age" in person:
    print("Yes, age is one of the keys in the person dictionary")   