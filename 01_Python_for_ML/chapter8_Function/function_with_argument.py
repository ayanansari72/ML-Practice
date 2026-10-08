def goodboy(name,ending="chala ja"):
    print("Good boy:"+name)
    print(ending)
    return "ok"
a=goodboy("Raju")       
print(a)
goodboy("Ramu","beta")

"""
Output:
Good boy:Raju
chala ja
ok
Good boy:Ramu
beta
ok
"""

def goodDay(name, ending):     #function definition with default arguments
    print("Good Day, " + name)
    print(ending)
    return "ok"

b = goodDay("Harry", "Thank you") 
print(b)

"""Output:
Good Day, Harry
Thank you
ok 
"""