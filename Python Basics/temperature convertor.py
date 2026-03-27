def convert_temperature(temp):
    try:
        # check length of input and count the number of alphabetic characters
        if len(temp) < 2:
            raise ValueError(
                'Wrong input. It must contain number and unit of temperature')
        count = 0
        for t in temp:
            if t.isalpha():
                count += 1
        if count > 1:
            raise ValueError(
                'Wrong input. It must contain only one unit of temperature')
        # extract the last character as the unit and the rest as the number
        char = temp[-1].upper()
        number = float(temp[:-1].strip())
        # convertion
        c_to_f = (number * 9/5) + 32
        f_to_c = (number - 32) * 5/9
        c_to_k = number + 273.15
        k_to_c = number - 273.15
        f_to_k = (number - 32) * 5/9 + 273.15
        k_to_f = (9/5) * (number - 273.15) + 32
        if char == 'C':
            result1 = f'{c_to_f:.2f} fahrenheit'
            result2 = f'{c_to_k:.2f} kelvin'
        elif char == 'F':
            result1 = f'{f_to_c:.2f} celsius'
            result2 = f'{f_to_k:.2f} kelvin'
        elif char == 'K':
            result1 = f'{k_to_c:.2f} celsius'
            result2 = f'{k_to_f:.2f} fahrenheit'
        else:
            raise ValueError(
                'Wrong input. It must contain only one unit of temperature (C or F)')
    except ValueError as e:
        print(e)
    except TypeError:
        print('Please enter valid input')
    else:
        return f'{number} {char} is equal to {result1} and {result2}.'


print(convert_temperature('89K'))
