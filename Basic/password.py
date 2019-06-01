import sys

PASSWORD = 'python'

answer = input('give me the right password: ')
attempt = 1
while answer != PASSWORD:
  attempt += 1
  answer = input('this is not the right password, try it again: ')
  if attempt > 3:
    sys.exit('you have missed it too many times')
print('welcome!')