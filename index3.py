''' Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!)
 and outputs the temperature converted to Celsius.'''

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Get input from the user
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_output = fahrenheit_to_celsius(fahrenheit_input)

print(f"{fahrenheit_input:.2f}°F is equivalent to {celsius_output:.2f}°C")

                                                                         