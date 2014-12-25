# Unit Converter
#
#   handles temp, currency, volume, mass, etc
#
#   to-do list:
#       [X] celsius -> fahrenheit
#       [X] fahrenheit -> celsius
#       [X] lb -> kg
#       [X] kg -> lb

def uconv(u_in, u_out, value):
    u_in = u_in.lower()
    u_out = u_out.lower()

    if u_in == 'celsius' or 'c' in u_in and u_out == 'fahrenheit' or 'f' in u_out:
        value_conv = value * 1.8 + 32

    elif u_in == 'fahrenheit' or 'f' in u_in and u_out == 'celsius' or 'c' in u_out:
        value_conv = (value - 32) / 1.8

    elif u_in == 'kilograms' or 'kg' in u_in and u_out == 'pounds' or 'lb' in u_out:
        value_conv = value * 2.2046

    elif u_in == 'pounds' or 'lb' in u_in and u_out == 'kilograms' or 'kg' in u_out:
        value_conv = value / 2.2046
    
    else:
        return ("Not valid input/output conversion values")
    
    return str(value) + " " + u_in + " --> " + str(value_conv) + " " + u_out

# Test cases
#print (uconv('Celsius', 'Fahrenheit', 47.5))
#print (uconv('Fahrenheit', 'Celsius', 3))
#print (uconv('f','c',3))
#print (uconv('kg', 'pounds', 5))
#print (uconv('lb', 'kilograms', 5))
