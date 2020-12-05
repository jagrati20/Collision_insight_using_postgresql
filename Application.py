from Database import *


def RunApplication():
    print('Choose a number from the following:')
    print('1. Query Collision Data')
    print('2. Query Hospital Data')
    value = input()
    switch(value)


def default():
    print("Incorrect! "
          "choose again")
    RunApplication()


def Collision(self):
    CollisionData.check_connectivity(self)


def Hospital(self):
    CollisionData.check_hospital(self)


switcher = {
    '1': Collision,
    '2': Hospital
}


def switch(value):
    return switcher.get(value, default)


RunApplication()
