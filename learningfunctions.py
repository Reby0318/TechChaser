#Building our Own Functions
#We create a new function using the def keyword followed by optional parameters in parentheses.
#We indent the body of the function
#This defines the function but does not execute the body of the function

x=5
print("Hello")
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.") 

print("YO")
x=x+2
print(x)

#Two lyrics above didnt invoke the function.
#Go to print("YO") directly below the function definition.

####Correct way to call the function
x=5
print("Hello")

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print("YO")
print_lyrics()  # This calls the function and executes its body
x = x + 2
print(x) 