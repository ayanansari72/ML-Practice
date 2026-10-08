# a1= int(input("Enter the first number : "))
# a2= int(input("Enter the second number : ")) 
# a3= int(input("Enter the third number : "))
# a4= int(input("Enter the fourth number : "))
# # Find the greatest number among four numbers using conditional expressions
# if (a1 >= a2) and (a1 >= a3) and (a1 >= a4):
#     greatest = a1
# elif (a2 >= a1) and (a2 >= a3) and (a2 >= a4):
#     greatest = a2
# elif (a3 >= a1) and (a3 >= a2) and (a3 >= a4):
#     greatest = a3
# else:
#     greatest = a4

# print("The greatest number among the four is:", greatest)   


#ps2
# x1= int(input("Enter the number : "))
# x2= int(input("Enter the second number :  "))
# x3= int(input("Enter the third number : "))

# total_percentage= (x1 + x2 + x3)/300 * 100

# if (total_percentage >=40 and x1>=33 and x2>=33 and x3>=33):
#     print("You have been promoted")
# else:
#     print("You have not been promoted")

# print("Your total percentage is :", total_percentage)


#ps3
# a= input("Enter the text comment : ")
# if ("make a lot of money" in a) or ("buy now" in a) or ("click this" in a) or ("subscribe this" in a):
#     print("This is a spam message")
# else:
#     print("This is not a spam message")


       #method 2
# spam_keywords = ["make a lot of money", "buy now", "click this", "subscribe this"]
# a = input("Enter the text comment: ") 
# if any(keyword in a for keyword in spam_keywords):
#     print("This is a spam message")
# else:
#     print("This is not a spam message")

  #method 3
# p1="make a lot of money"
# p2="buy now"
# p3="click this"
# p4="subscribe this"
# a= input("Enter the text comment : ")
# if (p1 in a) or (p2 in a) or (p3 in a) or (p4 in a):
#     print("This is a spam message")
# else:   
#     print("This is not a spam message")
    

#ps4
# username= input("Enter your username : ")
# if len(username) <10:
#     print("Username is valid")
# else:
#     print("Username is not valid")    


#ps5
# name = input("Enter your name : ")
# find_name=['ayan','saniya','ayaz','shiblu']
# if name in find_name:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present in the list")


# ps6
# marks= int(input("Enter your marks : "))

# if marks<=100 and marks >=90:
#     grade= "Excellent"
# elif marks<90 and marks >=80:
#     grade= "A"
# elif marks<80 and marks >=70:        
#     grade= "B"
# elif marks<70 and marks >=60:
#     grade= "C"
# elif marks<60 and marks >=50:
#     grade= "D" 
# else:
#     grade= "Fail"

# print("Your grade is :", grade)


#ps7
# year= int(input("Enter the year : "))     
# if (year % 4==0 and year % 100 !=0) or (year %400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

#ps8
a= input("Enter the post: ")
if("ayan"in a.lower()) or ("saniya"in a.lower()) or ("ayaz"in a.lower()) or ("shiblu"in a.lower()):
    print("This post is talking about you"  )
else:
    print("This post is not talking about you")

