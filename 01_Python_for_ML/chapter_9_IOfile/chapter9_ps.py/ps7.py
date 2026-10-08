with open("findpython.txt") as f:
    lines = f.readlines()

lineno = 0
for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno = lineno + 1

else:
    print("No Python is not present")