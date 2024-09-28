# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main function to handle user input and conversion
def main():
    try:
        # Prompt user for temperature input
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt user for the temperature unit (Celsius or Fahrenheit)
    unit = (
        input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    )

    if unit == "C":
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
