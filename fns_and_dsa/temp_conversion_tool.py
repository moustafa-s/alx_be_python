# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global factor to convert Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global factor to convert Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main function to handle user interaction
def main():
    try:
        # Prompt the user to enter the temperature
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        # Handle invalid input for temperature
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt the user to enter the unit of temperature (Celsius or Fahrenheit)
    unit = (
        input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    )

    # Determine the conversion based on the input unit
    if unit == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# Check if the script is run directly
if __name__ == "__main__":
    main()
