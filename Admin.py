import pickle
from Admin_home_page import AdminHomePage
class admin:
    def __init__(self):
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")
        self.validate_admin()

    def validate_admin(self):
        with open("Files/Admininfo.dat", "rb+") as fp:
            admin = pickle.load(fp)
            if admin["username"] == self.username and admin["password"] == self.password:
                AdminHomePage()
            else:
                print("Admin Login fail")

