def c(f_temp):
    return (f_temp - 32) * 5/9
f_temp = float(input("Enter temperature in Fahrenheit: "))
c_temp = c(f_temp)
print(f"The temperature in Celsius is: {round(c_temp, 2)}°C") 

