with open("example.txt", "w") as file:
    file.write("Hello there!\n")
    file.write("Hello there again!\n")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)