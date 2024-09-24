from User import user
import pickle
import pyfiglet
class Register:
    registered_User = []
    def __init__(self):
        Ascii = pyfiglet.figlet_format("Register",font="digital")
        print(Ascii)
        new_usr = user()
        self.registerUser(new_usr)

    def registerUser(self,new_usr):
        with open("Files/register.dat", "ab+") as fp:
            pickle.dump(new_usr, fp)
        print("Registered Successfully")


