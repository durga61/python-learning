try:
    # Open the file for reading
    with open("greet.py", "r") as file:
        # Reading an Entire File
        data = file.read()

    print(f" no of words: {len(data.split())}")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print("An error occurred:", e)
