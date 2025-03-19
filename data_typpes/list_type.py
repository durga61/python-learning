# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(fruits[0])
print(numbers[1:])
print(mixed[:3])


fruits[0] = "kiwi"
fruits.append("orange")

print(fruits)

fruits.remove("banana") 
fruits.pop()

fruits.insert(1, "mango")

fruits.append("banana")
fruits.append("banana2")

print(fruits)
for i in fruits:
  fruits_str = " ".join(fruits)

print(fruits_str)

if "apple" in fruits:
    print("Yes, apple is in the fruits list")