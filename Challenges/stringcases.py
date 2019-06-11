# Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:

# All uppercase - upper()
# All lowercase - lower()
# Titlecased (first letter of each word is capitalized) - loop each of word and take the index[0] and upper()
# Reversed - use slice [::-1] to reverse the whole string

# There are str methods for all but the last one.


def stringcases(string):
    lowercase = list(string.lower())
    uppercase = list(string.upper())
    initial = list(string.title())
    reverse = list(string[::-1])
    return(uppercase, lowercase, initial, reverse)


def stringcases2(string):
    return(string.upper(), string.lower(), string.title(), string[::-1])

test = stringcases2('vndlfanv adlfnavnp iehoavf fdknvp van sdfs vknwpn')
print(test)
