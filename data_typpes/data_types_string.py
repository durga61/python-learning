str1 = "Hello world"
str2 = "To the Python world"
print(f"{str1}, {str2}")
print(str1 + "       " + str2)
print(str1.split())
print(str1.split("o"))
print(str1.strip())
str_list = str1.split()
print("length of str_list", len(str_list))
sentance = " ".join(str_list)
print(sentance)
print("length of str1", len(str1))
print(str1[1:4])
print(len(str1.split()))
print(str1.upper())
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.startswith("H"))
print(str1.endswith("d"))
print(str1.find("world"))

new_str = str1.replace("world", "Python")
print(new_str)

fruit = ["apple", "banana", "cherry"]
print("fruit list", fruit)
str_fruit = " ".join(fruit)
print(str_fruit)
txt = "  I am a Python programmer    "
print(txt)
print(txt.strip())