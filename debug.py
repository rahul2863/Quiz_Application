
import pickle,os
#
# data=[0 for i in range(4)]
# print(data)
#
# try:
#     with open("Files/quizList.dat", "rb+") as fp:
#         quiz = pickle.load(fp)
#         print(quiz)
# except:
#     pass

# with open("Files/register.dat", "wb+") as fp:
#     pass

print("Registered: ")
with open("Files/register.dat", "rb+") as fp:
    try:
        while (fp):
            user = pickle.load(fp)
            print(user)
    except:
        pass


# print()
print("Logged in: ")
with open("Files/login.dat", "rb+") as fp:
    try:
        while (fp):
            user = pickle.load(fp)
            print(user)
    except:
        pass


# quiz_list = []
print("Quiz list: ")
try:
    with open("Files/quizList.dat", "rb+") as fp:
        while fp:
            quiz = pickle.load(fp)
            print(quiz)
except:
    pass


# user_status=[]
# try:
#     with open("Files/login.dat", "rb+") as fp:
#         while fp:
#             user = pickle.load(fp)
#             user_status = user.quizzes_status
# except EOFError:
#     print(user_status[1])

try:
    with open("Files/leaderboards.dat", "rb+") as fp:
        data = dict()
        while fp:
            data = pickle.load(fp)
            print(data)
except:
    pass


