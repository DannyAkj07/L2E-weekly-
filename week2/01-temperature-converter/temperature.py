def celsius_to_fahrenheit(celsius):
    # Write your code here
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    # Write your code here
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    # Write your code here
    return celsius + 273.15


def convert_temperature(value, from_unit, to_unit):
    # Write your code here
    if type(value) == bool or not isinstance(value, (int, float)):
        raise ValueError("Not a valid number. Must be int or float")
    
    if not (isinstance(from_unit,str) and isinstance(to_unit,str)):
        raise ValueError("Not a valid temperature")
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    valid_inputs = ["celsius", "fahrenheit", "kelvin"]

    if from_unit not in valid_inputs or to_unit not in valid_inputs:
        raise ValueError("Unsupported unit written.")

    if from_unit == "celsius" and value < -273.15:
        raise ValueError("Temperature below celsius point")

    elif from_unit == "fahrenheit" and value < -459.67:
        raise ValueError("Temperature below fahrenheit point")

    elif from_unit == "kelvin" and value < 0:
        raise ValueError("Temperature below kelvin point")

    if from_unit == "celsius":
        celsius_value = value
    elif from_unit == "fahrenheit":
        celsius_value = fahrenheit_to_celsius(value)
    elif from_unit == "kelvin":
        celsius_value = value - 273.15

    if to_unit == "celsius":
        return celsius_value
    elif to_unit == "fahrenheit":
        return celsius_to_fahrenheit(celsius_value)
    elif to_unit == "kelvin":
        return celsius_to_kelvin(celsius_value)


print(convert_temperature(25, "celsius", "celsius"))
