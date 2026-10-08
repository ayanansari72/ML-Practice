## Arithmetic Operations Module
a=88
b=44
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)               
print("Division:", a / b)

#Assignment Operations
a= 100-11
a /= 90
b=6
b += 3
print("Value of a after assignment:", a)
print("Value of b after += :", b)

#Comparison Operations
d= 8>=9
e= 5==5
print("Is 8 greater then equal to 9?:", d)
print("Is 5 equal to 5?:", e)

#Logical Operations                                 
x= True
y= False            
print("Logical AND(x and y):", x and y)
print("Logical OR (x or y):", x or y)
print("Logical NOT (ot x):", not x)
print("Logical NOT (not y):", not y)

#Bitwise Operations
p= 5 & 3
q= 5 | 3
r= 5 ^ 3
print("Bitwise AND (5 & 3):", p)
print("Bitwise OR (5 | 3):", q)     
print("Bitwise XOR (5 ^ 3):", r)    
s= ~5
print("Bitwise NOT (~5):", s)
t= 5 << 1
u= 5 >> 1
print("Left Shift (5 << 1):", t)
print("Right Shift (5 >> 1):", u)
#Membership Operations
list1= [10, 20, 30, 40, 50]
print("Is 20 in list1?:", 20 in list1)
print("Is 60 not in list1?:", 60 not in list1)
#Identity Operations
m= 10
n= 10
print("Does m is n?:", m is n)
print("Does m is not n?:", m is not n)      
#Special Operators
import math
num= 16
sqrt_num= math.sqrt(num)
print("Square root of", num, "is:", sqrt_num)
power_num= math.pow(2, 4)
print("2 raised to the power 4 is:", power_num)
log_num= math.log(100, 10)
print("Logarithm of 100 to base 10 is:", log_num)
exp_num= math.exp(2)
print("Exponential of 2 is:", exp_num)
factorial_num= math.factorial(5)
print("Factorial of 5 is:", factorial_num)
#Ternary Operator
age= 20
status= "Adult" if age >= 18 else "Minor"
print("Person is an:", status)
#Unary Operators
num1= 10
num2= -num1
print("Original number:", num1)
print("Negated number:", num2)      