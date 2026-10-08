a= int(input("Enter your age : "))

# message = "You are eligible to vote." if a >= 18 else "You are not eligible to vote."
# print(message)
  
  #multiple if_elif_else statements ladder using conditional expression
if (a ==0):
    print("Age cannot be zero.")

    #condition 1 is end here

if (a < 0):   
    print("Age cannot be negative.")

    #condition 2 is end here


if a >= 18:
    print("You are eligible to vote.")
elif a >= 16:
    print("You are eligible to drive.")
elif a >= 14:
    print("You are eligible to ride a bicycle.")

    #condition 3 is end here
else:
    print("You are not eligible for any activity.")

   
print("Thank you!")
