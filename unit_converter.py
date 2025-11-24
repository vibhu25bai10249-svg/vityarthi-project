import time


def print_header():
    print("=" * 50)
    print("      MULTI-PURPOSE UNIT CONVERTER")
    print("=" * 50)


def get_user_choice(options):
    """function to display options and get a valid input from user"""
    options_list = list(options)
    for i, option in enumerate(options_list, 1):
        print(f"{i}. {option.title()}")

    while True:
        try:
            choice = int(input("\nEnter choice number: "))
            if 1 <= choice <= len(options_list):
                return options_list[choice - 1]
            else:
                print("Invalid number. Please select from the list.")
        except ValueError:
            print("Please enter a valid number.")


def convert_length(value, from_unit, to_unit):
    # conversio from meter to feet
    if from_unit == "meter" and to_unit == "feet":
        return value * 3.28084
    return None


def convert_temperature(value, from_unit, to_unit):
    # conversion from fahrenheit to celsius
    if from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5 / 9
    return None


def convert_volume(value, from_unit, to_unit):
    # conversion from litre to millilitre
    if from_unit == "litre" and to_unit == "millilitre":
        return value * 1000
    return None


def convert_weight(value, from_unit, to_unit):
    # conversion from kg to gram,anf=d then from gram to miligram
    if from_unit == "kilogram" and to_unit == "gram":
        return value * 1000
    elif from_unit == "gram" and to_unit == "milligram":
        return value * 1000
    return None


def convert_data(value, from_unit, to_unit):
    # conversion from mb to kb,and from kb to bytes
    # 1024 bytes in 1 mb
    if from_unit == "megabytes (mb)" and to_unit == "kilobytes (kb)":
        return value * 1024
    elif from_unit == "kilobytes (kb)" and to_unit == "bytes":
        return value * 1024
    return None


def convert_power(value, from_unit, to_unit):
    # conversion from horsepower to watts
    if from_unit == "horsepower" and to_unit == "watts":
        return value * 745.7
    return None


def main():
    # Defining the structure of available conversion based on user input
    conversion_map = {
        "LENGTH": {
            "meter": ["feet"]
        },
        "TEMPERATURE": {
            "fahrenheit": ["celsius"]
        },
        "VOLUME": {
            "litre": ["millilitre"]
        },
        "WEIGHT": {
            "kilogram": ["gram"],
            "gram": ["milligram"]
        },
        "DATA": {
            "megabytes (mb)": ["kilobytes (kb)"],
            "kilobytes (kb)": ["bytes"]
        },
        "POWER": {
            "horsepower": ["watts"]
        }
    }

    logic_map = {
        "LENGTH": convert_length,
        "TEMPERATURE": convert_temperature,
        "VOLUME": convert_volume,
        "WEIGHT": convert_weight,
        "DATA": convert_data,
        "POWER": convert_power
    }

    while True:
        print_header()
        print("\nselect the type of quantity:")
        # 1. ask user for the type of quantity
        category = get_user_choice(conversion_map.keys())

        print(f"\n--- {category} conversion ---")
        print("celect the primary quantity (convert FROM):")

        # 2. ask user for unit that has to be converted
        available_sources = conversion_map[category].keys()
        primary_unit = get_user_choice(available_sources)

        print(f"\nselected primary: {primary_unit.title()}")
        print("select the secondary quantity (Convert INTO):")

        # 3. ask user for the quantity to which the first quantity is to be converted intpo
        available_targets = conversion_map[category][primary_unit]

        secondary_unit = get_user_choice(available_targets)

        # 4. get the numerical value
        while True:
            try:
                val_str = input(f"\nenter the value in {primary_unit}: ")
                value = float(val_str)
                break
            except ValueError:
                print("invalid input. Please enter a numeric value (e.g., 5, 10.5).")

        # 5. perform calculation
        converter_func = logic_map[category]
        result = converter_func(value, primary_unit, secondary_unit)

        # 6. show result
        print("-" * 40)
        if result is not None:
            # formatting to 4 decimal places for precision, removing trailing zeros
            formatted_res = f"{result:.4f}".rstrip('0').rstrip('.')
            print(f"RESULT: {value} {primary_unit} = {formatted_res} {secondary_unit}")
        else:
            print("conversion logic error. Please contact developer.")
        print("-" * 40)

        # 7. continue or exit
        again = input("\ndo you want to perform another conversion? (y/n): ").lower()
        if again != 'y':
            print("\nexiting program.")
            break
        print("\n" * 2)  # Add some space for the next go


if __name__ == "__main__":
    main()