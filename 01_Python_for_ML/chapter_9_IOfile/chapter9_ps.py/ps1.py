
with open("poem.txt","r") as f:
    a=f.read()
if("twinkle" in a):
    print("Yes")
else:
    print("No")