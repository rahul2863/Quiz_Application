import pickle, pyfiglet
from prettytable import PrettyTable
from PlayQuiz import playQuiz,QuizNotFoundError

class deleteQuiz(playQuiz):
    # print("Delete Quiz")
    def __init__(self):
        print("\n" * 10)
        Ascii = pyfiglet.figlet_format("Delete Quiz", font="digital")
        print(Ascii)
        self.quiz_list = []
        self.display_quizzes()

    def Choose_quiz(self):
        self.quiz_list.clear()  # Clear the list before loading

        choice = input("Enter(SrNo.) of quiz(type exit to quit): ")
        with open("Files/quizList.dat", "rb+") as fp:
            try:
                while fp:
                    quiz = pickle.load(fp)
                    self.quiz_list.append(quiz)
            except EOFError:
                fp.seek(0, 0)

            try:
                for quiz in self.quiz_list:
                    if quiz.count == int(choice):
                        print(f"You selected quiz {quiz.count}")
                        quiz_index = self.quiz_list.index(quiz)
                        self.delete_quiz(quiz_index)
                        break
                else:
                    raise QuizNotFoundError()
            except ValueError:
                return False
            except QuizNotFoundError:
                print(f"Quiz does not exist with SrNo {choice}")

    def delete_quiz(self, quiz_index):

        # Deleting quiz
        self.quiz_list.pop(quiz_index)

        # Updating the id of quizzes
        for quiz in self.quiz_list:
            quiz.count = self.quiz_list.index(quiz)+1

        with open("Files/quizList.dat", "wb+") as fp:
            for quiz in self.quiz_list:
                pickle.dump(quiz, fp)
            else:
                print(f"Quiz deleted successfully\n\n")

        #Updating User Quiz Status by removing corresponding element
        user_list = []
        try:
            with open("Files/register.dat", "rb+") as fp:
                while fp:
                    user = pickle.load(fp)
                    user.quizzes_status.pop(quiz_index)
                    user_list.append(user)
        except:
            pass

        with open("Files/register.dat", "wb+") as fp:
            for user in user_list:
                pickle.dump(user, fp)


    def display_quizzes(self):
        try:
            with open("Files/quizList.dat", "rb+") as fp:
                try:
                    ctr = 1
                    table = PrettyTable()
                    table.field_names = ["SrNo.", "Title", "Category", "Creator", "No. of Questions"]
                    while fp:
                        quiz = pickle.load(fp)
                        table.add_row([quiz.count, quiz.title, quiz.category, quiz.created_by, quiz.number_of_questions])
                        ctr += 1
                except:
                    var = True
                    while var:
                        print(table)
                        var = self.Choose_quiz()
                    pass
        except:
            # used if file does not exist
            pass






