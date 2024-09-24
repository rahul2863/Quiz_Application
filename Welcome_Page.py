from register import Register
from login import Login
class welcomePage:
    def __init__(self):
        welcomePage.Start()

    @staticmethod
    def Start():
        print("Welcome to Quizzard")
        request = input("Register / Login: ")

        if request == "Register":
            Register()
        else:
            Login()

