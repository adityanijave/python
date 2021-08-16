 #using def convert celsius to fahrenheit :

def celsius_to_fahrenheit(celsius):
     fahrenheit =(celsius*( 9/5) + 32)
     return fahrenheit
 
celsius = int(input("Enter Temperature in Celsius :\n"))
print("\nTemperature in Fahrenheit is:\n" +str( celsius_to_fahrenheit(celsius)))
