def log_and_run(func):
    print('I just got {}'.format(func.__name__))
    return func()

def log_and_retun(func):
    print('I just got {}'.format(func.__name__))
    return func

def say_hello():
    print('Hello!')

print('log and run:')

log_and_run(say_hello)
print('-'*10)
print('log and return')
variable = log_and_retun(say_hello)

variable()