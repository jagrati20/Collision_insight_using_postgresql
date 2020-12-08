from database import *


def RunApplication():
    print('Choose a number from the following:')
    print('1. Search in Collision Data')
    print('2. Search in Hospital Data')
    print('3. Search in Liquor Shop Data')
    print('4. Search in Repair Shop Data')
    print('5. Search in Liquor and Collision by location')
    print('6. Exit Application')
    value = input()
    switch(value)


def default():
    print("\nInvalid Input! "
          "Please choose again \n")
    RunApplication()


def Collision():
    cd = CollisionData()
    cd.check_collisions()
    Explore()


def Hospital():
    cd = CollisionData()
    cd.hospital_query()
    Explore()


def Liquor():
    cd = CollisionData()
    cd.liquor_query()
    Explore()


def ExitApplication():
    print("Okay! Exiting...")
    exit()


def SearchAll():
    cd = CollisionData()
    cd.search_all()
    Explore()


def Repairs():
    cd = CollisionData()
    cd.check_repairs()
    Explore()


switcher = {
    '1': Collision,
    '2': Hospital,
    '3': Liquor,
    '4': Repairs,
    '5': SearchAll,
    '6': ExitApplication
}


def switch(value):
    return switcher.get(value, default)()


def Explore():
    print("Explore more dataset? (y/n)")
    yes_or_no = input()
    yes_or_no = yes_or_no.upper()
    if yes_or_no == 'Y':
        RunApplication()
    elif yes_or_no == 'N':
        print("\nOkay, Exiting!")
        exit()
    else:
        print("\nEnter y/n")
        Explore()


RunApplication()
