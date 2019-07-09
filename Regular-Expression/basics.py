import re

file_object = open('basics.txt')

data = file_object.read()
first = re.match('samson', data)
last_name = re.search('blankenship', data)

file_object.close()