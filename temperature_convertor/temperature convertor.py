import customtkinter as ctk

# Temperature convertion functions
def celsius_to_fahrenheit(celsius): return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit): return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius): return celsius + 273.15

def kelvin_to_celsius(kelvin): return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit): return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin): return (9/5) * (kelvin - 273.15) + 32

def get_temperature():
    return input('Please enter a temperature with its temperature unit (C, F, or K): ').strip()
# temperature validator
def validate_temperature():
    """Checks and validates temperature input"""
    while True:
        try:
            temperature = get_temperature()
            if not temperature or len(temperature) < 2:
                print('Your input must contain al least one number and the unit of temperature')
                continue
            temperature_unit = temperature[-1].upper()

            if temperature_unit not in ['C', 'F', 'K']:
                print('Reminder! Temperature can be either C (celsius), K (kelvin) or F (fahrenheit)')
                continue

            number_unit = float(temperature[:-1].strip())
        except ValueError:
            print('Please enter valid number')
            continue
        else:
            return number_unit, temperature_unit

def main():
    """This is main function. Converts temperatures"""
    number, unit = validate_temperature()
    c_to_f = celsius_to_fahrenheit(number)
    c_to_k = celsius_to_kelvin(number)
    f_to_k = fahrenheit_to_kelvin(number)
    f_to_c = fahrenheit_to_celsius(number)
    k_to_c = kelvin_to_celsius(number)
    k_to_f = kelvin_to_fahrenheit(number)
    if unit == 'C':
        result1 = f'{c_to_f:.2f} fahrenheit'
        result2 = f'{c_to_k:.2f} kelvin'
    elif unit == 'F':
        result1 = f'{f_to_c:.2f} celsius'
        result2 = f'{f_to_k:.2f} kelvin'
    elif unit == 'K':
        result1 = f'{k_to_c:.2f} celsius'
        result2 = f'{k_to_f:.2f} fahrenheit'

    return f'{number}{unit} is equal to {result1} and {result2}.'

if __name__ == '__main__':
    print(main())