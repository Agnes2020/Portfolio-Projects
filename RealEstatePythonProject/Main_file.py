#Author: Agnes Fusese And Doreen Lawratu Baidoo
from Land_Class import Land
from House_class import House
from Property_class import Property
from AdminUser_class import MainUser
import datetime
import sys

# This is an array to hold all admin users
users = []

# Static house property instances
house1 = House('Kigali', 67, 345654, False, 54)
house2 = House('Awoshie', 6, 1000000, True, 4)
house3 = House('Haatso', 5, 700000, True, 5)
house4 = House('East_Legon', 4, 900000, False, 4)
house5 = House('Kwabenya', 3, 1200000, False, 6)

houses = [house1, house2, house3, house4, house5]

# Static land property instances
land1 = Land('Kigali', 67, 345654, False, 540)
land2 = Land('Awoshie', 6, 1000000, True, 400)
land3 = Land('Haatso', 5, 700000, True, 500)
land4 = Land('East_Legon', 4, 900000, False, 400)
land5 = Land('Kwabenya', 3, 1200000, False, 600)

lands = [land1, land2, land3, land4, land5]

properties = []
# land and houses properties combined

for i in lands:
    properties.append(i)
for i in houses:
    properties.append(i)


def add_house():
    # Method to add house by admin user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username and user.password == password:
            print("Successfully Logged In\n")
            location = input("Add the location of the House: ")
            rented_times = input("How many times has the house been rented out: ")
            price = input("What is the price of the house: ")

            no_of_rooms = input("How many rooms does this house have?: ")

            while 1:
                rented = input("Is the house rented?: \n 1 for yes and 2 for no: ")
                if rented == 1:
                    rented_final = True
                    break
                elif rented == 2:
                    rented_final = False
                    break
                else:
                    print("Please enter 1 or 2")

            house = House(location, rented_times, price, rented_final, no_of_rooms)
            houses.append(house)
            properties.append(house)


def add_land():
    # Method to add land by admin user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username and user.password == password:
            print("Successfully Logged In")
            location = input("Add the location of the Land: ")
            rented_times = input("How many times has the Land been rented out: ")
            price = input("What is the price of the Land: ")

            size = input("What is the size of the Land?: ")

            while 1:
                rented = input("Is the Land rented?: \n 1 for yes and 2 for no: ")
                if rented == 1:
                    rented_final = True
                    break
                elif rented == 2:
                    rented_final = False
                    break
                else:
                    print("Please enter 1 or 2")

            land = Land(location, rented_times, price, rented_final, size)
            lands.append(land)
            properties.append(land)


def rent(property):
    # Method to update the status and the number of times a property has been rented.
    property.RentOutTimes += 1
    property.rented = True
    print("Property Rented")


def view_property():
    # This function will display the property collection to normal user
    index = 0
    for house in houses:
        print(str(index) + ". " + house.house_info())
        index += 1

    index1 = 0
    for land in lands:
        print(str(index1) + ". " + land.Land_info())
        index1 += 1


def create_admins():
    username = input("Create username: ")
    password = input("Create password")

    user = MainUser(password, username)
    users.append(user)


def view_property_details():
    # this method displays a more detailed information about properties to the AdminUser
    username = input("Enter your username: ")
    password = input("Enter your password")

    for user in users:
        if user.username == username and user.password == password:
            index = 0
            for property in properties:
                print(str(index) + ". " + property.property_info())
                index += 1
    else:
        print("You are not an admin user")


def get_total_revenue():
    # this
    logged = False
    if len(users) == 0:
        print("Please create users first")
        create_admins()
    else:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in users:
            if user.username == username and user.password == password:
                logged = True
        if logged:
            print("Successfully Logged In")
            total = 0
            for prop in properties:
                total += prop.Total_revenue()
            print(total)
        else:
            print("Username or password wrong")


def main():
    print("\n\n\t\t\t----- Property Rental App -----")
    now = datetime.datetime.now()  # Display time and Date
    print("Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))

    def menu():
        print("Choose what you wanna do buddy")
        print("1. Create an Account\n2. Add Houses\n3. Add Land\n4. View Total Revenue\n"
              "5. View Property\n6. View Property Details\n7. Rent Property")
        selection = int(input("Please select one: "))
        runApp(selection)

    def choose_again():
        print("Wanna perform another operation?\n")
        sel = int(input("1. Yes\n2. No\n:"))
        if sel == 1:
            menu()
        elif sel == 2:
            print("Thanks for using the app")
            sys.exit()
        else:
            print("Select 1 or 2")

    def runApp(selection):
        while True:
            if selection == 1:
                create_admins()
                choose_again()

            elif selection == 2:
                add_house()
                choose_again()

            elif selection == 3:
                add_land()
                choose_again()

            elif selection == 4:
                get_total_revenue()
                choose_again()

            elif selection == 5:
                view_property()
                choose_again()

            elif selection == 6:
                view_property_details()
                choose_again()

            elif selection == 7:
                id_prop = int(input("Enter the id of the property to rented: "))
                if properties[id_prop].rented:
                    print("Property has already been rented")
                    choose_again()
                else:
                    rent(properties[id_prop])
                    choose_again()
            else:
                print("Please enter the choices given")

    menu()


main()
