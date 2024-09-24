import os,pickle
import CreateQuiz
class user:
    user_list=[]
    def __init__(self):
        self.id = self.user_count()+1
        self.name = input("Enter name: ").lower().strip()
        self.age = int(input("Enter Age: ").strip())
        self.password = input("Enter password: ").strip()
        self.quizzes_status = []
        self.quizzes_status_initialize()

    def __str__(self):
        return f"{self.id},{self.name},{self.age},{self.password},{self.quizzes_status}"

    def user_count(self):
        if os.path.exists("Files/register.dat"):
            with open("Files/register.dat", "rb+") as fp:
                ctr = 0
                try:
                    while (fp):
                        userObj = pickle.load(fp)
                        user.user_list.append(userObj)
                        ctr+=1
                except:
                    return ctr
        else:
            return 0

    def quizzes_status_initialize(self):
        quiz_count = 0
        if os.path.exists("Files/quizList.dat"):
            with open("Files/quizList.dat", "rb+") as fp:
                try:
                    while (fp):
                        quiz = pickle.load(fp)
                        quiz_count+=1
                except:
                    # print(f"Quiz Count {quiz_count}")
                    pass
        else:
            pass

        self.quizzes_status = [0 for i in range(quiz_count)]

# print(user())


