name = input('Please set your name: ')

if name == 'Mary':
    print(f'Hello, {name}')
else:
    print("I don't know you")

age = 10
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')


furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a lizard!")
    else:
        print("It's a human. Or a hairless bear.")


#ternary operator
a, b = 2, 5
print('Python') if a > b else print('Examples')


stuff = ''
while True:
    print("String to capitalize [type q to quit]: ")
    stuff = input()
    if stuff == "q":
        break
    print(stuff.capitalize())
print('Thank you!')


while True:
    print('Who are you?')
    name = input()
    if name != 'Jack':
        continue
    print('Hello, Jack. Please input your password')
    password = input()
    if password == 'secret':
        break
print('Access granted.')


a = 'birds'
for index, value in enumerate(a, 1):
     print(index, value)


result = 0
try:
    value_1 = int(input('Please set first value: '))
    value_2 = int(input('Please set second value: '))
    result = value_1 / value_2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Result is", result)
finally:
    print("End of the calculation.")