from register import Register
from login import Login
from Admin import admin
import pyfiglet

if __name__ == "__main__":
    while True:
        print("-"*30)
        Ascii = pyfiglet.figlet_format("BrainBuzz")
        # print("Welcome to Quizzard")
        Ascii = pyfiglet.figlet_format("BrainBuzz")
        print(Ascii)
        choice = input("Admin / User / exit: ").lower().strip()
        if choice == "admin":
            print("-"*30)
            Ascii = pyfiglet.figlet_format("BrainBuzz")
            print(Ascii)
            admin()

        elif choice == "user":
            while True:
                print("-"*30)
                Ascii = pyfiglet.figlet_format("BrainBuzz")
                print(Ascii)
                # print("Welcome to Quizzard")
                request = input("Register / Login / exit: ").lower().strip()
                if request == "register":
                    print("\n" * 30)
                    Register()
                elif request == "login":
                    print("\n" * 30)
                    Login()
                elif request == "exit":
                    break
                else:
                    print("Enter valid option")
        elif choice == "exit":
            break
        else:
            print("Choice can be either Admin or User")

