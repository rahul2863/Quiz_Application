from DeleteQuiz import deleteQuiz
from prettytable import PrettyTable
from PlayQuiz import QuizNotFoundError
import pickle,pyfiglet
class displayQuiz(deleteQuiz):
    quiz_list=[]
    def __init__(self):
        print("\n" * 10)
        Ascii = pyfiglet.figlet_format("Display Quiz", font="digital")
        print(Ascii)
        self.display_quizzes()
    def display_quizzes(self):
        self.quiz_list.clear()  # Clear the list before loading
        try:
            with open("Files/quizList.dat", "rb+") as fp:
                try:
                    ctr = 1
                    table = PrettyTable()
                    table.field_names = ["SrNo.", "Title", "Category", "Creator", "No. of Questions"]
                    while fp:
                        quiz = pickle.load(fp)
                        displayQuiz.quiz_list.append(quiz)
                        table.add_row([quiz.count, quiz.title, quiz.category, quiz.created_by, quiz.number_of_questions])
                        ctr += 1
                except:
                    if len(displayQuiz.quiz_list) == 0:
                        print("No Quizzes Available")
                    else:
                        print(table)
                        display_ques = input("Would you like to see the questions (yes/no): ")
                        if display_ques == "yes":
                            # quiz_no = int(input("Choose Quiz: "))-1
                            self.Choose_quiz()
                        else:
                            return
        except:
            # used if file does not exist
            pass

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
                        self.display_questions(quiz_index)
                        break
                else:
                    raise QuizNotFoundError()
            except ValueError:
                return False
            except QuizNotFoundError:
                print(f"Quiz does not exist with SrNo {choice}")

    def display_questions(self, quiz_index):
        print("\n" * 3)
        print("Displaying Questions")
        table = PrettyTable()
        table.field_names = ["SrNo.", "Question", "Right answer", "Wrong answers"]
        quiz_to_display = displayQuiz.quiz_list[quiz_index].question_bank
        for i in range(len(quiz_to_display)):
            table.add_row([i + 1, quiz_to_display[i].question, quiz_to_display[i].correct_answer,
                           quiz_to_display[i].incorrect_answers])
        print(table)
        x = input("Enter anything to exit: ")
        pass
# displayQuiz()