from CreateQuiz import CreateQuiz
from EditQuiz import editQuiz
from DeleteQuiz import deleteQuiz
from DisplayQuiz import displayQuiz
import pyfiglet
import pickle

class AdminHomePage():
    quiz_list = []
    print("\n"*30)
    def __init__(self):
        request=""
        while request!="e":
            print("\n" * 30)
            Ascii = pyfiglet.figlet_format("Admin Home Page", font="digital")
            print(Ascii)
            print("Welcome Admin\n")

            request = input("a.Create Quiz\nb.Delete Quiz\nc.Edit Quiz\nd.Display Quizzes\ne.Logout\nChoice: ")
            if request == "a":
                quiz = CreateQuiz()
                if quiz.creation:
                    AdminHomePage.quiz_list.append(quiz)
                    # quiz object making way to the file
                    with open("Files/quizList.dat", "ab+") as fp:
                        fp.seek(0, 2)
                        pickle.dump(quiz, fp)
                    print("Quiz Created Successfully")
                else:
                    print("Quiz Creation Failed")

            elif request == "b":
                print("Deleting Quiz")
                if CreateQuiz.quiz_count() == 0:
                    print("\nNo Quizzes available to Delete")
                else:
                    deleteQuiz()

            elif request == "c":
                print("\n\nEdit quiz")
                editQuiz()
                pass
            elif request == "d":
                displayQuiz()
                pass
            elif request == "e":
                print("\n\n")
                pass
            else:
                print("Enter valid choice")

# AdminHomePage()


