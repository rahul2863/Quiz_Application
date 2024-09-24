from CreateQuiz import CreateQuiz
from PlayQuiz import  playQuiz
from Leaderboards import Leaderboards
import pyfiglet
import pickle
class UserHomePage:
    quiz_list = []
    def __init__(self):
        self.display()
    def display(self):
        request = ""
        while request != "c":
            print("\n" * 30)
            Ascii = pyfiglet.figlet_format("User Home Page", font="digital")
            print(Ascii)
            # print("Welcome User")
            request = input("a.Play Quiz\nb.Leaderboards\nc.logout\nChoice: ")
            if request == "a":
                print("Playing Quiz")
                if CreateQuiz.quiz_count() == 0:
                    print("\nNo Quizzes available")
                else:
                    playQuiz()

            elif request == "b":
                Leaderboards()
                pass
            elif request == "c":
                with open("Files/login.dat", "wb+") as fp:
                    pass
            else:
                print("Enter valid choice")
# UserHomePage()


