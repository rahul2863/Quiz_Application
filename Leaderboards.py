from DeleteQuiz import deleteQuiz
from prettytable import PrettyTable
from PlayQuiz import QuizNotFoundError
import pickle,pyfiglet
class Leaderboards(deleteQuiz):
    quiz_list=[]
    def __init__(self):
        print("\n" * 10)
        Ascii = pyfiglet.figlet_format("Leaderboards", font="digital")
        print(Ascii)
        self.display_quizzes()

    def display_quizzes(self):
        try:
            with open("Files/quizList.dat", "rb+") as fp:
                try:
                    ctr = 1
                    table = PrettyTable()
                    table.field_names = ["SrNo.", "Title", "Category", "Creator", "No. of Questions"]
                    while fp:
                        quiz = pickle.load(fp)
                        table.add_row(
                            [quiz.count, quiz.title, quiz.category, quiz.created_by, quiz.number_of_questions])
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
                        self.evaluate_leaderboards(quiz_index)
                        break
                else:
                    raise QuizNotFoundError()
            except ValueError:
                return False
            except QuizNotFoundError:
                print(f"Quiz does not exist with SrNo {choice}")

    def evaluate_leaderboards(self, quiz_index):
        quiz_id = quiz_index + 1
        # Select that data from the leaderboard with quiz_id = quiz_index+1
        user_data = []
        try:
            with open("Files/leaderboards.dat", "rb") as fp:
                while fp:
                    data = pickle.load(fp)
                    if data["quiz_id"] == quiz_id:
                        user_data.append(data)
        except EOFError:
            print("\n" * 3)
            # Sort by Score in descending order, and by time taken in ascending order for tie-breaking

            # we negate the score (-x["Score"]).
            # This trick turns a larger score into a smaller negative number,
            # and a smaller score into a larger negative number.
            sorted_user_data = sorted(user_data, key=lambda x: (-x["Score"], x["finish_time"]))

            print("Displaying Leaderboards")
            table = PrettyTable()
            table.field_names = ["Rank", "User_Id", "Name", "Score", "Time Taken (s)"]

            # Display the rankings, considering tied scores
            previous_score = None
            previous_time = None
            rank = 0
            for user in sorted_user_data:
                # Only update rank if both score and time are different from the previous entry
                if user["Score"] != previous_score or user["finish_time"] != previous_time:
                    rank += 1  # Update rank only if the score or time is different

                # Add user details to the leaderboard table
                table.add_row([rank, user["User_id"], user["Name"], user["Score"], f"{user['finish_time']:.2f}"])

                # Update the previous score and time for the next iteration
                previous_score = user["Score"]
                previous_time = user["finish_time"]

            print(table)

            x = input("Enter any character to exit: ")
# Leaderboards()