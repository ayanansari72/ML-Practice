# with open("learnSample.txt", "r", encoding="utf-8") as f:
#     data = f.read()
#     print(data)
# import os
# print(os.getcwd())


st="hello world" \
"this is a test file" \
"we are writing multiple lines" \
"to see how it works"
st1=''' Dil ki basti purani hai,
Magar yaad teri nayi hai,
Humne toh sirf ishq kiya tha,
Par sazaa puri zindagi ki payi hai 
hii ayan
hii bro
hii men'''
f=open("no.txt","w")
f.write(st)
f.write(st1)
f.close()
with open("no.txt", "r") as f:
    data = f.read()
    print(data)