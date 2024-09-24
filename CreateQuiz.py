from Question import Question
import os, pickle, pyfiglet
class CreateQuiz:
    def __init__(self):
        print("\n" * 10)
        Ascii = pyfiglet.figlet_format("Create Quiz", font="digital")
        print(Ascii)
        try:
            self.number_of_questions = int(input("Enter Number of Questions: "))
            self.question_bank = []
            self.addQuestions()
            self.category = input("Enter Category: ")
            self.title = input("Enter title for the quiz: ")
            self.created_by = input("Enter creator name: ")
            self.count = CreateQuiz.quiz_count()+1
            self.status = "Incomplete"

            #update User_register with quizzes_Status
            self.update()
            self.creation = True

        except ValueError:
            self.creation = False
            print("Invalid value was given")

    def addQuestions(self):
        for i in range(0, self.number_of_questions):
            question = Question(i+1)
            self.question_bank.append(question)

    def quiz_count():
        if os.path.exists("Files/quizList.dat"):
            with open("Files/quizList.dat", "rb+") as fp:
                ctr=0
                try:
                    while (fp):
                        quiz = pickle.load(fp)
                        ctr+=1
                except:
                    return ctr
        else:
            return 0

    def update(self):
        user_list=[]
        try:
            with open("Files/register.dat", "rb+") as fp:
                while fp:
                    user = pickle.load(fp)
                    user.quizzes_status.append(0)
                    user_list.append(user)
        except:
            pass

        with open("Files/register.dat", "wb+") as fp:
            for user in user_list:
                pickle.dump(user, fp)

    def __str__(self):
        return f"{self.number_of_questions},{self.question_bank},{self.category},{self.title},{self.count},{self.status}"

# CreateQuiz()


