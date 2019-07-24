temperatures = [
    37,
    0,
    25,
    100,
    13.2,
    29.9,
    18.6,
    32.8
]

def c_to_f(temp):
    """Returns Celsius temperature as Fahrenheit"""
    return temp * (9/5) + 32

# x = list(map(c_to_f, temperatures))
# print(x)


good_temps = [c_to_f(each) for each in temperatures if each > 9 and each < 32.6]

# map version

good_temps2 = [each for each in list(map(c_to_f, temperatures)) if each > c_to_f(9) and each < c_to_f(32.6)]

print(good_temps)
print('-'*20)
print(good_temps2)
