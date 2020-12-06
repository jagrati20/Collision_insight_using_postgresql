from Database import *


def RunApplication():
    print('Choose a number from the following:')
    print('1. Query Collision Data')
    print('2. Query Hospital Data')
    print('3. Query Repair Shop Data')
    print('5. Exit Application')
    value = input()
    # if value == 5:
    #     sys.exit()
    # else:
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


def Repairs():
    cd = CollisionData()
    cd.check_repairs()


switcher = {
    '1': Collision,
    '2': Hospital,
    '3': Repairs,
    '5': SystemExit
}


def switch(value):
    return switcher.get(value, default)()


RunApplication()
