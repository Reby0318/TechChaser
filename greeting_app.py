import sys


def just_greeting():
    print("Hello, World! ", person)
    
def welcome_greeting():
    print("Hello, welcome to our company! ", person)

def count_hobbies(hobbies) -> int:
    return len(hobbies)

def recommend_subscription(hobbies=None):
    print("We see that you are interested in: ")
    for hobby in hobbies:
        print(f"- {hobby.capitalize()}")
    print("We want to add a complementary hobby for you.")
    hobbies.append("Piano")
    
    n_hobbies = count_hobbies(hobbies)

    print(n_hobbies, "hobbies in total.")
    if n_hobbies>3:
        print("We recommend premium subscription for you.")
    else:
        print("We recommend basic subscription for you.")

def price_calculator(household, hobbies):
    price=20*1+10*household+1*count_hobbies(hobbies)
    print(f"you have {household} people in your household")
    print(f"you have {count_hobbies(hobbies)} hobbies") 
    if household==1:
        print("price = household * 10 + 20")
    else:
        print("price = household * 10 + 20 + hobbies * 1")
    print(f"The total price is: {price}")
    print("We will calculate the price for you.")
    price_calculator = {
        "household": household,
        "hobbies": hobbies,
        "price": price
    }
    print(f"Your total price is: {price_calculator['price']}")
    




hobbies = sys.argv[1:] # Get command line arguments excluding the script name

person = input("What is your name? ")
status = input("Is this your first time here? (yes/no): ").strip().lower()

if status=="yes":
    welcome_greeting()

else:
    just_greeting()

recommend_subscription(hobbies)
household = input("How many people are in your household? ")


price_calculator(int(household), hobbies)

