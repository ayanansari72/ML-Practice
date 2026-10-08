word = "gadha"

with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "donkey")
counter = content.count(word)
print(f"The word '{word}' has been replaced {counter} times.")

with open("donkey.txt", "w") as f:
    f.write(contentNew)