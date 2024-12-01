# Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa
def temp(celcius):
    farenhite = celcius * 9/5 + 32
    print(celcius,"celcius")
    return farenhite
print("in farenhite",temp(27))