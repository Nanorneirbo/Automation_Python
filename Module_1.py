# for loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))


# while loop
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'yourname':
        break
print('Thanks')

spam = 0
while spam < 5:
    print('There are ' + str(spam) + ' spam')
    spam = spam + 1


# if else
print('enter name')
name = input()
if name == 'Ronan':
    print('Hi ' + name + 'Finally you have a great name')
    print('done')
else:
    print(name + ' is a dumb name your name - should be Ronan')
    name = input()


# This program says hello and asks for my name

print('Hello World')
print('What is your name?')
myName = input()
print(' It is good to meet you ' + myName)
print(' The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be' + str(int(myAge)+1) + '  in a year')

