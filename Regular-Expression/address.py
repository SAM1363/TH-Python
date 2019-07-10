import re

file_name = open('lorem.txt', encoding='utf-8')
data = file_name.read()
file_name.close()


# print(re.findall('[-\w\d+.]+@[-\w\d.]+', data))

# print(re.findall(r'''
#     \b@[-\w\d.]*
#     [^gov]+
#     \b
# ''', data, re.VERBOSE|re.I))

# print(re.findall('[el]{4}', data, re.I))


print(re.findall(r"""
    \b[-\w]*, # Find the word boundary, 1+ hyphens or charactors, and a comma
    \s  # Find a whitespace
    [-\w ]+  # 1+ hyphens and characters and explicit spaces
    [^\t\n]  # ignore the tabs and newlines
""",data ,re.X))

string = '1234567890'

# good_numbers = print(re.findall(r'[^5-7]', string))

string = 'Perotto, Pier Giorgio'

# name = re.match(r'''
#     ^(?P<first_name>[\w]*),\s  
#     (?P<last_name>[\w\s\w]*)$
#     ''', string, re.X|re.M)

# names = re.match(r'([\w]*), ([\w]+ [\w]+)', string)

# print(name)
# print(names)

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+)
    ,\s
    (?P<phone>\d{3}-\d{3}-\d{4})
    ''', string, re.X|re.M)

twitters = re.search(r'(?P<Twitter>@[\w\d]*)$', string, re.M)

print(contacts)
print(twitters)

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'(?P<last_name>[\w ]+),\s(?P<first_name>[\w ]+):\s(?P<score>[\d]*)', string, re.M)

print(players)