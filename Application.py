from Database import *


def RunApplication():
    print('Choose a number from the following:')
    print('1. Query Collision Data')
    print('2. Query Hospital Data')
    print('5. Exit Application')
    value = input()
    switch(value)


def default():
    print("\nInvalid Input! "
          "Please choose again \n")
    RunApplication()


def Collision():
    cd = CollisionData()
    cd.check_collisions()


def Hospital():
    cd = CollisionData()
    cd.check_hospital()


switcher = {
    '1': Collision,
    '2': Hospital,
    '5': SystemExit
}


def switch(value):
    return switcher.get(value, default)()


RunApplication()
