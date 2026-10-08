def inch_to_cm(inch):
    return inch * 2.54
inch = float(input("Enter length in inches: "))
cm = inch_to_cm(inch)  #function call with argument Stores it in cm

print(f"The length in centimeters is: {round(cm, 2)} cm")