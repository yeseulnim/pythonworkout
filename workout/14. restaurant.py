# create a new constant dict called MENU
# representing the possible items you can order at a restaurant
# keys = strings. values = prices(integers).
# write a function, restaurant, that asks the user to enter an order:
# if the user enters the name of a dish on the menu,
# print the price and the running total. then ask again for their order
# if the user enters the name of a dish not on the menu,
# scold the user then ask again for their order
# if the user eners an empty string, stop prompting and print the total amount

def restaurant():
    order = 0
    menu = {"sandwich":10, "tea":7, "coffee":8}
    while True:
        order_item = input("enter order: ")
        if order_item in menu.keys():
            order += menu[order_item]
            print(f"{order_item} costs {menu[order_item]}, total is {order}.")
        elif not order_item:
            print(f"Your total is {order}")
            break
        else:
            print(f"Sorry, we are fresh out of {order_item} today.")
# restaurant()


# 2. Create a dict in which the keys are usernames and the values are passwords
# both represented as strings
# create a tiny login system in which the user must enter a username and password
# if there is a match, then indicate that the user has successfully logged in
# if not then refuse then entry

id_pw = {"ys":"1234"}

def login():
    login_try = 0
    while True:
        id = input("Input ID:")
        if id not in id_pw.keys():
            print("ID not recognized. Try again?")
        else:
            password = input("Input Password:")
            if password == id_pw[id]:
                print("Logging in...")
                print("Logged in successfully!")
                break
            elif login_try < 2:
                login_try +=1
                print(f"Login failed {login_try} times")
                print("Try again?")
            else:
                print("Login failed three times")
                print("Goodbye")
                break
# login()



# Define a dict whose keys are dates (represented by strings) fron the most recent week
# and whose values are temperatures
# ask the user to enter a date
# and display the temperature on that date
# as well as the previous and subsequent dates, if available

weather = {"9/20":20, "9/21":17, "9/22":15, "9/23":17, "9/24":20}
def display_temperature():
    date = input("Input a date:")
    day = int(date[-2:])
    yesterday = "9/" + str(day-1)
    tomorrow = "9/" + str(day+1)
    print(f"Today's temperature is {weather[date]}")
    if yesterday in weather.keys():
        print(f"Yesterday's temperature is {weather[yesterday]}")
    if tomorrow in weather.keys():
        print(f"Tomorrow's temperature is {weather[tomorrow]}")

# display_temperature()



# define a dict whose keys are names of people in your family
# and whose values are their birth dates as represented by python date objects
# ask the user to enter the name of someone in your family
# and have the program calculate how many days old that person is

from datetime import date

family = {"Maria":date.fromisoformat('1990-10-05'),
          "Teresa":date.fromisoformat('1961-01-18'),
          "John":date.fromisoformat('1995-01-18')}

def days_since_born():
    while name := input("Choose a family member: "):
        if name not in family.keys():
            print("Choose again!")
        else:
            birthday = family[name]
            days_passed = (date.today() - birthday).days
            print(f"{name} is {days_passed} days old!")
            break

days_since_born()






