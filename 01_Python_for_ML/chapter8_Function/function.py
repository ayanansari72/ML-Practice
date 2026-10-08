def avg(): #function definition
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    c= int(input("Enter third number: "))
    average = (a + b + c) / 3       
    print("The average is:", average)

avg() #function call without arguments
print("1") #function call without arguments
avg("2") #function call with arguments will raise TypeError
