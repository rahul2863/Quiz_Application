import pickle, pyfiglet
from prettytable import PrettyTable
from quizBrain import QuizBrain

class QuizNotFoundError(Exception):
    def __init__(self):
        pass

class playQuiz:
    def __init__(self):
        print("\n" * 10)
        Ascii = pyfiglet.figlet_format("Play Quiz", font="digital")
        print(Ascii)
        self.display_updated_quiz_statuses()
        self.display_quizzes()
    def display_quizzes(self):
        try:
            with open("Files/quizList.dat", "rb+") as fp:
                try:
                    ctr = 1
                    table = PrettyTable()
                    table.field_names = ["SrNo.", "Title", "Category", "Creator", "No. of Questions", "Status"]
                    while fp:
                        quiz = pickle.load(fp)
                        table.add_row([quiz.count, quiz.title, quiz.category, quiz.created_by, quiz.number_of_questions, quiz.status])
                        ctr += 1
                except:
                    var = True
                    while var:
                        print(table)
                        var = self.Choose_quiz()
                    pass
        except:
            pass

    def Choose_quiz(self):
        choice = input("Enter choice(SrNo.)(type exit to quit): ")
        with open("Files/quizList.dat", "rb+") as fp:
            try:
                while fp:
                    quiz = pickle.load(fp)
                    if quiz.count == int(choice):
                        print(f"You selected quiz {quiz.count}")
                        print("\n"*50)
                        QuizBrain(quiz.question_bank, quiz.count)
                        print("\n"*2)
                        self.display_quizzes()
                        break
            except ValueError:
                # print("Value Error")
                return False
            except EOFError:
                # print("EOF Error")
                try:
                    raise QuizNotFoundError()
                except QuizNotFoundError:
                    print(f"quiz does not exist with SrNo {choice}")
                    self.display_quizzes()
# playQuiz()

    def display_updated_quiz_statuses(self):
        quiz_list = []
        try:
            with open("Files/quizList.dat", "rb+") as fp:
                while fp:
                    quiz_list.append(pickle.load(fp))
        except EOFError:
            pass

        user_status = []
        try:
            with open("Files/login.dat", "rb+") as fp:
                while fp:
                    user = pickle.load(fp)
                    user_status = user.quizzes_status
        except EOFError:
            pass

        for i in range(len(quiz_list)):
            if user_status[i] == 1:
                quiz_list[i].status = "Complete"
            else:
                quiz_list[i].status = "Incomplete"

        with open("Files/quizList.dat", "wb+") as fp:
            for quiz in quiz_list:
                pickle.dump(quiz, fp)












