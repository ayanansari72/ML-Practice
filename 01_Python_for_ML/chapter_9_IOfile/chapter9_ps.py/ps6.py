with open("findpython.txt", "r") as f:
    content = f.read()
if "python" in content:
    print("Yes, 'Python' is present in the file.")  
else :
    print("No, 'Python' is not present in the file.")