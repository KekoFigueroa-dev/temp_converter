# Program: Temperature Conversion App
# Description: This program converts Fahrenheit temperatures to Celsius and Kelvin

#====== Welcome Section ======#
# Display welcome message
print("Welcome to the Temperature Conversion App")

#====== User Input Section ======#
# Get temperature in Fahrenheit (allows decimals)
while True:
    try:
        temp_fahrenheit = float(input("What is the given temperature in degrees Fahrenheit: "))
        break
    except ValueError:
        print("Please enter a valid number")

#====== Conversion Section ======#
# Convert Fahrenheit to Celsius
temp_celsius = (temp_fahrenheit - 32) * 5/9
# Convert Fahrenheit to Kelvin
temp_kelvin = (temp_fahrenheit - 32) * 5/9 + 273.15
# Round all results to 4 decimal places
rounded_fahrenheit = round(temp_fahrenheit, 4)
rounded_celsius = round(temp_celsius, 4)
rounded_kelvin = round(temp_kelvin, 4)

#====== Display Section ======#
# Show all three temperatures in aligned format
print(f"Degrees Fahrenheit: {rounded_fahrenheit}\nDegrees Celsius: {rounded_celsius}\nDegrees Kelvin: {rounded_kelvin}")

print("You for testing my app")