#This is a comment
x=10#variable 
print(x)
item = 'Banana'
Item = 'Apple'
item_name = 'Orange'
print(item, Item)
print('Hello'+item + item_name)
interger = 2025
word='text'
isHappy=False
naughty_list=['luigi', 'mario','Toad']
print (interger)
print (word)
print (isHappy)
print(naughty_list) 

interger = 2025
name='Mario'
string_number='22'
print(name+str(interger))

print(10 + int(string_number))


a=10
b=5

addtion=a+b 
difference=a-b 
multiply=a+b
divide=a/b
power=a**b

print(addtion)
print(difference)
print(multiply)
print(divide)
print(power)

# This is a simple Python script to demonstrate variable usage and basic arithmetic operations.
# It defines several variables, performs arithmetic operations, and prints the results. 

age=28
isHappy=False

if age>21:
    print('You are old!.')
elif age==18:
    print('You are getting old.')
else:
    print('You are still young!')

if isHappy:
    print('You are happy!')
else:
    print('You are not happy!')

    for i in range(3):
        print('Hello', i+1)
#In programming the index always starts at 0

print(range(3))
#this works for lists.

i=0
while i <5:
    i=i+1
    print(1)

while True:
    user_input = input('Enter something >>')

    if user_input=='0':
        print('We are done here.')
        break

def say_hello(name):
    print('Hey there ', name)

say_hello('Luigi')
say_hello('Mario')
#reuse your code as much as possible or we have to write it again and again..

def get_internet():
    pass

def run_game():
    pass
#when dont know what to write, use pass
# This is a placeholder function for future implementation
    # You can add code here to fetch internet data or perform other tasks


number=input('please [provide a number>>"')
try:
    print(10+int(number))
except:
    print('That is not a valid number.')

