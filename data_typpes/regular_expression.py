import re

text = "The rain in Spain"
x = re.search("^The.*Spain$", text)
if x:
  print("YES! We have a match!")
else:
  print("No match")



text = "My phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, text)

if match:
  print("Phone number found:", match.group())  # Output: 123-456-7890

txt2 = "The rain in Spain"
match2 = re.findall("ai", txt2)
if match2:
  print(match2)  # Output: ['ai', 'ai']

txt3 = "The rain in Spain"
replace_txt = "india"
new_txt = re.sub("Spain", replace_txt, txt3)
print(new_txt)  # Output: The rain in india
