# Fun quiz
# ---------
def start_game():
    list_user_answer = []
    questions_num = 1
    score_user_answer = 0

    for key in questions:
        print(key)  # print out question
        for i in options[questions_num - 1]:
            print(i)  # print out each
        user_answer = input("choice: ").upper()  # change user answer to upper case
        list_user_answer.append(user_answer)
        score_user_answer += check_answer(questions.get(key), user_answer)
        questions_num += 1

    display_score(score_user_answer, list_user_answer)


# ---------

def check_answer(answer, user_answer):
    if answer == user_answer:
        print("[ Correct ]")
        return 1
    else:
        print("[ Incorrect ]")
        return 0


questions = {"\n1. How many wheels does a tricycle have? ": "C",
             "\n2. Which planet in milky way is the biggest? ": "B",
             "\n3. Who lives at number 4 private drive? ": "C",
             "\n4. What is the smallest breed dog?": "A",
             "\n5. What is the hardest substance in your body?": "B"
             }


# ---------

def display_score(score, list_user_answer):
    print("\n-----------")
    print("Result")
    print("------------")
    print("Your answer: ", end=" ")  # end=" " - output in one line / no new line
    for i in list_user_answer:
        print(i, end=" ")
    print("\nCorrect answer: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    score = int(score / len(questions) * 100)
    print("\nScore: " + str(score) + '%')


# ---------

def play_again():
    response = input("\nWould you like to play again? (yes/no)").lower()  # change user input to lower case
    if response == "yes":
        return True
    elif response == "no":
        return False
    else:
        print("[ Invalid response ]")


options = [
    ["A. 5", "B. 4", "C. 3"],
    ["A. Mars", "B. Jupiter", "C. Saturn"],
    ["A. Jack Rabbit", "B. Peter pan", "C. Harry potter"],
    ["A. The chihuahua", "B. German shepherd", "C. Siberian husky"],
    ["A. Ribs", "B. Tooth enamel", "C. Tongue"]
]

start_game()
