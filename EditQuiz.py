from DeleteQuiz import deleteQuiz
from PlayQuiz import QuizNotFoundError
import pickle, pyfiglet
from prettytable import PrettyTable
class editQuiz():
    def __init__(self):
        print("\n" * 10)
        Ascii = pyfiglet.figlet_format("Edit Quiz", font="digital")
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

                        #Edit Quiz Method
                        self.edit_quiz(quiz_index)

                        break
                else:
                    raise QuizNotFoundError()
            except ValueError:
                return False
            except QuizNotFoundError:
                print(f"Quiz does not exist with SrNo {choice}")

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
                        self.quiz_list.append(quiz)
                        table.add_row(
                            [quiz.count, quiz.title, quiz.category, quiz.created_by, quiz.number_of_questions])
                        ctr += 1
                except:
                    if len(self.quiz_list) == 0:
                        print("No quizzes Available")
                    else:
                        var = True
                        while var:
                            print(table)
                            var = self.Choose_quiz()
                        pass
        except:
            pass

    def edit_quiz(self, quiz_index):
        print(f"Editing quiz - {quiz_index+1}")
        quiz = self.quiz_list[quiz_index]

        while True:
            request = input("Update (Questions / Creator / Title / Category / Exit): ").lower()
            if request == "questions" or request == "question":
                self.edit_questions(quiz, quiz_index)
            elif request == "creator":
                self.edit_creator(quiz, quiz_index)
            elif request == "title":
                self.edit_title(quiz, quiz_index)
            elif request == "category":
                self.edit_category(quiz, quiz_index)
            elif request == "exit":
                break
            else:
                print("Invalid option. Try again.")

    def edit_questions(self, quiz, quiz_index):
        print("\n" * 3)
        print("Displaying Questions")
        table = PrettyTable()
        table.field_names = ["SrNo.", "Question", "Right answer", "Wrong answers"]

        quiz_to_display = quiz.question_bank
        for i, q in enumerate(quiz_to_display, start=1):
            table.add_row([i, q.question, q.correct_answer, q.incorrect_answers])

        print(table)

        try:
            qno = int(input("Enter Question number to edit (or 0 to cancel): "))
            if qno == 0:
                return
            qno -= 1  # Adjust for 0-based indexing
        except ValueError:
            print("Invalid input, returning to menu.")
            return

        if 0 <= qno < len(quiz.question_bank):
            while True:
                request = input("Update (question / correct answer / wrong answer / exit): ").lower()
                if request == "question":
                    quiz.question_bank[qno].question = input("New question: ")
                elif request == "correct answer":
                    quiz.question_bank[qno].correct_answer = input("New correct answer: ")
                elif request == "wrong answer":
                    quiz.question_bank[qno].incorrect_answers = [input(f"Wrong answer {i + 1}: ") for i in range(3)]
                elif request == "exit":
                    break
                else:
                    print("Invalid option. Try again.")
        else:
            print("Invalid question number.")


        # Save changes back to the file
        self.quiz_list[quiz_index] = quiz
        with open("Files/quizList.dat", "wb+") as fp:
            for qz in self.quiz_list:
                pickle.dump(qz, fp)
        print(f"Questions of quiz-{quiz_index + 1} edited successfully!\n\n")

    def edit_creator(self, quiz, quiz_index):
        quiz.created_by = input("New Creator: ")
        self.quiz_list[quiz_index] = quiz
        with open("Files/quizList.dat", "wb+") as fp:
            for quiz in self.quiz_list:
                pickle.dump(quiz, fp)
            else:
                print(f"Creator of quiz-{quiz_index+1} edited successfully\n\n")

    def edit_title(self, quiz, quiz_index):
        quiz.title = input("New Title: ")
        self.quiz_list[quiz_index] = quiz
        with open("Files/quizList.dat", "wb+") as fp:
            for quiz in self.quiz_list:
                pickle.dump(quiz, fp)
            else:
                print(f"Title of quiz-{quiz_index+1} edited successfully\n\n")


    def edit_category(self, quiz, quiz_index):
        quiz.category = input("New Category: ")
        self.quiz_list[quiz_index] = quiz
        print(self.quiz_list[quiz_index].category)
        with open("Files/quizList.dat", "wb+") as fp:
            for quiz in self.quiz_list:
                pickle.dump(quiz, fp)
            else:
                print(f"Category of quiz-{quiz_index+1} edited successfully\n\n")

# editQuiz()

