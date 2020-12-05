from Database import *


def RunApplication():
    print('Choose a number from the following:')
    print('1. Query Collision Data')
    print('2. Query Hospital Data')
    value = input()
    switch(value)


def default(self):
    print("Incorrect! "
          "choose again")
    self.RunApplication(self)


def Collision():
    cd = CollisionData()
    cd.check_connectivity()


def Hospital():
    cd = CollisionData()
    cd.check_hospital()


switcher = {
    '1': Collision,
    '2': Hospital
}


def switch(value):
    return switcher.get(value, default)()


RunApplication()
