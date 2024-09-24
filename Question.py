from Questions import Question_list
class Question:
    def __init__(self,question_num):
        self.question = input(f"Enter Question-{question_num}: ")
        self.correct_answer = input("Enter Correct Answer: ")
        print("Enter Incorrect Answers: ")
        self.incorrect_answers = [input(f"{i+1}. ") for i in range(3)]

    def __str__(self):
        return f"Question: {self.question} | correct_answer: {self.correct_answer} | incorrect_answer: {",".join(self.incorrect_answers)}"

