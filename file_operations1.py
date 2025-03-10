def find_welcome_word(filename):
    with open(filename, "r") as file:
        for line in file:
            if "welcome" in line.lower():
                print(line.strip())


filename = "greet.py"
find_welcome_word(filename)
