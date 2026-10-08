#ps1
# words ={
#     "madad": "help",
#     "salam": "hello",
#     "ketab": "book",
#     "doost": "friend",      
# }
# print(words["madad"])
# word = input("enter a word in urdu :")
# print("MEANING:",words[word])

#ps2
# s=set() 
# n= input("enter number")
# s.add(int(n))
# n= input("enter number")
# s.add(int(n))
# n= input("enter number")
# s.add(int(n))
# n= input("enter number")
# s.add(int(n))
# n= input("enter number")
# s.add(int(n))
# n= input("enter number")
# s.add(int(n))
# print(s)

#ps
# a=set()
# a.add(18)
# a.add('18')
# print(a,len(a),type(a))  #{18, '18'} 2 <class 'set'>

#ps4
b=set()
b.add(20)
b.add('20')
b.add(20.0)
print(b,len(b),type(b))  #{20, '20'} 2 <class 'set'>

#ps5
s={}
print(s,type(s))  # {} <class 'dict'>

#ps6
d={}  # empty dictionary
name = input("Enter your name: ")
lang= input("Enter your favorite programming language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang= input("Enter your favorite programming language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang= input("Enter your favorite programming language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang= input("Enter your favorite programming language: ")
d.update({name: lang})
name = input("Enter your name: ")
lang= input("Enter your favorite programming language: ")
d.update({name: lang})
print(d)  # prints the dictionary with names and their favorite programming languages