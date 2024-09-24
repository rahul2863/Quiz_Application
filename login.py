import pickle
from UserHomePage import UserHomePage
import pyfiglet
class Login:
    def __init__(self):
        Ascii = pyfiglet.figlet_format("Login ", font="digital")
        print(Ascii)
        self.validateLogin()

    def validateLogin(self):
        try:
            with open("Files/register.dat", "rb+") as fp:
                success = False
                while(success != True):
                    name = input("Enter Username: ").lower().strip()
                    password = input("Enter password: ").strip()
                    fp.seek(0, 0)
                    while fp:
                        try:
                            data = pickle.load(fp)
                        except EOFError:
                            print("Incorrect username or password"
                                  "\nif haven't registered do register first")
                            return
                            break
                        else:
                            if name == data.name and password == data.password:
                                print("Login Successful")
                                with open("Files/login.dat", "wb+") as fp:
                                    user = data
                                    pickle.dump(user, fp)
                                success = True
                                print("\n" * 30)
                                UserHomePage()
                                break
        except FileNotFoundError:
            print("Before you login please register")
