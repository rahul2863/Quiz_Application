import pickle,datetime
from CreateQuiz import CreateQuiz
from Question import Question
from Quiz_User_Details import quizUser
import random, time
class QuizBrain:
    score=0
    start_time = 0
    end_time = 0
    def __init__(self,question_bank,count):
        self.question_list = question_bank
        self.question_num = 0
        self.quiz_id = count
        self.finish_time = 0
        QuizBrain.start_time = time.time()
        self.start()

    def start(self):
        # Reset the timer for each new quiz
        self.display()

    def display(self):
        print("\n"*2)
        answers = (self.question_list[self.question_num]).incorrect_answers
        answers.append((self.question_list[self.question_num]).correct_answer)
        random.shuffle(answers)
        print(f"{self.question_num+1}. {self.question_list[self.question_num].question}")
        options = 97
        dict = {}
        for ans in answers:
            dict[chr(options)] = ans
            options += 1

        # Enter valid choice otherwise display options again
        while(True):
            for key,value in dict.items():
                print(f"{key}. {value}")
            selected_option = input("choice: ")

            if selected_option not in dict:
                print("Enter valid choice")
            else:
                break
        self.evaluate(selected_option, dict)



    def evaluate(self,selected_option,dict):
        ans = dict[selected_option]
        # print(ans)
        correct_ans = (self.question_list[self.question_num]).correct_answer
        if ans == correct_ans:
            QuizBrain.score += 1
            print("⭐ Correct! ⭐")
        else:
            print(f"The answer is {correct_ans!r}, not {ans!r}")

        print(f"Your Score: {QuizBrain.score}/{len(self.question_list)}")

        self.next_question()

    def next_question(self):
        if self.question_num != len(self.question_list)-1:
            self.question_num += 1
            self.start()
        else:
            print("Quiz Complete...")
            # Ending Timer
            QuizBrain.end_time = time.time()
            self.finish_time = QuizBrain.end_time - QuizBrain.start_time
            print(f"Your Final Score: {QuizBrain.score}/{len(self.question_list)}")

        self.update_status()
        # Saving into leaderboards
        self.save_leaderboards()
        # Reseting the score
        QuizBrain.score = 0


    def update_status(self):
        # print("Inside update status")
        quiz_list = []
        with open("Files/quizList.dat", "rb+") as fp:
            try:
                while fp:
                    quiz = pickle.load(fp)
                    quiz_list.append(quiz)
            except:
                pass


        try:
            with open("Files/login.dat", "rb+") as fp:
                name = pickle.load(fp)
                # print("Quiz-id: ", self.quiz_id)
                # print("Name-id: ", name.id)
                user_list = []
                try:
                    with open("Files/register.dat", "rb+") as fp:
                        while fp:
                            user = pickle.load(fp)
                            if name.id == user.id:
                                user.quizzes_status[self.quiz_id - 1] = 1
                                name.quizzes_status[self.quiz_id - 1] = 1
                            user_list.append(user)
                            # print("Quiz Statuses: ", user.quizzes_status)
                            # print(user_list[0])
                except EOFError:
                    with open("Files/register.dat", "wb+") as fp:
                        for userObj in user_list:
                            pickle.dump(userObj, fp)

                    with open("Files/login.dat", "wb+") as fp:
                        pickle.dump(name, fp)
        except:
            pass

        self.display_updated_quiz_statuses()

    def display_updated_quiz_statuses(self):
        quiz_list = []
        try:
            with open("Files/quizList.dat", "rb+") as fp:
                while fp:
                    quiz_list.append(pickle.load(fp))
        except EOFError:
            pass

        user_status=[]
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

    def save_leaderboards(self):
        data = dict()
        userid = 0
        try:
            with open("Files/login.dat", "rb") as fp:
                while True:
                    try:
                        user = pickle.load(fp)
                        data["User_id"] = user.id
                        data["Name"] = user.name
                        data["Score"] = QuizBrain.score
                        data["finish_time"] = self.finish_time
                        data["quiz_id"] = self.quiz_id
                        userid = user.id
                    except EOFError:
                        break

        except FileNotFoundError:
            print("User login data file not found.")
            return

        try:
            user_exists = False
            # Open the leaderboard file to check if the user already exists
            with open("Files/leaderboards.dat", "rb+") as fp:
                while True:
                    try:
                        leaderboard_data = pickle.load(fp)
                        if leaderboard_data["User_id"] == userid and leaderboard_data["quiz_id"] == self.quiz_id:
                            user_exists = True
                            print(userid, "- Matched, user already exists in leaderboard.")
                            break
                    except EOFError:
                        break

            if not user_exists:
                with open("Files/leaderboards.dat", "ab") as fp:
                    print("Saving new user data to leaderboard.")
                    pickle.dump(data, fp)

        except FileNotFoundError:
            # If leaderboard file doesn't exist, create it and add the user
            print("Leaderboard file not found, creating a new one.")
            with open("Files/leaderboards.dat", "wb") as fp:
                pickle.dump(data, fp)













