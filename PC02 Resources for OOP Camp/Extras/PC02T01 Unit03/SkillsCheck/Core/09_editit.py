# After the question is shown to the user, show the three possible answers in the 'these_answers' variable
# - It is a list containing three string values for the three possible answers
# - Loop through that list and output each answer on its own line
# - Add a tab before each line, followed by a number (from 1 to 3)
# - For example:
#   1. Answer 1
#   2. Answer 2
#   3. Answer 3
questions = ["What is a programming language?", "What is a variable?"]
possible_answers = [
    ["A way of creating a computer", "A language we use to create programs", "An IDE that can help create programs"],
    ["A statement that repeats code", "A statement that is run if a condition is true", "A location to store data"]
]
answers = [1, 2]
for index in range(len(questions)):
    print(f"Question {index + 1}: {questions[index]}")

    # SHOW POSSIBLE ANSWERS HERE
    these_answers = possible_answers[index]
    
    choice = int(input("Answer (1, 2, 3): ")) - 1
    if answers[index] == choice:
        print("Good job!")
    else:
        print(f"Unlucky, the answer was {possible_answers[index][answers[index]]}")
